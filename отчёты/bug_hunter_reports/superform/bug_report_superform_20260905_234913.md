# BugHunter Report: superform

**Generated:** 2026-09-05 23:49:13
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\superform`
**Analyzers:** static, ast, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 454 |
| Total lines | 110,551 |
| Bugs found | 179 |
| !!! Critical | 4 |
| !! High | 9 |
| ! Medium | 39 |
| ~ Low | 127 |

### Languages Detected

- **solidity**: 386 files
- **bash**: 56 files
- **go**: 10 files
- **javascript**: 2 files

## Security (13)

### [!!!] tx.origin For Authorization

- **File:** `script\forge-scripts\safe\BatchScript.sol:31`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
      29 |     //     "baseGas": 0,  // Gast costs not related to the transaction execution (signature check, refund payment...)
      30 |     //     "gasPrice": 0,  // Gas price used for the refund calculation
>>>   31 |     //     "refundReceiver": "<checksummed address>", //Address of receiver of gas payment (or `null` if tx.origin)
      32 | 
      33 |     //     "nonce": 0,  // Nonce of the Safe, transaction cannot be executed until Safe's nonce is not equal to this
```
</details>

---

### [!!!] tx.origin For Authorization

- **File:** `test\invariant\rewards-distributor\handlers\RewardsDistributorHandler.sol:132`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
     130 |     function randomUserIndex(uint256 seed, uint256 index, uint256 periodId) internal view returns (uint256) {
     131 |         return uint256(
>>>  132 |             keccak256(abi.encodePacked(index, seed, tx.origin, blockhash(block.number - 1), block.timestamp))
     133 |         ) % totalTestUsers[periodId];
     134 |     }
```
</details>

---

### [!!!] tx.origin For Authorization

- **File:** `test\invariant\rewards-distributor\handlers\RewardsDistributorHandler.sol:138`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
     136 |     function randomPeriod(uint256 seed, uint256 index) internal view returns (uint256) {
     137 |         return uint256(
>>>  138 |             keccak256(abi.encodePacked(index, seed, tx.origin, blockhash(block.number - 1), block.timestamp))
     139 |         ) % 3;
     140 |     }
```
</details>

---

### [!!!] tx.origin For Authorization

- **File:** `test\utils\BaseSetup.sol:2475`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
    2473 |     function _randomBytes32() internal view returns (bytes32) {
    2474 |         return keccak256(
>>> 2475 |             abi.encode(tx.origin, block.number, block.timestamp, block.coinbase, address(this).codehash, gasleft())
    2476 |         );
    2477 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\BatchScript.sol:80`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      78 |     enum Operation {
      79 |         CALL,
>>>   80 |         DELEGATECALL
      81 |     }
      82 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\BatchScript.sol:104`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     102 |     // Adds an encoded transaction to the batch.
     103 |     // Encodes the transaction as packed bytes of:
>>>  104 |     // - `operation` as a `uint8` with `0` for a `call` or `1` for a `delegatecall` (=> 1 byte),
     105 |     // - `to` as an `address` (=> 20 bytes),
     106 |     // - `value` as in msg.value, sent as a `uint256` (=> 32 bytes),
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\BatchScript.sol:217`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     215 |         batch.to = SAFE_MULTISEND_ADDRESS;
     216 |         batch.value = 0;
>>>  217 |         batch.operation = Operation.DELEGATECALL;
     218 | 
     219 |         // Encode the batch calldata. The list of transactions is tightly packed.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\lib\DelegatePrank.sol:17`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      15 |     dest.fn(args);
      16 | 
>>>   17 |   Now, to make c delegatecall dest.fn(args):
      18 | 
      19 |     delegatePrank(c,address(dest),abi.encodeCall(fn,(args)));
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\lib\DelegatePrank.sol:31`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      29 |     bytes memory code = from.code;
      30 |     vm.etch(from,address(delegator).code);
>>>   31 |     (success, ret) = from.call(abi.encodeCall(delegator.etchCodeAndDelegateCall,(to,cd,code)));
      32 |   }
      33 | }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\lib\DelegatePrank.sol:36`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      34 | 
      35 | contract Delegator is CommonBase {
>>>   36 |   function etchCodeAndDelegateCall(address dest, bytes memory cd, bytes calldata code) external payable virtual {
      37 |     vm.etch(address(this),code);
      38 |     assembly ("memory-safe") {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `script\forge-scripts\safe\lib\DelegatePrank.sol:39`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      37 |     vm.etch(address(this),code);
      38 |     assembly ("memory-safe") {
>>>   39 |       let result := delegatecall(gas(), dest, add(cd,32), mload(cd), 0, 0)
      40 |       returndatacopy(0, 0, returndatasize())
      41 |       switch result
```
</details>

---

### [!!] Reentrancy Vector (External Call with Value)

- **File:** `test\unit\crosschain-liquidity\DstSwapper.t.sol:40`
- **Severity:** HIGH
- **Confidence:** 55%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} detected. If state is updated after this call, an attacker can re-enter.

**Fix:** Follow checks-effects-interactions: update state before external calls, or use a reentrancy guard.

<details>
<summary>Code</summary>

```
      38 |         vm.startPrank(deployer);
      39 | 
>>>   40 |         (bool success,) = payable(dstSwapper).call{ value: 1e18 }("");
      41 | 
      42 |         if (success) {
```
</details>

---

### [!] Unchecked Low-Level Call Result

- **File:** `test\mocks\7540MockUtils\SafeTransferLib.sol:17`
- **Severity:** MEDIUM
- **Confidence:** 60%
- **Analyzer:** solidity_semantic

**Problem:** Low-level .call/.delegatecall return value is not captured; failures are silently ignored.

**Fix:** Capture the return value: (bool success, ...) = target.call(...); then verify success.

<details>
<summary>Code</summary>

```
      15 |     function safeTransferFrom(address token, address from, address to, uint256 value) internal {
      16 |         (bool success, bytes memory data) =
>>>   17 |             token.call(abi.encodeWithSelector(IERC20.transferFrom.selector, from, to, value));
      18 |         require(success && (data.length == 0 || abi.decode(data, (bool))), "SafeTransferLib/safe-transfer-from-failed");
      19 |     }
```
</details>

---

## Logic (17)

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\superform-forms\superform-form.ERC7540Form.t.sol:1049`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultAsset' is modified at line 1049, after an external call at line 1047. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
    1047 |         ERC7575Mock(IERC7540(vault).share()).mint(superform, depositAmount);
    1048 | 
>>> 1049 |         address vaultAsset = IBaseForm(superform).getVaultAsset();
    1050 |         vm.prank(0x423420Ae467df6e90291fd0252c0A8a637C1e03f);
    1051 |         MockERC20(vaultAsset).mint(vault, depositAmount * 2);
```
</details>

---

### [!] Balance Comparison

- **File:** `src\BaseRouterImplementation.sol:994`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     992 |     /// @dev forwards the residual payment to Paymaster
     993 |     function _forwardPayment(uint256 _balanceBefore) internal virtual {
>>>  994 |         if (address(this).balance < _balanceBefore) revert Error.INSUFFICIENT_BALANCE();
     995 | 
     996 |         /// @dev deducts what's already available sends what's left in msg.value to Paymaster
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\RewardsDistributor.sol:194`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     192 | 
     193 |         uint256 deadlineTimestamp = periodicRewardsMerkleRootData[periodId_].startTimestamp + DEADLINE;
>>>  194 |         if (block.timestamp > deadlineTimestamp) revert CLAIM_DEADLINE_PASSED();
     195 | 
     196 |         /// @dev a given receiver cannot claim rewards a second time for a given period
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\crosschain-data\extensions\CoreStateRegistry.sol:284`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     282 |         if (
     283 |             failedDeposits_.lastProposedTimestamp == 0
>>>  284 |                 || block.timestamp > failedDeposits_.lastProposedTimestamp + _getDelay()
     285 |         ) {
     286 |             revert Error.DISPUTE_TIME_ELAPSED();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `src\crosschain-data\extensions\CoreStateRegistry.sol:307`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     305 |         if (
     306 |             failedDeposits_.lastProposedTimestamp == 0
>>>  307 |                 || block.timestamp <= failedDeposits_.lastProposedTimestamp + _getDelay()
     308 |         ) {
     309 |             revert Error.RESCUE_LOCKED();
```
</details>

---

### [!] Balance Comparison

- **File:** `src\crosschain-liquidity\DstSwapper.sol:116`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     114 |         } else {
     115 |             if (interimToken == NATIVE) {
>>>  116 |                 if (address(this).balance < amount) {
     117 |                     revert Error.INVALID_DST_SWAPPER_FAILED_SWAP_NO_NATIVE_BALANCE();
     118 |                 }
```
</details>

---

### [!] Balance Comparison

- **File:** `src\crosschain-liquidity\DstSwapper.sol:331`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     329 |         }
     330 |         if (userSuppliedInterimToken_ == NATIVE) {
>>>  331 |             if (address(this).balance < v.amount) {
     332 |                 revert Error.INSUFFICIENT_BALANCE();
     333 |             }
```
</details>

---

### [!] Balance Comparison

- **File:** `src\crosschain-liquidity\DstSwapper.sol:427`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     425 |             }
     426 |         } else {
>>>  427 |             if (address(this).balance < amount_) {
     428 |                 revert Error.INSUFFICIENT_BALANCE();
     429 |             }
```
</details>

---

### [!] Balance Comparison

- **File:** `src\payments\PayMaster.sol:100`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
      98 |     /// @inheritdoc IPayMaster
      99 |     function treatAMB(uint8 ambId_, uint256 nativeValue_, bytes memory data_) external override onlyPaymentAdmin {
>>>  100 |         if (address(this).balance < nativeValue_) {
     101 |             revert Error.FAILED_TO_SEND_NATIVE();
     102 |         }
```
</details>

---

### [!] Balance Comparison

- **File:** `src\payments\PayMaster.sol:141`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     139 |     /// @dev helper to move native tokens same chain
     140 |     function _withdrawNative(address receiver_, uint256 amount_) internal {
>>>  141 |         if (address(this).balance < amount_) {
     142 |             revert Error.FAILED_TO_SEND_NATIVE();
     143 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `test\mocks\BaseERC7540Mock.sol:94`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      92 |         returns (bool)
      93 |     {
>>>   94 |         require(block.timestamp <= deadline, "ERC7540Vault/authorization-expired");
      95 |         require(controller != address(0), "ERC7540Vault/invalid-controller");
      96 |         require(!authorizations[controller][nonce], "ERC7540Vault/authorization-used");
```
</details>

---

### [!] Timestamp Dependence

- **File:** `test\mocks\7540MockUtils\ERC20.sol:145`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     143 |     // --- Approve by signature ---
     144 |     function permit(address owner, address spender, uint256 value, uint256 deadline, bytes memory signature) public {
>>>  145 |         require(block.timestamp <= deadline, "ERC20/permit-expired");
     146 |         require(owner != address(0), "ERC20/invalid-owner");
     147 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\crosschain-data\extensions\CoreStateRegistry.t.sol:45`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'nativeAmount' is modified at line 45, after an external call at line 40. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      43 |         PaymentHelper(getContract(AVAX, "PaymentHelper")).estimateAckCost(100);
      44 | 
>>>   45 |         uint256 nativeAmount = PaymentHelper(getContract(AVAX, "PaymentHelper")).estimateAckCost(1);
      46 | 
      47 |         vm.prank(deployer);
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:707`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'data' is modified at line 707, after an external call at line 701. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     705 |         vm.startPrank(getContract(ETH, "CoreStateRegistry"));
     706 | 
>>>  707 |         InitSingleVaultData memory data = InitSingleVaultData(
     708 |             1,
     709 |             superformId,
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:739`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'data' is modified at line 739, after an external call at line 734. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     737 |         vm.startPrank(getContract(ETH, "CoreStateRegistry"));
     738 | 
>>>  739 |         InitSingleVaultData memory data = InitSingleVaultData(
     740 |             1,
     741 |             superformId,
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:797`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'data' is modified at line 797, after an external call at line 791. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     795 |         vm.startPrank(getContract(ETH, "CoreStateRegistry"));
     796 | 
>>>  797 |         InitSingleVaultData memory data = InitSingleVaultData(
     798 |             1,
     799 |             1,
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:834`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'data' is modified at line 834, after an external call at line 829. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     832 |         vm.startPrank(getContract(ETH, "CoreStateRegistry"));
     833 | 
>>>  834 |         InitSingleVaultData memory data = InitSingleVaultData(
     835 |             1,
     836 |             superformId,
```
</details>

---

## Resource Management (22)

### [!] Fixed-Gas Transfer

- **File:** `src\crosschain-data\adapters\layerzero-v2\LayerzeroV2Implementation.sol:292`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     290 |     }
     291 | 
>>>  292 |     /// @dev interacts with the LayerZero EndpointV2.send() for sending a message
     293 |     function _lzSend(
     294 |         uint32 _dstEid,
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mocks\InterfaceNotSupported\ERC4626ImplementationInterfaceNotSupported.sol:345`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     343 |         }
     344 | 
>>>  345 |         vaultContract.transfer(receiverAddress_, amount_);
     346 | 
     347 |         emit EmergencyWithdrawalProcessed(receiverAddress_, amount_);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\crosschain-data\extensions\CoreStateRegistry.t.sol:40`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      38 | 
      39 |         vm.prank(getContract(AVAX, "CoreStateRegistry"));
>>>   40 |         MockERC20(getContract(AVAX, "DAI")).transfer(deployer, 999_900_000_000_000_000);
      41 | 
      42 |         vm.expectRevert(Error.INVALID_PAYLOAD_ID.selector);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\crosschain-data\extensions\CoreStateRegistry.t.sol:95`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      93 | 
      94 |         vm.prank(getContract(AVAX, "CoreStateRegistry"));
>>>   95 |         MockERC20(getContract(AVAX, "DAI")).transfer(deployer, 840);
      96 | 
      97 |         uint256 nativeValue = PaymentHelper(getContract(AVAX, "PaymentHelper")).estimateAckCost(1);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\crosschain-data\extensions\CoreStateRegistry.t.sol:104`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     102 | 
     103 |         vm.prank(deployer);
>>>  104 |         MockERC20(getContract(AVAX, "DAI")).transfer(getContract(AVAX, "CoreStateRegistry"), 838);
     105 | 
     106 |         vm.prank(deployer);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\crosschain-data\extensions\CoreStateRegistry.t.sol:1258`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    1256 |             /// @dev ALWAYS have to have a minimum of 1 for this to work (will be lost)
    1257 |             vm.prank(deployer);
>>> 1258 |             IERC20(v.interimOrUnderlyingDstToken1).transfer(getContract(AVAX, "DstSwapper"), 1);
    1259 | 
    1260 |             /// @dev try to call batchUpdateFailedTx, assert that it will pass
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\crosschain-liquidity\DstSwapper.t.sol:834`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     832 | 
     833 |         vm.prank(deployer);
>>>  834 |         payable(getContract(ETH, "DstSwapper")).transfer(1);
     835 | 
     836 |         vm.prank(getContract(ETH, "CoreStateRegistry"));
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\crosschain-liquidity\LiquidityHandler.t.sol:40`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      38 | 
      39 |         vm.startPrank(deployer);
>>>   40 |         MockERC20(token).transfer(address(liquidityHandler), transferAmount);
      41 | 
      42 |         liquidityHandler.dispatchTokensTest(
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\emergency\EmergencyQueue.t.sol:720`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     718 | 
     719 |         vm.prank(deployer);
>>>  720 |         MockERC20(dai).transfer(mrperfect, 2e18);
     721 | 
     722 |         vm.startPrank(mrperfect);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\emergency\EmergencyQueue.t.sol:755`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     753 | 
     754 |         vm.prank(deployer);
>>>  755 |         MockERC20(getContract(ETH, "DAI")).transfer(mrperfect, 2e18);
     756 | 
     757 |         address superformRouter = getContract(ETH, "SuperformRouter");
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\payments\PayMaster.t.sol:76`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      74 |         /// @dev at this point the contract has 1 ether extra
      75 |         address superformRouter = getContract(ETH, "SuperformRouter");
>>>   76 |         payable(superformRouter).transfer(1 ether);
      77 | 
      78 |         /// @dev make a deposit and send in 2 ether extra for other off-chain operations
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:430`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     428 | 
     429 |         /// @dev make sure the form proxy has enough usdc for the user to hack it
>>>  430 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, 3e18);
     431 |         MockERC20(getContract(ETH, "DAI")).approve(superform, 1e18);
     432 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:491`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     489 | 
     490 |         /// @dev make sure the form proxy has enough usdc for the user to hack it
>>>  491 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, 3e18);
     492 |         /// balanceBefore = 3e18
     493 |         MockERC20(getContract(ETH, "DAI")).approve(router, 1e18);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:701`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     699 |         IBaseForm(superform).getVaultAddress();
     700 | 
>>>  701 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, 1e18);
     702 |         vm.stopPrank();
     703 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:734`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     732 |         uint256 superformId = DataLib.packSuperform(superform, FORM_IMPLEMENTATION_IDS[0], ETH);
     733 | 
>>>  734 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, 1e18);
     735 |         vm.stopPrank();
     736 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:791`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     789 |         IBaseForm(superform).getVaultAddress();
     790 | 
>>>  791 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, 1e18);
     792 |         vm.stopPrank();
     793 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:829`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     827 | 
     828 |         vm.prank(deployer);
>>>  829 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, 1e18);
     830 | 
     831 |         /// @dev simulating withdrawals with malicious tx data
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:1133`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    1131 | 
    1132 |         /// Make Superform's initial balance to 10 DAI
>>> 1133 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, daiAmount);
    1134 | 
    1135 |         /// Single deposit 10 DAI to the Superform
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC4626Form.t.sol:1177`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    1175 | 
    1176 |         /// Make Superform's initial balance to 10 DAI
>>> 1177 |         MockERC20(getContract(ETH, "DAI")).transfer(superform, daiAmount);
    1178 | 
    1179 |         /// Single deposit 10 DAI to the Superform
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-forms\superform-form.ERC5115Form.t.sol:1459`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    1457 | 
    1458 |         vm.expectRevert(Error.NOT_IMPLEMENTED.selector);
>>> 1459 |         targetWrapper.transfer(address(11), balance);
    1460 | 
    1461 |         vm.expectRevert(Error.NOT_IMPLEMENTED.selector);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\superform-router\SuperformRouter.t.sol:3177`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    3175 | 
    3176 |         vm.prank(deployer);
>>> 3177 |         MockERC20(getContract(ETH, "DAI")).transfer(address(420), 3e18);
    3178 | 
    3179 |         superformId = DataLib.packSuperform(
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\utils\ProtocolActions.sol:4467`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    4465 | 
    4466 |         vm.prank(deployer);
>>> 4467 |         MockERC20(getContract(ETH, "DAI")).transfer(mrperfect, 2e18);
    4468 | 
    4469 |         address superformRouter = getContract(ETH, "SuperformRouter");
```
</details>

---

## Performance (103)

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\Mainnet.Deploy.s.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      11 | 
      12 |         uint256 trueIndex;
>>>   13 |         for (uint256 i = 0; i < chainIds.length; i++) {
      14 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      15 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\Mainnet.Deploy.s.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      28 | 
      29 |         uint256 trueIndex;
>>>   30 |         for (uint256 i = 0; i < chainIds.length; i++) {
      31 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      32 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\Mainnet.Deploy.s.sol:46`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      44 | 
      45 |         uint256 trueIndex;
>>>   46 |         for (uint256 i = 0; i < chainIds.length; i++) {
      47 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      48 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\Tenderly.Deploy.s.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      11 |         _preDeploymentSetup();
      12 |         uint256 trueIndex;
>>>   13 |         for (uint256 i = 0; i < chainIds.length; i++) {
      14 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      15 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\Tenderly.Deploy.s.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      29 | 
      30 |         uint256 trueIndex;
>>>   31 |         for (uint256 i = 0; i < chainIds.length; i++) {
      32 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      33 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\Tenderly.Deploy.s.sol:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      46 | 
      47 |         uint256 trueIndex;
>>>   48 |         for (uint256 i = 0; i < chainIds.length; i++) {
      49 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      50 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Configure.NewDVN.s.sol:316`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     314 | 
     315 |     function _getTrueIndex(uint256 chainId) public view returns (uint256 index) {
>>>  316 |         for (uint256 i; i < chainIds.length; i++) {
     317 |             if (chainId == chainIds[i]) {
     318 |                 index = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Configure.PreBeraLaunch.s.sol:135`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     133 |                 */
     134 |             } else {
>>>  135 |                 for (uint256 i; i < rescuerAddress.length; i++) {
     136 |                     ids[i] = keccak256("CORE_STATE_REGISTRY_RESCUER_ROLE");
     137 |                     rescuerAddress[i] = CSR_RESCUER;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Configure.PreBeraLaunch.s.sol:151`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     149 | 
     150 |     function _getTrueIndex(uint256 chainId) public view returns (uint256 index) {
>>>  151 |         for (uint256 i; i < chainIds.length; i++) {
     152 |             if (chainId == chainIds[i]) {
     153 |                 index = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.ConfigureERC5115AndDisableAMBs.s.sol:653`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     651 | 
     652 |     function _getTrueIndex(uint256 chainId) public view returns (uint256 index) {
>>>  653 |         for (uint256 i; i < chainIds.length; i++) {
     654 |             if (chainId == chainIds[i]) {
     655 |                 index = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Deploy.Axelar.s.sol:222`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     220 | 
     221 |     function _getTrueIndex(uint256 chainId) public view returns (uint256 index) {
>>>  222 |         for (uint256 i; i < chainIds.length; i++) {
     223 |             if (chainId == chainIds[i]) {
     224 |                 index = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Deploy.BridgeAdaptersV2.s.sol:365`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     363 |         bytes32[] memory ids = new bytes32[](TARGET_CHAINS.length);
     364 | 
>>>  365 |         for (uint256 i; i < rescuerAddress.length; i++) {
     366 |             ids[i] = 0xf98729ec1ce0343ca1d11c51d1d2d3aa1a7b3f4f6876d0611e0a6fa86520a0cb;
     367 |             rescuerAddress[i] = 0x90ed07A867bDb6a73565D7abBc7434Dd810Fafc5;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Deploy.BridgeAdaptersV2.s.sol:458`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     456 | 
     457 |     function _getTrueIndex(uint256 chainId) public view returns (uint256 index) {
>>>  458 |         for (uint256 i; i < chainIds.length; i++) {
     459 |             if (chainId == chainIds[i]) {
     460 |                 index = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Deploy.RescuerMissedConfig.s.sol:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      46 |         bytes32[] memory ids = new bytes32[](TARGET_CHAINS.length);
      47 | 
>>>   48 |         for (uint256 i; i < rescuerAddress.length; i++) {
      49 |             ids[i] = keccak256("CORE_STATE_REGISTRY_RESCUER_ROLE");
      50 |             rescuerAddress[i] = CSR_RESCUER;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Abstract.Deploy.RescuerMissedConfig.s.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      82 |         bytes32[] memory ids = new bytes32[](TARGET_CHAINS.length);
      83 | 
>>>   84 |         for (uint256 i; i < rescuerAddress.length; i++) {
      85 |             ids[i] = keccak256("CORE_STATE_REGISTRY_RESCUER_ROLE");
      86 |             rescuerAddress[i] = CSR_RESCUER;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\DecodeULNConfig.sol:28`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      26 | 
      27 |     function _getTrueIndex(uint256 chainId) public view returns (uint256 index) {
>>>   28 |         for (uint256 i; i < chainIds.length; i++) {
      29 |             if (chainId == chainIds[i]) {
      30 |                 index = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Configure.NewDVN.s.sol:12`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      10 | 
      11 |         uint256 trueIndex;
>>>   12 |         for (uint256 i = 0; i < chainIds.length; i++) {
      13 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      14 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Configure.NewDVN.s.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      33 |         uint256 dstTrueIndex;
      34 | 
>>>   35 |         for (uint256 i = 0; i < chainIds.length; i++) {
      36 |             if (TARGET_CHAINS[selectedSrcChainIndex] == chainIds[i]) {
      37 |                 srcTrueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Configure.NewDVN.s.sol:63`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      61 |         uint256 dstTrueIndex;
      62 | 
>>>   63 |         for (uint256 i = 0; i < chainIds.length; i++) {
      64 |             if (TARGET_CHAINS[selectedSrcChainIndex] == chainIds[i]) {
      65 |                 srcTrueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Configure.NewDVN.s.sol:91`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      89 |         uint256 dstTrueIndex;
      90 | 
>>>   91 |         for (uint256 i = 0; i < chainIds.length; i++) {
      92 |             if (TARGET_CHAINS[selectedSrcChainIndex] == chainIds[i]) {
      93 |                 srcTrueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Configure.PreBera.s.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      11 | 
      12 |         uint256 trueIndex;
>>>   13 |         for (uint256 i = 0; i < chainIds.length; i++) {
      14 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      15 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:12`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      10 | 
      11 |         uint256 trueIndex;
>>>   12 |         for (uint256 i = 0; i < chainIds.length; i++) {
      13 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      14 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      25 | 
      26 |         uint256 trueIndex;
>>>   27 |         for (uint256 i = 0; i < chainIds.length; i++) {
      28 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      29 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      40 | 
      41 |         uint256 trueIndex;
>>>   42 |         for (uint256 i = 0; i < chainIds.length; i++) {
      43 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      44 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:57`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      55 | 
      56 |         uint256 trueIndex;
>>>   57 |         for (uint256 i = 0; i < chainIds.length; i++) {
      58 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      59 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:78`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      76 | 
      77 |         uint256 trueIndex;
>>>   78 |         for (uint256 i = 0; i < chainIds.length; i++) {
      79 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      80 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:99`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      97 | 
      98 |         uint256 trueIndex;
>>>   99 |         for (uint256 i = 0; i < chainIds.length; i++) {
     100 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
     101 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:114`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     112 | 
     113 |         uint256 trueIndex;
>>>  114 |         for (uint256 i = 0; i < chainIds.length; i++) {
     115 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
     116 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.ConfigureERC5115AndDisableAMBs.s.sol:129`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     127 | 
     128 |         uint256 trueIndex;
>>>  129 |         for (uint256 i = 0; i < chainIds.length; i++) {
     130 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
     131 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.5115Form.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.5115Form.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.5115To4626Factory.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.7540Form.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.7540Form.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.AsyncStateRegistry.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.AsyncStateRegistry.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:17`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      15 |         _preDeploymentSetup();
      16 |         uint256 trueIndex;
>>>   17 |         for (uint256 i = 0; i < chainIds.length; i++) {
      18 |             if (TARGET_DEPLOYMENT_CHAINS[selectedChainIndex] == chainIds[i]) {
      19 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      33 | 
      34 |         uint256 trueIndex;
>>>   35 |         for (uint256 i = 0; i < chainIds.length; i++) {
      36 |             if (TARGET_DEPLOYMENT_CHAINS[selectedChainIndex] == chainIds[i]) {
      37 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      50 |         uint256 trueIndex;
      51 | 
>>>   52 |         for (uint256 i = 0; i < chainIds.length; i++) {
      53 |             if (TARGET_DEPLOYMENT_CHAINS[selectedChainIndex] == chainIds[i]) {
      54 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 | 
      68 |         uint256 trueIndex;
>>>   69 |         for (uint256 i = 0; i < chainIds.length; i++) {
      70 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      71 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:89`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      87 | 
      88 |         uint256 trueIndex;
>>>   89 |         for (uint256 i = 0; i < chainIds.length; i++) {
      90 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      91 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:107`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     105 |         _preDeploymentSetup();
     106 |         uint256 trueIndex;
>>>  107 |         for (uint256 i = 0; i < chainIds.length; i++) {
     108 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
     109 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.NewChain.s.sol:128`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     126 |         uint256 trueIndex;
     127 | 
>>>  128 |         for (uint256 i = 0; i < chainIds.length; i++) {
     129 |             if (TARGET_DEPLOYMENT_CHAINS[selectedChainIndex] == chainIds[i]) {
     130 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.OneInchValidator.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.OneInchValidator.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.PaymentHelperV2.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.PaymentHelperV2.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.PaymentHelperV2.s.sol:39`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      37 | 
      38 |         uint256 trueIndex;
>>>   39 |         for (uint256 i = 0; i < chainIds.length; i++) {
      40 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      41 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.RewardsDistributor.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.RewardsDistributor.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.SuperformRouterPlus.s.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      11 | 
      12 |         uint256 trueIndex;
>>>   13 |         for (uint256 i = 0; i < chainIds.length; i++) {
      14 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      15 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.SuperformRouterPlus.s.sol:29`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      27 | 
      28 |         uint256 trueIndex;
>>>   29 |         for (uint256 i = 0; i < chainIds.length; i++) {
      30 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      31 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.SuperformRouterPlus.s.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      45 | 
      46 |         uint256 trueIndex;
>>>   47 |         for (uint256 i = 0; i < chainIds.length; i++) {
      48 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      49 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy.SuperformRouterPlus.s.sol:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      60 |         _preDeploymentSetup();
      61 |         uint256 trueIndex;
>>>   62 |         for (uint256 i = 0; i < chainIds.length; i++) {
      63 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      64 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy1inch.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy1inch.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.Deploy1inch.s.sol:39`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      37 | 
      38 |         uint256 trueIndex;
>>>   39 |         for (uint256 i = 0; i < chainIds.length; i++) {
      40 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      41 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployAxelar.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployAxelar.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployAxelar.s.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      39 | 
      40 |         uint256 trueIndex;
>>>   41 |         for (uint256 i = 0; i < chainIds.length; i++) {
      42 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      43 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployBridgeAdaptersV2.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployBridgeAdaptersV2.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployBridgeAdaptersV2.s.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      39 | 
      40 |         uint256 trueIndex;
>>>   41 |         for (uint256 i = 0; i < chainIds.length; i++) {
      42 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      43 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployDeBridgeValidators.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployDeBridgeValidators.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployLiFiValidatorV2.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployLiFiValidatorV2.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployPayloadHelper.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployPayloadHelper.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployPaymasterV2.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployPaymasterV2.s.sol:25`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      23 | 
      24 |         uint256 trueIndex;
>>>   25 |         for (uint256 i = 0; i < chainIds.length; i++) {
      26 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      27 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DeployRescuerMissedConfig.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.DisableInvalidDeployment.s.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      11 |         _preDeploymentSetup();
      12 |         uint256 trueIndex;
>>>   13 |         for (uint256 i = 0; i < chainIds.length; i++) {
      14 |             if (TARGET_DEPLOYMENT_CHAINS[selectedChainIndex] == chainIds[i]) {
      15 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.EnableBroadcasting.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.EnableBroadcasting.s.sol:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      25 | 
      26 |         uint256 trueIndex;
>>>   27 |         for (uint256 i = 0; i < chainIds.length; i++) {
      28 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      29 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.SuperRegistryLiFiValidatorV2Paymaster.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.UpdatePaymentHelper.s.sol:11`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
       9 | 
      10 |         uint256 trueIndex;
>>>   11 |         for (uint256 i = 0; i < chainIds.length; i++) {
      12 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      13 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\forge-scripts\misc\Mainnet.UpdatePriceFeeds.s.sol:12`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      10 | 
      11 |         uint256 trueIndex;
>>>   12 |         for (uint256 i = 0; i < chainIds.length; i++) {
      13 |             if (TARGET_CHAINS[selectedChainIndex] == chainIds[i]) {
      14 |                 trueIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\forms\wrappers\ERC5115To4626Wrapper.sol:278`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     276 |             address[] memory tokensIn = IStandardizedYield(vault_).getTokensIn();
     277 |             bool found;
>>>  278 |             for (uint256 i = 0; i < tokensIn.length; i++) {
     279 |                 if (tokensIn[i] == token_) {
     280 |                     found = true;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\forms\wrappers\ERC5115To4626Wrapper.sol:301`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     299 |             address[] memory tokensOut = IStandardizedYield(vault_).getTokensOut();
     300 |             bool found;
>>>  301 |             for (uint256 i = 0; i < tokensOut.length; i++) {
     302 |                 if (tokensOut[i] == token_) {
     303 |                     found = true;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\forms\wrappers\ERC5115To4626WrapperFactory.sol:119`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     117 | 
     118 |         wrappers_ = new address[](len);
>>>  119 |         for (uint256 i; i < len; i++) {
     120 |             wrappers_[i] = _createWrapperWithSuperform(
     121 |                 formImplementationIds_[i], underlyingVaultAddresses[i], tokenIns[i], tokenOuts[i]
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\forms\wrappers\ERC5115To4626WrapperFactory.sol:163`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     161 | 
     162 |         address newFormImpl;
>>>  163 |         for (uint256 i = 0; i < wrapperKeys.length; i++) {
     164 |             WrapperMetadata storage metadata = wrappers[wrapperKeys[i]];
     165 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\payments\PaymentHelper.sol:841`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     839 |     {
     840 |         uint256 len = liqRequests_.length;
>>>  841 |         for (uint256 i; i < len; i++) {
     842 |             /// @dev liqRequests[i].token on withdraws is the desired token
     843 |             /// @dev if token is address(0) -> user wants settlement without any liq data
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\payments\PaymentHelperExtn.sol:168`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     166 |     function estimateBatchDeposit(bytes[] calldata callData_) external view override returns (uint256 msgValue) {
     167 |         uint256 len = callData_.length;
>>>  168 |         for (uint256 i = 0; i < len; i++) {
     169 |             SingleDirectSingleVaultStateReq memory req =
     170 |                 SingleDirectSingleVaultStateReq({ superformData: _decodeSingleVaultData(callData_[i]) });
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\fuzz\crosschain-data\adapters\LayerzeroImplementation.t.sol:91`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      89 | 
      90 |     function test_estimateFeesWithInvalidChainId(uint64 chainId) public {
>>>   91 |         for (uint256 i = 0; i < chainIds.length; i++) {
      92 |             vm.assume(chainId != chainIds[i]);
      93 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\fuzz\crosschain-data\adapters\LayerzeroImplementation.t.sol:325`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     323 |         uint256 userIndex = userSeed_ % users.length;
     324 | 
>>>  325 |         for (uint256 i = 0; i < chainIds.length; i++) {
     326 |             vm.assume(chainId != chainIds[i]);
     327 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariant\rewards-distributor\RewardsDistributorBase.invariant.t.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      39 | 
      40 |         vm.selectFork(FORKS[OP]);
>>>   41 |         for (uint256 i; i < 3; i++) {
      42 |             vm.writeLine(path, string.concat("Stats for period id: ", Strings.toString(i)));
      43 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariant\rewards-distributor\handlers\RewardsDistributorHandler.sol:80`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      78 |         vm.startPrank(deployer);
      79 | 
>>>   80 |         for (uint256 i = 0; i < 3; i++) {
      81 |             bytes32 root;
      82 |             uint256 claimers;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariant\rewards-distributor\handlers\RewardsDistributorHandler.sol:119`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     117 | 
     118 |         /// @dev add max amount of users here
>>>  119 |         for (uint256 i = 0; i < 3; i++) {
     120 |             address[] memory testUsersMem2 = new address[](totalTestUsers[i]);
     121 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\invariant\rewards-distributor\handlers\RewardsDistributorHandler.sol:146`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     144 |         vm.writeLine(path, string.concat("Normal Run id: ", Strings.toString(seed)));
     145 | 
>>>  146 |         for (uint256 i; i < 100; i++) {
     147 |             uint256 periodId = randomPeriod(seed, i);
     148 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\rewards-distributor\RewardsDistributor.t.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 | 
      68 |         /// @dev add max amount of users here
>>>   69 |         for (uint256 i = 0; i < 3; i++) {
      70 |             (, claimers,,,,,) = _generateMerkleTree(MerkleReader.MerkleArgs(i, address(0), OP));
      71 |             totalTestUsers.push(claimers);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\rewards-distributor\RewardsDistributor.t.sol:221`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     219 |         uint256[] memory balanceBefore = new uint256[](2);
     220 | 
>>>  221 |         for (uint256 i = 0; i < tokensToRescue.length; i++) {
     222 |             balanceBefore[i] = IERC20(tokensToRescue[i]).balanceOf(address(rewards));
     223 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\rewards-distributor\RewardsDistributor.t.sol:227`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     225 |         rewards.rescueRewards(tokensToRescue, amountsToRescue);
     226 | 
>>>  227 |         for (uint256 i = 0; i < tokensToRescue.length; i++) {
     228 |             assertEq(IERC20(tokensToRescue[i]).balanceOf(address(rewards)), balanceBefore[i] - amountsToRescue[i]);
     229 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:1780`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    1778 |         {
    1779 |             MultiVaultSFData[] memory multiVaultData = new MultiVaultSFData[](2);
>>> 1780 |             for (uint256 i = 0; i < 2; i++) {
    1781 |                 multiVaultData[i] = MultiVaultSFData({
    1782 |                     superformIds: new uint256[](2),
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:1981`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    1979 |         address interimAsset = getContract(SOURCE_CHAIN, "DAI");
    1980 | 
>>> 1981 |         for (uint256 i = 0; i < 2; i++) {
    1982 |             sfData.liqRequests[i] = LiqRequest({
    1983 |                 txData: "",
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:2245`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    2243 |         address interimAsset = getContract(SOURCE_CHAIN, "DAI");
    2244 | 
>>> 2245 |         for (uint256 i = 0; i < 2; i++) {
    2246 |             sfData.liqRequests[i] = LiqRequest({
    2247 |                 txData: "",
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:4153`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    4151 |         chainIds[1] = superformChainId2;
    4152 | 
>>> 4153 |         for (uint256 i = 0; i < 2; i++) {
    4154 |             vm.selectFork(FORKS[chainIds[i]]);
    4155 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:4674`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    4672 |         });
    4673 | 
>>> 4674 |         for (uint256 i = 0; i < superformIds.length; i++) {
    4675 |             (address superform,,) = superformIds[i].getSuperform();
    4676 |             address underlyingToken = IBaseForm(superform).getVaultAsset();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:4730`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    4728 |         chainIds[1] = superformChainId2;
    4729 | 
>>> 4730 |         for (uint256 i = 0; i < superformIds.length; i++) {
    4731 |             vm.selectFork(FORKS[chainIds[i]]);
    4732 |             (address superform,,) = superformIds[i].getSuperform();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:4908`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    4906 |         expDstChainAddresses[0] = address(getContract(toChain, "WormholeARImplementation"));
    4907 | 
>>> 4908 |         for (uint256 i = 0; i < AMBs.length; i++) {
    4909 |             if (AMBs[i] == 2) {
    4910 |                 // Hyperlane
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\router-plus\SuperformRouterPlus.t.sol:5189`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    5187 |         });
    5188 | 
>>> 5189 |         for (uint256 i = 0; i < superformIds.length; i++) {
    5190 |             (address superform,,) = superformIds[i].getSuperform();
    5191 |             address underlyingToken = IBaseForm(superform).getVaultAsset();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\utils\BaseSetup.sol:1783`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    1781 |         /// @dev These blocks have been chosen arbitrarily - can be updated to other values
    1782 |         mapping(uint64 => uint256) storage forks = FORKS;
>>> 1783 |         for (uint256 i = 0; i < chainIds.length; i++) {
    1784 |             // find selected chain ids and assign to selectedChainIds mapping
    1785 |             for (uint256 j = 0; j < defaultChainIds.length; j++) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\utils\MainnetBaseSetup.sol:124`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     122 |         for (uint256 j = 0; j < TARGET_DEPLOYMENT_CHAINS.length; ++j) {
     123 |             uint256 trueIndex;
>>>  124 |             for (uint256 i = 0; i < chainIds.length; i++) {
     125 |                 if (TARGET_DEPLOYMENT_CHAINS[j] == chainIds[i]) {
     126 |                     trueIndex = i;
```
</details>

---

## Code Quality (24)

### [~] UNCLEAR require Error Message

- **File:** `script\forge-scripts\safe\BatchScript.sol:268`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     266 | 
     267 |     function _simulateBatch(address safe_, Batch memory batch_) internal {
>>>  268 |         require(batch_.to.code.length > 0, "No code at address");
     269 |         vm.allowCheatcodes(safe_);
     270 |         (bool success, bytes memory data) = delegatePrank(safe_, batch_.to, batch_.data);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\BaseERC7540Mock.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      92 |         returns (bool)
      93 |     {
>>>   94 |         require(block.timestamp <= deadline, "ERC7540Vault/authorization-expired");
      95 |         require(controller != address(0), "ERC7540Vault/invalid-controller");
      96 |         require(!authorizations[controller][nonce], "ERC7540Vault/authorization-used");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\BaseERC7540Mock.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 |         require(block.timestamp <= deadline, "ERC7540Vault/authorization-expired");
      95 |         require(controller != address(0), "ERC7540Vault/invalid-controller");
>>>   96 |         require(!authorizations[controller][nonce], "ERC7540Vault/authorization-used");
      97 | 
      98 |         authorizations[controller][nonce] = true;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\BaseERC7540Mock.sol:188`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     186 | 
     187 |     function validateController(address controller) internal view {
>>>  188 |         require(controller == msg.sender || isOperator[controller][msg.sender], "ERC7540Vault/invalid-controller");
     189 |     }
     190 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMock.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 |     /// @inheritdoc IERC7540Deposit
      20 |     function requestDeposit(uint256 assets, address controller, address owner) public returns (uint256) {
>>>   21 |         require(owner == msg.sender || isOperator[owner][msg.sender], "ERC7540Vault/invalid-owner");
      22 |         require(IERC20(asset).balanceOf(owner) >= assets, "ERC7540Vault/insufficient-balance");
      23 |         SafeTransferLib.safeTransferFrom(asset, owner, address(this), assets);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMock.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      59 |         if (REQUEST_ID_FUNGIBLE) revert("ERC7540Vault/invalid-deposit-rid-fungible");
      60 |         validateController(controller);
>>>   61 |         require(assets == assetBalances[controller][0][1], "ERC7540Vault/invalid-deposit-claim");
      62 | 
      63 |         assetBalances[controller][0][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMock.sol:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      79 | 
      80 |         validateController(controller);
>>>   81 |         require(assets == assetBalances[controller][requestId][1], "ERC7540Vault/invalid-deposit-claim");
      82 | 
      83 |         assetBalances[controller][requestId][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMockRedeemRevert.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 |     /// @inheritdoc IERC7540Deposit
      20 |     function requestDeposit(uint256 assets, address controller, address owner) public returns (uint256) {
>>>   21 |         require(owner == msg.sender || isOperator[owner][msg.sender], "ERC7540Vault/invalid-owner");
      22 |         require(IERC20(asset).balanceOf(owner) >= assets, "ERC7540Vault/insufficient-balance");
      23 |         SafeTransferLib.safeTransferFrom(asset, owner, address(this), assets);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMockRedeemRevert.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      59 |         if (REQUEST_ID_FUNGIBLE) revert("ERC7540Vault/invalid-deposit-rid-fungible");
      60 |         validateController(controller);
>>>   61 |         require(assets == assetBalances[controller][0][1], "ERC7540Vault/invalid-deposit-claim");
      62 | 
      63 |         assetBalances[controller][0][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMockRedeemRevert.sol:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      79 | 
      80 |         validateController(controller);
>>>   81 |         require(assets == assetBalances[controller][requestId][1], "ERC7540Vault/invalid-deposit-claim");
      82 | 
      83 |         assetBalances[controller][requestId][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncDepositMockRevert.sol:21`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      19 |     /// @inheritdoc IERC7540Deposit
      20 |     function requestDeposit(uint256 assets, address controller, address owner) public returns (uint256) {
>>>   21 |         require(owner == msg.sender || isOperator[owner][msg.sender], "ERC7540Vault/invalid-owner");
      22 |         require(IERC20(asset).balanceOf(owner) >= assets, "ERC7540Vault/insufficient-balance");
      23 |         SafeTransferLib.safeTransferFrom(asset, owner, address(this), assets);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncRedeemMock.sol:73`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      71 | 
      72 |         validateController(controller);
>>>   73 |         require(shares == shareBalances[controller][0][1], "ERC7540Vault/invalid-redeem-claim");
      74 | 
      75 |         shareBalances[controller][0][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540AsyncRedeemMock.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      92 | 
      93 |         validateController(controller);
>>>   94 |         require(shares == shareBalances[controller][requestId][1], "ERC7540Vault/invalid-redeem-claim");
      95 | 
      96 |         shareBalances[controller][requestId][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540FullyAsyncMock.sol:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      21 |     /// @inheritdoc IERC7540Deposit
      22 |     function requestDeposit(uint256 assets, address controller, address owner) public returns (uint256) {
>>>   23 |         require(owner == msg.sender || isOperator[owner][msg.sender], "ERC7540Vault/invalid-owner");
      24 |         require(IERC20(asset).balanceOf(owner) >= assets, "ERC7540Vault/insufficient-balance");
      25 |         SafeTransferLib.safeTransferFrom(asset, owner, address(this), assets);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540FullyAsyncMock.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      92 |         if (REQUEST_ID_FUNGIBLE) revert("ERC7540Vault/invalid-deposit-rid-fungible");
      93 |         validateController(controller);
>>>   94 |         require(assets == assetBalances[controller][0][1], "ERC7540Vault/invalid-deposit-claim");
      95 | 
      96 |         assetBalances[controller][0][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540FullyAsyncMock.sol:114`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     112 | 
     113 |         validateController(controller);
>>>  114 |         require(assets == assetBalances[controller][requestId][1], "ERC7540Vault/invalid-deposit-claim");
     115 | 
     116 |         assetBalances[controller][requestId][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540FullyAsyncMock.sol:132`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     130 | 
     131 |         validateController(controller);
>>>  132 |         require(shares == shareBalances[controller][0][1], "ERC7540Vault/invalid-redeem-claim");
     133 | 
     134 |         shareBalances[controller][0][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\ERC7540FullyAsyncMock.sol:153`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     151 | 
     152 |         validateController(controller);
>>>  153 |         require(shares == shareBalances[controller][requestId][1], "ERC7540Vault/invalid-redeem-claim");
     154 | 
     155 |         shareBalances[controller][requestId][1] = 0;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\7540MockUtils\ERC20.sol:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      53 |         require(to != address(0) && to != address(this), "ERC20/invalid-address");
      54 |         uint256 balance = balanceOf[msg.sender];
>>>   55 |         require(balance >= value, "ERC20/insufficient-balance");
      56 | 
      57 |         unchecked {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\7540MockUtils\ERC20.sol:75`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      73 |         require(to != address(0) && to != address(this), "ERC20/invalid-address");
      74 |         uint256 balance = balanceOf[from];
>>>   75 |         require(balance >= value, "ERC20/insufficient-balance");
      76 | 
      77 |         if (from != sender) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\7540MockUtils\ERC20.sol:80`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      78 |             uint256 allowed = allowance[from][sender];
      79 |             if (allowed != type(uint256).max) {
>>>   80 |                 require(allowed >= value, "ERC20/insufficient-allowance");
      81 |                 unchecked {
      82 |                     allowance[from][sender] = allowed - value;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\7540MockUtils\ERC20.sol:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     119 |     function burn(address from, uint256 value) external {
     120 |         uint256 balance = balanceOf[from];
>>>  121 |         require(balance >= value, "ERC20/insufficient-balance");
     122 | 
     123 |         if (from != msg.sender) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\7540MockUtils\ERC20.sol:126`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     124 |             uint256 allowed = allowance[from][msg.sender];
     125 |             if (allowed != type(uint256).max) {
>>>  126 |                 require(allowed >= value, "ERC20/insufficient-allowance");
     127 | 
     128 |                 unchecked {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mocks\7540MockUtils\ERC20.sol:145`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     143 |     // --- Approve by signature ---
     144 |     function permit(address owner, address spender, uint256 value, uint256 deadline, bytes memory signature) public {
>>>  145 |         require(block.timestamp <= deadline, "ERC20/permit-expired");
     146 |         require(owner != address(0), "ERC20/invalid-owner");
     147 | 
```
</details>

---


---
*Generated by BugHunter*