import json
import logging
import time
from pathlib import Path

from .base import AnalysisResult, BaseAnalyzer, Bug
from .patterns import pattern_hints, validate_severity
from .. import config as _cfg
from ..config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL, MAX_AI_CHUNK_LINES
from ..config import AI_CHUNK_OVERLAP, AI_BACKOFF_BASE_S, AI_BACKOFF_MAX_RETRIES

SYSTEM_PROMPT_GENERIC = (
    "You are a senior security engineer and code auditor. Analyze source code for "
    "real bugs and security vulnerabilities. Output a findings JSON array, or [] if "
    "nothing is wrong."
)

SYSTEM_PROMPT_SOLIDITY = (
    "You analyze Solidity smart contracts for real security vulnerabilities. "
    "Output a findings JSON array, or [] if nothing is wrong."
)

AUDIT_PROMPT_SOLIDITY = """You find real security vulnerabilities in Solidity smart contracts. Only report concrete loss-of-funds or broken-invariant bugs with a traceable exploit. Return findings as a JSON array.

Example 1:
```solidity
function withdrawAll() external {
    uint256 bal = address(this).balance;
    (bool ok, ) = msg.sender.call{value: bal}("");
    require(ok, "fail");
    deposits[msg.sender] = 0;
}
```
Response:
[{"line": 2, "severity": "high", "title": "Full-balance sweep drains all pooled funds", "category": "accounting", "root_cause": "withdrawAll sends the entire contract balance instead of the caller's own deposit", "exploit_path": "any depositor calls withdrawAll and receives all funds parked in the contract, including other users' deposits", "impact": "complete drain of pooled ETH", "fix": "send only deposits[msg.sender] and subtract it before transfer", "confidence": 0.9, "in_scope": true}]

RULES:
- A function with a nonReentrant modifier is NOT a reentrancy report by itself. Only report reentrancy if you can show a concrete extra extraction of value enabled by stale state inside a callback.
- Do NOT report class-level or generic issues ("Potential X", "no check for Y"). Every High must contain a concrete attacker path ending in measurable loss.
- If the only concern is a missing check with no demonstrated loss, report nothing for that item.

Now analyse the contract below. Return a JSON array of findings, or [] if nothing is wrong.

--- {file_relpath} ---
```solidity
{code}
```
FINDINGS JSON:
"""

AUDIT_PROMPT_GENERIC = """You find real bugs and security vulnerabilities in {language} source code. Report only concrete, demonstrable issues with a clear failure or attack scenario — not style nits or generic "potential" concerns. Return findings as a JSON array.

Each finding: {{"line": <int>, "severity": "critical"|"high"|"medium"|"low"|"info", "title": "...", "category": "...", "root_cause": "...", "exploit_path": "concrete steps an attacker or user takes to trigger it", "impact": "what breaks / is lost", "fix": "how to fix", "confidence": 0.0-1.0, "in_scope": true}}

Focus on:
- Security: injection (SQL/command/code), auth bypass, secrets handling, unsafe deserialization, path traversal, SSRF, XSS.
- Correctness: unhandled errors, race conditions, null/None dereference, resource leaks, off-by-one, integer overflow, logic errors that corrupt data or crash.

RULES:
- Do NOT report style, naming, formatting, or documentation issues.
- Do NOT report generic issues ("could throw", "no validation"). Every High/Critical must describe a concrete trigger and its consequence.
- If the code is fine, return [].

Now analyse the file below. Return a JSON array of findings, or [] if nothing is wrong.

--- {file_relpath} ---
```{lang_tag}
{code}
```
FINDINGS JSON:
"""

RETRY_PROMPT_SOLIDITY = """Your previous analysis returned no findings. Find real vulnerabilities in this Solidity contract and return a JSON array, or [] if nothing is wrong.

{hints}

--- {file_relpath} ---
```solidity
{code}
```
FINDINGS JSON:
"""

RETRY_PROMPT_GENERIC = """Your previous analysis returned no findings. Re-check this {language} file carefully for real bugs (security, correctness, error handling) and return a JSON array, or [] if genuinely nothing is wrong.

{hints}

--- {file_relpath} ---
```{lang_tag}
{code}
```
FINDINGS JSON:
"""

VERIFY_PROMPT = """You are a security audit validator. A rule-based analyzer flagged a candidate issue in a {language} file. Inspect the code context and decide whether it is a REAL exploitable/reproducible bug.

CANDIDATE:
- file: {file_relpath}
- line: {line}
- severity: {severity}
- title: {title}
- description: {description}

Reason about whether an attacker or user can actually trigger the failure. Do NOT confirm class-level or theoretical issues; require a concrete trigger path.

Respond with exactly one JSON object:
{{"verdict": "confirmed" | "rejected" | "downgrade", "exploit_path": "concrete trigger steps", "impact": "what is lost/broken", "fix": "how to fix", "confidence": 0.0-1.0, "actual_severity": "high" | "medium" | "low"}}

Rules:
- verdict "confirmed": real bug. Provide exploit_path.
- verdict "downgrade": minor/theoretical. Set actual_severity to medium or low.
- verdict "rejected": not a bug. Explain in one line as fix.

--- {file_relpath} (context) ---
```{lang_tag}
{context}
```
VERDICT JSON:
"""

# Languages that get a specialized prompt; everything else falls back to generic.
_SPECIAL_PROMPTS = {"solidity"}

# Markers per language for the context header (enclosing function/class/etc.)
_HEADER_MARKERS = {
    "solidity": ("contract ", "library ", "interface ", "function ", "modifier ", "abstract contract "),
    "python": ("def ", "class ", "async def "),
    "javascript": ("function ", "class ", "const ", "export ", "async function "),
    "typescript": ("function ", "class ", "interface ", "const ", "export ", "async function "),
    "go": ("func ", "type ", "package "),
    "java": ("class ", "interface ", "public ", "private ", "protected ", "void "),
    "rust": ("fn ", "impl ", "struct ", "enum ", "trait ", "pub "),
}
_DEFAULT_MARKERS = ("def ", "class ", "function ", "func ", "fn ")

# Lines of surrounding structure injected above each chunk.
_MAX_CONTEXT_LINES = 40

# Hard cap on AI error entries appended to result.errors.
_MAX_ERRORS_CAP = 100

logger = logging.getLogger(__name__)


def _is_solidity(language: str) -> bool:
    return language in _SPECIAL_PROMPTS


class AIAnalyzer(BaseAnalyzer):
    name = "ai"

    def __init__(self):
        self.client = None
        if OPENAI_API_KEY:
            try:
                from openai import OpenAI
                kwargs = {"api_key": OPENAI_API_KEY}
                if OPENAI_BASE_URL:
                    kwargs["base_url"] = OPENAI_BASE_URL
                self.client = OpenAI(**kwargs)
            except ImportError:
                pass
        self._project_contracts = []
        self._errors = []
        self._last_error = ""

    def analyze(self, files: list) -> AnalysisResult:
        result = AnalysisResult()
        self._errors = result.errors
        if not self.client:
            result.errors.append(
                "OpenAI client not available. Set OPENAI_API_KEY environment variable "
                "and install openai package: pip install openai"
            )
            return result

        hints = pattern_hints(compact=True)
        # Analyze every supported language, not only Solidity.
        target_files = [f for f in files if f.language]
        self._project_contracts = [str(f.relative_path) for f in target_files]

        for f in target_files:
            self._analyze_file(f, result, hints)

        result.files_analyzed = len(target_files)
        return result

    def _analyze_file(self, f, result: AnalysisResult, hints: str):
        lines = f.content.split("\n")
        chunks = _split_into_chunks(lines, MAX_AI_CHUNK_LINES, overlap=AI_CHUNK_OVERLAP)

        seen = set()
        for chunk_start, chunk_lines in chunks:
            code = "\n".join(chunk_lines)
            if not code.strip():
                continue

            header = self._build_context_header(lines, chunk_start, len(chunk_lines), f.language)
            body = header + "\n" + code

            prompt = _render(_select_audit_prompt(f.language), body, hints,
                             str(f.relative_path), f.language)
            bugs = self._call_llm(prompt, f, chunk_start)
            if not bugs:
                retry_prompt = _render(_select_retry_prompt(f.language), body, hints,
                                       str(f.relative_path), f.language)
                bugs = self._call_llm(retry_prompt, f, chunk_start)

            for b in bugs:
                b.severity = validate_severity(b.severity, b.description, b.title)
                key = (b.file, b.line, b.title)
                if key in seen:
                    continue
                seen.add(key)
                result.bugs.append(b)

            time.sleep(0.2)

    # ------------------------------------------------------------------
    # AI verification of rule-detected candidates (hybrid: rules + AI).
    # ------------------------------------------------------------------
    def verify_candidates(self, candidates: list, files: list, errors=None) -> list[Bug]:
        if not candidates:
            return []
        if not self.client:
            return candidates
        if errors is None:
            errors = self._errors
        self._errors = errors

        import os as _os
        verify_delay = float(_os.environ.get("BH_VERIFY_DELAY", "1.0"))
        by_path = {str(f.relative_path): f for f in files}
        result = []
        for cand in candidates:
            f = by_path.get(str(cand.file))
            if f is None:
                result.append(cand)
                continue
            context = self._context_around(f.content.split("\n"), cand.line)
            prompt = (
                VERIFY_PROMPT
                .replace("{language}", f.language or "source")
                .replace("{lang_tag}", f.language or "")
                .replace("{file_relpath}", str(cand.file))
                .replace("{line}", str(cand.line))
                .replace("{severity}", cand.severity)
                .replace("{title}", cand.title)
                .replace("{description}", (cand.description or "")[:600])
                .replace("{context}", context)
            )
            verdict = self._call_verify(prompt, f.language)
            if verdict is None:
                result.append(cand)
                continue
            v = verdict.get("verdict", "").lower()
            if v == "confirmed":
                expl = verdict.get("exploit_path", "")
                if expl and expl.lower() not in ("none", "n/a"):
                    desc = cand.description
                    if "EXPLOIT:" not in desc:
                        desc = desc + "\nEXPLOIT: " + expl
                    cand.description = desc
                sev = str(verdict.get("actual_severity", cand.severity))
                if sev in ("critical", "high", "medium", "low"):
                    cand.severity = sev
                conf = verdict.get("confidence")
                if isinstance(conf, (int, float)):
                    cand.confidence = float(conf)
                result.append(cand)
            elif v == "downgrade":
                sev = str(verdict.get("actual_severity", "low"))
                if sev in ("medium", "low", "info"):
                    cand.severity = sev
                expl = verdict.get("exploit_path", "")
                if expl and "EXPLOIT:" not in cand.description:
                    cand.description = cand.description + "\nEXPLOIT: " + expl
                result.append(cand)
            else:  # rejected
                fix = verdict.get("fix", "")
                cand.severity = "info"
                cand.description = (cand.description or "") + "\n[AI REJECTED] " + fix
                result.append(cand)
            time.sleep(verify_delay)
        return result

    @staticmethod
    def _context_around(lines: list[str], line_no: int, ctx: int = 30) -> str:
        start = max(0, line_no - 1 - ctx)
        end = min(len(lines), line_no - 1 + ctx + 1)
        out = []
        for i in range(start, end):
            marker = ">>>" if i == line_no - 1 else "   "
            out.append(f"{marker} {i + 1:4d} | {lines[i]}")
        return "\n".join(out)

    def _call_verify(self, prompt: str, language: str = "") -> dict:
        label = "verify"
        messages = [
            {"role": "system", "content": _select_system_prompt(language)},
            {"role": "user", "content": prompt},
        ]
        try:
            response = self._chat(messages, label=label, max_tokens=2048)
            if response is None:
                self._record_error(f"AI verify call failed ({self._last_error}) — candidate kept as-is")
                return {}
            text = response.choices[0].message.content.strip()
            return _extract_single_json(text) or {}
        except Exception as e:  # noqa: BLE001
            self._record_error(f"AI verify call error: {e}")
            return {}

    def _record_error(self, message: str, *, warn: bool = False):
        logger.warning(message) if warn else logger.error(message)
        errs = self._errors
        if errs is not None:
            if len(errs) >= _MAX_ERRORS_CAP:
                if errs[-1] != f"... ({_MAX_ERRORS_CAP} errors) truncated, see logs":
                    errs.append(f"... ({_MAX_ERRORS_CAP} errors) truncated, see logs")
                return
            errs.append(f"[AI] {message}")

    def _chat(self, messages: list, *, label: str = "", max_tokens: int = 4096) -> object:
        """Single completions call with exponential backoff retries on
        transient failures (429, connection reset, timeouts)."""
        delay = AI_BACKOFF_BASE_S
        last_exc = None
        for attempt in range(AI_BACKOFF_MAX_RETRIES + 1):
            try:
                return self.client.chat.completions.create(
                    model=_cfg.OPENAI_MODEL,
                    messages=messages,
                    temperature=0.1,
                    max_tokens=max_tokens,
                )
            except Exception as e:  # noqa: BLE001
                last_exc = e
                msg = str(e).lower()
                status = getattr(e, "status_code", None)
                if status is None and hasattr(e, "response"):
                    try:
                        status = e.response.status_code
                    except Exception:
                        status = None
                status = getattr(getattr(e, "status_code", None), "value", None)
                if status is None and hasattr(e, "response"):
                    try:
                        status = e.response.status_code
                    except Exception:
                        status = None
                transient = (
                    status in (429, 500, 502, 503, 504)
                    or "rate limit" in msg
                    or "internal" in msg
                    or "too many requests" in msg
                    or "connection" in msg
                    or "timeout" in msg
                    or "temporarily unavailable" in msg
                )
                if attempt < AI_BACKOFF_MAX_RETRIES and transient:
                    self._record_error(
                        f"AI {label.strip()} rate-limit/transient error (attempt {attempt + 1}/{AI_BACKOFF_MAX_RETRIES + 1}): {e} — retrying in {delay:.1f}s",
                        warn=True,
                    )
                    time.sleep(delay)
                    delay *= 2
                    continue
                break
        self._last_error = f"{type(last_exc).__name__}: {last_exc}"
        logger.error("AI %s call failed after retries: %s", label or "llm", self._last_error)
        return None

    def _build_context_header(self, lines: list[str], chunk_start: int, chunk_len: int,
                              language: str = "solidity") -> str:
        """Inline enclosing function/class structure above the chunk."""
        markers = _HEADER_MARKERS.get(language, _DEFAULT_MARKERS)
        header_lines = []
        seen = set()
        scan_start = max(0, chunk_start - _MAX_CONTEXT_LINES)
        for i in range(scan_start, chunk_start + chunk_len):
            stripped = lines[i].strip()
            if not stripped:
                continue
            if any(stripped.startswith(k) for k in markers):
                key = stripped[:60]
                if key in seen:
                    continue
                seen.add(key)
                header_lines.append(f"// {i + 1}: {stripped[:80]}")
        return "\n".join(header_lines)

    def _call_llm(self, prompt: str, f, chunk_start: int) -> list[Bug]:
        try:
            response = self._chat(
                [
                    {"role": "system", "content": _select_system_prompt(f.language)},
                    {"role": "user", "content": prompt},
                ],
                label=f"audit {f.relative_path}:{chunk_start + 1}",
            )
            if response is None:
                return []
            text = response.choices[0].message.content.strip()
        except Exception as e:  # noqa: BLE001
            self._record_error(f"AI audit call error in {f.relative_path}:{chunk_start + 1}: {e}")
            return []

        try:
            issues = _extract_json_issues(text)
            if not issues:
                return []

            bugs = []
            for issue in issues:
                if not isinstance(issue, dict):
                    continue
                line_num = issue.get("line", 1)
                if isinstance(line_num, int) and line_num > 0:
                    line_num += chunk_start
                else:
                    line_num = 1 + chunk_start

                severity = issue.get("severity", "medium")
                if severity not in ("critical", "high", "medium", "low", "info"):
                    severity = "medium"

                in_scope = issue.get("in_scope", True)
                exploit_path = issue.get("exploit_path", "")
                if not in_scope:
                    if severity in ("critical", "high", "medium"):
                        severity = "low"
                elif in_scope and severity in ("critical", "high"):
                    if not exploit_path or exploit_path.strip().lower() in ("none", "n/a", "requires trusted role"):
                        severity = "medium"

                snippet = _get_snippet(f.content.split("\n"), line_num - 1, chunk_start)

                desc_lines = [issue.get("root_cause", "") or issue.get("description", "")]
                if exploit_path:
                    desc_lines.append("EXPLOIT: " + exploit_path)
                if issue.get("impact"):
                    desc_lines.append("IMPACT: " + str(issue["impact"]))
                description = "\n".join(x for x in desc_lines if x)

                bug = Bug(
                    file=str(f.relative_path),
                    line=line_num,
                    column=0,
                    severity=severity,
                    category=issue.get("category", "logic"),
                    title=issue.get("title", "AI-detected Issue"),
                    description=description,
                    suggestion=issue.get("fix", ""),
                    code_snippet=snippet,
                    analyzer="ai",
                    confidence=float(issue.get("confidence", 0.6)),
                )
                bugs.append(bug)

            return bugs
        except Exception as e:  # noqa: BLE001
            self._record_error(f"AI result parsing error in {f.relative_path}:{chunk_start + 1}: {e}")
            return []


def _select_system_prompt(language: str) -> str:
    return SYSTEM_PROMPT_SOLIDITY if _is_solidity(language) else SYSTEM_PROMPT_GENERIC


def _select_audit_prompt(language: str) -> str:
    return AUDIT_PROMPT_SOLIDITY if _is_solidity(language) else AUDIT_PROMPT_GENERIC


def _select_retry_prompt(language: str) -> str:
    return RETRY_PROMPT_SOLIDITY if _is_solidity(language) else RETRY_PROMPT_GENERIC


def dictlist(data):
    return [d for d in data if isinstance(d, dict)]


def _render(template: str, code: str, hints: str, file_relpath: str, language: str = "") -> str:
    """Render a prompt template without .format() so literal { } in code
    examples are preserved."""
    return (
        template
        .replace("{hints}", hints)
        .replace("{file_relpath}", file_relpath)
        .replace("{language}", language or "source")
        .replace("{lang_tag}", language or "")
        .replace("{code}", code)
    )


def _strip_code_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        first_newline = text.index("\n") if "\n" in text else len(text)
        text = text[first_newline + 1:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def _extract_json_issues(text: str) -> list:
    """Robustly extract a list of finding dicts from a model response."""
    text = _strip_code_fences(text)
    if not text:
        return []

    try:
        data = json.loads(text)
        if isinstance(data, list):
            return dictlist(data)
        if isinstance(data, dict):
            for key in ("findings", "issues", "results", "bugs"):
                val = data.get(key)
                if isinstance(val, list):
                    return dictlist(val)
            return []
    except (json.JSONDecodeError, ValueError):
        pass

    start = text.find("[")
    while start != -1:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    candidate = text[start:i + 1]
                    try:
                        data = json.loads(candidate)
                        if isinstance(data, list):
                            return dictlist(data)
                    except (json.JSONDecodeError, ValueError):
                        pass
                    break
        start = text.find("[", start + 1)

    try:
        data = json.loads(text)
        if isinstance(data, dict):
            for key in ("response", "result", "content"):
                val = data.get(key)
                if isinstance(val, str):
                    stripped = _strip_code_fences(val)
                    inner = json.loads(stripped)
                    if isinstance(inner, list):
                        return dictlist(inner)
    except (json.JSONDecodeError, ValueError):
        pass

    return []


def _extract_single_json(text: str) -> dict:
    """Extract a single JSON object from a model response (for verify_verdict)."""
    text = _strip_code_fences(text)
    if not text:
        return {}
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except (json.JSONDecodeError, ValueError):
        pass
    start = text.find("{")
    while start != -1:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    candidate = text[start:i + 1]
                    try:
                        data = json.loads(candidate)
                        if isinstance(data, dict):
                            return data
                    except (json.JSONDecodeError, ValueError):
                        pass
                    break
        start = text.find("{", start + 1)
    return {}


def _split_into_chunks(lines: list[str], max_lines: int, overlap: int = 0) -> list[tuple[int, list[str]]]:
    if overlap < 0:
        overlap = 0
    overlap = min(overlap, max_lines - 1)
    chunks = []
    step = max_lines - overlap
    if step <= 0:
        step = 1
    i = 0
    while i < len(lines):
        chunks.append((i, lines[i:i + max_lines]))
        if i + max_lines >= len(lines):
            break
        i += step
    return chunks


def _get_snippet(lines: list[str], index: int, offset: int = 0, context: int = 2) -> str:
    start = max(0, index - context)
    end = min(len(lines), index + context + 1)
    snippet_lines = []
    for i in range(start, end):
        marker = ">>>" if i == index else "   "
        snippet_lines.append(f"{marker} {i + 1:4d} | {lines[i]}")
    return "\n".join(snippet_lines)
