# BugHunter Report: zentory

**Generated:** 2026-09-08 20:04:29
**Project:** `C:\Users\123123\AppData\Local\Temp\opencode\zentory`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 65 |
| Total lines | 9,396 |
| Bugs found | 124 |
| !! High | 5 |
| ~ Low | 118 |
| i Info | 1 |

### Languages Detected

- **solidity**: 34 files
- **sql**: 14 files
- **typescript**: 12 files
- **javascript**: 4 files
- **css**: 1 files

## Logic (10)

### [!!] State Change After External Call (CEI Violation)

- **File:** `contracts\src\signals\EpochScoring.sol:653`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'count' is modified at line 653, after an external call at line 652. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     651 |             uint256 checkEpoch = epochId - i;
     652 |             if (IZENTStaking(zentStaking).getStakeAtEpoch(provider, checkEpoch) > 0) {
>>>  653 |                 epochsActive[count++] = checkEpoch;
     654 |             }
     655 |         }
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\validate-changes.js:83`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
      81 |       for (const e of output.contracts[file][c].errors) {
      82 |         if (e.severity === "error") {
>>>   83 |           errorCount++;
      84 |           errors.push(`[${path.relative(__dirname, file)}] ${c}: ${e.formattedMessage || e.message}`);
      85 |         }
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\validate-changes.js:93`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
      91 |   for (const e of output.errors) {
      92 |     if (e.severity === "error") {
>>>   93 |       errorCount++;
      94 |       errors.push(`[general] ${e.formattedMessage || e.message}`);
      95 |     }
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\validate-fix-files.js:90`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
      88 |       for (const e of output.contracts[file][c].errors) {
      89 |         if (e.severity === "error" && !knownFalse(e.formattedMessage || e.message)) {
>>>   90 |           errorCount++;
      91 |           errors.push(`[${path.relative(__dirname, file)}] ${c}: ${e.formattedMessage || e.message}`);
      92 |         }
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\validate-fix-files.js:100`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
      98 |   for (const e of output.errors) {
      99 |     if (e.severity === "error" && !knownFalse(e.formattedMessage || e.message)) {
>>>  100 |       errorCount++;
     101 |       errors.push(`[general] ${e.formattedMessage || e.message}`);
     102 |     }
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\validate-tests.js:255`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
     253 |       for (const e of output.contracts[file][c].errors) {
     254 |         if (e.severity === "error") {
>>>  255 |           errorCount++;
     256 |           errors.push(`[${path.relative(__dirname, file)}] ${c}: ${e.formattedMessage || e.message}`);
     257 |         }
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\validate-tests.js:265`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
     263 |   for (const e of output.errors) {
     264 |     if (e.severity === "error") {
>>>  265 |       errorCount++;
     266 |       errors.push(`[general] ${e.formattedMessage || e.message}`);
     267 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `contracts\keeper\src\chain.ts:336`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     334 |       // bytes into the address-typed field. Downstream Supabase writes would
     335 |       // store a garbage provider. Use the zero address sentinel; the caller
>>>  336 |       // can check `success === false` to skip the DB write entirely.
     337 |       provider: '0x0000000000000000000000000000000000000000' as `0x${string}`,
     338 |       payoutZent: 0n,
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\keeper\src\index.ts:238`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
     236 |     if (result.accuracyResult) {
     237 |       accuracyResults.push(result.accuracyResult);
>>>  238 |       settledSignals++;
     239 |     } else {
     240 |       failedSignals++;
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `contracts\keeper\src\index.ts:240`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
     238 |       settledSignals++;
     239 |     } else {
>>>  240 |       failedSignals++;
     241 |     }
     242 | 
```
</details>

---

## Performance (22)

### [~] Unoptimized Loop

- **File:** `contracts\src\ZENTVesting.sol:73`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      71 | 
      72 |         uint256 totalToFund = 0;
>>>   73 |         for (uint256 i = 0; i < scheduleBeneficiaries.length; i++) {
      74 |             require(scheduleBeneficiaries[i] != address(0), "ZENTVesting: zero beneficiary");
      75 |             require(scheduleAmounts[i] > 0, "ZENTVesting: zero amount");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\ZENTVesting.sol:86`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      84 |         }
      85 | 
>>>   86 |         for (uint256 i = 0; i < scheduleBeneficiaries.length; i++) {
      87 |             beneficiaries.push(scheduleBeneficiaries[i]);
      88 |             schedules[scheduleBeneficiaries[i]] = VestingSchedule({
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\keeper\HyperCoreAdapter.sol:276`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     274 | 
     275 |     function uint128ToBytes(uint128 value, bytes memory buffer, uint256 offset) internal pure {
>>>  276 |         for (uint256 i = 0; i < 16; i++) {
     277 |             buffer[offset + i] = bytes1(uint8(uint128(value) >> (i * 8)));
     278 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\keeper\StrategyExecutor.sol:496`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     494 |     ) external onlyRole(DEFAULT_ADMIN_ROLE) {
     495 |         require(vaults.length == maxBPS.length, "mismatch length");
>>>  496 |         for (uint256 i = 0; i < vaults.length; i++) {
     497 |             maxLeverageBPS[vaults[i]] = maxBPS[i];
     498 |             emit MaxLeverageUpdated(vaults[i], maxBPS[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\oracle\MedianOracle.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      92 |         _revokeRole(UPDATER_ROLE, u);
      93 |         uint256 n = updaters.length;
>>>   94 |         for (uint256 i = 0; i < n; i++) {
      95 |             if (updaters[i] == u) {
      96 |                 updaters[i] = updaters[n - 1];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\oracle\MedianOracle.sol:128`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     126 |         uint256 count;
     127 |         uint256 oldest = block.timestamp;
>>>  128 |         for (uint256 i = 0; i < n; i++) {
     129 |             Report memory r = reports[updaters[i]];
     130 |             if (r.timestamp != 0 && block.timestamp - r.timestamp <= maxStaleness) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\oracle\MedianOracle.sol:143`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     141 |     /// @dev Median of the first `count` elements (insertion sort; small set).
     142 |     function _median(int256[] memory a, uint256 count) internal pure returns (int256) {
>>>  143 |         for (uint256 i = 1; i < count; i++) {
     144 |             int256 key = a[i];
     145 |             uint256 j = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:286`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     284 |         // stake-weight normalization. M-2: scoped to epoch signals.
     285 |         totalStake = 0;
>>>  286 |         for (uint256 i = 0; i < signalCount; i++) {
     287 |             totalStake += IZENTStaking(zentStaking).getProviderStake(
     288 |                 ISignalRegistry(signalRegistry).getEpochSignalProvider(epochId, i)
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:308`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     306 |         // _scoreProvider() to keep settleEpoch under Yul's stack-depth limit.
     307 |         ScoreResult[] memory results = new ScoreResult[](signalCount);
>>>  308 |         for (uint256 i = 0; i < signalCount; i++) {
     309 |             results[i] = _scoreProvider(epochId, i);
     310 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:394`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     392 |         if (results.length == 0) return 0;
     393 |         uint256 reward = epochReward / results.length;
>>>  394 |         for (uint256 i = 0; i < results.length; i++) {
     395 |             if (results[i].rank <= REWARD_CUTOFF) {
     396 |                 emit SignalScored(results[i].provider, results[i].accuracy, results[i].finalScore, results[i].rank);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:508`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     506 |         if (msg.sender != scoringOracle) revert UnauthorizedOracle(msg.sender);
     507 |         if (signalIds.length != accuraciesBps.length) revert ArraysLengthMismatch();
>>>  508 |         for (uint256 i = 0; i < signalIds.length; i++) {
     509 |             if (accuraciesBps[i] > 10000) revert();
     510 |             accuracyCache[signalIds[i]] = accuraciesBps[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:605`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     603 |         uint256 windowStart = epochId > 2 ? epochId - 2 : 0;
     604 |         uint256 recentCount = 0;
>>>  605 |         for (uint256 i = 0; i < epochsActive.length; i++) {
     606 |             if (epochsActive[i] >= windowStart && epochsActive[i] <= epochId) {
     607 |                 recentCount++;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:617`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     615 |     function _rankResults(ScoreResult[] memory results) internal pure {
     616 |         // Bubble sort by finalScore descending.
>>>  617 |         for (uint256 i = 0; i < results.length; i++) {
     618 |             for (uint256 j = i + 1; j < results.length; j++) {
     619 |                 if (results[j].finalScore > results[i].finalScore) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:627`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     625 |         }
     626 |         // Assign ranks (1 = best).
>>>  627 |         for (uint256 i = 0; i < results.length; i++) {
     628 |             results[i].rank = i + 1;
     629 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\EpochScoring.sol:649`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     647 |         epochsActive = new uint256[](5);
     648 |         uint256 count = 0;
>>>  649 |         for (uint256 i = 0; i < 5; i++) {
     650 |             if (epochId < i) break; // guard against underflow on early epochs
     651 |             uint256 checkEpoch = epochId - i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SignalRegistry.sol:255`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     253 | 
     254 |         ids = new bytes32[](batch.length);
>>>  255 |         for (uint256 i = 0; i < batch.length; i++) {
     256 |             SignalTypes.Signal calldata s = batch[i];
     257 |             // Re-validate each signal before internal submission
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SignalRegistry.sol:309`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     307 |         if (signalIds.length != accuraciesBps.length) revert ArraysLengthMismatch();
     308 | 
>>>  309 |         for (uint256 i = 0; i < signalIds.length; i++) {
     310 |             bytes32 id = signalIds[i];
     311 |             if (!signalExists[id]) revert SignalNotFound(id);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SignalRegistry.sol:421`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     419 | 
     420 |         uint256 idx = 0;
>>>  421 |         for (uint256 i = from; i <= to && i < providerSignalIds[provider].length; i++) {
     422 |             bytes32 id = providerSignalIds[provider][i];
     423 |             ids[idx]     = id;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SubscriptionVault.sol:264`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     262 | 
     263 |         // Iterate only over subscriber's tokens to find one with matching asset class
>>>  264 |         for (uint256 i = 0; i < tokens.length; i++) {
     265 |             SubscriptionInfo storage sub = subscriptionInfo[tokens[i]];
     266 |             if (sub.expiration > uint32(block.timestamp) && _bitmapHas(sub.assetClassBitmap, bit)) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SubscriptionVault.sol:279`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     277 |         uint256[] storage all = subscriberTokens[subscriber];
     278 |         uint256 count = 0;
>>>  279 |         for (uint256 i = 0; i < all.length; i++) {
     280 |             if (subscriptionInfo[all[i]].expiration > block.timestamp) count++;
     281 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SubscriptionVault.sol:285`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     283 |         tokenIds = new uint256[](count);
     284 |         uint256 idx = 0;
>>>  285 |         for (uint256 i = 0; i < all.length; i++) {
     286 |             if (subscriptionInfo[all[i]].expiration > block.timestamp) {
     287 |                 tokenIds[idx++] = all[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\src\signals\SubscriptionVault.sol:348`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     346 |         uint256[] storage tokens = subscriberTokens[subscriber];
     347 |         uint32 maxExp = 0;
>>>  348 |         for (uint256 i = 0; i < tokens.length; i++) {
     349 |             uint32 exp = subscriptionInfo[tokens[i]].expiration;
     350 |             if (exp > maxExp) maxExp = exp;
```
</details>

---

## Code Quality (88)

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\InsuranceFund.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      50 |     {
      51 |         require(to != address(0), "InsuranceFund: zero recipient");
>>>   52 |         require(amount > 0, "InsuranceFund: zero amount");
      53 |         IERC20(token).safeTransfer(to, amount);
      54 |         emit PaidOut(token, to, amount, reason);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENT.sol:28`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      26 |     ///         Can only be called once by the deployer. Prevents accidental mainnet use.
      27 |     modifier onlyTestnet() {
>>>   28 |         require(block.chainid == 998, "ZENT: not testnet");
      29 |         _;
      30 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENT.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      40 |     /// @param amount Amount to mint (in ZENT wei — 18 decimals).
      41 |     function mintForTestnet(address to, uint256 amount) external onlyTestnet {
>>>   42 |         require(msg.sender == DEPLOYER, "ZENT: not deployer");
      43 |         require(!_testnetMintDone, "ZENT: testnet mint disabled");
      44 |         _testnetMintDone = true;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENT.sol:43`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      41 |     function mintForTestnet(address to, uint256 amount) external onlyTestnet {
      42 |         require(msg.sender == DEPLOYER, "ZENT: not deployer");
>>>   43 |         require(!_testnetMintDone, "ZENT: testnet mint disabled");
      44 |         _testnetMintDone = true;
      45 |         _mint(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      45 | 
      46 |     modifier onlyDeployer() {
>>>   47 |         require(msg.sender == deployer, "ZENTVesting: not deployer");
      48 |         _;
      49 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      65 |         uint64 startTime_
      66 |     ) external onlyDeployer {
>>>   67 |         require(scheduleBeneficiaries.length == scheduleAmounts.length, "ZENTVesting: length mismatch");
      68 |         require(scheduleBeneficiaries.length == scheduleCliffs.length, "ZENTVesting: length mismatch");
      69 |         require(scheduleBeneficiaries.length == scheduleVestDurations.length, "ZENTVesting: length mismatch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:68`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      66 |     ) external onlyDeployer {
      67 |         require(scheduleBeneficiaries.length == scheduleAmounts.length, "ZENTVesting: length mismatch");
>>>   68 |         require(scheduleBeneficiaries.length == scheduleCliffs.length, "ZENTVesting: length mismatch");
      69 |         require(scheduleBeneficiaries.length == scheduleVestDurations.length, "ZENTVesting: length mismatch");
      70 |         require(scheduleBeneficiaries.length == scheduleRevocables.length, "ZENTVesting: length mismatch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      67 |         require(scheduleBeneficiaries.length == scheduleAmounts.length, "ZENTVesting: length mismatch");
      68 |         require(scheduleBeneficiaries.length == scheduleCliffs.length, "ZENTVesting: length mismatch");
>>>   69 |         require(scheduleBeneficiaries.length == scheduleVestDurations.length, "ZENTVesting: length mismatch");
      70 |         require(scheduleBeneficiaries.length == scheduleRevocables.length, "ZENTVesting: length mismatch");
      71 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:70`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      68 |         require(scheduleBeneficiaries.length == scheduleCliffs.length, "ZENTVesting: length mismatch");
      69 |         require(scheduleBeneficiaries.length == scheduleVestDurations.length, "ZENTVesting: length mismatch");
>>>   70 |         require(scheduleBeneficiaries.length == scheduleRevocables.length, "ZENTVesting: length mismatch");
      71 | 
      72 |         uint256 totalToFund = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:75`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      73 |         for (uint256 i = 0; i < scheduleBeneficiaries.length; i++) {
      74 |             require(scheduleBeneficiaries[i] != address(0), "ZENTVesting: zero beneficiary");
>>>   75 |             require(scheduleAmounts[i] > 0, "ZENTVesting: zero amount");
      76 |             require(scheduleVestDurations[i] > 0, "ZENTVesting: zero duration");
      77 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:76`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      74 |             require(scheduleBeneficiaries[i] != address(0), "ZENTVesting: zero beneficiary");
      75 |             require(scheduleAmounts[i] > 0, "ZENTVesting: zero amount");
>>>   76 |             require(scheduleVestDurations[i] > 0, "ZENTVesting: zero duration");
      77 | 
      78 |             for (uint256 j = 0; j < i; j++) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:79`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      77 | 
      78 |             for (uint256 j = 0; j < i; j++) {
>>>   79 |                 require(scheduleBeneficiaries[i] != scheduleBeneficiaries[j], "ZENTVesting: duplicate beneficiary");
      80 |             }
      81 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:82`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      80 |             }
      81 | 
>>>   82 |             require(schedules[scheduleBeneficiaries[i]].totalAmount == 0, "ZENTVesting: schedule exists");
      83 |             totalToFund += scheduleAmounts[i];
      84 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:124`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     122 |         address beneficiary = msg.sender;
     123 |         amount = vestedAmount(beneficiary);
>>>  124 |         require(amount > 0, "ZENTVesting: nothing to claim");
     125 | 
     126 |         uint256 newClaimed = uint256(schedules[beneficiary].claimed) + amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:136`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     134 |     function revoke(address beneficiary) external onlyDeployer {
     135 |         VestingSchedule storage s = schedules[beneficiary];
>>>  136 |         require(s.revocable, "ZENTVesting: not revocable");
     137 |         require(!s.revoked, "ZENTVesting: already revoked");
     138 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\ZENTVesting.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 |         VestingSchedule storage s = schedules[beneficiary];
     136 |         require(s.revocable, "ZENTVesting: not revocable");
>>>  137 |         require(!s.revoked, "ZENTVesting: already revoked");
     138 | 
     139 |         uint256 vested = _vestedTotal(s, block.timestamp);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\adapters\HyperSwapRouterAdapter.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      82 |             "zero addr"
      83 |         );
>>>   84 |         require(asset_ != cash_, "asset == cash");
      85 |         router = ISwapRouterV3(router_);
      86 |         asset = asset_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\adapters\HyperSwapRouterAdapter.sol:142`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     140 |     /// @notice Tune the swap deadline window (admin only).
     141 |     function setDeadlineWindow(uint256 window) external onlyRole(DEFAULT_ADMIN_ROLE) {
>>>  142 |         require(window > 0 && window <= 1 hours, "bad window");
     143 |         swapDeadlineWindow = window;
     144 |         emit DeadlineWindowSet(window);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:75`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      73 |     function accumulate(address vault, uint256 amount) external {
      74 |         require(vault != address(0), "FeeDistributor: zero vault");
>>>   75 |         require(amount > 0, "FeeDistributor: zero amount");
      76 |         // Only the vault contract itself may trigger accumulation — no third-party approval needed.
      77 |         require(msg.sender == vault, "FeeDistributor: not vault");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:77`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      75 |         require(amount > 0, "FeeDistributor: zero amount");
      76 |         // Only the vault contract itself may trigger accumulation — no third-party approval needed.
>>>   77 |         require(msg.sender == vault, "FeeDistributor: not vault");
      78 | 
      79 |         pendingFees[vault] += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 | 
      95 |         uint256 accumulated = pendingFees[vault];
>>>   96 |         require(accumulated > 0, "FeeDistributor: nothing to distribute");
      97 | 
      98 |         delete pendingFees[vault];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:149`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     147 |     ///      is a keeper or the governor; gas is self-funded.
     148 |     function triggerBuyback(address[] calldata path) external onlyRole(GOVERNOR_ROLE) {
>>>  149 |         require(path.length >= 2, "FeeDistributor: invalid path");
     150 |         require(path[0] == address(asset), "FeeDistributor: wrong asset");
     151 |         require(path[path.length - 1] == address(zent), "FeeDistributor: path must end in ZENT");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:154`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     152 | 
     153 |         uint256 buybackPool = pools[POOL_BUYBACK];
>>>  154 |         require(buybackPool > 0, "FeeDistributor: nothing to buy back");
     155 | 
     156 |         pools[POOL_BUYBACK] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:176`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     174 |     function withdrawTo(address recipient, uint256 amount, uint8 poolId) external onlyRole(GOVERNOR_ROLE) {
     175 |         require(recipient != address(0), "FeeDistributor: zero recipient");
>>>  176 |         require(amount > 0, "FeeDistributor: zero amount");
     177 |         require(poolId == POOL_GP_ENGINE, "FeeDistributor: not directly withdrawable");
     178 |         require(pools[poolId] >= amount, "FeeDistributor: insufficient pool balance");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:177`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     175 |         require(recipient != address(0), "FeeDistributor: zero recipient");
     176 |         require(amount > 0, "FeeDistributor: zero amount");
>>>  177 |         require(poolId == POOL_GP_ENGINE, "FeeDistributor: not directly withdrawable");
     178 |         require(pools[poolId] >= amount, "FeeDistributor: insufficient pool balance");
     179 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\fees\FeeDistributor.sol:178`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     176 |         require(amount > 0, "FeeDistributor: zero amount");
     177 |         require(poolId == POOL_GP_ENGINE, "FeeDistributor: not directly withdrawable");
>>>  178 |         require(pools[poolId] >= amount, "FeeDistributor: insufficient pool balance");
     179 | 
     180 |         pools[poolId] -= amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\governance\ZentGovernor.sol:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      56 |         require(timelock_ != address(0), "ZentGovernor: zero timelock");
      57 |         require(zentroller_ != address(0), "ZentGovernor: zero zentroller");
>>>   58 |         require(quorumBps_ <= 10000, "ZentGovernor: invalid quorum");
      59 | 
      60 |         zentToken = zentToken_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\keeper\HyperCoreAdapter.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 |     /// @param  szDecimals_   Size decimals (sz = human * 10^szDecimals_)
      95 |     function setAssetConfig(uint8 localAsset, uint32 assetIndex, uint8 szDecimals_) external onlyRole(GOVERNOR_ROLE) {
>>>   96 |         require(localAsset <= 3, "HyperCoreAdapter: invalid local asset");
      97 |         assetConfigs[localAsset] = AssetConfig({
      98 |             assetIndex: assetIndex,
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\keeper\StrategyExecutor.sol:204`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     202 |         // bricking all future role administration on this contract.
     203 |         require(newAdmin != address(0), "StrategyExecutor: zero admin");
>>>  204 |         require(newAdmin != msg.sender, "StrategyExecutor: same admin");
     205 |         grantRole(DEFAULT_ADMIN_ROLE, newAdmin);
     206 |         renounceRole(DEFAULT_ADMIN_ROLE, msg.sender);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\keeper\StrategyExecutor.sol:495`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     493 |         uint256[] calldata maxBPS
     494 |     ) external onlyRole(DEFAULT_ADMIN_ROLE) {
>>>  495 |         require(vaults.length == maxBPS.length, "mismatch length");
     496 |         for (uint256 i = 0; i < vaults.length; i++) {
     497 |             maxLeverageBPS[vaults[i]] = maxBPS[i];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\oracle\MedianOracle.sol:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      56 |         address admin_
      57 |     ) {
>>>   58 |         require(decimals_ > 0 && decimals_ <= 18, "bad decimals");
      59 |         require(maxStaleness_ > 0, "zero staleness");
      60 |         require(minAnswer_ > 0 && maxAnswer_ > minAnswer_, "bad bounds");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\oracle\MedianOracle.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |     ) {
      58 |         require(decimals_ > 0 && decimals_ <= 18, "bad decimals");
>>>   59 |         require(maxStaleness_ > 0, "zero staleness");
      60 |         require(minAnswer_ > 0 && maxAnswer_ > minAnswer_, "bad bounds");
      61 |         require(minQuorum_ > 0, "zero quorum");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\oracle\MedianOracle.sol:60`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      58 |         require(decimals_ > 0 && decimals_ <= 18, "bad decimals");
      59 |         require(maxStaleness_ > 0, "zero staleness");
>>>   60 |         require(minAnswer_ > 0 && maxAnswer_ > minAnswer_, "bad bounds");
      61 |         require(minQuorum_ > 0, "zero quorum");
      62 |         require(admin_ != address(0), "zero admin");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\oracle\MedianOracle.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      59 |         require(maxStaleness_ > 0, "zero staleness");
      60 |         require(minAnswer_ > 0 && maxAnswer_ > minAnswer_, "bad bounds");
>>>   61 |         require(minQuorum_ > 0, "zero quorum");
      62 |         require(admin_ != address(0), "zero admin");
      63 |         _decimals = decimals_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\oracle\MedianOracle.sol:91`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      89 |         // insufficient fresh reports). To rotate out a compromised updater at the
      90 |         // boundary, addUpdater the replacement FIRST, then remove.
>>>   91 |         require(updaters.length > minQuorum, "MedianOracle: would break quorum");
      92 |         _revokeRole(UPDATER_ROLE, u);
      93 |         uint256 n = updaters.length;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\shadow\ShadowPriceOracle.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      31 |         // 999) so an accidental mainnet deploy can never enable oracle
      32 |         // manipulation. Testnet (998) and local test chains are unaffected.
>>>   33 |         require(block.chainid != 999, "ShadowPriceOracle: mainnet forbidden");
      34 |         require(decimals_ > 0 && decimals_ <= 18, "bad decimals");
      35 |         require(initialPrice > 0, "bad initial price");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\shadow\ShadowPriceOracle.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      32 |         // manipulation. Testnet (998) and local test chains are unaffected.
      33 |         require(block.chainid != 999, "ShadowPriceOracle: mainnet forbidden");
>>>   34 |         require(decimals_ > 0 && decimals_ <= 18, "bad decimals");
      35 |         require(initialPrice > 0, "bad initial price");
      36 |         require(admin != address(0), "zero admin");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\shadow\ShadowPriceOracle.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      33 |         require(block.chainid != 999, "ShadowPriceOracle: mainnet forbidden");
      34 |         require(decimals_ > 0 && decimals_ <= 18, "bad decimals");
>>>   35 |         require(initialPrice > 0, "bad initial price");
      36 |         require(admin != address(0), "zero admin");
      37 |         _decimals = decimals_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\shadow\ShadowPriceOracle.sol:57`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      55 |     ///         updatedAt so SpotVault's staleness guard sees a fresh feed.
      56 |     function setPrice(int256 newPrice) external onlyRole(UPDATER_ROLE) {
>>>   57 |         require(newPrice > 0, "bad price");
      58 |         _answer = newPrice;
      59 |         _updatedAt = block.timestamp;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\shadow\ShadowSpotAdapter.sol:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      53 |         require(asset_ != address(0) && cash_ != address(0) && oracle_ != address(0), "zero addr");
      54 |         require(admin != address(0), "zero admin");
>>>   55 |         require(simulatedSlippageBps_ <= 10000, "bad bps");
      56 |         asset = IERC20(asset_);
      57 |         cash = IERC20(cash_);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\shadow\ShadowUSDC.sol:18`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      16 |         // Hard-block deployment to HyperEVM mainnet (chain 999) to prevent
      17 |         // unlimited token inflation if accidentally deployed to production.
>>>   18 |         require(block.chainid != 999, "ShadowUSDC: mainnet forbidden");
      19 |     }
      20 |     function decimals() public pure override returns (uint8) { return 6; }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\signals\EpochScoring.sol:196`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     194 |     function transferAdmin(address newAdmin) external onlyRole(DEFAULT_ADMIN_ROLE) {
     195 |         require(newAdmin != address(0), "EpochScoring: zero admin");
>>>  196 |         require(newAdmin != msg.sender, "EpochScoring: same admin");
     197 |         _grantRole(DEFAULT_ADMIN_ROLE, newAdmin);
     198 |         _revokeRole(DEFAULT_ADMIN_ROLE, msg.sender);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\signals\SignalRegistry.sol:395`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     393 |     function transferAdmin(address newAdmin) external onlyRole(DEFAULT_ADMIN_ROLE) {
     394 |         require(newAdmin != address(0), "SignalRegistry: zero admin");
>>>  395 |         require(newAdmin != msg.sender, "SignalRegistry: same admin");
     396 |         _grantRole(DEFAULT_ADMIN_ROLE, newAdmin);
     397 |         _revokeRole(DEFAULT_ADMIN_ROLE, msg.sender);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\signals\SubscriptionVault.sol:255`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     253 |         // SIGNAL-005); out-of-range values would wrap in the uint8 bitmap cast
     254 |         // and silently mis-evaluate access.
>>>  255 |         require(assetClass < 5, "SubscriptionVault: invalid assetClass");
     256 | 
     257 |         // O(1) check: if latest expiration has passed, no active subscription exists
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:80`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      78 |     /// @notice Deposit ZENT and credit the caller's bond balance.
      79 |     function bond(uint256 amount) external {
>>>   80 |         require(amount > 0, "ModelBonding: zero amount");
      81 | 
      82 |         Bond storage b = _bonds[msg.sender];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      92 |     ///         during the cooldown.
      93 |     function requestUnbond(uint256 amount) external {
>>>   94 |         require(amount > 0, "ModelBonding: zero amount");
      95 | 
      96 |         Bond storage b = _bonds[msg.sender];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:97`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      95 | 
      96 |         Bond storage b = _bonds[msg.sender];
>>>   97 |         require(amount <= b.amount, "ModelBonding: exceeds bond");
      98 |         require(b.unbondRequestedAt == 0, "ModelBonding: request pending");
      99 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:98`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      96 |         Bond storage b = _bonds[msg.sender];
      97 |         require(amount <= b.amount, "ModelBonding: exceeds bond");
>>>   98 |         require(b.unbondRequestedAt == 0, "ModelBonding: request pending");
      99 | 
     100 |         b.unbondAmount = amount.toUint128();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:111`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     109 |         Bond storage b = _bonds[msg.sender];
     110 |         uint256 amount = b.unbondAmount;
>>>  111 |         require(amount > 0, "ModelBonding: no request");
     112 |         require(block.timestamp >= uint256(b.unbondRequestedAt) + unbondCooldown, "ModelBonding: cooldown active");
     113 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:127`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     125 |         Bond storage b = _bonds[msg.sender];
     126 |         uint256 amount = b.unbondAmount;
>>>  127 |         require(amount > 0, "ModelBonding: no request");
     128 | 
     129 |         b.unbondAmount = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ModelBonding.sol:142`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     140 |     function slash(address provider, uint256 amount, string calldata reason) external onlyRole(RISK_COUNCIL_ROLE) {
     141 |         Bond storage b = _bonds[provider];
>>>  142 |         require(amount > 0 && amount <= b.amount, "ModelBonding: invalid amount");
     143 | 
     144 |         uint128 newBalance = uint128(uint256(b.amount) - amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:89`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      87 |     /// @inheritdoc IZENTStaking
      88 |     function stake(uint256 amount, uint64 lockDuration) external returns (uint64 lockEnd) {
>>>   89 |         require(amount > 0, "ZENTStaking: zero amount");
      90 |         require(lockDuration >= MIN_LOCK && lockDuration <= MAX_LOCK, "ZENTStaking: lock out of range");
      91 |         // Intentional existence check: a zero stored amount means the caller has no position.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:90`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      88 |     function stake(uint256 amount, uint64 lockDuration) external returns (uint64 lockEnd) {
      89 |         require(amount > 0, "ZENTStaking: zero amount");
>>>   90 |         require(lockDuration >= MIN_LOCK && lockDuration <= MAX_LOCK, "ZENTStaking: lock out of range");
      91 |         // Intentional existence check: a zero stored amount means the caller has no position.
      92 |         // slither-disable-next-line incorrect-equality
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:93`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      91 |         // Intentional existence check: a zero stored amount means the caller has no position.
      92 |         // slither-disable-next-line incorrect-equality
>>>   93 |         require(_positions[msg.sender].amount == 0, "ZENTStaking: position exists");
      94 | 
      95 |         lockEnd = uint64(block.timestamp) + lockDuration;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 |     /// @inheritdoc IZENTStaking
     108 |     function increaseAmount(uint256 amount) external {
>>>  109 |         require(amount > 0, "ZENTStaking: zero amount");
     110 | 
     111 |         Position storage pos = _positions[msg.sender];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     110 | 
     111 |         Position storage pos = _positions[msg.sender];
>>>  112 |         require(pos.amount > 0, "ZENTStaking: no position");
     113 |         require(block.timestamp < pos.lockEnd, "ZENTStaking: lock expired");
     114 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:113`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     111 |         Position storage pos = _positions[msg.sender];
     112 |         require(pos.amount > 0, "ZENTStaking: no position");
>>>  113 |         require(block.timestamp < pos.lockEnd, "ZENTStaking: lock expired");
     114 | 
     115 |         uint128 oldAmount = pos.amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:130`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     128 |     /// @inheritdoc IZENTStaking
     129 |     function extendLock(uint64 newLockDuration) external returns (uint64 newLockEnd) {
>>>  130 |         require(newLockDuration <= MAX_LOCK, "ZENTStaking: lock out of range");
     131 | 
     132 |         Position storage pos = _positions[msg.sender];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:133`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     131 | 
     132 |         Position storage pos = _positions[msg.sender];
>>>  133 |         require(pos.amount > 0, "ZENTStaking: no position");
     134 | 
     135 |         newLockEnd = uint64(block.timestamp) + newLockDuration;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 |         newLockEnd = uint64(block.timestamp) + newLockDuration;
     136 |         uint64 oldLockEnd = pos.lockEnd;
>>>  137 |         require(newLockEnd > oldLockEnd, "ZENTStaking: not extending");
     138 | 
     139 |         // SECURITY FIX (spec-conformance audit, finding #4): maintain the
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:158`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     156 |         Position storage pos = _positions[msg.sender];
     157 |         uint256 amount = pos.amount;
>>>  158 |         require(amount > 0, "ZENTStaking: no position");
     159 |         require(block.timestamp >= pos.lockEnd, "ZENTStaking: locked");
     160 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:159`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     157 |         uint256 amount = pos.amount;
     158 |         require(amount > 0, "ZENTStaking: no position");
>>>  159 |         require(block.timestamp >= pos.lockEnd, "ZENTStaking: locked");
     160 | 
     161 |         // Defensive bound: clamp the bookkeeping delta to the current
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:251`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     249 |         if (amount == 0) return;
     250 |         Position storage pos = _positions[provider];
>>>  251 |         require(pos.amount >= amount, "ZENTStaking: slash exceeds stake");
     252 | 
     253 |         uint128 newAmount = pos.amount - uint128(amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\staking\ZENTStaking.sol:279`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     277 |         if (amount == 0) return;
     278 |         Position storage pos = _positions[provider];
>>>  279 |         require(pos.amount > 0, "ZENTStaking: no position to reward");
     280 | 
     281 |         uint256 oldVe = _veAt(pos.amount, pos.lockEnd, uint64(block.timestamp));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:104`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     102 |         require(feeRecipient_ != address(0), "BaseVault: zero fee recipient");
     103 |         require(admin_ != address(0), "BaseVault: zero admin");
>>>  104 |         require(maxPositionSizeBPS_ <= 10000, "BaseVault: invalid position limit");
     105 |         require(circuitBreakerDrawdownBPS_ <= 10000, "BaseVault: invalid drawdown");
     106 |         require(rebalanceThresholdBPS_ <= 10000, "BaseVault: invalid rebalance threshold");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:105`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     103 |         require(admin_ != address(0), "BaseVault: zero admin");
     104 |         require(maxPositionSizeBPS_ <= 10000, "BaseVault: invalid position limit");
>>>  105 |         require(circuitBreakerDrawdownBPS_ <= 10000, "BaseVault: invalid drawdown");
     106 |         require(rebalanceThresholdBPS_ <= 10000, "BaseVault: invalid rebalance threshold");
     107 |         require(performanceFeeBPS_ <= 10000, "BaseVault: invalid performance fee");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:106`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     104 |         require(maxPositionSizeBPS_ <= 10000, "BaseVault: invalid position limit");
     105 |         require(circuitBreakerDrawdownBPS_ <= 10000, "BaseVault: invalid drawdown");
>>>  106 |         require(rebalanceThresholdBPS_ <= 10000, "BaseVault: invalid rebalance threshold");
     107 |         require(performanceFeeBPS_ <= 10000, "BaseVault: invalid performance fee");
     108 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:107`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     105 |         require(circuitBreakerDrawdownBPS_ <= 10000, "BaseVault: invalid drawdown");
     106 |         require(rebalanceThresholdBPS_ <= 10000, "BaseVault: invalid rebalance threshold");
>>>  107 |         require(performanceFeeBPS_ <= 10000, "BaseVault: invalid performance fee");
     108 | 
     109 |         maxLeverage = maxLeverage_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:194`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     192 | 
     193 |     modifier onlyWhenCircuitBreakerInactive() {
>>>  194 |         require(!isCircuitBreakerActive, "Circuit breaker active");
     195 |         _;
     196 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:267`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     265 |     ///         units, same decimals as the underlying). Must be > 0.
     266 |     function updateMarkPrice(uint256 markPrice) external onlyRole(KEEPER_ROLE) {
>>>  267 |         require(markPrice > 0, "Invalid mark price");
     268 |         currentMarkPrice = markPrice;
     269 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:332`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     330 |     function claimFees() external nonReentrant returns (uint256 claimed) {
     331 |         claimed = performanceFeeAccrued;
>>>  332 |         require(claimed > 0, "No fees to claim");
     333 | 
     334 |         address recipient = feeRecipient;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:400`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     398 |     {
     399 |         require(direction == int8(1) || direction == int8(-1) || direction == int8(0), "Invalid direction");
>>>  400 |         require(entryPrice > 0, "Invalid entry price");
     401 |         require(!isCircuitBreakerActive, "Circuit breaker active");
     402 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:401`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     399 |         require(direction == int8(1) || direction == int8(-1) || direction == int8(0), "Invalid direction");
     400 |         require(entryPrice > 0, "Invalid entry price");
>>>  401 |         require(!isCircuitBreakerActive, "Circuit breaker active");
     402 | 
     403 |         uint256 tvl = totalAssets();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:406`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     404 |         if (tvl > 0) {
     405 |             uint256 maxSize = (tvl * maxPositionSizeBPS) / 10000;
>>>  406 |             require(size <= maxSize, "Position size exceeds limit");
     407 |             // Leverage cap: a vault declared `maxLeverage = 3x` (30000 BPS)
     408 |             // must reject any recordTrade whose notional exceeds 3× NAV.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:417`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     415 |             // vault-enforced invariant).
     416 |             uint256 maxNotional = (tvl * maxLeverage) / 10000;
>>>  417 |             require(size <= maxNotional, "Leverage exceeds max");
     418 |         }
     419 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:446`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     444 | 
     445 |     function activateCircuitBreaker(string calldata reason) external onlyRole(RISK_COUNCIL_ROLE) {
>>>  446 |         require(!isCircuitBreakerActive, "Already active");
     447 |         isCircuitBreakerActive = true;
     448 |         emit CircuitBreakerActivated(reason);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:452`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     450 | 
     451 |     function deactivateCircuitBreaker() external onlyRole(DEFAULT_ADMIN_ROLE) {
>>>  452 |         require(isCircuitBreakerActive, "Not active");
     453 |         isCircuitBreakerActive = false;
     454 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:503`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     501 |     {
     502 |         if (isCircuitBreakerActive) revert EmergencyBreakerActive();
>>>  503 |         require(shares > 0, "BaseVault: zero shares");
     504 |         require(receiver != address(0) && owner != address(0), "BaseVault: zero addr");
     505 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\BaseVault.sol:511`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     509 | 
     510 |         uint256 supply = totalSupply();
>>>  511 |         require(supply > 0, "BaseVault: empty vault");
     512 |         uint256 bal = IERC20(asset()).balanceOf(address(this));
     513 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     119 |         require(asset_ != address(0) && cashAsset_ != address(0) && oracle_ != address(0), "zero addr");
     120 |         require(feeRecipient_ != address(0) && admin_ != address(0), "zero addr");
>>>  121 |         require(rebalanceThresholdBps_ <= 10000 && maxSlippageBps_ <= 10000 && performanceFeeBps_ <= 10000, "bad bps");
     122 |         require(maxOracleStaleness_ > 0, "zero staleness");
     123 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:122`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     120 |         require(feeRecipient_ != address(0) && admin_ != address(0), "zero addr");
     121 |         require(rebalanceThresholdBps_ <= 10000 && maxSlippageBps_ <= 10000 && performanceFeeBps_ <= 10000, "bad bps");
>>>  122 |         require(maxOracleStaleness_ > 0, "zero staleness");
     123 | 
     124 |         cashAsset = IERC20(cashAsset_);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:272`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     270 |         IERC20(tokenIn).forceApprove(address(swapAdapter), amountIn);
     271 |         uint256 out = swapAdapter.swap(tokenIn, tokenOut, amountIn, minOut);
>>>  272 |         require(out >= minOut, "slippage");
     273 |     }
     274 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:334`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     332 |     {
     333 |         uint256 accrued = performanceFeeAccrued;
>>>  334 |         require(accrued > 0, "SpotVault: nothing accrued");
     335 |         // Pay what the underlying leg can cover; the remainder stays accrued for a
     336 |         // later claim (the keeper can rebalance to raise underlying first).
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:339`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     337 |         uint256 bal = IERC20(asset()).balanceOf(address(this));
     338 |         paid = accrued <= bal ? accrued : bal;
>>>  339 |         require(paid > 0, "SpotVault: no underlying liquidity");
     340 |         performanceFeeAccrued = accrued - paid;
     341 |         IERC20(asset()).safeTransfer(feeRecipient, paid);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:358`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     356 |     {
     357 |         uint256 accrued = performanceFeeAccrued;
>>>  358 |         require(amount > 0 && amount <= accrued, "SpotVault: bad write-down");
     359 |         performanceFeeAccrued = accrued - amount;
     360 |         emit PerformanceFeeWrittenDown(amount, performanceFeeAccrued);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:426`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     424 |     {
     425 |         if (isCircuitBreakerActive) revert EmergencyBreakerActive();
>>>  426 |         require(shares > 0, "SpotVault: zero shares");
     427 |         require(receiver != address(0) && owner != address(0), "SpotVault: zero addr");
     428 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\src\vaults\SpotVault.sol:450`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     448 |         // actual underlying balance the vault can pay right now. No oracle call.
     449 |         uint256 supply = totalSupply();
>>>  450 |         require(supply > 0, "SpotVault: empty vault");
     451 |         uint256 bal = IERC20(asset()).balanceOf(address(this));
     452 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `contracts\keeper\src\chain.ts:192`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
     190 |  * write. Audit F-03: previously the keeper would build a viem client bound
     191 |  * to chain 998 but trust the RPC URL to be correct — same failure mode that
>>>  192 |  * almost bit us on the zSOL bug. If RPC_URL is misconfigured (or poisoned),
     193 |  * viem signs against whatever chain the RPC returns. This check fails loud.
     194 |  *
```
</details>

---

## Oracle (4)

### [!!] Oracle Price Missing Positive Check
- **File:** `contracts\src\shadow\ShadowSpotAdapter.sol:76`
- **Severity:** HIGH
**Problem:** latestRoundData() at line 76 reads a signed int256 price that is cast/used as uint256 WITHOUT a price > 0 guard. If the feed ever returns a negative value (feed governor compromise, aggregator malfunction, or a manipulated L2 sequencer feed), uint256(price) wraps to a huge number: a buyer then receives an enormous amount of tokens for a tiny payment, draining the entire sale supply. validate price <= 0 and staleness before use.
**Fix:** Add `if (price <= 0) revert();` before any uint256(price) cast, and check round completeness + updatedAt freshness.
---
### [!!] Oracle Price Missing Positive Check
- **File:** `contracts\src\signals\EpochScoring.sol:343`
- **Severity:** HIGH
**Problem:** latestRoundData() at line 343 reads a signed int256 price that is cast/used as uint256 WITHOUT a price > 0 guard. If the feed ever returns a negative value (feed governor compromise, aggregator malfunction, or a manipulated L2 sequencer feed), uint256(price) wraps to a huge number: a buyer then receives an enormous amount of tokens for a tiny payment, draining the entire sale supply. validate price <= 0 and staleness before use.
**Fix:** Add `if (price <= 0) revert();` before any uint256(price) cast, and check round completeness + updatedAt freshness.
---
### [!!] Oracle Price Missing Positive Check
- **File:** `contracts\src\signals\EpochScoring.sol:532`
- **Severity:** HIGH
**Problem:** latestRoundData() at line 532 reads a signed int256 price that is cast/used as uint256 WITHOUT a price > 0 guard. If the feed ever returns a negative value (feed governor compromise, aggregator malfunction, or a manipulated L2 sequencer feed), uint256(price) wraps to a huge number: a buyer then receives an enormous amount of tokens for a tiny payment, draining the entire sale supply. validate price <= 0 and staleness before use.
**Fix:** Add `if (price <= 0) revert();` before any uint256(price) cast, and check round completeness + updatedAt freshness.
---
### [!!] Oracle Price Missing Positive Check
- **File:** `contracts\src\vaults\SpotVault.sol:156`
- **Severity:** HIGH
**Problem:** latestRoundData() at line 156 reads a signed int256 price that is cast/used as uint256 WITHOUT a price > 0 guard. If the feed ever returns a negative value (feed governor compromise, aggregator malfunction, or a manipulated L2 sequencer feed), uint256(price) wraps to a huge number: a buyer then receives an enormous amount of tokens for a tiny payment, draining the entire sale supply. validate price <= 0 and staleness before use.
**Fix:** Add `if (price <= 0) revert();` before any uint256(price) cast, and check round completeness + updatedAt freshness.
---


---
*Generated by BugHunter*