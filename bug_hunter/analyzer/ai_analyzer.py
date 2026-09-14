import json
import logging
import time
from pathlib import Path

from analyzer.base import AnalysisResult, BaseAnalyzer, Bug
from analyzer.patterns import pattern_hints, validate_severity
from config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL, MAX_AI_CHUNK_LINES
from config import AI_CHUNK_OVERLAP, AI_BACKOFF_BASE_S, AI_BACKOFF_MAX_RETRIES
import config as _cfg

SYSTEM_PROMPT = """You analyze Solidity smart contracts for real security vulnerabilities. Output a findings JSON array, or [] if nothing is wrong."""

AUDIT_PROMPT = """You find real security vulnerabilities in Solidity smart contracts. Only report concrete loss-of-funds or broken-invariant bugs with a traceable exploit. Return findings as a JSON array.

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

Example 2:
```solidity
function refund() external {
    if (address(this).balance > 0) {
        (bool ok, ) = msg.sender.call{value: address(this).balance}("");
        require(ok, "fail");
    }
}
```
Response:
[{"line": 3, "severity": "high", "title": "Refund-all sends whole balance to caller", "category": "accounting", "root_cause": "refund sends address(this).balance instead of the caller's own entitlement", "exploit_path": "anyone calls refund and sweeps all ETH parked in the contract", "impact": "contract drained entirely", "fix": "pay only the caller's tracked entitlement", "confidence": 0.9, "in_scope": true}]

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

RETRY_PROMPT = """Your previous analysis returned no findings. Find real vulnerabilities in this Solidity contract and return a JSON array, or [] if nothing is wrong. Follow the same format as the two examples below.

Example:
```solidity
function withdrawAll() external {
    uint256 bal = address(this).balance;
    (bool ok, ) = msg.sender.call{value: bal}("");
    require(ok, "fail");
    deposits[msg.sender] = 0;
}
```
Response:
[{"line": 2, "severity": "high", "title": "Full-balance sweep drains all pooled funds", "category": "accounting", "root_cause": "withdrawAll sends the entire contract balance instead of the caller's own deposit", "exploit_path": "any depositor calls withdrawAll and receives all funds parked in the contract", "impact": "complete drain of pooled ETH", "fix": "pay only the caller's deposit", "confidence": 0.9, "in_scope": true}]

{hints}

--- {file_relpath} ---
```solidity
{code}
```
FINDINGS JSON:
"""

VERIFY_PROMPT = """You are a smart-contract audit validator. A rule-based analyzer flagged a candidate issue in a Solidity file. Inspect the code context and decide whether it is a REAL exploitable vulnerability.

CANDIDATE:
- file: {file_relpath}
- line: {line}
- severity: {severity}
- title: {title}
- description: {description}

The context below shows the source around the flagged line. Reason about whether an attacker can actually cause loss of funds or a broken invariant. Do NOT confirm class-level or theoretical issues; require a concrete attacker path.

Respond with exactly one JSON object:
{{"verdict": "confirmed" | "rejected" | "downgrade", "exploit_path": "concrete attacker steps", "impact": "what is lost", "fix": "how to fix", "confidence": 0.0-1.0, "actual_severity": "high" | "medium" | "low"}}

Rules:
- verdict "confirmed": real, exploitable bug. Provide exploit_path.
- verdict "downgrade": minor/theoretical/requires-trusted-role. Set actual_severity to medium or low.
- verdict "rejected": not a bug. Explain in one line as fix.

--- {file_relpath} (context) ---
```solidity
{context}
```
VERDICT JSON:
"""

# Lines of surrounding structure injected above each chunk so the model sees the
# enclosing function/contract even when a chunk is mid-file.
_MAX_CONTEXT_LINES = 40

# Hard cap on AI error entries appended to result.errors so huge scans can't
# flood the report. The tail is replaced by a truncation note.
_MAX_ERRORS_CAP = 100

logger = logging.getLogger(__name__)


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
        sol_files = [f for f in files if f.language == "solidity"]
        self._project_contracts = [str(f.relative_path) for f in sol_files]

        for f in sol_files:
            self._analyze_file(f, result, hints)

        result.files_analyzed = len(sol_files)
        return result

    def _analyze_file(self, f, result: AnalysisResult, hints: str):
        lines = f.content.split("\n")
        chunks = _split_into_chunks(lines, MAX_AI_CHUNK_LINES, overlap=AI_CHUNK_OVERLAP)

        seen = set()
        for chunk_start, chunk_lines in chunks:
            code = "\n".join(chunk_lines)
            if not code.strip():
                continue

            actual_start = chunk_start + 1
            actual_end = chunk_start + len(chunk_lines)

            header = self._build_context_header(lines, chunk_start, len(chunk_lines))

            prompt = _render(AUDIT_PROMPT, header + "\n" + code, hints, str(f.relative_path))

            bugs = self._call_llm(prompt, f, chunk_start)
            if not bugs:
                retry_prompt = _render(RETRY_PROMPT, header + "\n" + code, hints, str(f.relative_path))
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
    # Each candidate gets the file context around its line; the model
    # decides confirmed / downgrade / rejected and writes exploit_path.
    # ------------------------------------------------------------------
    def verify_candidates(self, candidates: list, files: list, errors=None) -> list[Bug]:
        if not candidates:
            return []
        if not self.client:
            return candidates
        if errors is None:
            errors = self._errors
        self._errors = errors

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
                .replace("{file_relpath}", str(cand.file))
                .replace("{line}", str(cand.line))
                .replace("{severity}", cand.severity)
                .replace("{title}", cand.title)
                .replace("{description}", (cand.description or "")[:600])
                .replace("{context}", context)
            )
            verdict = self._call_verify(prompt)
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
            time.sleep(0.3)
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

    def _call_verify(self, prompt: str) -> dict:
        label = "verify"
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]
        try:
            response = self._chat(messages, label=label, max_tokens=2048)
            if response is None:
                self._record_error(f"AI verify call failed ({self._last_error}) — candidate kept as-is")
                return {}
            text = response.choices[0].message.content.strip()
            return _extract_single_json(text) or {}
        except Exception as e:  # noqa: BLE001 - logged via _record_error below
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
        transient failures (429 rate limit, connection reset, timeouts).

        Returns the response object or None if every attempt failed and keeps
        the last error in self._last_error for the caller to report.
        """
        base_delay = AI_BACKOFF_BASE_S
        max_retries = AI_BACKOFF_MAX_RETRIES
        delay = base_delay
        last_exc = None
        for attempt in range(max_retries + 1):
            try:
                return self.client.chat.completions.create(
                    model=_cfg.OPENAI_MODEL,
                    messages=messages,
                    temperature=0.1,
                    max_tokens=max_tokens,
                )
            except Exception as e:  # noqa: BLE001 - normalized below for retry decision
                last_exc = e
                msg = str(e).lower()
                status = getattr(getattr(e, "status_code", None), "value", None)
                if status is None and hasattr(e, "response"):
                    try:
                        status = e.response.status_code
                    except Exception:
                        status = None
                transient = (
                    status == 429
                    or "rate limit" in msg
                    or "too many requests" in msg
                    or "connection" in msg
                    or "timeout" in msg
                    or "temporarily unavailable" in msg
                )
                if attempt < max_retries and transient:
                    self._record_error(
                        f"AI {label.strip()} rate-limit/transient error (attempt {attempt + 1}/{max_retries + 1}): {e} — retrying in {delay:.1f}s",
                        warn=True,
                    )
                    time.sleep(delay)
                    delay *= 2
                    continue
                break
        self._last_error = f"{type(last_exc).__name__}: {last_exc}"
        logger.error("AI %s call failed after retries: %s", label or "llm", self._last_error)
        return None

    def _build_context_header(self, lines: list[str], chunk_start: int, chunk_len: int) -> str:
        """Inline contract/function structure above the chunk so the model sees
        the security-relevant skeleton even when the chunk is mid-file."""
        header_lines = []
        seen = set()
        # scan backwards up to _MAX_CONTEXT_LINES for the enclosing struct/func of chunk start
        scan_start = max(0, chunk_start - _MAX_CONTEXT_LINES)
        for i in range(scan_start, chunk_start + chunk_len):
            stripped = lines[i].strip()
            if not stripped:
                continue
            if any(stripped.startswith(k) for k in ("contract ", "library ", "interface ", "function ", "modifier ", "abstract contract ")):
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
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                label=f"audit {f.relative_path}:{chunk_start + 1}",
            )
            if response is None:
                return []
            text = response.choices[0].message.content.strip()
        except Exception as e:  # noqa: BLE001 - logged below
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
        except Exception as e:  # noqa: BLE001 - logged below
            self._record_error(f"AI result parsing error in {f.relative_path}:{chunk_start + 1}: {e}")
            return []


def dictlist(data):
    return [d for d in data if isinstance(d, dict)]


def _render(template: str, code: str, hints: str, file_relpath: str) -> str:
    """Render a prompt template without .format() so literal { } in Solidity
    examples are preserved."""
    return (
        template
        .replace("{hints}", hints)
        .replace("{file_relpath}", file_relpath)
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
    """Robustly extract a list of finding dicts from a model response.

    1. Strip code fences.
    2. Find the outermost [...] array anywhere in the text.
    3. If the response is a JSON object (not an array), look for a
       'findings' / 'issues' / 'response' key and unwrap it.
    4. Fall back to finding the first balanced [...] block.
    """
    text = _strip_code_fences(text)
    if not text:
        return []

    # Try the whole text as JSON first.
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

    # Search for a balanced [...] array in the raw text.
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

    # Last resort: unwrap a { "response": "<json string>" } wrapper.
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
    """Split `lines` into chunks of up to `max_lines` lines with a `overlap`-line
    overlap between consecutive chunks (so a state-write / call pair spanning a
    chunk boundary is still seen together by the model)."""
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