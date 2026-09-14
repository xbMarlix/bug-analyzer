"""Deduplicate findings from multiple analyzers.

Two findings are duplicates when they point at (nearly) the same location
(file, line within tolerance) and the same category. When duplicates exist,
keep the one from the higher-priority analyzer: ai > ast > solidity_semantic > static.
"""
from __future__ import annotations

_ANALYZER_PRIORITY = {"ai": 0, "ast": 1, "solidity_semantic": 2, "static": 3}
_LINE_TOLERANCE = 2


def dedup_bugs(bugs: list, line_tolerance: int = _LINE_TOLERANCE) -> list:
    if len(bugs) <= 1:
        return list(bugs)

    # Sort so the preferred analyzer's copy of each cluster comes first.
    ordered = sorted(
        bugs,
        key=lambda b: _ANALYZER_PRIORITY.get(getattr(b, "analyzer", "static"), 9),
    )

    kept: list = []
    for bug in ordered:
        dup = False
        for other in kept:
            if bug.file != other.file:
                continue
            if bug.category != other.category:
                continue
            if abs(int(bug.line or 0) - int(other.line or 0)) <= line_tolerance:
                dup = True
                break
        if not dup:
            kept.append(bug)
    return kept
