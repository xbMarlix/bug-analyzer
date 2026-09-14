# BugHunter Report: bug_hunter

**Generated:** 2026-09-08 19:56:27
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\bug_hunter`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 13 |
| Total lines | 3,023 |
| Bugs found | 83 |
| !!! Critical | 1 |
| ! Medium | 1 |
| ~ Low | 3 |
| i Info | 78 |

### Languages Detected

- **python**: 12 files
- **html**: 1 files

## Security (1)

### [!!!] Dangerous Code Execution

- **File:** `analyzer\static.py:33`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      31 |             "title": "Dangerous Code Execution",
      32 |             "description": "Dynamic code execution detected. This can lead to remote code execution vulnerabilities.",
>>>   33 |             "suggestion": "Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.",
      34 |             "severity": "critical",
      35 |             "languages": ["python", "javascript", "typescript"],
```
</details>

---

## Error Handling (1)

### [!] Bare Exception Handler

- **File:** `analyzer\ai_analyzer.py:313`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Catching all exceptions silently hides bugs and makes debugging nearly impossible.

**Fix:** Catch specific exceptions and log them. Never use bare 'except:' without re-raising.

<details>
<summary>Code</summary>

```
     311 |                     try:
     312 |                         status = e.response.status_code
>>>  313 |                     except Exception:
     314 |                         status = None
     315 |                 transient = (
```
</details>

---

## Code Quality (81)

### [~] Hardcoded Sleep

- **File:** `analyzer\ai_analyzer.py:182`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     180 |                 result.bugs.append(b)
     181 | 
>>>  182 |             time.sleep(0.2)
     183 | 
     184 |     # ------------------------------------------------------------------
```
</details>

---

### [~] Hardcoded Sleep

- **File:** `analyzer\ai_analyzer.py:247`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     245 |                 cand.description = (cand.description or "") + "\n[AI REJECTED] " + fix
     246 |                 result.append(cand)
>>>  247 |             time.sleep(0.3)
     248 |         return result
     249 | 
```
</details>

---

### [~] Hardcoded Sleep

- **File:** `analyzer\ai_analyzer.py:328`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     326 |                         warn=True,
     327 |                     )
>>>  328 |                     time.sleep(delay)
     329 |                     delay *= 2
     330 |                     continue
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `main.py:21`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      19 | def main():
      20 |     parser = argparse.ArgumentParser(
>>>   21 |         description="BugHunter - AI-powered automatic bug finder",
      22 |         formatter_class=argparse.RawDescriptionHelpFormatter,
      23 |         epilog="""
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `main.py:52`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      50 | 
      51 |     print("=" * 60)
>>>   52 |     print("  BugHunter - AI-Powered Bug Finder")
      53 |     print("=" * 60)
      54 |     print()
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `main.py:147`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     145 |     sorted_bugs = result.sorted_bugs()
     146 |     sev_counts = {}
>>>  147 |     for bug in sorted_bugs:
     148 |         sev_counts[bug.severity] = sev_counts.get(bug.severity, 0) + 1
     149 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `main.py:148`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     146 |     sev_counts = {}
     147 |     for bug in sorted_bugs:
>>>  148 |         sev_counts[bug.severity] = sev_counts.get(bug.severity, 0) + 1
     149 | 
     150 |     print("=" * 60)
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:6`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       4 | from pathlib import Path
       5 | 
>>>    6 | from analyzer.base import AnalysisResult, BaseAnalyzer, Bug
       7 | from analyzer.patterns import pattern_hints, validate_severity
       8 | from config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL, MAX_AI_CHUNK_LINES
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:92`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      90 | 
      91 | Rules:
>>>   92 | - verdict "confirmed": real, exploitable bug. Provide exploit_path.
      93 | - verdict "downgrade": minor/theoretical/requires-trusted-role. Set actual_severity to medium or low.
      94 | - verdict "rejected": not a bug. Explain in one line as fix.
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:94`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      92 | - verdict "confirmed": real, exploitable bug. Provide exploit_path.
      93 | - verdict "downgrade": minor/theoretical/requires-trusted-role. Set actual_severity to medium or low.
>>>   94 | - verdict "rejected": not a bug. Explain in one line as fix.
      95 | 
      96 | --- {file_relpath} (context) ---
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:189`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     187 |     # decides confirmed / downgrade / rejected and writes exploit_path.
     188 |     # ------------------------------------------------------------------
>>>  189 |     def verify_candidates(self, candidates: list, files: list, errors=None) -> list[Bug]:
     190 |         if not candidates:
     191 |             return []
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:355`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     353 |         return "\n".join(header_lines)
     354 | 
>>>  355 |     def _call_llm(self, prompt: str, f, chunk_start: int) -> list[Bug]:
     356 |         try:
     357 |             response = self._chat(
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:408`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     406 |                 description = "\n".join(x for x in desc_lines if x)
     407 | 
>>>  408 |                 bug = Bug(
     409 |                     file=str(f.relative_path),
     410 |                     line=line_num,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:421`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     419 |                     confidence=float(issue.get("confidence", 0.6)),
     420 |                 )
>>>  421 |                 bugs.append(bug)
     422 | 
     423 |             return bugs
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:5`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       3 | from pathlib import Path
       4 | 
>>>    5 | from analyzer.base import AnalysisResult, BaseAnalyzer, Bug
       6 | 
       7 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:24`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      22 |         except SyntaxError as e:
      23 |             result.errors.append(f"Syntax error in {f.relative_path}: {e}")
>>>   24 |             result.add(Bug(
      25 |                 file=str(f.relative_path),
      26 |                 line=e.lineno or 1,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:57`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      55 |         return False
      56 | 
>>>   57 |     def _add_bug(self, node, severity, category, title, description, suggestion, confidence=0.8):
      58 |         line = getattr(node, "lineno", 1)
      59 |         col = getattr(node, "col_offset", 0)
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:61`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      59 |         col = getattr(node, "col_offset", 0)
      60 |         snippet = _get_snippet(self.f.content.split("\n"), line - 1)
>>>   61 |         self.result.add(Bug(
      62 |             file=str(self.f.relative_path),
      63 |             line=line,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:134`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     132 |     def visit_ExceptHandler(self, node):
     133 |         if node.type is None:
>>>  134 |             self._add_bug(
     135 |                 node, "high", "error-handling",
     136 |                 "Bare Except Clause",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:152`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     150 |         if isinstance(node.func, ast.Name) and node.func.id == "print":
     151 |             if not any(
>>>  152 |                 isinstance(p, ast.Constant) and "debug" in str(p.value).lower()
     153 |                 for p in node.args
     154 |             ):
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:155`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     153 |                 for p in node.args
     154 |             ):
>>>  155 |                 self._add_bug(
     156 |                     node, "info", "code-quality",
     157 |                     "Extraneous print() Call",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:158`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     156 |                     node, "info", "code-quality",
     157 |                     "Extraneous print() Call",
>>>  158 |                     "A bare 'print()' without a 'debug' marker was left in the code. "
     159 |                     "It may expose internal data in production or indicate unfinished work.",
     160 |                     "Remove debug prints or gate them behind a logger/config flag.",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:160`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     158 |                     "A bare 'print()' without a 'debug' marker was left in the code. "
     159 |                     "It may expose internal data in production or indicate unfinished work.",
>>>  160 |                     "Remove debug prints or gate them behind a logger/config flag.",
     161 |                     confidence=0.5,
     162 |                 )
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:167`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     165 |     def visit_Global(self, node):
     166 |         for name in node.names:
>>>  167 |             self._add_bug(
     168 |                 node, "medium", "code-quality",
     169 |                 "Use of global Statement",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:201`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     199 |             if name.startswith("_"):
     200 |                 continue
>>>  201 |             self._add_bug(
     202 |                 func_node, "low", "code-quality",
     203 |                 "Unused Variable",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:213`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     211 |             if isinstance(comparator, ast.Constant) and comparator.value is None:
     212 |                 if not isinstance(op, (ast.Is, ast.IsNot)):
>>>  213 |                     self._add_bug(
     214 |                         node, "low", "logic",
     215 |                         "Use 'is None' Instead of '== None'",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:230`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     228 |                     not isinstance(o, (ast.Is, ast.IsNot)) for o in node.ops
     229 |                 ):
>>>  230 |                     self._add_bug(
     231 |                         node, "low", "logic",
     232 |                         "Ambiguous Chained None Comparison",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:286`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     284 |                 # redundant upper bound: sibling tightens beyond current hi already
     285 |                 if arrow in ("<", "<=") and hi is not None and s_val <= hi:
>>>  286 |                     self._add_bug(
     287 |                         sibling, "low", "logic",
     288 |                         "Redundant Chained Comparison",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:295`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     293 |                     )
     294 |                 elif arrow in (">", ">=") and lo is not None and s_val >= lo:
>>>  295 |                     self._add_bug(
     296 |                         sibling, "low", "logic",
     297 |                         "Redundant Chained Comparison",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\base.py:5`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       3 | 
       4 | @dataclass
>>>    5 | class Bug:
       6 |     file: str
       7 |     line: int
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\base.py:21`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      19 | @dataclass
      20 | class AnalysisResult:
>>>   21 |     bugs: list[Bug] = field(default_factory=list)
      22 |     files_analyzed: int = 0
      23 |     errors: list[str] = field(default_factory=list)
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\base.py:25`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      23 |     errors: list[str] = field(default_factory=list)
      24 | 
>>>   25 |     def add(self, bug: Bug):
      26 |         self.bugs.append(bug)
      27 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\base.py:26`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      24 | 
      25 |     def add(self, bug: Bug):
>>>   26 |         self.bugs.append(bug)
      27 | 
      28 |     def merge(self, other: "AnalysisResult"):
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\base.py:33`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      31 |         self.errors.extend(other.errors)
      32 | 
>>>   33 |     def sorted_bugs(self, by: str = "severity") -> list[Bug]:
      34 |         from config import SEVERITY_ORDER
      35 |         return sorted(self.bugs, key=lambda b: SEVERITY_ORDER.get(b.severity, 99))
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\patterns.py:145`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     143 |     """
     144 |     if compact:
>>>  145 |         lines = ["HIGH-VALUE BUG CLASSES (map code to these):"]
     146 |         for p in KNOWN_HIGH_VALUE_PATTERNS:
     147 |             lines.append(
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\patterns.py:158`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     156 |         return "\n".join(lines)
     157 | 
>>>  158 |     lines = ["HIGH-VALUE BUG CLASSES THAT ACTUALLY PAY (learn these):"]
     159 |     for p in KNOWN_HIGH_VALUE_PATTERNS:
     160 |         lines.append(
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:2`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       1 | import re
>>>    2 | from analyzer.base import AnalysisResult, BaseAnalyzer, Bug
       3 | 
       4 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:251`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     249 |             sc.calls.append((line_no, call_kind))
     250 |             if call_kind in ("call", "delegatecall") and not self._call_result_captured(line):
>>>  251 |                 self._add_bug(
     252 |                     result, f, line_no, "medium", "security",
     253 |                     "Unchecked Low-Level Call Result",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:260`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     258 |             if call_kind == "call" and re.search(r"\.call\s*\{", line):
     259 |                 if sc.guard:
>>>  260 |                     self._add_bug(
     261 |                         result, f, line_no, "info", "security",
     262 |                         "Reentrancy Vector (External Call with Value, Guard Present)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:270`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     268 |                     )
     269 |                 else:
>>>  270 |                     self._add_bug(
     271 |                         result, f, line_no, "high", "security",
     272 |                         "Reentrancy Vector (External Call with Value)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:310`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     308 |         else:
     309 |             sev, conf, note = "medium", 0.4, ""
>>>  310 |         self._add_bug(
     311 |             result, f, line_no, sev, "logic",
     312 |             "State Change After External Call (CEI Violation)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:329`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     327 |             return
     328 |         if not sc.oracle_price_checked:
>>>  329 |             self._add_bug(
     330 |                 result, f, sc.oracle_read_line, "high", "oracle",
     331 |                 "Oracle Price Missing Positive Check",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:345`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     343 |             )
     344 |         elif not sc.oracle_fresh_checked:
>>>  345 |             self._add_bug(
     346 |                 result, f, sc.oracle_read_line, "medium", "oracle",
     347 |                 "Oracle Price Missing Staleness Check",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:408`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     406 |             if var in self._sweep_vars and self._current_func is not None:
     407 |                 snap_line, is_native = self._sweep_vars[var]
>>>  408 |                 self._add_sweep_bug(
     409 |                     result, f, line_no,
     410 |                     "high" if is_native else "high",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:433`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     431 |         lowered = line.lower()
     432 |         if "address(this).balance" in lowered or "balanceof(address(this))" in lowered:
>>>  433 |             self._add_sweep_bug(
     434 |                 result, f, line_no, "high",
     435 |                 "Full-Balance Sweep in Payout",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:446`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     444 |             )
     445 |         else:
>>>  446 |             self._add_sweep_bug(
     447 |                 result, f, line_no, "medium",
     448 |                 "Suspicious Full-Balance Payout",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:457`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     455 |             )
     456 | 
>>>  457 |     def _add_sweep_bug(self, result, f, line, sev, title, desc, sug, conf):
     458 |         self._add_bug(result, f, line, sev, "accounting", title, desc, sug, conf)
     459 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:458`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     456 | 
     457 |     def _add_sweep_bug(self, result, f, line, sev, title, desc, sug, conf):
>>>  458 |         self._add_bug(result, f, line, sev, "accounting", title, desc, sug, conf)
     459 | 
     460 |     # ------------------------------------------------------------------
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:461`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     459 | 
     460 |     # ------------------------------------------------------------------
>>>  461 |     def _add_bug(self, result, f, line, sev, category, title, desc, sug, conf):
     462 |         snippet = self._get_snippet(f.content.split("\n"), line - 1)
     463 |         result.add(Bug(
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:463`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     461 |     def _add_bug(self, result, f, line, sev, category, title, desc, sug, conf):
     462 |         snippet = self._get_snippet(f.content.split("\n"), line - 1)
>>>  463 |         result.add(Bug(
     464 |             file=str(f.relative_path),
     465 |             line=line,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:3`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       1 | import re
       2 | 
>>>    3 | from analyzer.base import AnalysisResult, BaseAnalyzer, Bug
       4 | 
       5 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:110`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     108 |         },
     109 |         {
>>>  110 |             "pattern": r"(?:TODO|FIXME|HACK|XXX|BUG)\b",
     111 |             "category": "code-quality",
     112 |             "title": "Unresolved TODO/FIXME",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:112`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     110 |             "pattern": r"(?:TODO|FIXME|HACK|XXX|BUG)\b",
     111 |             "category": "code-quality",
>>>  112 |             "title": "Unresolved TODO/FIXME",
     113 |             "description": "Developer left a note indicating unfinished or problematic code.",
     114 |             "suggestion": "Review and resolve the TODO/FIXME before deploying.",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:114`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     112 |             "title": "Unresolved TODO/FIXME",
     113 |             "description": "Developer left a note indicating unfinished or problematic code.",
>>>  114 |             "suggestion": "Review and resolve the TODO/FIXME before deploying.",
     115 |             "severity": "info",
     116 |             "languages": ["python", "javascript", "typescript", "java", "go", "rust", "ruby", "php", "c", "cpp"],
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:122`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     120 |             "category": "concurrency",
     121 |             "title": "Manual Thread Management",
>>>  122 |             "description": "Manual thread creation detected. This can cause race conditions and hard-to-debug issues.",
     123 |             "suggestion": "Consider using thread pools, asyncio, or concurrent.futures instead.",
     124 |             "severity": "medium",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:258`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     256 |             "category": "syntax",
     257 |             "title": "Obsolete Solidity Version",
>>>  258 |             "description": "Using an outdated Solidity compiler version that lacks safety improvements and bug fixes.",
     259 |             "suggestion": "Upgrade to Solidity 0.8.x which has built-in overflow/underflow checks.",
     260 |             "severity": "low",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:315`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     313 |                 if compiled_re.search(line):
     314 |                     snippet = _get_snippet(lines, i - 1)
>>>  315 |                     bug = Bug(
     316 |                         file=str(f.relative_path),
     317 |                         line=i,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:328`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     326 |                         confidence=0.7,
     327 |                     )
>>>  328 |                     result.add(bug)
     329 | 
     330 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\__init__.py:1`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
>>>    1 | from analyzer.base import AnalysisResult, BaseAnalyzer, Bug
       2 | from analyzer.static import StaticAnalyzer
       3 | from analyzer.ast_analyzer import ASTAnalyzer
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\__init__.py:15`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      13 |     "AnalysisResult",
      14 |     "BaseAnalyzer",
>>>   15 |     "Bug",
      16 |     "StaticAnalyzer",
      17 |     "ASTAnalyzer",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:50`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      48 | 
      49 |     severity_counts = {}
>>>   50 |     for bug in sorted_bugs:
      51 |         severity_counts[bug.severity] = severity_counts.get(bug.severity, 0) + 1
      52 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:51`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      49 |     severity_counts = {}
      50 |     for bug in sorted_bugs:
>>>   51 |         severity_counts[bug.severity] = severity_counts.get(bug.severity, 0) + 1
      52 | 
      53 |     for sev in ["critical", "high", "medium", "low", "info"]:
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:78`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      76 | 
      77 |     category_groups = {}
>>>   78 |     for bug in sorted_bugs:
      79 |         cat = bug.category
      80 |         if cat not in category_groups:
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:79`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      77 |     category_groups = {}
      78 |     for bug in sorted_bugs:
>>>   79 |         cat = bug.category
      80 |         if cat not in category_groups:
      81 |             category_groups[cat] = []
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:82`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      80 |         if cat not in category_groups:
      81 |             category_groups[cat] = []
>>>   82 |         category_groups[cat].append(bug)
      83 | 
      84 |     category_order = ["security", "logic", "error-handling", "concurrency",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:93`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      91 |         lines.append(f"## {cat.replace('-', ' ').title()} ({len(bugs)})")
      92 |         lines.append(f"")
>>>   93 |         for bug in bugs:
      94 |             lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
      95 |             lines.append(f"")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:94`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      92 |         lines.append(f"")
      93 |         for bug in bugs:
>>>   94 |             lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
      95 |             lines.append(f"")
      96 |             lines.append(f"- **File:** `{bug.file}:{bug.line}`")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:96`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      94 |             lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
      95 |             lines.append(f"")
>>>   96 |             lines.append(f"- **File:** `{bug.file}:{bug.line}`")
      97 |             lines.append(f"- **Severity:** {bug.severity.upper()}")
      98 |             lines.append(f"- **Confidence:** {bug.confidence:.0%}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:97`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      95 |             lines.append(f"")
      96 |             lines.append(f"- **File:** `{bug.file}:{bug.line}`")
>>>   97 |             lines.append(f"- **Severity:** {bug.severity.upper()}")
      98 |             lines.append(f"- **Confidence:** {bug.confidence:.0%}")
      99 |             lines.append(f"- **Analyzer:** {bug.analyzer}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:98`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      96 |             lines.append(f"- **File:** `{bug.file}:{bug.line}`")
      97 |             lines.append(f"- **Severity:** {bug.severity.upper()}")
>>>   98 |             lines.append(f"- **Confidence:** {bug.confidence:.0%}")
      99 |             lines.append(f"- **Analyzer:** {bug.analyzer}")
     100 |             lines.append(f"")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:99`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      97 |             lines.append(f"- **Severity:** {bug.severity.upper()}")
      98 |             lines.append(f"- **Confidence:** {bug.confidence:.0%}")
>>>   99 |             lines.append(f"- **Analyzer:** {bug.analyzer}")
     100 |             lines.append(f"")
     101 |             lines.append(f"**Problem:** {bug.description}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:101`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      99 |             lines.append(f"- **Analyzer:** {bug.analyzer}")
     100 |             lines.append(f"")
>>>  101 |             lines.append(f"**Problem:** {bug.description}")
     102 |             lines.append(f"")
     103 |             lines.append(f"**Fix:** {bug.suggestion}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:103`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     101 |             lines.append(f"**Problem:** {bug.description}")
     102 |             lines.append(f"")
>>>  103 |             lines.append(f"**Fix:** {bug.suggestion}")
     104 |             lines.append(f"")
     105 |             if bug.code_snippet:
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:105`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     103 |             lines.append(f"**Fix:** {bug.suggestion}")
     104 |             lines.append(f"")
>>>  105 |             if bug.code_snippet:
     106 |                 lines.append(f"<details>")
     107 |                 lines.append(f"<summary>Code</summary>")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:110`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     108 |                 lines.append(f"")
     109 |                 lines.append(f"```")
>>>  110 |                 lines.append(bug.code_snippet)
     111 |                 lines.append(f"```")
     112 |                 lines.append(f"</details>")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:121`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     119 |             lines.append(f"## {cat.replace('-', ' ').title()} ({len(bugs)})")
     120 |             lines.append(f"")
>>>  121 |             for bug in bugs:
     122 |                 lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
     123 |                 lines.append(f"- **File:** `{bug.file}:{bug.line}`")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:122`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     120 |             lines.append(f"")
     121 |             for bug in bugs:
>>>  122 |                 lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
     123 |                 lines.append(f"- **File:** `{bug.file}:{bug.line}`")
     124 |                 lines.append(f"- **Severity:** {bug.severity.upper()}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:123`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     121 |             for bug in bugs:
     122 |                 lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
>>>  123 |                 lines.append(f"- **File:** `{bug.file}:{bug.line}`")
     124 |                 lines.append(f"- **Severity:** {bug.severity.upper()}")
     125 |                 lines.append(f"**Problem:** {bug.description}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:124`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     122 |                 lines.append(f"### [{SEVERITY_EMOJI[bug.severity].upper()}] {bug.title}")
     123 |                 lines.append(f"- **File:** `{bug.file}:{bug.line}`")
>>>  124 |                 lines.append(f"- **Severity:** {bug.severity.upper()}")
     125 |                 lines.append(f"**Problem:** {bug.description}")
     126 |                 lines.append(f"**Fix:** {bug.suggestion}")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:125`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     123 |                 lines.append(f"- **File:** `{bug.file}:{bug.line}`")
     124 |                 lines.append(f"- **Severity:** {bug.severity.upper()}")
>>>  125 |                 lines.append(f"**Problem:** {bug.description}")
     126 |                 lines.append(f"**Fix:** {bug.suggestion}")
     127 |                 lines.append(f"---")
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `reporters\__init__.py:126`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     124 |                 lines.append(f"- **Severity:** {bug.severity.upper()}")
     125 |                 lines.append(f"**Problem:** {bug.description}")
>>>  126 |                 lines.append(f"**Fix:** {bug.suggestion}")
     127 |                 lines.append(f"---")
     128 |             lines.append(f"")
```
</details>

---


---
*Generated by BugHunter*