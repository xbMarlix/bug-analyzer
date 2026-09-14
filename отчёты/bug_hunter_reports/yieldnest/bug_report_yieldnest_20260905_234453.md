# BugHunter Report: yieldnest

**Generated:** 2026-09-05 23:44:53
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\yieldnest`
**Analyzers:** static, ast, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 157 |
| Total lines | 31,948 |
| Bugs found | 197 |
| !! High | 18 |
| ! Medium | 107 |
| ~ Low | 72 |

### Languages Detected

- **solidity**: 155 files
- **bash**: 2 files

## Security (1)

### [!!] Reentrancy Vector (External Call with Value)

- **File:** `test\mainnet\buffer.spec.sol:77`
- **Severity:** HIGH
- **Confidence:** 55%
- **Analyzer:** solidity_semantic

**Problem:** External .call{value:...} detected. If state is updated after this call, an attacker can re-enter.

**Fix:** Follow checks-effects-interactions: update state before external calls, or use a reentrancy guard.

<details>
<summary>Code</summary>

```
      75 |             // Test the depositAsset function
      76 |             deal(address(this), assets);
>>>   77 |             (bool success,) = MC.WETH.call{value: assets}("");
      78 |             assertTrue(success, "Weth deposit failed");
      79 |             IERC20(MC.WETH).approve(address(vault), assets);
```
</details>

---

## Logic (36)

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\provider.spec.sol:137`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'rate' is modified at line 137, after an external call at line 136. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     135 |         uint256 expectedRate =
     136 |             IStETH(MC.STETH).getPooledEthByShares(IERC4626(MC.SMOKEHOUSE_WSTETH).convertToAssets(1e18));
>>>  137 |         uint256 rate = provider.getRate(MC.SMOKEHOUSE_WSTETH);
     138 |         assertEq(rate, expectedRate, "Rate for SMOKEHOUSE_WSTETH should match the combined rate");
     139 |     }
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\provider.spec.sol:173`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'rate' is modified at line 173, after an external call at line 172. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     171 |         uint256 expectedRate =
     172 |             IStETH(MC.STETH).getPooledEthByShares(IERC4626(MC.YNFLEX_WSTETH_YNETHX_LVG1).convertToAssets(1e18));
>>>  173 |         uint256 rate = provider.getRate(MC.YNFLEX_WSTETH_YNETHX_LVG1);
     174 |         assertEq(rate, expectedRate, "Rate for YNFLEX_WSTETH_YNETHX_LVG1 should match the combined rate");
     175 |         assertGt(rate, 1e18, "Rate for YNFLEX_WSTETH_YNETHX_LVG1 should be greater than 1e18");
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\provider.spec.sol:179`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedWstethRate' is modified at line 179, after an external call at line 172. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     177 | 
     178 |         // Assert that the rate for YNFLEX_WSTETH_YNETHX_LVG1 is a combination of WSTETH rate and its own convertToAssets
>>>  179 |         uint256 expectedWstethRate = provider.getRate(MC.WSTETH);
     180 |         uint256 stratConvertToAssets = IERC4626(MC.YNFLEX_WSTETH_YNETHX_LVG1).convertToAssets(1e18);
     181 |         uint256 expectedCombinedRate = stratConvertToAssets * expectedWstethRate / 1e18;
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\provider.spec.sol:180`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'stratConvertToAssets' is modified at line 180, after an external call at line 172. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     178 |         // Assert that the rate for YNFLEX_WSTETH_YNETHX_LVG1 is a combination of WSTETH rate and its own convertToAssets
     179 |         uint256 expectedWstethRate = provider.getRate(MC.WSTETH);
>>>  180 |         uint256 stratConvertToAssets = IERC4626(MC.YNFLEX_WSTETH_YNETHX_LVG1).convertToAssets(1e18);
     181 |         uint256 expectedCombinedRate = stratConvertToAssets * expectedWstethRate / 1e18;
     182 |         assertApproxEqAbs(
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\provider.spec.sol:181`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedCombinedRate' is modified at line 181, after an external call at line 172. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     179 |         uint256 expectedWstethRate = provider.getRate(MC.WSTETH);
     180 |         uint256 stratConvertToAssets = IERC4626(MC.YNFLEX_WSTETH_YNETHX_LVG1).convertToAssets(1e18);
>>>  181 |         uint256 expectedCombinedRate = stratConvertToAssets * expectedWstethRate / 1e18;
     182 |         assertApproxEqAbs(
     183 |             rate,
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:94`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'sharesMintedFromUSDE' is modified at line 94, after an external call at line 84. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      92 | 
      93 |         // Deposit USDE using depositAsset
>>>   94 |         uint256 sharesMintedFromUSDE = vault.depositAsset(MC.USDE, usdeDepositAmount, alice);
      95 |         vm.stopPrank();
      96 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:151`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'sharesMintedFromUSDE' is modified at line 151, after an external call at line 141. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     149 | 
     150 |         // Deposit USDE using depositAsset
>>>  151 |         uint256 sharesMintedFromUSDE = vault.depositAsset(MC.USDE, usdeDepositAmount, alice);
     152 |         vm.stopPrank();
     153 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:159`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'usdeReceived' is modified at line 159, after an external call at line 155. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     157 |         // Redeem USDE using redeemAsset
     158 |         vm.startPrank(alice);
>>>  159 |         uint256 usdeReceived = vault.redeemAsset(MC.USDE, sharesMintedFromUSDE, alice, alice);
     160 |         vm.stopPrank();
     161 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:208`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'sharesMintedFromUSDE' is modified at line 208, after an external call at line 198. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     206 | 
     207 |         // Deposit USDE using depositAsset
>>>  208 |         uint256 sharesMintedFromUSDE = vault.depositAsset(MC.USDE, usdeDepositAmount, alice);
     209 |         vm.stopPrank();
     210 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:216`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'assetsWithdrawn' is modified at line 216, after an external call at line 212. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     214 |         // Withdraw USDC using withdrawAsset
     215 |         vm.startPrank(alice);
>>>  216 |         uint256 assetsWithdrawn = vault.withdrawAsset(MC.USDC, sharesMintedFromUSDC / 1e12, alice, alice);
     217 |         vm.stopPrank();
     218 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:264`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'sharesMintedFromUSDE' is modified at line 264, after an external call at line 254. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     262 | 
     263 |         // Deposit USDE using depositAsset
>>>  264 |         uint256 sharesMintedFromUSDE = vault.depositAsset(MC.USDE, usdeDepositAmount, alice);
     265 |         vm.stopPrank();
     266 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\strategy\base6decimals\withdraw.t.sol:272`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'usdcReceived' is modified at line 272, after an external call at line 268. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     270 |         // Withdraw USDC using withdrawAsset
     271 |         vm.startPrank(alice);
>>>  272 |         uint256 usdcReceived = vault.redeemAsset(MC.USDC, sharesMintedFromUSDC, alice, alice);
     273 |         vm.stopPrank();
     274 | 
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\mint.t.sol:120`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'afterRate' is modified at line 120, after an external call at line 108. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     118 |         assertEq(vault.totalBaseAssets(), assetsDeposited, "Total base assets did not increase correctly");
     119 |         assertEq(vault.totalSupply(), sharesToMint, "Total supply mismatch");
>>>  120 |         uint256 afterRate = vault.convertToAssets(1e6);
     121 |         assertEq(afterRate, initialRate, "Vault conversion rate shouldn't change on mint");
     122 |     }
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\mint.t.sol:153`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'finalRate' is modified at line 153, after an external call at line 141. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     151 |         assertEq(vault.totalSupply(), sharesToMint, "Convert to shares failed");
     152 | 
>>>  153 |         uint256 finalRate = vault.convertToAssets(1e6);
     154 | 
     155 |         assertEq(finalRate, initialRate, "Vault conversion rate should not change after mint");
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\mint.t.sol:191`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'afterRate' is modified at line 191, after an external call at line 182. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     189 |         assertEq(vault.totalBaseAssets(), assetsDeposited, "TotalBaseAssets incorrect (fuzz)");
     190 | 
>>>  191 |         uint256 afterRate = vault.convertToAssets(1e6);
     192 |         assertEq(afterRate, initialRate, "Vault conversion rate should not change on mint");
     193 |     }
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\mint.t.sol:219`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'afterRate' is modified at line 219, after an external call at line 215. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     217 |         assertEq(vault.totalBaseAssets(), depositAmount, "Vault totalBaseAssets incorrect");
     218 | 
>>>  219 |         uint256 afterRate = vault.convertToAssets(1e6);
     220 |         assertEq(afterRate, initialRate, "Vault conversion rate changed after low deposit");
     221 |     }
```
</details>

---

### [!!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\mint.t.sol:295`
- **Severity:** HIGH
- **Confidence:** 45%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'afterRate' is modified at line 295, after an external call at line 291. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     293 |         assertEq(vault.totalBaseAssets(), sharesToMint, "Vault totalBaseAssets incorrect");
     294 | 
>>>  295 |         uint256 afterRate = vault.convertToAssets(1e6);
     296 |         assertEq(afterRate, initialRate, "Vault conversion rate changed after low deposit");
     297 |     }
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\processAccounting.spec.sol:58`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'totalAssetsBefore' is modified at line 58, after an external call at line 56. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      56 |         IERC20(MC.WETH).transfer(address(vault), donationAmount);
      57 | 
>>>   58 |         uint256 totalAssetsBefore = vault.totalAssets();
      59 |         uint256 totalSupplyBefore = vault.totalSupply();
      60 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\processAccounting.spec.sol:59`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'totalSupplyBefore' is modified at line 59, after an external call at line 56. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      57 | 
      58 |         uint256 totalAssetsBefore = vault.totalAssets();
>>>   59 |         uint256 totalSupplyBefore = vault.totalSupply();
      60 | 
      61 |         uint256 performanceFeeSharesBefore =
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\processAccounting.spec.sol:66`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'totalAssetsAfter' is modified at line 66, after an external call at line 56. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      64 |         vault.processAccounting();
      65 | 
>>>   66 |         uint256 totalAssetsAfter = vault.totalAssets();
      67 |         uint256 totalSupplyAfter = vault.totalSupply();
      68 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\mainnet\processAccounting.spec.sol:67`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'totalSupplyAfter' is modified at line 67, after an external call at line 56. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      65 | 
      66 |         uint256 totalAssetsAfter = vault.totalAssets();
>>>   67 |         uint256 totalSupplyAfter = vault.totalSupply();
      68 | 
      69 |         // Verify that total assets increased by the donation amount
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:78`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'performanceFeeSharesReceived' is modified at line 78, after an external call at line 70. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      76 |         uint256 performanceFeeRecipientSharesAfter =
      77 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
>>>   78 |         uint256 performanceFeeSharesReceived = performanceFeeRecipientSharesAfter - performanceFeeRecipientSharesBefore;
      79 | 
      80 |         assertLe(
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:143`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'convertToAssetsBefore' is modified at line 143, after an external call at line 139. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     141 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
     142 | 
>>>  143 |         uint256 convertToAssetsBefore = vault.convertToAssets(1e18);
     144 |         assertEq(convertToAssetsBefore, 1e6, "vault's convertToAssets should be 1e6");
     145 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:150`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'performanceFeeSharesReceived' is modified at line 150, after an external call at line 139. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     148 |         uint256 performanceFeeRecipientSharesAfter =
     149 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
>>>  150 |         uint256 performanceFeeSharesReceived = performanceFeeRecipientSharesAfter - performanceFeeRecipientSharesBefore;
     151 |         uint256 convertToAssetsAfter = vault.convertToAssets(1e18);
     152 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:151`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'convertToAssetsAfter' is modified at line 151, after an external call at line 139. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     149 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
     150 |         uint256 performanceFeeSharesReceived = performanceFeeRecipientSharesAfter - performanceFeeRecipientSharesBefore;
>>>  151 |         uint256 convertToAssetsAfter = vault.convertToAssets(1e18);
     152 | 
     153 |         assertEq(convertToAssetsBefore, convertToAssetsAfter, "convertToAssets for 1e18 should stay the same");
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:157`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'expectedPerformanceFeeShares' is modified at line 157, after an external call at line 139. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     155 |         if (yield > 0) {
     156 |             // With 100% performance fee, all yield should go to fee recipient as shares
>>>  157 |             uint256 expectedPerformanceFeeShares = vault.convertToShares(yield);
     158 |             assertEq(
     159 |                 performanceFeeSharesReceived,
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:171`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'aliceAssetValue' is modified at line 171, after an external call at line 139. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     169 | 
     170 |             // Alice's share value should remain the same (depositAmount worth of assets)
>>>  171 |             uint256 aliceAssetValue = vault.convertToAssets(vault.balanceOf(alice));
     172 |             assertEq(aliceAssetValue, depositAmount, "Alice's asset value should remain depositAmount");
     173 |         } else {
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:74`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'performanceFeeSharesReceived' is modified at line 74, after an external call at line 66. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
      72 |         uint256 performanceFeeRecipientSharesAfter =
      73 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
>>>   74 |         uint256 performanceFeeSharesReceived = performanceFeeRecipientSharesAfter - performanceFeeRecipientSharesBefore;
      75 | 
      76 |         assertLe(
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:120`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultTotalSupplyBefore' is modified at line 120, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     118 | 
     119 |         vm.startPrank(address(vault));
>>>  120 |         uint256 vaultTotalSupplyBefore = vault.totalSupply();
     121 |         uint256 vaultTotalAssetsBefore = vault.totalAssets();
     122 |         uint256 vaultExchangeRateBefore = vault.convertToAssets(10 ** vault.decimals());
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:121`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultTotalAssetsBefore' is modified at line 121, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     119 |         vm.startPrank(address(vault));
     120 |         uint256 vaultTotalSupplyBefore = vault.totalSupply();
>>>  121 |         uint256 vaultTotalAssetsBefore = vault.totalAssets();
     122 |         uint256 vaultExchangeRateBefore = vault.convertToAssets(10 ** vault.decimals());
     123 |         uint256 feesAccrued = (donationAmount * hooks.performanceFee()) / 1 ether;
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:122`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultExchangeRateBefore' is modified at line 122, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     120 |         uint256 vaultTotalSupplyBefore = vault.totalSupply();
     121 |         uint256 vaultTotalAssetsBefore = vault.totalAssets();
>>>  122 |         uint256 vaultExchangeRateBefore = vault.convertToAssets(10 ** vault.decimals());
     123 |         uint256 feesAccrued = (donationAmount * hooks.performanceFee()) / 1 ether;
     124 |         vm.stopPrank();
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:123`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'feesAccrued' is modified at line 123, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     121 |         uint256 vaultTotalAssetsBefore = vault.totalAssets();
     122 |         uint256 vaultExchangeRateBefore = vault.convertToAssets(10 ** vault.decimals());
>>>  123 |         uint256 feesAccrued = (donationAmount * hooks.performanceFee()) / 1 ether;
     124 |         vm.stopPrank();
     125 |         vault.processAccounting();
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:127`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultTotalSupplyAfter' is modified at line 127, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     125 |         vault.processAccounting();
     126 | 
>>>  127 |         uint256 vaultTotalSupplyAfter = vault.totalSupply();
     128 |         uint256 vaultExchangeRateAfter = vault.convertToAssets(10 ** vault.decimals());
     129 |         uint256 vaultTotalAssetsAfter = vault.totalAssets();
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:128`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultExchangeRateAfter' is modified at line 128, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     126 | 
     127 |         uint256 vaultTotalSupplyAfter = vault.totalSupply();
>>>  128 |         uint256 vaultExchangeRateAfter = vault.convertToAssets(10 ** vault.decimals());
     129 |         uint256 vaultTotalAssetsAfter = vault.totalAssets();
     130 | 
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:129`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'vaultTotalAssetsAfter' is modified at line 129, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     127 |         uint256 vaultTotalSupplyAfter = vault.totalSupply();
     128 |         uint256 vaultExchangeRateAfter = vault.convertToAssets(10 ** vault.decimals());
>>>  129 |         uint256 vaultTotalAssetsAfter = vault.totalAssets();
     130 | 
     131 |         if (feesAccrued > 0) {
```
</details>

---

### [!] State Change After External Call (CEI Violation)

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:132`
- **Severity:** MEDIUM
- **Confidence:** 40%
- **Analyzer:** solidity_semantic

**Problem:** State variable 'performanceFeeShares' is modified at line 132, after an external call at line 116. An attacker-controlled contract may re-enter before this write.

**Fix:** Move the state update before the external call, or apply a reentrancy guard.

<details>
<summary>Code</summary>

```
     130 | 
     131 |         if (feesAccrued > 0) {
>>>  132 |             uint256 performanceFeeShares = vaultTotalSupplyAfter - vaultTotalSupplyBefore;
     133 | 
     134 |             assertLe(
```
</details>

---

## Resource Management (88)

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\BaseWithdrawerTest.sol:196`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     194 |         // transfer donated amount to vault
     195 |         vm.startPrank(alice);
>>>  196 |         IERC20(asset).transfer(address(withdrawer), donatedAmount);
     197 |         vm.stopPrank();
     198 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\basicfunctionality.spec.sol:148`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     146 | 
     147 |         vm.startPrank(alice);
>>>  148 |         IERC20(asset).transfer(address(vault), donatedAmount);
     149 |         vm.stopPrank();
     150 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\buffer.spec.sol:148`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     146 |         (success,) = MC.WETH.call{value: 1 ether}("");
     147 |         assertTrue(success, "Weth deposit failed");
>>>  148 |         IERC20(MC.WETH).transfer(vault.buffer(), 1 ether);
     149 | 
     150 |         // Allocate to buffer
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\invariants.spec.sol:124`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     122 |         deal(MC.WETH, address(this), 1 ether);
     123 |         IERC20(MC.WETH).approve(address(vault), 1 ether);
>>>  124 |         IERC20(MC.WETH).transfer(address(vault), 1 ether);
     125 | 
     126 |         uint256 previewedShares = vault.previewDeposit(assets);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\processAccounting.spec.sol:56`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      54 |         // Now donate the additional amount
      55 |         deal(MC.WETH, address(this), donationAmount);
>>>   56 |         IERC20(MC.WETH).transfer(address(vault), donationAmount);
      57 | 
      58 |         uint256 totalAssetsBefore = vault.totalAssets();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\processAccounting.spec.sol:213`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     211 |         // Donate additional tokens directly to the vault
     212 |         deal(MC.WETH, address(this), donationAmount);
>>>  213 |         IERC20(MC.WETH).transfer(address(vault), donationAmount);
     214 | 
     215 |         uint256 totalAssetsBefore = vault.totalAssets();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\helpers\TestHelper.sol:155`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     153 |         // Have intermediary send to final receiver
     154 |         vm.prank(intermediary);
>>>  155 |         payable(receiver).transfer(amount);
     156 |     }
     157 | }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\mainnet\mocks\MockERC4626.sol:26`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      24 | 
      25 |         // Transfer the assets to the caller
>>>   26 |         ERC20(asset()).transfer(msg.sender, amountToSlash);
      27 | 
      28 |         return amountToSlash;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\mocks\MockSwapper.sol:77`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      75 | 
      76 |         // Transfer the calculated amount of tokenOut to the sender
>>>   77 |         IERC20(tokenOut).transfer(msg.sender, amountOut);
      78 | 
      79 |         return amountOut;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\mocks\MockWETH.sol:44`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      42 |         require(balanceOf[msg.sender] >= wad);
      43 |         balanceOf[msg.sender] -= wad;
>>>   44 |         payable(msg.sender).transfer(wad);
      45 |         emit Withdrawal(msg.sender, wad);
      46 |     }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\admin.t.sol:36`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      34 |         deal(alice, INITIAL_BALANCE);
      35 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   36 |         weth.transfer(alice, INITIAL_BALANCE);
      37 | 
      38 |         // Approve strategy to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\deposit.t.sol:34`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      32 |         deal(alice, INITIAL_BALANCE);
      33 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   34 |         weth.transfer(alice, INITIAL_BALANCE);
      35 | 
      36 |         // Approve strategy to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\hooks.t.sol:48`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      46 |         deal(caller, INITIAL_BALANCE);
      47 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   48 |         weth.transfer(caller, INITIAL_BALANCE);
      49 | 
      50 |         // Approve strategy to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\mint.t.sol:34`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      32 |         deal(alice, INITIAL_BALANCE);
      33 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   34 |         weth.transfer(alice, INITIAL_BALANCE);
      35 | 
      36 |         // Approve strategy to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\redeem.t.sol:40`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      38 |         deal(alice, INITIAL_BALANCE);
      39 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   40 |         weth.transfer(alice, INITIAL_BALANCE);
      41 | 
      42 |         // Approve strategy to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\views.t.sol:32`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      30 |         deal(alice, INITIAL_BALANCE);
      31 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   32 |         weth.transfer(alice, INITIAL_BALANCE);
      33 | 
      34 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\withdraw.t.sol:40`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      38 |         deal(alice, INITIAL_BALANCE);
      39 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   40 |         weth.transfer(alice, INITIAL_BALANCE);
      41 | 
      42 |         // Approve strategy to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\withdraw.t.sol:92`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      90 |         vm.startPrank(alice);
      91 |         deal(address(newAsset), alice, 1 ether);
>>>   92 |         IERC20(newAsset).transfer(address(strategy), 1 ether);
      93 |         vm.stopPrank();
      94 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\strategy\base6decimals\SetupBase6DecimalsBaseStrategy.sol:125`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     123 |             vm.startPrank(donor);
     124 |             IERC20(MC.USDE).approve(address(MC.SUSDE), donationAmount);
>>>  125 |             IERC20(MC.USDE).transfer(address(MC.SUSDE), donationAmount);
     126 |             vm.stopPrank();
     127 |         }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:41`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      39 |         deal(alice, INITIAL_BALANCE);
      40 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   41 |         weth.transfer(alice, INITIAL_BALANCE);
      42 | 
      43 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:321`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     319 |         // Direct transfer of WETH to the vault
     320 |         deal(MC.WETH, address(alice), depositAmountWETH);
>>>  321 |         IERC20(MC.WETH).transfer(address(vault), depositAmountWETH);
     322 |         expectedTotalAssets += depositAmountWETH;
     323 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:332`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     330 |         expectedTotalAssets += (aliceStEthDepositAmount2 * rate) / (10 ** 18);
     331 | 
>>>  332 |         IERC20(steth).transfer(address(vault), aliceStEthDepositAmount2);
     333 | 
     334 |         vault.processAccounting();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:377`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     375 |         // Direct transfer of WETH to the vault
     376 |         deal(MC.WETH, address(alice), depositAmountWETH);
>>>  377 |         IERC20(MC.WETH).transfer(address(vault), depositAmountWETH);
     378 |         expectedTotalAssets += depositAmountWETH;
     379 |         yieldEarned += depositAmountWETH;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:389`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     387 |         yieldEarned += (aliceStEthDepositAmount2 * rate) / (10 ** 18);
     388 | 
>>>  389 |         IERC20(steth).transfer(address(vault), aliceStEthDepositAmount2);
     390 |         uint256 performanceFeeShares;
     391 |         uint256 performanceFeeAmount;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:471`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     469 |         assertTrue(success, "WETH transfer failed");
     470 |         vm.prank(alice);
>>>  471 |         IERC20(MC.WETH).transfer(address(vault), wethAmount);
     472 |         expectedTotalAssets += wethAmount;
     473 |         yieldEarned += wethAmount;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:477`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     475 |         deal(MC.WBTC, alice, wbtcAmount);
     476 |         vm.prank(alice);
>>>  477 |         IERC20(MC.WBTC).transfer(address(vault), wbtcAmount);
     478 |         uint256 wbtcRate = IProvider(MC.PROVIDER).getRate(MC.WBTC);
     479 |         expectedTotalAssets += (wbtcAmount * wbtcRate) / (10 ** 8); // WBTC has 8 decimals
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:485`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     483 |         deal(MC.METH, alice, methAmount);
     484 |         vm.prank(alice);
>>>  485 |         IERC20(MC.METH).transfer(address(vault), methAmount);
     486 |         uint256 methRate = IProvider(MC.PROVIDER).getRate(MC.METH);
     487 |         expectedTotalAssets += (methAmount * methRate) / (10 ** 18);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:609`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     607 |         // Donate to inflate share price
     608 |         vm.prank(bob);
>>>  609 |         weth.transfer(address(vault), 100_000 ether);
     610 |         vault.processAccounting();
     611 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:658`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     656 |         // Direct transfer creates divergence
     657 |         vm.prank(bob);
>>>  658 |         weth.transfer(address(vault), 50 ether);
     659 | 
     660 |         assertEq(weth.balanceOf(address(vault)), 150 ether, "Actual balance = 150");
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\accounting.t.sol:789`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     787 |         // Direct transfer makes cached stale
     788 |         vm.prank(bob);
>>>  789 |         weth.transfer(address(vault), 50 ether);
     790 | 
     791 |         cachedTotal = vault.totalAssets();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\admin.t.sol:410`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     408 |         // Add some yield
     409 |         deal(address(weth), address(this), 0.1 ether);
>>>  410 |         weth.transfer(address(vault), 0.1 ether);
     411 | 
     412 |         // Disable always compute - should call processAccounting
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\compliance.t.sol:31`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      29 |         deal(alice, INITIAL_BALANCE);
      30 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   31 |         weth.transfer(alice, INITIAL_BALANCE);
      32 | 
      33 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\deposit.t.sol:44`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      42 |         deal(alice, INITIAL_BALANCE);
      43 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   44 |         weth.transfer(alice, INITIAL_BALANCE);
      45 | 
      46 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\deposit.t.sol:400`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     398 |         // Add yield
     399 |         deal(address(weth), address(this), yieldAmount);
>>>  400 |         weth.transfer(address(vault), yieldAmount);
     401 |         vault.processAccounting();
     402 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:58`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      56 |         deal(alice, INITIAL_BALANCE);
      57 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   58 |         weth.transfer(alice, INITIAL_BALANCE);
      59 | 
      60 |         deal(caller, INITIAL_BALANCE);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:62`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      60 |         deal(caller, INITIAL_BALANCE);
      61 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   62 |         weth.transfer(caller, INITIAL_BALANCE);
      63 | 
      64 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:84`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      82 | 
      83 |         // alice transfers 10% of vault's balance to vault which will be considered as yield
>>>   84 |         weth.transfer(address(vault), yield);
      85 | 
      86 |         uint256 performanceFee = 0.01 ether;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:124`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     122 | 
     123 |         uint256 yield = 1 ether;
>>>  124 |         weth.transfer(address(vault), yield);
     125 | 
     126 |         uint256 performanceFee = yield;
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:177`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     175 | 
     176 |         uint256 yield = 0.1 ether;
>>>  177 |         weth.transfer(address(vault), yield);
     178 | 
     179 |         uint256 performanceFeeRecipientSharesBefore =
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:227`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     225 |         assertEq(shares, depositAmount, "shares should be depositAmount");
     226 | 
>>>  227 |         weth.transfer(address(vault), yield);
     228 |         uint256 performanceFeeRecipientSharesBefore =
     229 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:285`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     283 |         assertEq(shares, depositAmount, "shares should be depositAmount");
     284 | 
>>>  285 |         weth.transfer(address(vault), yield);
     286 |         uint256 performanceFeeRecipientSharesBefore =
     287 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:327`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     325 |         assertEq(shares, depositAmount, "shares should be depositAmount");
     326 | 
>>>  327 |         weth.transfer(address(vault), yield);
     328 |         uint256 performanceFeeRecipientSharesBefore =
     329 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:377`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     375 |         vault.processAccounting();
     376 | 
>>>  377 |         IERC20(MC.WETH).transfer(address(vault), donationAmount);
     378 |         vm.stopPrank();
     379 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:468`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     466 |         vault.processAccounting();
     467 | 
>>>  468 |         IERC20(MC.WETH).transfer(address(vault), donationAmount);
     469 |         vm.stopPrank();
     470 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:519`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     517 |         uint256 shares2 = vault.deposit(depositAmount2, user2);
     518 |         vault.processAccounting();
>>>  519 |         IERC20(MC.WETH).transfer(address(vault), yieldAmount1);
     520 |         vm.stopPrank();
     521 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:664`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     662 |         uint256 yieldAmount = 1 ether;
     663 |         deal(address(weth), address(this), yieldAmount);
>>>  664 |         weth.transfer(address(vault), yieldAmount);
     665 | 
     666 |         assertEq(vault.convertToAssets(1e18), 1e18, "Vault should have yield amount");
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\feehooks.t.sol:692`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     690 |         uint256 yieldAmount = 1 ether;
     691 |         deal(address(weth), address(this), yieldAmount);
>>>  692 |         weth.transfer(address(vault), yieldAmount);
     693 | 
     694 |         // Now, process accounting should revert due to 100% fee on nonzero yield with zero initial assets
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\hooks.t.sol:62`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      60 |         deal(alice, INITIAL_BALANCE);
      61 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   62 |         weth.transfer(alice, INITIAL_BALANCE);
      63 | 
      64 |         deal(caller, INITIAL_BALANCE);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\hooks.t.sol:66`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      64 |         deal(caller, INITIAL_BALANCE);
      65 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   66 |         weth.transfer(caller, INITIAL_BALANCE);
      67 | 
      68 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\hooks.t.sol:271`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     269 |         vm.startPrank(alice);
     270 |         vault.deposit(depositAmount, alice);
>>>  271 |         weth.transfer(address(vault), yieldAmount);
     272 |         vault.processAccounting();
     273 |         vm.stopPrank();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\hooks.t.sol:1359`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
    1357 |             vm.startPrank(donor);
    1358 |             weth.deposit{value: donationAmount}();
>>> 1359 |             weth.transfer(address(vault), donationAmount);
    1360 |             vm.stopPrank();
    1361 |         }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\invariants.t.sol:32`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      30 |         deal(alice, INITIAL_BALANCE);
      31 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   32 |         weth.transfer(alice, INITIAL_BALANCE);
      33 | 
      34 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\mint.t.sol:44`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      42 |         deal(alice, INITIAL_BALANCE);
      43 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   44 |         weth.transfer(alice, INITIAL_BALANCE);
      45 | 
      46 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\mint.t.sol:181`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     179 |         // Simulate a donation (send tokens directly to vault)
     180 |         deal(address(weth), address(this), donationAmount);
>>>  181 |         weth.transfer(address(vault), donationAmount);
     182 | 
     183 |         if (!alwaysComputeTotalAssets) {
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\mint.t.sol:259`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     257 |         // Add yield
     258 |         deal(address(weth), address(this), yieldAmount);
>>>  259 |         weth.transfer(address(vault), yieldAmount);
     260 |         vault.processAccounting();
     261 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\processor.t.sol:52`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      50 |         deal(alice, INITIAL_BALANCE);
      51 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   52 |         weth.transfer(alice, INITIAL_BALANCE);
      53 | 
      54 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\processor.t.sol:67`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      65 |         // Set up some initial balances for assets and strategies
      66 |         vm.prank(alice);
>>>   67 |         weth.transfer(address(vault), 50 ether); // Transfer some WETH to the vault
      68 |         steth.transfer(address(vault), 50 ether); // Transfer some STETH to the vault
      69 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\processor.t.sol:68`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      66 |         vm.prank(alice);
      67 |         weth.transfer(address(vault), 50 ether); // Transfer some WETH to the vault
>>>   68 |         steth.transfer(address(vault), 50 ether); // Transfer some STETH to the vault
      69 | 
      70 |         vault.processAccounting();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\redeem.t.sol:42`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      40 |         deal(alice, INITIAL_BALANCE);
      41 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   42 |         weth.transfer(alice, INITIAL_BALANCE);
      43 | 
      44 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\slashing.t.sol:47`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      45 |         deal(alice, INITIAL_BALANCE);
      46 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   47 |         weth.transfer(alice, INITIAL_BALANCE);
      48 | 
      49 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\views.t.sol:43`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      41 |         deal(alice, INITIAL_BALANCE);
      42 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   43 |         weth.transfer(alice, INITIAL_BALANCE);
      44 | 
      45 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\views.t.sol:197`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     195 | 
     196 |         deal(MC.WETH, address(this), rewards);
>>>  197 |         IERC20(MC.WETH).transfer(address(vault), rewards);
     198 | 
     199 |         // Process accounting to update total assets
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\views.t.sol:260`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     258 | 
     259 |         deal(MC.WETH, address(this), rewards);
>>>  260 |         IERC20(MC.WETH).transfer(address(vault), rewards);
     261 | 
     262 |         // Process accounting to update total assets
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdraw.t.sol:42`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      40 |         deal(alice, INITIAL_BALANCE);
      41 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   42 |         weth.transfer(alice, INITIAL_BALANCE);
      43 | 
      44 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdraw.t.sol:139`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     137 |         uint256 depositShares1 = vault.deposit(deposit1, alice);
     138 |         vault.processAccounting();
>>>  139 |         IERC20(MC.WETH).transfer(address(vault), yieldAmount1);
     140 | 
     141 |         uint256 performanceFee = IFeeHooks(address(vault.hooks())).performanceFee();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdraw.t.sol:181`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     179 | 
     180 |         vm.startPrank(alice);
>>>  181 |         IERC20(MC.WETH).transfer(address(vault), yieldAmount2);
     182 | 
     183 |         performanceFee = IFeeHooks(address(vault.hooks())).performanceFee();
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdraw.t.sol:260`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     258 |         deal(bob, INITIAL_BALANCE);
     259 |         weth.deposit{value: INITIAL_BALANCE}();
>>>  260 |         weth.transfer(bob, INITIAL_BALANCE);
     261 | 
     262 |         vm.startPrank(bob);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdrawAsset.t.sol:38`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      36 |         deal(alice, INITIAL_BALANCE);
      37 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   38 |         weth.transfer(alice, INITIAL_BALANCE);
      39 | 
      40 |         // Approve vault to spend Alice's tokens
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdrawAsset.t.sol:69`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      67 |         // Bob sends his shares to withdrawerManager
      68 |         vm.startPrank(bob);
>>>   69 |         vault.transfer(withdrawerManager, vault.balanceOf(bob));
      70 |         vm.stopPrank();
      71 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdrawAsset.t.sol:145`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     143 |         // Bob sends his shares to withdrawerManager
     144 |         vm.startPrank(bob);
>>>  145 |         vault.transfer(withdrawerManager, vault.balanceOf(bob));
     146 |         vm.stopPrank();
     147 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdrawAsset.t.sol:227`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     225 |         // Transfer vault tokens to the vault to ensure it has enough assets
     226 |         vm.prank(bob);
>>>  227 |         weth.transfer(address(vault), withdrawAmount);
     228 | 
     229 |         // Calculate required shares for withdrawal
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdrawAsset.t.sol:236`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     234 |         // Burn most of Bob's shares, leaving insufficient shares for withdrawal
     235 |         vm.prank(bob);
>>>  236 |         vault.transfer(alice, sharesReceived * 2 / 3);
     237 | 
     238 |         // Verify Bob has insufficient shares
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\withdrawer.t.sol:32`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      30 |         deal(alice, INITIAL_BALANCE);
      31 |         weth.deposit{value: INITIAL_BALANCE}();
>>>   32 |         weth.transfer(alice, INITIAL_BALANCE);
      33 | 
      34 |         vm.startPrank(ADMIN);
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\base6decimals\deposit.t.sol:395`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     393 |             vm.startPrank(rewarder);
     394 |             MockERC20(MC.USDE).mint(rewardAmount);
>>>  395 |             IERC20(MC.USDE).transfer(address(vault), rewardAmount);
     396 |             vm.stopPrank();
     397 |         }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:70`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      68 |         // alice transfers yield to vault
      69 |         vm.prank(alice);
>>>   70 |         IERC20(MC.USDC).transfer(address(vault), yield);
      71 | 
      72 |         uint256 performanceFeeRecipientSharesBefore =
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:139`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     137 |         deal(MC.USDC, address(this), yield);
     138 | 
>>>  139 |         IERC20(MC.USDC).transfer(address(vault), yield);
     140 |         uint256 performanceFeeRecipientSharesBefore =
     141 |             vault.balanceOf(IFeeHooks(address(vault.hooks())).performanceFeeRecipient());
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:202`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     200 |         vault.processAccounting();
     201 | 
>>>  202 |         IERC20(MC.USDC).transfer(address(vault), donationAmount);
     203 |         vm.stopPrank();
     204 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\base6decimals\feehooks.t.sol:305`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     303 |         vault.processAccounting();
     304 | 
>>>  305 |         IERC20(MC.USDC).transfer(address(vault), donationAmount);
     306 |         vm.stopPrank();
     307 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\base6decimals\SetupBase6DecimalsVault.sol:151`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     149 |             vm.startPrank(donor);
     150 |             IERC20(MC.USDE).approve(address(MC.SUSDE), donationAmount);
>>>  151 |             IERC20(MC.USDE).transfer(address(MC.SUSDE), donationAmount);
     152 |             vm.stopPrank();
     153 |         }
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\security\inflationAttack.t.sol:64`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      62 |         uint256 donationAmount = 1000 ether;
      63 |         vm.prank(attacker);
>>>   64 |         weth.transfer(address(vault), donationAmount);
      65 | 
      66 |         // 3. Update accounting to reflect donation
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\security\inflationAttack.t.sol:102`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     100 |         // Attacker donates amount
     101 |         vm.prank(attacker);
>>>  102 |         weth.transfer(address(vault), donationAmount);
     103 |         vault.processAccounting();
     104 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\security\inflationAttack.t.sol:134`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     132 |         // 2. Attacker donates to inflate
     133 |         vm.prank(attacker);
>>>  134 |         weth.transfer(address(vault), 1000 ether);
     135 |         vault.processAccounting();
     136 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\security\inflationAttack.t.sol:180`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     178 | 
     179 |         vm.prank(attacker);
>>>  180 |         weth.transfer(address(vault), 1000 ether);
     181 |         vault.processAccounting();
     182 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\security\inflationAttack.t.sol:223`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     221 |         uint256 donationAmount = 1000 ether;
     222 |         vm.prank(attacker);
>>>  223 |         weth.transfer(address(vault), donationAmount);
     224 |         vault.processAccounting();
     225 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\security\inflationAttack.t.sol:256`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     254 |         uint256 donationAmount = 100_000 ether; // Large enough to cause dilution
     255 |         vm.prank(attacker);
>>>  256 |         weth.transfer(address(vault), donationAmount);
     257 |         vault.processAccounting();
     258 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:66`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
      64 |         // alice transfers yield to vault
      65 |         vm.prank(alice);
>>>   66 |         IERC20(MC.USDC).transfer(address(vault), yield);
      67 | 
      68 |         uint256 performanceFeeRecipientSharesBefore =
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:116`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     114 |         vault.processAccounting();
     115 | 
>>>  116 |         IERC20(MC.USDC).transfer(address(vault), donationAmount);
     117 |         vm.stopPrank();
     118 | 
```
</details>

---

### [!] Fixed-Gas Transfer

- **File:** `test\unit\vault\vault6decimals\feehooks.t.sol:219`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** transfer()/send() has a fixed 2300 gas stipend which may fail for contracts with complex receive functions.

**Fix:** Use .call{value: amount} with proper error handling (checks-effects-interactions).

<details>
<summary>Code</summary>

```
     217 |         vault.processAccounting();
     218 | 
>>>  219 |         IERC20(MC.USDC).transfer(address(vault), donationAmount);
     220 |         vm.stopPrank();
     221 | 
```
</details>

---

## Performance (54)

### [~] Unoptimized Loop

- **File:** `script\VerifyMaxVault.s.sol:175`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     173 |         console.log("Vault rate (1 share in assets):", assetAmount);
     174 | 
>>>  175 |         for (uint256 i = 0; i < assets.length; i++) {
     176 |             address asset = assets[i];
     177 |             uint256 rate = rateProvider.getRate(asset);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\rules\BaseRules.sol:264`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     262 |             whitelist = new address[](currentWhitelist.length + 1);
     263 | 
>>>  264 |             for (uint256 i = 0; i < currentWhitelist.length; i++) {
     265 |                 whitelist[i] = currentWhitelist[i];
     266 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\rules\SafeRules.sol:42`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      40 |             bytes4[] memory funcSigs = new bytes4[](params.length);
      41 |             IVault.FunctionRule[] memory rules = new IVault.FunctionRule[](params.length);
>>>   42 |             for (uint256 i = 0; i < params.length; i++) {
      43 |                 contractAddresses[i] = params[i].contractAddress;
      44 |                 funcSigs[i] = params[i].funcSig;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\rules\SafeRules.sol:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      49 |             return;
      50 |         }
>>>   51 |         for (uint256 i = 0; i < params.length; i++) {
      52 |             setProcessorRule(vault_, params[i], false);
      53 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\rules\SafeRules.sol:61`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      59 |         IVault.FunctionRule[] memory rules = new IVault.FunctionRule[](rules_.length);
      60 | 
>>>   61 |         for (uint256 i = 0; i < rules_.length; i++) {
      62 |             contractsAddresses[i] = rules_[i].contractAddress;
      63 |             funcSigs[i] = rules_[i].funcSig;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\upgrades\GenerateUpgradeTxData.s.sol:242`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     240 | 
     241 |     function printAddressArray(address[] memory addresses) internal pure {
>>>  242 |         for (uint256 i = 0; i < addresses.length; i++) {
     243 |             if (i < addresses.length - 1) {
     244 |                 console.log("  %s,", vm.toString(addresses[i]));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\upgrades\GenerateUpgradeTxData.s.sol:252`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     250 | 
     251 |     function printUintArray(uint256[] memory values) internal pure {
>>>  252 |         for (uint256 i = 0; i < values.length; i++) {
     253 |             if (i < values.length - 1) {
     254 |                 console.log("  %s,", values[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\upgrades\GenerateUpgradeTxData.s.sol:262`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     260 | 
     261 |     function printBytesArray(bytes[] memory data) internal pure {
>>>  262 |         for (uint256 i = 0; i < data.length; i++) {
     263 |             if (i < data.length - 1) {
     264 |                 console.logBytes(data[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\RulesVerification.sol:28`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      26 |         vm.assertEq(rule.paramRules.length, expectedResult.paramRules.length, "paramRules length does not match");
      27 | 
>>>   28 |         for (uint256 i = 0; i < rule.paramRules.length; i++) {
      29 |             vm.assertEq(
      30 |                 uint256(rule.paramRules[i].paramType),
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\VaultVerification.sol:37`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      35 |         activeAssets[0] = MC.WETH;
      36 | 
>>>   37 |         for (uint256 i = 0; i < activeAssets.length; i++) {
      38 |             IVault.AssetParams memory asset = vault.getAsset(activeAssets[i]);
      39 |             vm.assertTrue(asset.active);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\VaultVerification.sol:52`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      50 |         inactiveAssets[6] = MC.MORPHO_MEV_CAPITAL_WETH;
      51 | 
>>>   52 |         for (uint256 i = 0; i < inactiveAssets.length; i++) {
      53 |             IVault.AssetParams memory asset = vault.getAsset(inactiveAssets[i]);
      54 |             vm.assertFalse(asset.active);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\VaultVerification.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      65 |             address buffer = vault.buffer();
      66 |             bool bufferFound = false;
>>>   67 |             for (uint256 i = 0; i < assets.length; i++) {
      68 |                 if (assets[i] == buffer) {
      69 |                     bufferFound = true;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\VaultVerification.sol:132`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     130 |         assets[6] = MC.WETH;
     131 | 
>>>  132 |         for (uint256 i = 0; i < assets.length; i++) {
     133 |             IVault.AssetParams memory asset = Withdrawer(withdrawer).getAsset(assets[i]);
     134 |             vm.assertTrue(asset.active);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\VaultVerification.sol:292`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     290 |         // Look up withdrawer by symbol
     291 |         address[] memory assets = vault.getAssets();
>>>  292 |         for (uint256 i = 0; i < assets.length; i++) {
     293 |             if (keccak256(bytes(IVault(assets[i]).symbol())) == keccak256(bytes(WithdrawerConfig.WITHDRAWER_SYMBOL))) {
     294 |                 return Withdrawer(payable(assets[i]));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `script\verification\VaultVerification.sol:310`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     308 |         vm.assertEq(assets.length, assertsList.length, "Viewer assets length should match vault assets length");
     309 | 
>>>  310 |         for (uint256 i = 0; i < assets.length; i++) {
     311 |             vm.assertEq(assets[i].asset, assertsList[i]);
     312 |             vm.assertEq(assets[i].canDeposit, vault.getAsset(assertsList[i]).active);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\library\VaultLib.sol:341`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     339 |             revert IVault.InvalidArray();
     340 |         }
>>>  341 |         for (uint256 i = 0; i < targetLength; i++) {
     342 |             setProcessorRule(target[i], functionSig[i], rule[i]);
     343 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\library\VaultLib.sol:384`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     382 |         uint256 assetListLength = assetList.length;
     383 | 
>>>  384 |         for (uint256 i = 0; i < assetListLength; i++) {
     385 |             uint256 balance = IERC20(assetList[i]).balanceOf(address(this));
     386 |             if (balance == 0) continue;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\library\VaultLib.sol:448`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     446 |         returnData = new bytes[](targetsLength);
     447 | 
>>>  448 |         for (uint256 i = 0; i < targetsLength; i++) {
     449 |             Guard.validateCall(targets[i], values[i], data[i]);
     450 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\module\Guard.sol:22`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      20 |         }
      21 | 
>>>   22 |         for (uint256 i = 0; i < rule.paramRules.length; i++) {
      23 |             if (rule.paramRules[i].paramType == IVault.ParamType.ADDRESS) {
      24 |                 address addressValue = abi.decode(data[4 + i * 32:], (address));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\module\Guard.sol:36`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      34 | 
      35 |     function _isInArray(address value, address[] storage array) private view returns (bool) {
>>>   36 |         for (uint256 i = 0; i < array.length; i++) {
      37 |             if (array[i] == value) {
      38 |                 return true;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\withdraws\BaseWithdrawer.sol:66`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      64 |         uint256 assetListLength = assetList.length;
      65 | 
>>>   66 |         for (uint256 i = 0; i < assetListLength; i++) {
      67 |             totalBaseBalance += asyncWithdrawalBalance(assetList[i]);
      68 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\withdraws\library\AsyncWithdrawalLib.sol:39`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      37 |         uint256 decimals = 10 ** VaultLib.getAssetStorage().assets[asset_].decimals;
      38 | 
>>>   39 |         for (uint256 i = 0; i < requests.length; i++) {
      40 |             if (!requests[i].processed) {
      41 |                 // NOTE: needs to be fixed - assumes no slashing for now,
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\withdraws\library\AsyncWithdrawalLib.sol:58`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      56 |         uint256[] memory requestIds = queue.getWithdrawalRequests(address(this));
      57 |         IWithdrawalQueue.WithdrawalRequestStatus[] memory statuses = queue.getWithdrawalStatus(requestIds);
>>>   58 |         for (uint256 i = 0; i < statuses.length; i++) {
      59 |             baseAssets += statuses[i].amountOfStETH;
      60 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\withdraws\library\OriginWithdrawalLib.sol:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      46 |      */
      47 |     function _removeRequestIds(uint256[] calldata idsToRemove) private {
>>>   48 |         for (uint256 i = 0; i < idsToRemove.length; i++) {
      49 |             _removeRequestId(idsToRemove[i]);
      50 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\withdraws\library\OriginWithdrawalLib.sol:60`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      58 |         uint256[] storage requestIds = getOriginWithdrawalStorage().requestIds;
      59 | 
>>>   60 |         for (uint256 i = 0; i < requestIds.length; i++) {
      61 |             if (requestIds[i] == id) {
      62 |                 requestIds[i] = requestIds[requestIds.length - 1]; // Move the last element to the current index
```
</details>

---

### [~] Unoptimized Loop

- **File:** `src\withdraws\library\OriginWithdrawalLib.sol:146`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     144 | 
     145 |         uint256[] storage requestIds = getOriginWithdrawalStorage().requestIds;
>>>  146 |         for (uint256 i = 0; i < requestIds.length; i++) {
     147 |             uint256 requestId = requestIds[i];
     148 |             IOETHVault.WithdrawalRequest memory request = oethVault.withdrawalRequests(requestId);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\aaveV3.spec.sol:72`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      70 |         address[] memory assets = vault.getAssets();
      71 |         uint256 wstEthIndex = type(uint256).max;
>>>   72 |         for (uint256 i = 0; i < assets.length; i++) {
      73 |             if (assets[i] == MC.WSTETH) {
      74 |                 wstEthIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\basicfunctionality.spec.sol:117`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     115 |         address[] memory assets = vault.getAssets();
     116 | 
>>>  117 |         for (uint256 i = 0; i < assets.length; i++) {
     118 |             {
     119 |                 bool skip = false;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\basicfunctionality.spec.sol:342`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     340 |         uint256[] memory initialRates = new uint256[](assets.length);
     341 |         uint256 initialTotalAssets = address(vault).balance;
>>>  342 |         for (uint256 i = 0; i < assets.length; i++) {
     343 |             initialBalances[i] = IERC20(assets[i]).balanceOf(address(vault));
     344 |             initialRates[i] = IProvider(vault.provider()).getRate(assets[i]);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\basicfunctionality.spec.sol:536`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     534 |             // Expand tokenIds array and add new tokenId
     535 |             uint256[] memory newTokenIds = new uint256[](tokenIds.length + 1);
>>>  536 |             for (uint256 i = 0; i < tokenIds.length; i++) {
     537 |                 newTokenIds[i] = tokenIds[i];
     538 |             }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\basicfunctionality.spec.sol:566`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     564 |         uint256 withdrawerETHBefore = address(withdrawer).balance;
     565 | 
>>>  566 |         for (uint256 i = 0; i < tokenIds.length; i++) {
     567 |             WithdrawerProcessorUtils.claimWithdrawalWstETH(withdrawer, PROCESSOR, tokenIds[i]);
     568 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\curve.spec.sol:54`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      52 | 
      53 |         // Add curve pool actions
>>>   54 |         for (uint256 i = 0; i < curvePools.length; i++) {
      55 |             // Exchange function
      56 |             bytes4 exchange = bytes4(keccak256("exchange(int128,int128,uint256,uint256)"));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\provider.spec.sol:247`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     245 |     function test_Provider_AllAssetsHaveRate() public view {
     246 |         address[] memory assets = vault.getAssets();
>>>  247 |         for (uint256 i = 0; i < assets.length; i++) {
     248 |             uint256 rate = provider.getRate(assets[i]);
     249 |             // The rate should be nonzero for supported assets
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\upgrade.spec.sol:150`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     148 |         // Assert assets are the same before and after
     149 |         assertEq(assetsAfter.length, assetsBefore.length, "Assets length should be the same before and after upgrade");
>>>  150 |         for (uint256 i = 0; i < assetsBefore.length; i++) {
     151 |             assertEq(assetsAfter[i], assetsBefore[i], "Asset at index should be the same before and after upgrade");
     152 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\viewer.spec.sol:47`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      45 |         assertEq(assetsInfo.length, assets.length);
      46 | 
>>>   47 |         for (uint256 i = 0; i < assets.length; i++) {
      48 |             IERC20Metadata asset = IERC20Metadata(assets[i]);
      49 |             IVaultViewer.AssetInfo memory assetInfo = assetsInfo[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\mainnet\viewer.spec.sol:77`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      75 |         assertEq(assetsInfo.length, assets.length);
      76 | 
>>>   77 |         for (uint256 i = 0; i < assets.length; i++) {
      78 |             IERC20Metadata asset = IERC20Metadata(assets[i]);
      79 |             IVaultViewer.AssetInfo memory assetInfo = assetsInfo[i];
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\helpers\ERC4626ComplianceTest.sol:38`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      36 | 
      37 |         // setup initial shares and assets for individual users
>>>   38 |         for (uint256 i = 0; i < N; i++) {
      39 |             address user = init.user[i];
      40 |             vm.assume(_isEOA(user));
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\helpers\SetupVault.sol:227`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     225 | 
     226 |         // Set up approval rules for all swapable assets
>>>  227 |         for (uint256 i = 0; i < swapableAssets.length; i++) {
     228 |             setApprovalRule(vault_, swapableAssets[i], address(swapper));
     229 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\helpers\SetupVault.sol:254`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     252 | 
     253 |         // Transfer 10 billion of each asset to the Swapper with appropriate decimals
>>>  254 |         for (uint256 i = 0; i < swapableAssets.length; i++) {
     255 |             address asset = swapableAssets[i];
     256 |             uint256 decimals = IERC20Metadata(asset).decimals();
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\helpers\TestHelpers.sol:14`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      12 |         uint256 activeCount = 0;
      13 | 
>>>   14 |         for (uint256 i = 0; i < allAssets.length; i++) {
      15 |             IVault.AssetParams memory assetInfo = vault.getAsset(allAssets[i]);
      16 |             if (assetInfo.active) {
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\accounting.t.sol:584`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     582 |         uint256 depositAmount = 1 ether + 1; // Odd amount for rounding
     583 | 
>>>  584 |         for (uint256 i = 0; i < 10; i++) {
     585 |             vm.prank(alice);
     586 |             uint256 shares = vault.deposit(depositAmount, alice);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\admin.t.sol:213`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     211 |         address[] memory assets = vault.getAssets();
     212 |         uint256 assetIndex;
>>>  213 |         for (uint256 i = 0; i < assets.length; i++) {
     214 |             if (assets[i] == address(asset)) {
     215 |                 assetIndex = i;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\admin.t.sol:222`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     220 |         // Store asset params before deletion
     221 |         IVault.AssetParams[] memory beforeStates = new IVault.AssetParams[](assets.length);
>>>  222 |         for (uint256 i = 0; i < assets.length; i++) {
     223 |             beforeStates[i] = vault.getAsset(assets[i]);
     224 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\admin.t.sol:236`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     234 |         // Get updated assets and compare with before states
     235 |         address[] memory updatedAssets = vault.getAssets();
>>>  236 |         for (uint256 i = 0; i < updatedAssets.length; i++) {
     237 |             IVault.AssetParams memory currentParams = vault.getAsset(updatedAssets[i]);
     238 | 
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\admin.t.sol:272`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     270 |         // Store asset params before deletion
     271 |         IVault.AssetParams[] memory beforeStates = new IVault.AssetParams[](assets.length);
>>>  272 |         for (uint256 i = 0; i < assets.length; i++) {
     273 |             beforeStates[i] = vault.getAsset(assets[i]);
     274 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\admin.t.sol:286`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     284 |         // Verify the last asset is removed and the rest of the assets match the original array (except the last one)
     285 |         address[] memory updatedAssets = vault.getAssets();
>>>  286 |         for (uint256 i = 0; i < updatedAssets.length; i++) {
     287 |             assertNotEq(updatedAssets[i], lastAsset, "Last asset should not be in the assets array anymore");
     288 |             assertEq(updatedAssets[i], assets[i], "Remaining assets should match the original array");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\processor.t.sol:184`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     182 |         assertEq(rule.paramRules.length, expectedResult.paramRules.length, "paramRules length does not match");
     183 | 
>>>  184 |         for (uint256 i = 0; i < rule.paramRules.length; i++) {
     185 |             assertEq(
     186 |                 uint256(rule.paramRules[i].paramType),
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\views.t.sol:82`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      80 |         address[] memory assets = vault.getAssets();
      81 | 
>>>   82 |         for (uint256 i = 0; i < assets.length; i++) {
      83 |             address asset = assets[i];
      84 |             assertEq(vault.getAsset(asset).index, i, "Bad Index");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\views.t.sol:128`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     126 | 
     127 |         // Verify that all other assets (not the deleted one) are still valid
>>>  128 |         for (uint256 i = 0; i < assets.length; i++) {
     129 |             if (assets[i] != assetToDelete) {
     130 |                 assertTrue(vault.hasAsset(assets[i]), "Other assets should still be valid after deletion");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\views.t.sol:153`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     151 |         // Verify that all existing assets are still valid
     152 |         address[] memory existingAssets = vault.getAssets();
>>>  153 |         for (uint256 i = 0; i < existingAssets.length; i++) {
     154 |             if (existingAssets[i] != newAsset) {
     155 |                 assertTrue(vault.hasAsset(existingAssets[i]), "Existing assets should still be valid after addition");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\withdrawAsset.t.sol:366`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     364 |         address[] memory assets = vault.getAssets();
     365 |         uint256 wethIndex = 0;
>>>  366 |         for (uint256 i = 0; i < assets.length; i++) {
     367 |             if (assets[i] == address(weth)) {
     368 |                 wethIndex = vault.getAsset(address(weth)).index;
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\withdrawfees.t.sol:659`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     657 |         uint256 amountLeftToRedeem = amountToRedeem;
     658 |         uint256 amountToRedeemBatch = amountLeftToRedeem / loopCount;
>>>  659 |         for (uint256 i = 0; i < loopCount; i++) {
     660 |             vm.startPrank(alice);
     661 |             uint256 assetsRedeemedOnce = vault.redeem(amountToRedeemBatch, alice, alice);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\unit\vault\withdrawfees.t.sol:732`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     730 |         uint256 amountLeftToRedeem = amountToRedeem;
     731 |         uint256 amountToRedeemBatch = amountLeftToRedeem / loopCount;
>>>  732 |         for (uint256 i = 0; i < loopCount; i++) {
     733 |             vm.startPrank(alice);
     734 |             uint256 assetsRedeemedOnce = vault.redeem(amountToRedeemBatch, alice, alice);
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\utils\ViewUtils.sol:48`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      46 |             IMetaHooks metaHooks = IMetaHooks(address(hooks));
      47 |             IHooks[] memory metaHooksUnderlyingHooks = metaHooks.getHooks();
>>>   48 |             for (uint256 i = 0; i < metaHooksUnderlyingHooks.length; i++) {
      49 |                 if (keccak256(abi.encodePacked(metaHooksUnderlyingHooks[i].name())) == keccak256(abi.encodePacked(name))) {
      50 |                     return address(metaHooksUnderlyingHooks[i]);
```
</details>

---

## Code Quality (18)

### [~] UNCLEAR require Error Message

- **File:** `script\DeployFeeHooks.s.sol:69`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      67 |         bool isConfigValid = vm.parseBool(vm.prompt("Is the config valid? (true/false)"));
      68 | 
>>>   69 |         require(isConfigValid, "Config is not valid");
      70 | 
      71 |         feeHooks = new FeeHooks(address(vault), owner, performanceFee, performanceFeeRecipient, config);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `script\VerifyMaxVault.s.sol:180`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     178 |             console.log("Asset:", asset, "has rate:", rate);
     179 |             // this is just a sanity heuristic, in theory it can be lower, in practice strats are at >= 1.0
>>>  180 |             require(rate >= 1e18, "Asset in getAssets does not have a getRate() greater than 1e18");
     181 |             // This is just a sanity heuristic, in theory it can be higher, in practice nothing is there yet at 300% gains.
     182 |             require(rate < 3 ether, "Asset in getAssets does not have a getRate() lower than 3 ether");
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `script\VerifyMaxVault.s.sol:182`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     180 |             require(rate >= 1e18, "Asset in getAssets does not have a getRate() greater than 1e18");
     181 |             // This is just a sanity heuristic, in theory it can be higher, in practice nothing is there yet at 300% gains.
>>>  182 |             require(rate < 3 ether, "Asset in getAssets does not have a getRate() lower than 3 ether");
     183 |         }
     184 |     }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `script\upgrades\GenerateUpgradeTxData.s.sol:109`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     107 |         data.proxy = ITransparentUpgradeableProxy(data.proxyAddress);
     108 |         data.proxyAdmin = ProxyUtils.getProxyAdmin(address(data.proxy));
>>>  109 |         require(vaultProxyAdmin == data.proxyAdmin, "ProxyAdmin mismatch");
     110 | 
     111 |         bytes memory emptyData = ""; // Empty data for now, can be customized if needed
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mainnet\mocks\MockBuffer.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      33 | 
      34 |     function withdraw(uint256 assets, address receiver, address owner) public returns (uint256) {
>>>   35 |         require(balances[owner] >= assets, "Insufficient balance");
      36 |         balances[owner] -= assets;
      37 |         _totalAssets -= assets;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mainnet\mocks\MockBuffer.sol:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      51 | 
      52 |     function redeem(uint256 shares, address receiver, address owner) public returns (uint256) {
>>>   53 |         require(balances[owner] >= shares, "Insufficient balance");
      54 |         balances[owner] -= shares;
      55 |         uint256 bufferAssets = convertToAssets(shares);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mainnet\mocks\MockBuffer.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     110 |     function transferFrom(address owner, address spender, uint256 value) public override returns (bool) {
     111 |         uint256 currentAllowance = allowance(owner, spender);
>>>  112 |         require(currentAllowance >= value, "ERC20: insufficient allowance");
     113 |         unchecked {
     114 |             _approve(owner, spender, currentAllowance - value);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mainnet\mocks\MockERC4626.sol:17`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      15 |      */
      16 |     function slash(uint256 fraction) external returns (uint256) {
>>>   17 |         require(fraction > 0, "Fraction must be greater than 0");
      18 |         require(fraction <= 1e18, "Fraction must be less than or equal to 1e18");
      19 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mainnet\mocks\MockERC4626.sol:18`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      16 |     function slash(uint256 fraction) external returns (uint256) {
      17 |         require(fraction > 0, "Fraction must be greater than 0");
>>>   18 |         require(fraction <= 1e18, "Fraction must be less than or equal to 1e18");
      19 | 
      20 |         uint256 totalAssetAmount = totalAssets();
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\mainnet\mocks\MockERC4626.sol:23`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      21 |         uint256 amountToSlash = (totalAssetAmount * fraction) / 1e18;
      22 | 
>>>   23 |         require(amountToSlash > 0, "Slash amount too small");
      24 | 
      25 |         // Transfer the assets to the caller
```
</details>

---

### [~] Address Is Contract Check

- **File:** `test\unit\helpers\ERC4626ComplianceTest.sol:289`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
     287 | 
     288 |     function _isEOA(address account) internal view returns (bool) {
>>>  289 |         return account.code.length == 0;
     290 |     }
     291 | 
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\mocks\MockBuffer.sol:35`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      33 | 
      34 |     function withdraw(uint256 assets, address receiver, address owner) public returns (uint256) {
>>>   35 |         require(balances[owner] >= assets, "Insufficient balance");
      36 |         balances[owner] -= assets;
      37 |         _totalAssets -= assets;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\mocks\MockBuffer.sol:53`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      51 | 
      52 |     function redeem(uint256 shares, address receiver, address owner) public returns (uint256) {
>>>   53 |         require(balances[owner] >= shares, "Insufficient balance");
      54 |         balances[owner] -= shares;
      55 |         uint256 bufferAssets = convertToAssets(shares);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\mocks\MockBuffer.sol:112`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
     110 |     function transferFrom(address owner, address spender, uint256 value) public override returns (bool) {
     111 |         uint256 currentAllowance = allowance(owner, spender);
>>>  112 |         require(currentAllowance >= value, "ERC20: insufficient allowance");
     113 |         unchecked {
     114 |             _approve(owner, spender, currentAllowance - value);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\mocks\MockST_ETH.sol:45`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      43 | 
      44 |     function submit(address /*_referral*/ ) public payable override returns (uint256) {
>>>   45 |         require(msg.value != 0, "ZERO_DEPOSIT");
      46 |         uint256 sharesAmount = getSharesByPooledEth(msg.value);
      47 |         _mint(msg.sender, sharesAmount);
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\mocks\MockST_ETH.sol:67`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      65 |     // Add rewards to simulate staking rewards being added to the pool
      66 |     function addRewards() public payable {
>>>   67 |         require(msg.value > 0, "Must send ETH");
      68 |         // Increase total pooled ether without minting new shares
      69 |         totalPooledEther += msg.value;
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\unit\vault\processor.t.sol:27`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
      25 | 
      26 |     function validate(address, uint256, bytes calldata) external view {
>>>   27 |         require(validationResult, "Validation failed");
      28 |     }
      29 | }
```
</details>

---

### [~] UNCLEAR require Error Message

- **File:** `test\utils\MathUtils.sol:7`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** require() with a generic/empty revert message makes debugging harder.

**Fix:** Use custom errors (Solidity 0.8.4+) with specific names for better error handling.

<details>
<summary>Code</summary>

```
       5 | 
       6 |     function log10(uint256 x) internal pure returns (uint256) {
>>>    7 |         require(x > 0, "log10 undefined for 0");
       8 | 
       9 |         uint256 result = 0;
```
</details>

---


---
*Generated by BugHunter*