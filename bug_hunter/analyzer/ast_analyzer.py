import ast
import sys
from pathlib import Path

from .base import AnalysisResult, BaseAnalyzer, Bug


class ASTAnalyzer(BaseAnalyzer):
    name = "ast"

    def analyze(self, files: list) -> AnalysisResult:
        result = AnalysisResult()
        for f in files:
            if f.language == "python":
                self._analyze_python(f, result)
        result.files_analyzed = sum(1 for f in files if f.language == "python")
        return result

    def _analyze_python(self, f, result: AnalysisResult):
        try:
            tree = ast.parse(f.content, filename=str(f.path))
        except SyntaxError as e:
            result.errors.append(f"Syntax error in {f.relative_path}: {e}")
            result.add(Bug(
                file=str(f.relative_path),
                line=e.lineno or 1,
                column=e.offset or 0,
                severity="high",
                category="syntax",
                title="Syntax Error",
                description=f"Python syntax error: {e.msg}",
                suggestion="Fix the syntax error before running the analysis.",
                analyzer=self.name,
                confidence=1.0,
            ))
            return

        checker = _PythonChecker(f, result)
        checker.visit(tree)


class _PythonChecker(ast.NodeVisitor):
    def __init__(self, f, result: AnalysisResult):
        self.f = f
        self.result = result
        self._scope_names = [set()]

    def _current_scope(self):
        return self._scope_names[-1]

    def _find_defined(self, name):
        for scope in reversed(self._scope_names):
            if name in scope:
                return True
        return False

    def _add_bug(self, node, severity, category, title, description, suggestion, confidence=0.8):
        line = getattr(node, "lineno", 1)
        col = getattr(node, "col_offset", 0)
        snippet = _get_snippet(self.f.content.split("\n"), line - 1)
        self.result.add(Bug(
            file=str(self.f.relative_path),
            line=line,
            column=col,
            severity=severity,
            category=category,
            title=title,
            description=description,
            suggestion=suggestion,
            code_snippet=snippet,
            analyzer="ast",
            confidence=confidence,
        ))

    def visit_FunctionDef(self, node):
        self._check_function_common(node)
        self._scope_names.append(set())
        self.generic_visit(node)
        self._check_unused_names(node)
        self._scope_names.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_ClassDef(self, node):
        self._scope_names.append(set())
        self.generic_visit(node)
        self._scope_names.pop()

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self._current_scope().add(target.id)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        if isinstance(node.target, ast.Name):
            self._current_scope().add(node.target.id)
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self._current_scope().add(name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self._current_scope().add(name)
        self.generic_visit(node)

    def visit_For(self, node):
        self._current_scope().add(node.target.id if isinstance(node.target, ast.Name) else "")
        self.generic_visit(node)

    def visit_With(self, node):
        for item in node.items:
            if item.optional_vars and isinstance(item.optional_vars, ast.Name):
                self._current_scope().add(item.optional_vars.id)
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        for value in node.values:
            if isinstance(value, ast.Compare):
                self._check_chained_comparison(node, value)
        self.generic_visit(node)

    def visit_Compare(self, node):
        self._check_is_vs_eq(node)
        self._check_chained_comparison_none(node)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self._add_bug(
                node, "high", "error-handling",
                "Bare Except Clause",
                "Catching all exceptions with bare 'except:' hides bugs and interrupts flow.",
                "Catch specific exceptions: except ValueError as e:",
                confidence=0.9,
            )
        self.generic_visit(node)

    def visit_Raise(self, node):
        if node.exc is None and node.cause is None:
            self.generic_visit(node)
            return
        self.generic_visit(node)

    def visit_Call(self, node):
        # CLI entry points legitimately print to stdout; don't flag them.
        if self.f.path.name in ("main.py", "cli.py", "__main__.py"):
            self.generic_visit(node)
            return
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            if not any(
                isinstance(p, ast.Constant) and "debug" in str(p.value).lower()
                for p in node.args
            ):
                self._add_bug(
                    node, "info", "code-quality",
                    "Extraneous print() Call",
                    "A bare 'print()' without a 'debug' marker was left in the code. "
                    "It may expose internal data in production or indicate unfinished work.",
                    "Remove debug prints or gate them behind a logger/config flag.",
                    confidence=0.5,
                )
        self.generic_visit(node)

    def visit_Global(self, node):
        for name in node.names:
            self._add_bug(
                node, "medium", "code-quality",
                "Use of global Statement",
                f"Using 'global {name}' creates hidden state and makes code hard to test.",
                "Pass values as parameters and return results instead.",
                confidence=0.8,
            )
        self.generic_visit(node)

    def visit_Starred(self, node):
        self.generic_visit(node)

    def _check_function_common(self, node):
        """Cross-language quality checks on a function definition."""
        name = getattr(node, "name", "")
        end = getattr(node, "end_lineno", None) or getattr(node, "lineno", 0)
        length = end - getattr(node, "lineno", end) + 1
        if length > 60:
            self._add_bug(
                node, "low", "code-quality",
                "Overly Long Function",
                f"Function '{name}' is {length} lines long. Long functions are hard to test and review.",
                "Split it into smaller functions with a single responsibility.",
                confidence=0.6,
            )
        pos_args = list(getattr(node.args, "args", []) or [])
        kwonly = list(getattr(node.args, "kwonlyargs", []) or [])
        n_params = len(pos_args) + len(kwonly)
        if n_params > 6:
            self._add_bug(
                node, "low", "code-quality",
                "Too Many Parameters",
                f"Function '{name}' takes {n_params} parameters. Wide signatures are error-prone.",
                "Group related parameters into a dataclass/config object.",
                confidence=0.6,
            )
        returns = [
            n for n in _walk_scope(node)
            if isinstance(n, ast.Return) and n.value is not None
        ]
        if len(returns) > 5:
            self._add_bug(
                node, "info", "code-quality",
                "Many Return Statements",
                f"Function '{name}' has {len(returns)} return points — high cyclomatic complexity.",
                "Reduce branching or extract helper functions.",
                confidence=0.5,
            )

    def _check_unused_names(self, func_node):
        defined = set()
        used = set()

        # Scope-aware walk: visit the function's own body but DO NOT descend into
        # nested function/class/lambda bodies, so closures don't produce false
        # "unused" findings on names that are actually captured and used later.
        for node in _walk_scope(func_node):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Load):
                    used.add(node.id)
                elif isinstance(node.ctx, ast.Store):
                    defined.add(node.id)

        for arg in func_node.args.args:
            if arg.arg != "self" and arg.arg != "cls":
                used.add(arg.arg)

        unused = defined - used
        for name in unused:
            if name.startswith("_"):
                continue
            self._add_bug(
                func_node, "low", "code-quality",
                "Unused Variable",
                f"Variable '{name}' is assigned but never used.",
                f"Remove unused variable '{name}' or use it.",
                confidence=0.6,
            )

    def _check_is_vs_eq(self, node):
        for op, comparator in zip(node.ops, node.comparators):
            if isinstance(comparator, ast.Constant) and comparator.value is None:
                if not isinstance(op, (ast.Is, ast.IsNot)):
                    self._add_bug(
                        node, "low", "logic",
                        "Use 'is None' Instead of '== None'",
                        "Comparing with None using == is not idiomatic and can behave unexpectedly with custom __eq__.",
                        "Use 'is None' or 'is not None' for None comparisons.",
                        confidence=0.9,
                    )

    def _check_chained_comparison_none(self, node):
        # x < y is None  and  a == b is None  parse as (x<y) and (y is None). Flag
        # any chain that mixes an is/is-not on None with other comparison ops,
        # because it reads as a single boolean but is actually two chained checks.
        for op, comp in zip(node.ops, node.comparators):
            if isinstance(op, (ast.Is, ast.IsNot)):
                if len(node.ops) > 1 and any(
                    not isinstance(o, (ast.Is, ast.IsNot)) for o in node.ops
                ):
                    self._add_bug(
                        node, "low", "logic",
                        "Ambiguous Chained None Comparison",
                        "Chaining 'is/is not None' with other comparison operators is "
                        "evaluated as multiple chained conditions, which is almost always "
                        "not the intended single boolean check and can silently give the "
                        "wrong result.",
                        "Split the checks: 'x is not None and x < 10' instead of 'x < 10 is not None'.",
                        confidence=0.85,
                    )
                    return

    def _check_chained_comparison(self, boolop, compare):
        # Redundant overlapping bounds within an and-chain, e.g.  x < 10 and x < 5
        # (the second is redundant) or x > 3 and x > 1 (first is redundant).
        parsed = []
        base = None
        if isinstance(compare.left, ast.Name):
            base = compare.left.id
        elif isinstance(compare.left, ast.Attribute):
            base = compare.left.attr
        cmp_ops = compare.ops
        comparators = compare.comparators
        # ASTCompare can itself hold a chain (a < b < c); flatten its own pairs first.
        if isinstance(compare, ast.Compare):
            for op, comp in zip(cmp_ops, comparators):
                parsed.append((self._cmp_arrow(op), _const(comp)))
        if not base:
            return
        # only compare against constants to avoid false positives on mutable values
        if not all(c is not None for _, c in parsed):
            return
        op0 = parsed[0][0]
        lo, hi = None, None
        for arrow, cval in parsed:
            if arrow in ("<", "<="):
                hi = cval if hi is None else min(hi, cval)
            elif arrow in (">", ">="):
                lo = cval if lo is None else max(lo, cval)
        # look at the rest of the and-chain for the same base with redundant bounds
        for sibling in boolop.values:
            if sibling is compare:
                continue
            if not isinstance(sibling, ast.Compare):
                continue
            if not (isinstance(sibling.left, ast.Name) and sibling.left.id == base) and not (
                isinstance(sibling.left, ast.Attribute) and sibling.left.attr == base
            ):
                continue
            for s_op, s_comp in zip(sibling.ops, sibling.comparators):
                s_val = _const(s_comp)
                if s_val is None:
                    continue
                arrow = self._cmp_arrow(s_op)
                # redundant upper bound: sibling tightens beyond current hi already
                if arrow in ("<", "<=") and hi is not None and s_val <= hi:
                    self._add_bug(
                        sibling, "low", "logic",
                        "Redundant Chained Comparison",
                        f"Condition limits '{base}' to <= {hi} and then to {arrow} {s_val}, "
                        "which adds no information. One of the bounds is redundant.",
                        "Remove the redundant bound to make the intent clear.",
                        confidence=0.6,
                    )
                elif arrow in (">", ">=") and lo is not None and s_val >= lo:
                    self._add_bug(
                        sibling, "low", "logic",
                        "Redundant Chained Comparison",
                        f"Condition limits '{base}' to >= {lo} and then to {arrow} {s_val}, "
                        "which adds no information. One of the bounds is redundant.",
                        "Remove the redundant bound to make the intent clear.",
                        confidence=0.6,
                    )

    @staticmethod
    def _cmp_arrow(op) -> str:
        if isinstance(op, ast.Lt):
            return "<"
        if isinstance(op, ast.LtE):
            return "<="
        if isinstance(op, ast.Gt):
            return ">"
        if isinstance(op, ast.GtE):
            return ">="
        return ""


def _const(node):
    """Return the numeric/constant value of a node, or None if it is not a plain constant."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        operand = _const(node.operand)
        if operand is None:
            return None
        return -operand if isinstance(node.op, ast.USub) else operand
    return None

    def visit_Lambda(self, node):
        self._scope_names.append(set())
        self.generic_visit(node)
        self._scope_names.pop()


def _get_snippet(lines: list[str], index: int, context: int = 2) -> str:
    start = max(0, index - context)
    end = min(len(lines), index + context + 1)
    snippet_lines = []
    for i in range(start, end):
        marker = ">>>" if i == index else "   "
        snippet_lines.append(f"{marker} {i + 1:4d} | {lines[i]}")
    return "\n".join(snippet_lines)


_SCOPE_NODES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)


def _walk_scope(root):
    """Yield `root` and its descendants that belong to the same lexical scope,
    skipping nested function/class/lambda bodies (which introduce their own scope)."""
    yield root
    if isinstance(root, _SCOPE_NODES):
        return
    for child in ast.iter_child_nodes(root):
        yield from _walk_scope(child)
