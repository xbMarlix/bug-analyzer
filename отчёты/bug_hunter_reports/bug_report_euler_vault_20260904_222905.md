# BugHunter Report: euler_vault

**Generated:** 2026-09-04 22:29:05
**Project:** `C:\Users\123123\Desktop\euler_vault`
**Analyzers:** static, ast, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 442 |
| Total lines | 29,561 |
| Bugs found | 199 |
| !! High | 11 |
| ! Medium | 147 |
| ~ Low | 41 |

### Languages Detected

- **solidity**: 216 files
- **bash**: 4 files
- **python**: 3 files

## Security (36)

### [!!] Unsafe Delegatecall

- **File:** `src\EVault\Dispatch.sol:105`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     103 | 
     104 |     // External function which is only callable by the EVault itself. Its purpose is to be static called by
>>>  105 |     // `delegateToModuleView` which allows view functions to be implemented in modules, even though delegatecall cannot
     106 |     // be directly used within view functions.
     107 |     function viewDelegate() external payable {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `src\EVault\Dispatch.sol:113`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     111 |             let size := sub(calldatasize(), 36)
     112 |             calldatacopy(0, 36, size)
>>>  113 |             let result := delegatecall(gas(), calldataload(4), 0, size, 0, 0)
     114 |             returndatacopy(0, 0, returndatasize())
     115 |             switch result
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `src\EVault\Dispatch.sol:124`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     122 |         assembly {
     123 |             calldatacopy(0, 0, calldatasize())
>>>  124 |             let result := delegatecall(gas(), module, 0, calldatasize(), 0, 0)
     125 |             returndatacopy(0, 0, returndatasize())
     126 |             switch result
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `src\GenericFactory\BeaconProxy.sol:66`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      64 |             let implementation := mload(0)
      65 | 
>>>   66 |             // delegatecall to the implementation with trailing metadata
      67 |             calldatacopy(0, 0, calldatasize())
      68 |             mstore(calldatasize(), metadata0_)
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `src\GenericFactory\BeaconProxy.sol:72`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      70 |             mstore(add(64, calldatasize()), metadata2_)
      71 |             mstore(add(96, calldatasize()), metadata3_)
>>>   72 |             result := delegatecall(gas(), implementation, 0, add(metadataLength_, calldatasize()), 0, 0)
      73 |             returndatacopy(0, 0, returndatasize())
      74 | 
```
</details>

---

### [!!] Selfdestruct Used

- **File:** `test\mocks\TestERC20.sol:283`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** selfdestruct sends all remaining ETH to a target and destroys the contract, potentially bricking funds.

**Fix:** Avoid selfdestruct unless absolutely necessary and carefully reviewed.

<details>
<summary>Code</summary>

```
     281 | 
     282 |     // Compiling this function causes deprecation warnings
>>>  283 |     //function callSelfDestruct() external secured {
     284 |     //    selfdestruct(payable(address(0)));
     285 |     //}
```
</details>

---

### [!!] Selfdestruct Used

- **File:** `test\mocks\TestERC20.sol:284`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** selfdestruct sends all remaining ETH to a target and destroys the contract, potentially bricking funds.

**Fix:** Avoid selfdestruct unless absolutely necessary and carefully reviewed.

<details>
<summary>Code</summary>

```
     282 |     // Compiling this function causes deprecation warnings
     283 |     //function callSelfDestruct() external secured {
>>>  284 |     //    selfdestruct(payable(address(0)));
     285 |     //}
     286 | 
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\invariants\base\BaseHandler.t.sol:93`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      91 |     function _safeApprove(address token, address spender, uint256 amount) internal {
      92 |         (bool success, bytes memory retdata) =
>>>   93 |             token.call(abi.encodeWithSelector(IERC20.approve.selector, spender, amount));
      94 |         assert(success);
      95 |         if (retdata.length > 0) assert(abi.decode(retdata, (bool)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:46`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      44 |         eTST.setGovernorAdmin(address(this));
      45 | 
>>>   46 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
      47 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
      48 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:47`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      45 | 
      46 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
>>>   47 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
      48 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
      49 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:48`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      46 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
      47 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
>>>   48 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
      49 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
      50 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:49`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      47 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
      48 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
>>>   49 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
      50 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
      51 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:50`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      48 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
      49 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
>>>   50 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
      51 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
      52 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:51`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      49 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
      50 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
>>>   51 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
      52 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
      53 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:52`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      50 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
      51 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
>>>   52 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
      53 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
      54 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:53`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      51 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
      52 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
>>>   53 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
      54 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
      55 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:54`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      52 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
      53 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
>>>   54 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
      55 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
      56 |     }
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:55`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      53 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
      54 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
>>>   55 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
      56 |     }
      57 | 
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:91`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      89 |         // calls through the EVC are unauthorized, even if the authenticated account is the governor's sub-account
      90 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>   91 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
      92 |         vm.expectRevert(Errors.E_Unauthorized.selector);
      93 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:93`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      91 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
      92 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>   93 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
      94 |         vm.expectRevert(Errors.E_Unauthorized.selector);
      95 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:95`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      93 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
      94 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>   95 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
      96 |         vm.expectRevert(Errors.E_Unauthorized.selector);
      97 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:97`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      95 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setMaxLiquidationDiscount, 0));
      96 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>   97 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
      98 |         vm.expectRevert(Errors.E_Unauthorized.selector);
      99 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:99`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      97 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setLiquidationCoolOffTime, 0));
      98 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>   99 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
     100 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     101 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:101`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      99 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
     100 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  101 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
     102 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     103 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setConfigFlags, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:103`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     101 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
     102 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  103 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setConfigFlags, 0));
     104 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     105 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setCaps, (0, 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:105`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     103 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setConfigFlags, 0));
     104 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  105 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setCaps, (0, 0)));
     106 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     107 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:107`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     105 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setCaps, (0, 0)));
     106 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  107 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
     108 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     109 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:109`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     107 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
     108 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  109 |         evc.call(address(eTST), subAccount, 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
     110 | 
     111 |         // set address(1) as the operator
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:118`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     116 |         vm.startPrank(address(1));
     117 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  118 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
     119 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     120 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:120`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     118 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setFeeReceiver, address(0)));
     119 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  120 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
     121 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     122 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:122`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     120 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setLTV, (address(0), 0, 0, 0)));
     121 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  122 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
     123 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     124 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:124`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     122 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestRateModel, address(0)));
     123 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  124 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
     125 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     126 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:126`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     124 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setHookConfig, (address(0), 0)));
     125 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  126 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
     127 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     128 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:128`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     126 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setConfigFlags, 0));
     127 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  128 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
     129 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     130 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:130`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     128 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setCaps, (0, 0)));
     129 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  130 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
     131 |         vm.expectRevert(Errors.E_Unauthorized.selector);
     132 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:132`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
     130 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setInterestFee, 0.1e4));
     131 |         vm.expectRevert(Errors.E_Unauthorized.selector);
>>>  132 |         evc.call(address(eTST), address(this), 0, abi.encodeCall(eTST.setGovernorAdmin, address(0)));
     133 |         vm.stopPrank();
     134 | 
```
</details>

---

## Logic (33)

### [!!] block.number For Randomness

- **File:** `src\EVault\modules\Initialize.sol:96`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
      94 | 
      95 |             while (len > 0) {
>>>   96 |                 output[--len] = bytes1(uint8(48 + n % 10)); // 48 is ASCII '0'
      97 |                 n /= 10;
      98 |             }
```
</details>

---

### [!!] block.number For Randomness

- **File:** `test\invariants\utils\Pretty.sol:68`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
      66 | 
      67 |         while (n != 0) {
>>>   68 |             r = n % 10;
      69 |             n /= 10;
      70 |             place++;
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\mocks\MockBalanceTracker.sol:29`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'length' is modified at line 29, after an external call at line 27. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      27 |         (bool success, bytes memory result) = address(_reentrantCall.to).call(_reentrantCall.data);
      28 |         if (success) return;
>>>   29 |         if (result.length == 0) revert();
      30 |         assembly {
      31 |             revert(add(32, result), mload(result))
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Governance\governorOnly.t.sol:139`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'controller' is modified at line 139, after an external call at line 132. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     137 | 
     138 |         // enable malicious controller for the governor
>>>  139 |         MaliciousController controller = new MaliciousController(evc);
     140 |         evc.enableController(address(this), address(controller));
     141 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `certora\harness\ERC4626Harness.sol:26`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      24 |         // is called
      25 |         vaultCache = loadVault();
>>>   26 |         if(block.timestamp - vaultCache.lastInterestAccumulatorUpdate > 0) {
      27 |             vaultStorage.lastInterestAccumulatorUpdate = vaultCache.lastInterestAccumulatorUpdate;
      28 |             vaultStorage.accumulatedFees = vaultCache.accumulatedFees;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\EVault\modules\Liquidation.sol:243`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     241 |     function isInLiquidationCoolOff(address account) private view returns (bool) {
     242 |         unchecked {
>>>  243 |             return block.timestamp < getLastAccountStatusCheckTimestamp(account) + vaultStorage.liquidationCoolOffTime;
     244 |         }
     245 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\EVault\shared\types\LTVConfig.sol:40`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      38 |         }
      39 | 
>>>   40 |         if (block.timestamp >= self.targetTimestamp || self.liquidationLTV >= self.initialLiquidationLTV) {
      41 |             return self.liquidationLTV;
      42 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\Synths\EulerSavingsRate.sol:183`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     181 |     function interestAccruedFromCache(ESRSlot memory esrSlotCache) internal view returns (uint256) {
     182 |         // If distribution ended, full amount is accrued
>>>  183 |         if (block.timestamp >= esrSlotCache.interestSmearEnd) {
     184 |             return esrSlotCache.interestLeft;
     185 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\Synths\IRMSynth.sol:92`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      90 | 
      91 |         // If not time to update yet, return the last rate
>>>   92 |         if (block.timestamp < irmCache.lastUpdated + ADJUST_INTERVAL) {
      93 |             return (rate, updated);
      94 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `test\invariants\base\BaseTest.t.sol:35`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      33 |     /// @dev Solves medusa backward time warp issue
      34 |     modifier monotonicTimestamp() virtual {
>>>   35 |         if (block.timestamp < eTST.getLastInterestAccumulatorUpdate()) {
      36 |             vm.warp(eTST.getLastInterestAccumulatorUpdate());
      37 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `test\mocks\TestERC20.sol:228`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     226 |         require(signatory != address(0), "permit: invalid signature");
     227 |         require(signatory == holder, "permit: unauthorized");
>>>  228 |         require(block.timestamp <= deadline, "permit: signature expired");
     229 | 
     230 |         allowance[holder][spender] = value;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\esr\ESR.General.t.sol:131`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'balanceOfAddress1' is modified at line 131, after an external call at line 128. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     129 |         vm.stopPrank();
     130 | 
>>>  131 |         uint256 balanceOfAddress1 = esr.balanceOf(address(1));
     132 |         assertEq(balanceOfAddress1, balanceOfUser);
     133 |     }
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:86`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'collateralValue' is modified at line 86, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      84 |         (maxRepay, yield) = eTST.checkLiquidation(liquidator, borrower, address(eTST2));
      85 | 
>>>   86 |         uint256 collateralValue = eTST2.balanceOf(borrower) * 5e17 / 1e18;
      87 |         uint256 liquiditycollateralValue = collateralValue * uint256(eTST.LTVLiquidation(address(eTST2))) / 1e4;
      88 |         uint256 liabilityValue = eTST.debtOf(borrower);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:87`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'liquiditycollateralValue' is modified at line 87, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      85 | 
      86 |         uint256 collateralValue = eTST2.balanceOf(borrower) * 5e17 / 1e18;
>>>   87 |         uint256 liquiditycollateralValue = collateralValue * uint256(eTST.LTVLiquidation(address(eTST2))) / 1e4;
      88 |         uint256 liabilityValue = eTST.debtOf(borrower);
      89 |         uint256 discountFactor = liquiditycollateralValue * 1e18 / liabilityValue;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:88`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'liabilityValue' is modified at line 88, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      86 |         uint256 collateralValue = eTST2.balanceOf(borrower) * 5e17 / 1e18;
      87 |         uint256 liquiditycollateralValue = collateralValue * uint256(eTST.LTVLiquidation(address(eTST2))) / 1e4;
>>>   88 |         uint256 liabilityValue = eTST.debtOf(borrower);
      89 |         uint256 discountFactor = liquiditycollateralValue * 1e18 / liabilityValue;
      90 |         uint256 expectedMaxRepayValue = collateralValue * discountFactor / 1e18;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:89`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'discountFactor' is modified at line 89, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      87 |         uint256 liquiditycollateralValue = collateralValue * uint256(eTST.LTVLiquidation(address(eTST2))) / 1e4;
      88 |         uint256 liabilityValue = eTST.debtOf(borrower);
>>>   89 |         uint256 discountFactor = liquiditycollateralValue * 1e18 / liabilityValue;
      90 |         uint256 expectedMaxRepayValue = collateralValue * discountFactor / 1e18;
      91 |         uint256 expectedMaxYieldValue = collateralValue;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:90`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedMaxRepayValue' is modified at line 90, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      88 |         uint256 liabilityValue = eTST.debtOf(borrower);
      89 |         uint256 discountFactor = liquiditycollateralValue * 1e18 / liabilityValue;
>>>   90 |         uint256 expectedMaxRepayValue = collateralValue * discountFactor / 1e18;
      91 |         uint256 expectedMaxYieldValue = collateralValue;
      92 |         uint256 expectedRepayValue = expectedMaxRepayValue * eTST.debtOf(borrower) / liabilityValue;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:91`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedMaxYieldValue' is modified at line 91, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      89 |         uint256 discountFactor = liquiditycollateralValue * 1e18 / liabilityValue;
      90 |         uint256 expectedMaxRepayValue = collateralValue * discountFactor / 1e18;
>>>   91 |         uint256 expectedMaxYieldValue = collateralValue;
      92 |         uint256 expectedRepayValue = expectedMaxRepayValue * eTST.debtOf(borrower) / liabilityValue;
      93 |         uint256 expectedYield = expectedMaxYieldValue * eTST2.balanceOf(borrower) / collateralValue;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:92`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedRepayValue' is modified at line 92, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      90 |         uint256 expectedMaxRepayValue = collateralValue * discountFactor / 1e18;
      91 |         uint256 expectedMaxYieldValue = collateralValue;
>>>   92 |         uint256 expectedRepayValue = expectedMaxRepayValue * eTST.debtOf(borrower) / liabilityValue;
      93 |         uint256 expectedYield = expectedMaxYieldValue * eTST2.balanceOf(borrower) / collateralValue;
      94 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:93`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedYield' is modified at line 93, after an external call at line 60. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      91 |         uint256 expectedMaxYieldValue = collateralValue;
      92 |         uint256 expectedRepayValue = expectedMaxRepayValue * eTST.debtOf(borrower) / liabilityValue;
>>>   93 |         uint256 expectedYield = expectedMaxYieldValue * eTST2.balanceOf(borrower) / collateralValue;
      94 | 
      95 |         assertEq(maxRepay, expectedRepayValue);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\nested.t.sol:293`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'outstandingDebt' is modified at line 293, after an external call at line 284. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     291 | 
     292 |         eTST.approve(address(eTSTNested), type(uint256).max);
>>>  293 |         uint256 outstandingDebt = eTSTNested.debtOf(liquidator);
     294 |         assertEq(outstandingDebt, maxRepay);
     295 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:29`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value' is modified at line 29, after an external call at line 27. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      27 |         assetTST.transfer(address(eTST), amount);
      28 | 
>>>   29 |         uint256 value = 1e7;
      30 | 
      31 |         assertEq(eTST.balanceOf(user), 0);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:47`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value1' is modified at line 47, after an external call at line 45. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      45 |         assetTST.transfer(address(eTST), amount);
      46 | 
>>>   47 |         uint256 value1 = 22e18;
      48 | 
      49 |         assertEq(eTST.balanceOf(user), 0);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:54`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value2' is modified at line 54, after an external call at line 45. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      52 |         eTST.skim(value1, user);
      53 | 
>>>   54 |         uint256 value2 = 1e18;
      55 | 
      56 |         eTST.skim(value2, user);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:62`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value3' is modified at line 62, after an external call at line 45. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      60 |         assertEq(eTST.balanceOf(user), value2 * 2);
      61 | 
>>>   62 |         uint256 value3 = 18e18;
      63 | 
      64 |         eTST.skim(value3, user);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:76`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value' is modified at line 76, after an external call at line 74. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      74 |         assetTST.transfer(address(eTST), amount);
      75 | 
>>>   76 |         uint256 value = 0;
      77 | 
      78 |         assertEq(eTST.balanceOf(user), 0);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:80`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'result' is modified at line 80, after an external call at line 74. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      78 |         assertEq(eTST.balanceOf(user), 0);
      79 | 
>>>   80 |         uint256 result = eTST.skim(value, user);
      81 | 
      82 |         assertEq(result, value);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:91`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value' is modified at line 91, after an external call at line 89. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      89 |         assetTST.transfer(address(eTST), amount);
      90 | 
>>>   91 |         uint256 value = type(uint256).max;
      92 | 
      93 |         assertEq(eTST.balanceOf(user), 0);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:95`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'result' is modified at line 95, after an external call at line 89. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      93 |         assertEq(eTST.balanceOf(user), 0);
      94 | 
>>>   95 |         uint256 result = eTST.skim(value, user);
      96 | 
      97 |         assertEq(result, amount);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:109`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value' is modified at line 109, after an external call at line 107. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     107 |         assetTST.transfer(address(eTST), amount);
     108 | 
>>>  109 |         uint256 value = MAX_SANE_AMOUNT;
     110 | 
     111 |         assertEq(eTST.balanceOf(user), 0);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:116`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'result' is modified at line 116, after an external call at line 107. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     114 |         eTST.skim(value + 1, user);
     115 | 
>>>  116 |         uint256 result = eTST.skim(value, user);
     117 | 
     118 |         assertEq(result, value);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:130`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value' is modified at line 130, after an external call at line 128. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     128 |         assetTST.transfer(address(eTST), amount);
     129 | 
>>>  130 |         uint256 value = 1e18;
     131 | 
     132 |         vm.expectRevert(Errors.E_BadSharesReceiver.selector);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:141`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'value' is modified at line 141, after an external call at line 139. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     139 |         assetTST.transfer(address(eTST), amount);
     140 | 
>>>  141 |         uint256 value = 1e18;
     142 | 
     143 |         eTST.skim(value, address(1));
```
</details>

---

## Resource Management (89)

### [!] Fixed-Gas Transfer

- **File:** `src\EVault\EVault.sol:41`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      39 | 
      40 | 
>>>   41 |     function transfer(address to, uint256 amount) public virtual override callThroughEVC returns (bool) { return super.transfer(to, amount); }
      42 | 
      43 |     function transferFrom(address from, address to, uint256 amount) public virtual override callThroughEVC returns (bool) { return super.transferFrom(from, to, amount); }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\invariant\SimpleCriticalChecks.t.sol:112`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     110 |         amount = boundAmount(amount);
     111 | 
>>>  112 |         try selectedVault.transfer(to, amount) {
     113 |             assertTrue(true);
     114 |         } catch (bytes memory reason) {
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\invariants\handlers\simulators\DonationAttackHandler.t.sol:35`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      33 |         _token.mint(address(this), amount);
      34 | 
>>>   35 |         _token.transfer(vaultAddress, amount);
      36 |     }
      37 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\esr\ESR.General.t.sol:128`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     126 | 
     127 |         vm.startPrank(user);
>>>  128 |         esr.transfer(address(1), balanceOfUser);
     129 |         vm.stopPrank();
     130 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\DToken.t.sol:60`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      58 |         vm.expectRevert(Errors.E_NotSupported.selector);
      59 |         vm.prank(caller);
>>>   60 |         dToken.transfer(to, amount);
      61 |     }
      62 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\DToken.t.sol:89`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      87 | 
      88 |         vm.expectEmit();
>>>   89 |         emit Events.Transfer(address(0), user, amount);
      90 |         vm.prank(user);
      91 |         eTST.borrow(amount, user);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\DToken.t.sol:107`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     105 | 
     106 |         vm.expectEmit();
>>>  107 |         emit Events.Transfer(user, address(0), amountRepay);
     108 |         vm.prank(user);
     109 |         eTST.repay(amountRepay, user);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\DToken.t.sol:125`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     123 | 
     124 |         vm.expectEmit();
>>>  125 |         emit Events.Transfer(user, address(0), amountRepayWithShares);
     126 |         eTST.repayWithShares(amountRepayWithShares, user);
     127 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\DToken.t.sol:145`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     143 | 
     144 |         vm.expectEmit();
>>>  145 |         emit Events.Transfer(user, address(0), amountPull);
     146 |         vm.expectEmit();
     147 |         emit Events.Transfer(address(0), user2, amountPull);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\DToken.t.sol:147`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     145 |         emit Events.Transfer(user, address(0), amountPull);
     146 |         vm.expectEmit();
>>>  147 |         emit Events.Transfer(address(0), user2, amountPull);
     148 |         vm.prank(user2);
     149 |         eTST.pullDebt(amountPull, user);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\BalanceForwarder\hooks.t.sol:103`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     101 |     function test_OnTransfer_Origin() public {
     102 |         vm.prank(alice);
>>>  103 |         eTST.transfer(bob, 1 ether);
     104 |         assertEq(MBT.calls(alice, 9 ether, false), 1);
     105 |         assertBalance(alice, 9 ether);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\BalanceForwarder\hooks.t.sol:110`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     108 |     function test_OnTransfer_Receiver() public {
     109 |         vm.prank(alice);
>>>  110 |         eTST.transfer(bob, 1 ether);
     111 |         assertEq(MBT.calls(bob, 1 ether, false), 1);
     112 |         assertBalance(bob, 1 ether);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Governance\disabledOpsAndFlags.t.sol:137`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     135 |         vm.assume(to != address(this) && to != depositor && to != address(0));
     136 |         vm.expectRevert(Errors.E_OperationDisabled.selector);
>>>  137 |         eTST.transfer(to, amount);
     138 | 
     139 |         // re-enable
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Governance\disabledOpsAndFlags.t.sol:143`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     141 |         uint256 balance = eTST.balanceOf(depositor);
     142 |         vm.prank(depositor);
>>>  143 |         eTST.transfer(to, balance);
     144 |     }
     145 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Governance\disabledOpsAndFlags.t.sol:320`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     318 |         (uint256 amount, address eTSTAddr) = abi.decode(data, (uint256, address));
     319 |         // return the amount to the
>>>  320 |         IERC20(eTSTAddr).transfer(address(eTST), amount);
     321 |     }
     322 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Governance\hookedOps.t.sol:157`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     155 |         // the operation succeeds which proves that it's not affected if the hook target call succeeds
     156 |         vm.startPrank(receiver);
>>>  157 |         eTST.transfer(sender, amount);
     158 |         assertEq(eTST.balanceOf(sender), amount);
     159 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Governance\hookedOps.t.sol:164`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     162 |         MockHookTarget(hookTarget1).setExpectedDataHash(keccak256(data));
     163 |         vm.expectRevert(MockHookTarget.ExpectedData.selector);
>>>  164 |         eTST.transfer(sender, amount);
     165 | 
     166 |         // change the hook target
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Governance\hookedOps.t.sol:304`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     302 |             MockHookTarget(hookTarget).setExpectedDataHash(keccak256(data));
     303 |             vm.expectRevert(MockHookTarget.ExpectedData.selector);
>>>  304 |             eTST.transfer(address1, amount);
     305 | 
     306 |             vm.assume(address1 != CHECKACCOUNT_CALLER && address2 != address(0));
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Liquidation\basic.t.sol:60`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      58 |         uint256 assetTST2LiquidatorInitialBalance = 5e18;
      59 |         startHoax(borrower);
>>>   60 |         assetTST2.transfer(liquidator, assetTST2LiquidatorInitialBalance);
      61 |         startHoax(liquidator);
      62 |         assetTST2.approve(address(eTST2), type(uint256).max);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:22`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      20 | 
      21 |         vm.expectEmit();
>>>   22 |         emit Events.Transfer(alice, bob, amount);
      23 |         vm.prank(alice);
      24 |         bool success = eTST.transfer(bob, amount);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:24`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      22 |         emit Events.Transfer(alice, bob, amount);
      23 |         vm.prank(alice);
>>>   24 |         bool success = eTST.transfer(bob, amount);
      25 | 
      26 |         assertTrue(success);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:37`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      35 | 
      36 |         // vm.expectEmit();
>>>   37 |         // emit Events.Transfer(alice, bob, 0);
      38 |         vm.prank(alice);
      39 |         bool success = eTST.transfer(bob, 0);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:39`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      37 |         // emit Events.Transfer(alice, bob, 0);
      38 |         vm.prank(alice);
>>>   39 |         bool success = eTST.transfer(bob, 0);
      40 | 
      41 |         assertTrue(success);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:58`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      56 | 
      57 |         vm.prank(alice);
>>>   58 |         eTST.transfer(bob, amount);
      59 | 
      60 |         assertEq(MockBalanceTracker(balanceTracker).calls(alice, balance - amount, false), 1);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:71`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      69 | 
      70 |         vm.prank(alice);
>>>   71 |         eTST.transfer(bob, amount);
      72 | 
      73 |         assertFalse(eTST.balanceForwarderEnabled(alice));
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:86`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      84 |         vm.expectRevert(Errors.E_InsufficientBalance.selector);
      85 |         vm.prank(alice);
>>>   86 |         eTST.transfer(bob, amount);
      87 |     }
      88 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:97`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      95 |         vm.expectRevert(Errors.E_SelfTransfer.selector);
      96 |         vm.prank(alice);
>>>   97 |         eTST.transfer(alice, amount);
      98 |     }
      99 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:108`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     106 |         vm.expectRevert(Errors.E_BadSharesReceiver.selector);
     107 |         vm.prank(alice);
>>>  108 |         eTST.transfer(address(0), amount);
     109 |     }
     110 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:124`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     122 |         vm.prank(alice);
     123 |         vm.expectRevert(Errors.E_Reentrancy.selector);
>>>  124 |         eTST.transfer(bob, 0.5 ether);
     125 |         assertEq(eTST.balanceOf(bob), 0);
     126 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:140`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     138 | 
     139 |         vm.expectEmit();
>>>  140 |         emit Events.Transfer(alice, bob, amount);
     141 |         vm.prank(bob);
     142 |         bool success = eTST.transferFrom(alice, bob, amount);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Token\actions.t.sol:160`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     158 | 
     159 |         // vm.expectEmit();
>>>  160 |         // emit Events.Transfer(alice, bob, 0);
     161 |         vm.prank(bob);
     162 |         bool success = eTST.transferFrom(alice, bob, 0);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\balancesNoInterest.t.sol:45`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      43 | 
      44 |         vm.expectEmit();
>>>   45 |         emit Events.Transfer(address(0), user1, 10e18);
      46 |         vm.expectEmit();
      47 |         emit Events.Deposit(user1, user1, 10e18, 10e18);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\balancesNoInterest.t.sol:73`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      71 | 
      72 |         vm.expectEmit();
>>>   73 |         emit Events.Transfer(user1, address(0), 10e18);
      74 |         vm.expectEmit();
      75 |         emit Events.Withdraw(user1, user1, user1, 10e18, 10e18);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\balancesWithInterest.t.sol:241`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     239 | 
     240 |         startHoax(user2);
>>>  241 |         assetTST.transfer(address(eTST), 1e18);
     242 | 
     243 |         // no change
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:248`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     246 | 
     247 |         // transfering some minted asset to borrower2
>>>  248 |         assetTST2.transfer(borrower2, 10e18);
     249 |         vm.stopPrank();
     250 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:612`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     610 |         emit Events.Borrow(borrower, borrow1);
     611 |         vm.expectEmit(dTST);
>>>  612 |         emit Events.Transfer(address(0), borrower, borrow1);
     613 | 
     614 |         eTST.borrow(borrow1, borrower);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:628`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     626 |         emit Events.Borrow(borrower, borrow2);
     627 |         vm.expectEmit(dTST);
>>>  628 |         emit Events.Transfer(address(0), borrower, borrow2 + interest1);
     629 | 
     630 |         eTST.borrow(borrow2, borrower);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:644`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     642 |         emit Events.Repay(borrower, repay1);
     643 |         vm.expectEmit(dTST);
>>>  644 |         emit Events.Transfer(borrower, address(0), repay1 - interest2);
     645 | 
     646 |         eTST.repay(repay1, borrower);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:660`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     658 |         emit Events.Repay(borrower, repay2);
     659 |         vm.expectEmit(dTST);
>>>  660 |         emit Events.Transfer(address(0), borrower, interest3 - repay2); // Actually increases debt
     661 | 
     662 |         eTST.repay(repay2, borrower);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:675`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     673 |         emit Events.Repay(borrower, prevDebt + interest4);
     674 |         vm.expectEmit(dTST);
>>>  675 |         emit Events.Transfer(borrower, address(0), prevDebt); // Interest is netted out, repay amount appears less
     676 | 
     677 |         eTST.repay(type(uint256).max, borrower);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:694`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     692 |         eTST.borrow(1, borrower);
     693 | 
>>>  694 |         assetTST2.transfer(borrower2, type(uint256).max / 2);
     695 | 
     696 |         startHoax(borrower2);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:738`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     736 |         eTST.borrow(1, borrower);
     737 | 
>>>  738 |         assetTST2.transfer(borrower2, type(uint256).max / 2);
     739 | 
     740 |         startHoax(borrower2);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:854`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     852 |         assertEq(assetTST.balanceOf(borrower), amountToBorrow);
     853 | 
>>>  854 |         assetTST2.transfer(borrower2, 10e18);
     855 | 
     856 |         startHoax(borrower2);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrowBasic.t.sol:72`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      70 | 
      71 |         vm.expectEmit();
>>>   72 |         emit Events.Transfer(address(0), borrower, 0.4e18);
      73 |         eTST.borrow(0.4e18, borrower);
      74 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\borrowBasic.t.sol:97`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      95 | 
      96 |         vm.expectEmit();
>>>   97 |         emit Events.Transfer(borrower, address(0), 0.5e18);
      98 |         eTST.repay(0.5e18, borrower);
      99 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\caps.t.sol:855`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     853 |         startHoax(user1);
     854 |         vm.expectRevert(Errors.E_OperationDisabled.selector);
>>>  855 |         eTST.transfer(getSubAccount(user1, 1), 5e18);
     856 | 
     857 |         // Remove pause and it succeeds:
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\caps.t.sol:861`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     859 |         eTST.setHookConfig(address(0), 0);
     860 |         startHoax(user1);
>>>  861 |         eTST.transfer(getSubAccount(user1, 1), 5e18);
     862 | 
     863 |         // setup
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\caps.t.sol:1238`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    1236 |             abi.decode(data, (address, address, uint256));
    1237 | 
>>> 1238 |         IERC20(assetTSTAddress).transfer(eTSTAddress, repayAmount);
    1239 |     }
    1240 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\deposit.t.sol:223`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     221 | 
     222 |         vm.startPrank(user);
>>>  223 |         assetTST.transfer(address(eTST), amount);
     224 | 
     225 |         assertEq(assetTST.balanceOf(address(eTST)), amount);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\flashloan.t.sol:36`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      34 |             abi.decode(data, (address, address, uint256));
      35 | 
>>>   36 |         IERC20(assetTSTAddress).transfer(eTSTAddress, repayAmount);
      37 |     }
      38 | }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\liquidity.t.sol:131`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     129 |         assertEq(eTST2.balanceOf(user2), 10e18);
     130 |         vm.expectRevert(Errors.E_AccountLiquidity.selector);
>>>  131 |         eTST2.transfer(user3, 10e18);
     132 | 
     133 |         vm.expectRevert(Errors.E_AccountLiquidity.selector);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\liquidity.t.sol:134`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     132 | 
     133 |         vm.expectRevert(Errors.E_AccountLiquidity.selector);
>>>  134 |         eTST2.transfer(user3, 1.969e18);
     135 | 
     136 |         eTST2.transfer(user3, 1.967e18);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\liquidity.t.sol:136`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     134 |         eTST2.transfer(user3, 1.969e18);
     135 | 
>>>  136 |         eTST2.transfer(user3, 1.967e18);
     137 | 
     138 |         (, uint256[] memory collateralValues, uint256 liabilityValue) = eTST.accountLiquidityFull(user2, false);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\liquidity.t.sol:143`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     141 | 
     142 |         vm.expectRevert(Errors.E_AccountLiquidity.selector);
>>>  143 |         eTST2.transfer(user3, 0.002e18);
     144 |     }
     145 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\nested.t.sol:256`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     254 | 
     255 |         vm.expectRevert(Errors.E_AccountLiquidity.selector);
>>>  256 |         eTST2.transfer(liquidator, 19e18);
     257 | 
     258 |         // transfer collateral to liquidator
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\nested.t.sol:259`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     257 | 
     258 |         // transfer collateral to liquidator
>>>  259 |         eTST2.transfer(liquidator, 10e18);
     260 |         vm.stopPrank();
     261 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\nested.t.sol:284`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     282 |         vm.stopPrank();
     283 |         startHoax(depositor);
>>>  284 |         assetTST.transfer(liquidator, 10e18);
     285 |         vm.stopPrank();
     286 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\pullDebt.t.sol:114`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     112 |         startHoax(user1);
     113 |         vm.expectEmit();
>>>  114 |         emit Events.Transfer(user2, address(0), 0.1e18);
     115 |         vm.expectEmit();
     116 |         emit Events.Transfer(address(0), user1, 0.1e18);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\pullDebt.t.sol:116`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     114 |         emit Events.Transfer(user2, address(0), 0.1e18);
     115 |         vm.expectEmit();
>>>  116 |         emit Events.Transfer(address(0), user1, 0.1e18);
     117 |         eTST.pullDebt(0.1e18, user2);
     118 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\pullDebt.t.sol:160`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     158 | 
     159 |         eTST2.deposit(50e18, user2);
>>>  160 |         eTST2.transfer(getSubAccount(user2, 1), 50e18);
     161 |         evc.enableCollateral(getSubAccount(user2, 1), address(eTST2));
     162 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\pullDebt.t.sol:173`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     171 | 
     172 |         vm.expectEmit();
>>>  173 |         emit Events.Transfer(user2, address(0), 999.998477e6);
     174 |         vm.expectEmit();
     175 |         emit Events.Transfer(address(0), getSubAccount(user2, 1), 1000e6);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\pullDebt.t.sol:175`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     173 |         emit Events.Transfer(user2, address(0), 999.998477e6);
     174 |         vm.expectEmit();
>>>  175 |         emit Events.Transfer(address(0), getSubAccount(user2, 1), 1000e6);
     176 |         evc.batch(items);
     177 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\pullDebt.t.sol:225`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     223 | 
     224 |         eTST2.deposit(50e18, user2);
>>>  225 |         eTST2.transfer(getSubAccount(user2, 1), 50e18);
     226 |         evc.enableCollateral(getSubAccount(user2, 1), address(eTST2));
     227 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\repayWithShares.sol:137`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     135 | 
     136 |         vm.expectEmit();
>>>  137 |         emit Events.Transfer(address(0), user2, 0.4e18);
     138 |         eTST.borrow(0.4e18, user2);
     139 |         eTST.borrow(0.1e18, user2);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:27`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      25 |         uint256 amount = 20e18;
      26 |         vm.startPrank(user);
>>>   27 |         assetTST.transfer(address(eTST), amount);
      28 | 
      29 |         uint256 value = 1e7;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:45`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      43 |         uint256 amount = 20e18;
      44 |         vm.startPrank(user);
>>>   45 |         assetTST.transfer(address(eTST), amount);
      46 | 
      47 |         uint256 value1 = 22e18;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:74`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      72 |         uint256 amount = 20e18;
      73 |         vm.startPrank(user);
>>>   74 |         assetTST.transfer(address(eTST), amount);
      75 | 
      76 |         uint256 value = 0;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:89`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      87 |         uint256 amount = 20e18;
      88 |         vm.startPrank(user);
>>>   89 |         assetTST.transfer(address(eTST), amount);
      90 | 
      91 |         uint256 value = type(uint256).max;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:107`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     105 |         uint256 amount = MAX_SANE_AMOUNT;
     106 |         vm.startPrank(user);
>>>  107 |         assetTST.transfer(address(eTST), amount);
     108 | 
     109 |         uint256 value = MAX_SANE_AMOUNT;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:128`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     126 |         uint256 amount = 20e18;
     127 |         vm.startPrank(user);
>>>  128 |         assetTST.transfer(address(eTST), amount);
     129 | 
     130 |         uint256 value = 1e18;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\skim.t.sol:139`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     137 |         uint256 amount = 20e18;
     138 |         vm.startPrank(user);
>>>  139 |         assetTST.transfer(address(eTST), amount);
     140 | 
     141 |         uint256 value = 1e18;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:44`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      42 | 
      43 |         vm.expectEmit();
>>>   44 |         emit Events.Transfer(user1, user2, 400);
      45 |         vm.expectEmit();
      46 |         emit Events.VaultStatus(1000, 0, 0, 1000, 1e27, 0, block.timestamp);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:47`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      45 |         vm.expectEmit();
      46 |         emit Events.VaultStatus(1000, 0, 0, 1000, 1e27, 0, block.timestamp);
>>>   47 |         eTST.transfer(user2, 400);
      48 | 
      49 |         assertEq(eTST.balanceOf(user1), 600);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:58`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      56 |         eTST.deposit(1000, user1);
      57 | 
>>>   58 |         eTST.transfer(user2, 500);
      59 | 
      60 |         assertEq(eTST.balanceOf(user1), 500);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:65`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      63 |         // no-op, balances of sender and recipient not affected
      64 |         vm.expectEmit();
>>>   65 |         emit Events.Transfer(user1, user2, 0);
      66 |         vm.expectEmit();
      67 |         emit Events.VaultStatus(1000, 0, 0, 1000, 1e27, 0, block.timestamp);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:68`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      66 |         vm.expectEmit();
      67 |         emit Events.VaultStatus(1000, 0, 0, 1000, 1e27, 0, block.timestamp);
>>>   68 |         eTST.transfer(user2, 0);
      69 |     }
      70 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:76`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      74 |         eTST.deposit(1000, user1);
      75 | 
>>>   76 |         eTST.transfer(user2, 500);
      77 |         assertEq(eTST.balanceOf(user1), 500);
      78 |         assertEq(eTST.balanceOf(user2), 500);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:80`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      78 |         assertEq(eTST.balanceOf(user2), 500);
      79 | 
>>>   80 |         eTST.transfer(getSubAccount(user1, 1), 200);
      81 | 
      82 |         // no-op, balances of sender and recipient not affected
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:84`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      82 |         // no-op, balances of sender and recipient not affected
      83 |         vm.expectEmit();
>>>   84 |         emit Events.Transfer(getSubAccount(user1, 1), getSubAccount(user1, 255), 0);
      85 |         vm.expectEmit();
      86 |         emit Events.VaultStatus(1000, 0, 0, 1000, 1e27, 0, block.timestamp);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:100`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      98 |         // MAX_UINT is *not* a short-cut for this:
      99 |         vm.expectRevert(Errors.E_AmountTooLargeToEncode.selector);
>>>  100 |         eTST.transfer(user2, type(uint256).max);
     101 | 
     102 |         vm.expectEmit();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:103`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     101 | 
     102 |         vm.expectEmit();
>>>  103 |         emit Events.Transfer(user1, user2, 1000);
     104 |         vm.expectEmit();
     105 |         emit Events.VaultStatus(1000, 0, 0, 1000, 1e27, 0, block.timestamp);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:135`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     133 |         startHoax(user1);
     134 |         vm.expectEmit();
>>>  135 |         emit Events.Transfer(user2, user3, 300);
     136 |         eTST.transferFrom(user2, user3, 300);
     137 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:172`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     170 |         eTST.deposit(1000, user1);
     171 | 
>>>  172 |         eTST.transfer(getSubAccount(user1, 1), 700);
     173 |         // sub-accounts are not recognized by the vault itself
     174 |         vm.expectRevert(Errors.E_InsufficientAllowance.selector);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:200`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     198 |         // revert on self-transfer of eVault
     199 |         vm.expectRevert(Errors.E_SelfTransfer.selector);
>>>  200 |         eTST.transfer(user1, 10);
     201 | 
     202 |         assertEq(eTST.balanceOf(user1), 1000);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:214`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     212 |         // revert on self-transfer of eVault
     213 |         vm.expectRevert(Errors.E_SelfTransfer.selector);
>>>  214 |         eTST.transfer(user1, 0);
     215 | 
     216 |         assertEq(eTST.balanceOf(user1), 1000);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\modules\Vault\transferShares.t.sol:228`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     226 |         // revert on self-transfer of eVault
     227 |         vm.expectRevert(Errors.E_SelfTransfer.selector);
>>>  228 |         eTST.transfer(user1, 1);
     229 | 
     230 |         assertEq(eTST.balanceOf(user1), 1000);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\shared\Reentrancy.t.sol:44`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      42 | 
      43 |         vm.expectRevert(Errors.E_Reentrancy.selector);
>>>   44 |         eTST.transfer(account1, amount1);
      45 | 
      46 |         vm.expectRevert(Errors.E_Reentrancy.selector);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\shared\Reentrancy.t.sol:235`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     233 | 
     234 |         vm.expectRevert(Errors.E_Reentrancy.selector);
>>>  235 |         eTST.transfer(account1, amount1);
     236 | 
     237 |         vm.expectRevert(Errors.E_Reentrancy.selector);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\evault\shared\Reentrancy.t.sol:429`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     427 |         MockHookTarget(hookTarget).setEVault(address(eTST));
     428 | 
>>>  429 |         eTST.transfer(address(2), 0);
     430 |     }
     431 | }
```
</details>

---

## Performance (25)

### [~] Unoptimized Loop

- **File:** `test\invariant\SimpleCriticalChecks.t.sol:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      51 | 
      52 |         if (bytes4(msg.data) != EntryPoint(address(this)).liquidate.selector) {
>>>   53 |             for (uint256 i = 0; i < account.length; i++) {
      54 |                 address[] memory controllers = evc.getControllers(account[i]);
      55 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariant\SimpleCriticalChecks.t.sol:371`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     369 | 
     370 |         if (errors.length > 0) {
>>>  371 |             for (uint256 i = 0; i < errors.length; i++) {
     372 |                 console.log(errors[i]);
     373 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\Invariants.t.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      40 | 
      41 |         uint256 _sumBalanceOf;
>>>   42 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
      43 |             assert_TM_INVARIANT_B(actorAddresses[i]);
      44 |             _sumBalanceOf += eTST.balanceOf(actorAddresses[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\Invariants.t.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 | 
      68 |     function echidna_ERC4626_ACTIONS_INVARIANT() public monotonicTimestamp returns (bool) {
>>>   69 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
      70 |             assert_ERC4626_DEPOSIT_INVARIANT_A(actorAddresses[i]);
      71 |             assert_ERC4626_MINT_INVARIANT_A(actorAddresses[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\Invariants.t.sol:83`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      81 | 
      82 |     function echidna_BM_INVARIANT() public monotonicTimestamp returns (bool) {
>>>   83 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
      84 |             assert_BM_INVARIANT_A(actorAddresses[i]);
      85 |             assert_BM_INVARIANT_J(actorAddresses[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\Setup.t.sol:128`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     126 |         tokens[1] = address(assetTST2);
     127 | 
>>>  128 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
     129 |             // Deply actor proxies and approve system contracts
     130 |             address _actor = _setUpActor(addresses[i], tokens, vaults);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\invariants\BorrowingModuleInvariants.t.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 | 
      68 |     function _getDebtSum() internal view returns (uint256 totalDebt) {
>>>   69 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
      70 |             totalDebt += eTST.debtOf(address(actorAddresses[i]));
      71 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\invariants\VaultModuleInvariants.t.sol:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      53 |         bool notFirstLoop;
      54 | 
>>>   55 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
      56 |             vm.prank(actorAddresses[i]);
      57 |             uint256 tempShares = eTST.convertToShares(_assets);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\invariants\VaultModuleInvariants.t.sol:74`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      72 |         bool notFirstLoop;
      73 | 
>>>   74 |         for (uint256 i; i < NUMBER_OF_ACTORS; i++) {
      75 |             vm.prank(actorAddresses[i]);
      76 |             uint256 tempAssets = eTST.convertToAssets(_shares);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\utils\Actor.sol:19`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      17 |         tokens = _tokens;
      18 |         callers = _callers;
>>>   19 |         for (uint256 i = 0; i < tokens.length; i++) {
      20 |             IERC20(tokens[i]).approve(callers[i], type(uint256).max);
      21 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\utils\Pretty.sol:16`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      14 |         uint256 j;
      15 | 
>>>   16 |         for (i = 0; i < _baseBytes.length; i++) {
      17 |             _newValue[j++] = _baseBytes[i];
      18 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\utils\Pretty.sol:20`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      18 |         }
      19 | 
>>>   20 |         for (i = 0; i < _valueBytes.length; i++) {
      21 |             _newValue[j++] = _valueBytes[i];
      22 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\utils\Pretty.sol:132`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     130 |     function uintToBitString(uint256 n, uint16 bits) internal pure returns (string memory) {
     131 |         string memory s = "";
>>>  132 |         for (uint256 i; i < bits; i++) {
     133 |             if (n % 2 == 0) {
     134 |                 s = Strings.concat("0", s);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\utils\PropertiesAsserts.sol:396`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     394 |     function toString(address value) internal pure returns (string memory str) {
     395 |         bytes memory s = new bytes(40);
>>>  396 |         for (uint256 i = 0; i < 20; i++) {
     397 |             bytes1 b = bytes1(uint8(uint256(uint160(value)) / (2 ** (8 * (19 - i)))));
     398 |             bytes1 hi = bytes1(uint8(b) / 16);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariants\utils\StdAsserts.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 |         ok = true;
      68 |         if (a.length == b.length) {
>>>   69 |             for (uint256 i = 0; i < a.length; i++) {
      70 |                 if (a[i] != b[i]) {
      71 |                     ok = false;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\evault\modules\Governance\disabledOpsAndFlags.t.sol:264`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     262 |         liquidateSetup(liquidator1);
     263 |         Vm.Log[] memory entries = vm.getRecordedLogs();
>>>  264 |         for (uint256 i = 0; i < entries.length; i++) {
     265 |             bytes32 topic = entries[i].topics[0];
     266 |             assertNotEq(topic, Events.DebtSocialized.selector);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\evault\modules\Governance\disabledOpsAndFlags.t.sol:276`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     274 |         Vm.Log[] memory entriesReEnabled = vm.getRecordedLogs();
     275 |         bool foundLog = false;
>>>  276 |         for (uint256 i = 0; i < entriesReEnabled.length; i++) {
     277 |             bytes32 topic = entriesReEnabled[i].topics[0];
     278 |             if (topic == Events.DebtSocialized.selector) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\evault\modules\Token\views.t.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      19 |         // Numbers are incremented correctly
      20 | 
>>>   21 |         for (uint256 i = 2; i < 120; i++) {
      22 |             IEVault v = IEVault(
      23 |                 factory.createProxy(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:325`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     323 | 
     324 |         // addresses within sub-accounts range revert
>>>  325 |         for (uint160 i; i < 256; i++) {
     326 |             address subacc = address(uint160(subaccBase) | i);
     327 |             if (subacc != borrower) vm.expectRevert(Errors.E_BadAssetReceiver.selector);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:405`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     403 | 
     404 |         // Wait 5 years, touching pool each time so that rpow() will not overflow
>>>  405 |         for (uint256 i; i < 5; i++) {
     406 |             skip(365 * 1 days);
     407 |             eTST.touch();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\evault\modules\Vault\deposit.t.sol:412`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     410 |         // in a loop deposit max assets to create 1 share but not enough for 2. The rounding remainder is a stealth
     411 |         // donation
>>>  412 |         for (uint256 i; i < 1000; i++) {
     413 |             eTST.deposit(2, user1);
     414 |             // 2 were deposited, but they round down to 1 share
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\factory\GenericFactory.t.sol:138`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     136 |         // Create Tokens and activate Vaults
     137 |         uint256 amountEVault = 10;
>>>  138 |         for (uint256 i; i < amountEVault; i++) {
     139 |             TestERC20 TST = new TestERC20("Test Token", "TST", 18, false);
     140 |             MockEVault(factory.createProxy(address(0), true, abi.encodePacked(address(TST))));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\factory\GenericFactory.t.sol:159`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     157 |         address[] memory eVaultsList = new address[](amountEVaults);
     158 | 
>>>  159 |         for (uint256 i; i < amountEVaults; i++) {
     160 |             TestERC20 TST = new TestERC20("Test Token", "TST", 18, false);
     161 |             MockEVault eVault = MockEVault(factory.createProxy(address(0), true, abi.encodePacked(address(TST))));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\factory\GenericFactory.t.sol:186`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     184 | 
     185 |         listEVaultsTest = new address[](endIndex - startIndex);
>>>  186 |         for (uint256 i = startIndex; i < endIndex; i++) {
     187 |             listEVaultsTest[i - startIndex] = eVaultsList[i];
     188 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\factory\GenericFactory.t.sol:311`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     309 |         address[] memory eVaultsList = new address[](amountEVaults);
     310 | 
>>>  311 |         for (uint256 i; i < amountEVaults; i++) {
     312 |             TestERC20 TST = new TestERC20("Test Token", "TST", 18, false);
     313 |             MockEVault eVault = MockEVault(factory.createProxy(address(0), true, abi.encodePacked(address(TST))));
```
</details>

---

## Code Quality (16)

### [~] UNCLEAR require Error Message

- **File:** `certora\harness\ERC4626Harness.sol:39`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      37 | 
      38 |     function toSharesExt(uint256 amount) external view returns (uint256) {
>>>   39 |         require(amount < MAX_SANE_AMOUNT, "Assets are really uint112");
      40 |         VaultCache memory vaultCache = loadVault();
      41 |         return Assets.wrap(uint112(amount)).toSharesDownUint(vaultCache);
```
</details>

---

### [~] Address Is Contract Check

- **File:** `src\EVault\shared\lib\AddressUtils.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      11 | library AddressUtils {
      12 |     function checkContract(address addr) internal view returns (address) {
>>>   13 |         if (addr.code.length == 0) revert Errors.E_BadAddress();
      14 | 
      15 |         return addr;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `src\GenericFactory\BeaconProxy.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      29 |         emit Genesis();
      30 | 
>>>   31 |         require(trailingData.length <= MAX_TRAILING_DATA_LENGTH, "trailing data too long");
      32 | 
      33 |         // Beacon is always the proxy creator; store it in immutable
```
</details>

---

### [~] Address Is Contract Check

- **File:** `src\GenericFactory\GenericFactory.sol:155`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     153 |     /// @dev Upgrades all existing BeaconProxies to the new logic immediately
     154 |     function setImplementation(address newImplementation) external nonReentrant adminOnly {
>>>  155 |         if (newImplementation.code.length == 0) revert E_BadAddress();
     156 |         implementation = newImplementation;
     157 |         emit SetImplementation(newImplementation);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\MockMinimalStatusCheck.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      11 | 
      12 |     function checkAccountStatus(address, address[] calldata) external view returns (bytes4 magicValue) {
>>>   13 |         require(!shouldFail, "MockMinimalStatusCheck: account status check failed");
      14 |         return this.checkAccountStatus.selector;
      15 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\TestERC20.sol:105`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     103 | 
     104 |     function transferFrom(address from, address recipient, uint256 amount) public virtual {
>>>  105 |         require(balances[from] >= amount, "ERC20: transfer amount exceeds balance");
     106 |         address account = getAccount();
     107 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\TestERC20.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 | 
     108 |         if (from != account && allowance[from][account] != type(uint256).max) {
>>>  109 |             require(allowance[from][account] >= amount, "ERC20: transfer amount exceeds allowance");
     110 |             allowance[from][account] -= amount;
     111 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\TestERC20.sol:227`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     225 |         address signatory = ecrecover(digest, v, r, s);
     226 |         require(signatory != address(0), "permit: invalid signature");
>>>  227 |         require(signatory == holder, "permit: unauthorized");
     228 |         require(block.timestamp <= deadline, "permit: signature expired");
     229 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\TestERC20.sol:228`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     226 |         require(signatory != address(0), "permit: invalid signature");
     227 |         require(signatory == holder, "permit: unauthorized");
>>>  228 |         require(block.timestamp <= deadline, "permit: signature expired");
     229 | 
     230 |         allowance[holder][spender] = value;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\evault\EVaultTestBase.t.sol:168`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     166 | 
     167 |     function getSubAccount(address primary, uint8 subAccountId) internal pure returns (address) {
>>>  168 |         require(subAccountId <= 256, "invalid subAccountId");
     169 |         return address(uint160(uint160(primary) ^ subAccountId));
     170 |     }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `test\unit\evault\modules\Governance\hookedOps.t.sol:107`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     105 |         vm.assume(hookedOps & OP_VAULT_STATUS_CHECK == 0);
     106 |         vm.assume(
>>>  107 |             sender.code.length == 0 && receiver.code.length == 0 && !evc.haveCommonOwner(sender, address(0))
     108 |                 && !evc.haveCommonOwner(receiver, address(0)) && !evc.haveCommonOwner(sender, receiver)
     109 |         );
```
</details>

---

### [~] Address Is Contract Check

- **File:** `test\unit\evault\modules\Governance\hookedOps.t.sol:195`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     193 |     function testFuzz_vaultStatusCheckHook(address sender, uint256 amount, address receiver) public {
     194 |         vm.assume(
>>>  195 |             sender.code.length == 0 && receiver.code.length == 0 && !evc.haveCommonOwner(sender, address(0))
     196 |                 && !evc.haveCommonOwner(receiver, address(0)) && !evc.haveCommonOwner(sender, receiver)
     197 |         );
```
</details>

---

### [~] Address Is Contract Check

- **File:** `test\unit\evault\modules\Governance\hookedOps.t.sol:242`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     240 |     {
     241 |         hookedOps = uint32(bound(hookedOps, 0, OP_MAX_VALUE - 1));
>>>  242 |         vm.assume(sender.code.length == 0 && !evc.haveCommonOwner(sender, address(0)));
     243 | 
     244 |         // deploy the hook target
```
</details>

---

### [~] Address Is Contract Check

- **File:** `test\unit\evault\modules\Vault\borrow.t.sol:292`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     290 | 
     291 |     function test_ControllerRequiredOps(address controller, uint112 amount, address account) public {
>>>  292 |         vm.assume(controller.code.length == 0 && uint160(controller) > 256 && controller != console2.CONSOLE_ADDRESS);
     293 |         vm.assume(account != address(0) && account != controller && account != address(evc));
     294 |         vm.assume(amount > 0);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\evault\shared\Reentrancy.t.sol:217`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     215 | 
     216 |         (bool success,) = address(eTST).call(abi.encodeWithSignature("setReentrancyLock()"));
>>>  217 |         require(success, "setReentrancyLock failed");
     218 | 
     219 |         vm.startPrank(sender);
```
</details>

---

### [~] Address Is Contract Check

- **File:** `test\unit\factory\GenericFactory.t.sol:216`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     214 | 
     215 |     function test_isProxy(address proxy) public {
>>>  216 |         vm.assume(proxy.code.length == 0);
     217 | 
     218 |         // Create and install mock eVault impl
```
</details>

---


---
*Generated by BugHunter*