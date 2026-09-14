# BugHunter Report: contracts

**Generated:** 2026-09-04 23:23:35
**Project:** `C:\Users\123123\Desktop\exactly\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 41 |
| Total lines | 9,054 |
| Bugs found | 37 |
| !! High | 6 |
| ! Medium | 29 |
| ~ Low | 2 |

### Languages Detected

- **solidity**: 41 files

## Security (6)

### [!!] Unsafe Delegatecall

- **File:** `Market.sol:950`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     948 | 
     949 |   function delegateToExtension() internal returns (bytes memory) {
>>>  950 |     /// @custom:oz-upgrades-unsafe-allow delegatecall
     951 |     // solhint-disable-next-line avoid-low-level-calls
     952 |     (bool success, bytes memory data) = address(extension).delegatecall(msg.data);
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `Market.sol:952`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     950 |     /// @custom:oz-upgrades-unsafe-allow delegatecall
     951 |     // solhint-disable-next-line avoid-low-level-calls
>>>  952 |     (bool success, bytes memory data) = address(extension).delegatecall(msg.data);
     953 |     if (!success) {
     954 |       // solhint-disable-next-line no-inline-assembly
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `mocks\MarketHarness.sol:45`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      43 |   ) external {
      44 |     // solhint-disable-next-line avoid-low-level-calls
>>>   45 |     (, bytes memory data) = address(this).delegatecall(
      46 |       abi.encodeCall(this.borrowAtMaturity, (maturity, assets, maxAssetsAllowed, receiver, borrower))
      47 |     );
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `mocks\MarketHarness.sol:58`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      56 |   ) external {
      57 |     // solhint-disable-next-line avoid-low-level-calls
>>>   58 |     (, bytes memory data) = address(this).delegatecall(
      59 |       abi.encodeCall(this.depositAtMaturity, (maturity, assets, minAssetsRequired, receiver))
      60 |     );
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `mocks\MarketHarness.sol:72`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      70 |   ) external {
      71 |     // solhint-disable-next-line avoid-low-level-calls
>>>   72 |     (, bytes memory data) = address(this).delegatecall(
      73 |       abi.encodeCall(this.withdrawAtMaturity, (maturity, positionAssets, minAssetsRequired, receiver, owner))
      74 |     );
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `mocks\MarketHarness.sol:85`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      83 |   ) external {
      84 |     // solhint-disable-next-line avoid-low-level-calls
>>>   85 |     (, bytes memory data) = address(this).delegatecall(
      86 |       abi.encodeCall(this.repayAtMaturity, (maturity, positionAssets, maxAssetsAllowed, borrower))
      87 |     );
```
</details>

---

## Logic (26)

### [!] Timestamp Dependence

- **File:** `InterestRateModel.sol:110`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     108 |     uint256 uGlobal
     109 |   ) public view returns (uint256) {
>>>  110 |     if (block.timestamp >= maturity) revert AlreadyMatured();
     111 |     if (uFixed > uGlobal) revert UtilizationExceeded();
     112 |     if (uGlobal == 0) return baseRate(uFloating, 0);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `InterestRateModel.sol:202`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     200 |     uint256
     201 |   ) external view returns (uint256) {
>>>  202 |     if (block.timestamp >= maturity) revert AlreadyMatured();
     203 |     uint256 floatingAssets = previewFloatingAssetsAverage(maturity);
     204 |     uint256 floatingDebt = market.totalFloatingBorrowAssets();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Market.sol:362`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     360 | 
     361 |     // verify if there are any penalties/fee for the account because of early withdrawal, if so discount
>>>  362 |     if (block.timestamp < maturity) {
     363 |       uint256 memFloatingAssetsAverage = previewFloatingAssetsAverage();
     364 |       uint256 memFloatingDebt = floatingDebt;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Market.sol:473`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     471 | 
     472 |     // early repayment allows a discount from the unassigned earnings
>>>  473 |     if (block.timestamp < maturity) {
     474 |       // calculate the deposit fee considering the amount of debt the account'll pay
     475 |       (uint256 discountFee, uint256 backupFee) = pool.calculateDeposit(principalCovered, backupFeeRate);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Market.sol:550`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     548 |         if (packedMaturities & 1 != 0) {
     549 |           uint256 actualRepay;
>>>  550 |           if (block.timestamp < maturity) {
     551 |             actualRepay = noTransferRepayAtMaturity(maturity, maxAssets, maxAssets, borrower, false);
     552 |             maxAssets -= actualRepay;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Market.sol:794`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     792 |         debt += positionAssets;
     793 | 
>>>  794 |         if (block.timestamp > maturity) {
     795 |           debt += positionAssets.mulWadDown((block.timestamp - maturity) * memPenaltyRate);
     796 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `MarketBase.sol:191`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     189 | 
     190 |         if (maturity > lastAccrual) {
>>>  191 |           backupEarnings += block.timestamp < maturity
     192 |             ? pool.unassignedEarnings.mulDivDown(block.timestamp - lastAccrual, maturity - lastAccrual)
     193 |             : pool.unassignedEarnings;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RewardsController.sol:395`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     393 |       uint256 lastUpdate = rewardData.lastUpdate;
     394 |       // `lastUpdate` can be greater than `block.timestamp` if distribution is set to start on a future date
>>>  395 |       if (block.timestamp > lastUpdate && (lastUpdate < rewardData.end || rewardData.lastUndistributed != 0)) {
     396 |         (uint256 borrowIndex, uint256 depositIndex, uint256 newUndistributed) = previewAllocation(
     397 |           rewardData,
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RewardsController.sol:462`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     460 |       rewardData,
     461 |       ops.market,
>>>  462 |       block.timestamp > lastUpdate ? block.timestamp - lastUpdate : 0
     463 |     );
     464 |     mapping(bool => Account) storage operationAccount = rewardData.accounts[account];
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RewardsController.sol:553`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     551 |         ? rewardData.undistributedFactor.mulDivDown(target, t.period * 1e18)
     552 |         : 0;
>>>  553 |       if (block.timestamp <= t.end) {
     554 |         if (distributionFactor > 0) {
     555 |           uint256 exponential = uint256((-int256(distributionFactor * deltaTime)).expWad());
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RewardsController.sol:690`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     688 |   function withdrawUndistributed(Market market, ERC20 reward, address to) external onlyRole(DEFAULT_ADMIN_ROLE) {
     689 |     RewardData storage rewardData = distribution[market].rewards[reward];
>>>  690 |     if (block.timestamp < rewardData.end) revert NotEnded();
     691 | 
     692 |     bool[] memory ops = new bool[](1);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RewardsController.sol:743`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     741 |         );
     742 |         // properly update release rate
>>>  743 |         if (block.timestamp < end) {
     744 |           uint256 released = 0;
     745 |           uint256 elapsed = 0;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `RewardsController.sol:746`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     744 |           uint256 released = 0;
     745 |           uint256 elapsed = 0;
>>>  746 |           if (block.timestamp > start) {
     747 |             released =
     748 |               rewardData.lastConfigReleased +
```
</details>

---

### [!] Timestamp Dependence

- **File:** `StakedEXA.sol:217`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     215 |     updateIndex(reward);
     216 |     RewardData storage rewardData = rewards[reward];
>>>  217 |     if (block.timestamp >= rewardData.finishAt) {
     218 |       rewardData.rate = (amount * 1e18) / rewardData.duration;
     219 |     } else {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `StakedEXA.sol:332`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     330 |   function claimable(IERC20 reward, address account, uint256 shares) public view returns (uint256) {
     331 |     uint256 start = avgStart[account];
>>>  332 |     if (start == 0 || block.timestamp * 1e18 - start <= minTime * 1e18) return 0;
     333 | 
     334 |     uint256 rawClaimable_ = rawClaimable(reward, account, shares);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `StakedEXA.sol:438`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     436 |     updateIndex(reward);
     437 | 
>>>  438 |     if (block.timestamp < rewards[reward].finishAt) {
     439 |       uint256 finishAt = rewards[reward].finishAt;
     440 |       rewards[reward].finishAt = uint40(block.timestamp);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\DebtManager.sol:439`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     437 |       ? percentage.mulWadDown(position.principal + position.fee)
     438 |       : position.principal + position.fee;
>>>  439 |     if (block.timestamp < maturity) {
     440 |       FixedLib.Pool memory pool;
     441 |       (pool.borrowed, pool.supplied, pool.unassignedEarnings, pool.lastAccrual) = market.fixedPools(maturity);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\DebtPreviewer.sol:496`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     494 |           market,
     495 |           rewards[r.i].asset,
>>>  496 |           block.timestamp > r.config.start ? r.deltaTime : 0
     497 |         );
     498 |         r.firstMaturity = r.start - (r.start % FixedLib.INTERVAL) + FixedLib.INTERVAL;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\IntegrationPreviewer.sol:174`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     172 |     if (totalPosition == 0) return 0;
     173 |     if (positionAssets > totalPosition) positionAssets = totalPosition;
>>>  174 |     if (block.timestamp >= maturity) {
     175 |       return positionAssets + positionAssets.mulWad((block.timestamp - maturity) * market.penaltyRate());
     176 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\IntegrationPreviewer.sol:201`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     199 |     if (totalPosition == 0) return 0;
     200 |     if (assets > type(uint256).max / 1e18) return totalPosition;
>>>  201 |     if (block.timestamp >= maturity) {
     202 |       return Math.min(assets.divWad(1e18 + (block.timestamp - maturity) * market.penaltyRate()), totalPosition);
     203 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\Previewer.sol:203`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     201 |     uint256 assets
     202 |   ) public view returns (FixedPreview memory) {
>>>  203 |     if (block.timestamp > maturity) revert AlreadyMatured();
     204 |     FixedLib.Pool memory pool;
     205 |     (pool.borrowed, pool.supplied, pool.unassignedEarnings, pool.lastAccrual) = market.fixedPools(maturity);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\Previewer.sol:325`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     323 |       FixedPreview({
     324 |         maturity: maturity,
>>>  325 |         assets: block.timestamp < maturity
     326 |           ? positionAssets.divWadDown(
     327 |             1e18 +
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\Previewer.sol:366`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     364 |       FixedPreview({
     365 |         maturity: maturity,
>>>  366 |         assets: block.timestamp < maturity
     367 |           ? positionAssets - fixedDepositYield(market, maturity, principal)
     368 |           : positionAssets + positionAssets.mulWadDown((block.timestamp - maturity) * market.penaltyRate()),
```
</details>

---

### [!] Timestamp Dependence

- **File:** `periphery\Previewer.sol:491`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     489 |           market,
     490 |           rewards[r.i].asset,
>>>  491 |           block.timestamp > r.config.start ? r.deltaTime : 0
     492 |         );
     493 |         r.firstMaturity = r.start - (r.start % FixedLib.INTERVAL) + FixedLib.INTERVAL;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `utils\FixedLib.sol:87`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      85 |     uint256 lastAccrual = pool.lastAccrual;
      86 | 
>>>   87 |     if (block.timestamp < maturity) {
      88 |       uint256 unassignedEarnings = pool.unassignedEarnings;
      89 |       pool.lastAccrual = block.timestamp;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `PriceFeedWrapper.sol:34`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'rate' is modified at line 34, after an external call at line 33. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      32 | 
      33 |     (, bytes memory data) = address(wrapper).staticcall(abi.encodeWithSelector(conversionSelector, baseUnit));
>>>   34 |     uint256 rate = abi.decode(data, (uint256));
      35 | 
      36 |     return int256(uint256(mainPrice).mulDivDown(rate, baseUnit));
```
</details>

---

## Resource Management (3)

### [!] Fixed-Gas Transfer

- **File:** `MarketExtension.sol:63`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      61 |     handleRewards(false, msg.sender);
      62 |     handleRewards(false, to);
>>>   63 |     return super.transfer(to, shares);
      64 |   }
      65 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `periphery\FlashLoanAdapter.sol:74`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      72 |       vault.sendTo(tokens[0], recipient, amounts[0]);
      73 |       IFlashLoanRecipient(recipient).receiveFlashLoan(tokens, amounts, fees, data);
>>>   74 |       tokens[0].transfer(address(vault), amounts[0]);
      75 |       vault.settle(tokens[0], amounts[0]);
      76 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `verified\VerifiedMarket.sol:173`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     171 |   function transfer(address to, uint256 shares) public override returns (bool) {
     172 |     _requireAllowed(to);
>>>  173 |     return super.transfer(to, shares);
     174 |   }
     175 | 
```
</details>

---

## Code Quality (2)

### [~] UNCLEAR require Error Message

- **File:** `mocks\MockBalancerVault.sol:38`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      36 |       preLoanBalances[i] = token.balanceOf(address(this));
      37 | 
>>>   38 |       require(preLoanBalances[i] >= amount, "insufficient flashloan balance"); // solhint-disable-line gas-custom-errors
      39 |       address(token).safeTransfer(address(recipient), amount);
      40 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `mocks\MockBalancerVault.sol:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      49 |     for (uint256 i = 0; i < tokens.length; ++i) {
      50 |       uint256 postLoanBalance = tokens[i].balanceOf(address(this));
>>>   51 |       require(postLoanBalance >= preLoanBalances[i], "invalid post balance"); // solhint-disable-line gas-custom-errors
      52 |     }
      53 |   }
```
</details>

---


---
*Generated by BugHunter*