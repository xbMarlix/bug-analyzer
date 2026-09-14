# BugHunter Report: contracts

**Generated:** 2026-09-04 23:26:04
**Project:** `C:\Users\123123\Desktop\angle\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 125 |
| Total lines | 19,372 |
| Bugs found | 238 |
| !!! Critical | 1 |
| !! High | 1 |
| ! Medium | 24 |
| ~ Low | 212 |

### Languages Detected

- **solidity**: 117 files
- **vyper**: 8 files

## Security (1)

### [!!!] tx.origin For Authorization

- **File:** `oracle\utils\ChainlinkUtilsWithKeeper.sol:72`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
      70 |                 updatedAt + pausingPeriod > block.timestamp &&
      71 |                 //solhint-disable-next-line
>>>   72 |                 !keeperRegistry.isTrusted(tx.origin)
      73 |             ) revert OraclePaused();
      74 |             if (ratio <= 0 || roundId > answeredInRound || block.timestamp - updatedAt > stalePeriod)
```
</details>

---

## Logic (24)

### [!!] block.number For Randomness

- **File:** `perpetualManager\PerpetualManagerFront.sol:422`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
     420 |         while (perpetualID != 0) {
     421 |             digits -= 1;
>>>  422 |             buffer[digits] = bytes1(uint8(48 + uint256(perpetualID % 10)));
     423 |             perpetualID /= 10;
     424 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `collateralSettler\CollateralSettlerERC20.sol:166`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     164 |     modifier onlyClaimPeriod() {
     165 |         require(
>>>  166 |             startTimestamp != 0 && block.timestamp < claimTime + startTimestamp && block.timestamp > startTimestamp,
     167 |             "57"
     168 |         );
```
</details>

---

### [!] Timestamp Dependence

- **File:** `collateralSettler\CollateralSettlerERC20.sol:345`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     343 |     function setAmountToRedistributeEach() external whenNotPaused {
     344 |         // Checking if it is the right time to call the function: claim period should be over
>>>  345 |         require(startTimestamp != 0 && block.timestamp > claimTime + startTimestamp, "63");
     346 |         // This is what guarantees that this function can only be computed once
     347 |         require(baseAmountToEachComputed == 0, "62");
```
</details>

---

### [!] Timestamp Dependence

- **File:** `dao\ANGLE.sol:52`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      50 |     function mint(address dst, uint256 amount) external {
      51 |         require(msg.sender == minter, "68");
>>>   52 |         require(block.timestamp >= mintingAllowedAfter, "69");
      53 |         require(amount <= (totalSupply() * MAX_MINT) / 100, "70");
      54 |         // Record the mint
```
</details>

---

### [!] Timestamp Dependence

- **File:** `genericLender\GenericAave.sol:335`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     333 |         uint256 cooldownSeconds = IStakedAave(stkAave).COOLDOWN_SECONDS();
     334 |         uint256 unstakeWindow = IStakedAave(stkAave).UNSTAKE_WINDOW();
>>>  335 |         if (block.timestamp >= cooldownStartTimestamp + cooldownSeconds) {
     336 |             return
     337 |                 block.timestamp - cooldownStartTimestamp + cooldownSeconds <= unstakeWindow ||
```
</details>

---

### [!] Timestamp Dependence

- **File:** `genericLender\GenericAave.sol:337`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     335 |         if (block.timestamp >= cooldownStartTimestamp + cooldownSeconds) {
     336 |             return
>>>  337 |                 block.timestamp - cooldownStartTimestamp + cooldownSeconds <= unstakeWindow ||
     338 |                 cooldownStartTimestamp == 0;
     339 |         } else {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `genericLender\GenericAave.sol:352`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     350 |         // it will fail if the isIncentivised is set to true but there is no incentives
     351 |         IAaveIncentivesController incentivesController = _incentivesController();
>>>  352 |         if (isIncentivised && block.timestamp < incentivesController.getDistributionEnd() && totalLiquidity > 0) {
     353 |             uint256 _emissionsPerSecond;
     354 |             (, _emissionsPerSecond, ) = _incentivesController().getAssetData(address(aToken));
```
</details>

---

### [!] Timestamp Dependence

- **File:** `oracle\utils\ChainlinkUtils.sol:41`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      39 |         if (castedRatio == 0) {
      40 |             (uint80 roundId, int256 ratio, , uint256 updatedAt, uint80 answeredInRound) = feed.latestRoundData();
>>>   41 |             if (ratio <= 0 || roundId > answeredInRound || block.timestamp - updatedAt > stalePeriod)
      42 |                 revert InvalidChainlinkRate();
      43 |             castedRatio = uint256(ratio);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `oracle\utils\ChainlinkUtilsWithKeeper.sol:74`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      72 |                 !keeperRegistry.isTrusted(tx.origin)
      73 |             ) revert OraclePaused();
>>>   74 |             if (ratio <= 0 || roundId > answeredInRound || block.timestamp - updatedAt > stalePeriod)
      75 |                 revert InvalidChainlinkRate();
      76 |             castedRatio = uint256(ratio);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `perpetualManager\PerpetualManager.sol:81`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      79 |         rewardPerTokenStored = _rewardPerToken();
      80 | 
>>>   81 |         if (block.timestamp >= periodFinish) {
      82 |             // If the period is not done, then the reward rate changes
      83 |             rewardRate = reward / rewardsDuration;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `perpetualManager\PerpetualManagerInternal.sol:208`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     206 |     /// @return Current timestamp if a reward is being distributed or the last timestamp
     207 |     function _lastTimeRewardApplicable() internal view returns (uint256) {
>>>  208 |         uint256 returnValue = block.timestamp < periodFinish ? block.timestamp : periodFinish;
     209 |         return returnValue;
     210 |     }
```
</details>

---

### [!] Balance Comparison

- **File:** `router\AngleRouter.sol:1316`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
    1314 |         bytes memory args
    1315 |     ) internal returns (uint256) {
>>> 1316 |         if (address(this).balance >= amount) {
    1317 |             if (address(inToken) == address(WETH9)) {
    1318 |                 WETH9.deposit{ value: amount }(); // wrap only what is needed to pay
```
</details>

---

### [!] Timestamp Dependence

- **File:** `stableMaster\StableMasterInternal.sol:50`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      48 |         // This is a way to prevent flash loans attacks when an important amount of fees are going to be distributed
      49 |         // in a block: fees are stored but will just be distributed to SLPs who will be here during next blocks
>>>   50 |         if (block.timestamp != col.slpData.lastBlockUpdated && _lockedInterests > 0) {
      51 |             uint256 sanMint = col.sanToken.totalSupply();
      52 |             if (sanMint != 0) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\AngleDistributor.sol:214`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     212 |     /// this function has been slightly modified from Curve implementation by Angle Team
     213 |     function _updateMiningParameters() internal {
>>>  214 |         // When entering this function, we always have: `(block.timestamp - startEpochTime) / RATE_REDUCTION_TIME >= 1`
     215 |         uint256 epochDelta = (block.timestamp - startEpochTime) / RATE_REDUCTION_TIME;
     216 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\AngleDistributor.sol:254`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     252 |         require(distributionsOn == true, "109");
     253 |         // Updating rate distribution parameters if need be
>>>  254 |         if (block.timestamp >= startEpochTime + RATE_REDUCTION_TIME) {
     255 |             _updateMiningParameters();
     256 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\AngleDistributor.sol:269`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     267 |         require(distributionsOn == true, "109");
     268 |         // Updating rate distribution parameters if need be
>>>  269 |         if (block.timestamp >= startEpochTime + RATE_REDUCTION_TIME) {
     270 |             _updateMiningParameters();
     271 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\AngleDistributor.sol:280`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     278 |     /// @dev Callable by any address, but only once per epoch
     279 |     function updateMiningParameters() external {
>>>  280 |         require(block.timestamp >= startEpochTime + RATE_REDUCTION_TIME, "108");
     281 |         _updateMiningParameters();
     282 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\RewardsDistributor.sol:201`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     199 |     ) external override onlyRole(GOVERNOR_ROLE) {
     200 |         require(_duration > 0, "85");
>>>  201 |         require(_duration >= _updateFrequency && block.timestamp >= _updateFrequency, "86");
     202 | 
     203 |         IStakingRewards stakingContract = IStakingRewards(_stakingContract);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\RewardsDistributor.sol:292`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     290 |     /// @return If the `updateFrequency` has passed since the last drip
     291 |     function _isDripAvailable(StakingParameters memory stakingParams) internal view returns (bool) {
>>>  292 |         return block.timestamp >= _nextDripAvailable(stakingParams);
     293 |     }
     294 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `staking\StakingRewards.sol:237`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     235 |         updateReward(address(0))
     236 |     {
>>>  237 |         if (block.timestamp >= periodFinish) {
     238 |             // If no reward is currently being distributed, the new rate is just `reward / duration`
     239 |             rewardRate = reward / rewardsDuration;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `strategies\BaseStrategy.sol:151`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     149 |             uint256 lastReport = poolManager.strategies(address(this)).lastReport;
     150 |             if (
>>>  151 |                 (block.timestamp - lastReport >= minReportDelay) && // Should not trigger if we haven't waited long enough since previous harvest
     152 |                 ((block.timestamp - lastReport >= maxReportDelay) || // If hasn't been called in a while
     153 |                     (debtPayment > debtThreshold) || // If the debt was too high
```
</details>

---

### [!] Timestamp Dependence

- **File:** `strategies\BaseStrategy.sol:152`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     150 |             if (
     151 |                 (block.timestamp - lastReport >= minReportDelay) && // Should not trigger if we haven't waited long enough since previous harvest
>>>  152 |                 ((block.timestamp - lastReport >= maxReportDelay) || // If hasn't been called in a while
     153 |                     (debtPayment > debtThreshold) || // If the debt was too high
     154 |                     (loss > 0) || // If some loss occured
```
</details>

---

### [!] Timestamp Dependence

- **File:** `strategies\BaseStrategy.sol:233`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     231 | 
     232 |         // Should not trigger if we haven't waited long enough since previous harvest
>>>  233 |         if (block.timestamp - params.lastReport < minReportDelay) return false;
     234 | 
     235 |         // Should trigger if hasn't been called in a while
```
</details>

---

### [!] Timestamp Dependence

- **File:** `strategies\BaseStrategy.sol:236`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     234 | 
     235 |         // Should trigger if hasn't been called in a while
>>>  236 |         if (block.timestamp - params.lastReport >= maxReportDelay) return true;
     237 | 
     238 |         // If some amount is owed, pay it back
```
</details>

---

## Resource Management (1)

### [!] Fixed-Gas Transfer

- **File:** `collateralSettler\CollateralSettlerERC20.sol:422`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     420 |         }
     421 |         if (amountGovTokens > 0) {
>>>  422 |             angle.transfer(user, amountGovTokens);
     423 |         }
     424 |     }
```
</details>

---

## Performance (84)

### [~] Unoptimized Loop

- **File:** `collateralSettler\CollateralSettlerERC20.sol:210`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     208 | 
     209 |         // Access control
>>>  210 |         for (uint256 i = 0; i < governorList.length; i++) {
     211 |             require(governorList[i] != address(0), "0");
     212 |             _setupRole(GOVERNOR_ROLE, governorList[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      93 |         );
      94 |         uint256 indexMet;
>>>   95 |         for (uint256 i = 0; i < governorListLength; i++) {
      96 |             if (!governorMap[_newCoreGovernorList[i]]) {
      97 |                 indexMet = 1;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:101`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      99 |             }
     100 |         }
>>>  101 |         for (uint256 i = 0; i < stablecoinListLength; i++) {
     102 |             // The stablecoin lists should preserve exactly the same order of elements
     103 |             if (_stablecoinList[i] != _newStablecoinList[i]) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:111`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     109 |         require(indexMet == 0, "43");
     110 |         // Propagates the change
>>>  111 |         for (uint256 i = 0; i < stablecoinListLength; i++) {
     112 |             IStableMaster(_stablecoinList[i]).setCore(address(newCore));
     113 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:152`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     150 |         require(stablecoinListLength >= 1, "45");
     151 |         uint256 indexMet;
>>>  152 |         for (uint256 i = 0; i < stablecoinListLength - 1; i++) {
     153 |             if (_stablecoinList[i] == stableMaster) {
     154 |                 indexMet = 1;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:181`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     179 |         // Propagates the changes to maintain consistency across all the contracts that are attached to this
     180 |         // `Core` contract
>>>  181 |         for (uint256 i = 0; i < _stablecoinList.length; i++) {
     182 |             // Since a zero address check has already been performed in this contract, there is no need
     183 |             // to repeat this check in underlying contracts
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:200`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     198 |         // We still need to check if the address provided was well in the list
     199 |         uint256 indexMet;
>>>  200 |         for (uint256 i = 0; i < governorListLength - 1; i++) {
     201 |             if (_governorList[i] == _governor) {
     202 |                 indexMet = 1;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:212`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     210 |         delete governorMap[_governor];
     211 |         // Maintaining consistency across all contracts
>>>  212 |         for (uint256 i = 0; i < _stablecoinList.length; i++) {
     213 |             // We have checked in this contract that the mentionned `_governor` here was well a governor
     214 |             // There is no need to check this in the underlying contracts where this is going to be updated
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:233`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     231 |         address oldGuardian = guardian;
     232 |         guardian = _newGuardian;
>>>  233 |         for (uint256 i = 0; i < _stablecoinList.length; i++) {
     234 |             IStableMaster(_stablecoinList[i]).setGuardian(_newGuardian, oldGuardian);
     235 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `core\Core.sol:245`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     243 |         address oldGuardian = guardian;
     244 |         guardian = address(0);
>>>  245 |         for (uint256 i = 0; i < _stablecoinList.length; i++) {
     246 |             IStableMaster(_stablecoinList[i]).revokeGuardian(oldGuardian);
     247 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `deprecated\bondingCurve\BondingCurve.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      82 |         require(guardian != address(0) && address(_soldToken) != address(0), "0");
      83 |         // Access control
>>>   84 |         for (uint256 i = 0; i < governorList.length; i++) {
      85 |             require(governorList[i] != address(0), "0");
      86 |             _setupRole(GOVERNOR_ROLE, governorList[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `feeManager\FeeManager.sol:49`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      47 |         address _perpetualManager
      48 |     ) external override onlyRole(POOLMANAGER_ROLE) initializer {
>>>   49 |         for (uint256 i = 0; i < governorList.length; i++) {
      50 |             _grantRole(GUARDIAN_ROLE, governorList[i]);
      51 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `feeManager\FeeManager.sol:119`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     117 |     ) external override onlyRole(GUARDIAN_ROLE) {
     118 |         require(xArray.length == yArray.length && yArray.length > 0, "5");
>>>  119 |         for (uint256 i = 0; i <= yArray.length - 1; i++) {
     120 |             if (i > 0) {
     121 |                 require(xArray[i] > xArray[i - 1], "7");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `feeManager\FeeManager.sol:168`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     166 |         // of the two arrays is zero
     167 |         if (xSlippage.length >= 1 && xSlippageFee.length >= 1) {
>>>  168 |             for (uint256 i = 0; i <= ySlippageFee.length - 1; i++) {
     169 |                 if (ySlippageFee[i] > 0) {
     170 |                     require(ySlippageFee[i] <= BASE_PARAMS_CASTED, "37");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `genericLender\GenericLenderBase.sol:56`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      54 | 
      55 |         _setupRole(GUARDIAN_ROLE, address(poolManager));
>>>   56 |         for (uint256 i = 0; i < governorList.length; i++) {
      57 |             _setupRole(GUARDIAN_ROLE, governorList[i]);
      58 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `genericLender\GenericLenderBase.sol:103`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     101 |     function sweep(address _token, address to) external override onlyRole(GUARDIAN_ROLE) {
     102 |         address[] memory __protectedTokens = _protectedTokens();
>>>  103 |         for (uint256 i = 0; i < __protectedTokens.length; i++) require(_token != __protectedTokens[i], "93");
     104 | 
     105 |         IERC20(_token).safeTransfer(to, IERC20(_token).balanceOf(address(this)));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\OracleChainlinkMultiEfficient.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      28 |         stalePeriod = _stalePeriod;
      29 |         if (guardians.length == 0) revert InvalidLength();
>>>   30 |         for (uint256 i = 0; i < guardians.length; i++) {
      31 |             if (guardians[i] == address(0)) revert ZeroAddress();
      32 |             _setupRole(GUARDIAN_ROLE_CHAINLINK, guardians[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\OracleChainlinkMultiEfficient.sol:83`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      81 |         uint8[2] memory circuitChainIsMultiplied = _circuitChainIsMultiplied();
      82 |         uint8[2] memory chainlinkDecimals = _chainlinkDecimals();
>>>   83 |         for (uint256 i = 0; i < circuitChainlink.length; i++) {
      84 |             (quoteAmount, ) = _readChainlinkFeed(
      85 |                 quoteAmount,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\OracleChainlinkMultiEfficientWithKeeper.sol:90`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      88 |         uint8[2] memory circuitChainIsMultiplied = _circuitChainIsMultiplied();
      89 |         uint8[2] memory chainlinkDecimals = _chainlinkDecimals();
>>>   90 |         for (uint256 i = 0; i < circuitChainlink.length; i++) {
      91 |             (quoteAmount, ) = _readChainlinkFeed(
      92 |                 quoteAmount,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleChainlinkMulti.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      33 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
      34 |         require(guardians.length > 0, "101");
>>>   35 |         for (uint256 i = 0; i < guardians.length; i++) {
      36 |             require(guardians[i] != address(0), "0");
      37 |             _setupRole(GUARDIAN_ROLE_CHAINLINK, guardians[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleChainlinkMulti.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      39 |         _setRoleAdmin(GUARDIAN_ROLE_CHAINLINK, GUARDIAN_ROLE_CHAINLINK);
      40 | 
>>>   41 |         for (uint256 i = 0; i < circuitLength; i++) {
      42 |             AggregatorV3Interface _pool = AggregatorV3Interface(_circuitChainlink[i]);
      43 |             circuitChainlink.push(_pool);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleChainlinkMulti.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      57 |         uint256 castedRatio;
      58 |         // An invariant should be that `circuitChainlink.length > 0` otherwise `castedRatio = 0`
>>>   59 |         for (uint256 i = 0; i < circuitChainlink.length; i++) {
      60 |             (quoteAmount, castedRatio) = _readChainlinkFeed(
      61 |                 quoteAmount,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleChainlinkMultiWithKeeper.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      45 |         ) revert InvalidLength();
      46 | 
>>>   47 |         for (uint256 i = 0; i < circuitLength; i++) {
      48 |             AggregatorV3Interface _pool = AggregatorV3Interface(_circuitChainlink[i]);
      49 |             circuitChainlink.push(_pool);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleChainlinkMultiWithKeeper.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      67 |         uint256 castedRatio;
      68 |         // An invariant should be that `circuitChainlink.length > 0` otherwise `castedRatio = 0`
>>>   69 |         for (uint256 i = 0; i < circuitChainlink.length; i++) {
      70 |             (quoteAmount, castedRatio) = _readChainlinkFeed(
      71 |                 quoteAmount,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleChainlinkSingle.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      32 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
      33 |         require(guardians.length > 0, "101");
>>>   34 |         for (uint256 i = 0; i < guardians.length; i++) {
      35 |             require(guardians[i] != address(0), "0");
      36 |             _setupRole(GUARDIAN_ROLE_CHAINLINK, guardians[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMulti.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      31 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
      32 |         require(guardians.length > 0, "101");
>>>   33 |         for (uint256 i = 0; i < guardians.length; i++) {
      34 |             require(guardians[i] != address(0), "0");
      35 |             _setupRole(GUARDIAN_ROLE_UNISWAP, guardians[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMulti.sol:49`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      47 |         circuitUniIsMultiplied = _circuitUniIsMultiplied;
      48 | 
>>>   49 |         for (uint256 i = 0; i < circuitUniLength; i++) {
      50 |             circuitUniswap[i].increaseObservationCardinalityNext(observationLength);
      51 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMulti.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      57 |     /// the end currency
      58 |     function _quoteUniswap(uint256 quoteAmount) internal view returns (uint256) {
>>>   59 |         for (uint256 i = 0; i < circuitUniswap.length; i++) {
      60 |             quoteAmount = _readUniswapPool(quoteAmount, circuitUniswap[i], circuitUniIsMultiplied[i]);
      61 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMulti.sol:70`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      68 |     /// @dev newLengthStored should be larger than all previous pools observations length
      69 |     function increaseTWAPStore(uint16 newLengthStored) external {
>>>   70 |         for (uint256 i = 0; i < circuitUniswap.length; i++) {
      71 |             circuitUniswap[i].increaseObservationCardinalityNext(newLengthStored);
      72 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMultiWithKeeper.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      39 |         circuitUniIsMultiplied = _circuitUniIsMultiplied;
      40 | 
>>>   41 |         for (uint256 i = 0; i < circuitUniLength; i++) {
      42 |             circuitUniswap[i].increaseObservationCardinalityNext(observationLength);
      43 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMultiWithKeeper.sol:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      49 |     /// the end currency
      50 |     function _quoteUniswap(uint256 quoteAmount) internal view returns (uint256) {
>>>   51 |         for (uint256 i = 0; i < circuitUniswap.length; i++) {
      52 |             quoteAmount = _readUniswapPool(quoteAmount, circuitUniswap[i], circuitUniIsMultiplied[i]);
      53 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `oracle\modules\ModuleUniswapMultiWithKeeper.sol:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      60 |     /// @dev newLengthStored should be larger than all previous pools observations length
      61 |     function increaseTWAPStore(uint16 newLengthStored) external {
>>>   62 |         for (uint256 i = 0; i < circuitUniswap.length; i++) {
      63 |             circuitUniswap[i].increaseObservationCardinalityNext(newLengthStored);
      64 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `perpetualManager\PerpetualManager.sol:62`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      60 |         IOracle oracle_
      61 |     ) external override onlyRole(POOLMANAGER_ROLE) {
>>>   62 |         for (uint256 i = 0; i < governorList.length; i++) {
      63 |             _grantRole(GUARDIAN_ROLE, governorList[i]);
      64 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `perpetualManager\PerpetualManagerFront.sol:245`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     243 |         (uint256 rateDown, ) = _getOraclePrice();
     244 |         uint256 liquidationFees;
>>>  245 |         for (uint256 i = 0; i < perpetualIDs.length; i++) {
     246 |             uint256 perpetualID = perpetualIDs[i];
     247 |             if (_exists(perpetualID)) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `perpetualManager\PerpetualManagerFront.sol:289`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     287 |         Pairs[] memory outputPairs = new Pairs[](perpetualIDs.length);
     288 | 
>>>  289 |         for (uint256 i = 0; i < perpetualIDs.length; i++) {
     290 |             uint256 perpetualID = perpetualIDs[i];
     291 |             address owner = _owners[perpetualID];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `poolManager\PoolManager.sol:70`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      68 | 
      69 |         // Access control
>>>   70 |         for (uint256 i = 0; i < governorList.length; i++) {
      71 |             _grantRole(GOVERNOR_ROLE, governorList[i]);
      72 |             _grantRole(GUARDIAN_ROLE, governorList[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `poolManager\PoolManager.sol:146`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     144 |         if (supply == 0) return type(uint256).max;
     145 | 
>>>  146 |         for (uint256 i = 0; i < strategyList.length; i++) {
     147 |             apr =
     148 |                 apr +
```
</details>

---

### [~] Unoptimized Loop

- **File:** `poolManager\PoolManager.sol:411`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     409 |         require(params.lastReport != 0 && strategyListLength >= 1, "78");
     410 |         // It has already been checked whether the strategy was a valid strategy
>>>  411 |         for (uint256 i = 0; i < strategyListLength - 1; i++) {
     412 |             if (strategyList[i] == strategy) {
     413 |                 strategyList[i] = strategyList[strategyListLength - 1];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `poolManager\PoolManagerInternal.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      39 |         feeManager.grantRole(GUARDIAN_ROLE, _guardian);
      40 |         uint256 strategyListLength = strategyList.length;
>>>   41 |         for (uint256 i = 0; i < strategyListLength; i++) {
      42 |             IStrategy(strategyList[i]).addGuardian(_guardian);
      43 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `poolManager\PoolManagerInternal.sol:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      51 |         feeManager.revokeRole(GUARDIAN_ROLE, guardian);
      52 |         uint256 strategyListLength = strategyList.length;
>>>   53 |         for (uint256 i = 0; i < strategyListLength; i++) {
      54 |             IStrategy(strategyList[i]).revokeGuardian(guardian);
      55 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:238`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     236 |         if (poolManagers.length != stablecoins.length || liquidityGauges.length != stablecoins.length)
     237 |             revert IncompatibleLengths();
>>>  238 |         for (uint256 i = 0; i < stablecoins.length; i++) {
     239 |             IStableMasterFront stableMaster = mapStableMasters[stablecoins[i]];
     240 |             _addPair(stableMaster, poolManagers[i], liquidityGauges[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:260`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     258 |         Pairs memory pairs;
     259 |         IStableMasterFront stableMaster;
>>>  260 |         for (uint256 i = 0; i < stablecoins.length; i++) {
     261 |             if (address(stableMasters[i]) == address(0))
     262 |                 // In this case `collaterals[i]` is a collateral address
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:290`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     288 |         if (collaterals.length != stablecoins.length || newLiquidityGauges.length != stablecoins.length)
     289 |             revert IncompatibleLengths();
>>>  290 |         for (uint256 i = 0; i < stablecoins.length; i++) {
     291 |             IStableMasterFront stableMaster = mapStableMasters[stablecoins[i]];
     292 |             Pairs storage pairs = mapPoolManagers[stableMaster][collaterals[i]];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:321`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     319 |     ) external onlyGovernorOrGuardian {
     320 |         if (tokens.length != spenders.length || tokens.length != amounts.length) revert IncompatibleLengths();
>>>  321 |         for (uint256 i = 0; i < tokens.length; i++) {
     322 |             _changeAllowance(tokens[i], spenders[i], amounts[i]);
     323 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:445`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     443 |     ) public payable {
     444 |         // Do all the permits once for all: if all tokens have already been approved, there's no need for this step
>>>  445 |         for (uint256 i = 0; i < paramsPermit.length; i++) {
     446 |             IERC20PermitUpgradeable(paramsPermit[i].token).permit(
     447 |                 paramsPermit[i].owner,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:462`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     460 |         uint256[_MAX_TOKENS] memory balanceTokens;
     461 | 
>>>  462 |         for (uint256 i = 0; i < paramsTransfer.length; i++) {
     463 |             paramsTransfer[i].inToken.safeTransferFrom(msg.sender, address(this), paramsTransfer[i].amountIn);
     464 |             _addToList(listTokens, balanceTokens, address(paramsTransfer[i].inToken), paramsTransfer[i].amountIn);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:467`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     465 |         }
     466 | 
>>>  467 |         for (uint256 i = 0; i < paramsSwap.length; i++) {
     468 |             // Caution here: if the args are not set such that end token is the params `paramsSwap[i].collateral`,
     469 |             // then the funds will be lost, and any user could take advantage of it to fetch the funds
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:481`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     479 | 
     480 |         // Performing actions one after the others
>>>  481 |         for (uint256 i = 0; i < actions.length; i++) {
     482 |             if (actions[i] == ActionType.claimRewards) {
     483 |                 (
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:710`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     708 |         // If a user sends funds (through a swap) but specifies incorrectly the collateral associated to it, then
     709 |         //  the mixer will revert when trying to send the remaining funds back
>>>  710 |         for (uint256 i = 0; i < balanceTokens.length; i++) {
     711 |             if (balanceTokens[i] > 0) IERC20(listTokens[i]).safeTransfer(msg.sender, balanceTokens[i]);
     712 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:731`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     729 |         bytes[] calldata data
     730 |     ) external payable {
>>>  731 |         for (uint256 i = 0; i < paramsPermitVaultManager.length; i++) {
     732 |             if (paramsPermitVaultManager[i].approved) {
     733 |                 IVaultManagerFunctions(paramsPermitVaultManager[i].vaultManager).permit(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:747`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     745 |         // Storing the index at which starting the iteration for revoking approvals in a variable would make the stack
     746 |         // too deep
>>>  747 |         for (uint256 i = 0; i < paramsPermitVaultManager.length; i++) {
     748 |             if (!paramsPermitVaultManager[i].approved) {
     749 |                 IVaultManagerFunctions(paramsPermitVaultManager[i].vaultManager).permit(
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:791`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     789 |             revert IncompatibleLengths();
     790 | 
>>>  791 |         for (uint256 i = 0; i < liquidityGauges.length; i++) {
     792 |             ILiquidityGauge(liquidityGauges[i]).claim_rewards(gaugeUser);
     793 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:795`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     793 |         }
     794 | 
>>>  795 |         for (uint256 i = 0; i < perpetualIDs.length; i++) {
     796 |             IPerpetualManagerFrontWithClaim perpManager;
     797 |             if (addressProcessed) perpManager = IPerpetualManagerFrontWithClaim(collateralsOrPerpetualManagers[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:1103`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    1101 |         uint256 lastVaultID;
    1102 |         uint256 vaultIDLength;
>>> 1103 |         for (uint256 i = 0; i < actionsBorrow.length; i++) {
    1104 |             uint256 vaultID;
    1105 |             // If there is a createVault action, the router should not worry about looking at
```
</details>

---

### [~] Unoptimized Loop

- **File:** `router\AngleRouter.sol:1447`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
    1445 |         ANGLE.safeApprove(address(VEANGLE), type(uint256).max);
    1446 | 
>>> 1447 |         for (uint256 i = 0; i < existingPoolManagers.length; i++) {
    1448 |             _addPair(existingStableMaster, existingPoolManagers[i], existingLiquidityGauges[i]);
    1449 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:40`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      38 |         address _agToken
      39 |     ) external override onlyRole(CORE_ROLE) {
>>>   40 |         for (uint256 i = 0; i < governorList.length; i++) {
      41 |             _grantRole(GOVERNOR_ROLE, governorList[i]);
      42 |             _grantRole(GUARDIAN_ROLE, governorList[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:151`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     149 |         uint256 val;
     150 |         uint256 mints;
>>>  151 |         for (uint256 i = 0; i < _managerList.length; i++) {
     152 |             mints += collateralMap[_managerList[i]].stocksUsers;
     153 |             // Oracle needs to be called for each collateral to compute the collateral ratio
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:231`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     229 |         _grantRole(GUARDIAN_ROLE, governor);
     230 | 
>>>  231 |         for (uint256 i = 0; i < _managerList.length; i++) {
     232 |             // The `PoolManager` will echo the changes across all the corresponding contracts
     233 |             _managerList[i].addGovernor(governor);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:248`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     246 |         _revokeRole(GUARDIAN_ROLE, governor);
     247 | 
>>>  248 |         for (uint256 i = 0; i < _managerList.length; i++) {
     249 |             // The `PoolManager` will echo the changes across all the corresponding contracts
     250 |             _managerList[i].removeGovernor(governor);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:264`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     262 |         _grantRole(GUARDIAN_ROLE, newGuardian);
     263 | 
>>>  264 |         for (uint256 i = 0; i < _managerList.length; i++) {
     265 |             _managerList[i].setGuardian(newGuardian, oldGuardian);
     266 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:274`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     272 |     function revokeGuardian(address oldGuardian) external override onlyRole(CORE_ROLE) {
     273 |         _revokeRole(GUARDIAN_ROLE, oldGuardian);
>>>  274 |         for (uint256 i = 0; i < _managerList.length; i++) {
     275 |             _managerList[i].revokeGuardian(oldGuardian);
     276 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `stableMaster\StableMaster.sol:368`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     366 |         uint256 managerListLength = _managerList.length;
     367 |         require(managerListLength >= 1, "10");
>>>  368 |         for (uint256 i = 0; i < managerListLength - 1; i++) {
     369 |             if (_managerList[i] == poolManager) {
     370 |                 indexMet = 1;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `staking\AngleDistributor.sol:155`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     153 |         // We use this variable to keep track of the emission rate across different weeks
     154 |         uint256 weeklyRate = rate;
>>>  155 |         for (uint256 i = 0; i < weeksElapsed; i++) {
     156 |             uint256 relWeightAtWeek;
     157 |             if (i == 0) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `staking\AngleDistributor.sol:224`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     222 |         miningEpoch += epochDelta;
     223 | 
>>>  224 |         for (uint256 i = 0; i < epochDelta; i++) {
     225 |             // Updating the intermediate values of the `startEpochSupply`
     226 |             _startEpochSupply += _rate * RATE_REDUCTION_TIME;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `staking\AngleDistributor.sol:272`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     270 |             _updateMiningParameters();
     271 |         }
>>>  272 |         for (uint256 i = 0; i < gauges.length; i++) {
     273 |             _distributeReward(gauges[i]);
     274 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `staking\RewardsDistributor.sol:72`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      70 |         _setRoleAdmin(GOVERNOR_ROLE, GOVERNOR_ROLE);
      71 |         _setRoleAdmin(GUARDIAN_ROLE, GOVERNOR_ROLE);
>>>   72 |         for (uint256 i = 0; i < governorList.length; i++) {
      73 |             require(governorList[i] != address(0), "0");
      74 |             _setupRole(GOVERNOR_ROLE, governorList[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `staking\RewardsDistributor.sol:150`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     148 |         require(address(IRewardsDistributor(newRewardsDistributor).rewardToken()) == address(rewardToken), "83");
     149 |         require(newRewardsDistributor != address(this), "84");
>>>  150 |         for (uint256 i = 0; i < stakingContractsList.length; i++) {
     151 |             stakingContractsList[i].setNewRewardsDistribution(newRewardsDistributor);
     152 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `staking\RewardsDistributor.sol:167`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     165 |         uint256 stakingContractsListLength = stakingContractsList.length;
     166 |         require(stakingContractsListLength >= 1, "80");
>>>  167 |         for (uint256 i = 0; i < stakingContractsListLength - 1; i++) {
     168 |             if (stakingContractsList[i] == stakingContract) {
     169 |                 indexMet = 1;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\BaseStrategy.sol:98`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      96 |         // `PoolManager` is guardian as well to allow for more flexibility
      97 |         _setupRole(POOLMANAGER_ROLE, address(_poolManager));
>>>   98 |         for (uint256 i = 0; i < governorList.length; i++) {
      99 |             require(governorList[i] != address(0), "0");
     100 |             _setupRole(GUARDIAN_ROLE, governorList[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\BaseStrategy.sol:427`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     425 | 
     426 |         address[] memory __protectedTokens = _protectedTokens();
>>>  427 |         for (uint256 i = 0; i < __protectedTokens.length; i++)
     428 |             // In the strategy we use so far, the only protectedToken is the want token
     429 |             // and this has been checked above
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:156`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     154 |         _highest = 0;
     155 | 
>>>  156 |         for (uint256 i = 0; i < lendersList.length; i++) {
     157 |             uint256 aprAfterDeposit = lendersList[i].aprAfterDeposit(looseAssets);
     158 |             if (aprAfterDeposit > highestApr) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:226`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     224 |             uint256 lowestApr = type(uint256).max;
     225 |             uint256 lowest = 0;
>>>  226 |             for (uint256 i = 0; i < lendersList.length; i++) {
     227 |                 if (lendersList[i].hasAssets()) {
     228 |                     uint256 apr = lendersList[i].apr();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:292`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     290 |         uint256 lendersListLength = lenders.length;
     291 |         LendStatus[] memory statuses = new LendStatus[](lendersListLength);
>>>  292 |         for (uint256 i = 0; i < lendersListLength; i++) {
     293 |             LendStatus memory s;
     294 |             s.name = lenders[i].lenderName();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:306`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     304 |     function lentTotalAssets() public view returns (uint256) {
     305 |         uint256 nav = 0;
>>>  306 |         for (uint256 i = 0; i < lenders.length; i++) {
     307 |             nav = nav + lenders[i].nav();
     308 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:331`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     329 |         uint256 weightedAPR = 0;
     330 | 
>>>  331 |         for (uint256 i = 0; i < lenders.length; i++) {
     332 |             weightedAPR = weightedAPR + lenders[i].weightedApr();
     333 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:360`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     358 |         IGenericLender[] memory lendersList = lenders;
     359 |         uint256 share = 0;
>>>  360 |         for (uint256 i = 0; i < lendersList.length; i++) {
     361 |             lendersList[i].withdrawAll();
     362 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:366`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     364 |         uint256 assets = want.balanceOf(address(this));
     365 | 
>>>  366 |         for (uint256 i = 0; i < _newPositions.length; i++) {
     367 |             bool found = false;
     368 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:399`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     397 |         require(newLender.strategy() == address(this), "96");
     398 | 
>>>  399 |         for (uint256 i = 0; i < lenders.length; i++) {
     400 |             require(address(newLender) != address(lenders[i]), "97");
     401 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:424`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     422 |     function _removeLender(address lender, bool force) internal {
     423 |         IGenericLender[] memory lendersList = lenders;
>>>  424 |         for (uint256 i = 0; i < lendersList.length; i++) {
     425 |             if (lender == address(lendersList[i])) {
     426 |                 bool allWithdrawn = lendersList[i].withdrawAll();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:466`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     464 |         _grantRole(GUARDIAN_ROLE, _guardian);
     465 |         // Propagating the new role in other contract
>>>  466 |         for (uint256 i = 0; i < lenders.length; i++) {
     467 |             lenders[i].grantRole(GUARDIAN_ROLE, _guardian);
     468 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `strategies\Strategy.sol:475`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     473 |     function revokeGuardian(address guardian) external override onlyRole(POOLMANAGER_ROLE) {
     474 |         _revokeRole(GUARDIAN_ROLE, guardian);
>>>  475 |         for (uint256 i = 0; i < lenders.length; i++) {
     476 |             lenders[i].revokeRole(GUARDIAN_ROLE, guardian);
     477 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `surplus\BaseSurplusConverter.sol:60`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      58 |         IERC20(_rewardToken).safeApprove(_feeDistributor, type(uint256).max);
      59 |         require(guardians.length > 0, "101");
>>>   60 |         for (uint256 i = 0; i < guardians.length; i++) {
      61 |             require(guardians[i] != address(0), "0");
      62 |             _setupRole(GUARDIAN_ROLE, guardians[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `surplus\SurplusConverterUniV3.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      59 | 
      60 |         bytes memory path;
>>>   61 |         for (uint256 i = 0; i < pathFees.length; i++) {
      62 |             require(pathAddresses[i] != address(0) && pathAddresses[i + 1] != address(0), "0");
      63 |             path = abi.encodePacked(path, pathAddresses[i], pathFees[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `utils\FunctionUtils.sol:73`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      71 |     modifier onlyCompatibleInputArrays(uint64[] memory xArray, uint64[] memory yArray) {
      72 |         require(xArray.length == yArray.length && xArray.length > 0, "5");
>>>   73 |         for (uint256 i = 0; i <= yArray.length - 1; i++) {
      74 |             require(yArray[i] <= uint64(BASE_PARAMS) && xArray[i] <= uint64(BASE_PARAMS), "6");
      75 |             if (i > 0) {
```
</details>

---

## Code Quality (128)

### [~] UNCLEAR require Error Message

- **File:** `agToken\AgToken.sol:46`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      44 |     /// @dev There is no Access Control here, because it can be handled cheaply through this modifier
      45 |     modifier onlyStableMaster() {
>>>   46 |         require(msg.sender == stableMaster, "1");
      47 |         _;
      48 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `agToken\AgToken.sol:125`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     123 |     ) internal {
     124 |         uint256 currentAllowance = allowance(burner, sender);
>>>  125 |         require(currentAllowance >= amount, "23");
     126 |         _approve(burner, sender, currentAllowance - amount);
     127 |         _burn(burner, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:177`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     175 |     /// allows at the same time to check if claim period is over
     176 |     modifier onlyBaseAmountsComputed() {
>>>  177 |         require(baseAmountToEachComputed != 0, "58");
     178 |         _;
     179 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:244`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     242 |         uint256 _stocksUsers
     243 |     ) external override onlyRole(STABLEMASTER_ROLE) {
>>>  244 |         require(startTimestamp == 0, "59");
     245 |         require(proportionalRatioGovLP != 0 && proportionalRatioGovUser != 0, "60");
     246 |         oracleValueHA = _oracleValue;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:245`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     243 |     ) external override onlyRole(STABLEMASTER_ROLE) {
     244 |         require(startTimestamp == 0, "59");
>>>  245 |         require(proportionalRatioGovLP != 0 && proportionalRatioGovUser != 0, "60");
     246 |         oracleValueHA = _oracleValue;
     247 |         sanRate = _sanRate;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:267`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     265 |     ) external onlyClaimPeriod whenNotPaused {
     266 |         require(dest != address(0), "0");
>>>  267 |         require(totalUserClaimsWithGov + totalUserClaims + amountAgToken <= maxStablecoinsClaimable, "61");
     268 |         // Since this involves a `transferFrom`, it is normal to update the variables after the transfers are done
     269 |         // No need to use `safeTransfer` for agTokens and ANGLE tokens
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:303`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     301 |         // The zero address cannot own a perpetual
     302 |         address dest = perpetualManager.ownerOf(perpetualID);
>>>  303 |         require(haClaimCheck[perpetualID] == 0, "64");
     304 |         // A HA cannot claim a given perpetual twice
     305 |         haClaimCheck[perpetualID] = 1;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:345`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     343 |     function setAmountToRedistributeEach() external whenNotPaused {
     344 |         // Checking if it is the right time to call the function: claim period should be over
>>>  345 |         require(startTimestamp != 0 && block.timestamp > claimTime + startTimestamp, "63");
     346 |         // This is what guarantees that this function can only be computed once
     347 |         require(baseAmountToEachComputed == 0, "62");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:347`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     345 |         require(startTimestamp != 0 && block.timestamp > claimTime + startTimestamp, "63");
     346 |         // This is what guarantees that this function can only be computed once
>>>  347 |         require(baseAmountToEachComputed == 0, "62");
     348 |         baseAmountToEachComputed = 1;
     349 |         // Fetching the oracle value at which stablecoins will be converted to collateral
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:452`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     450 |     ) external onlyRole(GOVERNOR_ROLE) onlyBaseAmountsComputed {
     451 |         if (tokenAddress == address(underlyingToken)) {
>>>  452 |             require(amountToRedistribute >= amountToRecover, "66");
     453 |             amountToRedistribute -= amountToRecover;
     454 |             underlyingToken.safeTransfer(to, amountToRecover);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `collateralSettler\CollateralSettlerERC20.sol:471`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     469 |         onlyRole(GOVERNOR_ROLE)
     470 |     {
>>>  471 |         require(startTimestamp == 0, "65");
     472 |         proportionalRatioGovUser = _proportionalRatioGovUser;
     473 |         proportionalRatioGovLP = _proportionalRatioGovLP;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:36`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      34 |     /// sure that governors cannot bypass the `addGovernor` or `revokeGovernor` functions
      35 |     modifier onlyGovernor() {
>>>   36 |         require(governorMap[msg.sender], "1");
      37 |         _;
      38 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:44`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      42 |     /// cannot bypass the functions defined on purpose in this contract
      43 |     modifier onlyGuardian() {
>>>   44 |         require(governorMap[msg.sender] || msg.sender == guardian, "1");
      45 |         _;
      46 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:63`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      61 |         // Creating references
      62 |         require(_guardian != address(0) && _governor != address(0), "0");
>>>   63 |         require(_guardian != _governor, "39");
      64 |         _governorList.push(_governor);
      65 |         guardian = _guardian;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 |         }
     108 |         // Only performing one require, hence making it cheaper for a governance with a correct initialization
>>>  109 |         require(indexMet == 0, "43");
     110 |         // Propagates the change
     111 |         for (uint256 i = 0; i < stablecoinListLength; i++) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:128`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     126 |         address stableMaster = IAgToken(agToken).stableMaster();
     127 |         // Checking if `stableMaster` has not already been deployed
>>>  128 |         require(!deployedStableMasterMap[stableMaster], "44");
     129 | 
     130 |         // Storing and initializing information about the stablecoin
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:150`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     148 |         uint256 stablecoinListLength = _stablecoinList.length;
     149 |         // Checking if `stableMaster` is correct and removing the stablecoin from the `_stablecoinList`
>>>  150 |         require(stablecoinListLength >= 1, "45");
     151 |         uint256 indexMet;
     152 |         for (uint256 i = 0; i < stablecoinListLength - 1; i++) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:159`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     157 |             }
     158 |         }
>>>  159 |         require(indexMet == 1 || _stablecoinList[stablecoinListLength - 1] == stableMaster, "45");
     160 |         _stablecoinList.pop();
     161 |         // Deleting the stablecoin from the list
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:176`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     174 |     /// @dev Governor is also guardian everywhere in all contracts
     175 |     function addGovernor(address _governor) external override onlyGovernor zeroCheck(_governor) {
>>>  176 |         require(!governorMap[_governor], "46");
     177 |         governorMap[_governor] = true;
     178 |         _governorList.push(_governor);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:196`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     194 |         // Checking if removing the governor will leave with at least more than one governor
     195 |         uint256 governorListLength = _governorList.length;
>>>  196 |         require(governorListLength > 1, "47");
     197 |         // Removing the governor from the list of governors
     198 |         // We still need to check if the address provided was well in the list
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:207`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     205 |             }
     206 |         }
>>>  207 |         require(indexMet == 1 || _governorList[governorListLength - 1] == _governor, "48");
     208 |         _governorList.pop();
     209 |         // Once it has been checked that the given address was a correct address, we can proceed to other changes
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:229`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     227 |     /// @dev The guardian address cannot be a governor address
     228 |     function setGuardian(address _newGuardian) external override onlyGuardian zeroCheck(_newGuardian) {
>>>  229 |         require(!governorMap[_newGuardian], "39");
     230 |         require(guardian != _newGuardian, "49");
     231 |         address oldGuardian = guardian;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `core\Core.sol:230`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     228 |     function setGuardian(address _newGuardian) external override onlyGuardian zeroCheck(_newGuardian) {
     229 |         require(!governorMap[_newGuardian], "39");
>>>  230 |         require(guardian != _newGuardian, "49");
     231 |         address oldGuardian = guardian;
     232 |         guardian = _newGuardian;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `dao\ANGLE.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      39 |     /// @param minter_ Address of the new minter
      40 |     function setMinter(address minter_) external {
>>>   41 |         require(msg.sender == minter, "67");
      42 |         require(minter_ != address(0), "0");
      43 |         emit MinterChanged(minter, minter_);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `dao\ANGLE.sol:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      49 |     /// @param amount Number of tokens to be minted
      50 |     function mint(address dst, uint256 amount) external {
>>>   51 |         require(msg.sender == minter, "68");
      52 |         require(block.timestamp >= mintingAllowedAfter, "69");
      53 |         require(amount <= (totalSupply() * MAX_MINT) / 100, "70");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `dao\ANGLE.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      50 |     function mint(address dst, uint256 amount) external {
      51 |         require(msg.sender == minter, "68");
>>>   52 |         require(block.timestamp >= mintingAllowedAfter, "69");
      53 |         require(amount <= (totalSupply() * MAX_MINT) / 100, "70");
      54 |         // Record the mint
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `deprecated\bondingCurve\BondingCurve.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     110 |         uint256 maxAmountToPayInAgToken
     111 |     ) external override whenNotPaused isValid(_agToken) {
>>>  112 |         require(targetSoldTokenQuantity > 0, "4");
     113 |         // Computing the number of reference stablecoins to burn to get the desired quantity
     114 |         // of tokens sold by this contract
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `deprecated\bondingCurve\BondingCurve.sol:130`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     128 |             amountToPayInAgToken = (amountToPayInReference * BASE_TOKENS) / oracleValue;
     129 |         }
>>>  130 |         require(amountToPayInAgToken > 0 && amountToPayInAgToken <= maxAmountToPayInAgToken, "50");
     131 | 
     132 |         // Transferring the correct amount of agToken
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `deprecated\bondingCurve\BondingCurve.sol:248`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     246 |     /// @dev As this function can manipulate the price, it has to be governor only
     247 |     function changeStartPrice(uint256 _startPrice) external onlyRole(GOVERNOR_ROLE) {
>>>  248 |         require(_startPrice > 0, "53");
     249 |         startPrice = _startPrice;
     250 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `deprecated\bondingCurve\BondingCurve.sol:297`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     295 |     /// @dev It can be used to decrease or increase what has already been sold
     296 |     function _changeTokensToSell(uint256 _totalTokensToSell) internal {
>>>  297 |         require(_totalTokensToSell > tokensSold, "54");
     298 |         require(soldToken.balanceOf(address(this)) >= _totalTokensToSell - tokensSold, "56");
     299 |         totalTokensToSell = _totalTokensToSell;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `deprecated\bondingCurve\BondingCurve.sol:317`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     315 |     function _computePriceFromQuantity(uint256 targetQuantity) internal view returns (uint256 value) {
     316 |         uint256 leftToSell = _getQuantityLeftToSell();
>>>  317 |         require(targetQuantity < leftToSell, "55");
     318 | 
     319 |         // The global value to compute is (with `power = 2` here):
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `deprecated\dao\Governor.sol:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      56 |     /// @notice Returns the quorum
      57 |     function quorum(uint256 blockNumber) public view override returns (uint256) {
>>>   58 |         require(blockNumber < block.number, "ERC20Votes: block not yet mined");
      59 |         return _quorum;
      60 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\AccessControlUpgradeable.sol:191`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     189 |      */
     190 |     function renounceRole(bytes32 role, address account) external override {
>>>  191 |         require(account == msg.sender, "71");
     192 | 
     193 |         _revokeRole(role, account);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\SmartWalletChecker.sol:40`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      38 |     /// @param _admin New admin of the contract
      39 |     function commitAdmin(address _admin) external {
>>>   40 |         require(msg.sender == admin, "!admin");
      41 |         future_admin = _admin;
      42 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\SmartWalletChecker.sol:46`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      44 |     /// @notice Changes the admin to the admin that has been committed
      45 |     function applyAdmin() external {
>>>   46 |         require(msg.sender == admin, "!admin");
      47 |         require(future_admin != address(0), "admin not set");
      48 |         admin = future_admin;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\SmartWalletChecker.sol:55`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      53 |     /// @dev This address can be the zero address in which case there will be no checker
      54 |     function commitSetChecker(address _checker) external {
>>>   55 |         require(msg.sender == admin, "!admin");
      56 |         future_checker = _checker;
      57 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\SmartWalletChecker.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      59 |     /// @notice Applies the checker previously committed
      60 |     function applySetChecker() external {
>>>   61 |         require(msg.sender == admin, "!admin");
      62 |         checker = future_checker;
      63 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\SmartWalletChecker.sol:68`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      66 |     /// @param _wallet Wallet to approve
      67 |     function approveWallet(address _wallet) public {
>>>   68 |         require(msg.sender == admin, "!admin");
      69 |         wallets[_wallet] = true;
      70 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `external\SmartWalletChecker.sol:77`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      75 |     /// @param _wallet Wallet to revoke
      76 |     function revokeWallet(address _wallet) external {
>>>   77 |         require(msg.sender == admin, "!admin");
      78 |         wallets[_wallet] = false;
      79 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `feeManager\FeeManager.sol:118`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     116 |         uint8 typeChange
     117 |     ) external override onlyRole(GUARDIAN_ROLE) {
>>>  118 |         require(xArray.length == yArray.length && yArray.length > 0, "5");
     119 |         for (uint256 i = 0; i <= yArray.length - 1; i++) {
     120 |             if (i > 0) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `feeManager\FeeManager.sol:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     119 |         for (uint256 i = 0; i <= yArray.length - 1; i++) {
     120 |             if (i > 0) {
>>>  121 |                 require(xArray[i] > xArray[i - 1], "7");
     122 |             }
     123 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `feeManager\FeeManager.sol:170`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     168 |             for (uint256 i = 0; i <= ySlippageFee.length - 1; i++) {
     169 |                 if (ySlippageFee[i] > 0) {
>>>  170 |                     require(ySlippageFee[i] <= BASE_PARAMS_CASTED, "37");
     171 |                     require(_piecewiseLinearCollatRatio(xSlippageFee[i], xSlippage, ySlippage) > 0, "38");
     172 |                 }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `genericLender\GenericAave.sol:441`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     439 |     /// @param __customReferral New custom referral
     440 |     function setReferralCode(uint16 __customReferral) external onlyRole(GUARDIAN_ROLE) {
>>>  441 |         require(__customReferral != 0, "invalid referral code");
     442 |         _customReferral = __customReferral;
     443 |         emit CustomReferralUpdated(_customReferral);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `genericLender\GenericLenderBase.sol:103`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     101 |     function sweep(address _token, address to) external override onlyRole(GUARDIAN_ROLE) {
     102 |         address[] memory __protectedTokens = _protectedTokens();
>>>  103 |         for (uint256 i = 0; i < __protectedTokens.length; i++) require(_token != __protectedTokens[i], "93");
     104 | 
     105 |         IERC20(_token).safeTransfer(to, IERC20(_token).balanceOf(address(this)));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\OracleDAI.sol:57`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      55 |         ModuleChainlinkMulti(_circuitChainlink, _circuitChainIsMultiplied, stalePeriod, guardians)
      56 |     {
>>>   57 |         require(addressInAndOutUni.length == 2, "107");
      58 |         // Using the tokens' metadata to get the in and out currencies decimals
      59 |         IERC20Metadata inCur = IERC20Metadata(addressInAndOutUni[0]);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\OracleMulti.sol:57`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      55 |         ModuleChainlinkMulti(_circuitChainlink, _circuitChainIsMultiplied, stalePeriod, guardians)
      56 |     {
>>>   57 |         require(addressInAndOutUni.length == 2, "107");
      58 |         // Using the tokens' metadata to get the in and out currencies decimals
      59 |         IERC20Metadata inCur = IERC20Metadata(addressInAndOutUni[0]);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleChainlinkMulti.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      29 |     ) {
      30 |         uint256 circuitLength = _circuitChainlink.length;
>>>   31 |         require(circuitLength > 0, "106");
      32 |         require(circuitLength == _circuitChainIsMultiplied.length, "104");
      33 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleChainlinkMulti.sol:32`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      30 |         uint256 circuitLength = _circuitChainlink.length;
      31 |         require(circuitLength > 0, "106");
>>>   32 |         require(circuitLength == _circuitChainIsMultiplied.length, "104");
      33 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
      34 |         require(guardians.length > 0, "101");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleChainlinkMulti.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      32 |         require(circuitLength == _circuitChainIsMultiplied.length, "104");
      33 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
>>>   34 |         require(guardians.length > 0, "101");
      35 |         for (uint256 i = 0; i < guardians.length; i++) {
      36 |             require(guardians[i] != address(0), "0");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleChainlinkSingle.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      31 |         chainlinkDecimals = AggregatorV3Interface(_poolChainlink).decimals();
      32 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
>>>   33 |         require(guardians.length > 0, "101");
      34 |         for (uint256 i = 0; i < guardians.length; i++) {
      35 |             require(guardians[i] != address(0), "0");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleUniswapMulti.sol:32`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      30 |     ) {
      31 |         // There is no `GOVERNOR_ROLE` in this contract, governor has `GUARDIAN_ROLE`
>>>   32 |         require(guardians.length > 0, "101");
      33 |         for (uint256 i = 0; i < guardians.length; i++) {
      34 |             require(guardians[i] != address(0), "0");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleUniswapMulti.sol:41`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      39 |         require(int32(_twapPeriod) > 0, "102");
      40 |         uint256 circuitUniLength = _circuitUniswap.length;
>>>   41 |         require(circuitUniLength > 0, "103");
      42 |         require(circuitUniLength == _circuitUniIsMultiplied.length, "104");
      43 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleUniswapMulti.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      40 |         uint256 circuitUniLength = _circuitUniswap.length;
      41 |         require(circuitUniLength > 0, "103");
>>>   42 |         require(circuitUniLength == _circuitUniIsMultiplied.length, "104");
      43 | 
      44 |         twapPeriod = _twapPeriod;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleUniswapMultiWithKeeper.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      31 |         if (int32(_twapPeriod) == 0) revert ZeroParameter();
      32 |         uint256 circuitUniLength = _circuitUniswap.length;
>>>   33 |         require(circuitUniLength > 0, "103");
      34 |         require(circuitUniLength == _circuitUniIsMultiplied.length, "104");
      35 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `oracle\modules\ModuleUniswapMultiWithKeeper.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      32 |         uint256 circuitUniLength = _circuitUniswap.length;
      33 |         require(circuitUniLength > 0, "103");
>>>   34 |         require(circuitUniLength == _circuitUniIsMultiplied.length, "104");
      35 | 
      36 |         twapPeriod = _twapPeriod;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManager.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      40 |     /// @notice Checks if the message sender is the rewards distribution address
      41 |     modifier onlyRewardsDistribution() {
>>>   42 |         require(msg.sender == rewardsDistribution, "1");
      43 |         _;
      44 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManager.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 |         uint256 balance = rewardToken.balanceOf(address(this));
      95 | 
>>>   96 |         require(rewardRate <= balance / rewardsDuration, "22");
      97 | 
      98 |         lastUpdateTime = block.timestamp;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManager.sol:209`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     207 |     {
     208 |         // Checking the compatibility of the parameters
>>>  209 |         require(BASE_PARAMS**2 > _maxLeverage * _maintenanceMargin, "8");
     210 |         maxLeverage = _maxLeverage;
     211 |         maintenanceMargin = _maintenanceMargin;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManager.sol:254`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     252 |         onlyCompatibleFees(_limitHAHedge)
     253 |     {
>>>  254 |         require(_targetHAHedge <= _limitHAHedge, "8");
     255 |         limitHAHedge = _limitHAHedge;
     256 |         targetHAHedge = _targetHAHedge;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:86`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      84 |     ) external override whenNotPaused zeroCheck(owner) returns (uint256 perpetualID) {
      85 |         // Transaction will revert anyway if `margin` is zero
>>>   86 |         require(committedAmount > 0, "27");
      87 | 
      88 |         // There could be a reentrancy attack as a call to an external contract is done before state variables
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:98`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      96 |         // Checking if the oracle rate is not too big: a too big oracle rate could mean for a HA that the price
      97 |         // has become too high to make it interesting to open a perpetual
>>>   98 |         require(rateUp <= maxOracleRate, "28");
      99 | 
     100 |         // Computing the total amount of stablecoins that this perpetual is going to hedge for the protocol
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:104`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     102 |         // Computing the net amount brought by the HAs to store in the perpetual
     103 |         uint256 netMargin = _getNetMargin(margin, totalHedgeAmountUpdate, committedAmount);
>>>  104 |         require(netMargin >= minNetMargin, "29");
     105 |         // Checking if the perpetual is not too leveraged, even after computing the fees
     106 |         require((committedAmount * BASE_PARAMS) <= maxLeverage * netMargin, "30");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:153`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     151 |         if (liquidated == 0) {
     152 |             // You need to wait `lockTime` before being able to withdraw funds from the protocol as a HA
>>>  153 |             require(perpetual.entryTimestamp + lockTime <= block.timestamp, "31");
     154 |             // Cashing out the perpetual internally
     155 |             _closePerpetual(perpetualID, perpetual);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:164`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     162 |                 _computeHedgeRatio(totalHedgeAmount)
     163 |             );
>>>  164 |             require(netCashOutAmount >= minCashOutAmount, "32");
     165 |             emit PerpetualClosed(perpetualID, netCashOutAmount);
     166 |             _secureTransfer(to, netCashOutAmount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:450`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     448 |     function approve(address to, uint256 perpetualID) external override {
     449 |         address owner = _ownerOf(perpetualID);
>>>  450 |         require(to != owner, "35");
     451 |         require(msg.sender == owner || isApprovedForAll(owner, msg.sender), "21");
     452 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `perpetualManager\PerpetualManagerFront.sol:467`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     465 |     /// @param approved Whether the sender wants to approve or block the operator
     466 |     function setApprovalForAll(address operator, bool approved) external override {
>>>  467 |         require(operator != msg.sender, "36");
     468 |         _operatorApprovals[msg.sender][operator] = approved;
     469 |         emit ApprovalForAll(_msgSender(), operator, approved);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManager.sol:335`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     333 |         StrategyParams storage params = strategies[strategy];
     334 | 
>>>  335 |         require(params.lastReport == 0, "73");
     336 |         require(address(this) == IStrategy(strategy).poolManager(), "74");
     337 |         // Using current code, this condition should always be verified as in the constructor
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManager.sol:340`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     338 |         // of the strategy the `want()` is set to the token of this `PoolManager`
     339 |         require(address(token) == IStrategy(strategy).want(), "75");
>>>  340 |         require(debtRatio + _debtRatio <= BASE_PARAMS, "76");
     341 | 
     342 |         // Add strategy to approved strategies
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManager.sol:406`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     404 |         StrategyParams storage params = strategies[strategy];
     405 | 
>>>  406 |         require(params.debtRatio == 0, "77");
     407 |         require(params.totalStrategyDebt == 0, "77");
     408 |         uint256 strategyListLength = strategyList.length;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManager.sol:407`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     405 | 
     406 |         require(params.debtRatio == 0, "77");
>>>  407 |         require(params.totalStrategyDebt == 0, "77");
     408 |         uint256 strategyListLength = strategyList.length;
     409 |         require(params.lastReport != 0 && strategyListLength >= 1, "78");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManager.sol:409`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     407 |         require(params.totalStrategyDebt == 0, "77");
     408 |         uint256 strategyListLength = strategyList.length;
>>>  409 |         require(params.lastReport != 0 && strategyListLength >= 1, "78");
     410 |         // It has already been checked whether the strategy was a valid strategy
     411 |         for (uint256 i = 0; i < strategyListLength - 1; i++) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManager.sol:438`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     436 |     function withdrawFromStrategy(IStrategy strategy, uint256 amount) external onlyRole(GUARDIAN_ROLE) {
     437 |         StrategyParams storage params = strategies[address(strategy)];
>>>  438 |         require(params.lastReport != 0, "78");
     439 | 
     440 |         uint256 loss;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManagerInternal.sol:64`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      62 |     function _updateStrategyDebtRatio(address strategy, uint256 _debtRatio) internal {
      63 |         StrategyParams storage params = strategies[strategy];
>>>   64 |         require(params.lastReport != 0, "78");
      65 |         debtRatio = debtRatio + _debtRatio - params.debtRatio;
      66 |         require(debtRatio <= BASE_PARAMS, "76");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `poolManager\PoolManagerInternal.sol:66`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      64 |         require(params.lastReport != 0, "78");
      65 |         debtRatio = debtRatio + _debtRatio - params.debtRatio;
>>>   66 |         require(debtRatio <= BASE_PARAMS, "76");
      67 |         params.debtRatio = _debtRatio;
      68 |         emit StrategyAdded(strategy, debtRatio);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `router\AngleRouter.sol:1432`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
    1430 |             "0"
    1431 |         );
>>> 1432 |         require(_governor != _guardian, "49");
    1433 |         require(existingPoolManagers.length == existingLiquidityGauges.length, "104");
    1434 |         // Fetching the stablecoin and mapping it to the `StableMaster`
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `router\AngleRouter.sol:1433`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
    1431 |         );
    1432 |         require(_governor != _guardian, "49");
>>> 1433 |         require(existingPoolManagers.length == existingLiquidityGauges.length, "104");
    1434 |         // Fetching the stablecoin and mapping it to the `StableMaster`
    1435 |         mapStableMasters[
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `sanToken\SanToken.sol:64`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      62 |     /// @dev There is no Access Control here, because it can be handled cheaply through these modifiers
      63 |     modifier onlyStableMaster() {
>>>   64 |         require(msg.sender == stableMaster, "1");
      65 |         _;
      66 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `sanToken\SanToken.sol:115`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     113 |     ) external override onlyStableMaster {
     114 |         uint256 currentAllowance = allowance(burner, sender);
>>>  115 |         require(currentAllowance >= amount, "23");
     116 |         _approve(burner, sender, currentAllowance - amount);
     117 |         _burn(burner, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:203`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     201 |         Collateral storage col = collateralMap[IPoolManager(poolManager)];
     202 |         _contractMapCheck(col);
>>>  203 |         require(col.stocksUsers >= amount, "4");
     204 |         col.stocksUsers -= amount;
     205 |         emit StocksUsersUpdated(address(col.token), col.stocksUsers);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:367`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     365 |         uint256 indexMet;
     366 |         uint256 managerListLength = _managerList.length;
>>>  367 |         require(managerListLength >= 1, "10");
     368 |         for (uint256 i = 0; i < managerListLength - 1; i++) {
     369 |             if (_managerList[i] == poolManager) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:375`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     373 |             }
     374 |         }
>>>  375 |         require(indexMet == 1 || _managerList[managerListLength - 1] == poolManager, "10");
     376 |         _managerList.pop();
     377 |         Collateral memory col = collateralMap[poolManager];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:453`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     451 |         // The invariant `col.stocksUsers <= col.capOnStableMinted` should remain true even after a
     452 |         // governance update
>>>  453 |         require(colUp.stocksUsers + amount <= colUp.feeData.capOnStableMinted, "8");
     454 |         colDown.stocksUsers -= amount;
     455 |         colUp.stocksUsers += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:472`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     470 |         // Checking for the `poolManager`
     471 |         _contractMapCheck(col);
>>>  472 |         require(col.oracle != _oracle, "12");
     473 |         // The `inBase` of the new oracle should be the same as the `_collatBase` stored for this collateral
     474 |         require(col.collatBase == _oracle.inBase(), "11");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:496`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     494 |         // The invariant `col.stocksUsers <= col.capOnStableMinted` should remain true even after a
     495 |         // governance update
>>>  496 |         require(_capOnStableMinted >= col.stocksUsers, "8");
     497 |         col.feeData.capOnStableMinted = _capOnStableMinted;
     498 |         col.slpData.maxInterestsDistributed = _maxInterestsDistributed;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:515`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     513 |         // Checking for the `poolManager`
     514 |         _contractMapCheck(col);
>>>  515 |         require(_contractMap[oldFeeManager] == poolManager, "10");
     516 |         require(newFeeManager != oldFeeManager, "14");
     517 |         delete _contractMap[oldFeeManager];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMaster.sol:516`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     514 |         _contractMapCheck(col);
     515 |         require(_contractMap[oldFeeManager] == poolManager, "10");
>>>  516 |         require(newFeeManager != oldFeeManager, "14");
     517 |         delete _contractMap[oldFeeManager];
     518 |         _contractMap[newFeeManager] = poolManager;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMasterFront.sol:78`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      76 |         // Checking if the user got more stablecoins than the least amount specified in the parameters of the
      77 |         // function
>>>   78 |         require(amountForUserInStable >= minStableAmount, "15");
      79 | 
      80 |         // Updating the `stocksUsers` for this collateral, that is the amount of collateral that was
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMasterFront.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      82 |         col.stocksUsers += amountForUserInStable;
      83 |         // Checking if stablecoins can still be issued using this collateral type
>>>   84 |         require(col.stocksUsers <= col.feeData.capOnStableMinted, "16");
      85 | 
      86 |         // Event needed to track `col.stocksUsers` off-chain
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMasterFront.sol:133`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     131 |         // between different collateral types, or at least rebalance what is stored in the reserves through
     132 |         // the `recoverERC20` function followed by a swap and then a transfer
>>>  133 |         require(amount <= col.stocksUsers, "17");
     134 | 
     135 |         // Burning the tokens will revert if there are not enough tokens in balance or if the `msg.sender`
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `stableMaster\StableMasterFront.sol:159`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     157 |         uint256 redeemInC = (amount * (BASE_PARAMS - _computeFeeBurn(amount, col)) * col.collatBase) /
     158 |             (oracleValue * BASE_PARAMS);
>>>  159 |         require(redeemInC >= minCollatAmount, "15");
     160 | 
     161 |         // Updating the `stocksUsers` that is the amount of collateral that was brought by users
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\AngleDistributor.sol:131`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     129 |         // Checking if the gauge has been added or if it still possible to distribute rewards to this gauge
     130 |         int128 gaugeType = IGaugeController(controller).gauge_types(gaugeAddr);
>>>  131 |         require(gaugeType >= 0 && !killedGauges[gaugeAddr], "110");
     132 | 
     133 |         // Calculate the elapsed time in weeks.
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\AngleDistributor.sol:252`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     250 |     function distributeReward(address gaugeAddr) external nonReentrant returns (uint256, uint256) {
     251 |         // Checking if distribution is on
>>>  252 |         require(distributionsOn == true, "109");
     253 |         // Updating rate distribution parameters if need be
     254 |         if (block.timestamp >= startEpochTime + RATE_REDUCTION_TIME) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\AngleDistributor.sol:267`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     265 |     function distributeRewardToMultipleGauges(address[] memory gauges) external nonReentrant {
     266 |         // Checking if distribution is on
>>>  267 |         require(distributionsOn == true, "109");
     268 |         // Updating rate distribution parameters if need be
     269 |         if (block.timestamp >= startEpochTime + RATE_REDUCTION_TIME) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\AngleDistributor.sol:280`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     278 |     /// @dev Callable by any address, but only once per epoch
     279 |     function updateMiningParameters() external {
>>>  280 |         require(block.timestamp >= startEpochTime + RATE_REDUCTION_TIME, "108");
     281 |         _updateMiningParameters();
     282 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:65`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      63 |     ) {
      64 |         require(rewardTokenAddress != address(0) && guardian != address(0), "0");
>>>   65 |         require(governorList.length > 0, "47");
      66 |         rewardToken = IERC20(rewardTokenAddress);
      67 |         // Since this contract is independent from the rest of the protocol
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:93`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      91 |     function drip(IStakingRewards stakingContract) external override returns (uint256) {
      92 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
>>>   93 |         require(stakingParams.duration > 0, "80");
      94 |         require(_isDripAvailable(stakingParams), "81");
      95 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:98`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      96 |         uint256 dripAmount = _computeDripAmount(stakingParams);
      97 |         stakingParams.lastDistributionTime = block.timestamp;
>>>   98 |         require(dripAmount != 0, "82");
      99 |         stakingParams.distributedRewards += dripAmount;
     100 |         emit Dripped(msg.sender, dripAmount, address(stakingContract));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:166`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     164 |         uint256 indexMet;
     165 |         uint256 stakingContractsListLength = stakingContractsList.length;
>>>  166 |         require(stakingContractsListLength >= 1, "80");
     167 |         for (uint256 i = 0; i < stakingContractsListLength - 1; i++) {
     168 |             if (stakingContractsList[i] == stakingContract) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:174`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     172 |             }
     173 |         }
>>>  174 |         require(indexMet == 1 || stakingContractsList[stakingContractsListLength - 1] == stakingContract, "80");
     175 | 
     176 |         stakingContractsList.pop();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:200`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     198 |         uint256 _amountToDistribute
     199 |     ) external override onlyRole(GOVERNOR_ROLE) {
>>>  200 |         require(_duration > 0, "85");
     201 |         require(_duration >= _updateFrequency && block.timestamp >= _updateFrequency, "86");
     202 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:201`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     199 |     ) external override onlyRole(GOVERNOR_ROLE) {
     200 |         require(_duration > 0, "85");
>>>  201 |         require(_duration >= _updateFrequency && block.timestamp >= _updateFrequency, "86");
     202 | 
     203 |         IStakingRewards stakingContract = IStakingRewards(_stakingContract);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:231`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     229 |     {
     230 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
>>>  231 |         require(stakingParams.duration > 0, "80");
     232 |         require(stakingParams.duration >= _updateFrequency, "87");
     233 |         stakingParams.updateFrequency = _updateFrequency;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:232`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     230 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
     231 |         require(stakingParams.duration > 0, "80");
>>>  232 |         require(stakingParams.duration >= _updateFrequency, "87");
     233 |         stakingParams.updateFrequency = _updateFrequency;
     234 |         emit FrequencyUpdated(_updateFrequency, address(stakingContract));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:246`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     244 |     {
     245 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
>>>  246 |         require(stakingParams.duration > 0, "80");
     247 |         stakingParams.incentiveAmount = _incentiveAmount;
     248 |         emit IncentiveUpdated(_incentiveAmount, address(stakingContract));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:260`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     258 |     {
     259 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
>>>  260 |         require(stakingParams.duration > 0, "80");
     261 |         require(stakingParams.distributedRewards < _amountToDistribute, "88");
     262 |         stakingParams.amountToDistribute = _amountToDistribute;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:261`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     259 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
     260 |         require(stakingParams.duration > 0, "80");
>>>  261 |         require(stakingParams.distributedRewards < _amountToDistribute, "88");
     262 |         stakingParams.amountToDistribute = _amountToDistribute;
     263 |         emit AmountToDistributeUpdated(_amountToDistribute, address(stakingContract));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:271`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     269 |     function setDuration(uint256 _duration, IStakingRewards stakingContract) external override onlyRole(GUARDIAN_ROLE) {
     270 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
>>>  271 |         require(stakingParams.duration > 0, "80");
     272 |         require(_duration >= stakingParams.updateFrequency, "87");
     273 |         uint256 timeElapsed = _timeSinceStart(stakingParams);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:272`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     270 |         StakingParameters storage stakingParams = stakingContractsMap[stakingContract];
     271 |         require(stakingParams.duration > 0, "80");
>>>  272 |         require(_duration >= stakingParams.updateFrequency, "87");
     273 |         uint256 timeElapsed = _timeSinceStart(stakingParams);
     274 |         require(timeElapsed < stakingParams.duration && timeElapsed < _duration, "66");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\RewardsDistributor.sol:274`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     272 |         require(_duration >= stakingParams.updateFrequency, "87");
     273 |         uint256 timeElapsed = _timeSinceStart(stakingParams);
>>>  274 |         require(timeElapsed < stakingParams.duration && timeElapsed < _duration, "66");
     275 |         stakingParams.duration = _duration;
     276 |         emit DurationUpdated(_duration, address(stakingContract));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\StakingRewards.sol:18`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      16 |     /// @dev There is no Access Control here, because it can be handled cheaply through these modifiers
      17 |     modifier onlyRewardsDistribution() {
>>>   18 |         require(msg.sender == rewardsDistribution, "1");
      19 |         _;
      20 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\StakingRewards.sol:171`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     169 |     /// @param amount Amount of the ERC20 staking token that the `msg.sender` wants to withdraw
     170 |     function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
>>>  171 |         require(amount > 0, "89");
     172 |         _totalSupply = _totalSupply - amount;
     173 |         _balances[msg.sender] = _balances[msg.sender] - amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\StakingRewards.sol:218`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     216 |     /// @dev Before calling this function, it has already been verified whether this address was a zero address or not
     217 |     function _stake(uint256 amount, address onBehalf) internal {
>>>  218 |         require(amount > 0, "90");
     219 |         stakingToken.safeTransferFrom(msg.sender, address(this), amount);
     220 |         _totalSupply = _totalSupply + amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `staking\StakingRewards.sol:252`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     250 |         // Reward + leftover must be less than 2^256 / 10^18 to avoid overflow.
     251 |         uint256 balance = rewardToken.balanceOf(address(this));
>>>  252 |         require(rewardRate <= balance / rewardsDuration, "91");
     253 | 
     254 |         lastUpdateTime = block.timestamp;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `strategies\BaseStrategy.sol:430`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     428 |             // In the strategy we use so far, the only protectedToken is the want token
     429 |             // and this has been checked above
>>>  430 |             require(_token != __protectedTokens[i], "93");
     431 | 
     432 |         IERC20(_token).safeTransfer(to, IERC20(_token).balanceOf(address(this)));
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `strategies\Strategy.sol:375`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     373 |                 }
     374 |             }
>>>  375 |             require(found, "94");
     376 | 
     377 |             share = share + _newPositions[i].share;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `strategies\Strategy.sol:383`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     381 |         }
     382 | 
>>>  383 |         require(share == 1000, "95");
     384 |     }
     385 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `strategies\Strategy.sol:429`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     427 | 
     428 |                 if (!force) {
>>>  429 |                     require(allWithdrawn, "98");
     430 |                 }
     431 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `strategies\Strategy.sol:451`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     449 |             }
     450 |         }
>>>  451 |         require(false, "94");
     452 |     }
     453 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `surplus\BaseSurplusConverter.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |         // zero address
      58 |         IERC20(_rewardToken).safeApprove(_feeDistributor, type(uint256).max);
>>>   59 |         require(guardians.length > 0, "101");
      60 |         for (uint256 i = 0; i < guardians.length; i++) {
      61 |             require(guardians[i] != address(0), "0");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `surplus\SurplusConverterSanTokens.sol:74`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      72 |         bool transfer
      73 |     ) external override whenNotPaused onlyRole(WHITELISTED_ROLE) {
>>>   74 |         require(token == supportedToken, "20");
      75 |         stableMaster.deposit(amount, address(this), poolManager);
      76 |         if (transfer) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `surplus\SurplusConverterUniV2Sushi.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 |         address[] memory sushiswapPath = sushiswapPaths[token];
     136 |         address[] memory uniswapPath = uniswapPaths[token];
>>>  137 |         require(sushiswapPath.length > 0 || uniswapPath.length > 0, "20");
     138 |         if (sushiswapPath.length > 0 && uniswapPath.length > 0) {
     139 |             // Storing the router addresses in memory to avoid duplicate storage reads for one of the two
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `surplus\SurplusConverterUniV3.sol:56`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      54 |     ) external onlyRole(GUARDIAN_ROLE) {
      55 |         require(token != address(0), "0");
>>>   56 |         require(pathAddresses.length >= 2, "5");
      57 |         require(pathAddresses.length == (pathFees.length + 1), "104");
      58 |         require(pathAddresses[0] == token && pathAddresses[pathAddresses.length - 1] == address(rewardToken), "111");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `surplus\SurplusConverterUniV3.sol:101`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      99 |     ) external override whenNotPaused onlyRole(WHITELISTED_ROLE) {
     100 |         bytes memory path = uniswapPaths[token];
>>>  101 |         require(path.length != 0, "111");
     102 |         uniswapV3Router.exactInput(ExactInputParams(path, address(this), block.timestamp, amount, minAmount));
     103 |         if (transfer) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `utils\FunctionUtils.sol:72`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      70 |     /// to `BASE_PARAMS`
      71 |     modifier onlyCompatibleInputArrays(uint64[] memory xArray, uint64[] memory yArray) {
>>>   72 |         require(xArray.length == yArray.length && xArray.length > 0, "5");
      73 |         for (uint256 i = 0; i <= yArray.length - 1; i++) {
      74 |             require(yArray[i] <= uint64(BASE_PARAMS) && xArray[i] <= uint64(BASE_PARAMS), "6");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `utils\FunctionUtils.sol:76`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      74 |             require(yArray[i] <= uint64(BASE_PARAMS) && xArray[i] <= uint64(BASE_PARAMS), "6");
      75 |             if (i > 0) {
>>>   76 |                 require(xArray[i] > xArray[i - 1], "7");
      77 |             }
      78 |         }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `utils\FunctionUtils.sol:86`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      84 |     /// @param fees Value of the new parameter to check
      85 |     modifier onlyCompatibleFees(uint64 fees) {
>>>   86 |         require(fees <= BASE_PARAMS, "4");
      87 |         _;
      88 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `utils\PausableMapUpgradeable.sol:31`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      29 |     /// @dev The contract must not be paused for `name`
      30 |     function _pause(bytes32 name) internal {
>>>   31 |         require(!paused[name], "18");
      32 |         paused[name] = true;
      33 |         emit Paused(name);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `utils\PausableMapUpgradeable.sol:40`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      38 |     /// @dev The contract must be paused for `name`
      39 |     function _unpause(bytes32 name) internal {
>>>   40 |         require(paused[name], "19");
      41 |         paused[name] = false;
      42 |         emit Unpaused(name);
```
</details>

---


---
*Generated by BugHunter*