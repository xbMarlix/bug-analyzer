# BugHunter Report: notional

**Generated:** 2026-09-08 22:15:01
**Project:** `C:\Users\123123\AppData\Local\Temp\opencode\notional`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 158 |
| Total lines | 31,036 |
| Bugs found | 236 |
| !! High | 14 |
| ! Medium | 12 |
| ~ Low | 207 |
| i Info | 3 |

### Languages Detected

- **solidity**: 153 files
- **bash**: 4 files
- **javascript**: 1 files

## Security (19)

### [!!] Unsafe Delegatecall

- **File:** `contracts\external\PauseRouter.sol:199`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     197 |             // Call the implementation.
     198 |             // out and outsize are 0 because we don't know the size yet.
>>>  199 |             let result := delegatecall(gas(), implementation, 0, calldatasize(), 0, 0)
     200 | 
     201 |             // Copy the returned data.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\external\PauseRouter.sol:205`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     203 | 
     204 |             switch result
>>>  205 |             // delegatecall returns 0 on error.
     206 |             case 0 {
     207 |                 revert(0, returndatasize())
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\external\Router.sol:289`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     287 |             // Call the implementation.
     288 |             // out and outsize are 0 because we don't know the size yet.
>>>  289 |             let result := delegatecall(gas(), implementation, 0, calldatasize(), 0, 0)
     290 | 
     291 |             // Copy the returned data.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\external\Router.sol:295`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     293 | 
     294 |             switch result
>>>  295 |                 // delegatecall returns 0 on error.
     296 |                 case 0 {
     297 |                     revert(0, returndatasize())
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\external\liquidators\TradeHandler.sol:21`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      19 |     ) internal returns (uint256 amountSold, uint256 amountBought) {
      20 |         (bool success, bytes memory result) = nProxy(payable(address(tradingModule))).getImplementation()
>>>   21 |             .delegatecall(abi.encodeWithSelector(
      22 |                 ITradingModule.executeTradeWithDynamicSlippage.selector,
      23 |                 dexId, trade, dynamicSlippageLimit
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\external\liquidators\TradeHandler.sol:38`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      36 |     ) internal returns (uint256 amountSold, uint256 amountBought) {
      37 |         (bool success, bytes memory result) = nProxy(payable(address(tradingModule))).getImplementation()
>>>   38 |             .delegatecall(abi.encodeWithSelector(ITradingModule.executeTrade.selector, dexId, trade));
      39 |         require(success);
      40 |         (amountSold, amountBought) = abi.decode(result, (uint256, uint256));
```
</details>

---

### [!!] Selfdestruct Used

- **File:** `contracts\external\patchfix\BasePatchFixRouter.sol:50`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** selfdestruct sends all remaining ETH to a target and destroys the contract, potentially bricking funds.

**Fix:** Avoid selfdestruct unless absolutely necessary and carefully reviewed.

<details>
<summary>Code</summary>

```
      48 |         // Safety check that we do not lose ownership
      49 |         require(NOTIONAL.owner() == OWNER);
>>>   50 |         selfdestruct(payable(OWNER));
      51 |     }
      52 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\Proxy.sol:7`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
       5 | /**
       6 |  * @dev This abstract contract provides a fallback function that delegates all calls to another contract using the EVM
>>>    7 |  * instruction `delegatecall`. We refer to the second contract as the _implementation_ behind the proxy, and it has to
       8 |  * be specified by overriding the virtual {_implementation} function.
       9 |  *
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\Proxy.sol:30`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      28 |             // Call the implementation.
      29 |             // out and outsize are 0 because we don't know the size yet.
>>>   30 |             let result := delegatecall(gas(), implementation, 0, calldatasize(), 0, 0)
      31 | 
      32 |             // Copy the returned data.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\Proxy.sol:36`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      34 | 
      35 |             switch result
>>>   36 |             // delegatecall returns 0 on error.
      37 |             case 0 {
      38 |                 revert(0, returndatasize())
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Upgrade.sol:70`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      68 |         _upgradeTo(newImplementation);
      69 |         if (data.length > 0 || forceCall) {
>>>   70 |             Address.functionDelegateCall(newImplementation, data);
      71 |         }
      72 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Upgrade.sol:89`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      87 |         _setImplementation(newImplementation);
      88 |         if (data.length > 0 || forceCall) {
>>>   89 |             Address.functionDelegateCall(newImplementation, data);
      90 |         }
      91 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Upgrade.sol:97`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      95 |             // Trigger rollback using upgradeTo from the new implementation
      96 |             rollbackTesting.value = true;
>>>   97 |             Address.functionDelegateCall(
      98 |                 newImplementation,
      99 |                 abi.encodeWithSignature("upgradeTo(address)", oldImplementation)
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Upgrade.sol:190`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     188 |         emit BeaconUpgraded(newBeacon);
     189 |         if (data.length > 0 || forceCall) {
>>>  190 |             Address.functionDelegateCall(IBeacon(newBeacon).implementation(), data);
     191 |         }
     192 |     }
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `contracts\external\liquidators\TradeHandler.sol:21`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      19 |     ) internal returns (uint256 amountSold, uint256 amountBought) {
      20 |         (bool success, bytes memory result) = nProxy(payable(address(tradingModule))).getImplementation()
>>>   21 |             .delegatecall(abi.encodeWithSelector(
      22 |                 ITradingModule.executeTradeWithDynamicSlippage.selector,
      23 |                 dexId, trade, dynamicSlippageLimit
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `contracts\external\liquidators\TradeHandler.sol:38`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      36 |     ) internal returns (uint256 amountSold, uint256 amountBought) {
      37 |         (bool success, bytes memory result) = nProxy(payable(address(tradingModule))).getImplementation()
>>>   38 |             .delegatecall(abi.encodeWithSelector(ITradingModule.executeTrade.selector, dexId, trade));
      39 |         require(success);
      40 |         (amountSold, amountBought) = abi.decode(result, (uint256, uint256));
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, CEI Respected)

- **File:** `contracts\external\actions\ERC1155Action.sol:456`
- **Severity:** INFO
- **Confidence:** 20%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} at line 456 has no storage write after it, so the checks-effects-interactions pattern effectively prevents reentrant state corruption; flag kept for review only.

**Fix:** Verify no cross-function re-entry path or later setter can be reached via the callee.

<details>
<summary>Code</summary>

```
     454 |             // We can only call back to Notional itself at this point, account context is already
     455 |             // stored and all three of the whitelisted methods above will check free collateral.
>>>  456 |             (bool status, bytes memory result) = address(this).call{value: msg.value}(data);
     457 |             require(status, _getRevertMsg(result));
     458 |         }
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, CEI Respected)

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:155`
- **Severity:** INFO
- **Confidence:** 20%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} at line 155 has no storage write after it, so the checks-effects-interactions pattern effectively prevents reentrant state corruption; flag kept for review only.

**Fix:** Verify no cross-function re-entry path or later setter can be reached via the callee.

<details>
<summary>Code</summary>

```
     153 |     function recover(address token, uint256 amount) external onlyOwner {
     154 |         if (Constants.ETH_ADDRESS == token) {
>>>  155 |             (bool status,) = msg.sender.call{value: amount}("");
     156 |             require(status);
     157 |         } else {
```
</details>

---

### [I] Reentrancy Vector (External Call with Value, CEI Respected)

- **File:** `contracts\internal\balances\protocols\GenericToken.sol:71`
- **Severity:** INFO
- **Confidence:** 20%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} at line 71 has no storage write after it, so the checks-effects-interactions pattern effectively prevents reentrant state corruption; flag kept for review only.

**Fix:** Verify no cross-function re-entry path or later setter can be reached via the callee.

<details>
<summary>Code</summary>

```
      69 |         bytes memory callData
      70 |     ) internal  {
>>>   71 |         (bool status, bytes memory returnData) = target.call{value: msgValue}(callData);
      72 |         require(status, checkRevertMessage(returnData));
      73 |     }
```
</details>

---

## Resource Management (7)

### [!] Fixed-Gas Transfer

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:232`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     230 | 
     231 |         if (0 < rewardToClaim) {
>>>  232 |             try IEIP20NonStandard(REWARD_TOKEN).transfer(account, rewardToClaim) {
     233 |                 bool success = checkReturnCode();
     234 |                 if (success) {
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\external\governance\Reservoir.sol:69`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      67 |         // No need to do special checking for return codes, here we know that the token
      68 |         // will be compliant because it is the NOTE contract
>>>   69 |         bool success = TOKEN.transfer(TARGET, amountToDrip);
      70 |         require(success, "Transfer failed");
      71 |         emit ReservoirDrip(TARGET, amountToDrip);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\external\liquidators\ManualLiquidator.sol:111`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     109 |     function claimNOTE() external ownerOrUser returns (uint256) {
     110 |         uint256 notesClaimed = NOTIONAL.nTokenClaimIncentives();
>>>  111 |         IERC20(NOTE).transfer(owner, notesClaimed);
     112 |         return notesClaimed;
     113 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\external\patchfix\MigrateUSDC.sol:37`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      35 | 
      36 |         USDC.transferFrom(FUNDING, address(this), currentUSDC_E);
>>>   37 |         USDC_E.transfer(FUNDING, currentUSDC_E);
      38 |         uint256 currentUSDC = USDC.balanceOf(address(this));
      39 |         // Confirm transfer success
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\internal\balances\protocols\GenericToken.sol:18`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      16 |         bool withdrawWrapped
      17 |     ) internal {
>>>   18 |         // Native token withdraws are processed using .transfer() which is may not work
      19 |         // for certain contracts that do not implement receive() with minimal gas requirements.
      20 |         // Prior to the prime cash upgrade, these contracts could withdraw cETH, however, post
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\internal\balances\protocols\GenericToken.sol:28`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      26 |         } else {
      27 |             // TODO: consider using .call with a manual amount of gas forwarding
>>>   28 |             payable(account).transfer(amount);
      29 |         }
      30 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\internal\balances\protocols\GenericToken.sol:37`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      35 |         uint256 amount
      36 |     ) internal {
>>>   37 |         IEIP20NonStandard(token).transfer(account, amount);
      38 |         checkReturnCode();
      39 |     }
```
</details>

---

## Performance (72)

### [~] Unoptimized Loop

- **File:** `contracts\bots\RebalanceHelper.sol:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      42 |         }
      43 | 
>>>   44 |         for (uint256 i = 0; i < currencyIds.length; i++) {
      45 |             uint16 currencyId = currencyIds[i];
      46 |             // ensure currency ids are unique and sorted
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\bots\RebalanceHelper.sol:71`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      69 |         // happened after block.timestamp - DELAY_AFTER_FAILURE period
      70 |         uint16 numOfCurrencyIdsToProcess = 0;
>>>   71 |         for (uint256 i = 0; i < currencyIds.length; i++) {
      72 |             if (
      73 |                 failedRebalanceMap[currencyIds[i]] + DELAY_AFTER_FAILURE <
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\bots\RebalanceHelper.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      82 |                 numOfCurrencyIdsToProcess
      83 |             );
>>>   84 |             for (uint256 i = 0; i < numOfCurrencyIdsToProcess; i++) {
      85 |                 currencyIdsToProcess[i] = currencyIds[i];
      86 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\Views.sol:203`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     201 |         activeInterestRateCurve = new InterestRateParameters[](maxMarketIndex);
     202 | 
>>>  203 |         for (uint256 i = 1; i <= maxMarketIndex; i++) {
     204 |             nextInterestRateCurve[i - 1] = InterestRateCurve
     205 |                 .getNextInterestRateParameters(currencyId, i);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\Views.sol:383`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     381 |         MarketParameters[] memory markets = new MarketParameters[](cashGroup.maxMarketIndex);
     382 | 
>>>  383 |         for (uint256 i = 0; i < cashGroup.maxMarketIndex; i++) {
     384 |             cashGroup.loadMarket(markets[i], i + 1, true, blockTime);
     385 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\Views.sol:568`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     566 |         if (account == nTokenHandler.nTokenAddress(currencyId)) {
     567 |             MarketParameters[] memory markets = _getActiveMarketsAtBlockTime(currencyId, block.timestamp);
>>>  568 |             for (uint256 i; i < markets.length; i++) cashBalance = cashBalance.add(markets[i].totalPrimeCash);
     569 |         }
     570 |     }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\BatchAction.sol:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      60 |         BalanceState memory balanceState;
      61 | 
>>>   62 |         for (uint256 i = 0; i < actions.length; i++) {
      63 |             BalanceAction calldata action = actions[i];
      64 |             // msg.value will only be used when currency id == 1, referencing ETH. The requirement
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\BatchAction.sol:133`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     131 |         BalanceState memory balanceState;
     132 | 
>>>  133 |         for (uint256 i = 0; i < actions.length; i++) {
     134 |             BatchLend calldata action = actions[i];
     135 |             // msg.value will never be used in this method because it is non-payable
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\BatchAction.sol:268`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     266 |         );
     267 | 
>>>  268 |         for (uint256 i = 0; i < actions.length; i++) {
     269 |             BalanceActionWithTrades calldata action = actions[i];
     270 |             // msg.value will only be used when currency id == 1, referencing ETH. The requirement
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\ERC1155Action.sol:101`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      99 |         int256[] memory amounts = new int256[](accounts.length);
     100 | 
>>>  101 |         for (uint256 i; i < accounts.length; i++) {
     102 |             // This is pretty inefficient but gets the job done
     103 |             amounts[i] = signedBalanceOf(accounts[i], ids[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\ERC1155Action.sol:123`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     121 |         uint256[] memory amounts = new uint256[](accounts.length);
     122 | 
>>>  123 |         for (uint256 i; i < accounts.length; i++) {
     124 |             // This is pretty inefficient but gets the job done
     125 |             amounts[i] = balanceOf(accounts[i], ids[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\ERC1155Action.sol:149`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     147 |         PortfolioAsset[] memory portfolio, uint16 currencyId, uint256 maturity
     148 |     ) internal pure returns (int256) {
>>>  149 |         for (uint256 i; i < portfolio.length; i++) {
     150 |             PortfolioAsset memory asset = portfolio[i];
     151 |             if (
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\ERC1155Action.sol:266`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     264 |         _validateAccounts(from, to);
     265 | 
>>>  266 |         for (uint256 i; i < ids.length; i++) {
     267 |             int256 amount = int256(amounts[i]);
     268 |             int256 balance = amount > 0 ? signedBalanceOf(from, ids[i]) : signedBalanceOf(to, ids[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\ERC1155Action.sol:350`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     348 |         PortfolioAsset[] memory assets = new PortfolioAsset[](ids.length);
     349 | 
>>>  350 |         for (uint256 i; i < ids.length; i++) {
     351 |             // Require that ids are not duplicated, there is no valid reason to have duplicate ids
     352 |             if (i > 0) require(ids[i] > ids[i - 1], "IDs must be sorted");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\GovernanceAction.sol:331`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     329 |         require(marketIndices.length == settings.length);
     330 | 
>>>  331 |         for (uint256 i = 0; i < marketIndices.length; i++) {
     332 |             require(0 < marketIndices[i]);
     333 |             require(marketIndices[i] <= maxMarketIndex);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:85`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      83 |         // NOTE: this conversion from int256 => uint256 is done for legacy reasons
      84 |         params.proportions = new uint256[](_proportions.length);
>>>   85 |         for (uint256 i = 0; i < _proportions.length; i++) {
      86 |             params.proportions[i] = _proportions[i].toUint();
      87 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      92 |         params.interestRateParams = new InterestRateParameters[](maxMarketIndex);
      93 |         // maxMarketIndex is 1-indexed
>>>   94 |         for (uint256 i = 1; i <= maxMarketIndex; i++) {
      95 |             params.interestRateParams[i - 1] = InterestRateCurve.getActiveInterestRateParameters(
      96 |                 currencyId,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     110 | 
     111 |         // The nToken portfolio only ever has liquidity tokens sorted in ascending order
>>>  112 |         for (uint256 i; i < storedAssets.length; i++) {
     113 |             PortfolioAsset memory asset = storedAssets[i];
     114 |             // Must be liquidity token type
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:224`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     222 |         // the subsequent calculations. Since nTokens never allow liquidity to go to zero then we know
     223 |         // there is always a matching token for each market.
>>>  224 |         for (uint256 i = 1; i < nToken.portfolioState.storedAssets.length; i++) {
     225 |             previousMarkets[i].loadMarketWithSettlementDate(
     226 |                 currencyId,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:413`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     411 |         // Oracle rate is carried over between loops
     412 |         uint256 oracleRate;
>>>  413 |         for (uint256 i = 0; i < nToken.cashGroup.maxMarketIndex; i++) {
     414 |             // Traded markets are 1-indexed
     415 |             newMarket.maturity = DateTime.getReferenceTime(blockTime).add(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:210`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     208 |         MarketParameters memory market;
     209 | 
>>>  210 |         for (uint256 i = 0; i < nToken.portfolioState.storedAssets.length; i++) {
     211 |             PortfolioAsset memory asset = nToken.portfolioState.storedAssets[i];
     212 |             asset.notional = asset.notional.sub(tokensToWithdraw[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:302`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     300 |         hasResidual = false;
     301 | 
>>>  302 |         for (uint256 i = 0; i < netfCash.length; i++) {
     303 |             if (netfCash[i] == 0) continue;
     304 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:338`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     336 |     ) internal pure returns (PortfolioAsset[] memory finalfCashAssets) {
     337 |         uint256 numAssetsToExtend;
>>>  338 |         for (uint256 i = 0; i < netfCash.length; i++) {
     339 |             if (netfCash[i] != 0) numAssetsToExtend++;
     340 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\TradingAction.sol:82`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      80 |         c.blockTime = block.timestamp;
      81 | 
>>>   82 |         for (uint256 i = 0; i < trades.length; i++) {
      83 |             uint256 maturity;
      84 |             (maturity, c.cash, c.fCashAmount) = _executeTrade(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\TradingAction.sol:125`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     123 |         c.blockTime = block.timestamp;
     124 | 
>>>  125 |         for (uint256 i = 0; i < trades.length; i++) {
     126 |             TradeActionType tradeType = TradeActionType(uint256(uint8(bytes1(trades[i]))));
     127 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\actions\TreasuryAction.sol:287`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     285 |         if (counter != 0) {
     286 |             currencyIdsForRebalance = new uint16[](counter);
>>>  287 |             for (uint16 i = 0; i < counter; i++) currencyIdsForRebalance[i] = currencyIds[i];
     288 |         }
     289 |     }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\governance\NoteERC20.sol:104`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     102 | 
     103 |         uint96 totalGrants = 0;
>>>  104 |         for (uint256 i = 0; i < initialGrantAmount.length; i++) {
     105 |             totalGrants = _add96(totalGrants, initialGrantAmount[i], "");
     106 |             require(balances[initialAccounts[i]] == 0, "Duplicate account");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\liquidators\BaseLiquidator.sol:103`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     101 | 
     102 |     function enableCurrencies(uint16[] calldata currencies) external onlyOwner {
>>>  103 |         for (uint256 i; i < currencies.length; i++) {
     104 |             _enableCurrency(currencies[i]);
     105 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\liquidators\BaseLiquidator.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     107 | 
     108 |     function approveTokens(address[] calldata tokens, address spender) external onlyOwner {
>>>  109 |         for (uint256 i; i < tokens.length; i++) {
     110 |             IERC20(tokens[i]).safeApprove(spender, 0);
     111 |             IERC20(tokens[i]).safeApprove(spender, type(uint256).max);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\liquidators\FlashLiquidator.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 |         uint256 numTrades;
      68 |         bytes32[] memory trades = new bytes32[](fCashMaturities.length);
>>>   69 |         for (uint256 i; i < fCashNotional.length; i++) {
      70 |             if (fCashNotional[i] == 0) continue;
      71 |             (uint256 marketIndex, bool isIdiosyncratic) = DateTime.getMarketIndex(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\liquidators\FlashLiquidator.sol:91`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      89 |             // Shrink the trades array to length if it is not full
      90 |             bytes32[] memory newTrades = new bytes32[](numTrades);
>>>   91 |             for (uint256 i; i < numTrades; i++) {
      92 |                 newTrades[i] = trades[i];
      93 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\liquidators\ManualLiquidator.sol:214`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     212 | 
     213 |         // Make sure we leave enough cash to cover the negative fCash residuals
>>>  214 |         for (uint256 i; i < assets.length; i++) {
     215 |             if (assets[i].currencyId == nTokenCurrencyId && assets[i].notional < 0) {
     216 |                 cashBalance = cashBalance.add(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:103`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     101 |         // Clear existing array
     102 |         uint256 existingLength = _storageSettings.fCashCurves.length;
>>>  103 |         for (uint256 i; i < existingLength; i++)  _storageSettings.fCashCurves.pop();
     104 | 
     105 |         for (uint256 i; i < settings.fCashCurves.length; i++) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:105`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     103 |         for (uint256 i; i < existingLength; i++)  _storageSettings.fCashCurves.pop();
     104 | 
>>>  105 |         for (uint256 i; i < settings.fCashCurves.length; i++) {
     106 |             _storageSettings.fCashCurves.push(settings.fCashCurves[i]);
     107 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:111`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     109 |         // Clear existing array
     110 |         existingLength = _storageSettings.fCashDebts.length;
>>>  111 |         for (uint256 i; i < existingLength; i++)  _storageSettings.fCashDebts.pop();
     112 | 
     113 |         for (uint256 i; i < settings.fCashDebts.length; i++) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:113`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     111 |         for (uint256 i; i < existingLength; i++)  _storageSettings.fCashDebts.pop();
     112 | 
>>>  113 |         for (uint256 i; i < settings.fCashDebts.length; i++) {
     114 |             _storageSettings.fCashDebts.push(settings.fCashDebts[i]);
     115 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:129`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     127 |         // Clear existing array
     128 |         uint256 existingLength = _storageSettings.fCashDebts.length;
>>>  129 |         for (uint256 i; i < existingLength; i++)  _storageSettings.fCashDebts.pop();
     130 | 
     131 |         for (uint256 i; i < fCashDebts.length; i++) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:131`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     129 |         for (uint256 i; i < existingLength; i++)  _storageSettings.fCashDebts.pop();
     130 | 
>>>  131 |         for (uint256 i; i < fCashDebts.length; i++) {
     132 |             _storageSettings.fCashDebts.push(fCashDebts[i]);
     133 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:296`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     294 |         finalRates = new uint256[](fCashCurves.length);
     295 | 
>>>  296 |         for (uint256 i = 0; i < fCashCurves.length; i++) {
     297 |             InterestRateCurveSettings memory irCurve = fCashCurves[i];
     298 |             MarketParameters memory market = markets[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:406`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     404 | 
     405 |         MarketParameters[] memory markets = new MarketParameters[](maxMarketIndex);
>>>  406 |         for (uint256 i = 0; i < maxMarketIndex; i++) {
     407 |             uint256 maturity = DateTime.getReferenceTime(block.timestamp).add(DateTime.getTradedMarket(i + 1));
     408 |             // NOTE: oracle rate does not matter in this context, oracleRateWindow is set to a minimum amount
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:428`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     426 |         );
     427 | 
>>>  428 |         for (uint256 i; i < finalCurves.length; i++) {
     429 |             InterestRateCurve.setNextInterestRateParameters(currencyId, i + 1, finalCurves[i]);
     430 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:442`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     440 |         mapping(uint256 => mapping(uint256 => TotalfCashDebtStorage)) storage store = LibStorage.getTotalfCashDebtOutstanding();
     441 | 
>>>  442 |         for (uint256 i; i < fCashDebts.length; i++) {
     443 |             // Only future dated fcash debt should be set
     444 |             require(block.timestamp < fCashDebts[i].maturity);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\Emitter.sol:225`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     223 |         uint256 len = assets.length;
     224 |         // Emit single events since it's unknown if all of the notional values are positive or negative.
>>>  225 |         for (uint256 i; i < len; i++) {
     226 |             emitTransferfCash(from, to, assets[i].currencyId, assets[i].maturity, assets[i].notional);
     227 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\balances\BalanceHandler.sol:296`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     294 |         mapping(uint256 => BalanceStorage) storage store = LibStorage.getBalanceStorage()[account];
     295 | 
>>>  296 |         for (uint256 i = 0; i < settleAmounts.length; i++) {
     297 |             SettleAmount memory amt = settleAmounts[i];
     298 |             if (amt.positiveSettledCash == 0 && amt.negativeSettledCash == 0) continue;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\balances\ExternalLending.sol:163`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     161 |         RedeemData[] memory redeemData
     162 |     ) internal returns (uint256 totalUnderlyingRedeemed) {
>>>  163 |         for (uint256 i; i < redeemData.length; i++) {
     164 |             RedeemData memory data = redeemData[i];
     165 |             // Measure the token balance change if the `assetToken` value is set in the
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\balances\ExternalLending.sol:213`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     211 |     /// by the TreasuryAction contract.
     212 |     function executeDeposits(Token memory underlyingToken, DepositData[] memory deposits) internal {
>>>  213 |         for (uint256 i; i < deposits.length; i++) {
     214 |             DepositData memory depositData = deposits[i];
     215 |             // Measure the token balance change if the `assetToken` value is set in the
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\liquidation\LiquidatefCash.sol:162`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     160 |         );
     161 | 
>>>  162 |         for (uint256 i = 0; i < fCashMaturities.length; i++) {
     163 |             // Require that fCash maturities are sorted descending. This ensures that a maturity can only
     164 |             // be specified exactly once. It also ensures that the longest dated assets (most risky) are
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\liquidation\LiquidatefCash.sol:275`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     273 |         }
     274 | 
>>>  275 |         for (uint256 i = 0; i < fCashMaturities.length; i++) {
     276 |             // Require that fCash maturities are sorted descending. This ensures that a maturity can only
     277 |             // be specified exactly once. It also ensures that the longest dated assets (most risky) are
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\liquidation\LiquidatefCash.sol:560`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     558 |         PortfolioAsset[] memory assets = new PortfolioAsset[](fCashMaturities.length);
     559 |         bool liquidatorIncursDebt = false;
>>>  560 |         for (uint256 i = 0; i < fCashMaturities.length; i++) {
     561 |             PortfolioAsset memory asset = assets[i];
     562 |             asset.currencyId = fCashCurrency;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\markets\DateTime.sol:49`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      47 |         uint256 tRef = DateTime.getReferenceTime(blockTime);
      48 | 
>>>   49 |         for (uint256 i = 1; i <= maxMarketIndex; i++) {
      50 |             if (maturity == tRef.add(DateTime.getTradedMarket(i))) return true;
      51 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\markets\DateTime.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      82 |         uint256 tRef = DateTime.getReferenceTime(blockTime);
      83 | 
>>>   84 |         for (uint256 i = 1; i <= maxMarketIndex; i++) {
      85 |             uint256 marketMaturity = tRef.add(DateTime.getTradedMarket(i));
      86 |             // If market matches then is not idiosyncratic
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\markets\InterestRateCurve.sol:602`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     600 |         );
     601 | 
>>>  602 |         for (uint8 i = 0; i < 250; i++) {
     603 |             int256 fCashDelta = (fCash_1 - fCash_0);
     604 |             if (fCashDelta == 0) return fCash_1;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenCalculations.sol:178`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     176 |         netfCash = new int256[](numMarkets);
     177 | 
>>>  178 |         for (uint256 i = 0; i < numMarkets; i++) {
     179 |             int256 totalTokens = nToken.portfolioState.storedAssets[i].notional;
     180 |             tokensToWithdraw[i] = totalTokens.mul(nTokensToRedeem).div(nToken.totalSupply);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenCalculations.sol:238`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     236 |         // the requisite amount of present value after adjusting for the ifCash residual value that is
     237 |         // not accessible via redemption.
>>>  238 |         for (uint256 i = 0; i < tokensToWithdraw.length; i++) {
     239 |             int256 totalTokens = nToken.portfolioState.storedAssets[i].notional;
     240 |             // Redeemer's baseline share of the liquidity tokens based on total supply:
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenCalculations.sol:277`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     275 | 
     276 |         MarketParameters memory market;
>>>  277 |         for (uint256 i = 0; i < numMarkets; i++) {
     278 |             // Load the corresponding market into memory
     279 |             nToken.cashGroup.loadMarket(market, i + 1, true, blockTime);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenCalculations.sol:341`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     339 |             // 1. initializing a cash group with 3+ markets for the first time (not beginning on the tRef)
     340 |             // 2. somehow initialize markets has been delayed for more than 24 hours
>>>  341 |             for (uint i = 1; i <= maxMarketIndex; i++) {
     342 |                 // In this loop we get the maturity of each active market and turn off the corresponding bit
     343 |                 // one by one. It is less efficient than the option above.
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenHandler.sol:180`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     178 | 
     179 |         uint256 shareSum;
>>>  180 |         for (uint256 i; i < depositShares.length; i++) {
     181 |             // This cannot overflow in uint 256 with 9 max slots
     182 |             shareSum = shareSum + depositShares[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenHandler.sol:207`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     205 |         require(proportions.length == annualizedAnchorRates.length, "PT: proportions length");
     206 | 
>>>  207 |         for (uint256 i; i < proportions.length; i++) {
     208 |             // Anchor rates are no longer used and must always be set to zero
     209 |             require(annualizedAnchorRates[i] == 0);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenHandler.sol:242`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     240 |         int256[] memory array1 = new int256[](maxMarketIndex);
     241 |         int256[] memory array2 = new int256[](maxMarketIndex);
>>>  242 |         for (uint256 i; i < maxMarketIndex; i++) {
     243 |             array1[i] = slot[index];
     244 |             index++;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\nToken\nTokenHandler.sol:258`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     256 |     ) private {
     257 |         uint256 index = 0;
>>>  258 |         for (uint256 i = 0; i < array1.length; i++) {
     259 |             slot[index] = array1[i];
     260 |             index++;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\pCash\PrimeCashExchangeRate.sol:135`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     133 |         TokenHandler.updateStoredTokenBalance(underlying, 0, newBalance);
     134 | 
>>>  135 |         for (uint256 i; i < holdings.length; i++) {
     136 |             newBalance = IERC20(holdings[i]).balanceOf(address(this));
     137 |             TokenHandler.updateStoredTokenBalance(holdings[i], 0, newBalance);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\BitmapAssetsHandler.sol:65`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      63 |         uint16 currencyId = accountContext.bitmapCurrencyId;
      64 | 
>>>   65 |         for (uint256 i; i < assets.length; i++) {
      66 |             PortfolioAsset memory asset = assets[i];
      67 |             if (asset.notional == 0) continue;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      29 |         pure
      30 |     {
>>>   31 |         for (uint256 i = 0; i < assets.length; i++) {
      32 |             PortfolioAsset memory asset = assets[i];
      33 |             if (asset.notional == 0) continue;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      50 |         int256 notional
      51 |     ) private pure returns (bool) {
>>>   52 |         for (uint256 i = 0; i < assetArray.length; i++) {
      53 |             PortfolioAsset memory asset = assetArray[i];
      54 |             if (
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:150`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     148 |         uint256 newLength = newAssets.length == 0 ? 1 : newAssets.length * 2;
     149 |         PortfolioAsset[] memory extendedArray = new PortfolioAsset[](newLength);
>>>  150 |         for (uint256 i = 0; i < newAssets.length; i++) {
     151 |             extendedArray[i] = newAssets[i];
     152 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:183`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     181 |         uint256 nextSettleTime;
     182 | 
>>>  183 |         for (uint256 i = 0; i < portfolioState.storedAssets.length; i++) {
     184 |             PortfolioAsset memory asset = portfolioState.storedAssets[i];
     185 |             // NOTE: this is to prevent the storage of assets that have been modified in the AssetHandler
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:196`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     194 | 
     195 |         // First delete assets from asset storage to maintain asset storage indexes
>>>  196 |         for (uint256 i = 0; i < portfolioState.storedAssets.length; i++) {
     197 |             PortfolioAsset memory asset = portfolioState.storedAssets[i];
     198 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:232`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     230 |             PortfolioAssetStorage[MAX_PORTFOLIO_ASSETS]) storage store = LibStorage.getPortfolioArrayStorage();
     231 |         PortfolioAssetStorage[MAX_PORTFOLIO_ASSETS] storage storageArray = store[account];
>>>  232 |         for (uint256 i = 0; i < portfolioState.newAssets.length; i++) {
     233 |             PortfolioAsset memory asset = portfolioState.newAssets[i];
     234 |             if (asset.notional == 0) continue;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:327`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     325 |         // The max active slot is the last storage slot where an asset exists, it's not clear where this will be in the
     326 |         // array so we search for it here.
>>>  327 |         for (uint256 i; i < portfolioState.storedAssets.length; i++) {
     328 |             PortfolioAsset memory a = portfolioState.storedAssets[i];
     329 |             if (a.storageSlot > maxActiveSlot && a.storageState != AssetStorageState.Delete) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\PortfolioHandler.sol:431`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     429 |         PortfolioAsset[] memory assets = new PortfolioAsset[](length);
     430 | 
>>>  431 |         for (uint256 i = 0; i < length; i++) {
     432 |             PortfolioAssetStorage storage assetStorage = storageArray[i];
     433 |             PortfolioAsset memory asset = assets[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\portfolio\TransferAssets.sol:24`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      22 |     /// @dev Used to flip the sign of assets to decrement the `from` account that is sending assets
      23 |     function invertNotionalAmountsInPlace(PortfolioAsset[] memory assets) internal pure {
>>>   24 |         for (uint256 i; i < assets.length; i++) {
      25 |             assets[i].notional = assets[i].notional.neg();
      26 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\internal\settlement\SettlePortfolioAssets.sol:66`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      64 |         uint256 settleAmountIndex;
      65 | 
>>>   66 |         for (uint256 i; i < portfolioState.storedAssets.length; i++) {
      67 |             PortfolioAsset memory asset = portfolioState.storedAssets[i];
      68 |             // Settlement date is on block time exactly
```
</details>

---

## Code Quality (135)

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\CalculationViews.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      50 | 
      51 |     function _checkValidCurrency(uint16 currencyId) internal view {
>>>   52 |         require(0 < currencyId && currencyId <= maxCurrencyId, "Invalid currency id");
      53 |     }
      54 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\CalculationViews.sol:138`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     136 |         cashGroup.loadMarket(market, marketIndex, false, blockTime);
     137 | 
>>>  138 |         require(market.maturity > blockTime, "Invalid block time");
     139 |         uint256 timeToMaturity = market.maturity - blockTime;
     140 |         InterestRateParameters memory irParams = InterestRateCurve.getActiveInterestRateParameters(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\CalculationViews.sol:182`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     180 |         cashGroup.loadMarket(market, marketIndex, false, blockTime);
     181 | 
>>>  182 |         require(market.maturity > blockTime, "Invalid block time");
     183 |         uint256 timeToMaturity = market.maturity - blockTime;
     184 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\CalculationViews.sol:193`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     191 |             if (fCashAmount < 0) {
     192 |                 // Do not allow borrows over the rate limit
>>>  193 |                 require(postFeeInterestRate <= rateLimit, "Trade failed, slippage");
     194 |             } else {
     195 |                 // Do not allow lends under the rate limit
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\CalculationViews.sol:196`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     194 |             } else {
     195 |                 // Do not allow lends under the rate limit
>>>  196 |                 require(postFeeInterestRate >= rateLimit, "Trade failed, slippage");
     197 |             }
     198 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\FreeCollateralExternal.sol:26`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      24 |                 /*uint80 answeredInRound*/
      25 |             ) = Deployments.SEQUENCER_UPTIME_ORACLE.latestRoundData();
>>>   26 |             require(answer == 0, "Sequencer Down");
      27 |             require(SEQUENCER_UPTIME_GRACE_PERIOD < block.timestamp - startedAt, "Sequencer Grace Period");
      28 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\FreeCollateralExternal.sol:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      25 |             ) = Deployments.SEQUENCER_UPTIME_ORACLE.latestRoundData();
      26 |             require(answer == 0, "Sequencer Down");
>>>   27 |             require(SEQUENCER_UPTIME_GRACE_PERIOD < block.timestamp - startedAt, "Sequencer Grace Period");
      28 |         }
      29 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\FreeCollateralExternal.sol:73`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      71 |         }
      72 | 
>>>   73 |         require(ethDenominatedFC >= 0, "Insufficient free collateral");
      74 |     }
      75 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\PauseRouter.sol:86`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      84 | 
      85 |         // Checks
>>>   86 |         require(msg.sender == _pendingOwner, "Ownable: caller != pending owner");
      87 | 
      88 |         // Effects
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\Router.sol:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      53 |         assembly { chainId := chainid() }
      54 |         if (chainId == Deployments.MAINNET || chainId == Deployments.LOCAL) {
>>>   55 |             require(Deployments.NOTE_TOKEN_ADDRESS == 0xCFEAead4947f0705A14ec42aC3D44129E1Ef3eD5, "NOTE");
      56 |             require(address(Deployments.WETH) == 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2, "WETH");
      57 |             require(address(Deployments.SEQUENCER_UPTIME_ORACLE) == address(0), "SEQUENCER");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\Router.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |             require(address(Deployments.SEQUENCER_UPTIME_ORACLE) == address(0), "SEQUENCER");
      58 |         } else if (chainId == Deployments.ARBITRUM_ONE) {
>>>   59 |             require(Deployments.NOTE_TOKEN_ADDRESS == 0x019bE259BC299F3F653688c7655C87F998Bc7bC1, "NOTE");
      60 |             require(address(Deployments.WETH) == 0x82aF49447D8a07e3bd95BD0d56f35241523fBab1, "WETH");
      61 |             require(address(Deployments.SEQUENCER_UPTIME_ORACLE) == 0xFdB631F5EE196F0ed6FAa767959853A9F217697D, "SEQUENCER");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\Views.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      67 | 
      68 |     function _checkValidCurrency(uint16 currencyId) internal view {
>>>   69 |         require(0 < currencyId && currencyId <= maxCurrencyId, "Invalid currency id");
      70 |     }
      71 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\Views.sol:87`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      85 |     {
      86 |         currencyId = tokenAddressToCurrencyId[tokenAddress];
>>>   87 |         require(currencyId != 0, "Token not listed");
      88 |     }
      89 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\AccountAction.sol:141`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     139 |     ) external nonReentrant returns (uint256) {
     140 |         if (currencyId != Constants.ETH_CURRENCY_ID) {
>>>  141 |             require(redeemToUnderlying, "Deprecated: Redeem to cToken");
     142 |         }
     143 |         // This happens before reading the balance state to get the most up to date cash balance
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\AccountAction.sol:187`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     185 |         if (account != spender) {
     186 |             uint256 allowance = LibStorage.getPCashTransferAllowance()[account][spender][currencyId];
>>>  187 |             require(allowance >= withdrawAmountPrimeCash, "Insufficient allowance");
     188 |             LibStorage.getPCashTransferAllowance()[account][spender][currencyId] = allowance - withdrawAmountPrimeCash;
     189 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\AccountAction.sol:197`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     195 |         balanceState.loadBalanceState(account, currencyId, accountContext);
     196 |         // Cannot withdraw more than existing balance via proxy.
>>>  197 |         require(withdrawAmountPrimeCash <= balanceState.storedCashBalance, "Insufficient Balance");
     198 |         // Overflow is not possible due to uint88
     199 |         balanceState.primeCashWithdraw = int256(withdrawAmountPrimeCash).neg();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\AccountAction.sol:241`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     239 |         balance.loadBalanceState(redeemer, currencyId, context);
     240 | 
>>>  241 |         require(balance.storedNTokenBalance >= tokensToRedeem, "Insufficient tokens");
     242 |         balance.netNTokenSupplyChange = tokensToRedeem.neg();
     243 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\ActionGuards.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |     /// @dev Throws if called by any account other than the owner.
      58 |     modifier onlyOwner() {
>>>   59 |         require(owner == msg.sender, "Ownable: caller is not the owner");
      60 |         _;
      61 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\ActionGuards.sol:64`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      62 | 
      63 |     function _checkValidCurrency(uint16 currencyId) internal view {
>>>   64 |         require(0 < currencyId && currencyId <= maxCurrencyId, "Invalid currency id");
      65 |     }
      66 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\BatchAction.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      65 |             // to sort actions by increasing id enforces that msg.value will only be used once.
      66 |             if (i > 0) {
>>>   67 |                 require(action.currencyId > actions[i - 1].currencyId, "Unsorted actions");
      68 |             }
      69 |             // Loads the currencyId into balance state
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\BatchAction.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 |             // msg.value will never be used in this method because it is non-payable
     136 |             if (i > 0) {
>>>  137 |                 require(action.currencyId > actions[i - 1].currencyId, "Unsorted actions");
     138 |             }
     139 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\BatchAction.sol:195`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     193 |                 // Batch lending requires that the balance state does not go below zero, i.e. it does not allow users
     194 |                 // to borrow variable to lend fixed. That can be accomplished via batchActionWithTrades.
>>>  195 |                 require(primeCashDeposited >= requiredCash, "Insufficient deposit");
     196 |             }
     197 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\BatchAction.sol:234`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     232 |     ) external payable {
     233 |         // NOTE: Re-entrancy is allowed for authorized callback functions.
>>>  234 |         require(authorizedCallbackContract[msg.sender], "Unauthorized");
     235 |         requireValidAccount(account);
     236 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\BatchAction.sol:273`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     271 |             // to sort actions by increasing id enforces that msg.value will only be used once.
     272 |             if (i > 0) {
>>>  273 |                 require(action.currencyId > actions[i - 1].currencyId, "Unsorted actions");
     274 |             }
     275 |             // Loads the currencyId into balance state
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\BatchAction.sol:425`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     423 |         // possible. In the case of ETH, if redeemToUnderlying == false then ETH will be redeemed as WETH.
     424 |         if (balanceState.currencyId != Constants.ETH_CURRENCY_ID) {
>>>  425 |             require(redeemToUnderlying, "Deprecated: Redemption to cToken");
     426 |         }
     427 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\ERC1155Action.sol:269`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     267 |             int256 amount = int256(amounts[i]);
     268 |             int256 balance = amount > 0 ? signedBalanceOf(from, ids[i]) : signedBalanceOf(to, ids[i]);
>>>  269 |             require(balance > 0, "Insufficient Balance");
     270 |             require(balance >= amount.abs(), "Insufficient Balance");
     271 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\ERC1155Action.sol:336`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     334 |         // Technically debt is transferrable inside this method, but for clarity and backwards compatibility
     335 |         // this restriction is applied here.
>>>  336 |         require(!isfCashDebt, "No Debt Transfer");
     337 | 
     338 |         asset.assetType = Constants.FCASH_ASSET_TYPE;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\ERC1155Action.sol:352`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     350 |         for (uint256 i; i < ids.length; i++) {
     351 |             // Require that ids are not duplicated, there is no valid reason to have duplicate ids
>>>  352 |             if (i > 0) require(ids[i] > ids[i - 1], "IDs must be sorted");
     353 | 
     354 |             PortfolioAsset memory asset = assets[i];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\GovernanceAction.sol:71`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      69 | 
      70 |         // Checks
>>>   71 |         require(msg.sender == _pendingOwner, "Ownable: caller != pending owner");
      72 | 
      73 |         // Effects
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:451`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     449 |                 // If this fails it is because the rate anchor and proportion are not set properly by
     450 |                 // governance.
>>>  451 |                 require(newMarket.oracleRate > 0, "IM: implied rate failed");
     452 |             } else {
     453 |                 // Two special cases for the 3 month and 6 month market when interpolating implied rates. The 3 month market
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\InitializeMarketsAction.sol:512`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     510 |                     utilization = parameters.leverageThresholds[i].toUint();
     511 |                     oracleRate = parameters.interestRateParams[i].getInterestRate(utilization);
>>>  512 |                     require(oracleRate != 0, "Oracle rate overflow");
     513 |                 }
     514 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenAction.sol:188`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     186 |         if (allowance > 0) {
     187 |             // This is the specific allowance for the nToken.
>>>  188 |             require(allowance >= amount, "Insufficient allowance");
     189 |             // Overflow checked above
     190 |             nTokenAllowance[from][spender][currencyId] = allowance - amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenAction.sol:194`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     192 |             // This whitelist allowance works across all nTokens
     193 |             allowance = nTokenWhitelist[from][spender];
>>>  194 |             require(allowance >= amount, "Insufficient allowance");
     195 |             // Overflow checked above
     196 |             nTokenWhitelist[from][spender] = allowance - amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenAction.sol:215`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     213 | 
     214 |         uint256 allowance = LibStorage.getPCashTransferAllowance()[from][spender][currencyId];
>>>  215 |         require(allowance >= amount, "Insufficient allowance");
     216 |         LibStorage.getPCashTransferAllowance()[from][spender][currencyId] = allowance - amount;
     217 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenAction.sol:296`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     294 |             // Do not allow debt to accrue during transfer. This would violate standard
     295 |             // expectations around ERC20 transfers
>>>  296 |             require(senderBalance.storedCashBalance > 0, "Insufficient balance");
     297 |             require(amountInt <= senderBalance.storedCashBalance, "Insufficient balance");
     298 |             senderBalance.netCashChange = amountInt.neg();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenAction.sol:297`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     295 |             // expectations around ERC20 transfers
     296 |             require(senderBalance.storedCashBalance > 0, "Insufficient balance");
>>>  297 |             require(amountInt <= senderBalance.storedCashBalance, "Insufficient balance");
     298 |             senderBalance.netCashChange = amountInt.neg();
     299 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenMintAction.sol:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      93 | 
      94 |         int256 tokensToMint = nTokenCalculations.calculateTokensToMint(nToken, primeCashToDeposit, blockTime);
>>>   95 |         require(tokensToMint >= 0, "Invalid token amount");
      96 | 
      97 |         if (nToken.portfolioState.storedAssets.length == 0) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenMintAction.sol:186`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     184 | 
     185 |         // Defensive check to ensure that we do not somehow accrue negative residual cash.
>>>  186 |         require(residualCash >= 0, "Negative residual cash");
     187 |         if (residualCash > 0) {
     188 |             // Any residual cash is donated to the fee reserve rather than the nToken. Because of
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenMintAction.sol:322`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     320 |             // fCash amount actual cannot be negative or zero. Negative would represent something very wrong
     321 |             // since we are lending here. Zero would represent a failed trade.
>>>  322 |             require(0 < fCashAmount, "Deleverage Buffer");
     323 | 
     324 |             // If the actual slippage is greater than the DELEVERAGE_BUFFER than we want to revert here to
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenMintAction.sol:329`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     327 |             // the fCash amount at DELEVERAGE_BUFFER slippage, so this is the the minimum amount of fCash
     328 |             // that we can purchase given the deposit amount.
>>>  329 |             require(fCashAmountAssumed <= fCashAmount, "Deleverage Buffer");
     330 |         }
     331 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenMintAction.sol:346`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     344 |         // The residual remaining should never be more than a dust amount due to how the fCashAmount is
     345 |         // calculated above.
>>>  346 |         require(0 <= residual && residual < 500, "Deleverage Buffer");
     347 |         return (residual, fCashAmount);
     348 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      56 |         });
      57 | 
>>>   58 |         require(newifCashAssets.length == 0, "Cannot redeem via batch, residual");
      59 |         return totalPrimeCash;
      60 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:74`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      72 |         // nTokens cannot be redeemed during the period of time where they require settlement.
      73 |         require(nToken.getNextSettleTime() > block.timestamp, "Requires settlement");
>>>   74 |         require(tokensToRedeem < nToken.totalSupply, "Cannot redeem");
      75 |         PortfolioAsset[] memory newifCashAssets;
      76 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:146`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     144 |         }
     145 | 
>>>  146 |         require(netfCashRemaining == false, "Residuals");
     147 | 
     148 |         return (totalPrimeCash, newifCashAssets);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\nTokenRedeemAction.sol:215`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     213 |             // Cannot redeem liquidity tokens down to zero or this will cause many issues with
     214 |             // market initialization.
>>>  215 |             require(asset.notional > 0, "Cannot redeem to zero");
     216 |             require(asset.storageState == AssetStorageState.NoChange);
     217 |             asset.storageState = AssetStorageState.Update;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TradingAction.sol:189`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     187 |                 account, cashGroup, market, tradeType, blockTime, trade
     188 |             );
>>>  189 |             require(cashAmount != 0, "Trade failed, liquidity");
     190 | 
     191 |             // This is a little ugly but required to deal with stack issues. We know the market is loaded
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TradingAction.sol:242`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     240 |             if (tradeType == TradeActionType.Borrow) {
     241 |                 // Do not allow borrows over the rate limit
>>>  242 |                 require(postFeeInterestRate <= rateLimit, "Trade failed, slippage");
     243 |             } else {
     244 |                 // Do not allow lends under the rate limit
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TradingAction.sol:245`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     243 |             } else {
     244 |                 // Do not allow lends under the rate limit
>>>  245 |                 require(postFeeInterestRate >= rateLimit, "Trade failed, slippage");
     246 |             }
     247 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TradingAction.sol:273`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     271 |         uint256 maturity = uint256(uint32(uint256(trade) >> 216));
     272 |         int256 fCashAmountToPurchase = int88(uint88(uint256(trade) >> 128));
>>>  273 |         require(maturity > blockTime, "Invalid maturity");
     274 |         // Require that the residual to purchase does not fall on an existing maturity (i.e.
     275 |         // it is an idiosyncratic maturity)
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TreasuryAction.sol:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      49 |     /// @dev Harvest methods are only callable by the authorized treasury manager contract
      50 |     modifier onlyManagerContract() {
>>>   51 |         require(treasuryManagerContract == msg.sender, "Treasury manager required");
      52 |         _;
      53 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TreasuryAction.sol:92`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      90 |         require(nTokenAddress != address(0));
      91 |         // Sanity check that emissions rate is not specified in 1e8 terms.
>>>   92 |         require(newEmissionRate < Constants.INTERNAL_TOKEN_PRECISION, "Invalid rate");
      93 | 
      94 |         nTokenSupply.setIncentiveEmissionRate(nTokenAddress, newEmissionRate, block.timestamp);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TreasuryAction.sol:160`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     158 |         for (uint256 i; i < currencies.length; ++i) {
     159 |             // Prevents duplicate currency IDs
>>>  160 |             if (i > 0) require(currencies[i] > currencies[i - 1], "IDs must be sorted");
     161 | 
     162 |             uint16 currencyId = currencies[i];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TreasuryAction.sol:202`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     200 |         for (uint256 i; i < currencies.length; ++i) {
     201 |             // Prevents duplicate currency IDs
>>>  202 |             if (i > 0) require(currencies[i] > currencies[i - 1], "IDs must be sorted");
     203 | 
     204 |             uint16 currencyId = currencies[i];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\TreasuryAction.sol:297`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     295 |     /// @param currencyId currency id
     296 |     function rebalance(uint16 currencyId) external override nonReentrant {
>>>  297 |         require(msg.sender == rebalancingBot, "Unauthorized");
     298 | 
     299 |         // The gelato bot cannot skip the cooldown check.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultAccountHealth.sol:71`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      69 |         // may exit in full at any time.)
      70 |         if (vaultAccount.vaultShares > 0) {
>>>   71 |             require(collateralRatio <= vaultConfig.maxRequiredAccountCollateralRatio, "Above Max Collateral");
      72 |         }
      73 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultAccountHealth.sol:74`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      72 |         }
      73 | 
>>>   74 |         require(vaultConfig.minCollateralRatio <= collateralRatio, "Insufficient Collateral");
      75 |     }
      76 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultAccountHealth.sol:279`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     277 |             (h, er) = VaultValuation.calculateAccountHealthFactors(vaultConfig, vaultAccount, vaultState, primeRates);
     278 |             // Require account is eligible for liquidation
>>>  279 |             require(h.collateralRatio < vaultConfig.minCollateralRatio , "Sufficient Collateral");
     280 |         }
     281 |         
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultAction.sol:189`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     187 |             vaultConfig, account, maturity, underlyingToBorrow, maxBorrowRate, netPrimeCashOne, netPrimeCashTwo, pr
     188 |         );
>>>  189 |         require(netPrimeCashOne >= 0, "Insufficient Secondary Borrow");
     190 |         require(netPrimeCashTwo >= 0, "Insufficient Secondary Borrow");
     191 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultAction.sol:190`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     188 |         );
     189 |         require(netPrimeCashOne >= 0, "Insufficient Secondary Borrow");
>>>  190 |         require(netPrimeCashTwo >= 0, "Insufficient Secondary Borrow");
     191 | 
     192 |         underlyingTokensTransferred[0] = _transferSecondary(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultLiquidationAction.sol:312`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     310 |         // Vault accounts that are not settled must be settled first by calling settleVaultAccount
     311 |         // before liquidation. settleVaultAccount is not permissioned so anyone may settle the account.
>>>  312 |         require(block.timestamp < vaultAccount.maturity, "Must Settle");
     313 | 
     314 |         if (vaultAccount.maturity == Constants.PRIME_CASH_VAULT_MATURITY) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\actions\VaultLiquidationAction.sol:374`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     372 |         // vault at the same maturity). If the liquidator has fCash in the current maturity then their collateral
     373 |         // ratio will increase as a result of the liquidation, no need to check their collateral position.
>>>  374 |         require(liquidator.maturity == 0 || liquidator.maturity == maturity, "Maturity Mismatch"); // dev: has vault shares
     375 |         liquidator.maturity = maturity;
     376 |         liquidator.vaultShares = liquidator.vaultShares.add(vaultSharesToLiquidator);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\ChainlinkAdapter.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |                 /*uint80 answeredInRound*/
      58 |             ) = sequencerUptimeOracle.latestRoundData();
>>>   59 |             require(answer == 0, "Sequencer Down");
      60 |             require(SEQUENCER_UPTIME_GRACE_PERIOD < block.timestamp - startedAt, "Sequencer Grace Period");
      61 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\ChainlinkAdapter.sol:60`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      58 |             ) = sequencerUptimeOracle.latestRoundData();
      59 |             require(answer == 0, "Sequencer Down");
>>>   60 |             require(SEQUENCER_UPTIME_GRACE_PERIOD < block.timestamp - startedAt, "Sequencer Grace Period");
      61 |         }
      62 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\ChainlinkAdapter.sol:72`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      70 |             /* answeredInRound */
      71 |         ) = quoteToUSDOracle.latestRoundData();
>>>   72 |         require(quoteRate > 0, "Chainlink Rate Error");
      73 |         if (invertQuote) quoteRate = (quoteToUSDDecimals * quoteToUSDDecimals) / quoteRate;
      74 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\ChainlinkAdapter.sol:93`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      91 |             answeredInRound
      92 |         ) = baseToUSDOracle.latestRoundData();
>>>   93 |         require(baseToUSD > 0, "Chainlink Rate Error");
      94 |         // Overflow and div by zero not possible
      95 |         if (invertBase) baseToUSD = (baseToUSDDecimals * baseToUSDDecimals) / baseToUSD;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\cTokenAggregator.sol:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      60 |         uint256 borrowRateMantissa = _getBorrowRate(totalCash, borrowsPrior, reservesPrior);
      61 | 
>>>   62 |         require(borrowRateMantissa <= 0.0005e16, "RATE_TOO_HIGH"); // Same as borrowRateMaxMantissa in CTokenInterfaces.sol
      63 | 
      64 |         // Interest accumulated = (borrowRate * blocksSinceLastAccrual * borrowsPrior) / 1e18
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:76`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      74 |         packedEmissionRatePerYear = FloatingPoint.packTo56Bits(_emissionRatePerYear);
      75 |         lastAccumulatedTime = uint32(block.timestamp);
>>>   76 |         require(lastAccumulatedTime < _endTime, "Invalid End Time");
      77 |         endTime = _endTime;
      78 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      92 |         returns (uint256 rewardToClaim)
      93 |     {
>>>   94 |         require(!detached, "Detached");
      95 |         require(lastAccumulatedTime <= blockTime, "Invalid block time");
      96 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      93 |     {
      94 |         require(!detached, "Detached");
>>>   95 |         require(lastAccumulatedTime <= blockTime, "Invalid block time");
      96 | 
      97 |         uint256 totalSupply = IERC20(NTOKEN_ADDRESS).totalSupply();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:129`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     127 |     /// @param _endTime time in seconds when incentive period will end
     128 |     function setIncentiveEmissionRate(uint128 _emissionRatePerYear, uint32 _endTime) external onlyOwner {
>>>  129 |         require(!detached, "Detached");
     130 |         uint256 totalSupply = IERC20(NTOKEN_ADDRESS).totalSupply();
     131 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 |         // lastAccumulatedTime is at block.timestamp here, ensure that the end time is always
     136 |         // further in the future.
>>>  137 |         require(lastAccumulatedTime < _endTime, "Invalid End Time");
     138 |         endTime = _endTime;
     139 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:166`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     164 |     /// offline and merkle root uploaded to this contract
     165 |     function detach() external override onlyNotional {
>>>  166 |         require(!detached, "Already detached");
     167 | 
     168 |         // accumulate for the last time if needed
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:190`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     188 |         override
     189 |     {
>>>  190 |         require(detached, "Not detached");
     191 | 
     192 |         _checkProof(account, nTokenBalanceAtDetach, proof);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:210`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     208 |         uint256 priorNTokenSupply
     209 |     ) external override onlyNotional {
>>>  210 |         require(!detached, "Detached");
     211 |         require(currencyId == CURRENCY_ID, "Wrong currency id");
     212 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:211`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     209 |     ) external override onlyNotional {
     210 |         require(!detached, "Detached");
>>>  211 |         require(currencyId == CURRENCY_ID, "Wrong currency id");
     212 | 
     213 |         _accumulateRewardPerNToken(uint32(block.timestamp), priorNTokenSupply);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\adapters\SecondaryRewarder.sol:304`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     302 |         bytes32 leaf = keccak256(abi.encodePacked(account, balance));
     303 |         bool isValidLeaf = MerkleProof.verify(proof, merkleRoot, leaf);
>>>  304 |         require(isValidLeaf, "NotInMerkle");
     305 |     }
     306 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:201`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     199 |             "GovernorAlpha::propose: proposal function information arity mismatch"
     200 |         );
>>>  201 |         require(targets.length != 0, "GovernorAlpha::propose: must provide actions");
     202 |         require(
     203 |             targets.length <= PROPOSAL_MAX_OPERATIONS,
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:285`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     283 |         {
     284 |             Proposal storage proposal = proposals[proposalId];
>>>  285 |             require(computedOperationHash == proposal.operationHash, "Operation hash mismatch");
     286 |         }
     287 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:330`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     328 | 
     329 |         bytes32 computedOperationHash = _computeHash(targets, values, calldatas, proposalId);
>>>  330 |         require(computedOperationHash == proposal.operationHash, "Operation hash mismatch");
     331 |         // Execute batch will revert if the call has not been scheduled
     332 |         _executeBatch(targets, values, calldatas, proposalId);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:354`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     352 |     function cancelProposal(uint256 proposalId) public {
     353 |         ProposalState proposalState = state(proposalId);
>>>  354 |         require(proposalState != ProposalState.Executed, "Proposal already executed");
     355 | 
     356 |         Proposal storage proposal = proposals[proposalId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:458`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     456 |         Proposal storage proposal = proposals[proposalId];
     457 |         Receipt storage receipt = receipts[proposalId][voter];
>>>  458 |         require(receipt.hasVoted == false, "GovernorAlpha::_castVote: voter already voted");
     459 |         uint96 votes = note.getPriorVotes(voter, proposal.startBlock);
     460 |         // Short circuit if voter has no votes
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:508`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     506 |     function updateVotingPeriodBlocks(uint32 newVotingPeriodBlocks) external {
     507 |         require(msg.sender == address(this), "Unauthorized caller");
>>>  508 |         require(newVotingPeriodBlocks >= MIN_VOTING_PERIOD_BLOCKS, "Below min voting period");
     509 |         votingPeriodBlocks = newVotingPeriodBlocks;
     510 |         emit UpdateVotingPeriodBlocks(newVotingPeriodBlocks);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:515`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     513 |     /// @dev Hidden public method
     514 |     function __abdicate() external {
>>>  515 |         require(msg.sender == guardian, "GovernorAlpha::__abdicate: sender must be gov guardian");
     516 |         guardian = address(0);
     517 |         emit Abdicate();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:536`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     534 |     function _add96(uint96 a, uint96 b) private pure returns (uint96) {
     535 |         uint96 c = a + b;
>>>  536 |         require(c >= a, "addition overflow");
     537 |         return c;
     538 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\GovernorAlpha.sol:543`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     541 |     function _add32(uint32 a, uint32 b) private pure returns (uint32) {
     542 |         uint32 c = a + b;
>>>  543 |         require(c >= a, "addition overflow");
     544 |         return c;
     545 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\NoteERC20.sol:106`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     104 |         for (uint256 i = 0; i < initialGrantAmount.length; i++) {
     105 |             totalGrants = _add96(totalGrants, initialGrantAmount[i], "");
>>>  106 |             require(balances[initialAccounts[i]] == 0, "Duplicate account");
     107 |             balances[initialAccounts[i]] = initialGrantAmount[i];
     108 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\NoteERC20.sol:117`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     115 | 
     116 |     modifier onlyOwner() {
>>>  117 |         require(owner == msg.sender, "Ownable: caller is not the owner");
     118 |         _;
     119 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\NoteERC20.sol:239`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     237 |         bytes32 s
     238 |     ) public {
>>>  239 |         require(block.timestamp <= expiry, "Note::delegateBySig: signature expired");
     240 |         bytes32 domainSeparator =
     241 |             keccak256(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\NoteERC20.sol:248`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     246 |         // ECDSA will check if address is zero inside
     247 |         address signatory = ECDSA.recover(digest, v, r, s);
>>>  248 |         require(nonce == nonces[signatory]++, "Note::delegateBySig: invalid nonce");
     249 |         _delegate(signatory, delegatee);
     250 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\NoteERC20.sol:267`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     265 |     /// @return The number of votes the account had as of the given block
     266 |     function getPriorVotes(address account, uint256 blockNumber) public view returns (uint96) {
>>>  267 |         require(blockNumber < block.number, "Note::getPriorVotes: not yet determined");
     268 | 
     269 |         uint32 nCheckpoints = numCheckpoints[account];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\Reservoir.sol:45`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      43 |         address target_
      44 |     ) {
>>>   45 |         require(dripRate_ > 0, "Drip rate cannot be zero");
      46 | 
      47 |         DRIP_START = block.timestamp;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\Reservoir.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |     function drip() public returns (uint256 amountToDrip) {
      58 |         uint256 reservoirBalance = TOKEN.balanceOf(address(this));
>>>   59 |         require(reservoirBalance > 0, "Reservoir empty");
      60 |         uint256 blockTime = block.timestamp;
      61 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\governance\Reservoir.sol:70`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      68 |         // will be compliant because it is the NOTE contract
      69 |         bool success = TOKEN.transfer(TARGET, amountToDrip);
>>>   70 |         require(success, "Transfer failed");
      71 |         emit ReservoirDrip(TARGET, amountToDrip);
      72 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\liquidators\BaseLiquidator.sol:82`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      80 | 
      81 |     modifier onlyOwner() {
>>>   82 |         require(owner == msg.sender, "Ownable: caller is not the owner");
      83 |         _;
      84 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:319`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     317 |             require(utilization < uint256(Constants.RATE_PRECISION), "Over Utilization");
     318 |             // Cannot overflow the new market's max rate
>>>  319 |             require(market.lastImpliedRate < irParams.maxRate, "Over Max Rate");
     320 | 
     321 |             if (utilization <= irParams.kinkUtilization1) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\external\patchfix\MigratePrimeCash.sol:403`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     401 |         // NOTE: inside this method we are accessing storage values directly since it is inside a delegate call context.
     402 |         uint256 maxMarketIndex = CashGroup.getMaxMarketIndex(currencyId);
>>>  403 |         require(fCashCurves.length == maxMarketIndex, "market index length");
     404 | 
     405 |         MarketParameters[] memory markets = new MarketParameters[](maxMarketIndex);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\AccountContextHandler.sol:50`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      48 |     ) internal pure {
      49 |         require(!isBitmapEnabled(accountContext), "Cannot change bitmap");
>>>   50 |         require(0 < currencyId && currencyId <= Constants.MAX_CURRENCIES, "Invalid currency id");
      51 | 
      52 |         // Account cannot have assets or debts
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\AccountContextHandler.sol:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      51 | 
      52 |         // Account cannot have assets or debts
>>>   53 |         require(accountContext.assetArrayLength == 0, "Cannot have assets");
      54 |         require(accountContext.hasDebt == 0x00, "Cannot have debt");
      55 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\AccountContextHandler.sol:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      52 |         // Account cannot have assets or debts
      53 |         require(accountContext.assetArrayLength == 0, "Cannot have assets");
>>>   54 |         require(accountContext.hasDebt == 0x00, "Cannot have debt");
      55 | 
      56 |         // Ensure that the active currency is set to false in the array so that there is no double
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\BalanceHandler.sol:195`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     193 |                 // During liquidation, liquidators may have negative net cash change a token has transfer fees, however, in
     194 |                 // LiquidationHelpers.finalizeLiquidatorLocal they are not allowed to go into debt.
>>>  195 |                 require(accountContext.allowPrimeBorrow, "No Prime Borrow");
     196 |                 checkDebtCap = true;
     197 |             }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\BalanceHandler.sol:212`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     210 |                 .add(balanceState.netNTokenSupplyChange);
     211 |             // Ensure that nToken balances never become negative
>>>  212 |             require(finalNTokenBalance >= 0, "Neg nToken");
     213 | 
     214 |             // overflow checked above
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\BalanceHandler.sol:265`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     263 |         // the netCashChange must be positive so that it is coming out of debt.
     264 |         if (newCashBalance < 0) {
>>>  265 |             require(netPrimeCashChange > 0, "Neg Cash");
     266 |             // NOTE: HAS_CASH_DEBT cannot be extinguished except by a free collateral check
     267 |             // where all balances are examined. In this case the has cash debt flag should
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\TokenHandler.sol:200`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     198 |                 );
     199 |             } else {
>>>  200 |                 require(underlyingExternalDeposit == msg.value, "ETH Balance");
     201 |             }
     202 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\protocols\CompoundHandler.sol:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      25 | 
      26 |         uint256 success = CErc20Interface(assetToken.tokenAddress).redeem(assetAmountExternal);
>>>   27 |         require(success == COMPOUND_RETURN_CODE_NO_ERROR, "Redeem");
      28 | 
      29 |         uint256 endingBalance = address(this).balance;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\protocols\CompoundHandler.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      40 | 
      41 |         uint256 success = CErc20Interface(assetToken.tokenAddress).redeem(assetAmountExternal);
>>>   42 |         require(success == COMPOUND_RETURN_CODE_NO_ERROR, "Redeem");
      43 | 
      44 |         uint256 endingBalance = IERC20(underlyingToken.tokenAddress).balanceOf(address(this));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\balances\protocols\GenericToken.sol:106`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     104 |         }
     105 | 
>>>  106 |         require(success, "ERC20");
     107 |     }
     108 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\liquidation\LiquidateCurrency.sol:157`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     155 |         LiquidationFactors memory factors
     156 |     ) internal pure returns (int256) {
>>>  157 |         require(factors.localPrimeAvailable < 0, "No local debt");
     158 |         require(factors.collateralAssetAvailable > 0, "No collateral");
     159 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\liquidation\LiquidateCurrency.sol:158`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     156 |     ) internal pure returns (int256) {
     157 |         require(factors.localPrimeAvailable < 0, "No local debt");
>>>  158 |         require(factors.collateralAssetAvailable > 0, "No collateral");
     159 | 
     160 |         (
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\liquidation\LiquidatefCash.sol:449`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     447 |             // or else we won't be able to net off the correct amount. We also require that the account
     448 |             // does not have debt so that we do not have to run a free collateral check here
>>>  449 |             require(liquidatorContext.hasDebt == 0x00, "Has debt"); // dev: token has transfer fee, no liquidator balance
     450 | 
     451 |             // Net off the cash balance for the liquidator. If the cash balance goes negative here then it will revert.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\liquidation\LiquidationHelpers.sol:267`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     265 |         bool redeemToUnderlying
     266 |     ) internal returns (AccountContext memory) {
>>>  267 |         require(redeemToUnderlying, "Deprecated: Redeem to cToken");
     268 |         BalanceState memory balance;
     269 |         balance.loadBalanceState(liquidator, collateralCurrencyId, liquidatorContext);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\markets\CashGroup.sol:116`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     114 |         uint256 blockTime
     115 |     ) internal view {
>>>  116 |         require(1 <= marketIndex && marketIndex <= cashGroup.maxMarketIndex, "Invalid market");
     117 |         uint256 maturity =
     118 |             DateTime.getReferenceTime(blockTime).add(DateTime.getTradedMarket(marketIndex));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\markets\DateTime.sol:43`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      41 |         uint256 blockTime
      42 |     ) internal pure returns (bool) {
>>>   43 |         require(maxMarketIndex > 0, "CG: no markets listed");
      44 |         require(maxMarketIndex <= Constants.MAX_TRADED_MARKET_INDEX, "CG: market index bound");
      45 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\markets\DateTime.sol:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      42 |     ) internal pure returns (bool) {
      43 |         require(maxMarketIndex > 0, "CG: no markets listed");
>>>   44 |         require(maxMarketIndex <= Constants.MAX_TRADED_MARKET_INDEX, "CG: market index bound");
      45 | 
      46 |         if (maturity % Constants.QUARTER != 0) return false;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\markets\InterestRateCurve.sol:564`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     562 |         require(netUnderlyingToAccount != 0);
     563 |         // Cannot borrow more than total cash underlying
>>>  564 |         require(netUnderlyingToAccount <= totalCashUnderlying, "Over Market Limit");
     565 | 
     566 |         int256 fCash_0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\markets\Market.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      29 |         returns (int256 liquidityTokens, int256 fCash)
      30 |     {
>>>   31 |         require(market.totalLiquidity > 0, "M: zero liquidity");
      32 |         if (primeCash == 0) return (0, 0);
      33 |         require(primeCash > 0); // dev: negative asset cash
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\markets\Market.sol:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     119 |         // during this time, but market initialization can be called by anyone so the actual time that this condition
     120 |         // exists for should be quite short.
>>>  121 |         require(oracleRate > 0, "Market not initialized");
     122 | 
     123 |         return
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenCalculations.sol:46`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      44 |             uint256 nextSettleTime = nTokenHandler.getNextSettleTime(nToken);
      45 |             // If next settle time <= blockTime then the token can be settled
>>>   46 |             require(nextSettleTime > blockTime, "Requires settlement");
      47 |         }
      48 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenCalculations.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      65 |             int256 deviationInRP = nTokenOracleValue.sub(nTokenSpotValue).abs()
      66 |                 .divInRatePrecision(nTokenOracleValue);
>>>   67 |             require(deviationInRP <= maxValueDeviationRP, "Over Deviation Limit");
      68 | 
      69 |             // Use the larger PV when minting nTokens to ensure that the minting is at the lower price
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:65`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      63 |         mapping(address => nTokenContext) storage contextStore = LibStorage.getNTokenContextStorage();
      64 |         nTokenContext storage context = contextStore[tokenAddress];
>>>   65 |         require(context.currencyId == 0, "PT: currency exists");
      66 | 
      67 |         // This will initialize all other context slots to zero
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:85`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      83 |         nTokenContext storage context = store[tokenAddress];
      84 | 
>>>   85 |         require(liquidationHaircutPercentage <= Constants.PERCENTAGE_DECIMALS, "Invalid haircut");
      86 |         // The pv haircut percentage must be less than the liquidation percentage or else liquidators will not
      87 |         // get profit for liquidating nToken.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:88`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      86 |         // The pv haircut percentage must be less than the liquidation percentage or else liquidators will not
      87 |         // get profit for liquidating nToken.
>>>   88 |         require(pvHaircutPercentage < liquidationHaircutPercentage, "Invalid pv haircut");
      89 |         // The mint deviation percentage cannot be greater than the difference between the liquidation haircut
      90 |         // percentage and the pv haircut percentage.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:97`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      95 |         // Ensure that the cash withholding buffer is greater than the residual purchase incentive or
      96 |         // the nToken may not have enough cash to pay accounts to buy its negative ifCash
>>>   97 |         require(residualPurchaseIncentive10BPS <= cashWithholdingBuffer10BPS, "Invalid discounts");
      98 | 
      99 |         bytes6 parameters = (
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:177`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     175 |             "PT: deposit share length"
     176 |         );
>>>  177 |         require(depositShares.length == leverageThresholds.length, "PT: leverage share length");
     178 | 
     179 |         uint256 shareSum;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:204`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     202 |         uint32[] calldata proportions
     203 |     ) internal {
>>>  204 |         require(annualizedAnchorRates.length <= Constants.MAX_TRADED_MARKET_INDEX, "PT: annualized anchor rates length");
     205 |         require(proportions.length == annualizedAnchorRates.length, "PT: proportions length");
     206 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\nToken\nTokenHandler.sol:205`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     203 |     ) internal {
     204 |         require(annualizedAnchorRates.length <= Constants.MAX_TRADED_MARKET_INDEX, "PT: annualized anchor rates length");
>>>  205 |         require(proportions.length == annualizedAnchorRates.length, "PT: proportions length");
     206 | 
     207 |         for (uint256 i; i < proportions.length; i++) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\pCash\PrimeRateLib.sol:447`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     445 |         MarketParameters memory market;
     446 |         market.loadSettlementMarket(currencyId, maturity, maturity);
>>>  447 |         require(market.totalLiquidity == 0, "Must init markets");
     448 | 
     449 |         // totalDebt is negative, but netPrimeSupplyChange and netPrimeDebtChange must both be positive
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\pCash\PrimeSupplyCap.sol:32`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      30 |         if (maxUnderlyingSupply == 0) return;
      31 | 
>>>   32 |         require(totalUnderlyingSupply <= maxUnderlyingSupply, "Over Supply Cap");
      33 |     }
      34 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\pCash\PrimeSupplyCap.sol:43`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      41 |         if (maxUnderlyingDebt == 0) return;
      42 | 
>>>   43 |         require(totalUnderlyingDebt <= maxUnderlyingDebt, "Over Debt Cap");
      44 |     }
      45 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\valuation\FreeCollateral.sol:527`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     525 | 
     526 |         liquidationFactors.netETHValue = factors.netETHValue;
>>>  527 |         require(liquidationFactors.netETHValue < 0, "Sufficient collateral");
     528 | 
     529 |         // Refetch the portfolio if it exists, AssetHandler.getNetCashValue updates values in memory to do fCash
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\vaults\VaultAccount.sol:164`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     162 |             // NOTE: use 1 to represent the minimum amount of vault shares due to rounding in the
     163 |             // vaultSharesToLiquidator calculation
>>>  164 |             require(vaultAccount.accountDebtUnderlying == 0 || vaultAccount.vaultShares <= 1, "Min Borrow");
     165 |         }
     166 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\vaults\VaultSecondaryBorrow.sol:331`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     329 |         if (checkMinBorrow) {
     330 |             // No overflow on negation due to overflow checks above
>>>  331 |             require(accountDebtOne == 0 || vaultConfig.minAccountSecondaryBorrow[0] <= -accountDebtOne, "min borrow");
     332 |             require(accountDebtTwo == 0 || vaultConfig.minAccountSecondaryBorrow[1] <= -accountDebtTwo, "min borrow");
     333 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\vaults\VaultSecondaryBorrow.sol:332`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     330 |             // No overflow on negation due to overflow checks above
     331 |             require(accountDebtOne == 0 || vaultConfig.minAccountSecondaryBorrow[0] <= -accountDebtOne, "min borrow");
>>>  332 |             require(accountDebtTwo == 0 || vaultConfig.minAccountSecondaryBorrow[1] <= -accountDebtTwo, "min borrow");
     333 |         }
     334 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\internal\vaults\VaultSecondaryBorrow.sol:397`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     395 | 
     396 |             // Require that borrows always succeed
>>>  397 |             if (netDebtInUnderlying < 0) require(netPrimeCash > 0, "Borrow Failed");
     398 |         }
     399 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\proxy\EmptyProxy.sol:12`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      10 | 
      11 |     modifier onlyOwner() {
>>>   12 |         require(owner == msg.sender, "Ownable: caller is not the owner");
      13 |         _;
      14 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\proxy\EmptyProxy.sol:17`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      15 | 
      16 |     function _authorizeUpgrade(address /* */) internal view override {
>>>   17 |         require(owner == msg.sender, "Unauthorized upgrade");
      18 |     }
      19 | 
```
</details>

---

## Oracle (3)

### [!] Oracle Price Missing Staleness Check
- **File:** `contracts\external\adapters\ChainlinkAdapter.sol:71`
- **Severity:** MEDIUM
**Problem:** latestRoundData() at line 71 has no updatedAt/staleness guard. A stopped or delayed feed keeps returning the last price, letting trades execute at a stale rate advantageously to one side.
**Fix:** Revert when block.timestamp - updatedAt exceeds the feed heartbeat threshold and when answeredInRound < roundId.
---
### [!] Oracle Price Missing Staleness Check
- **File:** `contracts\external\adapters\ChainlinkAdapter.sol:92`
- **Severity:** MEDIUM
**Problem:** latestRoundData() at line 92 has no updatedAt/staleness guard. A stopped or delayed feed keeps returning the last price, letting trades execute at a stale rate advantageously to one side.
**Fix:** Revert when block.timestamp - updatedAt exceeds the feed heartbeat threshold and when answeredInRound < roundId.
---
### [!] Oracle Price Missing Staleness Check
- **File:** `contracts\internal\valuation\ExchangeRate.sol:77`
- **Severity:** MEDIUM
**Problem:** latestRoundData() at line 77 has no updatedAt/staleness guard. A stopped or delayed feed keeps returning the last price, letting trades execute at a stale rate advantageously to one side.
**Fix:** Revert when block.timestamp - updatedAt exceeds the feed heartbeat threshold and when answeredInRound < roundId.
---


---
*Generated by BugHunter*