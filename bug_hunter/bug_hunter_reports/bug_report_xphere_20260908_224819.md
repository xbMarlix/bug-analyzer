# BugHunter Report: xphere

**Generated:** 2026-09-08 22:48:19
**Project:** `C:\Users\123123\AppData\Local\Temp\opencode\xphere`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 29 |
| Total lines | 8,507 |
| Bugs found | 54 |
| !! High | 32 |
| ! Medium | 1 |
| ~ Low | 16 |
| i Info | 5 |

### Languages Detected

- **javascript**: 8 files
- **bash**: 7 files
- **solidity**: 6 files
- **html**: 6 files
- **python**: 1 files
- **css**: 1 files

## Security (31)

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:185`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     183 |       const rl = $('[data-metric="burnRate"]');
     184 |       if (rl)
>>>  185 |         rl.innerHTML =
     186 |           accrued >= cap
     187 |             ? `today's burn fully accrued — <b>waiting for the settlement</b> 🔥`
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:231`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     229 |       const s = burnNextTs - Math.floor(Date.now() / 1000);
     230 |       if (s <= 0) {
>>>  231 |         el.innerHTML = `🔥 settling now…`;
     232 |         return;
     233 |       }
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:237`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     235 |       const m = String(Math.floor((s % 3600) / 60)).padStart(2, "0");
     236 |       const sec = String(s % 60).padStart(2, "0");
>>>  237 |       el.innerHTML = `burns in <b>${h}:${m}:${sec}</b> 🔥`;
     238 |     }, 1000);
     239 |   }
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:339`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     337 |         burnAnchorTs = Number(lastS.settledAt);
     338 |         const rl = $('[data-metric="burnRate"]');
>>>  339 |         if (rl) rl.innerHTML = `burning <b>\u2248${burnRatePerSec.toFixed(5)} XP</b> every second, right now`;
     340 |       }
     341 |       renderMetrics({
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:927`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     925 |   async function renderRequests(vault, ids) {
     926 |     const box = $("#requestList");
>>>  927 |     box.innerHTML = "";
     928 |     for (const id of ids) {
     929 |       try {
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:941`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     939 |         el.className = "req";
     940 |         const when = new Date(Number(r.claimableAt) * 1000);
>>>  941 |         el.innerHTML = `<div class="req-top"><span>#${id} · ${fmtXP(r.assets)} XP</span>
     942 |           <span class="${ready ? "ready" : "wait"}">${
     943 |             ready ? "ready to claim ✓" : `D-${daysLeft} · matures ${when.toLocaleDateString()}`
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\app.js:1166`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
    1164 |       ["WXP", CFG.contracts.wxp],
    1165 |     ].filter(([, a]) => a && a !== ZERO);
>>> 1166 |     box.innerHTML =
    1167 |       items
    1168 |         .map(
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\burn.js:57`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      55 |         rate = (fe(lastS.totalAmount) * burnShare) / 86400;
      56 |         anchor = Number(lastS.settledAt);
>>>   57 |         $("rateLine").innerHTML = `growing <b>≈${rate.toFixed(5)} XP</b> every second`;
      58 |       }
      59 |       if (burnAddr) $("burnAddrLink").href = `${CFG.chain.blockExplorerUrl}/address/${burnAddr}`;
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\burn.js:70`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      68 |     const cap = rate * 86400;
      69 |     const accrued = Math.min(rate * elapsed, cap);
>>>   70 |     $("rateLine").innerHTML =
      71 |       accrued >= cap
      72 |         ? "today's burn fully accrued — <b>waiting for the settlement</b> 🔥"
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\burn.js:104`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     102 |     const log = $("log");
     103 |     if (!days.length) {
>>>  104 |       chart.innerHTML = '<span class="chart-empty">history will appear after the next settlement</span>';
     105 |       log.innerHTML = '<div class="row"><span class="d">—</span><span class="note">no settlements recorded yet</span></div>';
     106 |       return;
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\burn.js:105`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     103 |     if (!days.length) {
     104 |       chart.innerHTML = '<span class="chart-empty">history will appear after the next settlement</span>';
>>>  105 |       log.innerHTML = '<div class="row"><span class="d">—</span><span class="note">no settlements recorded yet</span></div>';
     106 |       return;
     107 |     }
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\burn.js:110`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     108 |     const recent = days.slice(-30);
     109 |     const max = Math.max(...recent.map((d) => d.burned), 1);
>>>  110 |     chart.innerHTML = recent
     111 |       .map((d) => {
     112 |         const h = Math.max(2, (d.burned / max) * 100);
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\burn.js:120`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     118 |       })
     119 |       .join("");
>>>  120 |     log.innerHTML = [...recent]
     121 |       .reverse()
     122 |       .map(
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\partners.js:38`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      36 |         .sort((a, b) => b.tvl - a.tvl);
      37 |       const maxT = Math.max(...rows.map((r) => r.tvl), 1e-9);
>>>   38 |       document.getElementById("rows").innerHTML = rows
      39 |         .map(
      40 |           (r) => `<div class="b-row">
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:157`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     155 |         ? '<span class="pill warn">DUE</span>'
     156 |         : '<span class="pill ok">ON SCHEDULE</span>';
>>>  157 |     $("components").innerHTML = `
     158 |       <div class="comp"><span class="name">Vault solvency</span><span class="spacer"></span>
     159 |         <span class="desc">surplus ${solvent ? fn(fe(held - oblig)) : "—"} XP</span>
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:171`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     169 | 
     170 |     // ── metrics ──
>>>  171 |     $("metrics").innerHTML =
     172 |       card("Total value locked", `${fn(fe(tvl))} <small>XP</small>`, "", `${fn(utilization, 2)}% of ${fn(fe(cap), 0)} XP cap`) +
     173 |       card("Staking APR", stakingApr !== null ? stakingApr.toFixed(2) + " <small>%</small>" : "—", "",
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:188`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     186 |     $("pBarOwe").style.width = (obligN / maxN) * 100 + "%";
     187 |     $("proof").className = "proof" + (solvent ? "" : " bad");
>>>  188 |     $("pVerdict").innerHTML = solvent
     189 |       ? `<b class="ok">✓ SOLVENT</b> — holdings cover obligations with ${fn(holdN - obligN)} XP to spare`
     190 |       : `<b class="bad">✗ CHECK FAILED</b> — holdings below obligations`;
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:195`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     193 |     if (lastS && Number(lastS.settledAt) > 0) {
     194 |       const when = new Date(Number(lastS.settledAt) * 1000);
>>>  195 |       $("lastSettle").innerHTML =
     196 |         card("Settled at", when.toISOString().slice(0, 16).replace("T", " ") + " <small>UTC</small>") +
     197 |         card("Amount settled", `${fn(fe(lastS.totalAmount))} <small>XP</small>`) +
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:201`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     199 |         card("To stakers", `${fn(fe(lastS.distributed))} <small>XP</small>`, "ok");
     200 |     } else {
>>>  201 |       $("lastSettle").innerHTML = card("Settled at", "—", "", "no settlement yet");
     202 |     }
     203 | 
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:205`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     203 | 
     204 |     // ── parameters ──
>>>  205 |     $("params").innerHTML =
     206 |       kv("Stake cap", fn(fe(cap), 0) + " XP") +
     207 |       kv("Unstake cooldown", dur(cooldown)) +
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\status.js:240`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     238 |       /* role reads unavailable — links above still render */
     239 |     }
>>>  240 |     $("gov").innerHTML = rows.join("");
     241 | 
     242 |     $("footLeft").textContent =
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\zigap.js:70`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
      68 |     overlay.className = "zg-overlay";
      69 |     overlay.hidden = true;
>>>   70 |     overlay.innerHTML = `
      71 |       <div class="zg-card">
      72 |         <div class="zg-head"><b id="zgTitle"><img class="zg-logo" src="assets/brand/zigap_symbol.svg" alt="" />ZIGAP</b>
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\zigap.js:106`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     104 |     ensureOverlay();
     105 |     overlay.hidden = false;
>>>  106 |     overlay.querySelector("#zgTitle").innerHTML =
     107 |       '<img class="zg-logo" src="assets/brand/zigap_symbol.svg" alt="" />' + title;
     108 |     overlay.querySelector("#zgNote").innerHTML = note;
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\zigap.js:108`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     106 |     overlay.querySelector("#zgTitle").innerHTML =
     107 |       '<img class="zg-logo" src="assets/brand/zigap_symbol.svg" alt="" />' + title;
>>>  108 |     overlay.querySelector("#zgNote").innerHTML = note;
     109 |     const mountEl = overlay.querySelector("#zgMount");
     110 |     mountEl.innerHTML = '<span class="zg-loading">loading ZIGAP…</span>';
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\zigap.js:110`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     108 |     overlay.querySelector("#zgNote").innerHTML = note;
     109 |     const mountEl = overlay.querySelector("#zgMount");
>>>  110 |     mountEl.innerHTML = '<span class="zg-loading">loading ZIGAP…</span>';
     111 |     const { createRoot } = await loadLibs();
     112 |     return new Promise((resolve, reject) => {
```
</details>

---

### [!!] Possible XSS Vulnerability

- **File:** `web\zigap.js:114`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct HTML injection detected. User-controlled data may be executed as HTML/JS.

**Fix:** Sanitize input or use textContent/innerText instead of innerHTML.

<details>
<summary>Code</summary>

```
     112 |     return new Promise((resolve, reject) => {
     113 |       rejectOpen = reject;
>>>  114 |       mountEl.innerHTML = "";
     115 |       root = createRoot(mountEl);
     116 |       root.render(makeElement(resolve));
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, Guard Present)

- **File:** `src\PartnerCommissionDistributor.sol:201`
- **Severity:** INFO
- **Confidence:** 25%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} detected at line 201. The enclosing function carries a reentrancy-guard modifier, so re-entering this function is blocked; flag kept for review only (state writes before/after the call are not re-entrant here).

**Fix:** Verify the guard actually precedes the call and that no cross-function re-entry path exists.

<details>
<summary>Code</summary>

```
     199 |         totalAccrued -= amount;
     200 | 
>>>  201 |         (bool ok,) = payout.call{value: amount}("");
     202 |         if (!ok) revert NativeTransferFailed();
     203 |         emit CommissionClaimed(partnerId, payout, amount);
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, Guard Present)

- **File:** `src\RewardDistributor.sol:185`
- **Severity:** INFO
- **Confidence:** 25%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} detected at line 185. The enclosing function carries a reentrancy-guard modifier, so re-entering this function is blocked; flag kept for review only (state writes before/after the call are not re-entrant here).

**Fix:** Verify the guard actually precedes the call and that no cross-function re-entry path exists.

<details>
<summary>Code</summary>

```
     183 |         // (1) burn share -> permanent sink
     184 |         if (burned > 0) {
>>>  185 |             (bool ok,) = burnAddress.call{value: burned}("");
     186 |             if (!ok) revert NativeTransferFailed();
     187 |         }
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, CEI Respected)

- **File:** `src\WXP.sol:44`
- **Severity:** INFO
- **Confidence:** 20%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} at line 44 has no storage write after it, so the checks-effects-interactions pattern effectively prevents reentrant state corruption; flag kept for review only.

**Fix:** Verify no cross-function re-entry path or later setter can be reached via the callee.

<details>
<summary>Code</summary>

```
      42 |         if (balanceOf[msg.sender] < wad) revert InsufficientBalance();
      43 |         balanceOf[msg.sender] -= wad;
>>>   44 |         (bool ok,) = msg.sender.call{value: wad}("");
      45 |         if (!ok) revert NativeTransferFailed();
      46 |         emit Withdrawal(msg.sender, wad);
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, Guard Present)

- **File:** `src\XPStakingVault.sol:531`
- **Severity:** INFO
- **Confidence:** 25%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} detected at line 531. The enclosing function carries a reentrancy-guard modifier, so re-entering this function is blocked; flag kept for review only (state writes before/after the call are not re-entrant here).

**Fix:** Verify the guard actually precedes the call and that no cross-function re-entry path exists.

<details>
<summary>Code</summary>

```
     529 |         rewardReserves -= amount;
     530 |         wxp.withdraw(amount);
>>>  531 |         (bool ok,) = distributor.call{value: amount}(abi.encodeWithSignature("receiveSweep()"));
     532 |         if (!ok) revert NativeTransferFailed();
     533 |         emit UnallocatedRewardsSwept(amount);
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, CEI Respected)

- **File:** `src\XPStakingVault.sol:739`
- **Severity:** INFO
- **Confidence:** 20%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} at line 739 has no storage write after it, so the checks-effects-interactions pattern effectively prevents reentrant state corruption; flag kept for review only.

**Fix:** Verify no cross-function re-entry path or later setter can be reached via the callee.

<details>
<summary>Code</summary>

```
     737 | 
     738 |     function _sendNative(address to, uint256 amount) private {
>>>  739 |         (bool ok,) = to.call{value: amount}("");
     740 |         if (!ok) revert NativeTransferFailed();
     741 |     }
```
</details>

---

## Logic (9)

### [~] Balance Comparison

- **File:** `src\PartnerCommissionDistributor.sol:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends. Note: in admin-only withdraw paths this is usually benign.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      21 | ///      split across registered partners in proportion to their current vault TVL snapshot and
      22 | ///      accrued to each partner's pull-claimable balance. Partners `claim()` to their payout
>>>   23 | ///      address. Solvency invariant: address(this).balance >= totalAccrued at all times.
      24 | contract PartnerCommissionDistributor is AccessControl, ReentrancyGuard {
      25 |     /// @notice Role allowed to register partners, fund the budget, and distribute commission.
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\app.js:726`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     724 |   function reportClaim(receipt) {
     725 |     const amt = claimedAmount(receipt);
>>>  726 |     if (amt === null) {
     727 |       setTx("Rewards claimed \u2713", "ok");
     728 |     } else if (amt === 0n) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\app.js:1234`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
    1232 | 
    1233 |     // At launch: flip CFG.launch.live = true → hide the modal/ribbon and restore LIVE.
>>> 1234 |     if (launch.live === true) {
    1235 |       if (modal) {
    1236 |         modal.hidden = true;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\status.js:119`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     117 |     // figures are shown here — this card is the headline, the raw on-chain
     118 |     // value sits underneath it, so the difference is visible rather than hidden.
>>>  119 |     let stakingApr = apr !== null ? Number(apr) / 1e16 : null;
     120 |     if (lastS && Number(lastS.settledAt) > 0 && ratioBps && epoch) {
     121 |       const denom = Math.max(fe(tvl), fe(cap));
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\status.js:129`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     127 |     // ── health checks ──
     128 |     const oblig = (tvl ?? 0n) + (pendingRedeem ?? 0n) + (reserves ?? 0n);
>>>  129 |     const solvent = held !== null && held >= oblig;
     130 |     const settleOver = nextSettle ? now - Number(nextSettle) : 0;
     131 |     const settleDelayed = settleOver > SETTLE_GRACE_S && pending !== null && fe(pending) > 0;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\status.js:131`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     129 |     const solvent = held !== null && held >= oblig;
     130 |     const settleOver = nextSettle ? now - Number(nextSettle) : 0;
>>>  131 |     const settleDelayed = settleOver > SETTLE_GRACE_S && pending !== null && fe(pending) > 0;
     132 |     const streaming = periodFinish && Number(periodFinish) > now;
     133 |     const issues = [];
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\status.js:149`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     147 |       cap && fe(cap) > 0 ? 1 - (Number(ratioBps ?? 6000) / 10000) * Math.min(1, fe(tvl) / fe(cap)) : 1;
     148 |     queuedTxt =
>>>  149 |       pending !== null && fe(pending) > 0
     150 |         ? ` · ≈${fn(fe(pending))} XP queued (≈${fn(fe(pending) * burnShare)} to burn)`
     151 |         : "";
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\status.js:173`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     171 |     $("metrics").innerHTML =
     172 |       card("Total value locked", `${fn(fe(tvl))} <small>XP</small>`, "", `${fn(utilization, 2)}% of ${fn(fe(cap), 0)} XP cap`) +
>>>  173 |       card("Staking APR", stakingApr !== null ? stakingApr.toFixed(2) + " <small>%</small>" : "—", "",
     174 |            apr !== null ? `on-chain currentAPR() reads ${(Number(apr) / 1e16).toFixed(2)}%` : "from real validator revenue") +
     175 |       card("Burned forever", `${fn(fe(burned))} <small>XP</small>`, "burn", "removed from supply") +
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `web\status.js:174`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     172 |       card("Total value locked", `${fn(fe(tvl))} <small>XP</small>`, "", `${fn(utilization, 2)}% of ${fn(fe(cap), 0)} XP cap`) +
     173 |       card("Staking APR", stakingApr !== null ? stakingApr.toFixed(2) + " <small>%</small>" : "—", "",
>>>  174 |            apr !== null ? `on-chain currentAPR() reads ${(Number(apr) / 1e16).toFixed(2)}%` : "from real validator revenue") +
     175 |       card("Burned forever", `${fn(fe(burned))} <small>XP</small>`, "burn", "removed from supply") +
     176 |       card("Paid to stakers", `${fn(fe(distributed))} <small>XP</small>`, "ok", "lifetime distributed") +
```
</details>

---

## Error Handling (6)

### [!!] Empty Catch Block

- **File:** `web\app.js:662`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Empty catch block silently swallows errors.

**Fix:** Handle the error or re-throw it. At minimum, log the error.

<details>
<summary>Code</summary>

```
     660 |     try {
     661 |       gasPrice = BigInt(await readProvider.send("eth_gasPrice", [])).toString();
>>>  662 |     } catch (_) {}
     663 |     const res = await window.ZigapBridge.sendTx(
     664 |       {
```
</details>

---

### [!!] Empty Catch Block

- **File:** `web\app.js:743`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Empty catch block silently swallows errors.

**Fix:** Handle the error or re-throw it. At minimum, log the error.

<details>
<summary>Code</summary>

```
     741 |       try {
     742 |         r = await readProvider.send("eth_getTransactionReceipt", [hash]);
>>>  743 |       } catch (_) {}
     744 |       if (r) {
     745 |         if (BigInt(r.status ?? 0) !== 1n) throw new Error("Transaction reverted on-chain");
```
</details>

---

### [!!] Empty Catch Block

- **File:** `web\app.js:947`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Empty catch block silently swallows errors.

**Fix:** Handle the error or re-throw it. At minimum, log the error.

<details>
<summary>Code</summary>

```
     945 |           <div class="req-track"><i style="width:${pct}%"></i></div>`;
     946 |         box.appendChild(el);
>>>  947 |       } catch (_) {}
     948 |     }
     949 |   }
```
</details>

---

### [!!] Empty Catch Block

- **File:** `web\app.js:1219`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Empty catch block silently swallows errors.

**Fix:** Handle the error or re-throw it. At minimum, log the error.

<details>
<summary>Code</summary>

```
    1217 |           input.value = E.formatEther(usable);
    1218 |           updateEstimate();
>>> 1219 |         } catch (_) {}
    1220 |       });
    1221 |   }
```
</details>

---

### [!!] Empty Catch Block

- **File:** `web\burn.js:100`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Empty catch block silently swallows errors.

**Fix:** Handle the error or re-throw it. At minimum, log the error.

<details>
<summary>Code</summary>

```
      98 |       const res = await fetch("data/stats.json", { cache: "no-store" });
      99 |       days = (await res.json()).days || [];
>>>  100 |     } catch (_) {}
     101 |     const chart = $("chart");
     102 |     const log = $("log");
```
</details>

---

### [!!] Empty Catch Block

- **File:** `web\zigap.js:92`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Empty catch block silently swallows errors.

**Fix:** Handle the error or re-throw it. At minimum, log the error.

<details>
<summary>Code</summary>

```
      90 |   function close(reason) {
      91 |     if (root) {
>>>   92 |       try { root.unmount(); } catch (_) {}
      93 |       root = null;
      94 |     }
```
</details>

---

## Resource Management (1)

### [!] Fixed-Gas Transfer

- **File:** `src\RewardDistributor.sol:192`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     190 |         if (distributed > 0) {
     191 |             wxp.deposit{value: distributed}();
>>>  192 |             require(wxp.transfer(address(vault), distributed), "WXP transfer failed");
     193 |             vault.notifyRewardAmount(distributed);
     194 |         }
```
</details>

---

## Performance (5)

### [~] Unoptimized Loop

- **File:** `src\PartnerCommissionDistributor.sol:144`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     142 |         p.registered = false;
     143 |         uint256 n = partnerList.length;
>>>  144 |         for (uint256 i = 0; i < n; i++) {
     145 |             if (partnerList[i] == partnerId) {
     146 |                 partnerList[i] = partnerList[n - 1];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\PartnerCommissionDistributor.sol:166`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     164 |         uint256 n = partnerList.length;
     165 |         uint256 totalTvl;
>>>  166 |         for (uint256 i = 0; i < n; i++) {
     167 |             totalTvl += vault.partnerTVL(partnerList[i]);
     168 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\PartnerCommissionDistributor.sol:171`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     169 |         if (totalTvl == 0) revert NoPartnerTVL();
     170 | 
>>>  171 |         for (uint256 i = 0; i < n; i++) {
     172 |             bytes32 pid = partnerList[i];
     173 |             uint256 tvl = vault.partnerTVL(pid);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\PartnerCommissionDistributor.sol:248`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     246 |         shares = new uint256[](n);
     247 |         uint256 totalTvl;
>>>  248 |         for (uint256 i = 0; i < n; i++) {
     249 |             totalTvl += vault.partnerTVL(partnerList[i]);
     250 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\PartnerCommissionDistributor.sol:251`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     249 |             totalTvl += vault.partnerTVL(partnerList[i]);
     250 |         }
>>>  251 |         for (uint256 i = 0; i < n; i++) {
     252 |             ids[i] = partnerList[i];
     253 |             if (totalTvl == 0) continue;
```
</details>

---

## Code Quality (2)

### [~] Hardcoded Sleep

- **File:** `ops\vault-activity.py:77`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
      75 |         except Exception as e:  # noqa: BLE001 — retry anything, the RPC rate-limits
      76 |             last = e
>>>   77 |             time.sleep(1.5 * (attempt + 1))
      78 |     raise RuntimeError(f"RPC {method} failed after {tries} tries: {last}")
      79 | 
```
</details>

---

### [~] Hardcoded Sleep

- **File:** `ops\vault-activity.py:337`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using sleep() in code can cause performance issues and race conditions.

**Fix:** Use proper synchronization primitives, event loops, or polling with backoff.

<details>
<summary>Code</summary>

```
     335 |         write_checkpoint(end)
     336 |         cur = end + 1
>>>  337 |         time.sleep(0.15)
     338 | 
     339 |     print(f"scanned {frm}..{head}, {seen} event(s)")
```
</details>

---


---
*Generated by BugHunter*