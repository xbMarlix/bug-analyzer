# BugHunter Report: oz_contracts

**Generated:** 2026-09-04 21:52:09
**Project:** `C:\Users\123123\Desktop\oz_contracts`
**Analyzers:** static, ast

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 723 |
| Total lines | 99,717 |
| Bugs found | 160 |
| !!! Critical | 2 |
| !! High | 38 |
| ! Medium | 18 |
| ~ Low | 97 |
| i Info | 5 |

### Languages Detected

- **solidity**: 419 files
- **javascript**: 237 files
- **typescript**: 52 files
- **bash**: 15 files

## Security (40)

### [!!!] Dangerous Code Execution

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:79`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
      77 |   // Longest target first: multiple remappings may apply, the most specific one is the right one.
      78 |   const item = remappings
>>>   79 |     .map(remapping => remappingRegex.exec(remapping)?.groups ?? {})
      80 |     .filter(
      81 |       ({ context, target }) => [undefined, '', 'project/'].includes(context) && inputSourceName.startsWith(target),
```
</details>

---

### [!!!] Dangerous Code Execution

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\execall.ts:10`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Dynamic code execution detected. This can lead to remote code execution vulnerabilities.

**Fix:** Avoid eval/exec. Use safe alternatives like ast.literal_eval() or specific function calls.

<details>
<summary>Code</summary>

```
       8 | 
       9 |   while (true) {
>>>   10 |     const match = re.exec(text);
      11 | 
      12 |     // We break out of the loop if there is no match or if the empty string is
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\extensions\draft-AccountERC7579.sol:113`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     111 |             (callType == ERC7579Utils.CALLTYPE_SINGLE ||
     112 |                 callType == ERC7579Utils.CALLTYPE_BATCH ||
>>>  113 |                 callType == ERC7579Utils.CALLTYPE_DELEGATECALL) &&
     114 |             (execType == ERC7579Utils.EXECTYPE_DEFAULT || execType == ERC7579Utils.EXECTYPE_TRY);
     115 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\extensions\draft-AccountERC7579.sol:240`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     238 |         if (callType == ERC7579Utils.CALLTYPE_SINGLE) return executionCalldata.execSingle(execType);
     239 |         if (callType == ERC7579Utils.CALLTYPE_BATCH) return executionCalldata.execBatch(execType);
>>>  240 |         if (callType == ERC7579Utils.CALLTYPE_DELEGATECALL) return executionCalldata.execDelegateCall(execType);
     241 |         revert ERC7579Utils.ERC7579UnsupportedCallType(callType);
     242 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\extensions\draft-AccountERC7579.sol:296`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     294 |      * NOTE: The module's {IERC7579Module-onUninstall} callback is invoked without catching reverts, so a buggy or
     295 |      * malicious module can block its own uninstallation by reverting. A forced uninstallation that bypasses this
>>>  296 |      * callback can still be performed through a delegate call (`CALLTYPE_DELEGATECALL`) via {execute}, running logic
     297 |      * in the account's context that clears the module from storage directly.
     298 |      */
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\extensions\draft-AccountERC7579Hooked.sol:86`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      84 |      *
      85 |      * NOTE: Uninstalling the hook runs through its own `withHook` `preCheck`/`postCheck`, so a hook that reverts
>>>   86 |      * there blocks its removal. Since `_execute` is `withHook`-gated too, the delegatecall escape hatch does not
      87 |      * apply, and such a hook may be impossible to uninstall.
      88 |      */
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:31`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      29 |     CallType internal constant CALLTYPE_BATCH = CallType.wrap(0x01);
      30 | 
>>>   31 |     /// @dev A `delegatecall` execution.
      32 |     CallType internal constant CALLTYPE_DELEGATECALL = CallType.wrap(0xFF);
      33 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:32`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      30 | 
      31 |     /// @dev A `delegatecall` execution.
>>>   32 |     CallType internal constant CALLTYPE_DELEGATECALL = CallType.wrap(0xFF);
      33 | 
      34 |     /// @dev Default execution type that reverts on failure.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:97`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      95 | 
      96 |     /// @dev Executes a delegate call.
>>>   97 |     function execDelegateCall(
      98 |         bytes calldata executionCalldata,
      99 |         ExecType execType
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:103`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     101 |         (address target, bytes calldata callData) = decodeDelegate(executionCalldata);
     102 |         returnData = new bytes[](1);
>>>  103 |         returnData[0] = _delegatecall(0, execType, target, callData);
     104 |     }
     105 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:261`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     259 |     }
     260 | 
>>>  261 |     /// @dev Executes a `delegatecall` to the target with the provided {ExecType}.
     262 |     function _delegatecall(
     263 |         uint256 index,
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:262`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     260 | 
     261 |     /// @dev Executes a `delegatecall` to the target with the provided {ExecType}.
>>>  262 |     function _delegatecall(
     263 |         uint256 index,
     264 |         ExecType execType,
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\account\utils\draft-ERC7579Utils.sol:268`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     266 |         bytes calldata data
     267 |     ) private returns (bytes memory) {
>>>  268 |         (bool success, bytes memory returndata) = (target == address(0) ? address(this) : target).delegatecall(data);
     269 |         return _validateExecutionMode(index, execType, success, returndata);
     270 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\crosschain\CrosschainRemoteExecutor.sol:95`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      93 |         } else if (callType == ERC7579Utils.CALLTYPE_BATCH) {
      94 |             executionCalldata.execBatch(execType);
>>>   95 |         } else if (callType == ERC7579Utils.CALLTYPE_DELEGATECALL) {
      96 |             executionCalldata.execDelegateCall(execType);
      97 |         } else revert ERC7579Utils.ERC7579UnsupportedCallType(callType);
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\crosschain\CrosschainRemoteExecutor.sol:96`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      94 |             executionCalldata.execBatch(execType);
      95 |         } else if (callType == ERC7579Utils.CALLTYPE_DELEGATECALL) {
>>>   96 |             executionCalldata.execDelegateCall(execType);
      97 |         } else revert ERC7579Utils.ERC7579UnsupportedCallType(callType);
      98 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\metatx\ERC2771Context.sol:17`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      15 |  * function only accessible if `msg.data.length == 0`.
      16 |  *
>>>   17 |  * WARNING: The usage of `delegatecall` in this contract is dangerous and may result in context corruption.
      18 |  * Any forwarded request to this contract triggering a `delegatecall` to itself will result in an invalid {_msgSender}
      19 |  * recovery.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\metatx\ERC2771Context.sol:18`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      16 |  *
      17 |  * WARNING: The usage of `delegatecall` in this contract is dangerous and may result in context corruption.
>>>   18 |  * Any forwarded request to this contract triggering a `delegatecall` to itself will result in an invalid {_msgSender}
      19 |  * recovery.
      20 |  */
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\Proxy.sol:8`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
       6 | /**
       7 |  * @dev This abstract contract provides a fallback function that delegates all calls to another contract using the EVM
>>>    8 |  * instruction `delegatecall`. We refer to the second contract as the _implementation_ behind the proxy, and it has to
       9 |  * be specified by overriding the virtual {_implementation} function.
      10 |  *
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\Proxy.sol:31`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      29 |             // Call the implementation.
      30 |             // out and outsize are 0 because we don't know the size yet.
>>>   31 |             let result := delegatecall(gas(), implementation, 0x00, calldatasize(), 0x00, 0x00)
      32 | 
      33 |             // Copy the returned data.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\Proxy.sol:37`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      35 | 
      36 |             switch result
>>>   37 |             // delegatecall returns 0 on error.
      38 |             case 0 {
      39 |                 revert(0x00, returndatasize())
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Clones.sol:44`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      42 |      * 0x29   | 54          | SLOAD            | addr 0 cds 0 0             | [0..cds): calldata
      43 |      * 0x2A   | 5a          | GAS              | gas addr 0 cds 0 0         | [0..cds): calldata
>>>   44 |      * 0x2B   | f4          | DELEGATECALL     | success                    |
      45 |      * 0x2C   | 3d          | RETURNDATASIZE   | rds success                |
      46 |      * 0x2D   | 5f          | PUSH0            | 0 rds success              |
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Utils.sol:72`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      70 | 
      71 |         if (data.length > 0) {
>>>   72 |             Address.functionDelegateCall(newImplementation, data);
      73 |         } else {
      74 |             _checkNonPayable();
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\ERC1967\ERC1967Utils.sol:162`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     160 | 
     161 |         if (data.length > 0) {
>>>  162 |             Address.functionDelegateCall(IBeacon(newBeacon).implementation(), data);
     163 |         } else {
     164 |             _checkNonPayable();
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\utils\UUPSUpgradeable.sol:46`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      44 | 
      45 |     /**
>>>   46 |      * @dev Check that the execution is being performed through a delegatecall call and that the execution context is
      47 |      * a proxy contract with an implementation (as defined in ERC-1967) pointing to self. This should only be the case
      48 |      * for UUPS and transparent proxies that are using the current contract as their implementation. Execution of a
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\utils\UUPSUpgradeable.sol:86`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      84 |      * Emits an {Upgraded} event.
      85 |      *
>>>   86 |      * @custom:oz-upgrades-unsafe-allow-reachable delegatecall
      87 |      */
      88 |     function upgradeToAndCall(address newImplementation, bytes memory data) public payable virtual onlyProxy {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\utils\UUPSUpgradeable.sol:94`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      92 | 
      93 |     /**
>>>   94 |      * @dev Reverts if the execution is not performed via delegatecall or the execution
      95 |      * context is not of a proxy with an ERC-1967 compliant implementation pointing to self.
      96 |      */
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\utils\UUPSUpgradeable.sol:99`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      97 |     function _checkProxy() internal view virtual {
      98 |         if (
>>>   99 |             address(this) == __self || // Must be called through delegatecall
     100 |             ERC1967Utils.getImplementation() != __self // Must be called through an active proxy
     101 |         ) {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\utils\UUPSUpgradeable.sol:107`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     105 | 
     106 |     /**
>>>  107 |      * @dev Reverts if the execution is performed via delegatecall.
     108 |      * See {notDelegated}.
     109 |      */
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\proxy\utils\UUPSUpgradeable.sol:112`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     110 |     function _checkNotDelegated() internal view virtual {
     111 |         if (address(this) != __self) {
>>>  112 |             // Must not be called through delegatecall
     113 |             revert UUPSUnauthorizedCallContext();
     114 |         }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\Address.sol:116`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     114 |      * but performing a delegate call.
     115 |      */
>>>  116 |     function functionDelegateCall(address target, bytes memory data) internal returns (bytes memory) {
     117 |         bool success = LowLevelCall.delegatecallNoReturn(target, data);
     118 |         if (success && (LowLevelCall.returnDataSize() > 0 || target.code.length > 0)) {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\LowLevelCall.sol:73`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      71 |     }
      72 | 
>>>   73 |     /// @dev Performs a Solidity function call using a low level `delegatecall` and ignoring the return data.
      74 |     function delegatecallNoReturn(address target, bytes memory data) internal returns (bool success) {
      75 |         assembly ("memory-safe") {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\LowLevelCall.sol:76`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      74 |     function delegatecallNoReturn(address target, bytes memory data) internal returns (bool success) {
      75 |         assembly ("memory-safe") {
>>>   76 |             success := delegatecall(gas(), target, add(data, 0x20), mload(data), 0x00, 0x00)
      77 |         }
      78 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\LowLevelCall.sol:80`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      78 |     }
      79 | 
>>>   80 |     /// @dev Performs a Solidity function call using a low level `delegatecall` and returns the first 64 bytes of the result
      81 |     /// in the scratch space of memory. Useful for functions that return a tuple with two single-word values.
      82 |     ///
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\LowLevelCall.sol:90`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      88 |     ) internal returns (bool success, bytes32 result1, bytes32 result2) {
      89 |         assembly ("memory-safe") {
>>>   90 |             success := delegatecall(gas(), target, add(data, 0x20), mload(data), 0x00, 0x40)
      91 |             result1 := mload(0x00)
      92 |             result2 := mload(0x20)
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\Multicall.sol:17`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      15 |  *
      16 |  * NOTE: Since 5.0.1 and 4.9.4, this contract identifies non-canonical contexts (i.e. `msg.sender` is not {Context-_msgSender}).
>>>   17 |  * If a non-canonical context is identified, the following self `delegatecall` appends the last bytes of `msg.data`
      18 |  * to the subcall. This makes it safe to use with {ERC2771Context}. Contexts that don't affect the resolution of
      19 |  * {Context-_msgSender} are not propagated to subcalls.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\Multicall.sol:24`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      22 |     /**
      23 |      * @dev Receives and executes a batch of function calls on this contract.
>>>   24 |      * @custom:oz-upgrades-unsafe-allow-reachable delegatecall
      25 |      */
      26 |     function multicall(bytes[] calldata data) public virtual returns (bytes[] memory results) {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\Multicall.sol:33`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      31 |         results = new bytes[](data.length);
      32 |         for (uint256 i = 0; i < data.length; i++) {
>>>   33 |             results[i] = Address.functionDelegateCall(address(this), bytes.concat(data[i], context));
      34 |         }
      35 |         return results;
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `contracts\utils\SimulateCall.sol:26`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      24 |         bytes memory data
      25 |     ) internal returns (bool success, bytes memory retData) {
>>>   26 |         (success, retData) = getSimulator().delegatecall(abi.encodePacked(target, value, data));
      27 |         success = !success; // getSimulator() returns the success value inverted
      28 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `test\account\utils\draft-ERC7579Utils.t.sol:101`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      99 | 
     100 |             emit Log(false, executionCalldata.decodeBatch());
>>>  101 |         } else if (callType == ERC7579Utils.CALLTYPE_DELEGATECALL) {
     102 |             executionCalldata.execDelegateCall(execType);
     103 |         } else {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `test\account\utils\draft-ERC7579Utils.t.sol:102`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     100 |             emit Log(false, executionCalldata.decodeBatch());
     101 |         } else if (callType == ERC7579Utils.CALLTYPE_DELEGATECALL) {
>>>  102 |             executionCalldata.execDelegateCall(execType);
     103 |         } else {
     104 |             revert UnsupportedCallType(callType);
```
</details>

---

## Logic (55)

### [!] Timestamp Dependence

- **File:** `contracts\governance\extensions\GovernorTimelockAccess.sol:258`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     256 |     ) internal virtual override {
     257 |         uint48 etaSeconds = SafeCast.toUint48(proposalEta(proposalId));
>>>  258 |         if (block.timestamp < etaSeconds) {
     259 |             revert GovernorUnmetDelay(proposalId, etaSeconds);
     260 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `contracts\governance\extensions\GovernorTimelockCompound.sol:44`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      42 |         return
      43 |             (currentState == ProposalState.Queued &&
>>>   44 |                 block.timestamp >= proposalEta(proposalId) + _timelock.GRACE_PERIOD())
      45 |                 ? ProposalState.Expired
      46 |                 : currentState;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `contracts\governance\utils\Votes.sol:144`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     142 |         bytes32 s
     143 |     ) public virtual {
>>>  144 |         if (block.timestamp > expiry) {
     145 |             revert VotesExpiredSignature(expiry);
     146 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `contracts\mocks\token\ERC20VotesLegacyMock.sol:146`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     144 |         bytes32 s
     145 |     ) public virtual {
>>>  146 |         require(block.timestamp <= expiry, "ERC20Votes: signature expired");
     147 |         address signer = ECDSA.recover(
     148 |             _hashTypedDataV4(keccak256(abi.encode(_DELEGATION_TYPEHASH, delegatee, nonce, expiry))),
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\proxy\Clones.sol:48`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      46 |      */
      47 |     function clone(address implementation, uint256 value) internal returns (address instance) {
>>>   48 |         if (address(this).balance < value) {
      49 |             revert Errors.InsufficientBalance(address(this).balance, value);
      50 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\proxy\Clones.sol:95`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      93 |         uint256 value
      94 |     ) internal returns (address instance) {
>>>   95 |         if (address(this).balance < value) {
      96 |             revert Errors.InsufficientBalance(address(this).balance, value);
      97 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\proxy\Clones.sol:172`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     170 |         uint256 value
     171 |     ) internal returns (address instance) {
>>>  172 |         if (address(this).balance < value) {
     173 |             revert Errors.InsufficientBalance(address(this).balance, value);
     174 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\proxy\ERC1967\ERC1967Clones.sol:112`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     110 |      */
     111 |     function clone(address implementation, uint256 value) internal returns (address instance) {
>>>  112 |         require(address(this).balance >= value, Errors.InsufficientBalance(address(this).balance, value));
     113 |         bytes32 implementationSlot = ERC1967Utils.IMPLEMENTATION_SLOT;
     114 |         bytes32 topic1 = IERC1967.Upgraded.selector;
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\proxy\ERC1967\ERC1967Clones.sol:167`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     165 |         uint256 value
     166 |     ) internal returns (address instance) {
>>>  167 |         require(address(this).balance >= value, Errors.InsufficientBalance(address(this).balance, value));
     168 |         bytes32 implementationSlot = ERC1967Utils.IMPLEMENTATION_SLOT;
     169 |         bytes32 topic1 = IERC1967.Upgraded.selector;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `contracts\token\ERC20\extensions\ERC20Permit.sol:51`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      49 |         bytes32 s
      50 |     ) public virtual {
>>>   51 |         if (block.timestamp > deadline) {
      52 |             revert ERC2612ExpiredSignature(deadline);
      53 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\utils\Address.sol:35`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      33 |      */
      34 |     function sendValue(address payable recipient, uint256 amount) internal {
>>>   35 |         if (address(this).balance < amount) {
      36 |             revert Errors.InsufficientBalance(address(this).balance, amount);
      37 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\utils\Address.sol:80`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      78 |      */
      79 |     function functionCallWithValue(address target, bytes memory data, uint256 value) internal returns (bytes memory) {
>>>   80 |         if (address(this).balance < value) {
      81 |             revert Errors.InsufficientBalance(address(this).balance, value);
      82 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\utils\Create2.sol:39`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      37 |      */
      38 |     function deploy(uint256 amount, bytes32 salt, bytes memory bytecode) internal returns (address addr) {
>>>   39 |         if (address(this).balance < amount) {
      40 |             revert Errors.InsufficientBalance(address(this).balance, amount);
      41 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `contracts\utils\Create3.sol:87`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      85 |      */
      86 |     function deploy(uint256 amount, bytes32 salt, bytes memory bytecode) internal returns (address) {
>>>   87 |         if (address(this).balance < amount) {
      88 |             revert Errors.InsufficientBalance(address(this).balance, amount);
      89 |         }
```
</details>

---

### [!] Infinite Loop Risk

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\execall.ts:9`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Detected an infinite loop construct. Ensure there is a proper exit condition.

**Fix:** Verify the loop has a reachable break/return condition and a timeout.

<details>
<summary>Code</summary>

```
       7 |   re = new RegExp(re, re.flags + (re.sticky ? '' : 'y'));
       8 | 
>>>    9 |   while (true) {
      10 |     const match = re.exec(text);
      11 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `docs\templates\helpers.ts:16`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      14 | 
      15 | export const slug = str => {
>>>   16 |   if (str === undefined) {
      17 |     throw new Error('Missing argument');
      18 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\hook-handlers\config.ts:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
       9 |     const results: Array<{ path: string[]; message: string }> = [];
      10 | 
>>>   11 |     if (userConfig.exposed?.prefix !== undefined && typeof userConfig.exposed?.prefix !== 'string') {
      12 |       results.push({ path: ['exposed', 'prefix'], message: 'Expected an optional string.' });
      13 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\hook-handlers\config.ts:15`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      13 |     }
      14 |     if (
>>>   15 |       userConfig.exposed?.exclude !== undefined &&
      16 |       (!Array.isArray(userConfig.exposed.exclude) || userConfig.exposed.exclude.some(e => typeof e !== 'string'))
      17 |     ) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\hook-handlers\config.ts:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      19 |     }
      20 |     if (
>>>   21 |       userConfig.exposed?.include !== undefined &&
      22 |       (!Array.isArray(userConfig.exposed.include) || userConfig.exposed.include.some(e => typeof e !== 'string'))
      23 |     ) {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\hook-handlers\config.ts:26`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      24 |       results.push({ path: ['exposed', 'include'], message: 'Expected an optional string[].' });
      25 |     }
>>>   26 |     if (userConfig.exposed?.outDir !== undefined && typeof userConfig.exposed?.outDir !== 'string') {
      27 |       results.push({ path: ['exposed', 'outDir'], message: 'Expected an optional string.' });
      28 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\hook-handlers\config.ts:29`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      27 |       results.push({ path: ['exposed', 'outDir'], message: 'Expected an optional string.' });
      28 |     }
>>>   29 |     if (userConfig.exposed?.initializers !== undefined && typeof userConfig.exposed?.initializers !== 'boolean') {
      30 |       results.push({ path: ['exposed', 'initializers'], message: 'Expected an optional boolean.' });
      31 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      42 | 
      43 |     const exposedFile = getExposedFile(sourceName, inputSourceName, ast, deref, config, remappings);
>>>   44 |     if (exposedFile !== undefined) {
      45 |       res.set(exposedFile.absolutePath, exposedFile.content);
      46 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:114`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     112 |   );
     113 | 
>>>  114 |   return content === undefined ? undefined : { absolutePath: exposedFileAbsolutePath, content };
     115 | }
     116 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:323`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     321 |     fn.name +
     322 |     args
>>>  323 |       .filter(a => !onlyConflicting || a.type !== a.abiType || a.storageType !== undefined)
     324 |       .map(arg => arg.storageType ?? arg.type)
     325 |       .map(type => type.replace(/ .*/, '').replace(/[^0-9a-zA-Z$_]+/g, '_')) // sanitize
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:443`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     441 |   const isUnchained = m?.[1] === '_unchained';
     442 |   const wantsUnchained = kind === 'unchained';
>>>  443 |   return m !== null && (kind === 'any' || isUnchained === wantsUnchained);
     444 | }
     445 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:461`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     459 | 
     460 | function isTypeExternalizable(typeName: TypeName | null | undefined, deref: ASTDereferencer): boolean {
>>>  461 |   if (typeName == undefined) {
     462 |     return true;
     463 |   } else if (typeName.nodeType === 'UserDefinedTypeName') {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:472`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     470 |   } else if (typeName.nodeType === 'ArrayTypeName' && typeName.length != undefined) {
     471 |     const value = typeName.length.typeDescriptions.typeIdentifier?.match(/^t_rational_([^_]*)_by_1$/)?.[1];
>>>  472 |     return value !== undefined && parseInt(value) < 2 ** 27;
     473 |   } else {
     474 |     return typeName.nodeType !== 'Mapping' && typeName.nodeType !== 'FunctionTypeName';
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-exposed\internal\expose.ts:748`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     746 | function mustGet<K, V>(map: Map<K, V>, key: K): V {
     747 |   const value = map.get(key);
>>>  748 |   if (value === undefined) {
     749 |     throw new Error('Key not found');
     750 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\render.ts:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      49 | function buildRenderer(templates: Templates): (page: Page, options: TemplateOptions) => string {
      50 |   const pageTemplate = templates.partials?.page;
>>>   51 |   if (pageTemplate === undefined) {
      52 |     throw new Error(`Missing 'page' template`);
      53 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\site.ts:88`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      86 |         defineProperties(withContext, properties);
      87 | 
>>>   88 |         if (isNewFile && page !== undefined) {
      89 |           (pages[page] ??= []).push(withContext);
      90 |           items.push(withContext);
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\site.ts:99`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      97 |         for (const item of topLevelItem.nodes) {
      98 |           if (!isDocItem(item)) continue;
>>>   99 |           if (isNewFile && page !== undefined) items.push(item as DocItemWithContext);
     100 |           const contract = topLevelItem.nodeType === 'ContractDefinition' ? topLevelItem : undefined;
     101 |           const withContext = defineContext(item, build, file, page, contract);
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\common\properties.ts:97`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      95 |     ...p,
      96 |     type: p.typeDescriptions.typeString!,
>>>   97 |     natspec: natspec?.find((q, j) => (q.name === undefined ? i === j : p.name === q.name))?.description,
      98 |   }));
      99 | }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\natspec.ts:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      33 |   const docSource = readItemDocs(item);
      34 |   const docString =
>>>   35 |     docSource !== undefined
      36 |       ? cleanUpDocstringFromSource(docSource)
      37 |       : 'documentation' in item && item.documentation
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\natspec.ts:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      49 | 
      50 |   for (const [, tag = 'notice', content] of tagMatches) {
>>>   51 |     if (content === undefined) throw new ItemError('Unexpected error', item);
      52 | 
      53 |     if (tag === 'dev' || tag === 'notice') {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\natspec.ts:78`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      76 |       const i = res.returns.length;
      77 |       const p = item.returnParameters.parameters[i];
>>>   78 |       if (p === undefined) {
      79 |         throw new ItemError('Got more @return tags than expected', item);
      80 |       }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\read-item-docs.ts:10`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
       8 |     const { source, start, length } = decodeSrc(item.documentation.src, build);
       9 |     const content = build.input.sources[source]?.content;
>>>   10 |     if (content !== undefined) {
      11 |       return Buffer.from(content, 'utf8')
      12 |         .slice(start, start + length)
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\read-item-docs.ts:20`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      18 | function decodeSrc(src: string, build: Build): { source: string; start: number; length: number } {
      19 |   const [start, length, sourceId] = src.split(':').map(s => parseInt(s));
>>>   20 |   if (start === undefined || length === undefined || sourceId === undefined) {
      21 |     throw new Error(`Bad source string ${src}`);
      22 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\read-item-docs.ts:24`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      22 |   }
      23 |   const source = Object.keys(build.output.sources).find(s => build.output.sources[s]?.id === sourceId);
>>>   24 |   if (source === undefined) {
      25 |     throw new Error(`No source with id ${sourceId}`);
      26 |   }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `hardhat\hardhat-transpiler\tasks\transpile.ts:108`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     106 | 
     107 |       // If we have an initializablePath and no peer project, we need to preserve the initializablePath.
>>>  108 |       if (options.initializablePath && options.peerProject === undefined) {
     109 |         keep.add(path.join(hre.config.paths.root, options.initializablePath.replace(/^project\//, '')));
     110 |       }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `scripts\release\workflow\state.js:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      93 | async function readChangesetState(cwd = process.cwd()) {
      94 |   const preState = await readPreState(cwd);
>>>   95 |   const isInPreMode = preState !== undefined && preState.mode === 'pre';
      96 | 
      97 |   let changesets = await readChangesets(cwd);
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `scripts\solhint-custom\index.js:15`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      13 |     this.ignored = this.constructor.global || ignore.some(p => minimatch(path.normalize(fileName), p));
      14 |     this.ruleId = this.constructor.ruleId;
>>>   15 |     if (this.ruleId === undefined) {
      16 |       throw Error('missing ruleId static property');
      17 |     }
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\eip712.js:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      29 | 
      30 | export function domainType(domain) {
>>>   31 |   return EIP712Domain.filter(({ name }) => domain[name] !== undefined);
      32 | }
      33 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\erc4337.js:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      25 |     ['uint48', 'uint48', 'address'],
      26 |     [
>>>   27 |       range === undefined
      28 |         ? BigInt(validAfter)
      29 |         : (BigInt(validAfter) & BLOCK_RANGE_MASK) | (range == ValidationRange.Block ? BLOCK_RANGE_FLAG : 0n),
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\erc4337.js:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      28 |         ? BigInt(validAfter)
      29 |         : (BigInt(validAfter) & BLOCK_RANGE_MASK) | (range == ValidationRange.Block ? BLOCK_RANGE_FLAG : 0n),
>>>   30 |       range === undefined
      31 |         ? BigInt(validUntil)
      32 |         : range == ValidationRange.Block && (BigInt(validUntil) & BLOCK_RANGE_MASK) == 0n
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\erc4337.js:60`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      58 |       [getAddress(paymaster), paymasterVerificationGasLimit, paymasterPostOpGasLimit, paymasterData],
      59 |     ),
>>>   60 |     signature === undefined
      61 |       ? '0x'
      62 |       : ethers.solidityPacked(
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\governance.js:79`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      77 |       .then(
      78 |         () =>
>>>   79 |           delegation.value === undefined ||
      80 |           delegation.token.connect(this.governor.runner).transfer(delegation.to, delegation.value),
      81 |       )
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\governance.js:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      82 |       .then(
      83 |         () =>
>>>   84 |           delegation.tokenId === undefined ||
      85 |           delegation.token
      86 |             .ownerOf(delegation.tokenId)
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\helpers\iterate.js:15`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      13 | // Example: range(17,42,7) → [17,24,31,38]
      14 | export const range = (start, stop = undefined, step = 1) => {
>>>   15 |   if (stop == undefined) {
      16 |     stop = start;
      17 |     start = 0;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\metatx\ERC2771Forwarder.test.js:256`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     254 |           );
     255 | 
>>>  256 |         // All requests emit the event — the reverting one has success == false
     257 |         expect(events).to.have.lengthOf(this.requests.length);
     258 |         expect(events[idx].args.success).to.be.false;
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\metatx\ERC2771Forwarder.test.js:284`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     282 |           const receipt = this.forwarder.executeBatch(this.requests, ethers.ZeroAddress, { value: this.value });
     283 | 
>>>  284 |           // The reverting request emits success == false; the others still execute normally
     285 |           await expect(receipt)
     286 |             .to.emit(this.forwarder, 'ExecutedForwardRequest')
```
</details>

---

### [~] Side-Effect in Condition

- **File:** `test\metatx\ERC2771Forwarder.test.js:358`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Pre/post increment used in a standalone statement may indicate logic confusion.

**Fix:** Ensure increment is intentional and not a mistyped comparison (== vs =).

<details>
<summary>Code</summary>

```
     356 |           // Execute first a request
     357 |           await this.forwarder.execute(this.requests[idx], { value: this.requests[idx].value });
>>>  358 |           this.initialTamperedRequestNonce++; // Should be already incremented by the individual `execute`
     359 | 
     360 |           // And then ignore the same request in a batch due to an already used nonce
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\utils\BlockHeader.test.js:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      33 | );
      34 | 
>>>   35 | const sanitize = hex => (hex === undefined ? undefined : hex === '0x0' ? '0x' : ethers.toBeHex(hex));
      36 | const rlpEncodeBlock = block =>
      37 |   ethers.encodeRlp(
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\utils\BlockHeader.test.js:60`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
      58 |       block.parentBeaconBlockRoot,
      59 |       block.requestsHash,
>>>   60 |     ].filter(x => x !== undefined),
      61 |   ); // filter out fields not present in older blocks
      62 | 
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\utils\cryptography\TrieProof.test.js:698`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     696 |     ]) {
     697 |       it(title, async function () {
>>>  698 |         if (error === undefined) {
     699 |           await expect(this.mock.$traverse(root, key, proof)).to.eventually.equal(value);
     700 |         } else {
```
</details>

---

### [~] Comparison with Boolean Literal

- **File:** `test\utils\introspection\SupportsInterface.behavior.js:155`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Direct comparison with true/false is usually redundant and may hide type coercion bugs.

**Fix:** Use the value directly as a boolean: 'if (value)' instead of 'if (value === true)'.

<details>
<summary>Code</summary>

```
     153 |       for (const k of interfaces) {
     154 |         // skip interfaces for which we don't have a function list
>>>  155 |         if (signatures[k] === undefined) continue;
     156 | 
     157 |         // Check the presence of each function in the contract's interface
```
</details>

---

## Resource Management (3)

### [!] Fixed-Gas Transfer

- **File:** `contracts\governance\utils\VotesExtended.sol:23`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      21 |  * contract VotingToken is Token, VotesExtended {
      22 |  *   function transfer(address from, address to, uint256 tokenId) public override {
>>>   23 |  *     super.transfer(from, to, tokenId); // <- Perform the transfer first ...
      24 |  *     _transferVotingUnits(from, to, 1); // <- ... then call _transferVotingUnits.
      25 |  *   }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\mocks\token\ERC20NoReturnMock.sol:10`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
       8 |     function transfer(address to, uint256 amount) public override returns (bool) {
       9 |         // forge-lint: disable-next-line(erc20-unchecked-transfer)
>>>   10 |         super.transfer(to, amount);
      11 |         assembly {
      12 |             return(0, 0)
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `contracts\token\ERC20\utils\SafeERC20.sol:180`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     178 | 
     179 |     /**
>>>  180 |      * @dev Imitates a Solidity `token.transfer(to, value)` call, relaxing the requirement on the return value: the
     181 |      * return value is optional (but if data is returned, it must not be false).
     182 |      *
```
</details>

---

## Performance (20)

### [~] Unoptimized Loop

- **File:** `contracts\mocks\ERC165Mock.sol:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      52 | contract ERC165InterfacesSupported is SupportsInterfaceWithLookupMock {
      53 |     constructor(bytes4[] memory interfaceIds) {
>>>   54 |         for (uint256 i = 0; i < interfaceIds.length; i++) {
      55 |             _registerInterface(interfaceIds[i]);
      56 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\mocks\ERC165Mock.sol:63`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      61 | contract ERC165RevertInvalid is SupportsInterfaceWithLookupMock {
      62 |     constructor(bytes4[] memory interfaceIds) {
>>>   63 |         for (uint256 i = 0; i < interfaceIds.length; i++) {
      64 |             _registerInterface(interfaceIds[i]);
      65 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\mocks\MulticallHelper.sol:14`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      12 |     ) external {
      13 |         bytes[] memory calls = new bytes[](recipients.length);
>>>   14 |         for (uint256 i = 0; i < recipients.length; i++) {
      15 |             calls[i] = abi.encodeCall(multicallToken.transfer, (recipients[i], amounts[i]));
      16 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\mocks\MulticallHelper.sol:19`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      17 | 
      18 |         bytes[] memory results = multicallToken.multicall(calls);
>>>   19 |         for (uint256 i = 0; i < results.length; i++) {
      20 |             require(abi.decode(results[i], (bool)));
      21 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\Multicall.sol:32`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      30 | 
      31 |         results = new bytes[](data.length);
>>>   32 |         for (uint256 i = 0; i < data.length; i++) {
      33 |             results[i] = Address.functionDelegateCall(address(this), bytes.concat(data[i], context));
      34 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      57 |     function processProof(bytes32[] memory proof, bytes32 leaf) internal pure returns (bytes32) {
      58 |         bytes32 computedHash = leaf;
>>>   59 |         for (uint256 i = 0; i < proof.length; i++) {
      60 |             computedHash = Hashes.commutativeKeccak256(computedHash, proof[i]);
      61 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      94 |     ) internal view returns (bytes32) {
      95 |         bytes32 computedHash = leaf;
>>>   96 |         for (uint256 i = 0; i < proof.length; i++) {
      97 |             computedHash = hasher(computedHash, proof[i]);
      98 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:124`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     122 |     function processProofCalldata(bytes32[] calldata proof, bytes32 leaf) internal pure returns (bytes32) {
     123 |         bytes32 computedHash = leaf;
>>>  124 |         for (uint256 i = 0; i < proof.length; i++) {
     125 |             computedHash = Hashes.commutativeKeccak256(computedHash, proof[i]);
     126 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:161`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     159 |     ) internal view returns (bytes32) {
     160 |         bytes32 computedHash = leaf;
>>>  161 |         for (uint256 i = 0; i < proof.length; i++) {
     162 |             computedHash = hasher(computedHash, proof[i]);
     163 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:232`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     230 |             // - depending on the flag, either another value from the "main queue" (merging branches) or an element from the
     231 |             //   `proof` array.
>>>  232 |             for (uint256 i = 0; i < proofFlagsLen; i++) {
     233 |                 bytes32 a = leafPos < leavesLen ? leaves[leafPos++] : hashes[hashPos++];
     234 |                 bytes32 b = proofFlags[i]
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:319`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     317 |             // - depending on the flag, either another value from the "main queue" (merging branches) or an element from the
     318 |             //   `proof` array.
>>>  319 |             for (uint256 i = 0; i < proofFlagsLen; i++) {
     320 |                 bytes32 a = leafPos < leavesLen ? leaves[leafPos++] : hashes[hashPos++];
     321 |                 bytes32 b = proofFlags[i]
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:404`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     402 |             // - depending on the flag, either another value from the "main queue" (merging branches) or an element from the
     403 |             //   `proof` array.
>>>  404 |             for (uint256 i = 0; i < proofFlagsLen; i++) {
     405 |                 bytes32 a = leafPos < leavesLen ? leaves[leafPos++] : hashes[hashPos++];
     406 |                 bytes32 b = proofFlags[i]
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\cryptography\MerkleProof.sol:491`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     489 |             // - depending on the flag, either another value from the "main queue" (merging branches) or an element from the
     490 |             //   `proof` array.
>>>  491 |             for (uint256 i = 0; i < proofFlagsLen; i++) {
     492 |                 bytes32 a = leafPos < leavesLen ? leaves[leafPos++] : hashes[hashPos++];
     493 |                 bytes32 b = proofFlags[i]
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\introspection\ERC165Checker.sol:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      60 |         if (supportsERC165(account)) {
      61 |             // query support of each interface in interfaceIds
>>>   62 |             for (uint256 i = 0; i < interfaceIds.length; i++) {
      63 |                 interfaceIdsSupported[i] = supportsERC165InterfaceUnchecked(account, interfaceIds[i]);
      64 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\introspection\ERC165Checker.sol:86`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      84 | 
      85 |         // query support of each interface in interfaceIds
>>>   86 |         for (uint256 i = 0; i < interfaceIds.length; i++) {
      87 |             if (!supportsERC165InterfaceUnchecked(account, interfaceIds[i])) {
      88 |                 return false;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\structs\MerkleTree.sol:153`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     151 |         uint256 currentIndex = index;
     152 |         bytes32 currentLevelHash = leaf;
>>>  153 |         for (uint256 i = 0; i < treeDepth; i++) {
     154 |             // Reaching the parent node, is currentLevelHash the left child?
     155 |             bool isLeft = currentIndex % 2 == 0;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\utils\structs\MerkleTree.sol:235`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     233 |             bytes32 currentLevelHashOld = oldValue;
     234 |             bytes32 currentLevelHashNew = newValue;
>>>  235 |             for (uint32 i = 0; i < treeDepth; i++) {
     236 |                 bool isLeft = currentIndex % 2 == 0;
     237 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\account\utils\draft-ERC7579Utils.t.sol:473`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     471 |     function _collectAndPrintLogs(bool includeTotalValue) internal view {
     472 |         Vm.Log[] memory logs = vm.getRecordedLogs();
>>>  473 |         for (uint256 i = 0; i < logs.length; i++) {
     474 |             if (logs[i].emitter == _account) {
     475 |                 _printDecodedCalls(logs[i].data, includeTotalValue);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\token\ERC721\extensions\ERC721Consecutive.t.sol:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      21 |     constructor(address[] memory receivers, uint256[] memory batches, uint256 startingId) ERC721("", "") {
      22 |         _offset = uint96(startingId);
>>>   23 |         for (uint256 i = 0; i < batches.length; i++) {
      24 |             address receiver = receivers[i % receivers.length];
      25 |             uint96 batchSize = uint96(bound(batches[i], 0, _maxBatchSize()));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\utils\Arrays.t.sol:18`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      16 |     function symbolicSort() public pure {
      17 |         uint256[] memory values = new uint256[](3);
>>>   18 |         for (uint256 i = 0; i < 3; i++) {
      19 |             values[i] = svm.createUint256("arrayElement");
      20 |         }
```
</details>

---

## Code Quality (42)

### [~] Address Is Contract Check

- **File:** `contracts\access\manager\AccessManaged.sol:71`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      69 |             revert AccessManagedUnauthorized(caller);
      70 |         }
>>>   71 |         if (newAuthority.code.length == 0) {
      72 |             revert AccessManagedInvalidAuthority(newAuthority);
      73 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\DummyImplementation.sol:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      42 | 
      43 |     function reverts() public pure {
>>>   44 |         require(false, "DummyImplementation reverted");
      45 |     }
      46 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\ERC165Mock.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      45 |      */
      46 |     function _registerInterface(bytes4 interfaceId) internal {
>>>   47 |         require(interfaceId != 0xffffffff, "ERC165InterfacesSupported: invalid interface id");
      48 |         _supportedInterfaces[interfaceId] = true;
      49 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\InitializableMock.sol:45`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      43 | 
      44 |     function fail() public pure {
>>>   45 |         require(false, "InitializableMock forced failure");
      46 |     }
      47 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\ReentrancyAttack.sol:10`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
       8 |     function callSender(bytes calldata data) public {
       9 |         (bool success, ) = _msgSender().call(data);
>>>   10 |         require(success, "ReentrancyAttack: failed call");
      11 |     }
      12 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\ReentrancyAttack.sol:15`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      13 |     function staticcallSender(bytes calldata data) public view {
      14 |         (bool success, ) = _msgSender().staticcall(data);
>>>   15 |         require(success, "ReentrancyAttack: failed call");
      16 |     }
      17 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\ReentrancyMock.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      32 |             _count();
      33 |             (bool success, ) = address(this).call(abi.encodeCall(this.countThisRecursive, (n - 1)));
>>>   34 |             require(success, "ReentrancyMock: failed call");
      35 |         }
      36 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\ReentrancyTransientMock.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      32 |             _count();
      33 |             (bool success, ) = address(this).call(abi.encodeCall(this.countThisRecursive, (n - 1)));
>>>   34 |             require(success, "ReentrancyTransientMock: failed call");
      35 |         }
      36 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\account\modules\ERC7579Mock.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      65 |         bytes calldata msgData
      66 |     ) external returns (bytes memory hookData) {
>>>   67 |         require(!_shouldRevertOnPreCheck, "preCheck reverts");
      68 |         emit PreCheck(msgSender, value, msgData);
      69 |         return msgData;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\account\modules\ERC7579Mock.sol:73`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      71 | 
      72 |     function postCheck(bytes calldata hookData) external {
>>>   73 |         require(!_shouldRevertOnPostCheck, "postCheck reverts");
      74 |         emit PostCheck(hookData);
      75 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      67 | 
      68 |     constructor(address admin_, uint256 delay_) {
>>>   69 |         require(delay_ >= MINIMUM_DELAY, "Timelock::constructor: Delay must exceed minimum delay.");
      70 |         require(delay_ <= MAXIMUM_DELAY, "Timelock::setDelay: Delay must not exceed maximum delay.");
      71 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:70`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      68 |     constructor(address admin_, uint256 delay_) {
      69 |         require(delay_ >= MINIMUM_DELAY, "Timelock::constructor: Delay must exceed minimum delay.");
>>>   70 |         require(delay_ <= MAXIMUM_DELAY, "Timelock::setDelay: Delay must not exceed maximum delay.");
      71 | 
      72 |         admin = admin_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:80`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      78 |     function setDelay(uint256 delay_) public {
      79 |         require(msg.sender == address(this), "Timelock::setDelay: Call must come from Timelock.");
>>>   80 |         require(delay_ >= MINIMUM_DELAY, "Timelock::setDelay: Delay must exceed minimum delay.");
      81 |         require(delay_ <= MAXIMUM_DELAY, "Timelock::setDelay: Delay must not exceed maximum delay.");
      82 |         delay = delay_;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      79 |         require(msg.sender == address(this), "Timelock::setDelay: Call must come from Timelock.");
      80 |         require(delay_ >= MINIMUM_DELAY, "Timelock::setDelay: Delay must exceed minimum delay.");
>>>   81 |         require(delay_ <= MAXIMUM_DELAY, "Timelock::setDelay: Delay must not exceed maximum delay.");
      82 |         delay = delay_;
      83 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:88`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      86 | 
      87 |     function acceptAdmin() public {
>>>   88 |         require(msg.sender == pendingAdmin, "Timelock::acceptAdmin: Call must come from pendingAdmin.");
      89 |         admin = msg.sender;
      90 |         pendingAdmin = address(0);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 |         uint256 eta
     108 |     ) public returns (bytes32) {
>>>  109 |         require(msg.sender == admin, "Timelock::queueTransaction: Call must come from admin.");
     110 |         require(
     111 |             eta >= getBlockTimestamp() + delay,
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:129`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     127 |         uint256 eta
     128 |     ) public {
>>>  129 |         require(msg.sender == admin, "Timelock::cancelTransaction: Call must come from admin.");
     130 | 
     131 |         bytes32 txHash = keccak256(abi.encode(target, value, signature, data, eta));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:144`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     142 |         uint256 eta
     143 |     ) public payable returns (bytes memory) {
>>>  144 |         require(msg.sender == admin, "Timelock::executeTransaction: Call must come from admin.");
     145 | 
     146 |         bytes32 txHash = keccak256(abi.encode(target, value, signature, data, eta));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\compound\CompTimelock.sol:163`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     161 |         // solium-disable-next-line security/no-call-value
     162 |         (bool success, bytes memory returnData) = target.call{value: value}(callData);
>>>  163 |         require(success, "Timelock::executeTransaction: Transaction execution reverted.");
     164 | 
     165 |         emit ExecuteTransaction(txHash, target, value, signature, data, eta);
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\mocks\docs\account\MyFactoryAccount.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      29 |     function cloneAndInitialize(bytes calldata callData) public returns (address) {
      30 |         address predicted = predictAddress(callData);
>>>   31 |         if (predicted.code.length == 0) {
      32 |             _impl.cloneDeterministic(keccak256(callData));
      33 |             predicted.functionCall(callData);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\token\ERC20VotesLegacyMock.sol:66`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      64 |      */
      65 |     function getPastVotes(address account, uint256 blockNumber) public view virtual returns (uint256) {
>>>   66 |         require(blockNumber < block.number, "ERC20Votes: block not yet mined");
      67 |         return _checkpointsLookup(_checkpoints[account], blockNumber);
      68 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\token\ERC20VotesLegacyMock.sol:79`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      77 |      */
      78 |     function getPastTotalSupply(uint256 blockNumber) public view virtual returns (uint256) {
>>>   79 |         require(blockNumber < block.number, "ERC20Votes: block not yet mined");
      80 |         return _checkpointsLookup(_totalSupplyCheckpoints, blockNumber);
      81 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\mocks\token\ERC20VotesLegacyMock.sol:146`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     144 |         bytes32 s
     145 |     ) public virtual {
>>>  146 |         require(block.timestamp <= expiry, "ERC20Votes: signature expired");
     147 |         address signer = ECDSA.recover(
     148 |             _hashTypedDataV4(keccak256(abi.encode(_DELEGATION_TYPEHASH, delegatee, nonce, expiry))),
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\proxy\beacon\UpgradeableBeacon.sol:64`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      62 |      */
      63 |     function _setImplementation(address newImplementation) private {
>>>   64 |         if (newImplementation.code.length == 0) {
      65 |             revert BeaconInvalidImplementation(newImplementation);
      66 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\proxy\ERC1967\ERC1967Utils.sol:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      52 |      */
      53 |     function _setImplementation(address newImplementation) private {
>>>   54 |         if (newImplementation.code.length == 0) {
      55 |             revert ERC1967InvalidImplementation(newImplementation);
      56 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\proxy\ERC1967\ERC1967Utils.sol:134`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     132 |      */
     133 |     function _setBeacon(address newBeacon) private {
>>>  134 |         if (newBeacon.code.length == 0) {
     135 |             revert ERC1967InvalidBeacon(newBeacon);
     136 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\proxy\ERC1967\ERC1967Utils.sol:141`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     139 | 
     140 |         address beaconImplementation = IBeacon(newBeacon).implementation();
>>>  141 |         if (beaconImplementation.code.length == 0) {
     142 |             revert ERC1967InvalidImplementation(beaconImplementation);
     143 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\proxy\utils\Initializable.sol:118`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     116 |         //                 current contract is just being deployed
     117 |         bool initialSetup = initialized == 0 && isTopLevelCall;
>>>  118 |         bool construction = initialized == 1 && address(this).code.length == 0;
     119 | 
     120 |         if (!initialSetup && !construction) {
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\token\ERC20\utils\ERC1363Utils.sol:43`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      41 |         bytes memory data
      42 |     ) internal {
>>>   43 |         if (to.code.length == 0) {
      44 |             revert ERC1363InvalidReceiver(to);
      45 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\token\ERC20\utils\ERC1363Utils.sol:77`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      75 |         bytes memory data
      76 |     ) internal {
>>>   77 |         if (spender.code.length == 0) {
      78 |             revert ERC1363InvalidSpender(spender);
      79 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\token\ERC20\utils\SafeERC20.sol:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     119 |      */
     120 |     function transferAndCallRelaxed(IERC1363 token, address to, uint256 value, bytes memory data) internal {
>>>  121 |         if (to.code.length == 0) {
     122 |             safeTransfer(token, to, value);
     123 |         } else if (!token.transferAndCall(to, value, data)) {
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\token\ERC20\utils\SafeERC20.sol:142`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     140 |         bytes memory data
     141 |     ) internal {
>>>  142 |         if (to.code.length == 0) {
     143 |             safeTransferFrom(token, from, to, value);
     144 |         } else if (!token.transferFromAndCall(from, to, value, data)) {
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\token\ERC20\utils\SafeERC20.sol:161`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     159 |      */
     160 |     function approveAndCallRelaxed(IERC1363 token, address to, uint256 value, bytes memory data) internal {
>>>  161 |         if (to.code.length == 0) {
     162 |             forceApprove(token, to, value);
     163 |         } else if (!token.approveAndCall(to, value, data)) {
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\token\ERC721\extensions\ERC721Consecutive.sol:145`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     143 | 
     144 |         // only mint after construction
>>>  145 |         if (previousOwner == address(0) && address(this).code.length == 0) {
     146 |             revert ERC721ForbiddenMint();
     147 |         }
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\utils\cryptography\P256.sol:97`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      95 |             return (true, true); // precompile is present, signature is valid
      96 |         } else if (
>>>   97 |             // Given precompiles have no bytecode (i.e. `address(0x100).code.length == 0`), we use
      98 |             // a valid signature with small `r` and `s` values to check if the precompile is present. Taken from
      99 |             // https://github.com/C2SP/wycheproof/blob/4672ff74d68766e7785c2cac4c597effccef2c5c/testvectors/ecdsa_secp256r1_sha256_p1363_test.json#L1173-L1204
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\utils\cryptography\SignatureChecker.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      31 |      */
      32 |     function isValidSignatureNow(address signer, bytes32 hash, bytes memory signature) internal view returns (bool) {
>>>   33 |         if (signer.code.length == 0) {
      34 |             (address recovered, ECDSA.RecoverError err, ) = ECDSA.tryRecover(hash, signature);
      35 |             return err == ECDSA.RecoverError.NoError && recovered == signer;
```
</details>

---

### [~] Address Is Contract Check

- **File:** `contracts\utils\cryptography\SignatureChecker.sol:49`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      47 |         bytes calldata signature
      48 |     ) internal view returns (bool) {
>>>   49 |         if (signer.code.length == 0) {
      50 |             (address recovered, ECDSA.RecoverError err, ) = ECDSA.tryRecoverCalldata(hash, signature);
      51 |             return err == ECDSA.RecoverError.NoError && recovered == signer;
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `hardhat\hardhat-solidity-docgen\hook-handlers\config.ts:14`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      12 |       config.docgen.root = config.paths.root;
      13 |       config.docgen.sourcesDir = path
>>>   14 |         .relative(config.paths.root, config.paths.sources.solidity[0]) // TODO: support multiple source directories
      15 |         .split(path.sep)
      16 |         .join(path.posix.sep);
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\memoized-getter.ts:6`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
       4 |   getter: () => T,
       5 | ) {
>>>    6 |   let state: 'todo' | 'doing' | 'done' = 'todo';
       7 |   let value: T;
       8 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `hardhat\hardhat-solidity-docgen\internal\utils\memoized-getter.ts:19`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      17 |           throw new Error('Detected recursion');
      18 | 
>>>   19 |         case 'todo':
      20 |           state = 'doing';
      21 |           value = getter();
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `scripts\release\workflow\state.js:86`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      84 |   state.isPublishedOnNpm = await isPublishedOnNpm(packageName, version);
      85 | 
>>>   86 |   // Log every state value in debug mode
      87 |   if (core.isDebug()) for (const [key, value] of Object.entries(state)) core.debug(`${key}: ${value}`);
      88 | 
```
</details>

---

### [I] Unresolved TODO/FIXME

- **File:** `scripts\release\workflow\state.js:87`
- **Severity:** INFO
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Developer left a note indicating unfinished or problematic code.

**Fix:** Review and resolve the TODO/FIXME before deploying.

<details>
<summary>Code</summary>

```
      85 | 
      86 |   // Log every state value in debug mode
>>>   87 |   if (core.isDebug()) for (const [key, value] of Object.entries(state)) core.debug(`${key}: ${value}`);
      88 | 
      89 |   return state;
```
</details>

---


---
*Generated by BugHunter*