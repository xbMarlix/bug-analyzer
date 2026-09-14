import re
from analyzer.base import AnalysisResult, BaseAnalyzer, Bug


_COMMENT_RE = re.compile(r"\s*(//.*|/\*.*)$")
_STORAGE_DECL_RE = re.compile(
    r"^\s*(?P<type>mapping\s*\([^;{}]*\)\s*=>\s*[^;{}]+|(?:immutable\s+|constant\s+)?[A-Za-z_][A-Za-z0-9_.<>\[\]]+)\s+"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*(?:\=.*)?;",
    re.MULTILINE,
)
_DELEGATECALL_RE = re.compile(r"\.\s*delegatecall\s*\(", re.MULTILINE)
_CALL_RE = re.compile(r"\.\s*call\s*[({]", re.MULTILINE)
_STATICCALL_RE = re.compile(r"\.\s*staticcall\s*\(", re.MULTILINE)
_TRANSFER_RE = re.compile(r"\.\s*(?:transfer|send)\s*\(", re.MULTILINE)
_TYPECAST_CALL_RE = re.compile(
    r"\(\s*I[A-Z][A-Za-z0-9_]*\s*[^)]*\)\s*\.\s*[A-Za-z_][A-Za-z0-9_]*\s*\(", re.MULTILINE
)
_REENTRANCY_GUARD_MODS = ("nonreentrant", "nonrentrant", "_nonreentrant", "reentrancyguard")

# --- Oracle sanity detectors (Chainlink latestRoundData) -------------------
_ORACLE_READ_RE = re.compile(r"latestRoundData\s*\(", re.MULTILINE)
# A positivity/negativity guard on the int256 price BEFORE it is cast to uint.
_ORACLE_POS_CHECK_RE = re.compile(
    r"\bprice\s*(?:<=|<|==|>|>=|!=)\s*0\b|\bprice\s*>\s*0\b|0\s*<\s*price\b|\b(?:require|if)\s*\([^)]*price[^)]*[*+-]?0",
    re.IGNORECASE,
)
# A freshness/staleness guard (updatedAt staleness or round-completeness).
_ORACLE_FRESH_RE = re.compile(
    r"updatedAt\s*[-+<>=]|block\.timestamp\s*-\s*updatedAt|startedAt|answeredInRound|staleness|heartbeat",
    re.IGNORECASE,
)


class SolidScope:
    __slots__ = ("kind", "owner", "storage", "calls", "line", "guard",
                 "uses_oracle", "oracle_read_line", "oracle_price_checked", "oracle_fresh_checked",
                 "oracle_price_vars", "oracle_price_casted", "eth_call_line", "write_after_eth")

    def __init__(self, kind, owner, storage, line, guard=False):
        self.kind = kind          # contract | library | interface | function | modifier
        self.owner = owner
        self.storage = storage    # set[str]
        self.calls = []           # [(line, kind)]
        self.line = line
        self.guard = guard
        self.uses_oracle = False
        self.oracle_read_line = 0
        self.oracle_price_checked = False
        self.oracle_fresh_checked = False
        self.oracle_price_vars = set()   # variable names holding the raw signed price
        self.oracle_price_casted = False  # True if a raw price var is later uint256()-cast
        self.eth_call_line = 0   # line of the first .call{value:} without a guard
        self.write_after_eth = False  # storage write observed after the value-call


class SolidityAnalyzer(BaseAnalyzer):
    """Semantic Solidity analysis: CEI/reentrancy candidates, unchecked low-level calls."""

    name = "solidity_semantic"

    def __init__(self):
        self._scopes = []
        self._current_func = None
        self._write_re_cache = {}

    def analyze(self, files: list) -> AnalysisResult:
        result = AnalysisResult()
        count = 0
        sol_files = [f for f in files if f.language == "solidity"]
        # Build a project-wide set of storage variable names so inherited storage
        # (included via base contracts in other files) is also tracked.
        project_storage = set()
        if sol_files:
            import itertools
            for f in sol_files:
                decls = self._collect_storage_decls(f.content.split("\n"))
                for name_set in decls.values():
                    project_storage |= name_set
        for f in sol_files:
            count += 1
            try:
                self._analyze_file(f, result, project_storage)
            except Exception as e:
                result.errors.append(f"solidity_analyzer error in {f.relative_path}: {e}")
        result.files_analyzed = count
        return result

    # ------------------------------------------------------------------
    @staticmethod
    def _strip_comment(line: str) -> str:
        return _COMMENT_RE.sub(" ", line)

    def _analyze_file(self, f, result, project_storage: set):
        self._scopes = []
        self._current_func = None
        self._pending_func = None  # multi-line function header keyword-lines seen so far
        self._file_lines = f.content.split("\n")
        self._sweep_vars = {}  # local var holding a full-balance snapshot: {name: (line_no, is_native)}
        lines = self._file_lines
        storage_by_contract = self._collect_storage_decls(lines)

        for i, raw in enumerate(lines, 1):
            line = self._strip_comment(raw).strip()
            if not line:
                continue

            # --- track local vars assigned from a full-balance snapshot ---------
            vm = self._match_sweep_assignment(line)
            if vm and self._current_func is not None:
                self._sweep_vars[vm[0]] = (i, vm[1])

            # --- sweep-all payout detector (line location + cross-line) ---------
            self._check_sweep(line, i, result, f)

            closes = line.count("}")
            # --- process the line inside the current function -----------------
            if self._current_func is not None:
                self._track_line(self._current_func, line, i, result, f)

            # --- pop scopes on closing braces ---------------------------------
            for _ in range(closes):
                if self._scopes:
                    popped = self._scopes.pop()
                    if popped.kind == "function" and popped.uses_oracle:
                        self._check_oracle(popped, result, f)
                    if popped.kind == "function" and popped.eth_call_line:
                        self._report_reentrancy_vector(popped, result, f)
                    if popped is self._current_func:
                        self._current_func = None
                        self._sweep_vars.clear()
            if not self._scopes:
                self._current_func = None
                self._sweep_vars.clear()

            opens = line.count("{")
            opened = 0

            # --- try to open contract-level scope -----------------------------
            cm = self._match_contract(line)
            if cm and opens > 0:
                kind, name = cm
                if kind in ("contract", "library", "interface", "abstract"):
                    storage = set(storage_by_contract.get(name, set()))
                    storage |= project_storage
                    self._scopes.append(SolidScope(kind, name, storage, i))
                else:  # struct/enum -> plain block scope marker
                    self._scopes.append(SolidScope(kind, None, set(), i))
                opened += 1

            # --- track a multi-line function header keyword line ---------------
            fm = self._match_func(line)
            if fm and ";" not in line:
                # start (or restart) accumulating the full multiline signature so
                # modifiers like nonReentrant are visible to the guard detector
                self._pending_func = " " + line.strip()
            elif self._pending_func and ";" not in line:
                self._pending_func += " " + line.strip()
            elif ";" in line and self._pending_func and opens == 0:
                # interface-style declaration terminated by ';' -> not a body
                self._pending_func = None

            # --- try to open function/modifier scope --------------------------
            if opens > opened and any(sc.kind in ("contract", "library") for sc in self._scopes):
                header = fm or self._pending_func
                if header:
                    owner = None
                    storage = set()
                    for sc in reversed(self._scopes):
                        if sc.kind in ("contract", "library"):
                            owner = sc.owner
                            storage = sc.storage
                            break
                    guard = any(g in header.lower() for g in _REENTRANCY_GUARD_MODS)
                    new_scope = SolidScope("function", owner, storage, i, guard)
                    self._scopes.append(new_scope)
                    self._current_func = new_scope
                    self._pending_func = None
                    opened += 1

            # --- every other '{' keeps the brace stack balanced ---------------
            while opened < opens:
                self._scopes.append(SolidScope("block", None, set(), i))
                opened += 1

    # ------------------------------------------------------------------
    def _collect_storage_decls(self, lines: list) -> dict:
        contracts = {}
        cur = None
        depth = 0
        in_func = False      # inside a function signature/body
        ever_opened = False  # saw the function's own '{'
        fn_scope = 0         # brace balance local to the current function
        for raw in lines:
            line = self._strip_comment(raw).strip()
            cm = self._match_contract(line)
            if cm and cm[0] in ("contract", "library", "abstract"):
                if cur:
                    depth = 0
                cur = cm[1]
                contracts.setdefault(cur, set())
                depth += line.count("{") - line.count("}")
                in_func = False
                ever_opened = False
                fn_scope = 0
                continue
            if cur:
                if not in_func:
                    if self._match_func(line):
                        in_func = True
                        ever_opened = False
                        fn_scope = 0
                        fn_scope += line.count("{") - line.count("}")
                        if fn_scope > 0:
                            ever_opened = True
                    elif depth == 1:
                        for m in _STORAGE_DECL_RE.finditer(line):
                            contracts[cur].add(m.group("name"))
                else:
                    fn_scope += line.count("{") - line.count("}")
                    if fn_scope > 0:
                        ever_opened = True
                    if ever_opened and fn_scope <= 0:
                        in_func = False
                depth += line.count("{") - line.count("}")
                if depth <= 0:
                    cur = None
        return contracts

    @staticmethod
    def _match_contract(line: str):
        m = re.match(r"^(abstract\s+)?(contract|library|interface|struct|enum)\s+([A-Za-z_][A-Za-z0-9_]*)", line)
        if m:
            kind = m.group(2)
            if m.group(1):
                kind = "abstract"
            return kind, m.group(3)
        return None

    @staticmethod
    def _match_func(line: str):
        # 'keyword(' may appear without a space (constructor(/receive())
        if re.match(r"^\s*(function|modifier|constructor)\s*[^;{]*\{", line):
            return line.split("{")[0]
        m = re.match(r"^\s*(?:(?:function|modifier)\s+|\s*constructor\s*\()", line)
        if m:
            return m.group(0).strip()
        if re.match(r"^\s*(?:function|modifier|constructor)\s*\(", line):
            return line.split("(")[0]
        return None

    # ------------------------------------------------------------------
    def _track_line(self, sc, line, line_no, result, f):
        # Track oracle-sanity guards inside the current function.
        if _ORACLE_READ_RE.search(line):
            sc.uses_oracle = True
            if sc.oracle_read_line == 0:
                sc.oracle_read_line = line_no
            if not sc.oracle_price_vars:
                # The signed price variable is often declared several lines above
                # the actual latestRoundData() call (multi-line tuple destructuring).
                lo = max(sc.line - 1, line_no - 14)
                for prev in self._file_lines[lo:line_no]:
                    m = re.search(r"\bint(?:256|128|64)\s+([A-Za-z_][A-Za-z0-9_]*)", prev)
                    if m:
                        sc.oracle_price_vars.add(m.group(1))
            m = re.search(r"\bint(?:256|128|64)\s+([A-Za-z_][A-Za-z0-9_]*)", line)
            if m:
                sc.oracle_price_vars.add(m.group(1))
        elif sc.uses_oracle:
            if not sc.oracle_price_checked:
                if self._matches_oracle_pos_check(line, sc.oracle_price_vars):
                    sc.oracle_price_checked = True
            if not sc.oracle_fresh_checked and _ORACLE_FRESH_RE.search(line):
                sc.oracle_fresh_checked = True
            if not sc.oracle_price_casted and sc.oracle_price_vars:
                for var in sc.oracle_price_vars:
                    if re.search(
                        rf"\buint(?:256|128|64)\s*\(\s*{re.escape(var)}\s*\)",
                        line,
                        re.IGNORECASE,
                    ):
                        sc.oracle_price_casted = True
                        break

        call_kind = None
        if _DELEGATECALL_RE.search(line):
            call_kind = "delegatecall"
        elif _CALL_RE.search(line):
            call_kind = "call"
        elif _TYPECAST_CALL_RE.search(line):
            call_kind = "interface"
        elif _STATICCALL_RE.search(line):
            call_kind = "staticcall"
        elif _TRANSFER_RE.search(line):
            call_kind = "transfer"

        # --- Sweep-all detector: transfers of the FULL contract balance -------------

        if call_kind:
            method = None
            if call_kind == "interface":
                m = _TYPECAST_CALL_RE.search(line)
                if m:
                    method = m.group(0).rsplit(".", 1)[-1].strip().rstrip("(").strip()
            sc.calls.append((line_no, call_kind, method))
            if call_kind in ("call", "delegatecall") and not self._call_result_captured(line):
                self._add_bug(
                    result, f, line_no, "medium", "security",
                    "Unchecked Low-Level Call Result",
                    "Low-level .call/.delegatecall return value is not captured; failures are silently ignored.",
                    "Capture the return value: (bool success, ...) = target.call(...); then verify success.",
                    0.6,
                )
            if call_kind == "call" and re.search(r"\.call\s*\{", line):
                if sc.guard:
                    self._add_bug(
                        result, f, line_no, "info", "security",
                        "Reentrancy Vector (External Call with Value, Guard Present)",
                        "External .call{{value:...}} detected at line {}. The enclosing function carries a "
                        "reentrancy-guard modifier, so re-entering this function is blocked; flag kept for "
                        "review only (state writes before/after the call are not re-entrant here).".format(line_no),
                        "Verify the guard actually precedes the call and that no cross-function re-entry path exists.",
                        0.25,
                    )
                elif sc.eth_call_line == 0:
                    # Defer: only a HIGH if a storage write happens AFTER this call.
                    sc.eth_call_line = line_no

        # Storage writes
        storage = sc.storage
        if storage:
            # Quick pre-filter: only lines containing '=' or '++' or '--' can be writes
            if "=" in line or "++" in line or "--" in line:
                for name in storage:
                    if self._is_storage_write(line, name):
                        if sc.eth_call_line and line_no > sc.eth_call_line:
                            sc.write_after_eth = True
                        self._check_cei(sc, name, line_no, result, f)

    def _report_reentrancy_vector(self, sc, result, f):
        if sc.write_after_eth:
            self._add_bug(
                result, f, sc.eth_call_line, "high", "security",
                "Reentrancy Vector (External Call with Value)",
                f"External .call{{value:...}} at line {sc.eth_call_line} is followed by a storage write, "
                "so an attacker-controlled callee can re-enter the contract before state is finalised "
                "and corrupt accounting.",
                "Follow checks-effects-interactions: update state before external calls, or use a "
                "reentrancy guard.",
                0.55,
            )
        else:
            self._add_bug(
                result, f, sc.eth_call_line, "info", "security",
                "Reentrancy Vector (External Call with Value, CEI Respected)",
                f"External .call{{value:...}} at line {sc.eth_call_line} has no storage write after it, "
                "so the checks-effects-interactions pattern effectively prevents reentrant state "
                "corruption; flag kept for review only.",
                "Verify no cross-function re-entry path or later setter can be reached via the callee.",
                0.2,
            )

    def _is_storage_write(self, line, name) -> bool:
        rx = self._write_re_cache.get(name)
        if rx is None:
            rx = re.compile(r"\b" + re.escape(name) + r"\s*(?:[+\-*/]?=|\+\+|--)")
            self._write_re_cache[name] = rx
        if not rx.search(line):
            return False
        if re.search(r"\bas\b|\bemit\b|require\s*\(|\breturn\b", line):
            return False
        return True

    @staticmethod
    def _is_read_only_call(call_entry) -> bool:
        """Heuristic: interface method names that are almost certainly `view`
        getters cannot re-enter the caller, so CEI does not apply."""
        if call_entry[1] in ("staticcall", "transfer"):
            return True
        if call_entry[1] != "interface" or len(call_entry) < 3 or not call_entry[2]:
            return False
        name = call_entry[2]
        lowered = name.lower()
        if lowered in ("balanceof", "allowance", "stakeof", "userstake", "totalstaked",
                       "totalsupply", "getstakeatepoch", "getstake", "getbalance", "peek"):
            return True
        return lowered.startswith(("get", "is", "has", "read", "peek", "view", "total", "balance"))

    def _check_cei(self, sc, name, line_no, result, f):
        if not sc.calls:
            return
        last = sc.calls[-1]
        if line_no <= last[0]:
            return
        if sc.guard:
            sev, conf, note = "info", 0.2, " (guard present, likely safe)"
        elif self._is_read_only_call(last) or last[1] == "staticcall":
            # external view/static reads cannot hold the caller's execution hostage
            # for state mutation; flag at info for manual sanity only
            sev, conf, note = "info", 0.15, " (external call is a view/static read; re-entry unlikely)"
        elif last[1] in ("call", "delegatecall", "interface"):
            sev, conf, note = "high", 0.45, ""
        else:
            sev, conf, note = "medium", 0.4, ""
        self._add_bug(
            result, f, line_no, sev, "logic",
            "State Change After External Call (CEI Violation)",
            f"State variable '{name}' is modified at line {line_no}, after an external call at line {last[0]}. "
            f"An attacker-controlled contract may re-enter before this write.{note}",
            "Move the state update before the external call, or apply a reentrancy guard.",
            conf,
        )

    def _check_oracle(self, sc, result, f):
        """Report missing sanity checks around a Chainlink latestRoundData() read.

        - No price > 0 guard: a negative/zero int256 price is cast to uint256 and
          wraps to a huge number -> buyer receives the whole token pool / pays nothing.
        - No staleness guard: a frozen feed silently prices trades at an outdated rate.
        """
        if not sc.uses_oracle:
            return
        if sc.oracle_price_checked and sc.oracle_fresh_checked:
            return
        if not sc.oracle_price_checked and sc.oracle_price_casted:
            self._add_bug(
                result, f, sc.oracle_read_line, "high", "oracle",
                "Oracle Price Missing Positive Check",
                (
                    f"latestRoundData() at line {sc.oracle_read_line} reads a signed int256 price "
                    "that is cast to uint256 WITHOUT a price > 0 guard. If the feed ever returns "
                    "a negative value (feed governor compromise, aggregator malfunction, or a "
                    "manipulated L2 sequencer feed), uint256(price) wraps to a huge number: a buyer "
                    "then receives an enormous amount of tokens for a tiny payment, draining the "
                    "entire sale supply. validate price <= 0 and staleness before use."
                ),
                "Add `if (price <= 0) revert();` before any uint256(price) cast, and check "
                "round completeness + updatedAt freshness.",
                0.65,
            )
            return
        if not sc.oracle_fresh_checked:
            self._add_bug(
                result, f, sc.oracle_read_line, "medium", "oracle",
                "Oracle Price Missing Staleness Check",
                (
                    f"latestRoundData() at line {sc.oracle_read_line} has no updatedAt/staleness "
                    "guard. A stopped or delayed feed keeps returning the last price, letting trades "
                    "execute at a stale rate advantageously to one side."
                ),
                "Revert when block.timestamp - updatedAt exceeds the feed heartbeat threshold "
                "and when answeredInRound < roundId.",
                0.4,
            )

    @staticmethod
    def _matches_oracle_pos_check(line: str, price_vars: set) -> bool:
        """True if `line` guards any tracked price variable for positive value,
        e.g. `require(ans > 0)`, `if (price <= 0) revert`, `assert(answer != 0)`."""
        lowered = line.lower()
        if _ORACLE_POS_CHECK_RE.search(line):
            return True
        if not price_vars:
            return False
        for var in price_vars:
            if re.search(
                rf"\b{re.escape(var)}\s*(?:<=|<|==|>|>=|!=)\s*0\b",
                line,
                re.IGNORECASE,
            ):
                return True
            if re.search(
                rf"\b(?:require|if|assert)\s*\([^)]*\b{re.escape(var)}\b[^)]*\)",
                lowered,
            ):
                # only counts if it actually compares the var to 0
                body = re.search(
                    rf"\(([^)]*)\)", re.search(
                        rf"\b(?:require|if|assert)\s*\([^)]*\b{re.escape(var)}\b[^)]*\)",
                        lowered,
                    ).group(0)
                ).group(1)
                if re.search(rf"\b{re.escape(var)}\s*(?:<=|<|==|>|>=|!=)\s*0\b", body):
                    return True
        return False

    @staticmethod
    def _call_result_captured(line: str) -> bool:
        if "=" in line:
            lhs = line.split("=")[0]
            if re.search(r"\([^)]*(bool|success)[^)]*\)", lhs):
                return True
        return False

    # ------------------------------------------------------------------
    # Sweep-all detector: a payout that sends the ENTIRE contract balance
    # (or full balanceOf(this) of an ERC20) instead of the caller's exact
    # entitlement. This is a judge-confirmed High/Critical class.
    # ------------------------------------------------------------------
    _SWEEP_SENDERS = re.compile(
        r"address\(this\)\.balance|\.balance\s*;|balanceOf\s*\(address\s*\(this\)\)|totalBalance|contractBalance",
        re.IGNORECASE,
    )
    _SWEEP_TRANSFER_CALL = re.compile(
        r"(?:safeTransferETH|safeTransfer\s*\([^,]+,\s*|\.transfer\s*\(|\.call\s*\{[^}]*value\s*[:=]\s*|send\s*\()"
        r"[^;]*",
        re.IGNORECASE,
    )
    # (?:uint256|...)?  var = address(this).balance   or   var = token.balanceOf(address(this))
    _SWEEP_ASSIGN = re.compile(
        r"^\s*(?:(?:u?int\d+|bool|address)\s+)?(?P<var>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*"
        r"(?P<src>address\s*\(\s*this\s*\)\s*\.\s*balance|[A-Za-z_][A-Za-z0-9_]*\.\s*balanceOf\s*\(\s*address\s*\(\s*this\s*\)\s*\))",
        re.IGNORECASE,
    )

    def _match_sweep_assignment(self, line: str):
        m = self._SWEEP_ASSIGN.search(line)
        if not m:
            return None
        src = re.sub(r"\s+", "", m.group("src").lower())
        is_native = "this).balance" in src
        return m.group("var"), is_native

    def _check_sweep(self, line: str, line_no: int, result, f):
        # ---- Case A: transfer / payout target is a var that holds a full-balance
        #      snapshot taken earlier in the SAME function (multi-line correlation).
        tm = re.search(
            r"(?:safeTransferETH|\.transfer\s*\(|\.call\s*\{[^}]*value\s*[:=]\s*|send\s*\()\s*"
            r"(?P<var>[A-Za-z_][A-Za-z0-9_]*)\b",
            line,
            re.IGNORECASE,
        )
        if tm:
            var = tm.group("var")
            if var in self._sweep_vars and self._current_func is not None:
                snap_line, is_native = self._sweep_vars[var]
                self._add_sweep_bug(
                    result, f, line_no,
                    "high" if is_native else "high",
                    "Full-Balance Sweep in Payout",
                    (
                        f"A payout at line {line_no} sends the full {('native' if is_native else 'token')} "
                        f"balance captured at line {snap_line} instead of the caller's exact entitlement. "
                        f"Any caller that reaches this path drains everything parked in the contract "
                        f"(other users' funds, fees, escrow). Confirmed High/Critical audit class."
                    ),
                    "Pay the caller's exact tracked entitlement; never send address(this).balance "
                    "or balanceOf(address(this)) (directly or via a cached local).",
                    0.85,
                )
                self._sweep_vars.pop(var, None)
                return

        # ---- Case B: transfer / payout line references the full balance inline --.
        if not SolidityAnalyzer._SWEEP_TRANSFER_CALL.search(line):
            return
        if not SolidityAnalyzer._SWEEP_SENDERS.search(line):
            return

        lowered = line.lower()
        if "address(this).balance" in lowered or "balanceof(address(this))" in lowered:
            self._add_sweep_bug(
                result, f, line_no, "high",
                "Full-Balance Sweep in Payout",
                (
                    "A payout path sends the full contract balance instead of the exact amount owed. "
                    "If the contract holds other users' funds or uncollected fees, any caller triggers "
                    "this path and drains everything parked in the contract. Confirmed High/Critical audit class."
                ),
                "Pay the caller's exact tracked entitlement; never use address(this).balance or "
                "balanceOf(address(this)) as the payout amount.",
                0.8,
            )
        else:
            self._add_sweep_bug(
                result, f, line_no, "medium",
                "Suspicious Full-Balance Payout",
                (
                    "A payout references the contract's total balance. Verify the amount is the caller's "
                    "exact entitlement and not the full pooled balance."
                ),
                "Track per-user balances and pay exactly what is owed.",
                0.55,
            )

    def _add_sweep_bug(self, result, f, line, sev, title, desc, sug, conf):
        self._add_bug(result, f, line, sev, "accounting", title, desc, sug, conf)

    # ------------------------------------------------------------------
    def _add_bug(self, result, f, line, sev, category, title, desc, sug, conf):
        snippet = self._get_snippet(f.content.split("\n"), line - 1)
        result.add(Bug(
            file=str(f.relative_path),
            line=line,
            column=0,
            severity=sev,
            category=category,
            title=title,
            description=desc,
            suggestion=sug,
            code_snippet=snippet,
            analyzer=self.name,
            confidence=conf,
        ))

    @staticmethod
    def _get_snippet(lines: list[str], index: int, context: int = 2) -> str:
        start = max(0, index - context)
        end = min(len(lines), index + context + 1)
        out = []
        for i in range(start, end):
            marker = ">>>" if i == index else "   "
            out.append(f"{marker} {i + 1:4d} | {lines[i]}")
        return "\n".join(out)