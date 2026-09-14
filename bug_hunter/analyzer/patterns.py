"""Knowledge base of high-value vulnerability patterns distilled from completed
competitive audit contests (CodeHawks / Code4rena / Cantina / Sherlock).

The goal is in-context learning: instead of fine-tuning the model weights, we
inject real, judge-confirmed finding classes into the prompt so the model
recognises attack surfaces that actually pay, and rejects classes judges
routinely dismiss.
"""

# ---------------------------------------------------------------------------
# High-value patterns: classes of findings that repeatedly win High/Critical
# in real contests. Each entry teaches the model how a judge would recognise
# and price the issue.
# ---------------------------------------------------------------------------
KNOWN_HIGH_VALUE_PATTERNS = [
    {
        "name": "full-balance sweep / refund-all",
        "root_cause": "A user-facing refund or payout that sends balanceOf(this) or address(this).balance instead of the exact amount the caller is owed",
        "impact": "A crafted call drains native tokens or ERC20s cubated in the contract that belong to the protocol (fees, escrow, other users)",
        "judge_test": "Can the caller recover more than they deposited by triggering a refund path while other value is parked in the contract?",
        "in_scope": True,
    },
    {
        "name": "share / receipt token rounding in favour of the caller",
        "root_cause": "Minting or withdrawing proportional value with a direction of rounding (floor/ceil) that can be called repeatedly to extract value",
        "impact": "Slow or fast drain of the vault value as shares are minted/burned at a stale or rounded price",
        "judge_test": "Can repeated deposit/withdraw cycles net-gain funds when amounts are small? Is the invariant totalAssets == sum(share*price)?",
        "in_scope": True,
    },
    {
        "name": "stale / manipulable accounting snapshot",
        "root_cause": "State (liquidity, price, balances) snapshotted at deposit and reused for later pricing or settlement without re-validation",
        "impact": "Under-collateralised positions pass health checks, liquidation claims wrong amounts, or a third party changes the underlying snapshot",
        "judge_test": "Can an external actor change the assumed invariant between snapshot and use, and does that change attack value?",
        "in_scope": True,
    },
    {
        "name": "index / counter wrap arithmetic",
        "root_cause": "Truncated time or index arithmetic (e.g. epoch = (block.timestamp >> 6) & 0xFFFFFF, uint16/uint24 cast) causing periodic wrap",
        "impact": "Periodic epoch/period collisions change timing assumptions, rewards, or liquidation windows",
        "judge_test": "Does the arithmetic width wrap within reachable time/use and does a wrap flip a core decision?",
        "in_scope": True,
    },
    {
        "name": "liquidation / auction math error at edge sizes",
        "root_cause": "Reward or penalty calculations that use a floor or weight unbounded by the actual debt for very small positions",
        "impact": "Liquidators profit beyond intended cap or a small-dust account gets drained past the intended penalty",
        "judge_test": "For the smallest eligible position, is the extracted reward still within the documented total-penalty bound?",
        "in_scope": True,
    },
    {
        "name": "missing fee-on-transfer / rebasing handling",
        "root_cause": "Accounting assumes standard ERC20 transfer semantics (exact amount in/out) while the asset is fee-on-transfer or rebasing",
        "impact": "Protocol receives less than recorded credit, or withdrawals accounting mismatches the real received amount",
        "judge_test": "Is the token whitelisted as collateral/payout while its real transfer semantics differ from the accounting model?",
        "in_scope": True,
    },
    {
        "name": "array-length desync between parallel inputs",
        "root_cause": "Multiple input arrays (addresses/ids/amounts) iterated with different semantics or not checked to same length",
        "impact": "Asset credited/borrowed mismatches the recorded entry, phantom balances, or out-of-bounds reads",
        "judge_test": "Can the caller supply arrays of different lengths and cause credit without deposit / withdraw of unowned value?",
        "in_scope": True,
    },
    {
        "name": "approval / allowance persists after asset transfer",
        "root_cause": "ERC20 or NFT allowance not cleared when the underlying asset moves to a new owner, keeping spend rights on the old owner",
        "impact": "Old owner or a third party spends the moved asset",
        "judge_test": "After a legitimate ownership transfer, does any approval still grant spending power to a party that should lose it?",
        "in_scope": True,
    },
    {
        "name": "integer overflow / underflow not covered by compiler version",
        "root_cause": "Checked-arithmetic bypass: arithmetic inside unchecked{} blocks or with casts that truncate (uint256->uint128) losing value",
        "impact": "Balances or accounting wrap to attacker advantage",
        "judge_test": "Is the truncation reachable with attacker-controlled inputs and does it flip a check the protocol relies on?",
        "in_scope": True,
    },
    {
        "name": "reentrancy with economic impact",
        "root_cause": "State updated after an external call where the callback lets the attacker make repeated profitable operations before the write",
        "impact": "Attacker reads stale state during callback to extract more value than a single entry would allow",
        "judge_test": "CEI alone is a root cause: show the concrete extra extraction enabled by the stale read, not just the ordering",
        "in_scope": True,
    },
    {
        "name": "wrong owner / signer check",
        "root_cause": "Signature or ownership validation checks the wrong party (e.g. owner of the token vs msg.sender, or a stale authorization entry)",
        "impact": "Unauthorized transfer, withdraw, or action on behalf of a user",
        "judge_test": "Can an address that never legitimately owned/authorised the asset still trigger the privileged path?",
        "in_scope": True,
    },
    {
        "name": "preview/prediction used as settlement value",
        "root_cause": "A view/preview function returning an estimate is used for final accounting or payout rather than a realised value",
        "impact": "Attacker manipulates the preview to settle at a wrong price",
        "judge_test": "Is an estimate ever trusted for a value transfer, and can the input to that estimate be skewed by the attacker?",
        "in_scope": True,
    },
]

# ---------------------------------------------------------------------------
# Rules judges routinely use to dismiss / downgrade submissions. Every
# candidate must be filtered through these before being reported as High/Critical.
# ---------------------------------------------------------------------------
OUT_OF_SCOPE_RULES = [
    {
        "rule": "Trusted-role / admin / governance action",
        "test": "Requires the admin, owner, guardian, keeper, or risk manager to act / be compromised. Centralisation risk is not in-scope by default.",
    },
    {
        "rule": "Trusted third-party oracle",
        "test": "Requires Chainlink oracle / sequencer feed or a trusted integration (e.g. CoW solver) to misbehave or be manipulated.",
    },
    {
        "rule": "Recoverable / reversible loss",
        "test": "Funds can be recovered by admin rescue, timelock, pause, or reversion. Recoverable is never Critical.",
    },
    {
        "rule": "Theoretical / no demonstrated impact",
        "test": "No concrete path shown to actual fund loss or invariant break. Class-level observation is not impact.",
    },
    {
        "rule": "Exposure caps / risk limits",
        "test": "maxExposure / concentration limits miscounting without realised loss is a risk control, not a solvency invariant.",
    },
    {
        "rule": "Documented design behaviour",
        "test": "The mechanism operating as designed (frozen valuation, intended loss absorption, documented rounding) is not a vulnerability.",
    },
    {
        "rule": "Gas / style / optimisations",
        "test": "Gas optimisations, style violations, redundant code, and best-practice nits are never High/Critical.",
    },
]


def pattern_hints(compact: bool = False) -> str:
    """Render the pattern knowledge as a prompt block.

    compact=True produces a terse keyword list suitable for small local models
    so the model does not drown in prose and forgets the actual task.
    """
    if compact:
        lines = ["HIGH-VALUE BUG CLASSES (map code to these):"]
        for p in KNOWN_HIGH_VALUE_PATTERNS:
            lines.append(
                f"- {p['name']}: {p['root_cause']} -> {p['impact']}. Judge test: {p['judge_test']}"
            )
        lines.append("")
        lines.append("DOWNGRADE / REJECT IF:")
        for r in OUT_OF_SCOPE_RULES:
            lines.append(f"- {r['rule']} ({r['test']})")
        lines.append("")
        lines.append("Report ONLY findings with a concrete irreversible loss of funds or a broken core invariant.")
        return "\n".join(lines)

    lines = ["HIGH-VALUE BUG CLASSES THAT ACTUALLY PAY (learn these):"]
    for p in KNOWN_HIGH_VALUE_PATTERNS:
        lines.append(
            f"- {p['name']}:\n"
            f"    root cause: {p['root_cause']}\n"
            f"    impact: {p['impact']}\n"
            f"    how a judge checks it: {p['judge_test']}"
        )
    lines.append("")
    lines.append("WAYS JUDGES DISMISS / DOWNGRADE SUBMISSIONS (apply all of these to every candidate):")
    for r in OUT_OF_SCOPE_RULES:
        lines.append(f"- {r['rule']}: {r['test']}")
    return "\n".join(lines)


def validate_severity(severity: str, description: str, title: str) -> str:
    """Conservative, rule-based severity adjustment after the model's own call.

    Deliberately conservative: we only *downgrade* high/critical when there is a
    strong, specific signal (an explicit trusted-role/rescue statement or an
    explicitly theoretical hedge). Generic keywords touching the title/description
    are NOT enough, to avoid the classifier low-balling a real finding. We never
    upgrade.
    """
    text = f"{title} {description}".lower()

    # Strong markers that unambiguously signal an out-of-scope finding.
    # These are phrases a reporter would only write if the issue truly depends
    # on trust/centralisation/recovery — not words that merely co-occur (e.g.
    # "owner" can legitimately appear in a real reentrancy write-up).
    strong_trusted = [
        "onlyowner", "requires the admin", "requires admin", "requires the owner",
        "requires owner", "requires a trusted actor", "requires the keeper",
        "requires governance", "requires the multisig", "centralisation risk",
        "centralization risk", "relies on the admin", "trusted role is required",
        "can only be exploited by the admin",
    ]
    strong_recovered = [
        "recoverab", "reversible", "admin can rescue", "can be rescued",
        "pausable and recoverable", "timelock allows recovery",
    ]
    strong_theory = [
        "purely theoretical", "theoretical only", "no poc", "without a proof",
        "no concrete path", "in theory only", "strictly theoretical",
        "unproven assumption", "under conditions that cannot occur",
    ]

    if severity in ("critical", "high"):
        if any(m in text for m in strong_trusted):
            severity = "low"
        elif any(m in text for m in strong_recovered):
            severity = "low"
        elif any(m in text for m in strong_theory):
            severity = "medium"
        # generic reentrancy with no demonstrated loss path -> downgrade to medium
        if "reentran" in text and "loss" not in text and "drain" not in text \
                and "steal" not in text and "extract" not in text and "sweep" not in text:
            severity = "medium"
    elif severity == "medium":
        # Only drop a medium on an explicit trust signal; never on broad keywords.
        if any(m in text for m in strong_trusted):
            severity = "low"
    return severity