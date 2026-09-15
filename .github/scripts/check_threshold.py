"""Fail CI if findings at/above severity threshold exist in the BugHunter report.

Usage: python check_threshold.py <report-dir> <critical|high|medium|low|never>
Exit 0 = pass, 1 = threshold exceeded.
"""
import re
import sys
from pathlib import Path

SEVERITIES = ["critical", "high", "medium", "low"]


def main():
    report_dir = Path(sys.argv[1])
    fail_on = sys.argv[2].lower()

    if fail_on == "never":
        print("fail-on=never, skipping threshold check")
        return 0

    threshold_idx = SEVERITIES.index(fail_on)
    report = None
    for f in report_dir.glob("bug_report_*.md"):
        if report is None or f.name > report.name:
            report = f

    if report is None:
        print("No BugHunter report found — passing (scan may have produced nothing)")
        return 0

    text = report.read_text(encoding="utf-8", errors="replace")
    counts = {}
    for sev in SEVERITIES:
        m = re.search(rf"{sev.capitalize()}\s*\|\s*(\d+)", text)
        counts[sev] = int(m.group(1)) if m else 0

    print(f"Findings: {counts}")
    for sev in SEVERITIES[: threshold_idx + 1]:
        if counts[sev] > 0:
            print(f"FAIL: {counts[sev]} {sev} finding(s) at/above threshold '{fail_on}'")
            return 1

    print(f"PASS: no findings at/above '{fail_on}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
