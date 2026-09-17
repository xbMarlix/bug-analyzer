"""Ignore mechanism for bug_hunter findings.

Three layers:

1. Inline: a line ending with a ``bug-hunter-ignore`` comment suppresses any
   finding on that line. Optionally name a rule title:
   ``# bug-hunter-ignore: Hardcoded Secret``.

2. Project file: ``.bughunterignore`` in the scanned project root.
   One glob per line; a finding is suppressed when its file matches.
   ``#`` starts a comment. A trailing ``:Rule Title`` limits the suppression
   to one rule title, e.g.::

       # skip vendored code entirely
       third_party/**
       # only the secret rule in this config sample
       config/example.py:Hardcoded Secret

3. Built-in self-exclusion: bug_hunter's own rule/pattern source files
   (rules/*.yaml, static.py pattern table) contain the very strings the rules
   search for, so findings on them are always false positives and are dropped.
"""
from __future__ import annotations

from fnmatch import fnmatch
from pathlib import Path

INLINE_MARKER = "bug-hunter-ignore"

# Files inside the bug_hunter package itself whose content is rule definitions
# (regex source), not real code under audit.
_SELF_EXCLUDED = (
    "rules/",
    "analyzer/static.py",
    "analyzer/patterns.py",
)


class IgnoreRules:
    def __init__(self, project_path: str | Path | None = None):
        self._file_globs: list[tuple[str, str | None]] = []
        if project_path:
            self._load(Path(project_path) / ".bughunterignore")

    def _load(self, path: Path):
        if not path.is_file():
            return
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            return
        for raw in lines:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            glob, _, title = line.partition(":")
            title = title.strip() or None
            self._file_globs.append((glob.strip(), title))

    def is_ignored(self, file: str, line_no: int, title: str,
                   line_content: str | None = None) -> bool:
        # Layer 1: inline marker
        if line_content and INLINE_MARKER in line_content:
            after = line_content.split(INLINE_MARKER, 1)[1].lstrip(" :")
            # bare marker, or marker naming this rule
            if not after or title.lower().startswith(after.lower()):
                return True

        # Layer 3: bug_hunter's own rule files
        normalized = file.replace("\\", "/")
        for prefix in _SELF_EXCLUDED:
            if normalized.endswith(prefix.rstrip("/")) or f"/{prefix}" in normalized:
                return True

        # Layer 2: .bughunterignore globs
        for glob, rule_title in self._file_globs:
            if rule_title and rule_title.lower() != title.lower():
                continue
            if fnmatch(normalized, glob) or fnmatch(Path(normalized).name, glob):
                return True
        return False


def apply_ignores(bugs: list, ignore: IgnoreRules,
                  file_lines: dict[str, list[str]] | None = None) -> list:
    """Drop bugs suppressed by the ignore rules.

    file_lines: optional {relative_path: [line, ...]} for inline-marker lookup;
    when absent, inline markers are still honored if the bug's code_snippet
    carries the flagged line (it does, marked with '>>>').
    """
    kept = []
    for bug in bugs:
        line_content = None
        if file_lines and bug.file in file_lines:
            idx = int(bug.line or 0) - 1
            lines = file_lines[bug.file]
            if 0 <= idx < len(lines):
                line_content = lines[idx]
        elif bug.code_snippet:
            for snip_line in bug.code_snippet.splitlines():
                if snip_line.startswith(">>>"):
                    line_content = snip_line.split("|", 1)[-1]
                    break
        if not ignore.is_ignored(bug.file, bug.line, bug.title, line_content):
            kept.append(bug)
    return kept
