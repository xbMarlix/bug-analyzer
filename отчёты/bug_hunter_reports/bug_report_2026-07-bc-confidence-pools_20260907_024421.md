# BugHunter Report: 2026-07-bc-confidence-pools

**Generated:** 2026-09-07 02:44:21
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\codehawks\2026-07-bc-confidence-pools`
**Analyzers:** static, ast, solidity_semantic, ai

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 6 |
| Total lines | 1,313 |
| Bugs found | 17 |
| ! Medium | 15 |
| ~ Low | 2 |

### Languages Detected

- **solidity**: 6 files

## Logic (17)

### [!] Timestamp Dependence

- **File:** `src\ConfidencePool.sol:226`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     224 |         if (amount < minStake) revert BelowMinStake();
     225 |         if (outcome != PoolStates.Outcome.UNRESOLVED) revert OutcomeAlreadySet();
>>>  226 |         if (block.timestamp >= expiry) revert StakingClosed();
     227 |         _assertDepositsAllowed(_observePoolState());
     228 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\ConfidencePool.sol:269`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     267 |         if (amount == 0) revert InvalidAmount();
     268 |         if (outcome != PoolStates.Outcome.UNRESOLVED) revert OutcomeAlreadySet();
>>>  269 |         if (block.timestamp >= expiry) revert StakingClosed();
     270 | 
     271 |         _assertDepositsAllowed(_observePoolState());
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\ConfidencePool.sol:437`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     435 |         if (!goodFaith) revert InvalidGoodFaithParams();
     436 |         if (msg.sender != attacker) revert NotAttacker();
>>>  437 |         if (block.timestamp > corruptedClaimDeadline) revert ClaimWindowExpired();
     438 | 
     439 |         uint256 remaining = bountyEntitlement - bountyClaimed;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\ConfidencePool.sol:459`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     457 |         if (outcome != PoolStates.Outcome.CORRUPTED) revert OutcomeNotSet();
     458 |         if (!goodFaith) revert NotGoodFaithCorrupted();
>>>  459 |         if (block.timestamp <= corruptedClaimDeadline) revert ClaimWindowNotExpired();
     460 | 
     461 |         // aderyn-fp-next-line(reentrancy-state-change)
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\ConfidencePool.sol:513`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     511 |     /// @inheritdoc IConfidencePool
     512 |     function claimExpired() external nonReentrant {
>>>  513 |         if (block.timestamp < expiry) revert PoolNotExpired();
     514 |         if (outcome != PoolStates.Outcome.UNRESOLVED && outcome != PoolStates.Outcome.EXPIRED) {
     515 |             revert InvalidOutcome();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\ConfidencePool.sol:540`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     538 |                 // window; after that, anyone can finalize as bad-faith CORRUPTED so funds aren't
     539 |                 // trapped if the DAO becomes permanently unavailable.
>>>  540 |                 if (block.timestamp < expiry + MODERATOR_CORRUPTED_GRACE) {
     541 |                     revert AgreementCorruptedAwaitingModerator();
     542 |                 }
```
</details>

---

### [!] Potential Arithmetic Overflow in `_bonusShare` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_bonusShare` function calculates `userScore` and `globalScore` using arithmetic operations. If `userEligible`, `snapshotTotalStaked`, `userSumStakeTime`, `snapshotSumStakeTime`, `userSumStakeTimeSq`, and `snapshotSumStakeTimeSq` are very large, there is a risk of arithmetic overflow, which could lead to incorrect results or even a denial of service.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Arithmetic Underflow in `_bonusShare` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_bonusShare` function calculates `userScore` and `globalScore` using arithmetic operations. If `userEligible`, `snapshotTotalStaked`, `userSumStakeTime`, `snapshotSumStakeTime`, `userSumStakeTimeSq`, and `snapshotSumStakeTimeSq` are very small, there is a risk of arithmetic underflow, which could lead to incorrect results or even a denial of service.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Unchecked External Call in `_getAgreementState` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_getAgreementState` function calls `safeHarborRegistry.getAttackRegistry()`, which is an external function. If the external contract reverts, the function will also revert, which could lead to a loss of funds or other unintended consequences.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Unchecked External Call in `_getAgreementState` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_getAgreementState` function calls `IAttackRegistry(attackRegistry).getAgreementState(agreement)`, which is an external function. If the external contract reverts, the function will also revert, which could lead to a loss of funds or other unintended consequences.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Unchecked External Call in `_replaceScope` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_replaceScope` function calls `IAgreement(agreement).isContractInScope(account)`, which is an external function. If the external contract reverts, the function will also revert, which could lead to a loss of funds or other unintended consequences.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Unchecked External Call in `_observePoolState` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_observePoolState` function calls `_getAgreementState`, which is an external function. If the external contract reverts, the function will also revert, which could lead to a loss of funds or other unintended consequences.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Unchecked External Call in `_observePoolState` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_observePoolState` function calls `IAttackRegistry(attackRegistry).getAgreementState(agreement)`, which is an external function. If the external contract reverts, the function will also revert, which could lead to a loss of funds or other unintended consequences.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] Potential Unchecked External Call in `_observePoolState` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_observePoolState` function calls `IAgreement(agreement).isContractInScope(account)`, which is an external function. If the external contract reverts, the function will also revert, which could lead to a loss of funds or other unintended consequences.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [!] AI-detected Issue

- **File:** `src\interfaces\IConfidencePool.sol:1`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** 

**Fix:** 

<details>
<summary>Code</summary>

```
>>>    1 | // SPDX-License-Identifier: MIT
       2 | pragma solidity 0.8.26;
       3 | 
```
</details>

---

### [~] Potential Reentrancy in `_replaceScope` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_replaceScope` function modifies the `isAccountInScope` mapping and `_scopeAccounts` array. If a malicious contract calls this function, it could potentially cause a reentrancy attack by calling the function again before the state is fully updated.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---

### [~] Potential Reentrancy in `_observePoolState` Function

- **File:** `src\ConfidencePool.sol:501`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `_observePoolState` function calls `_getAgreementState`, which is an external function. If a malicious contract calls this function, it could potentially cause a reentrancy attack by calling the function again before the state is fully updated.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 |         if (totalEligibleStake == 0 || riskWindowStart == 0) {
     500 |             totalBonus -= amount <= totalBonus ? amount : totalBonus;
>>>  501 |         }
     502 | 
     503 |         // Intentionally does NOT set claimsStarted. A direct-transfer donation of as little as 1
```
</details>

---


---
*Generated by BugHunter*