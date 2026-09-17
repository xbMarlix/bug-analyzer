# BugHunter Report: bug_hunter

**Generated:** 2026-09-17 02:30:11
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\bug_hunter`
**Analyzers:** static, ast, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 52 |
| Total lines | 39,863 |
| Bugs found | 107 |
| !!! Critical | 1 |
| !! High | 2 |
| ! Medium | 2 |
| ~ Low | 16 |
| i Info | 86 |

### Languages Detected

- **html**: 38 files
- **python**: 14 files

## Security (1)

### [!!!] Dangerous Code Execution

- **File:** `analyzer\static.py:34`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      32 |             "title": "Dangerous Code Execution",
      33 |             "description": "Dynamic code execution detected. This can lead to remote code execution vulnerabilities.",
>>>   34 |             "suggestion": "Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.",
      35 |             "severity": "critical",
      36 |             "languages": ["python", "javascript", "typescript"],
```
</details>

---

## Error Handling (3)

### [!!] Bare Exception Handler

- **File:** `analyzer\ai_analyzer.py:344`
- **Severity:** HIGH
- **Confidence:** 90%
- **Analyzer:** static

**Problem:** Catching all exceptions silently hides bugs and makes debugging nearly impossible.
EXPLOIT: An attacker can trigger a bare exception handler by causing a transient error in the AI chat method. This can be done by sending a request that results in a 429, 500, 502, 503, or 504 status code, or by sending a request that includes a message containing keywords like 'rate limit', 'internal', 'too many requests', 'connection', 'timeout', or 'temporarily unavailable'.

**Fix:** Catch specific exceptions and log them. Never use bare 'except:' without re-raising.

<details>
<summary>Code</summary>

```
     342 |                     try:
     343 |                         status = e.response.status_code
>>>  344 |                     except Exception:
     345 |                         status = None
     346 |                 status = getattr(getattr(e, "status_code", None), "value", None)
```
</details>

---

### [!] Bare Exception Handler

- **File:** `analyzer\ai_analyzer.py:350`
- **Severity:** MEDIUM
- **Confidence:** 90%
- **Analyzer:** static

**Problem:** Catching all exceptions silently hides bugs and makes debugging nearly impossible.
EXPLOIT: No concrete trigger path provided.

**Fix:** Catch specific exceptions and log them. Never use bare 'except:' without re-raising.

<details>
<summary>Code</summary>

```
     348 |                     try:
     349 |                         status = e.response.status_code
>>>  350 |                     except Exception:
     351 |                         status = None
     352 |                 transient = (
```
</details>

---

### [!] Bare Exception Handler

- **File:** `analyzer\static.py:371`
- **Severity:** MEDIUM
- **Confidence:** 90%
- **Analyzer:** static

**Problem:** Catching all exceptions silently hides bugs and makes debugging nearly impossible.
EXPLOIT: No concrete trigger path provided.

**Fix:** Catch specific exceptions and log them. Never use bare 'except:' without re-raising.

<details>
<summary>Code</summary>

```
     369 |         try:
     370 |             data = yaml.safe_load(path.read_text(encoding="utf-8"))
>>>  371 |         except Exception:
     372 |             continue
     373 |         if not isinstance(data, list):
```
</details>

---

## Code Quality (103)

### [!!] Use of global Statement

- **File:** `analyzer\static.py:352`
- **Severity:** HIGH
- **Confidence:** 90%
- **Analyzer:** ast

**Problem:** Using 'global _RULES_CACHE' creates hidden state and makes code hard to test.
EXPLOIT: Modify the rules_dir parameter to a non-existent directory to trigger the bug.

**Fix:** Pass values as parameters and return results instead.

<details>
<summary>Code</summary>

```
     350 |         languages (optional: derived from the filename, e.g. python.yaml -> python).
     351 |     """
>>>  352 |     global _RULES_CACHE
     353 |     if _RULES_CACHE is not None and rules_dir is None:
     354 |         return _RULES_CACHE
```
</details>

---

### [~] Overly Long Function

- **File:** `main.py:19`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function 'main' is 156 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
      17 | 
      18 | 
>>>   19 | def main():
      20 |     parser = argparse.ArgumentParser(
      21 |         description="BugHunter - AI-powered automatic bug finder",
```
</details>

---

### [~] Overly Long Function

- **File:** `analyzer\ai_analyzer.py:222`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function 'verify_candidates' is 64 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
     220 |     # AI verification of rule-detected candidates (hybrid: rules + AI).
     221 |     # ------------------------------------------------------------------
>>>  222 |     def verify_candidates(self, candidates: list, files: list, errors=None) -> list[Bug]:
     223 |         if not candidates:
     224 |             return []
```
</details>

---

### [~] Overly Long Function

- **File:** `analyzer\ai_analyzer.py:393`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_call_llm' is 72 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
     391 |         return "\n".join(header_lines)
     392 | 
>>>  393 |     def _call_llm(self, prompt: str, f, chunk_start: int) -> list[Bug]:
     394 |         try:
     395 |             response = self._chat(
```
</details>

---

### [~] Overly Long Function

- **File:** `analyzer\ai_analyzer.py:506`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_extract_json_issues' is 65 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
     504 | 
     505 | 
>>>  506 | def _extract_json_issues(text: str) -> list:
     507 |     """Robustly extract a list of finding dicts from a model response."""
     508 |     text = _strip_code_fences(text)
```
</details>

---

### [~] Too Many Parameters

- **File:** `analyzer\ast_analyzer.py:57`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_add_bug' takes 8 parameters. Wide signatures are error-prone.

**Fix:** Group related parameters into a dataclass/config object.

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

### [~] Overly Long Function

- **File:** `analyzer\ast_analyzer.py:280`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_check_chained_comparison' is 61 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
     278 |                     return
     279 | 
>>>  280 |     def _check_chained_comparison(self, boolop, compare):
     281 |         # Redundant overlapping bounds within an and-chain, e.g.  x < 10 and x < 5
     282 |         # (the second is redundant) or x > 3 and x > 1 (first is redundant).
```
</details>

---

### [~] Overly Long Function

- **File:** `analyzer\solidity_analyzer.py:93`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_analyze_file' is 91 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
      91 |         return _COMMENT_RE.sub(" ", line)
      92 | 
>>>   93 |     def _analyze_file(self, f, result, project_storage: set):
      94 |         self._scopes = []
      95 |         self._current_func = None
```
</details>

---

### [~] Overly Long Function

- **File:** `analyzer\solidity_analyzer.py:252`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_track_line' is 87 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
     250 | 
     251 |     # ------------------------------------------------------------------
>>>  252 |     def _track_line(self, sc, line, line_no, result, f):
     253 |         # Track oracle-sanity guards inside the current function.
     254 |         if _ORACLE_READ_RE.search(line):
```
</details>

---

### [~] Overly Long Function

- **File:** `analyzer\solidity_analyzer.py:524`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_check_sweep' is 61 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
     522 |         return m.group("var"), is_native
     523 | 
>>>  524 |     def _check_sweep(self, line: str, line_no: int, result, f):
     525 |         # ---- Case A: transfer / payout target is a var that holds a full-balance
     526 |         #      snapshot taken earlier in the SAME function (multi-line correlation).
```
</details>

---

### [~] Too Many Parameters

- **File:** `analyzer\solidity_analyzer.py:586`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_add_sweep_bug' takes 9 parameters. Wide signatures are error-prone.

**Fix:** Group related parameters into a dataclass/config object.

<details>
<summary>Code</summary>

```
     584 |             )
     585 | 
>>>  586 |     def _add_sweep_bug(self, result, f, line, sev, title, desc, sug, conf):
     587 |         self._add_bug(result, f, line, sev, "accounting", title, desc, sug, conf)
     588 | 
```
</details>

---

### [~] Too Many Parameters

- **File:** `analyzer\solidity_analyzer.py:590`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function '_add_bug' takes 10 parameters. Wide signatures are error-prone.

**Fix:** Group related parameters into a dataclass/config object.

<details>
<summary>Code</summary>

```
     588 | 
     589 |     # ------------------------------------------------------------------
>>>  590 |     def _add_bug(self, result, f, line, sev, category, title, desc, sug, conf):
     591 |         snippet = self._get_snippet(f.content.split("\n"), line - 1)
     592 |         result.add(Bug(
```
</details>

---

### [~] Overly Long Function

- **File:** `reporters\html_report.py:84`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function 'generate_html_report' is 144 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
      82 | 
      83 | 
>>>   84 | def generate_html_report(result, project_path: str, project_stats: dict, analyzers_used: list[str]) -> Path:
      85 |     REPORT_DIR = reporters.REPORT_DIR  # noqa: F821
      86 |     REPORT_DIR.mkdir(exist_ok=True)
```
</details>

---

### [~] Overly Long Function

- **File:** `reporters\__init__.py:24`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ast

**Problem:** Function 'generate_report' is 118 lines long. Long functions are hard to test and review.

**Fix:** Split it into smaller functions with a single responsibility.

<details>
<summary>Code</summary>

```
      22 | 
      23 | 
>>>   24 | def generate_report(result, project_path: str, project_stats: dict, analyzers_used: list[str]) -> Path:
      25 |     REPORT_DIR.mkdir(exist_ok=True)
      26 | 
```
</details>

---

### [~] Hardcoded Sleep

- **File:** `analyzer\ai_analyzer.py:217`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     215 |                 result.bugs.append(b)
     216 | 
>>>  217 |             time.sleep(0.2)
     218 | 
     219 |     # ------------------------------------------------------------------
```
</details>

---

### [~] Hardcoded Sleep

- **File:** `analyzer\ai_analyzer.py:284`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     282 |                 cand.description = (cand.description or "") + "\n[AI REJECTED] " + fix
     283 |                 result.append(cand)
>>>  284 |             time.sleep(verify_delay)
     285 |         return result
     286 | 
```
</details>

---

### [~] Hardcoded Sleep

- **File:** `analyzer\ai_analyzer.py:366`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     364 |                         warn=True,
     365 |                     )
>>>  366 |                     time.sleep(delay)
     367 |                     delay *= 2
     368 |                     continue
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:47`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      45 |     project_path = Path(args.project).resolve()
      46 |     if not project_path.is_dir():
>>>   47 |         print(f"Error: '{project_path}' is not a directory.")
      48 |         sys.exit(1)
      49 | 
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:50`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      48 |         sys.exit(1)
      49 | 
>>>   50 |     print("=" * 60)
      51 |     print("  BugHunter - AI-Powered Bug Finder")
      52 |     print("=" * 60)
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:53`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      51 |     print("  BugHunter - AI-Powered Bug Finder")
      52 |     print("=" * 60)
>>>   53 |     print()
      54 | 
      55 |     print(f"[*] Scanning project: {project_path}")
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:61`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      59 | 
      60 |     if not files:
>>>   61 |         print("[!] No source files found. Check the project path.")
      62 |         sys.exit(0)
      63 | 
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:65`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      63 | 
      64 |     stats = get_project_stats(files)
>>>   65 |     print(f"[+] Found {stats['total_files']} files ({stats['total_lines']:,} lines)")
      66 |     print(f"[+] Languages: {', '.join(f'{k}({v})' for k, v in stats['languages'].items())}")
      67 |     print(f"[+] Scan completed in {scan_time:.2f}s")
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:68`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      66 |     print(f"[+] Languages: {', '.join(f'{k}({v})' for k, v in stats['languages'].items())}")
      67 |     print(f"[+] Scan completed in {scan_time:.2f}s")
>>>   68 |     print()
      69 | 
      70 |     analyzers_used = []
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:73`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      71 |     result = AnalysisResult()
      72 | 
>>>   73 |     print("[*] Running static analysis...")
      74 |     start = time.time()
      75 |     static = StaticAnalyzer()
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:79`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      77 |     result.merge(static_result)
      78 |     analyzers_used.append("static")
>>>   79 |     print(f"[+] Static analysis: {len(static_result.bugs)} issues found ({time.time() - start:.2f}s)")
      80 | 
      81 |     if not args.static_only and not args.no_ast:
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:82`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      80 | 
      81 |     if not args.static_only and not args.no_ast:
>>>   82 |         print("[*] Running AST analysis (Python)...")
      83 |         start = time.time()
      84 |         ast_analyzer = ASTAnalyzer()
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:88`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      86 |         result.merge(ast_result)
      87 |         analyzers_used.append("ast")
>>>   88 |         print(f"[+] AST analysis: {len(ast_result.bugs)} issues found ({time.time() - start:.2f}s)")
      89 | 
      90 |     if not args.static_only:
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:91`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      89 | 
      90 |     if not args.static_only:
>>>   91 |         print("[*] Running Solidity semantic analysis...")
      92 |         start = time.time()
      93 |         sol_analyzer = SolidityAnalyzer()
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:97`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      95 |         result.merge(sol_result)
      96 |         analyzers_used.append("solidity_semantic")
>>>   97 |         print(f"[+] Solidity analysis: {len(sol_result.bugs)} issues found ({time.time() - start:.2f}s)")
      98 | 
      99 |     if not args.static_only and not args.no_ai:
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:100`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
      98 | 
      99 |     if not args.static_only and not args.no_ai:
>>>  100 |         print("[*] Verifying rule candidates with AI (hybrid)...", flush=True)
     101 |         start = time.time()
     102 |         candidates = [
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:108`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     106 |         max_verify = int(os.environ.get("BH_MAX_VERIFY", "100"))
     107 |         if len(candidates) > max_verify:
>>>  108 |             print(f"[!] {len(candidates)} rule candidates — verifying top {max_verify} by severity "
     109 |                   f"(raise limit with BH_MAX_VERIFY)", flush=True)
     110 |             sev_rank = {"high": 0, "medium": 1}
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:122`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     120 |                     result.bugs.remove(b)
     121 |             result.bugs.extend(verified)
>>>  122 |             print(f"[+] AI verified {len(candidates)} rule candidates in {time.time() - start:.2f}s", flush=True)
     123 |         else:
     124 |             print("[+] No rule candidates to verify (skipped)", flush=True)
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:127`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     125 | 
     126 |         if not args.hybrid_only:
>>>  127 |             print("[*] Running AI analysis (this may take a while)...", flush=True)
     128 |             start = time.time()
     129 |             ai = AIAnalyzer()
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:135`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     133 |             if ai_result.errors:
     134 |                 for err in ai_result.errors:
>>>  135 |                     print(f"[!] {err}", flush=True)
     136 |             print(f"[+] AI analysis: {len(ai_result.bugs)} issues found ({time.time() - start:.2f}s)", flush=True)
     137 | 
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:141`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     139 |     result.bugs = dedup_bugs(result.bugs)
     140 |     if len(result.bugs) < before_dedup:
>>>  141 |         print(f"[+] Deduplication: {before_dedup} -> {len(result.bugs)} issues")
     142 | 
     143 |     print()
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:150`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     148 | 
     149 |     report_path = generate_report(result, str(project_path), stats, analyzers_used)
>>>  150 |     print(f"[+] Report saved to: {report_path}")
     151 | 
     152 |     html_path = generate_html_report(result, str(project_path), stats, analyzers_used)
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:153`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     151 | 
     152 |     html_path = generate_html_report(result, str(project_path), stats, analyzers_used)
>>>  153 |     print(f"[+] HTML security review saved to: {html_path}")
     154 |     print()
     155 | 
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:161`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     159 |         sev_counts[bug.severity] = sev_counts.get(bug.severity, 0) + 1
     160 | 
>>>  161 |     print("=" * 60)
     162 |     print("  RESULTS SUMMARY")
     163 |     print("=" * 60)
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:164`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     162 |     print("  RESULTS SUMMARY")
     163 |     print("=" * 60)
>>>  164 |     print(f"  Total issues: {len(result.bugs)}")
     165 |     for sev in ["critical", "high", "medium", "low", "info"]:
     166 |         count = sev_counts.get(sev, 0)
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:169`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     167 |         if count > 0:
     168 |             marker = "!!!" if sev == "critical" else "!!" if sev == "high" else "!" if sev == "medium" else "~" if sev == "low" else "i"
>>>  169 |             print(f"  {marker} {sev.upper():10s}: {count}")
     170 |     if result.errors:
     171 |         print(f"  ERRORS     : {len(result.errors)}")
```
</details>

---

### [I] Extraneous print() Call

- **File:** `main.py:172`
- **Severity:** INFO
- **Confidence:** 50%
- **Analyzer:** ast

**Problem:** A bare 'print()' without a 'debug' marker was left in the code. It may expose internal data in production or indicate unfinished work.

**Fix:** Remove debug prints or gate them behind a logger/config flag.

<details>
<summary>Code</summary>

```
     170 |     if result.errors:
     171 |         print(f"  ERRORS     : {len(result.errors)}")
>>>  172 |     print("=" * 60)
     173 | 
     174 |     sys.exit(1 if sev_counts.get("critical", 0) > 0 else 0)
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `main.py:158`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     156 |     sorted_bugs = result.sorted_bugs()
     157 |     sev_counts = {}
>>>  158 |     for bug in sorted_bugs:
     159 |         sev_counts[bug.severity] = sev_counts.get(bug.severity, 0) + 1
     160 | 
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
>>>    6 | from .base import AnalysisResult, BaseAnalyzer, Bug
       7 | from .patterns import pattern_hints, validate_severity
       8 | from .. import config as _cfg
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:95`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      93 | """
      94 | 
>>>   95 | VERIFY_PROMPT = """You are a security audit validator. A rule-based analyzer flagged a candidate issue in a {language} file. Inspect the code context and decide whether it is a REAL exploitable/reproducible bug.
      96 | 
      97 | CANDIDATE:
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:110`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     108 | 
     109 | Rules:
>>>  110 | - verdict "confirmed": real bug. Provide exploit_path.
     111 | - verdict "downgrade": minor/theoretical. Set actual_severity to medium or low.
     112 | - verdict "rejected": not a bug. Explain in one line as fix.
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:446`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     444 |                 description = "\n".join(x for x in desc_lines if x)
     445 | 
>>>  446 |                 bug = Bug(
     447 |                     file=str(f.relative_path),
     448 |                     line=line_num,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ai_analyzer.py:459`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     457 |                     confidence=float(issue.get("confidence", 0.6)),
     458 |                 )
>>>  459 |                 bugs.append(bug)
     460 | 
     461 |             return bugs
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
>>>    5 | from .base import AnalysisResult, BaseAnalyzer, Bug
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

- **File:** `analyzer\ast_analyzer.py:135`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     133 |     def visit_ExceptHandler(self, node):
     134 |         if node.type is None:
>>>  135 |             self._add_bug(
     136 |                 node, "high", "error-handling",
     137 |                 "Bare Except Clause",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:153`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     151 |         if isinstance(node.func, ast.Name) and node.func.id == "print":
     152 |             if not any(
>>>  153 |                 isinstance(p, ast.Constant) and "debug" in str(p.value).lower()
     154 |                 for p in node.args
     155 |             ):
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:156`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     154 |                 for p in node.args
     155 |             ):
>>>  156 |                 self._add_bug(
     157 |                     node, "info", "code-quality",
     158 |                     "Extraneous print() Call",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:159`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     157 |                     node, "info", "code-quality",
     158 |                     "Extraneous print() Call",
>>>  159 |                     "A bare 'print()' without a 'debug' marker was left in the code. "
     160 |                     "It may expose internal data in production or indicate unfinished work.",
     161 |                     "Remove debug prints or gate them behind a logger/config flag.",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:168`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     166 |     def visit_Global(self, node):
     167 |         for name in node.names:
>>>  168 |             self._add_bug(
     169 |                 node, "medium", "code-quality",
     170 |                 "Use of global Statement",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:186`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     184 |         length = end - getattr(node, "lineno", end) + 1
     185 |         if length > 60:
>>>  186 |             self._add_bug(
     187 |                 node, "low", "code-quality",
     188 |                 "Overly Long Function",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:197`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     195 |         n_params = len(pos_args) + len(kwonly)
     196 |         if n_params > 6:
>>>  197 |             self._add_bug(
     198 |                 node, "low", "code-quality",
     199 |                 "Too Many Parameters",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:209`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     207 |         ]
     208 |         if len(returns) > 5:
>>>  209 |             self._add_bug(
     210 |                 node, "info", "code-quality",
     211 |                 "Many Return Statements",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:239`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     237 |             if name.startswith("_"):
     238 |                 continue
>>>  239 |             self._add_bug(
     240 |                 func_node, "low", "code-quality",
     241 |                 "Unused Variable",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:251`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     249 |             if isinstance(comparator, ast.Constant) and comparator.value is None:
     250 |                 if not isinstance(op, (ast.Is, ast.IsNot)):
>>>  251 |                     self._add_bug(
     252 |                         node, "low", "logic",
     253 |                         "Use 'is None' Instead of '== None'",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:268`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     266 |                     not isinstance(o, (ast.Is, ast.IsNot)) for o in node.ops
     267 |                 ):
>>>  268 |                     self._add_bug(
     269 |                         node, "low", "logic",
     270 |                         "Ambiguous Chained None Comparison",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:324`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     322 |                 # redundant upper bound: sibling tightens beyond current hi already
     323 |                 if arrow in ("<", "<=") and hi is not None and s_val <= hi:
>>>  324 |                     self._add_bug(
     325 |                         sibling, "low", "logic",
     326 |                         "Redundant Chained Comparison",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\ast_analyzer.py:333`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     331 |                     )
     332 |                 elif arrow in (">", ">=") and lo is not None and s_val >= lo:
>>>  333 |                     self._add_bug(
     334 |                         sibling, "low", "logic",
     335 |                         "Redundant Chained Comparison",
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
      34 |         from ..config import SEVERITY_ORDER
      35 |         return sorted(self.bugs, key=lambda b: SEVERITY_ORDER.get(b.severity, 99))
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\dedup.py:24`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      22 | 
      23 |     kept: list = []
>>>   24 |     for bug in ordered:
      25 |         dup = False
      26 |         for other in kept:
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\dedup.py:27`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      25 |         dup = False
      26 |         for other in kept:
>>>   27 |             if bug.file != other.file:
      28 |                 continue
      29 |             if bug.category != other.category:
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\dedup.py:31`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      29 |             if bug.category != other.category:
      30 |                 continue
>>>   31 |             if abs(int(bug.line or 0) - int(other.line or 0)) <= line_tolerance:
      32 |                 dup = True
      33 |                 break
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\dedup.py:35`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      33 |                 break
      34 |         if not dup:
>>>   35 |             kept.append(bug)
      36 |     return kept
      37 | 
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
>>>    2 | from .base import AnalysisResult, BaseAnalyzer, Bug
       3 | 
       4 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:307`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     305 |             sc.calls.append((line_no, call_kind, method))
     306 |             if call_kind in ("call", "delegatecall") and not self._call_result_captured(line):
>>>  307 |                 self._add_bug(
     308 |                     result, f, line_no, "medium", "security",
     309 |                     "Unchecked Low-Level Call Result",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:316`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     314 |             if call_kind == "call" and re.search(r"\.call\s*\{", line):
     315 |                 if sc.guard:
>>>  316 |                     self._add_bug(
     317 |                         result, f, line_no, "info", "security",
     318 |                         "Reentrancy Vector (External Call with Value, Guard Present)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:342`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     340 |     def _report_reentrancy_vector(self, sc, result, f):
     341 |         if sc.write_after_eth:
>>>  342 |             self._add_bug(
     343 |                 result, f, sc.eth_call_line, "high", "security",
     344 |                 "Reentrancy Vector (External Call with Value)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:353`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     351 |             )
     352 |         else:
>>>  353 |             self._add_bug(
     354 |                 result, f, sc.eth_call_line, "info", "security",
     355 |                 "Reentrancy Vector (External Call with Value, CEI Respected)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:405`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     403 |         else:
     404 |             sev, conf, note = "medium", 0.4, ""
>>>  405 |         self._add_bug(
     406 |             result, f, line_no, sev, "logic",
     407 |             "State Change After External Call (CEI Violation)",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:426`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     424 |             return
     425 |         if not sc.oracle_price_checked and sc.oracle_price_casted:
>>>  426 |             self._add_bug(
     427 |                 result, f, sc.oracle_read_line, "high", "oracle",
     428 |                 "Oracle Price Missing Positive Check",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:443`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     441 |             return
     442 |         if not sc.oracle_fresh_checked:
>>>  443 |             self._add_bug(
     444 |                 result, f, sc.oracle_read_line, "medium", "oracle",
     445 |                 "Oracle Price Missing Staleness Check",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:537`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     535 |             if var in self._sweep_vars and self._current_func is not None:
     536 |                 snap_line, is_native = self._sweep_vars[var]
>>>  537 |                 self._add_sweep_bug(
     538 |                     result, f, line_no,
     539 |                     "high" if is_native else "high",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:562`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     560 |         lowered = line.lower()
     561 |         if "address(this).balance" in lowered or "balanceof(address(this))" in lowered:
>>>  562 |             self._add_sweep_bug(
     563 |                 result, f, line_no, "high",
     564 |                 "Full-Balance Sweep in Payout",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\solidity_analyzer.py:575`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     573 |             )
     574 |         else:
>>>  575 |             self._add_sweep_bug(
     576 |                 result, f, line_no, "medium",
     577 |                 "Suspicious Full-Balance Payout",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:4`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       2 | from pathlib import Path
       3 | 
>>>    4 | from .base import AnalysisResult, BaseAnalyzer, Bug
       5 | 
       6 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:111`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     109 |         },
     110 |         {
>>>  111 |             "pattern": r"(?:TODO|FIXME|HACK|XXX|BUG)\b",
     112 |             "category": "code-quality",
     113 |             "title": "Unresolved TODO/FIXME",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:115`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     113 |             "title": "Unresolved TODO/FIXME",
     114 |             "description": "Developer left a note indicating unfinished or problematic code.",
>>>  115 |             "suggestion": "Review and resolve the TODO/FIXME before deploying.",
     116 |             "severity": "info",
     117 |             "languages": ["python", "javascript", "typescript", "java", "go", "rust", "ruby", "php", "c", "cpp"],
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:123`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     121 |             "category": "concurrency",
     122 |             "title": "Manual Thread Management",
>>>  123 |             "description": "Manual thread creation detected. This can cause race conditions and hard-to-debug issues.",
     124 |             "suggestion": "Consider using thread pools, asyncio, or concurrent.futures instead.",
     125 |             "severity": "medium",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:261`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     259 |             "category": "syntax",
     260 |             "title": "Obsolete Solidity Version",
>>>  261 |             "description": "Using an outdated Solidity compiler version that lacks safety improvements and bug fixes.",
     262 |             "suggestion": "Upgrade to Solidity 0.8.x which has built-in overflow/underflow checks.",
     263 |             "severity": "low",
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:326`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     324 |                 if m is not None:
     325 |                     snippet = _get_snippet(lines, i - 1)
>>>  326 |                     bug = Bug(
     327 |                         file=str(f.relative_path),
     328 |                         line=i,
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `analyzer\static.py:339`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     337 |                         confidence=0.7,
     338 |                     )
>>>  339 |                     result.add(bug)
     340 | 
     341 | 
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
>>>    1 | from .base import AnalysisResult, BaseAnalyzer, Bug
       2 | from .static import StaticAnalyzer
       3 | from .ast_analyzer import ASTAnalyzer
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


---
*Generated by BugHunter*