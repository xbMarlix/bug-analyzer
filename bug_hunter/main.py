import argparse
import os
import sys
import time
from pathlib import Path

from .scanner import scan_project, get_project_stats
from .analyzer.static import StaticAnalyzer
from .analyzer.ast_analyzer import ASTAnalyzer
from .analyzer.solidity_analyzer import SolidityAnalyzer
from .analyzer.ai_analyzer import AIAnalyzer
from .analyzer.base import AnalysisResult
from .analyzer.dedup import dedup_bugs
from .reporters import generate_report
from .reporters.html_report import generate_html_report
from . import config


def main():
    parser = argparse.ArgumentParser(
        description="BugHunter - AI-powered automatic bug finder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py .
  python main.py ./my_project --no-ai
  python main.py ./my_project --report-dir ./reports
        """,
    )
    parser.add_argument("project", help="Path to the project directory to analyze")
    parser.add_argument("--no-ai", action="store_true", help="Skip AI analysis (static only)")
    parser.add_argument("--no-ast", action="store_true", help="Skip AST analysis")
    parser.add_argument("--static-only", action="store_true", help="Run only static analysis")
    parser.add_argument("--hybrid-only", action="store_true",
                        help="Run rules + AI verification of rule candidates only (skip the full AI audit loop)")
    parser.add_argument("--report-dir", type=str, default=None, help="Custom report output directory")
    parser.add_argument("--model", type=str, default=None, help="Override AI model (e.g. qwen2.5-coder:14b)")

    args = parser.parse_args()

    if args.model:
        os.environ["OPENAI_MODEL"] = args.model
        config.OPENAI_MODEL = args.model

    project_path = Path(args.project).resolve()
    if not project_path.is_dir():
        print(f"Error: '{project_path}' is not a directory.")
        sys.exit(1)

    print("=" * 60)
    print("  BugHunter - AI-Powered Bug Finder")
    print("=" * 60)
    print()

    print(f"[*] Scanning project: {project_path}")
    start = time.time()
    files = scan_project(project_path, extra_ignored=config.IGNORED_DIRS)
    scan_time = time.time() - start

    if not files:
        print("[!] No source files found. Check the project path.")
        sys.exit(0)

    stats = get_project_stats(files)
    print(f"[+] Found {stats['total_files']} files ({stats['total_lines']:,} lines)")
    print(f"[+] Languages: {', '.join(f'{k}({v})' for k, v in stats['languages'].items())}")
    print(f"[+] Scan completed in {scan_time:.2f}s")
    print()

    analyzers_used = []
    result = AnalysisResult()

    print("[*] Running static analysis...")
    start = time.time()
    static = StaticAnalyzer()
    static_result = static.analyze(files)
    result.merge(static_result)
    analyzers_used.append("static")
    print(f"[+] Static analysis: {len(static_result.bugs)} issues found ({time.time() - start:.2f}s)")

    if not args.static_only and not args.no_ast:
        print("[*] Running AST analysis (Python)...")
        start = time.time()
        ast_analyzer = ASTAnalyzer()
        ast_result = ast_analyzer.analyze(files)
        result.merge(ast_result)
        analyzers_used.append("ast")
        print(f"[+] AST analysis: {len(ast_result.bugs)} issues found ({time.time() - start:.2f}s)")

    if not args.static_only:
        print("[*] Running Solidity semantic analysis...")
        start = time.time()
        sol_analyzer = SolidityAnalyzer()
        sol_result = sol_analyzer.analyze(files)
        result.merge(sol_result)
        analyzers_used.append("solidity_semantic")
        print(f"[+] Solidity analysis: {len(sol_result.bugs)} issues found ({time.time() - start:.2f}s)")

    if not args.static_only and not args.no_ai:
        print("[*] Verifying rule candidates with AI (hybrid)...", flush=True)
        start = time.time()
        candidates = [
            b for b in result.bugs
            if b.severity in ("high", "medium") and b.analyzer != "ai"
        ]
        max_verify = int(os.environ.get("BH_MAX_VERIFY", "100"))
        if len(candidates) > max_verify:
            print(f"[!] {len(candidates)} rule candidates — verifying top {max_verify} by severity "
                  f"(raise limit with BH_MAX_VERIFY)", flush=True)
            sev_rank = {"high": 0, "medium": 1}
            candidates.sort(key=lambda b: (sev_rank.get(b.severity, 2), -b.confidence))
            candidates = candidates[:max_verify]
        if candidates:
            ai = AIAnalyzer()
            verified = ai.verify_candidates(candidates, files, errors=result.errors)
            verified_by_line = {(b.file, b.line, b.title) for b in verified}
            for b in list(result.bugs):
                key = (b.file, b.line, b.title)
                if key in verified_by_line:
                    result.bugs.remove(b)
            result.bugs.extend(verified)
            print(f"[+] AI verified {len(candidates)} rule candidates in {time.time() - start:.2f}s", flush=True)
        else:
            print("[+] No rule candidates to verify (skipped)", flush=True)

        if not args.hybrid_only:
            print("[*] Running AI analysis (this may take a while)...", flush=True)
            start = time.time()
            ai = AIAnalyzer()
            ai_result = ai.analyze(files)
            result.merge(ai_result)
            analyzers_used.append("ai")
            if ai_result.errors:
                for err in ai_result.errors:
                    print(f"[!] {err}", flush=True)
            print(f"[+] AI analysis: {len(ai_result.bugs)} issues found ({time.time() - start:.2f}s)", flush=True)

    before_dedup = len(result.bugs)
    result.bugs = dedup_bugs(result.bugs)
    if len(result.bugs) < before_dedup:
        print(f"[+] Deduplication: {before_dedup} -> {len(result.bugs)} issues")

    print()

    if args.report_dir:
        from . import reporters
        reporters.REPORT_DIR = Path(args.report_dir)

    report_path = generate_report(result, str(project_path), stats, analyzers_used)
    print(f"[+] Report saved to: {report_path}")

    html_path = generate_html_report(result, str(project_path), stats, analyzers_used)
    print(f"[+] HTML security review saved to: {html_path}")
    print()

    sorted_bugs = result.sorted_bugs()
    sev_counts = {}
    for bug in sorted_bugs:
        sev_counts[bug.severity] = sev_counts.get(bug.severity, 0) + 1

    print("=" * 60)
    print("  RESULTS SUMMARY")
    print("=" * 60)
    print(f"  Total issues: {len(result.bugs)}")
    for sev in ["critical", "high", "medium", "low", "info"]:
        count = sev_counts.get(sev, 0)
        if count > 0:
            marker = "!!!" if sev == "critical" else "!!" if sev == "high" else "!" if sev == "medium" else "~" if sev == "low" else "i"
            print(f"  {marker} {sev.upper():10s}: {count}")
    if result.errors:
        print(f"  ERRORS     : {len(result.errors)}")
    print("=" * 60)

    sys.exit(1 if sev_counts.get("critical", 0) > 0 else 0)


if __name__ == "__main__":
    main()
