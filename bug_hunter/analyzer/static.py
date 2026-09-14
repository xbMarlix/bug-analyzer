import re
from pathlib import Path

from .base import AnalysisResult, BaseAnalyzer, Bug


class StaticAnalyzer(BaseAnalyzer):
    name = "static"

    PATTERNS = [
        {
            "pattern": r"(?:execute|cursor\.execute)\s*\(\s*(?:f[\"']|.*\.format\(|.*%\s)",
            "category": "security",
            "title": "Possible SQL Injection",
            "description": "String interpolation used in SQL query. This may allow SQL injection attacks.",
            "suggestion": "Use parameterized queries instead of string formatting.",
            "severity": "critical",
            "languages": ["python", "javascript", "typescript", "java", "php", "ruby"],
        },
        {
            "pattern": r"innerHTML\s*=|document\.write\s*\(|\.html\s*\(",
            "category": "security",
            "title": "Possible XSS Vulnerability",
            "description": "Direct HTML injection detected. User-controlled data may be executed as HTML/JS.",
            "suggestion": "Sanitize input or use textContent/innerText instead of innerHTML.",
            "severity": "high",
            "languages": ["javascript", "typescript"],
        },
        {
            "pattern": r"eval\s*\(|exec\s*\(|subprocess\.call\s*\(\s*f[\"']|os\.system\s*\(",
            "category": "security",
            "title": "Dangerous Code Execution",
            "description": "Dynamic code execution detected. This can lead to remote code execution vulnerabilities.",
            "suggestion": "Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.",
            "severity": "critical",
            "languages": ["python", "javascript", "typescript"],
        },
        {
            "pattern": r"except\s*:\s*$|except\s+Exception\s*:\s*$",
            "category": "error-handling",
            "title": "Bare Exception Handler",
            "description": "Catching all exceptions silently hides bugs and makes debugging nearly impossible.",
            "suggestion": "Catch specific exceptions and log them. Never use bare 'except:' without re-raising.",
            "severity": "medium",
            "languages": ["python"],
        },
        {
            "pattern": r"except\s+\w+.*:\s*\n\s*pass",
            "category": "error-handling",
            "title": "Swallowed Exception",
            "description": "Exception is caught but silently ignored. Errors will go unnoticed.",
            "suggestion": "At minimum, log the exception. Consider whether swallowing it is really necessary.",
            "severity": "high",
            "languages": ["python"],
        },
        {
            "pattern": r"catch\s*\(\s*\w*\s*\)\s*\{\s*\}",
            "category": "error-handling",
            "title": "Empty Catch Block",
            "description": "Empty catch block silently swallows errors.",
            "suggestion": "Handle the error or re-throw it. At minimum, log the error.",
            "severity": "high",
            "languages": ["javascript", "typescript", "java"],
        },
        {
            "pattern": r"=\s*(?:None|null|undefined)\s*(?:==|!=)\s*(?:None|null|undefined)",
            "category": "logic",
            "title": "Redundant None/null Comparison",
            "description": "Comparing a value to None/null using == instead of 'is' or proper null check.",
            "suggestion": "Use 'is None' in Python, or optional chaining (?.) in JS/TS.",
            "severity": "low",
            "languages": ["python"],
        },
        {
            "pattern": r"(?:password|secret|api_key|token|private_key)\s*=\s*[\"'][^\"']+[\"']",
            "category": "security",
            "title": "Hardcoded Secret",
            "description": "A secret or password appears to be hardcoded in source code.",
            "suggestion": "Use environment variables or a secrets manager instead of hardcoding.",
            "severity": "critical",
            "languages": ["python", "javascript", "typescript", "java", "go", "ruby", "php", "rust"],
        },
        {
            "pattern": r"SELECT\s+\*\s+FROM",
            "category": "performance",
            "title": "SELECT * Query",
            "description": "Using SELECT * retrieves all columns, which wastes bandwidth and breaks if schema changes.",
            "suggestion": "Select only the columns you need.",
            "severity": "medium",
            "languages": ["python", "javascript", "typescript", "java", "php", "ruby", "go"],
        },
        {
            "pattern": r"(?:while|for)\s*\(\s*true\s*\)|while\s+True\s*:",
            "category": "logic",
            "title": "Infinite Loop Risk",
            "description": "Detected an infinite loop construct. Ensure there is a proper exit condition.",
            "suggestion": "Verify the loop has a reachable break/return condition and a timeout.",
            "severity": "medium",
            "languages": ["python", "javascript", "typescript", "java", "go", "c", "cpp", "rust"],
        },
        {
            "pattern": r"===?\s*(?:true|false|null|undefined)\b",
            "category": "logic",
            "title": "Comparison with Boolean Literal",
            "description": "Direct comparison with true/false is usually redundant and may hide type coercion bugs.",
            "suggestion": "Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.",
            "severity": "low",
            "languages": ["javascript", "typescript"],
        },
        {
            "pattern": r"(?:TODO|FIXME|HACK|XXX|BUG)\b",
            "category": "code-quality",
            "title": "Unresolved TODO/FIXME",
            "description": "Developer left a note indicating unfinished or problematic code.",
            "suggestion": "Review and resolve the TODO/FIXME before deploying.",
            "severity": "info",
            "languages": ["python", "javascript", "typescript", "java", "go", "rust", "ruby", "php", "c", "cpp"],
        },
        {
            "pattern": r"threading\.Thread\s*\(|new\s+Thread\s*\(|Thread\.start\s*\(",
            "category": "concurrency",
            "title": "Manual Thread Management",
            "description": "Manual thread creation detected. This can cause race conditions and hard-to-debug issues.",
            "suggestion": "Consider using thread pools, asyncio, or concurrent.futures instead.",
            "severity": "medium",
            "languages": ["python", "java"],
        },
        {
            "pattern": r"\.close\(\)|defer\s+.*\.Close\(\)",
            "category": "resource-management",
            "title": "Resource Cleanup Without Context Manager",
            "description": "Resource is manually closed. If an exception occurs before close(), the resource leaks.",
            "suggestion": "Use context managers (with statement) or try-finally to guarantee cleanup.",
            "severity": "medium",
            "languages": ["python"],
        },
        {
            "pattern": r"time\.sleep\s*\(",
            "category": "code-quality",
            "title": "Hardcoded Sleep",
            "description": "Using sleep() in code can cause performance issues and race conditions.",
            "suggestion": "Use proper synchronization primitives, event loops, or polling with backoff.",
            "severity": "low",
            "languages": ["python"],
        },
        {
            "pattern": r"(?:\+\+\s*\w+|\w+\s*\+\+)\s*;",
            "category": "logic",
            "title": "Side-Effect in Condition",
            "description": "Pre/post increment used in a standalone statement may indicate logic confusion.",
            "suggestion": "Ensure increment is intentional and not a mistyped comparison (== vs =).",
            "severity": "low",
            "languages": ["javascript", "typescript", "java", "c", "cpp"],
        },
        {
            "pattern": r"assert\s+\w+\s*,\s*[\"'].*[\"']\s*$",
            "category": "error-handling",
            "title": "Assert Used for Validation",
            "description": "Asserts are stripped in optimized mode (-O). Never use them for input validation.",
            "suggestion": "Use proper if/raise or validation libraries for runtime checks.",
            "severity": "medium",
            "languages": ["python"],
        },
        {
            "pattern": r"mutable\s+default\s*=\s*\[|def\s+\w+\([^)]*=\s*\[\]|def\s+\w+\([^)]*=\s*\{\}",
            "category": "logic",
            "title": "Mutable Default Argument",
            "description": "Mutable default argument (list/dict) is shared across all calls. This causes state leakage.",
            "suggestion": "Use None as default and create the mutable object inside the function.",
            "severity": "high",
            "languages": ["python"],
        },
        {
            "pattern": r"\.call\.value\s*\(\s*[^)]*\)\{",
            "category": "security",
            "title": "Reentrancy Risk - Low-Level Call with Value",
            "description": "External call with value transfer. If state is not updated before the call, an attacker can reenter the contract.",
            "suggestion": "Use the checks-effects-interactions pattern: update state before external calls, or use a reentrancy guard.",
            "severity": "critical",
            "languages": ["solidity"],
        },
        {
            "pattern": r"(?:tx\.origin\s*[=!]=\s*msg\.sender|msg\.sender\s*[=!]=\s*tx\.origin|"
                       r"tx\.origin\s*[=!]=\s*\w+\s*[=!]=\s*\w+|require\s*\([^)]*tx\.origin|"
                       r"(?:if|require)\s*\([^)]*tx\.origin)",
            "category": "security",
            "title": "tx.origin For Authorization",
            "description": "Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.",
            "suggestion": "Use msg.sender instead of tx.origin for authorization checks.",
            "severity": "critical",
            "languages": ["solidity"],
        },
        {
            # block.timestamp is only dangerous when it feeds randomness / lottery /
            # cryptographic selection. Plain time-gating (ICO windows, vesting,
            # auction decay) is NOT a vulnerability — miners can only shift a few
            # seconds, which buys no economic edge for deterministic sales.
            # So we fire ONLY on randomness-y uses of the timestamp.
            "pattern": r"(?:block\.timestamp\s*(?:%|mod\b|/)|"
                       r"keccak256?\s*\([^)]*block\.timestamp[^;]*?(?:%|mod\b)|"
                       r"block\.timestamp\s*[+\-*/]\s*block\.(?:number|difficulty|prevrandao)|"
                       r"(?:seed|random|rand|nonce|lottery|winner)\w*\s*[=(].{0,40}block\.timestamp|"
                       r"block\.timestamp\s*[=:]\s*[^;]*%|"
                       r"(?:prng|rng|randomSeed|randomNumber)\b)",
            "category": "logic",
            "title": "block.timestamp Used for Randomness/Selection",
            "description": "block.timestamp feeds randomness, lottery, or winner-selection logic. Miners/validators can bias the timestamp a few seconds to tilt outcomes, or the value is predictable. This is an exploitable randomness source.",
            "suggestion": "Use a verifiable random function (Chainlink VRF, commit-reveal with a private seed) instead of block.timestamp/blockhash for randomness.",
            "severity": "high",
            "languages": ["solidity"],
        },
        {
            "pattern": r"(?:block\.number\b.*\bmod\b|blockhash\s*\(|block\.(?:number|difficulty|gaslimit|timestamp)\s*%\s*\d+|keccak256?\s*\([^)]*block\.(?:number|difficulty|blockhash))",
            "category": "logic",
            "title": "block.number/blockhash For Randomness",
            "description": "Using block.number/blockhash/difficulty as a randomness source is predictable and exploitable by miners or MEV searchers.",
            "suggestion": "Use Chainlink VRF or a commit-reveal scheme for randomness.",
            "severity": "high",
            "languages": ["solidity"],
        },
        {
            "pattern": r"delegatecall\b|callcode\b",
            "category": "security",
            "title": "Unsafe Delegatecall",
            "description": "delegatecall executes code in the caller's storage context. Contract state can be corrupted.",
            "suggestion": "If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.",
            "severity": "high",
            "languages": ["solidity"],
        },
        {
            "pattern": r"selfdestruct\b",
            "category": "security",
            "title": "Selfdestruct Used",
            "description": "selfdestruct sends all remaining ETH to a target and destroys the contract, potentially bricking funds.",
            "suggestion": "Avoid selfdestruct unless absolutely necessary and carefully reviewed.",
            "severity": "high",
            "languages": ["solidity"],
        },
        {
            "pattern": r"\.(?:transfer|send)\s*\(\s*[^,()]+\)",
            "category": "resource-management",
            "title": "Fixed-Gas Transfer",
            "description": "transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.",
            "suggestion": "Use .call{value: amount} with proper error handling (checks-effects-interactions).",
            "severity": "medium",
            "languages": ["solidity"],
        },
        {
            "pattern": r"require\s*\(\s*[^,)]*,\s*[\"'][^\"']*[\"']\s*\)",
            "category": "code-quality",
            "title": "UNCLEAR require Error Message",
            "description": "require() with a generic/empty revert message makes debugging harder.",
            "suggestion": "Use custom errors (Solidity 0.8.4+) with specific names for better error handling.",
            "severity": "low",
            "languages": ["solidity"],
        },
        {
            "pattern": r"pragma\s+solidity\s+\^?0\.[0-4]",
            "category": "syntax",
            "title": "Obsolete Solidity Version",
            "description": "Using an outdated Solidity compiler version that lacks safety improvements and bug fixes.",
            "suggestion": "Upgrade to Solidity 0.8.x which has built-in overflow/underflow checks.",
            "severity": "low",
            "languages": ["solidity"],
        },
        {
            "pattern": r"for\s*\(\s*.*i\s*[<>=]+\s*[^;]*;\s*i\+\+\)",
            "category": "performance",
            "title": "Unoptimized Loop",
            "description": "Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.",
            "suggestion": "Cache state variables in memory before the loop, and consider if the loop can be avoided.",
            "severity": "low",
            "languages": ["solidity"],
        },
        {
            "pattern": r"\.balance\s*>|\.balance\s*>=|\.balance\s*<",
            "category": "logic",
            "title": "Balance Comparison",
            "description": "Comparing contract balance to determine behavior can be exploited by forced ETH sends. Note: in admin-only withdraw paths this is usually benign.",
            "suggestion": "Track balances internally instead of relying on contract.balance.",
            "severity": "low",
            "languages": ["solidity"],
        },
        {
            "pattern": r"\.code\.length\s*==\s*0",
            "category": "code-quality",
            "title": "Address Is Contract Check",
            "description": ".code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.",
            "suggestion": "Consider upgrading to a better EOA detection or avoiding this check entirely.",
            "severity": "low",
            "languages": ["solidity"],
        },
    ]

    def __init__(self, extra_rules: list[dict] | None = None):
        self._compiled = []
        for p in self.PATTERNS:
            try:
                self._compiled.append((re.compile(p["pattern"], re.MULTILINE | re.IGNORECASE), p))
            except re.error:
                continue
        for rule in load_yaml_rules() + list(extra_rules or []):
            try:
                self._compiled.append((re.compile(rule["pattern"], re.MULTILINE | re.IGNORECASE), rule))
            except (re.error, KeyError):
                continue

    def analyze(self, files: list) -> AnalysisResult:
        result = AnalysisResult()
        for f in files:
            self._analyze_file(f, result)
        result.files_analyzed = len(files)
        return result

    def _analyze_file(self, f, result: AnalysisResult):
        lines = f.content.split("\n")
        for compiled_re, pattern_info in self._compiled:
            if f.language not in pattern_info["languages"]:
                continue
            for i, line in enumerate(lines, 1):
                m = compiled_re.search(line)
                if m and _in_comment(f.language, m, line):
                    m = None
                if m is not None:
                    snippet = _get_snippet(lines, i - 1)
                    bug = Bug(
                        file=str(f.relative_path),
                        line=i,
                        column=0,
                        severity=pattern_info["severity"],
                        category=pattern_info["category"],
                        title=pattern_info["title"],
                        description=pattern_info["description"],
                        suggestion=pattern_info["suggestion"],
                        code_snippet=snippet,
                        analyzer=self.name,
                        confidence=0.7,
                    )
                    result.add(bug)


_RULES_CACHE: list[dict] | None = None


def load_yaml_rules(rules_dir=None) -> list[dict]:
    """Load pattern rules from YAML files in bug_hunter/rules/.

    Each YAML file is a list of rules:
      - id, pattern (regex), severity, category, title, description, suggestion,
        languages (optional: derived from the filename, e.g. python.yaml -> python).
    """
    global _RULES_CACHE
    if _RULES_CACHE is not None and rules_dir is None:
        return _RULES_CACHE

    try:
        import yaml
    except ImportError:
        return []

    directory = Path(rules_dir) if rules_dir else Path(__file__).resolve().parent.parent / "rules"
    rules: list[dict] = []
    if not directory.is_dir():
        _RULES_CACHE = rules
        return rules

    for path in sorted(directory.glob("*.yaml")) + sorted(directory.glob("*.yml")):
        language = path.stem
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        for entry in data:
            if not isinstance(entry, dict) or "pattern" not in entry:
                continue
            rule = {
                "pattern": entry["pattern"],
                "category": entry.get("category", "security"),
                "title": entry.get("title", entry.get("id", "YAML rule")),
                "description": entry.get("description", ""),
                "suggestion": entry.get("suggestion", ""),
                "severity": entry.get("severity", "medium"),
                "languages": entry.get("languages") or [language],
            }
            rules.append(rule)

    if rules_dir is None:
        _RULES_CACHE = rules
    return rules


def _in_comment(language: str, m, line: str) -> bool:
    if language == "solidity":
        # whole-line comment: strip leading whitespace
        stripped = line.lstrip()
        if stripped.startswith("//") or stripped.startswith("*"):
            return True
        # trailing comment: find last // that precedes the match start
        pos = m.start()
        cidx = line.find("//")
        if cidx != -1 and cidx < pos:
            return True
    return False


def _get_snippet(lines: list[str], index: int, context: int = 2) -> str:
    start = max(0, index - context)
    end = min(len(lines), index + context + 1)
    snippet_lines = []
    for i in range(start, end):
        marker = ">>>" if i == index else "   "
        snippet_lines.append(f"{marker} {i + 1:4d} | {lines[i]}")
    return "\n".join(snippet_lines)
