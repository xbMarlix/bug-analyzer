# BugHunter Report: axionova

**Generated:** 2026-09-08 20:04:27
**Project:** `C:\Users\123123\AppData\Local\Temp\opencode\axionova`
**Analyzers:** static, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 13 |
| Total lines | 3,761 |
| Bugs found | 154 |
| ~ Low | 154 |

### Languages Detected

- **solidity**: 13 files

## Performance (12)

### [~] Unoptimized Loop

- **File:** `contracts\AXNVAirdrop.sol:293`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     291 |         if (length == 0) revert InvalidArrayLength();
     292 | 
>>>  293 |         for (uint256 i = 0; i < length; i++) {
     294 |             address user = users[i];
     295 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVAirdrop.sol:310`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     308 |         if (length == 0) revert InvalidArrayLength();
     309 | 
>>>  310 |         for (uint256 i = 0; i < length; i++) {
     311 |             address user = users[i];
     312 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVBatchDistributor.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      50 |         uint256 totalAmount;
      51 | 
>>>   52 |         for (uint256 i = 0; i < length; i++) {
      53 |             require(recipients[i] != address(0), "Invalid recipient");
      54 |             require(amounts[i] > 0, "Zero amount");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVBatchDistributor.sol:66`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      64 |         totalDistributed += totalAmount;
      65 | 
>>>   66 |         for (uint256 i = 0; i < length; i++) {
      67 |             axnv.safeTransfer(recipients[i], amounts[i]);
      68 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:139`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     137 |         uint256 totalAmount;
     138 | 
>>>  139 |         for (uint256 i = 0; i < wallets.length; i++) {
     140 |             address wallet = wallets[i];
     141 |             uint256 amount = amounts[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:226`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     224 |         uint256 totalAmount;
     225 | 
>>>  226 |         for (uint256 i = 0; i < campaignIds.length; i++) {
     227 |             uint256 campaignId = campaignIds[i];
     228 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:158`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     156 |         require(startTimes.length == length, "Length mismatch");
     157 | 
>>>  158 |         for (uint256 i = 0; i < length; i++) {
     159 |             _createSchedule(
     160 |                 categories[i],
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:277`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     275 |         uint256 totalAmount;
     276 | 
>>>  277 |         for (uint256 i = 0; i < scheduleIds.length; i++) {
     278 |             uint256 scheduleId = scheduleIds[i];
     279 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:406`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     404 |         scheduleCount = ids.length;
     405 | 
>>>  406 |         for (uint256 i = 0; i < ids.length; i++) {
     407 |             VestingSchedule memory s = schedules[ids[i]];
     408 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:547`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     545 |         uint256[] storage ids = beneficiaryScheduleIds[beneficiary];
     546 | 
>>>  547 |         for (uint256 i = 0; i < ids.length; i++) {
     548 |             if (ids[i] == scheduleId) {
     549 |                 ids[i] = ids[ids.length - 1];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVTreasury.sol:122`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     120 |         uint256 batchTotal;
     121 | 
>>>  122 |         for (uint256 i = 0; i < length; i++) {
     123 |             uint8 category = categories[i];
     124 |             address to = recipients[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `contracts\AXNVTreasury.sol:157`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     155 |         totalSpent += batchTotal;
     156 | 
>>>  157 |         for (uint256 i = 0; i < length; i++) {
     158 |             axnv.safeTransfer(recipients[i], amounts[i]);
     159 | 
```
</details>

---

## Code Quality (142)

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVBatchDistributor.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      45 |         uint256 length = recipients.length;
      46 | 
>>>   47 |         require(length > 0, "Empty recipients");
      48 |         require(length == amounts.length, "Length mismatch");
      49 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVBatchDistributor.sol:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      46 | 
      47 |         require(length > 0, "Empty recipients");
>>>   48 |         require(length == amounts.length, "Length mismatch");
      49 | 
      50 |         uint256 totalAmount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVBatchDistributor.sol:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      52 |         for (uint256 i = 0; i < length; i++) {
      53 |             require(recipients[i] != address(0), "Invalid recipient");
>>>   54 |             require(amounts[i] > 0, "Zero amount");
      55 | 
      56 |             totalAmount += amounts[i];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVBatchDistributor.sol:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      79 |     {
      80 |         require(to != address(0), "Invalid recipient");
>>>   81 |         require(amount > 0, "Zero amount");
      82 |         require(amount <= axnv.balanceOf(address(this)), "Insufficient AXNV");
      83 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVBatchDistributor.sol:97`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      95 |         require(token != address(0), "Invalid token");
      96 |         require(to != address(0), "Invalid recipient");
>>>   97 |         require(amount > 0, "Zero amount");
      98 | 
      99 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 | 
      58 |     function fundVault(uint256 amount) external onlyOwner nonReentrant {
>>>   59 |         require(amount > 0, "Zero amount");
      60 |         require(accountedAXNV() + amount <= COMMUNITY_INCENTIVES_CAP, "Cap exceeded");
      61 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:70`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      68 |     function createCampaign(string calldata name, uint256 allocation) external onlyOwner returns (uint256 campaignId) {
      69 |         require(bytes(name).length > 0, "Empty name");
>>>   70 |         require(allocation > 0, "Zero allocation");
      71 |         require(totalCampaignAllocated + allocation <= COMMUNITY_INCENTIVES_CAP, "Cap exceeded");
      72 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:71`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      69 |         require(bytes(name).length > 0, "Empty name");
      70 |         require(allocation > 0, "Zero allocation");
>>>   71 |         require(totalCampaignAllocated + allocation <= COMMUNITY_INCENTIVES_CAP, "Cap exceeded");
      72 | 
      73 |         campaignId = campaigns.length;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:90`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      88 | 
      89 |     function decreaseCampaignAllocation(uint256 campaignId, uint256 newAllocation) external onlyOwner {
>>>   90 |         require(campaignId < campaigns.length, "Invalid campaign");
      91 | 
      92 |         Campaign storage c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:93`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      91 | 
      92 |         Campaign storage c = campaigns[campaignId];
>>>   93 |         require(c.exists, "Campaign missing");
      94 |         require(newAllocation > 0, "Zero allocation");
      95 |         require(newAllocation < c.allocation, "Not decreased");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:94`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      92 |         Campaign storage c = campaigns[campaignId];
      93 |         require(c.exists, "Campaign missing");
>>>   94 |         require(newAllocation > 0, "Zero allocation");
      95 |         require(newAllocation < c.allocation, "Not decreased");
      96 |         require(newAllocation >= c.assigned, "Below assigned");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      93 |         require(c.exists, "Campaign missing");
      94 |         require(newAllocation > 0, "Zero allocation");
>>>   95 |         require(newAllocation < c.allocation, "Not decreased");
      96 |         require(newAllocation >= c.assigned, "Below assigned");
      97 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 |         require(newAllocation > 0, "Zero allocation");
      95 |         require(newAllocation < c.allocation, "Not decreased");
>>>   96 |         require(newAllocation >= c.assigned, "Below assigned");
      97 | 
      98 |         uint256 oldAllocation = c.allocation;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:108`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     106 | 
     107 |     function removeCampaign(uint256 campaignId) external onlyOwner {
>>>  108 |         require(campaignId < campaigns.length, "Invalid campaign");
     109 | 
     110 |         Campaign storage c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:111`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     109 | 
     110 |         Campaign storage c = campaigns[campaignId];
>>>  111 |         require(c.exists, "Campaign missing");
     112 |         require(c.assigned == 0, "Campaign has assigned rewards");
     113 |         require(c.claimed == 0, "Campaign has claimed rewards");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     110 |         Campaign storage c = campaigns[campaignId];
     111 |         require(c.exists, "Campaign missing");
>>>  112 |         require(c.assigned == 0, "Campaign has assigned rewards");
     113 |         require(c.claimed == 0, "Campaign has claimed rewards");
     114 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:113`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     111 |         require(c.exists, "Campaign missing");
     112 |         require(c.assigned == 0, "Campaign has assigned rewards");
>>>  113 |         require(c.claimed == 0, "Campaign has claimed rewards");
     114 | 
     115 |         uint256 allocation = c.allocation;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:130`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     128 |         uint256[] calldata amounts
     129 |     ) external onlyOwner {
>>>  130 |         require(campaignId < campaigns.length, "Invalid campaign");
     131 |         require(wallets.length == amounts.length, "Length mismatch");
     132 |         require(wallets.length > 0, "Empty batch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:131`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     129 |     ) external onlyOwner {
     130 |         require(campaignId < campaigns.length, "Invalid campaign");
>>>  131 |         require(wallets.length == amounts.length, "Length mismatch");
     132 |         require(wallets.length > 0, "Empty batch");
     133 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:132`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     130 |         require(campaignId < campaigns.length, "Invalid campaign");
     131 |         require(wallets.length == amounts.length, "Length mismatch");
>>>  132 |         require(wallets.length > 0, "Empty batch");
     133 | 
     134 |         Campaign storage c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:135`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     133 | 
     134 |         Campaign storage c = campaigns[campaignId];
>>>  135 |         require(c.exists, "Campaign missing");
     136 | 
     137 |         uint256 totalAmount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:144`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     142 | 
     143 |             require(wallet != address(0), "Invalid wallet");
>>>  144 |             require(amount > 0, "Zero amount");
     145 |             require(!claimed[campaignId][wallet], "Already claimed");
     146 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:145`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     143 |             require(wallet != address(0), "Invalid wallet");
     144 |             require(amount > 0, "Zero amount");
>>>  145 |             require(!claimed[campaignId][wallet], "Already claimed");
     146 | 
     147 |             rewards[campaignId][wallet] += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:151`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     149 |         }
     150 | 
>>>  151 |         require(c.assigned + totalAmount <= c.allocation, "Campaign allocation exceeded");
     152 | 
     153 |         c.assigned += totalAmount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:160`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     158 | 
     159 |     function setCampaignActive(uint256 campaignId, bool active) external onlyOwner {
>>>  160 |         require(campaignId < campaigns.length, "Invalid campaign");
     161 | 
     162 |         Campaign storage c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:163`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     161 | 
     162 |         Campaign storage c = campaigns[campaignId];
>>>  163 |         require(c.exists, "Campaign missing");
     164 | 
     165 |         c.active = active;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:177`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     175 |     function recoverUnallocatedAXNV(uint256 amount, address to) external onlyOwner nonReentrant {
     176 |         require(to != address(0), "Invalid recipient");
>>>  177 |         require(amount > 0, "Zero amount");
     178 | 
     179 |         uint256 available = unallocatedAXNV();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:180`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     178 | 
     179 |         uint256 available = unallocatedAXNV();
>>>  180 |         require(amount <= available, "Exceeds unallocated");
     181 | 
     182 |         axnv.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:191`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     189 |         require(token != address(0), "Invalid token");
     190 |         require(to != address(0), "Invalid recipient");
>>>  191 |         require(amount > 0, "Zero amount");
     192 | 
     193 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:199`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     197 | 
     198 |     function claim(uint256 campaignId) external nonReentrant {
>>>  199 |         require(!claimsPaused, "Claims paused");
     200 |         require(campaignId < campaigns.length, "Invalid campaign");
     201 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:200`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     198 |     function claim(uint256 campaignId) external nonReentrant {
     199 |         require(!claimsPaused, "Claims paused");
>>>  200 |         require(campaignId < campaigns.length, "Invalid campaign");
     201 | 
     202 |         Campaign storage c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:203`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     201 | 
     202 |         Campaign storage c = campaigns[campaignId];
>>>  203 |         require(c.exists, "Campaign missing");
     204 |         require(c.active, "Campaign inactive");
     205 |         require(!claimed[campaignId][msg.sender], "Already claimed");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:204`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     202 |         Campaign storage c = campaigns[campaignId];
     203 |         require(c.exists, "Campaign missing");
>>>  204 |         require(c.active, "Campaign inactive");
     205 |         require(!claimed[campaignId][msg.sender], "Already claimed");
     206 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:205`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     203 |         require(c.exists, "Campaign missing");
     204 |         require(c.active, "Campaign inactive");
>>>  205 |         require(!claimed[campaignId][msg.sender], "Already claimed");
     206 | 
     207 |         uint256 amount = rewards[campaignId][msg.sender];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:208`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     206 | 
     207 |         uint256 amount = rewards[campaignId][msg.sender];
>>>  208 |         require(amount > 0, "Nothing claimable");
     209 | 
     210 |         claimed[campaignId][msg.sender] = true;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:221`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     219 | 
     220 |     function claimMany(uint256[] calldata campaignIds) external nonReentrant {
>>>  221 |         require(!claimsPaused, "Claims paused");
     222 |         require(campaignIds.length > 0, "Empty array");
     223 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:222`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     220 |     function claimMany(uint256[] calldata campaignIds) external nonReentrant {
     221 |         require(!claimsPaused, "Claims paused");
>>>  222 |         require(campaignIds.length > 0, "Empty array");
     223 | 
     224 |         uint256 totalAmount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:229`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     227 |             uint256 campaignId = campaignIds[i];
     228 | 
>>>  229 |             require(campaignId < campaigns.length, "Invalid campaign");
     230 | 
     231 |             Campaign storage c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:232`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     230 | 
     231 |             Campaign storage c = campaigns[campaignId];
>>>  232 |             require(c.exists, "Campaign missing");
     233 |             require(c.active, "Campaign inactive");
     234 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:233`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     231 |             Campaign storage c = campaigns[campaignId];
     232 |             require(c.exists, "Campaign missing");
>>>  233 |             require(c.active, "Campaign inactive");
     234 | 
     235 |             if (claimed[campaignId][msg.sender]) continue;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:249`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     247 |         }
     248 | 
>>>  249 |         require(totalAmount > 0, "Nothing claimable");
     250 | 
     251 |         axnv.safeTransfer(msg.sender, totalAmount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:268`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     266 |         )
     267 |     {
>>>  268 |         require(campaignId < campaigns.length, "Invalid campaign");
     269 | 
     270 |         Campaign memory c = campaigns[campaignId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVCommunityIncentivesDistributor.sol:291`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     289 |         )
     290 |     {
>>>  291 |         require(campaignId < campaigns.length, "Invalid campaign");
     292 | 
     293 |         assignedAmount = rewards[campaignId][user];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      40 | 
      41 |     function fundVault(uint256 amount) external onlyOwner nonReentrant {
>>>   42 |         require(amount > 0, "Zero amount");
      43 | 
      44 |         uint256 newAccounted = accountedAXNV() + amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:45`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      43 | 
      44 |         uint256 newAccounted = accountedAXNV() + amount;
>>>   45 |         require(newAccounted <= LIQUIDITY_ALLOCATION_CAP, "Cap exceeded");
      46 | 
      47 |         axnv.safeTransferFrom(msg.sender, address(this), amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:57`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      55 |         nonReentrant
      56 |     {
>>>   57 |         require(!releasePaused, "Release paused");
      58 |         require(amount > 0, "Zero amount");
      59 |         require(totalReleased + amount <= LIQUIDITY_ALLOCATION_CAP, "Cap exceeded");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      56 |     {
      57 |         require(!releasePaused, "Release paused");
>>>   58 |         require(amount > 0, "Zero amount");
      59 |         require(totalReleased + amount <= LIQUIDITY_ALLOCATION_CAP, "Cap exceeded");
      60 |         require(amount <= contractAXNVBalance(), "Insufficient AXNV");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      57 |         require(!releasePaused, "Release paused");
      58 |         require(amount > 0, "Zero amount");
>>>   59 |         require(totalReleased + amount <= LIQUIDITY_ALLOCATION_CAP, "Cap exceeded");
      60 |         require(amount <= contractAXNVBalance(), "Insufficient AXNV");
      61 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      79 |     {
      80 |         require(to != address(0), "Invalid recipient");
>>>   81 |         require(amount > 0, "Zero amount");
      82 | 
      83 |         uint256 excess = excessAXNV();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:84`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      82 | 
      83 |         uint256 excess = excessAXNV();
>>>   84 |         require(amount <= excess, "Exceeds excess");
      85 | 
      86 |         axnv.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVLiquidityAllocationVault.sol:99`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      97 |         require(token != address(0), "Invalid token");
      98 |         require(to != address(0), "Invalid recipient");
>>>   99 |         require(amount > 0, "Zero amount");
     100 | 
     101 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 | 
     108 |     function buy(uint256 usdtAmount) external nonReentrant whenNotPaused {
>>>  109 |         require(presaleActive, "Presale is not active");
     110 |         require(!saleEnded, "Sale has ended");
     111 |         require(usdtAmount > 0, "Invalid USDT amount");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:110`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     108 |     function buy(uint256 usdtAmount) external nonReentrant whenNotPaused {
     109 |         require(presaleActive, "Presale is not active");
>>>  110 |         require(!saleEnded, "Sale has ended");
     111 |         require(usdtAmount > 0, "Invalid USDT amount");
     112 |         require(totalAXNVSold < PRESALE_SUPPLY, "Sold out");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:111`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     109 |         require(presaleActive, "Presale is not active");
     110 |         require(!saleEnded, "Sale has ended");
>>>  111 |         require(usdtAmount > 0, "Invalid USDT amount");
     112 |         require(totalAXNVSold < PRESALE_SUPPLY, "Sold out");
     113 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     110 |         require(!saleEnded, "Sale has ended");
     111 |         require(usdtAmount > 0, "Invalid USDT amount");
>>>  112 |         require(totalAXNVSold < PRESALE_SUPPLY, "Sold out");
     113 | 
     114 |         if (tgeTimestamp != 0) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:115`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     113 | 
     114 |         if (tgeTimestamp != 0) {
>>>  115 |             require(block.timestamp < tgeTimestamp, "Buying after TGE disabled");
     116 |         }
     117 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:166`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     164 |         }
     165 | 
>>>  166 |         require(totalAXNVToBuy > 0, "AXNV amount is zero");
     167 |         require(
     168 |             totalAXNVSold + totalAXNVToBuy <= PRESALE_SUPPLY,
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:173`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     171 | 
     172 |         uint256 usdtActuallyUsed = usdtAmount - remainingUSDT;
>>>  173 |         require(usdtActuallyUsed > 0, "No USDT used");
     174 | 
     175 |         require(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:219`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     217 |         returns (uint256)
     218 |     {
>>>  219 |         require(axnvAmount > 0, "Invalid AXNV amount");
     220 | 
     221 |         uint256 remainingAXNV = axnvAmount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:245`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     243 |         }
     244 | 
>>>  245 |         require(remainingAXNV == 0, "Not enough AXNV left");
     246 | 
     247 |         return totalUSDT;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:298`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     296 | 
     297 |     function claim() external nonReentrant whenNotPaused {
>>>  298 |         require(tgeTimestamp != 0, "TGE is not set");
     299 |         require(block.timestamp >= tgeTimestamp, "TGE has not started");
     300 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:299`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     297 |     function claim() external nonReentrant whenNotPaused {
     298 |         require(tgeTimestamp != 0, "TGE is not set");
>>>  299 |         require(block.timestamp >= tgeTimestamp, "TGE has not started");
     300 | 
     301 |         uint256 amount = claimableAmount(msg.sender);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:302`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     300 | 
     301 |         uint256 amount = claimableAmount(msg.sender);
>>>  302 |         require(amount > 0, "Nothing to claim");
     303 | 
     304 |         BuyerInfo storage buyer = buyers[msg.sender];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:515`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     513 | 
     514 |     function startSale() external onlyOwner {
>>>  515 |         require(!saleEnded, "Sale already ended");
     516 |         require(!presaleActive, "Sale already active");
     517 |         require(totalAXNVSold < PRESALE_SUPPLY, "Sold out");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:516`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     514 |     function startSale() external onlyOwner {
     515 |         require(!saleEnded, "Sale already ended");
>>>  516 |         require(!presaleActive, "Sale already active");
     517 |         require(totalAXNVSold < PRESALE_SUPPLY, "Sold out");
     518 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:517`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     515 |         require(!saleEnded, "Sale already ended");
     516 |         require(!presaleActive, "Sale already active");
>>>  517 |         require(totalAXNVSold < PRESALE_SUPPLY, "Sold out");
     518 | 
     519 |         presaleActive = true;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:525`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     523 | 
     524 |     function stopSale() external onlyOwner {
>>>  525 |         require(presaleActive, "Sale not active");
     526 | 
     527 |         presaleActive = false;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:540`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     538 | 
     539 |     function setTGE(uint256 newTgeTimestamp) external onlyOwner {
>>>  540 |         require(newTgeTimestamp > 0, "Invalid TGE timestamp");
     541 | 
     542 |         if (tgeTimestamp != 0) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:543`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     541 | 
     542 |         if (tgeTimestamp != 0) {
>>>  543 |             require(block.timestamp < tgeTimestamp, "TGE already started");
     544 |         }
     545 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:571`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     569 |     {
     570 |         require(to != address(0), "Invalid receiver");
>>>  571 |         require(amount > 0, "Invalid amount");
     572 | 
     573 |         USDT.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:582`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     580 | 
     581 |         uint256 amount = USDT.balanceOf(address(this));
>>>  582 |         require(amount > 0, "No USDT to withdraw");
     583 | 
     584 |         USDT.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:595`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     593 |     {
     594 |         require(to != address(0), "Invalid receiver");
>>>  595 |         require(amount > 0, "Invalid amount");
     596 | 
     597 |         uint256 available = availableAXNVBalance();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:598`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     596 | 
     597 |         uint256 available = availableAXNVBalance();
>>>  598 |         require(amount <= available, "Amount exceeds unreserved AXNV");
     599 | 
     600 |         AXNV.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:613`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     611 | 
     612 |         uint256 amount = availableAXNVBalance();
>>>  613 |         require(amount > 0, "No unsold AXNV");
     614 | 
     615 |         AXNV.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:625`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     623 |         nonReentrant
     624 |     {
>>>  625 |         require(token != AXNV_ADDRESS, "Use withdrawUnsoldAXNV");
     626 |         require(token != USDT_ADDRESS, "Use withdrawUSDT");
     627 |         require(to != address(0), "Invalid receiver");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:626`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     624 |     {
     625 |         require(token != AXNV_ADDRESS, "Use withdrawUnsoldAXNV");
>>>  626 |         require(token != USDT_ADDRESS, "Use withdrawUSDT");
     627 |         require(to != address(0), "Invalid receiver");
     628 |         require(amount > 0, "Invalid amount");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVPresaleVesting.sol:628`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     626 |         require(token != USDT_ADDRESS, "Use withdrawUSDT");
     627 |         require(to != address(0), "Invalid receiver");
>>>  628 |         require(amount > 0, "Invalid amount");
     629 | 
     630 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVReserveVault.sol:33`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      31 | 
      32 |     function fundVault(uint256 amount) external onlyOwner nonReentrant {
>>>   33 |         require(amount > 0, "Zero amount");
      34 | 
      35 |         totalFunded += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVReserveVault.sol:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      46 |     ) external onlyOwner nonReentrant {
      47 |         require(to != address(0), "Invalid recipient");
>>>   48 |         require(amount > 0, "Zero amount");
      49 |         require(amount <= axnv.balanceOf(address(this)), "Insufficient AXNV");
      50 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVReserveVault.sol:65`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      63 | 
      64 |         uint256 balance = axnv.balanceOf(address(this));
>>>   65 |         require(balance > 0, "No AXNV");
      66 | 
      67 |         totalReleased += balance;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVReserveVault.sol:82`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      80 |         require(token != address(0), "Invalid token");
      81 |         require(to != address(0), "Invalid recipient");
>>>   82 |         require(amount > 0, "Zero amount");
      83 | 
      84 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:85`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      83 | 
      84 |     function stake(uint256 amount) external nonReentrant whenNotPaused {
>>>   85 |         require(amount >= minStake, "Below minimum stake");
      86 | 
      87 |         axnv.safeTransferFrom(msg.sender, address(this), amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 | 
     108 |     function claimReward(uint256 stakeId) public nonReentrant whenNotPaused {
>>>  109 |         require(stakeId < stakes.length, "Invalid stake");
     110 | 
     111 |         StakeInfo storage s = stakes[stakeId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:113`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     111 |         StakeInfo storage s = stakes[stakeId];
     112 | 
>>>  113 |         require(s.user == msg.sender, "Not stake owner");
     114 |         require(!s.withdrawn, "Stake withdrawn");
     115 |         require(block.timestamp >= s.startTime + SIX_MONTHS, "Reward locked");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:114`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     112 | 
     113 |         require(s.user == msg.sender, "Not stake owner");
>>>  114 |         require(!s.withdrawn, "Stake withdrawn");
     115 |         require(block.timestamp >= s.startTime + SIX_MONTHS, "Reward locked");
     116 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:115`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     113 |         require(s.user == msg.sender, "Not stake owner");
     114 |         require(!s.withdrawn, "Stake withdrawn");
>>>  115 |         require(block.timestamp >= s.startTime + SIX_MONTHS, "Reward locked");
     116 | 
     117 |         uint256 reward = claimableReward(stakeId);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:119`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     117 |         uint256 reward = claimableReward(stakeId);
     118 | 
>>>  119 |         require(reward > 0, "Nothing claimable");
     120 |         require(availableRewardPool() >= reward, "Insufficient reward pool");
     121 |         require(totalRewardsPaid + reward <= STAKING_REWARD_CAP, "Reward cap exceeded");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:121`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     119 |         require(reward > 0, "Nothing claimable");
     120 |         require(availableRewardPool() >= reward, "Insufficient reward pool");
>>>  121 |         require(totalRewardsPaid + reward <= STAKING_REWARD_CAP, "Reward cap exceeded");
     122 | 
     123 |         s.rewardClaimed += reward;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:132`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     130 | 
     131 |     function withdraw(uint256 stakeId) external nonReentrant whenNotPaused {
>>>  132 |         require(stakeId < stakes.length, "Invalid stake");
     133 | 
     134 |         StakeInfo storage s = stakes[stakeId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:136`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     134 |         StakeInfo storage s = stakes[stakeId];
     135 | 
>>>  136 |         require(s.user == msg.sender, "Not stake owner");
     137 |         require(!s.withdrawn, "Already withdrawn");
     138 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:137`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     135 | 
     136 |         require(s.user == msg.sender, "Not stake owner");
>>>  137 |         require(!s.withdrawn, "Already withdrawn");
     138 | 
     139 |         uint256 elapsed = block.timestamp - s.startTime;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:191`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     189 | 
     190 |     function accruedReward(uint256 stakeId) public view returns (uint256) {
>>>  191 |         require(stakeId < stakes.length, "Invalid stake");
     192 | 
     193 |         StakeInfo memory s = stakes[stakeId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:218`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     216 | 
     217 |     function claimableReward(uint256 stakeId) public view returns (uint256) {
>>>  218 |         require(stakeId < stakes.length, "Invalid stake");
     219 | 
     220 |         StakeInfo memory s = stakes[stakeId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:244`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     242 |         nonReentrant
     243 |     {
>>>  244 |         require(amount > 0, "Zero amount");
     245 |         require(
     246 |             totalRewardPoolFunded + amount <= STAKING_REWARD_CAP,
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:261`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     259 |         onlyOwner
     260 |     {
>>>  261 |         require(newMinStake > 0, "Invalid min stake");
     262 | 
     263 |         uint256 oldMinStake = minStake;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:284`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     282 |         require(paused(), "Pause first");
     283 |         require(to != address(0), "Invalid receiver");
>>>  284 |         require(amount > 0, "Zero amount");
     285 | 
     286 |         uint256 available = unallocatedAXNV();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:288`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     286 |         uint256 available = unallocatedAXNV();
     287 | 
>>>  288 |         require(amount <= available, "Exceeds unallocated AXNV");
     289 | 
     290 |         axnv.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:303`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     301 |         require(token != address(0), "Invalid token");
     302 |         require(to != address(0), "Invalid receiver");
>>>  303 |         require(amount > 0, "Zero amount");
     304 | 
     305 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVStaking.sol:382`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     380 |         )
     381 |     {
>>>  382 |         require(stakeId < stakes.length, "Invalid stake");
     383 | 
     384 |         StakeInfo memory s = stakes[stakeId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:108`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     106 |     ) external onlyOwner validCategory(category) returns (uint256 scheduleId) {
     107 |         require(beneficiary != address(0), "Invalid beneficiary");
>>>  108 |         require(amount > 0, "Zero amount");
     109 |         require(startTime >= block.timestamp, "Past start");
     110 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 |         require(beneficiary != address(0), "Invalid beneficiary");
     108 |         require(amount > 0, "Zero amount");
>>>  109 |         require(startTime >= block.timestamp, "Past start");
     110 | 
     111 |         require(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:116`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     114 |         );
     115 | 
>>>  116 |         require(totalAllocated + amount <= TOTAL_CAP, "Total cap exceeded");
     117 | 
     118 |         categoryAllocated[category] += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:153`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     151 |         uint256 length = categories.length;
     152 | 
>>>  153 |         require(length > 0, "Empty array");
     154 |         require(beneficiaries.length == length, "Length mismatch");
     155 |         require(amounts.length == length, "Length mismatch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:154`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     152 | 
     153 |         require(length > 0, "Empty array");
>>>  154 |         require(beneficiaries.length == length, "Length mismatch");
     155 |         require(amounts.length == length, "Length mismatch");
     156 |         require(startTimes.length == length, "Length mismatch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:155`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     153 |         require(length > 0, "Empty array");
     154 |         require(beneficiaries.length == length, "Length mismatch");
>>>  155 |         require(amounts.length == length, "Length mismatch");
     156 |         require(startTimes.length == length, "Length mismatch");
     157 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:156`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     154 |         require(beneficiaries.length == length, "Length mismatch");
     155 |         require(amounts.length == length, "Length mismatch");
>>>  156 |         require(startTimes.length == length, "Length mismatch");
     157 | 
     158 |         for (uint256 i = 0; i < length; i++) {
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:175`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     173 |     ) internal validCategory(category) returns (uint256 scheduleId) {
     174 |         require(beneficiary != address(0), "Invalid beneficiary");
>>>  175 |         require(amount > 0, "Zero amount");
     176 |         require(startTime >= block.timestamp, "Past start");
     177 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:176`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     174 |         require(beneficiary != address(0), "Invalid beneficiary");
     175 |         require(amount > 0, "Zero amount");
>>>  176 |         require(startTime >= block.timestamp, "Past start");
     177 | 
     178 |         require(
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:183`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     181 |         );
     182 | 
>>>  183 |         require(totalAllocated + amount <= TOTAL_CAP, "Total cap exceeded");
     184 | 
     185 |         categoryAllocated[category] += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:216`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     214 |         address newBeneficiary
     215 |     ) external onlyOwner {
>>>  216 |         require(scheduleId < schedules.length, "Invalid schedule");
     217 |         require(newBeneficiary != address(0), "Invalid beneficiary");
     218 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:221`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     219 |         VestingSchedule storage s = schedules[scheduleId];
     220 | 
>>>  221 |         require(s.exists, "Schedule missing");
     222 | 
     223 |         address oldBeneficiary = s.beneficiary;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:225`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     223 |         address oldBeneficiary = s.beneficiary;
     224 | 
>>>  225 |         require(oldBeneficiary != newBeneficiary, "Same beneficiary");
     226 | 
     227 |         _removeScheduleFromBeneficiary(oldBeneficiary, scheduleId);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:237`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     235 | 
     236 |     function fundVault(uint256 amount) external onlyOwner {
>>>  237 |         require(amount > 0, "Zero amount");
     238 | 
     239 |         axnv.safeTransferFrom(msg.sender, address(this), amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:251`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     249 | 
     250 |     function claim(uint256 scheduleId) public nonReentrant {
>>>  251 |         require(!claimsPaused, "Claims paused");
     252 |         require(scheduleId < schedules.length, "Invalid schedule");
     253 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:252`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     250 |     function claim(uint256 scheduleId) public nonReentrant {
     251 |         require(!claimsPaused, "Claims paused");
>>>  252 |         require(scheduleId < schedules.length, "Invalid schedule");
     253 | 
     254 |         VestingSchedule storage s = schedules[scheduleId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:256`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     254 |         VestingSchedule storage s = schedules[scheduleId];
     255 | 
>>>  256 |         require(s.exists, "Schedule missing");
     257 |         require(s.beneficiary == msg.sender, "Not beneficiary");
     258 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:257`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     255 | 
     256 |         require(s.exists, "Schedule missing");
>>>  257 |         require(s.beneficiary == msg.sender, "Not beneficiary");
     258 | 
     259 |         uint256 amount = claimable(scheduleId);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:261`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     259 |         uint256 amount = claimable(scheduleId);
     260 | 
>>>  261 |         require(amount > 0, "Nothing claimable");
     262 | 
     263 |         s.releasedAmount += amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:272`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     270 | 
     271 |     function claimMany(uint256[] calldata scheduleIds) external nonReentrant {
>>>  272 |         require(!claimsPaused, "Claims paused");
     273 |         require(scheduleIds.length > 0, "Empty array");
     274 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:273`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     271 |     function claimMany(uint256[] calldata scheduleIds) external nonReentrant {
     272 |         require(!claimsPaused, "Claims paused");
>>>  273 |         require(scheduleIds.length > 0, "Empty array");
     274 | 
     275 |         uint256 totalAmount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:280`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     278 |             uint256 scheduleId = scheduleIds[i];
     279 | 
>>>  280 |             require(scheduleId < schedules.length, "Invalid schedule");
     281 | 
     282 |             VestingSchedule storage s = schedules[scheduleId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:284`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     282 |             VestingSchedule storage s = schedules[scheduleId];
     283 | 
>>>  284 |             require(s.exists, "Schedule missing");
     285 |             require(s.beneficiary == msg.sender, "Not beneficiary");
     286 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:285`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     283 | 
     284 |             require(s.exists, "Schedule missing");
>>>  285 |             require(s.beneficiary == msg.sender, "Not beneficiary");
     286 | 
     287 |             uint256 amount = claimable(scheduleId);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:298`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     296 |         }
     297 | 
>>>  298 |         require(totalAmount > 0, "Nothing claimable");
     299 | 
     300 |         axnv.safeTransfer(msg.sender, totalAmount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:304`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     302 | 
     303 |     function claimable(uint256 scheduleId) public view returns (uint256) {
>>>  304 |         require(scheduleId < schedules.length, "Invalid schedule");
     305 | 
     306 |         VestingSchedule memory s = schedules[scheduleId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:322`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     320 | 
     321 |     function vestedAmount(uint256 scheduleId) public view returns (uint256) {
>>>  322 |         require(scheduleId < schedules.length, "Invalid schedule");
     323 | 
     324 |         VestingSchedule memory s = schedules[scheduleId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:364`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     362 |         )
     363 |     {
>>>  364 |         require(scheduleId < schedules.length, "Invalid schedule");
     365 | 
     366 |         VestingSchedule memory s = schedules[scheduleId];
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:515`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     513 |     ) external onlyOwner nonReentrant {
     514 |         require(to != address(0), "Invalid receiver");
>>>  515 |         require(amount > 0, "Zero amount");
     516 | 
     517 |         uint256 recoverable = recoverableAXNV();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:519`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     517 |         uint256 recoverable = recoverableAXNV();
     518 | 
>>>  519 |         require(amount <= recoverable, "Exceeds recoverable");
     520 | 
     521 |         axnv.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTeamAdvisorFounderVestingVault.sol:534`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     532 |         require(token != address(0), "Invalid token");
     533 |         require(to != address(0), "Invalid receiver");
>>>  534 |         require(amount > 0, "Zero amount");
     535 | 
     536 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTreasury.sol:115`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     113 |         uint256 length = categories.length;
     114 | 
>>>  115 |         require(length > 0, "Empty batch");
     116 |         require(recipients.length == length, "Recipients length mismatch");
     117 |         require(amounts.length == length, "Amounts length mismatch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTreasury.sol:116`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     114 | 
     115 |         require(length > 0, "Empty batch");
>>>  116 |         require(recipients.length == length, "Recipients length mismatch");
     117 |         require(amounts.length == length, "Amounts length mismatch");
     118 |         require(purposes.length == length, "Purposes length mismatch");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTreasury.sol:117`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     115 |         require(length > 0, "Empty batch");
     116 |         require(recipients.length == length, "Recipients length mismatch");
>>>  117 |         require(amounts.length == length, "Amounts length mismatch");
     118 |         require(purposes.length == length, "Purposes length mismatch");
     119 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTreasury.sol:118`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     116 |         require(recipients.length == length, "Recipients length mismatch");
     117 |         require(amounts.length == length, "Amounts length mismatch");
>>>  118 |         require(purposes.length == length, "Purposes length mismatch");
     119 | 
     120 |         uint256 batchTotal;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\AXNVTreasury.sol:302`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     300 |         uint256 recoverable = recoverableAXNV();
     301 | 
>>>  302 |         require(amount <= recoverable, "Exceeds recoverable AXNV");
     303 | 
     304 |         axnv.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:32`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      30 | 
      31 |     function fundVault(uint256 amount) external onlyOwner nonReentrant {
>>>   32 |         require(amount > 0, "Zero amount");
      33 | 
      34 |         uint256 newAccounted = accountedAXNV() + amount;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      33 | 
      34 |         uint256 newAccounted = accountedAXNV() + amount;
>>>   35 |         require(newAccounted <= GOVERNANCE_ALLOCATION_CAP, "Cap exceeded");
      36 | 
      37 |         axnv.safeTransferFrom(msg.sender, address(this), amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      51 |     {
      52 |         require(to != address(0), "Invalid recipient");
>>>   53 |         require(amount > 0, "Zero amount");
      54 |         require(totalReleased + amount <= GOVERNANCE_ALLOCATION_CAP, "Cap exceeded");
      55 |         require(amount <= contractAXNVBalance(), "Insufficient AXNV");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      52 |         require(to != address(0), "Invalid recipient");
      53 |         require(amount > 0, "Zero amount");
>>>   54 |         require(totalReleased + amount <= GOVERNANCE_ALLOCATION_CAP, "Cap exceeded");
      55 |         require(amount <= contractAXNVBalance(), "Insufficient AXNV");
      56 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:78`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      76 |     {
      77 |         require(to != address(0), "Invalid recipient");
>>>   78 |         require(amount > 0, "Zero amount");
      79 | 
      80 |         uint256 excess = excessAXNV();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:81`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      79 | 
      80 |         uint256 excess = excessAXNV();
>>>   81 |         require(amount <= excess, "Exceeds excess");
      82 | 
      83 |         axnv.safeTransfer(to, amount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `contracts\governance\AXNVGovernanceVault.sol:96`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      94 |         require(token != address(0), "Invalid token");
      95 |         require(to != address(0), "Invalid recipient");
>>>   96 |         require(amount > 0, "Zero amount");
      97 | 
      98 |         IERC20(token).safeTransfer(to, amount);
```
</details>

---


---
*Generated by BugHunter*