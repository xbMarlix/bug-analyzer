# BugHunter Report: contracts

**Generated:** 2026-09-05 18:52:48
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\swell\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 62 |
| Total lines | 12,965 |
| Bugs found | 8 |
| ! Medium | 5 |
| ~ Low | 3 |

### Languages Detected

- **solidity**: 62 files

## Logic (5)

### [!] Balance Comparison

- **File:** `lrt\contracts\implementations\DepositManager.sol:150`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     148 |     uint256 exitingETH = AccessControlManager.rswEXIT().exitingETH();
     149 | 
>>>  150 |     if (address(this).balance < _pubKeys.length * DEPOSIT_AMOUNT + exitingETH) {
     151 |       revert InsufficientETHBalance();
     152 |     }
```
</details>

---

### [!] Balance Comparison

- **File:** `lrt\contracts\implementations\DepositManager.sol:257`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     255 | 
     256 |     uint256 exitingETH = AccessControlManager.rswEXIT().exitingETH();
>>>  257 |     if (address(this).balance < amount + exitingETH) {
     258 |       revert InsufficientETHBalance();
     259 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `lrt\contracts\implementations\RepricingOracle.sol:616`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     614 |     uint256 roundDataExpiryTime = updatedAt + maximumRoundDataStalenessTime;
     615 | 
>>>  616 |     if (block.timestamp > roundDataExpiryTime) {
     617 |       revert RoundDataIsStale(updatedAt, block.timestamp - roundDataExpiryTime);
     618 |     }
```
</details>

---

### [!] Balance Comparison

- **File:** `lst\contracts\implementations\DepositManager.sol:107`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     105 |     uint256 depositAmount = 32 ether;
     106 | 
>>>  107 |     if (address(this).balance < _pubKeys.length * depositAmount + exitingETH) {
     108 |       revert InsufficientETHBalance();
     109 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `lst\contracts\implementations\RepricingOracle.sol:581`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     579 |     uint256 roundDataExpiryTime = updatedAt + maximumRoundDataStalenessTime;
     580 | 
>>>  581 |     if (block.timestamp > roundDataExpiryTime) {
     582 |       revert RoundDataIsStale(updatedAt, block.timestamp - roundDataExpiryTime);
     583 |     }
```
</details>

---

## Performance (3)

### [~] Unoptimized Loop

- **File:** `lrt\contracts\implementations\DepositManager.sol:168`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     166 |       memory withdrawalCredentials = generateWithdrawalCredentialsForEigenPod();
     167 | 
>>>  168 |     for (uint256 i; i < validatorDetails.length; i++) {
     169 |       bytes32 depositDataRoot = DepositDataRoot.formatDepositDataRoot(
     170 |         validatorDetails[i].pubKey,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `lrt\contracts\libraries\EnumberableSetValidatorDetails.sol:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      42 |     );
      43 | 
>>>   44 |     for (uint256 i; i < validatorDetails.length; i++) {
      45 |       validatorDetails[i] = set._values[startIndex + i];
      46 |     }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `lst\contracts\libraries\EnumberableSetValidatorDetails.sol:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      42 |     );
      43 | 
>>>   44 |     for (uint256 i; i < validatorDetails.length; i++) {
      45 |       validatorDetails[i] = set._values[startIndex + i];
      46 |     }
```
</details>

---


---
*Generated by BugHunter*