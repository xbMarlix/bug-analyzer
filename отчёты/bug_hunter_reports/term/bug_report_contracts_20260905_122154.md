# BugHunter Report: contracts

**Generated:** 2026-09-05 12:21:54
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\term\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 162 |
| Total lines | 25,540 |
| Bugs found | 119 |
| !! High | 17 |
| ! Medium | 63 |
| ~ Low | 39 |

### Languages Detected

- **solidity**: 162 files

## Security (14)

### [!!] Unsafe Delegatecall

- **File:** `TermDiamond.sol:79`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      77 |         address facet = ds.selectorToFacetAndPosition[msg.sig].facetAddress;
      78 |         require(facet != address(0), "Diamond: Function does not exist");
>>>   79 |         // Execute external function from facet using delegatecall and return any value.
      80 |         assembly {
      81 |             // copy function selector and any arguments
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `TermDiamond.sol:84`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      82 |             calldatacopy(0, 0, calldatasize())
      83 |             // execute function call using the facet
>>>   84 |             let result := delegatecall(gas(), facet, 0, calldatasize(), 0, 0)
      85 |             // get any return value
      86 |             returndatacopy(0, 0, returndatasize())
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\DiamondCutFacet.sol:52`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      50 | 
      51 |     /// @notice Initializes diamond access control roles and supported interfaces
>>>   52 |     /// @dev This function is intended to be called only via delegatecall during diamond
      53 |     ///      construction. The msg.sender check ensures it can only be called from within
      54 |     ///      the diamond contract itself, preventing external role hijacking attacks.
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\DiamondCutFacet.sol:76`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      74 | 
      75 |     /// @notice Add/replace/remove any number of1 functions and optionally execute
>>>   76 |     ///         a function with delegatecall
      77 |     /// @param _diamondCut Contains the facet addresses and function selectors
      78 |     /// @param _init The address of the contract or facet to execute _calldata
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\DiamondCutFacet.sol:80`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      78 |     /// @param _init The address of the contract or facet to execute _calldata
      79 |     /// @param _calldata A function call, including function selector and arguments
>>>   80 |     ///                  _calldata is executed with delegatecall on _init
      81 |     function diamondCut(
      82 |         FacetCut[] calldata _diamondCut,
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\MulticallFacet.sol:88`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      86 |             require(facet != address(0), "MulticallFacet: Function does not exist");
      87 |             
>>>   88 |             // Direct delegatecall to facet (bypasses diamond fallback)
      89 |             (bool ok, bytes memory ret) = facet.delegatecall(calls[i]);
      90 |             successes[i] = ok;
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\MulticallFacet.sol:89`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      87 |             
      88 |             // Direct delegatecall to facet (bypasses diamond fallback)
>>>   89 |             (bool ok, bytes memory ret) = facet.delegatecall(calls[i]);
      90 |             successes[i] = ok;
      91 |             
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\flashloan\TermFlashLoanCentralReceiverFacet.sol:131`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     129 | 
     130 |         // Execute the flash loan operation using the callback's selector
>>>  131 |         Address.functionDelegateCall(actualFacet, encodedData);
     132 |         return true;
     133 |     }
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `facets\flashloan\TermFlashLoanExecutorFacet.sol:34`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      32 | ///      1. Previews the first action to determine the required flash loan amount.
      33 | ///      2. Borrows that amount from the flash loan aggregator (Instadapp).
>>>   34 | ///      3. In the callback, sequentially executes each action via `delegatecall`-style routing
      35 | ///         through the diamond, snapshotting token balances before/after each step.
      36 | ///      4. Optionally back-propagates minimum output requirements from the final repayment
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `factory\TermDiamondFactory.sol:53`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      51 | 
      52 |         // Deploy TermDiamond with the facet address
>>>   53 |         // This will automatically call initDiamondRoles via delegateCall during construction
      54 |         diamond = address(new TermDiamond(devopsWallet, adminWallet, diamondCutFacet));
      55 | 
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `libraries\LibDiamond.sol:20`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      18 | 
      19 |     /// @notice Add/replace/remove any number of functions and optionally execute
>>>   20 |     ///         a function with delegatecall
      21 |     /// @param _diamondCut Contains the facet addresses and function selectors
      22 |     /// @param _init The address of the contract or facet to execute _calldata
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `libraries\LibDiamond.sol:24`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      22 |     /// @param _init The address of the contract or facet to execute _calldata
      23 |     /// @param _calldata A function call, including function selector and arguments
>>>   24 |     ///                  _calldata is executed with delegatecall on _init
      25 |     function diamondCut(
      26 |         FacetCut[] calldata _diamondCut,
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `libraries\LibDiamond.sol:220`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
     218 |         }
     219 |         enforceHasContractCode(_init, "LibDiamondCut: _init address has no code");        
>>>  220 |         (bool success, bytes memory error) = _init.delegatecall(_calldata);
     221 |         if (!success) {
     222 |             if (error.length > 0) {
```
</details>

---

### [!!] Unsafe Delegatecall

- **File:** `test\TestTermFlashLoanCentralReceiverFacetHelper.sol:25`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** delegatecall executes code in the caller's storage context. Contract state can be corrupted.

**Fix:** If delegatecall is required, ensure the target is trusted and there are proper storage layout checks.

<details>
<summary>Code</summary>

```
      23 |     }
      24 | 
>>>   25 |     /// @notice No-op callback used as delegatecall target in success path tests
      26 |     function mockCallback(
      27 |         address[] calldata,
```
</details>

---

## Logic (47)

### [!!] block.number For Randomness

- **File:** `facets\MulticallFacet.sol:161`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
     159 |         j = _i;
     160 |         while (j != 0) {
>>>  161 |             bstr[--k] = bytes1(uint8(48 + j % 10));
     162 |             j /= 10;
     163 |         }
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `facets\ERC4626InterfaceFacet.sol:70`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'isTermApproved' is modified at line 70, after an external call at line 69. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      68 |         for (uint8 i = 0; i < ts.approvedTermControllerList.length; ++i) {
      69 |             if (ITermController(ts.approvedTermControllerList[i]).isTermApproved(vault)) {
>>>   70 |                 isTermApproved = true;
      71 |                 break;
      72 |             }
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `facets\external\TermAaveInterfaceFacet.sol:103`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'termApproved' is modified at line 103, after an external call at line 102. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     101 |         for (uint8 i = 0; i < ts.approvedTermControllerList.length; ++i) {
     102 |             if (ITermController(ts.approvedTermControllerList[i]).isTermApproved(aavePool)) {
>>>  103 |                 termApproved = true;
     104 |                 break;
     105 |             }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuction.sol:109`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     107 |     modifier onlyWhileAuctionClosed() {
     108 |         // solhint-disable-next-line not-rely-on-time
>>>  109 |         if (block.timestamp <= auctionEndTime) {
     110 |             revert AuctionNotClosed();
     111 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:91`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      89 |         if (
      90 |             // solhint-disable-next-line not-rely-on-time
>>>   91 |             block.timestamp > revealTime || block.timestamp < auctionStartTime
      92 |         ) {
      93 |             revert AuctionNotOpen();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:100`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      98 |         if (
      99 |             // solhint-disable-next-line not-rely-on-time
>>>  100 |             block.timestamp < revealTime
     101 |         ) {
     102 |             revert AuctionNotRevealing();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:300`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     298 |         if (
     299 |             // solhint-disable-next-line not-rely-on-time
>>>  300 |             block.timestamp > revealTime
     301 |         ) {
     302 |             revert AuctionNotOpen();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:367`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     365 |     ) external whenUnlockingNotPaused whileTermContractsNotPaused(termRepoServicer.termController()) nonReentrant {
     366 |         // solhint-disable-next-line not-rely-on-time
>>>  367 |         if (block.timestamp < auctionStartTime) {
     368 |             revert AuctionNotOpen();
     369 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:372`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     370 |         // solhint-disable-next-line not-rely-on-time
     371 |         if (
>>>  372 |             block.timestamp > revealTime &&
     373 |             !termAuction.auctionCancelledForWithdrawal()
     374 |         ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:395`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     393 |     ) external onlyRole(DIAMOND_ROLE) whenUnlockingNotPaused whileTermContractsNotPaused(termRepoServicer.termController()) nonReentrant {
     394 |         // solhint-disable-next-line not-rely-on-time
>>>  395 |         if (block.timestamp < auctionStartTime) {
     396 |             revert AuctionNotOpen();
     397 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:400`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     398 |         // solhint-disable-next-line not-rely-on-time
     399 |         if (
>>>  400 |             block.timestamp > revealTime &&
     401 |             !termAuction.auctionCancelledForWithdrawal()
     402 |         ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:694`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     692 |             // NOTE: Include bid for assignment only if term repurchase window hasn't expired.
     693 |             // solhint-disable-next-line not-rely-on-time
>>>  694 |             if (block.timestamp > pairOffServicer.endOfRepurchaseWindow()) {
     695 |                 _processBidForAuction(expiredRolloverBid.id);
     696 |             } else {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionBidLocker.sol:806`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     804 |                 if (
     805 |                     // solhint-disable-next-line not-rely-on-time
>>>  806 |                     block.timestamp > pairOffServicer.endOfRepurchaseWindow()
     807 |                 ) {
     808 |                     revert RolloverBidExpired(revealedBid.id);
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionOfferLocker.sol:80`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      78 |         if (
      79 |             // solhint-disable-next-line not-rely-on-time
>>>   80 |             block.timestamp > revealTime || block.timestamp < auctionStartTime
      81 |         ) {
      82 |             revert AuctionNotOpen();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionOfferLocker.sol:89`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      87 |         if (
      88 |             // solhint-disable-next-line not-rely-on-time
>>>   89 |             block.timestamp < revealTime
      90 |         ) {
      91 |             revert AuctionNotRevealing();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionOfferLocker.sol:355`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     353 |     ) external whenUnlockingNotPaused whileTermContractsNotPaused(termRepoServicer.termController()) nonReentrant {
     354 |         // solhint-disable-next-line not-rely-on-time
>>>  355 |         if (block.timestamp < auctionStartTime) {
     356 |             revert AuctionNotOpen();
     357 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionOfferLocker.sol:360`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     358 |         // solhint-disable-next-line not-rely-on-time
     359 |         if (
>>>  360 |             block.timestamp > revealTime &&
     361 |             !termAuction.auctionCancelledForWithdrawal()
     362 |         ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionOfferLocker.sol:384`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     382 |     ) external onlyRole(DIAMOND_ROLE) whenUnlockingNotPaused whileTermContractsNotPaused(termRepoServicer.termController()) nonReentrant {
     383 |         // solhint-disable-next-line not-rely-on-time
>>>  384 |         if (block.timestamp < auctionStartTime) {
     385 |             revert AuctionNotOpen();
     386 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermAuctionOfferLocker.sol:389`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     387 |         // solhint-disable-next-line not-rely-on-time
     388 |         if (
>>>  389 |             block.timestamp > revealTime &&
     390 |             !termAuction.auctionCancelledForWithdrawal()
     391 |         ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermPriceConsumerV3.sol:296`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     294 |                 priceFeeds[token].refreshRateThreshold == 0 ||
     295 |                 (lastUpdatedTimestamp > block.timestamp) ||
>>>  296 |                 (block.timestamp - lastUpdatedTimestamp) <= priceFeeds[token].refreshRateThreshold
     297 |             ) {
     298 |                 return (price, priceFeeds[token].priceFeed.decimals()); // Use primary price feed if there is no fallback price feed and update within refresh rate.
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermPriceConsumerV3.sol:307`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     305 |                 price > 0 && lastUpdatedTimestamp <= block.timestamp + DEFAULT_MAX_DATA_TIMESTAMP_AHEAD_SECONDS &&
     306 |                 ((lastUpdatedTimestamp > block.timestamp) ||
>>>  307 |                  (block.timestamp - lastUpdatedTimestamp) <= priceFeeds[token].refreshRateThreshold)
     308 |             ) {
     309 |                 return (price, priceFeeds[token].priceFeed.decimals()); // Return primary price feed if it is not stale
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermPriceConsumerV3.sol:327`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     325 |                 fallbackPriceFeeds[token].refreshRateThreshold == 0 ||
     326 |                 (fallbackLastUpdatedTimestamp > block.timestamp) ||
>>>  327 |                 (block.timestamp - fallbackLastUpdatedTimestamp) <= fallbackPriceFeeds[token].refreshRateThreshold
     328 |             ) {
     329 |                 return (fallbackPrice, fallbackPriceFeed.decimals()); // Use fallback price feed if primary price feed unavailable
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermPriceConsumerV3WithSequencer.sol:282`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     280 |             } else if (
     281 |                 priceFeeds[token].refreshRateThreshold == 0 ||
>>>  282 |                 (block.timestamp - lastUpdatedTimestamp) <=
     283 |                 priceFeeds[token].refreshRateThreshold
     284 |             ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermPriceConsumerV3WithSequencer.sol:293`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     291 |             if (
     292 |                 price > 0 &&
>>>  293 |                 (block.timestamp - lastUpdatedTimestamp) <=
     294 |                 priceFeeds[token].refreshRateThreshold
     295 |             ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermPriceConsumerV3WithSequencer.sol:311`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     309 |             } else if (
     310 |                 fallbackPriceFeeds[token].refreshRateThreshold == 0 ||
>>>  311 |                 (block.timestamp - fallbackLastUpdatedTimestamp) <=
     312 |                 fallbackPriceFeeds[token].refreshRateThreshold
     313 |             ) {
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoCollateralManager.sol:473`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     471 |     ) external whileLiquidationsNotPaused whileTermContractsNotPaused(termController) {
     472 |         // solhint-disable-next-line not-rely-on-time
>>>  473 |         if (block.timestamp <= termRepoServicer.endOfRepurchaseWindow()) {
     474 |             revert DefaultsClosed();
     475 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoCollateralManager.sol:552`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     550 |     ) external whileLiquidationsNotPaused whileTermContractsNotPaused(termController) {
     551 |         // solhint-disable-next-line not-rely-on-time
>>>  552 |         if (block.timestamp <= termRepoServicer.endOfRepurchaseWindow()) {
     553 |             revert DefaultsClosed();
     554 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoCollateralManager.sol:925`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     923 |     function _externalLockCollateralInternal(address borrower, address sender, address collateralToken, uint256 amount) internal {
     924 |         // solhint-disable-next-line not-rely-on-time
>>>  925 |         if (block.timestamp > termRepoServicer.endOfRepurchaseWindow()) {
     926 |             revert CollateralDepositClosed();
     927 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoCollateralManager.sol:946`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     944 |         if (
     945 |             // solhint-disable-next-line not-rely-on-time
>>>  946 |             block.timestamp >= termRepoServicer.endOfRepurchaseWindow() &&
     947 |             // solhint-disable-next-line not-rely-on-time
     948 |             block.timestamp < termRepoServicer.redemptionTimestamp()
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoCollateralManager.sol:948`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     946 |             block.timestamp >= termRepoServicer.endOfRepurchaseWindow() &&
     947 |             // solhint-disable-next-line not-rely-on-time
>>>  948 |             block.timestamp < termRepoServicer.redemptionTimestamp()
     949 |         ) {
     950 |             revert CollateralWithdrawalClosed();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoCollateralManager.sol:1113`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
    1111 |     ) internal returns (bool) {
    1112 |         // solhint-disable-next-line not-rely-on-time
>>> 1113 |         if (block.timestamp > termRepoServicer.endOfRepurchaseWindow()) {
    1114 |             revert ShortfallLiquidationsClosed();
    1115 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoRolloverManager.sol:70`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      68 |     modifier notPastRepaymentWindow() {
      69 |         // solhint-disable-next-line not-rely-on-time
>>>   70 |         if (block.timestamp >= termRepoServicer.endOfRepurchaseWindow()) {
      71 |             revert EndOfRepurchaseWindowReached();
      72 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:291`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     289 |     ) external onlyRole(DIAMOND_ROLE) returns (uint256) {
     290 |          // solhint-disable-next-line not-rely-on-time
>>>  291 |         if (block.timestamp > maturityTimestamp) {
     292 |             revert AfterMaturity();
     293 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:374`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     372 |     ) external {
     373 |         // solhint-disable-next-line not-rely-on-time
>>>  374 |         if (block.timestamp <= redemptionTimestamp) {
     375 |             revert RedemptionPeriodNotOpen();
     376 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:466`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     464 |     ) external onlyRole(AUCTIONEER) {
     465 |         // solhint-disable-next-line not-rely-on-time
>>>  466 |         if (block.timestamp >= maturityTimestamp) {
     467 |             revert AfterMaturity();
     468 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:533`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     531 |     ) external onlyRole(AUCTIONEER) returns (uint256) {
     532 |         // solhint-disable-next-line not-rely-on-time
>>>  533 |         if (block.timestamp >= maturityTimestamp) {
     534 |             revert AfterMaturity();
     535 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:581`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     579 |     ) external onlyRole(ROLLOVER_TARGET_AUCTIONEER_ROLE) returns (uint256) {
     580 |         // solhint-disable-next-line not-rely-on-time
>>>  581 |         if (block.timestamp < maturityTimestamp) {
     582 |             revert NotMaturedYet();
     583 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:585`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     583 |         }
     584 |         // solhint-disable-next-line not-rely-on-time
>>>  585 |         if (block.timestamp >= endOfRepurchaseWindow) {
     586 |             revert AfterRepurchaseWindow();
     587 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:703`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     701 | 
     702 |         // solhint-disable-next-line not-rely-on-time
>>>  703 |         if (block.timestamp >= endOfRepurchaseWindow) {
     704 |             revert AfterRepurchaseWindow();
     705 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:731`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     729 | 
     730 |     function _burnCollapseExposureInternal (address borrower, uint256 amountToBurn) internal {
>>>  731 |         if (block.timestamp >= endOfRepurchaseWindow) {
     732 |             revert AfterRepurchaseWindow();
     733 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `TermRepoServicer.sol:798`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     796 |     function _mintOpenExposureInternal(address borrower, address sender, uint256 amount, uint256[] calldata collateralAmounts) internal {
     797 |         // solhint-disable-next-line not-rely-on-time
>>>  798 |         if (block.timestamp > maturityTimestamp) {
     799 |             revert AfterMaturity();
     800 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `facets\ERC4626InterfaceFacet.sol:309`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     307 |         bytes calldata sigData
     308 |     ) external {
>>>  309 |         if (block.timestamp > deadline) {
     310 |             revert ExpiredSignature();
     311 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `facets\SwapRouterFacet.sol:148`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     146 |             );
     147 |             uint256 expiry = IPPrincipalToken(tokenIn).expiry();
>>>  148 |             if (block.timestamp >= expiry) {
     149 |                 (, address market, uint256 netPtIn, uint256 netLpIn, TokenOutput memory output) = abi.decode(data.swapData, (address, address, uint256, uint256, TokenOutput));
     150 |                 if (netPtIn != amountIn) revert InputAmountMismatch();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `facets\TermLoanIntentFacet.sol:454`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     452 |         }
     453 | 
>>>  454 |         if (block.timestamp > servicer.maturityTimestamp()) {
     455 |             revert AfterMaturity();
     456 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `facets\TermLoanIntentHookFacet.sol:218`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     216 |         }
     217 | 
>>>  218 |         if (block.timestamp > servicer.maturityTimestamp()) {
     219 |             revert AfterMaturity();
     220 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `facets\TermRepoTokenIntentFacet.sol:418`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     416 | 
     417 |         uint256 maturityTimestamp = servicer.maturityTimestamp();
>>>  418 |         if (block.timestamp > maturityTimestamp ) {
     419 |             revert AfterMaturity();
     420 |         }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `facets\TermStrategyFacet.sol:457`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     455 |         }
     456 | 
>>>  457 |         if (block.timestamp > servicer.maturityTimestamp()) {
     458 |             revert AfterMaturity();
     459 |         }
```
</details>

---

## Resource Management (19)

### [!] Fixed-Gas Transfer

- **File:** `test\TestInconsistentVault.sol:102`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     100 |         }
     101 |         _burn(owner, actualSharesBurned);
>>>  102 |         IERC20(_asset).transfer(receiver, assets);
     103 |         
     104 |         shares = reportedShares; // Return inconsistent value
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestInconsistentVault.sol:120`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     118 |         _burn(owner, reportedShares);
     119 | 
>>>  120 |         IERC20(_asset).transfer(receiver, assets);
     121 |         emit Withdraw(msg.sender, receiver, owner, assets, reportedShares);
     122 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestLyingVault.sol:103`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     101 |         _burn(owner, shares);
     102 |         uint256 actualAssets = (assets * 90) / 100; // Actually send 10% less
>>>  103 |         IERC20(_asset).transfer(receiver, actualAssets);
     104 |         emit Withdraw(msg.sender, receiver, owner, actualAssets, shares);
     105 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestLyingVault.sol:118`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     116 |         _burn(owner, shares);
     117 |         uint256 actualAssets = (assets * 90) / 100; // Actually send 10% less
>>>  118 |         IERC20(_asset).transfer(receiver, actualAssets);
     119 |         emit Withdraw(msg.sender, receiver, owner, actualAssets, shares);
     120 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockAavePool.sol:171`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     169 |         uint256 sendAmt = overrideWithdrawSend ? withdrawSendAmount : amount;
     170 |         if (sendAmt > 0) {
>>>  171 |             IERC20(asset).transfer(to, sendAmt);
     172 |         }
     173 |         return overrideWithdrawReturn ? withdrawReturnAmount : amount;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockAavePool.sol:180`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     178 |         uint256 sendAmt = overrideBorrowSend ? borrowSendAmount : amount;
     179 |         if (sendAmt > 0) {
>>>  180 |             IERC20(asset).transfer(msg.sender, sendAmt);
     181 |         }
     182 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockFlashLoanAggregator.sol:22`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      20 |         for (uint256 i = 0; i < tokens.length; i++) {
      21 |             startBalances[i] = IERC20(tokens[i]).balanceOf(address(this));
>>>   22 |             IERC20(tokens[i]).transfer(msg.sender, amounts[i]);
      23 |         }
      24 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockMorphoPool.sol:162`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     160 |         address receiver
     161 |     ) external {
>>>  162 |         IERC20(marketParams.collateralToken).transfer(receiver, assets);
     163 |     }
     164 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockMorphoPool.sol:175`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     173 |         assetsBorrowed = overrideBorrowReturn ? borrowReturnAmount : assets;
     174 |         if (assetsBorrowed > 0) {
>>>  175 |             IERC20(marketParams.loanToken).transfer(receiver, assetsBorrowed);
     176 |         }
     177 |         sharesBorrowed = 0;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockStrategy.sol:57`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      55 | 
      56 |         // Transfer asset tokens back to caller
>>>   57 |         IERC20(asset).transfer(msg.sender, proceeds);
      58 |     }
      59 | }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockStrategyFull.sol:72`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      70 |         if (exchangeRate > 0 && consumeAmount > 0) {
      71 |             uint256 proceeds = (consumeAmount * exchangeRate) / 1e18;
>>>   72 |             IERC20(asset).transfer(msg.sender, proceeds);
      73 |         }
      74 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockSwapAggregator.sol:31`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      29 |         address out = tokenOutFor[tokenIn];
      30 |         uint256 amountOut = amountIn * rateFor[tokenIn] / 1e18;
>>>   31 |         IERC20(out).transfer(msg.sender, amountOut);
      32 |     }
      33 | }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockVault.sol:105`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     103 |         }
     104 |         _burn(owner, shares);
>>>  105 |         IERC20(_asset).transfer(receiver, assets);
     106 |         emit Withdraw(msg.sender, receiver, owner, assets, shares);
     107 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestMockVault.sol:119`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     117 |         assets = convertToAssets(shares);
     118 |         _burn(owner, shares);
>>>  119 |         IERC20(_asset).transfer(receiver, assets);
     120 |         emit Withdraw(msg.sender, receiver, owner, assets, shares);
     121 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestPartialConsumeVault.sol:101`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      99 |         }
     100 |         _burn(owner, shares);
>>>  101 |         IERC20(_asset).transfer(receiver, assets);
     102 |         emit Withdraw(msg.sender, receiver, owner, assets, shares);
     103 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestPartialConsumeVault.sol:115`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     113 |         assets = shares;
     114 |         _burn(owner, shares);
>>>  115 |         IERC20(_asset).transfer(receiver, assets);
     116 |         emit Withdraw(msg.sender, receiver, owner, assets, shares);
     117 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestRefundVault.sol:102`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     100 |         }
     101 |         _burn(owner, shares);
>>>  102 |         IERC20(_asset).transfer(receiver, assets);
     103 |         emit Withdraw(msg.sender, receiver, owner, assets, shares);
     104 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestRefundVault.sol:116`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     114 |         assets = shares;
     115 |         _burn(owner, shares);
>>>  116 |         IERC20(_asset).transfer(receiver, assets);
     117 |         emit Withdraw(msg.sender, receiver, owner, assets, shares);
     118 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\TestTermFlashLoanExecutorFacetHelper.sol:56`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      54 |         uint256 mintAmt
      55 |     ) external {
>>>   56 |         if (burnAmt > 0) IERC20(tokenIn).transfer(address(1), burnAmt);
      57 |         if (mintAmt > 0) TestMockRepoTokenFull(tokenOut).mint(address(this), mintAmt);
      58 |     }
```
</details>

---

## Performance (19)

### [~] Unoptimized Loop

- **File:** `facets\DiamondLoupeFacet.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      59 |         uint256 numFacets = ds.facetAddresses.length;
      60 |         facets_ = new Facet[](numFacets);
>>>   61 |         for (uint256 i; i < numFacets; i++) {
      62 |             address facetAddress_ = ds.facetAddresses[i];
      63 |             facets_[i].facetAddress = facetAddress_;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\MulticallFacet.sol:79`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      77 |         bool[] memory successes = new bool[](calls.length);
      78 |         
>>>   79 |         for (uint256 i = 0; i < calls.length; i++) {
      80 |             // Validate the function selector and target facet
      81 |             _validateCall(calls[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\MulticallFacet.sol:124`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     122 |         bool facetEnabled = false;
     123 |         
>>>  124 |         for (uint256 i = 0; i < enabledFacets.length; i++) {
     125 |             if (enabledFacets[i] == facetAddress) {
     126 |                 facetEnabled = true;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\TermLoanIntentFacet.sol:373`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     371 |     function _hashRetrieveFundsArray(RetrieveFundsStruct[] memory items) private pure returns (bytes32) {
     372 |         bytes32[] memory hashes = new bytes32[](items.length);
>>>  373 |         for (uint256 i = 0; i < items.length; i++) {
     374 |             hashes[i] = _hashRetrieveFundsStruct(items[i]);
     375 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\TermLoanIntentHookFacet.sol:243`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     241 | 
     242 |         bool collateralSupported;
>>>  243 |         for (uint256 i = 0; i < numCollateralTokens; i++) {
     244 |             if (collateralManager.collateralTokens(i) == collateralToken) {
     245 |                 collateralAmounts[i] = collateralAmount;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\TermStrategyFacet.sol:474`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     472 | 
     473 |         bool collateralSupported;
>>>  474 |         for (uint256 i = 0; i < numCollateralTokens; i++) {
     475 |             if (collateralManager.collateralTokens(i) == collateralToken) {
     476 |                 collateralAmounts[i] = collateralAmount;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\flashloan\TermFlashLoanCentralReceiverFacet.sol:102`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     100 |             revert ArrayLengthMismatch();
     101 |         }
>>>  102 |         for (uint i = 0; i < assets.length; i++) {
     103 |             if (assets[i] == address(0)) {
     104 |                 revert InvalidAssetAddress();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `facets\flashloan\TermFlashLoanExecutorFacet.sol:297`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     295 |         address actualOutputToken;
     296 | 
>>>  297 |         for (uint256 i = 0; i < executionPlan.actions.length; i++) {
     298 | 
     299 |             // Validate action inputToken
```
</details>

---

### [~] Unoptimized Loop

- **File:** `factory\TermRepoDeployerFactory.sol:555`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     553 |         
     554 |         IERC20[] memory collateralTokens = new IERC20[](collateralManager.numOfAcceptedCollateralTokens());
>>>  555 |         for (uint8 i = 0; i < collateralTokens.length; i++) {
     556 |             collateralTokens[i] = IERC20(collateralManager.collateralTokens(i));
     557 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `factory\TermRepoDeployerFactory.sol:808`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     806 |         address[] memory seen = new address[](params.collateralTokens.length);
     807 |         uint256 j;
>>>  808 |         for (uint256 i = 0; i < params.collateralTokens.length; i++) {
     809 |             address token = params.collateralTokens[i].tokenAddress;
     810 |             for (j = 0; j < i; j++) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `libraries\LibDiamond.sol:147`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     145 |         for (uint256 selectorIndex; selectorIndex < _functionSelectors.length; selectorIndex++) {
     146 |             bytes4 selector = _functionSelectors[selectorIndex];
>>>  147 |             for (uint256 i = 0; i < selectorIndex; i++) {
     148 |                 require(_functionSelectors[i] != selector, "Duplicate function selector");
     149 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestMockCollateralManager.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      11 |     function setCollateralTokens(address[] calldata tokens) external {
      12 |         delete _collateralTokens;
>>>   13 |         for (uint256 i = 0; i < tokens.length; i++) {
      14 |             _collateralTokens.push(tokens[i]);
      15 |             maintenanceCollateralRatios[tokens[i]] = 150e16; // Set a default maintenance ratio of 150% for testing
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestMockFlashLoanAggregator.sol:20`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      18 |         // Record starting balances and transfer flash loan amounts to borrower
      19 |         uint256[] memory startBalances = new uint256[](tokens.length);
>>>   20 |         for (uint256 i = 0; i < tokens.length; i++) {
      21 |             startBalances[i] = IERC20(tokens[i]).balanceOf(address(this));
      22 |             IERC20(tokens[i]).transfer(msg.sender, amounts[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestMockFlashLoanAggregator.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      40 | 
      41 |         // Verify repayment: balance must be restored to at least what it was before
>>>   42 |         for (uint256 i = 0; i < tokens.length; i++) {
      43 |             uint256 endBalance = IERC20(tokens[i]).balanceOf(address(this));
      44 |             if (endBalance < startBalances[i]) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestMockMorphoPool.sol:211`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     209 |     function extSloads(bytes32[] memory slots) external view returns (bytes32[] memory) {
     210 |         bytes32[] memory results = new bytes32[](slots.length);
>>>  211 |         for (uint256 i = 0; i < slots.length; i++) {
     212 |             bytes32 slot = slots[i];
     213 |             bytes32 value;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestMockPermitToken.sol:30`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      28 |         ERC20Upgradeable.__ERC20_init(_name, _symbol);
      29 |         decimals_ = _decimals;
>>>   30 |         for (uint8 i = 0; i < _holder.length; i++) {
      31 |             _mint(_holder[i], amount_[i]);
      32 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestMockRepoServicerFull.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      92 |         ITermRepoCollateralManager collateralMgr = ITermRepoCollateralManager(_collateralManager);
      93 |         uint8 numTokens = collateralMgr.numOfAcceptedCollateralTokens();
>>>   94 |         for (uint8 i = 0; i < numTokens; i++) {
      95 |             address token = collateralMgr.collateralTokens(i);
      96 |             uint256 balance = collateralMgr.getCollateralBalance(borrower, token);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestTermLoanIntentHookFacetHelper.sol:39`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      37 |     ) external {
      38 |         uint256[] memory copy = new uint256[](collateralAmounts.length);
>>>   39 |         for (uint256 i = 0; i < collateralAmounts.length; i++) {
      40 |             copy[i] = collateralAmounts[i];
      41 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\TestToken.sol:19`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      17 |         ERC20Upgradeable.__ERC20_init(_name, _symbol);
      18 |         decimals_ = _decimals;
>>>   19 |         for (uint8 i = 0; i < _holder.length; i++) {
      20 |             _mint(_holder[i], amount_[i]);
      21 |         }
```
</details>

---

## Code Quality (20)

### [~] UNCLEAR require Error Message

- **File:** `TermController.sol:320`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     318 |         address externalContract
     319 |     ) external onlyRole(ADMIN_ROLE) {
>>>  320 |         require(!approvedExternalAddresses[externalContract], "Contract is already approved");
     321 |         approvedExternalAddresses[externalContract] = true;
     322 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `TermController.sol:329`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     327 |         address externalContract
     328 |     ) external onlyRole(ADMIN_ROLE) {
>>>  329 |         require(approvedExternalAddresses[externalContract], "Contract is not approved");
     330 |         delete approvedExternalAddresses[externalContract];
     331 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\WETHWrappingFacet.sol:63`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      61 |         wrappedToken.withdraw(amount);
      62 |         (bool success, ) = payable(msg.sender).call{value: amount}("");
>>>   63 |         require(success, "ETH transfer failed");
      64 |     }
      65 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\base\TermAtomicTxProtection.sol:13`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      11 |     modifier initiateAtomicTxProtection() {
      12 |         TermStorage storage ts = LibTermStorage.termStorage();
>>>   13 |         require(ts.atomicTxInitiatior == UNSET_ATOMIC_TX_INITIATOR, "AtomicTx already initiated");
      14 |         ts.atomicTxInitiatior = msg.sender;
      15 |         _;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\base\TermMulticallProtection.sol:20`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      18 |     modifier initiateMulticallProtection() {
      19 |         TermStorage storage ts = LibTermStorage.termStorage();
>>>   20 |         require(ts.multicallInitiator == UNSET_MULTICALL_INITIATOR, "Multicall already initiated");
      21 |         ts.multicallInitiator = msg.sender;
      22 |         _;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\base\TermMulticallProtection.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      33 |     function _revert(bytes memory returnData) internal pure {
      34 |         uint256 length = returnData.length;
>>>   35 |         require(length > 0, "call reverted");
      36 | 
      37 |         assembly ("memory-safe") {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\external\TermMorphoInterfaceFacet.sol:438`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     436 |         require(marketParams.oracle != address(0), "Invalid oracle address");
     437 |         uint256 collateralPrice = IOracle(marketParams.oracle).price();
>>>  438 |         require(collateralPrice > 0, "Invalid price");
     439 | 
     440 |         uint256 denominator = collateralPrice.mulDivDown(marketParams.lltv, 1e18);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\external\TermMorphoInterfaceFacet.sol:441`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     439 | 
     440 |         uint256 denominator = collateralPrice.mulDivDown(marketParams.lltv, 1e18);
>>>  441 |         require(denominator > 0, "Price*LTV rounds to zero");
     442 | 
     443 |         // Calculate minimum collateral required to maintain LTV
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `facets\external\TermMorphoInterfaceFacet.sol:476`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     474 |         require(marketParams.oracle != address(0), "Invalid oracle address");
     475 |         uint256 collateralPrice = IOracle(marketParams.oracle).price();
>>>  476 |         require(collateralPrice > 0, "Invalid price");
     477 | 
     478 |         uint256 collateralBalance = morpho.position(wrappedMarketId, user).collateral;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\LibDiamond.sol:119`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     117 | 
     118 |     function addFunctions(address _facetAddress, bytes4[] memory _functionSelectors) internal {
>>>  119 |         require(_functionSelectors.length > 0, "LibDiamondCut: No selectors in facet to cut");
     120 |         DiamondStorage storage ds = diamondStorage();        
     121 |         require(_facetAddress != address(0), "LibDiamondCut: Add facet can't be address(0)");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\LibDiamond.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 | 
     136 |     function replaceFunctions(address _facetAddress, bytes4[] memory _functionSelectors) internal {
>>>  137 |         require(_functionSelectors.length > 0, "LibDiamondCut: No selectors in facet to cut");
     138 |         DiamondStorage storage ds = diamondStorage();
     139 |         require(_facetAddress != address(0), "LibDiamondCut: Add facet can't be address(0)");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\LibDiamond.sol:148`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     146 |             bytes4 selector = _functionSelectors[selectorIndex];
     147 |             for (uint256 i = 0; i < selectorIndex; i++) {
>>>  148 |                 require(_functionSelectors[i] != selector, "Duplicate function selector");
     149 |             }
     150 |             address oldFacetAddress = ds.selectorToFacetAndPosition[selector].facetAddress;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\LibDiamond.sol:159`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     157 | 
     158 |     function removeFunctions(address _facetAddress, bytes4[] memory _functionSelectors) internal {
>>>  159 |         require(_functionSelectors.length > 0, "LibDiamondCut: No selectors in facet to cut");
     160 |         DiamondStorage storage ds = diamondStorage();
     161 |         // if function does not exist then do nothing and return
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\LibTermStorage.sol:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      93 |         TermStorage storage ts = termStorage();
      94 |         address initiator = ts.multicallInitiator;
>>>   95 |         require(initiator != UNSET_INITIATOR, "uninitialized");
      96 |         require(msg.sender == initiator, "unauthorized");
      97 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `libraries\LibTermStorage.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 |         address initiator = ts.multicallInitiator;
      95 |         require(initiator != UNSET_INITIATOR, "uninitialized");
>>>   96 |         require(msg.sender == initiator, "unauthorized");
      97 |     }
      98 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\TestMockWETH.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      31 | 
      32 |     function withdraw(uint256 wad) public {
>>>   33 |         require(!shouldRevertOnWithdraw, "MockWETH: withdraw reverted");
      34 |         require(balanceOf[msg.sender] >= wad, "MockWETH: insufficient balance");
      35 |         balanceOf[msg.sender] -= wad;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\TestMockWETH.sol:34`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      32 |     function withdraw(uint256 wad) public {
      33 |         require(!shouldRevertOnWithdraw, "MockWETH: withdraw reverted");
>>>   34 |         require(balanceOf[msg.sender] >= wad, "MockWETH: insufficient balance");
      35 |         balanceOf[msg.sender] -= wad;
      36 |         totalSupply -= wad;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\TestMockWETH.sol:38`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      36 |         totalSupply -= wad;
      37 |         (bool success, ) = payable(msg.sender).call{value: wad}("");
>>>   38 |         require(success, "MockWETH: ETH transfer failed");
      39 |         emit Withdrawal(msg.sender, wad);
      40 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\TestMockWETH.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |         uint256 amount
      58 |     ) external override returns (bool) {
>>>   59 |         require(balanceOf[msg.sender] >= amount, "MockWETH: insufficient balance");
      60 |         balanceOf[msg.sender] -= amount;
      61 |         balanceOf[to] += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\TestMockWETH.sol:71`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      69 |         uint256 amount
      70 |     ) external override returns (bool) {
>>>   71 |         require(balanceOf[from] >= amount, "MockWETH: insufficient balance");
      72 |         if (allowance[from][msg.sender] != type(uint256).max) {
      73 |             require(
```
</details>

---


---
*Generated by BugHunter*