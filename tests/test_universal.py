"""Tests for the universal-analyzer improvements."""
import textwrap
from pathlib import Path

import pytest

from bug_hunter.scanner import ScannedFile, scan_project, should_ignore
from bug_hunter.analyzer.dedup import dedup_bugs
from bug_hunter.analyzer.base import Bug
from bug_hunter.analyzer.static import StaticAnalyzer, load_yaml_rules
from bug_hunter.analyzer.ai_analyzer import (
    _select_audit_prompt,
    _select_system_prompt,
    AUDIT_PROMPT_GENERIC,
    AUDIT_PROMPT_SOLIDITY,
    SYSTEM_PROMPT_GENERIC,
    SYSTEM_PROMPT_SOLIDITY,
)


def make_file(content, name="x.py", language="python"):
    f = ScannedFile(Path(name), language, content)
    f.relative_path = Path(name)
    return f


# ---- dedup ----

def _bug(file, line, category, analyzer):
    return Bug(file=file, line=line, column=0, severity="high", category=category,
               title="t", description="d", suggestion="s", analyzer=analyzer)


def test_dedup_prefers_ai_over_static():
    bugs = [_bug("a.py", 10, "injection", "static"), _bug("a.py", 11, "injection", "ai")]
    out = dedup_bugs(bugs)
    assert len(out) == 1 and out[0].analyzer == "ai"


def test_dedup_keeps_different_categories_and_files():
    bugs = [_bug("a.py", 10, "injection", "ai"), _bug("a.py", 10, "xss", "static"),
            _bug("b.py", 10, "injection", "static")]
    assert len(dedup_bugs(bugs)) == 3


def test_dedup_line_tolerance():
    bugs = [_bug("a.py", 10, "injection", "static"), _bug("a.py", 14, "injection", "ai")]
    assert len(dedup_bugs(bugs)) == 2  # 4 lines apart > tolerance 2


# ---- prompts ----

def test_prompt_selection_by_language():
    assert _select_audit_prompt("solidity") is AUDIT_PROMPT_SOLIDITY
    assert _select_system_prompt("solidity") is SYSTEM_PROMPT_SOLIDITY
    assert _select_audit_prompt("python") is AUDIT_PROMPT_GENERIC
    assert _select_system_prompt("javascript") is SYSTEM_PROMPT_GENERIC


# ---- yaml rules ----

def test_yaml_rules_load():
    rules = load_yaml_rules()
    langs = {l for r in rules for l in r["languages"]}
    assert {"python", "javascript", "go"} <= langs
    assert all(r["pattern"] and r["severity"] for r in rules)


def test_yaml_rule_finds_pickle():
    sa = StaticAnalyzer()
    f = make_file("import pickle\npickle.loads(data)\n")
    res = sa.analyze([f])
    titles = [b.title for b in res.bugs]
    assert "Unsafe pickle deserialization" in titles


def test_yaml_rule_finds_go_insecure_tls():
    sa = StaticAnalyzer()
    f = make_file('c := &tls.Config{InsecureSkipVerify: true}\n', "main.go", "go")
    res = sa.analyze([f])
    assert any(b.category == "crypto" for b in res.bugs)


# ---- scanner ignores ----

def test_extra_ignored_dirs(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "a.py").write_text("x = 1")
    (tmp_path / "generated").mkdir()
    (tmp_path / "generated" / "b.py").write_text("y = 2")
    files = scan_project(tmp_path, extra_ignored={"generated"})
    names = {str(f.relative_path) for f in files}
    assert names == {str(Path("src") / "a.py")}


def test_default_ignored_still_works(tmp_path):
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "c.js").write_text("z = 3")
    files = scan_project(tmp_path)
    assert files == []


# ---- package import ----

def test_package_imports():
    import bug_hunter.main  # noqa: F401
    from bug_hunter.analyzer import StaticAnalyzer as SA, AIAnalyzer as AA  # noqa: F401
