# BugHunter Report: contracts

**Generated:** 2026-09-05 02:21:53
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\merkl\contracts`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 42 |
| Total lines | 4,669 |
| Bugs found | 13 |
| !!! Critical | 4 |
| ! Medium | 9 |

### Languages Detected

- **solidity**: 42 files

## Security (4)

### [!!!] tx.origin For Authorization

- **File:** `DistributionCreator.sol:154`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
     152 | 
     153 |     /// @notice Ensures the caller has accepted the current terms or is whitelisted for this
>>>  154 |     /// @dev Checks both msg.sender and tx.origin for signature or whitelist status
     155 |     modifier hasSigned() {
     156 |         if (
```
</details>

---

### [!!!] tx.origin For Authorization

- **File:** `DistributionCreator.sol:158`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
     156 |         if (
     157 |             userSignatureWhitelist[msg.sender] == 0 &&
>>>  158 |             userSignatureWhitelist[tx.origin] == 0 &&
     159 |             userSignatures[msg.sender] != messageHash &&
     160 |             userSignatures[tx.origin] != messageHash
```
</details>

---

### [!!!] tx.origin For Authorization

- **File:** `DistributionCreator.sol:160`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
     158 |             userSignatureWhitelist[tx.origin] == 0 &&
     159 |             userSignatures[msg.sender] != messageHash &&
>>>  160 |             userSignatures[tx.origin] != messageHash
     161 |         ) revert Errors.NotSigned();
     162 |         _;
```
</details>

---

### [!!!] tx.origin For Authorization

- **File:** `Distributor.sol:448`
- **Severity:** CRITICAL
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using tx.origin for authorization is a vulnerability. A phishing attack can authorize transactions from the victim's account.

**Fix:** Use msg.sender instead of tx.origin for authorization checks.

<details>
<summary>Code</summary>

```
     446 |             if (
     447 |                 msg.sender != user &&
>>>  448 |                 tx.origin != user &&
     449 |                 mainOperators[msg.sender][token] == 0 &&
     450 |                 mainOperators[msg.sender][address(0)] == 0 &&
```
</details>

---

## Logic (6)

### [!] Timestamp Dependence

- **File:** `DistributionCreator.sol:252`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     250 |         newCampaign.rewardToken = _campaign.rewardToken; // Reward token cannot be changed
     251 |         if (
>>>  252 |             (newCampaign.startTimestamp != _campaign.startTimestamp && block.timestamp > _campaign.startTimestamp) || // Allow to update startTimestamp before campaign start
     253 |             newCampaign.amount * HOUR < rewardTokenMinAmounts[newCampaign.rewardToken] * newCampaign.duration
     254 |         ) revert Errors.InvalidOverride();
```
</details>

---

### [!] Timestamp Dependence

- **File:** `DistributionCreator.sol:272`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     270 |         _isSenderValidOperatorForCampaign(_campaign.creator);
     271 |         // Check campaign end time using the overridden parameters if they exist
>>>  272 |         if (block.timestamp < _campaign.startTimestamp + _campaign.duration) revert Errors.InvalidReallocation();
     273 |         if (to == address(0)) revert Errors.ZeroAddress();
     274 | 
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Distributor.sol:227`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     225 |     /// @dev Returns tree.merkleRoot if dispute period has passed and no active dispute
     226 |     function getMerkleRoot() public view returns (bytes32) {
>>>  227 |         if (block.timestamp >= endOfDisputePeriod && disputer == address(0)) return tree.merkleRoot;
     228 |         else return lastTree.merkleRoot;
     229 |     }
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Distributor.sol:285`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     283 |     function disputeTree(string memory reason) external {
     284 |         if (disputer != address(0)) revert Errors.UnresolvedDispute();
>>>  285 |         if (block.timestamp >= endOfDisputePeriod) revert Errors.InvalidDispute();
     286 |         IERC20(disputeToken).safeTransferFrom(msg.sender, address(this), disputeAmount);
     287 |         disputer = msg.sender;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `Distributor.sol:305`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
     303 |             // A trusted address cannot update a tree right after a precedent tree update otherwise it can de facto
     304 |             // validate a tree which has not passed the dispute period
>>>  305 |             ((canUpdateMerkleRoot[msg.sender] != 1 || block.timestamp < endOfDisputePeriod) && !accessControlManager.isGovernor(msg.sender))
     306 |         ) revert Errors.NotTrusted();
     307 |         MerkleTree memory _lastTree = tree;
```
</details>

---

### [!] Timestamp Dependence

- **File:** `partners\tokenWrappers\TokenTGEWrapper.sol:37`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.timestamp for critical logic (lotteries, randomness). Miners can manipulate timestamps within a range.

**Fix:** Avoid relying on block.timestamp for randomness or critical timing decisions.

<details>
<summary>Code</summary>

```
      35 |     /// @notice On claim: checks unlock timestamp, then sends underlying to the claimer
      36 |     function _onClaim(address to, uint256 amount) internal override {
>>>   37 |         if (block.timestamp < unlockTimestamp) revert Errors.NotAllowed();
      38 |         IERC20(token).safeTransfer(to, amount);
      39 |     }
```
</details>

---

## Resource Management (3)

### [!] Fixed-Gas Transfer

- **File:** `Disputer.sol:69`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      67 |     /// @param amount Amount to withdraw
      68 |     function withdrawFunds(address asset, address to, uint256 amount) external onlyOwner {
>>>   69 |         IERC20(asset).transfer(to, amount);
      70 |     }
      71 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `mock\weth.sol:103`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     101 |         require(_balanceOf[msg.sender] >= wad);
     102 |         _balanceOf[msg.sender] -= wad;
>>>  103 |         payable(msg.sender).transfer(wad);
     104 |         emit Withdrawal(msg.sender, wad);
     105 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `mock\weth9.sol:42`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      40 |         require(balanceOf[msg.sender] >= wad);
      41 |         balanceOf[msg.sender] -= wad;
>>>   42 |         payable(msg.sender).transfer(wad);
      43 |         emit Withdrawal(msg.sender, wad);
      44 |     }
```
</details>

---


---
*Generated by BugHunter*