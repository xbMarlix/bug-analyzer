# BugHunter Report: contracts

**Generated:** 2026-09-05 12:27:15
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\panoptic-v2\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 37 |
| Total lines | 17,757 |
| Bugs found | 25 |
| !! High | 10 |
| ! Medium | 12 |
| ~ Low | 3 |

### Languages Detected

- **solidity**: 37 files

## Security (5)

### [!!] Unsafe Delegatecall

- **File:** `CollateralTracker.sol:366`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     364 |     /// @return The name of the token
     365 |     function name() external view returns (string memory) {
>>>  366 |         // this logic requires multiple external calls and error handling, so we do it in a delegatecall to a library to save bytecode size
     367 |         return
     368 |             InteractionHelper.computeName(
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `CollateralTracker.sol:380`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     378 |     /// @return The symbol of the token
     379 |     function symbol() external view returns (string memory) {
>>>  380 |         // this logic requires multiple external calls and error handling, so we do it in a delegatecall to a library to save bytecode size
     381 |         return InteractionHelper.computeSymbol(underlyingToken(), TICKER_PREFIX);
     382 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `CollateralTracker.sol:387`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     385 |     /// @return The decimals of the token
     386 |     function decimals() external view returns (uint8) {
>>>  387 |         // this logic requires multiple external calls and error handling, so we do it in a delegatecall to a library to save bytecode size
     388 |         return InteractionHelper.computeDecimals(underlyingToken());
     389 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `PanopticPool.sol:369`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     367 |            */
     368 | 
>>>  369 |         // consolidate all 4 approval calls to one library delegatecall in order to reduce bytecode size
     370 |         // approves:
     371 |         // SFPM: token0, token1
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `base\Multicall.sol:15`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      13 |         results = new bytes[](data.length);
      14 |         for (uint256 i = 0; i != data.length; ) {
>>>   15 |             (bool success, bytes memory result) = address(this).delegatecall(data[i]);
      16 | 
      17 |             if (!success) {
```
</details>

---

## Logic (16)

### [!!] block.number For Randomness

- **File:** `RiskEngine.sol:2166`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
    2164 |                           |         .       . .
    2165 |                           +---------+-------+-+--->   POOL_
>>> 2166 |                                    50%    90% 100%     UTILIZATION
    2167 |         */
    2168 | 
```
</details>

---

### [!!] block.number For Randomness

- **File:** `RiskEngine.sol:2233`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
    2231 |                  |         .    ¯-_
    2232 |            0% -  +---------+-------∓---+--->   POOL_
>>> 2233 |                           90%     95% 100%      UTILIZATION
    2234 |          */
    2235 |         unchecked {
```
</details>

---

### [!!] block.number For Randomness

- **File:** `libraries\PanopticMath.sol:97`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
      95 |             string.concat(
      96 |                 Strings.toString(fee / 100),
>>>   97 |                 fee % 100 == 0
      98 |                     ? ""
      99 |                     : string.concat(
```
</details>

---

### [!!] block.number For Randomness

- **File:** `libraries\PanopticMath.sol:101`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
      99 |                     : string.concat(
     100 |                         ".",
>>>  101 |                         Strings.toString((fee / 10) % 10),
     102 |                         Strings.toString(fee % 10)
     103 |                     ),
```
</details>

---

### [!!] block.number For Randomness

- **File:** `libraries\PanopticMath.sol:102`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
     100 |                         ".",
     101 |                         Strings.toString((fee / 10) % 10),
>>>  102 |                         Strings.toString(fee % 10)
     103 |                     ),
     104 |                 "bps"
```
</details>

---

### [!] Timestamp Dependence

- **File:** `CollateralTracker.sol:299`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     297 | 
     298 |         // store the initial block and initialize the borrowIndex
>>>  299 |         s_marketState = MarketStateLibrary.storeMarketState(WAD, block.timestamp >> 2, 0, 0);
     300 |     }
     301 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `CollateralTracker.sol:1013`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
    1011 |         MarketState accumulator = s_marketState;
    1012 | 
>>> 1013 |         currentEpoch = block.timestamp >> 2;
    1014 |         uint256 previousEpoch = accumulator.marketEpoch();
    1015 |         uint128 deltaTime;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `PanopticGuardian.sol:200`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     198 |         uint256 eta = unlockEta[pool];
     199 |         if (eta == 0) revert NoPendingUnlock();
>>>  200 |         if (block.timestamp < eta) revert UnlockNotReady(eta);
     201 | 
     202 |         unlockEta[pool] = 0;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `PanopticGuardian.sol:306`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     304 |     function isPoolUnlockReady(PanopticPoolV2 pool) external view returns (bool) {
     305 |         uint256 eta = unlockEta[pool];
>>>  306 |         return eta != 0 && block.timestamp >= eta;
     307 |     }
     308 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `PanopticPool.sol:331`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     329 |     /// @dev Must be called first (by the factory contract) before any transaction can occur.
     330 |     function initialize() external {
>>>  331 |         // reverts if this contract has already been initialized (assuming block.timestamp > 0)
     332 |         if (OraclePack.unwrap(s_oraclePack) != 0) revert Errors.AlreadyInitialized();
     333 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `PanopticPool.sol:344`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     342 |         );
     343 |         s_oraclePack = OraclePackLibrary.storeOraclePack(
>>>  344 |             block.timestamp >> 6,
     345 |             0xf590a6, // orderMap
     346 |             EMAs,
```
</details>

---

### [!] Timestamp Dependence

- **File:** `PanopticPool.sol:353`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     351 |         );
     352 |         /*
>>>  353 |             (uint256((block.timestamp >> 6) % 2 ** 24) << 232) +
     354 |             // magic number which adds (7,5,3,1,0,2,4,6) order and minTick in positions 7, 5, 3 and maxTick in 6, 4, 2
     355 |             // see comment on s_oraclePack initialization for format of this magic number
```
</details>

---

### [!] Timestamp Dependence

- **File:** `PanopticPool.sol:421`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     419 |     /// @param maxTimestamp The latest acceptable block timestamp
     420 |     function assertTimestampRange(uint256 minTimestamp, uint256 maxTimestamp) external view {
>>>  421 |         if ((block.timestamp < minTimestamp) || (block.timestamp > maxTimestamp)) revert Deadline();
     422 |     }
     423 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RiskEngine.sol:2316`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
    2314 |                 // So the rate is always underestimated.
    2315 |                 int256 speed = Math.wMulToZero(ADJUSTMENT_SPEED, err);
>>> 2316 |                 // Safe "unchecked" cast because block.timestamp - market.lastUpdate <= block.timestamp <= type(int256).max.
    2317 |                 // Cap the elapsed time to prevent IRM drift
    2318 |                 uint256 epochTime = uint256(block.timestamp) & ~uint256(3);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `types\OraclePack.sol:430`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     428 |     ///                   - Bits 11-0:    Most recent observation residual (12 bits)
     429 |     /// @param newTick The new tick observation to insert (as a residual relative to reference tick)
>>>  430 |     /// @param currentEpoch The current epoch timestamp ((block.timestamp >> 6) & 0xFFFFFF)
     431 |     /// @param timeDelta Time difference in seconds between current and last epoch (currentEpoch - recordedEpoch) * 64
     432 |     /// @param EMAperiods The packed EMA period values for spot, fast, slow, and eons EMAs
```
</details>

---

### [!] Timestamp Dependence

- **File:** `types\OraclePack.sol:548`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     546 |             int256 timeDelta;
     547 |             {
>>>  548 |                 currentEpoch = (block.timestamp >> 6) & 0xFFFFFF; // 64-long epoch, taken mod 2**24
     549 |                 uint256 recordedEpoch = oraclePack.epoch();
     550 |                 differentEpoch = currentEpoch != recordedEpoch;
```
</details>

---

## Resource Management (1)

### [!] Fixed-Gas Transfer

- **File:** `CollateralTracker.sol:410`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     408 |         if (panopticPool().numberOfLegs(msg.sender) != 0) revert Errors.PositionCountNotZero();
     409 | 
>>>  410 |         return ERC20Minimal.transfer(recipient, amount);
     411 |     }
     412 | 
```
</details>

---

## Code Quality (3)

### [~] UNCLEAR require Error Message

- **File:** `Builder.sol:165`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     163 |     /// @dev Reverts with "NOT_OWNER" if msg.sender is not the OWNER
     164 |     function _onlyOwner() internal view {
>>>  165 |         require(msg.sender == OWNER, "NOT_OWNER");
     166 |     }
     167 | 
```
</details>

---

### [~] Address Is Contract Check

- **File:** `PanopticGuardian.sol:332`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     330 |         }
     331 | 
>>>  332 |         if (wallet == address(0) || wallet.code.length == 0) {
     333 |             return false;
     334 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `RiskEngine.sol:977`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     975 |         // Optional: enforce whitelist by checking that the contract actually exists
     976 |         if (builderCode != 0) {
>>>  977 |             if (feeRecipient.code.length == 0) revert Errors.InvalidBuilderCode();
     978 |         }
     979 |     }
```
</details>

---


---
*Generated by BugHunter*