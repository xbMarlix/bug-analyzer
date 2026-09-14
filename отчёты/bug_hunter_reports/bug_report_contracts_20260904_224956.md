# BugHunter Report: contracts

**Generated:** 2026-09-04 22:49:56
**Project:** `C:\Users\123123\Desktop\silo\silo-core\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 254 |
| Total lines | 18,081 |
| Bugs found | 42 |
| !! High | 15 |
| ! Medium | 3 |
| ~ Low | 24 |

### Languages Detected

- **solidity**: 127 files

## Security (15)

### [!!] Unsafe Delegatecall

- **File:** `hooks\PendleRewardsClaimer.sol:47`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      45 |     /// @notice Redeem rewards from Pendle
      46 |     /// @dev Redeem rewards from Pendle and transfer them to the incentives controller for immediate distribution.
>>>   47 |     /// This function is designed to be called by the hook from the silo via delegatecall.
      48 |     /// @param _market Pendle market address
      49 |     /// @param _incentivesController Incentives controller address
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `hooks\PendleRewardsClaimer.sol:64`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      62 |     {
      63 |         rewardTokens = _market.getRewardTokens();
>>>   64 |         _market.redeemRewards({user: address(this)}); // address(this) is a Silo as we do a delegatecall.
      65 |         rewards = new uint256[](rewardTokens.length);
      66 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `hooks\PendleRewardsClaimer.sol:132`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     130 |             _target: address(this),
     131 |             _value: 0,
>>>  132 |             _callType: ISilo.CallType.Delegatecall,
     133 |             _input: input
     134 |         });
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `hooks\defaulting\PartialLiquidationByDefaulting.sol:255`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     253 |             _target: LIQUIDATION_LOGIC,
     254 |             _value: 0,
>>>  255 |             _callType: ISilo.CallType.Delegatecall,
     256 |             _input: _calldata
     257 |         });
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `interfaces\ISilo.sol:51`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      49 |     enum CallType {
      50 |         Call, // default
>>>   51 |         Delegatecall
      52 |     }
      53 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `interfaces\ISilo.sol:207`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     205 |     /// @param _target address of the contract to call
     206 |     /// @param _value amount of ETH to send
>>>  207 |     /// @param _callType type of the call (Call or Delegatecall)
     208 |     /// @param _input calldata for the call
     209 |     function callOnBehalfOfSilo(address _target, uint256 _value, CallType _callType, bytes calldata _input)
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `lib\Actions.sol:437`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     435 |     /// @param _target address of the contract to call
     436 |     /// @param _value amount of ETH to send
>>>  437 |     /// @param _callType type of the call (Call or Delegatecall)
     438 |     /// @param _input calldata for the call
     439 |     function callOnBehalfOfSilo(address _target, uint256 _value, ISilo.CallType _callType, bytes calldata _input)
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `lib\Actions.sol:450`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     448 |         // Silo will not send back any ether leftovers after the call.
     449 |         // The hook receiver should request the ether if needed in a separate call.
>>>  450 |         if (_callType == ISilo.CallType.Delegatecall) {
     451 |             (success, result) = _target.delegatecall(_input); // solhint-disable-line avoid-low-level-calls
     452 |         } else {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `lib\Actions.sol:451`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     449 |         // The hook receiver should request the ether if needed in a separate call.
     450 |         if (_callType == ISilo.CallType.Delegatecall) {
>>>  451 |             (success, result) = _target.delegatecall(_input); // solhint-disable-line avoid-low-level-calls
     452 |         } else {
     453 |             (success, result) = _target.call{value: _value}(_input); // solhint-disable-line avoid-low-level-calls
```
</details>

---

### [!!] Selfdestruct Used

- **File:** `lib\IsContract.sol:22`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** selfdestruct sends all remaining ETH to a target and destroys the contract, potentially bricking funds.

**Fix:** Avoid selfdestruct unless absolutely necessary and carefully reviewed.

<details>
<summary>Code</summary>

```
      20 |      *
      21 |      * Furthermore, `isContract` will also return true if the target contract within
>>>   22 |      * the same transaction is already scheduled for destruction by `SELFDESTRUCT`,
      23 |      * which only has an effect at the end of a transaction.
      24 |      * ====
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `lib\ShareTokenLib.sol:130`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     128 |         // Share token will not send back any ether leftovers after the call.
     129 |         // The hook receiver should request the ether if needed in a separate call.
>>>  130 |         if (_callType == ISilo.CallType.Delegatecall) {
     131 |             (success, result) = _target.delegatecall(_input); // solhint-disable-line avoid-low-level-calls
     132 |         } else {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `lib\ShareTokenLib.sol:131`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     129 |         // The hook receiver should request the ether if needed in a separate call.
     130 |         if (_callType == ISilo.CallType.Delegatecall) {
>>>  131 |             (success, result) = _target.delegatecall(_input); // solhint-disable-line avoid-low-level-calls
     132 |         } else {
     133 |             (success, result) = _target.call{value: _value}(_input); // solhint-disable-line avoid-low-level-calls
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `silo-router\SiloRouterV2.sol:49`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      47 |         for (uint256 i = 0; i < data.length; i++) {
      48 |             // expect implementation not to use `msg.value`
>>>   49 |             results[i] = Address.functionDelegateCall(IMPLEMENTATION, data[i]);
      50 |         }
      51 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `silo-router\SiloRouterV2Implementation.sol:80`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      78 |  */
      79 | 
>>>   80 | /// @dev This contract should never use `msg.value` as `SiloRouterV2` contract executes multicall with a delegatecall.
      81 | /// @dev This contract should not work with storage. If needed, update SiloRouterV2 accordingly.
      82 | /// @dev Caller should ensure that the router balance is empty after multicall.
```
</details>

---

### [!!] Reentrancy Vector (External Call with Value)

- **File:** `utils\RescueTokens.sol:39`
- **Severity:** HIGH
- **Confidence:** 55%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} detected. If state is updated after this call, an attacker can re-enter.

**Fix:** Follow checks-effects-interactions: update state before external calls, or use a reentrancy guard.

<details>
<summary>Code</summary>

```
      37 |         require(balance != 0, EmptyBalance());
      38 | 
>>>   39 |         (bool success, ) = payable(TOKEN_RECEIVER).call{value: balance}("");
      40 |         require(success, NativeTokenTransferFailed());
      41 | 
```
</details>

---

## Logic (1)

### [!] Timestamp Dependence

- **File:** `incentives\base\DistributionManager.sol:332`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     330 |         }
     331 | 
>>>  332 |         uint256 currentTimestamp = block.timestamp > distributionEnd ? distributionEnd : block.timestamp;
     333 |         uint256 timeDelta = currentTimestamp - lastUpdateTimestamp;
     334 | 
```
</details>

---

## Resource Management (2)

### [!] Fixed-Gas Transfer

- **File:** `hooks\liquidation\PartialLiquidation.sol:249`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     247 |             if (_isToAssetsConvertionError(e)) {
     248 |                 // forge-lint: disable-next-line(erc20-unchecked-transfer)
>>>  249 |                 IERC20(_shareToken).transfer(msg.sender, _shares);
     250 |             } else {
     251 |                 RevertLib.revertBytes(e, string(""));
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `utils\ShareToken.sol:153`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     151 |         ISiloConfig siloConfigCached = _crossNonReentrantBefore();
     152 | 
>>>  153 |         result = ERC20Upgradeable.transfer(_to, _amount);
     154 | 
     155 |         siloConfigCached.turnOffReentrancyProtection();
```
</details>

---

## Performance (23)

### [~] Unoptimized Loop

- **File:** `SiloDeployer.sol:152`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     150 |         if (c == 0) return;
     151 | 
>>>  152 |         for (uint256 i = 0; i < c; i++) {
     153 |             Whitelist(_hookReceiver).grantRole(ALLOWED_ROLE, _addresses[i]);
     154 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `SiloLens.sol:37`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      35 |         versions = new string[](_contracts.length);
      36 | 
>>>   37 |         for (uint256 i; i < _contracts.length; i++) {
      38 |             versions[i] = SiloLensLib.getVersion(_contracts[i]);
      39 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `SiloLens.sol:75`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      73 |         usersLTs = new uint256[](_borrowers.length);
      74 | 
>>>   75 |         for (uint256 i; i < _borrowers.length; i++) {
      76 |             Borrower memory borrower = _borrowers[i];
      77 |             usersLTs[i] = SiloLensLib.getUserLt(borrower.silo, borrower.wallet);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `SiloLens.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      82 |         healths = new BorrowerHealth[](_borrowers.length);
      83 | 
>>>   84 |         for (uint256 i; i < _borrowers.length; i++) {
      85 |             Borrower memory borrower = _borrowers[i];
      86 |             BorrowerHealth memory health = healths[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `SiloLens.sol:283`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     281 |         aprs = new APR[](_silos.length);
     282 | 
>>>  283 |         for (uint256 i; i < _silos.length; i++) {
     284 |             ISilo silo = _silos[i];
     285 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `SiloLens.sol:305`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     303 |         programsNames = new string[](originalProgramsNames.length);
     304 | 
>>>  305 |         for (uint256 i; i < originalProgramsNames.length; i++) {
     306 |             bytes memory originalProgramName = bytes(originalProgramsNames[i]);
     307 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `hooks\PendleRewardsClaimer.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      65 |         rewards = new uint256[](rewardTokens.length);
      66 | 
>>>   67 |         for (uint256 i = 0; i < rewardTokens.length; i++) {
      68 |             address rewardToken = rewardTokens[i];
      69 |             // Pendle should never distribute rewards in the Pendle market LP tokens.
```
</details>

---

### [~] Unoptimized Loop

- **File:** `hooks\PendleRewardsClaimer.sol:143`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     141 |         (rewardTokens, rewards) = abi.decode(data, (address[], uint256[]));
     142 | 
>>>  143 |         for (uint256 i = 0; i < rewardTokens.length; i++) {
     144 |             uint256 rewardAmount = rewards[i];
     145 |             if (rewardAmount == 0) continue;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\SiloIncentivesController.sol:91`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      89 | 
      90 |         // iterate over incentives programs
>>>   91 |         for (uint256 i = 0; i < numberOfPrograms; i++) {
      92 |             bytes32 programId = _incentivesProgramIds.at(i);
      93 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\base\BaseIncentivesController.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     110 |         (uint256 stakedByUser, uint256 totalStaked) = _getScaledUserBalanceAndSupply(_user);
     111 | 
>>>  112 |         for (uint256 i = 0; i < _programNames.length; i++) {
     113 |             bytes32 programId = getProgramId(_programNames[i]);
     114 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\base\BaseIncentivesController.sol:243`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     241 |         AccruedRewards[] memory accruedRewards
     242 |     ) internal virtual {
>>>  243 |         for (uint256 i = 0; i < accruedRewards.length; i++) {
     244 |             uint256 unclaimedRewards = _usersUnclaimedRewards[user][accruedRewards[i].programId];
     245 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\base\BaseIncentivesController.sol:302`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     300 |      */
     301 |     function _requireExistingPrograms(bytes32[] memory _programIds) internal view virtual {
>>>  302 |         for (uint256 i = 0; i < _programIds.length; i++) {
     303 |             require(_incentivesProgramIds.contains(_programIds[i]), IncentivesProgramNotFound());
     304 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\base\BaseIncentivesController.sol:320`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     318 |         programIds = new bytes32[](_programNames.length);
     319 | 
>>>  320 |         for (uint256 i = 0; i < _programNames.length; i++) {
     321 |             programIds[i] = getProgramId(_programNames[i]);
     322 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\base\DistributionManager.sol:116`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     114 |         programsNames = new string[](length);
     115 | 
>>>  116 |         for (uint256 i = 0; i < length; i++) {
     117 |             programsNames[i] = getProgramName(_incentivesProgramIds.values()[i]);
     118 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `incentives\base\DistributionManager.sol:240`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     238 |         (uint256 userStaked, uint256 totalStaked) = _getScaledUserBalanceAndSupply(_user);
     239 | 
>>>  240 |         for (uint256 i = 0; i < length; i++) {
     241 |             accruedRewards[i] = _accrueRewards(_user, _programIds[i], totalStaked, userStaked);
     242 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `lib\AddressUtilsLib.sol:15`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      13 |         require(bytes(_hexString).length == 42, InvalidAddressString());
      14 | 
>>>   15 |         for (uint256 i = 2; i < 42; i++) {
      16 |             (bool success, uint8 value) = tryHexToUint(bytes(_hexString)[i]);
      17 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `lib\TokenHelper.sol:49`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      47 |         uint256 n = _data.length;
      48 | 
>>>   49 |         for (uint256 i; i < n; i++) {
      50 |             if (_data[i] == 0) continue;
      51 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `silo-router\SiloRouterV2.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      45 |         results = new bytes[](data.length);
      46 | 
>>>   47 |         for (uint256 i = 0; i < data.length; i++) {
      48 |             // expect implementation not to use `msg.value`
      49 |             results[i] = Address.functionDelegateCall(IMPLEMENTATION, data[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `utils\GlobalPause.sol:38`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      36 |         uint256 length = _contracts.length();
      37 | 
>>>   38 |         for (uint256 i = 0; i < length; i++) {
      39 |             _pause(_contracts.at(i));
      40 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `utils\GlobalPause.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      45 |         uint256 length = _contracts.length();
      46 | 
>>>   47 |         for (uint256 i = 0; i < length; i++) {
      48 |             _unpause(_contracts.at(i));
      49 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `utils\GlobalPause.sol:120`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     118 |         address[] memory signers = IGnosisSafeLike(owner()).getOwners();
     119 | 
>>>  120 |         for (uint256 i = 0; i < signers.length; i++) {
     121 |             if (signers[i] == _account) {
     122 |                 return true;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `utils\GlobalPause.sol:132`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     130 |         result = new ContractPauseStatus[](length);
     131 | 
>>>  132 |         for (uint256 i = 0; i < length; i++) {
     133 |             address contractAddress = _contracts.at(i);
     134 |             bool isPaused = IPausable(contractAddress).paused();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `utils\liquidationHelper\LiquidationHelper.sol:192`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     190 | 
     191 |     function _executeSwap(DexSwapInput[] memory _swapInputs) internal virtual {
>>>  192 |         for (uint256 i; i < _swapInputs.length; i++) {
     193 |             fillQuote({
     194 |                 _sellToken: _swapInputs[i].sellToken,
```
</details>

---

## Code Quality (1)

### [~] Address Is Contract Check

- **File:** `lib\SiloLensLib.sol:22`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      20 | 
      21 |     function getVersion(address _contract) internal view returns (string memory version) {
>>>   22 |         if (_contract.code.length == 0) return "Not a contract";
      23 | 
      24 |         try IVersioned(_contract).VERSION() returns (string memory v) {
```
</details>

---


---
*Generated by BugHunter*