# BugHunter Report: scan-key

**Generated:** 2026-09-07 23:15:51
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\predy\scan-key`
**Analyzers:** static, ast, solidity_semantic, ai

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 14 |
| Total lines | 2,821 |
| Bugs found | 29 |
| !! High | 5 |
| ! Medium | 12 |
| ~ Low | 12 |

### Languages Detected

- **solidity**: 14 files

## Logic (14)

### [!] Potential Reentrancy in `withdrawProtocolRevenue` and `withdrawCreatorRevenue`

- **File:** `PredyPool.sol:1`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The functions `withdrawProtocolRevenue` and `withdrawCreatorRevenue` do not use the `nonReentrant` modifier, which means they are vulnerable to reentrancy attacks. An attacker could call these functions multiple times in a row, potentially draining the contract's funds.

**Fix:** 

<details>
<summary>Code</summary>

```
>>>    1 | // SPDX-License-Identifier: UNLICENSED
       2 | pragma solidity ^0.8.17;
       3 | 
```
</details>

---

### [!] Potential Arithmetic Over/Underflow in `supply` and `withdraw`

- **File:** `PredyPool.sol:1`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The functions `supply` and `withdraw` perform arithmetic operations on the `accumulatedProtocolRevenue` and `accumulatedCreatorRevenue` variables. However, there is no check to ensure that these operations do not result in arithmetic over/underflow.

**Fix:** 

<details>
<summary>Code</summary>

```
>>>    1 | // SPDX-License-Identifier: UNLICENSED
       2 | pragma solidity ^0.8.17;
       3 | 
```
</details>

---

### [!] Potential Gas Limit Exceedance in `trade`

- **File:** `PredyPool.sol:1`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `trade` function calls the `trade` function of the `TradeLogic` contract. If the `trade` function of the `TradeLogic` contract has a high gas cost, it could cause the `trade` function to exceed the gas limit and fail.

**Fix:** 

<details>
<summary>Code</summary>

```
>>>    1 | // SPDX-License-Identifier: UNLICENSED
       2 | pragma solidity ^0.8.17;
       3 | 
```
</details>

---

### [!] Potential Unchecked External Calls in `take`

- **File:** `PredyPool.sol:1`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `take` function makes an external call to the `predySettlementCallback` and `predyTradeAfterCallback` functions. However, there is no check to ensure that these functions are callable and do not revert.

**Fix:** 

<details>
<summary>Code</summary>

```
>>>    1 | // SPDX-License-Identifier: UNLICENSED
       2 | pragma solidity ^0.8.17;
       3 | 
```
</details>

---

### [!] Potential Unchecked External Calls in `execLiquidationCall`

- **File:** `PredyPool.sol:1`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The `execLiquidationCall` function makes an external call to the `liquidate` function of the `LiquidationLogic` contract. However, there is no check to ensure that the `liquidate` function is callable and does not revert.

**Fix:** 

<details>
<summary>Code</summary>

```
>>>    1 | // SPDX-License-Identifier: UNLICENSED
       2 | pragma solidity ^0.8.17;
       3 | 
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `decrease` makes an external call to `IUniswapV3Pool(_assetStatus.uniswapPool).burn` and `IUniswapV3Pool(_assetStatus.uniswapPool).collect`. These calls should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `increase` makes an external call to `IUniswapV3Pool(_assetStatus.uniswapPool).mint`. This call should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `updateRebalancePosition` makes an external call to `sqrtAsset.rebalancePositionQuote.updatePosition` and `sqrtAsset.rebalancePositionBase.updatePosition`. These calls should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `finalizeReallocation` makes an external call to `sqrtPerpStatus.lastRebalanceTotalSquartAmount`. This call should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `getUtilizationRatio` makes an external call to `Constants.ONE`. This call should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `updateRebalanceEntry` makes an external call to `LPMath.calculateAmount0ForLiquidityWithTicks` and `LPMath.calculateAmount1ForLiquidityWithTicks`. These calls should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [!] Potential Unchecked External Calls

- **File:** `libraries\Perp.sol:501`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `calculateSqrtPerpOffset` makes an external call to `LPMath.calculateAmount0OffsetWithTick` and `LPMath.calculateAmount1OffsetWithTick`. These calls should be checked for errors to prevent potential reentrancy attacks.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [~] Potential Arithmetic Overflow

- **File:** `libraries\Perp.sol:501`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `calculateEntry` performs arithmetic operations that could potentially overflow. For example, when calculating `deltaEntry` and `payoff`, the values could exceed the maximum int256 value.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

### [~] Potential Arithmetic Underflow

- **File:** `libraries\Perp.sol:501`
- **Severity:** LOW
- **Confidence:** 60%
- **Analyzer:** ai

**Problem:** The function `decrease` performs arithmetic operations that could potentially underflow. For example, when calculating `receivedAmount0` and `receivedAmount1`, the values could become negative if `_liquidityAmount` is greater than `_assetStatus.totalAmount - _assetStatus.borrowedAmount`.

**Fix:** 

<details>
<summary>Code</summary>

```
     499 | 
     500 |         // Update entry value
>>>  501 |         _userStatus.perp.entryValue += payoff.perpEntryUpdate;
     502 |         _userStatus.sqrtPerp.entryValue += payoff.sqrtEntryUpdate;
     503 |         _userStatus.sqrtPerp.quoteRebalanceEntryValue += payoff.sqrtRebalanceEntryUpdateStable;
```
</details>

---

## Code Quality (9)

### [~] UNCLEAR require Error Message

- **File:** `PredyPool.sol:182`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     180 |         uint256 amount = pool.accumulatedProtocolRevenue;
     181 | 
>>>  182 |         require(amount > 0, "AZ");
     183 | 
     184 |         pool.accumulatedProtocolRevenue = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `PredyPool.sol:204`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     202 |         uint256 amount = pool.accumulatedCreatorRevenue;
     203 | 
>>>  204 |         require(amount > 0, "AZ");
     205 | 
     206 |         pool.accumulatedCreatorRevenue = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\ScaledAsset.sol:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      53 |         }
      54 | 
>>>   55 |         require(_supplyTokenAmount > 0, "S3");
      56 | 
      57 |         uint256 burnAmount = FixedPointMathLib.mulDivDown(_amount, Constants.ONE, tokenState.assetScaler);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\ScaledAsset.sol:85`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      83 |         // Confirms fee has been settled before position updating.
      84 |         if (userStatus.positionAmount > 0) {
>>>   85 |             require(userStatus.lastFeeGrowth == tokenStatus.assetGrowth, "S2");
      86 |         } else if (userStatus.positionAmount < 0) {
      87 |             require(userStatus.lastFeeGrowth == tokenStatus.debtGrowth, "S2");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\ScaledAsset.sol:87`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      85 |             require(userStatus.lastFeeGrowth == tokenStatus.assetGrowth, "S2");
      86 |         } else if (userStatus.positionAmount < 0) {
>>>   87 |             require(userStatus.lastFeeGrowth == tokenStatus.debtGrowth, "S2");
      88 |         }
      89 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\ScaledAsset.sol:160`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     158 |         returns (uint256)
     159 |     {
>>>  160 |         require(accountState.positionAmount >= 0, "S1");
     161 | 
     162 |         return FixedPointMathLib.mulDivDown(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\ScaledAsset.sol:175`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     173 |         returns (uint256)
     174 |     {
>>>  175 |         require(accountState.positionAmount <= 0, "S1");
     176 | 
     177 |         return FixedPointMathLib.mulDivUp(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\logic\LiquidationLogic.sol:45`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      43 |         bytes memory settlementData
      44 |     ) external returns (IPredyPool.TradeResult memory tradeResult) {
>>>   45 |         require(closeRatio > 0 && closeRatio <= 1e18, "ICR");
      46 |         DataType.Vault storage vault = globalData.vaults[vaultId];
      47 |         DataType.PairStatus storage pairStatus = globalData.pairs[vault.openPosition.pairId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\logic\SupplyLogic.sol:64`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      62 |         globalData.validate(_pairId);
      63 |         // Checks amount is not 0
>>>   64 |         require(_amount > 0, "AZ");
      65 |         // Updates interest rate related to the pair
      66 |         ApplyInterestLib.applyInterestForToken(globalData.pairs, _pairId);
```
</details>

---

## Accounting (4)

### [!!] Potential rounding error in premium calculation
- **File:** `libraries\PerpFee.sol:65`
- **Severity:** HIGH
**Problem:** The premium calculation uses `Math.fullMulDivDownInt256`, which rounds down. If the growthDiff is not a multiple of Constants.Q128, this can lead to a loss of precision.
EXPLOIT: A user with a small position size can repeatedly deposit and withdraw to exploit the rounding error, gradually draining the contract's value.
IMPACT: Potential loss of funds due to rounding errors in premium calculations.
**Fix:** Use a rounding method that does not lose precision, such as `Math.fullMulDivUpInt256`.
---
### [!!] Potential full-balance sweep of quote token
- **File:** `libraries\logic\ReallocationLogic.sol:45`
- **Severity:** HIGH
**Problem:** The contract transfers more quote tokens to the caller than they are owed, which could drain the contract's quote token balance if not properly accounted for.
EXPLOIT: If the contract's quote token balance is not properly tracked, an attacker could repeatedly call reallocate and receive more quote tokens than they deposited.
IMPACT: Complete drain of the contract's quote token balance
**Fix:** Ensure that the contract only transfers the exact amount of quote tokens owed to the caller.
---
### [!!] Full-balance sweep drains all pooled funds
- **File:** `libraries\logic\SupplyLogic.sol:46`
- **Severity:** HIGH
**Problem:** receiveTokenAndMintBond sends the entire contract balance instead of the caller's own deposit
EXPLOIT: any depositor calls receiveTokenAndMintBond and receives all funds parked in the contract
IMPACT: complete drain of pooled funds
**Fix:** pay only the caller's deposit
---
### [!!] Full-balance sweep drains all pooled funds
- **File:** `libraries\logic\SupplyLogic.sol:79`
- **Severity:** HIGH
**Problem:** burnBondAndTransferToken sends the entire contract balance instead of the caller's own deposit
EXPLOIT: any depositor calls burnBondAndTransferToken and receives all funds parked in the contract
IMPACT: complete drain of pooled funds
**Fix:** pay only the caller's deposit
---

## Reentrancy (1)

### [!!] Reentrancy with economic impact
- **File:** `libraries\logic\TradeLogic.sol:68`
- **Severity:** HIGH
**Problem:** callTradeAfterCallback makes an external call to IHooks(msg.sender).predyTradeAfterCallback, which could be reentered by the attacker to make repeated profitable operations before the write
EXPLOIT: an attacker calls IHooks(msg.sender).predyTradeAfterCallback and makes repeated profitable operations before the write
IMPACT: attacker can extract more value than a single entry would allow
**Fix:** use a reentrancy guard or check the return value of the external call
---

## Liquidation (1)

### [~] Potential liquidation math error at edge sizes
- **File:** `libraries\logic\LiquidationLogic.sol:159`
- **Severity:** LOW
**Problem:** calculateSlippageTolerance uses a floor or weight unbounded by the actual debt for very small positions
EXPLOIT: For the smallest eligible position, the extracted reward might still be within the documented total-penalty bound, but it could be higher than intended
IMPACT: Liquidators might profit beyond intended cap or a small-dust account might get drained past the intended penalty
**Fix:** Ensure that the calculation of slippage tolerance is bounded by the actual debt
---


---
*Generated by BugHunter*