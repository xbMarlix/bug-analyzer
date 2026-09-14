# BugHunter Report: contracts

**Generated:** 2026-09-05 23:54:09
**Project:** `C:\Users\123123\Desktop\BugHunter_Work\протоколы\lambda\contracts`
**Analyzers:** static, ast, solidity_semantic

## Summary

| Metric | Value |
|--------|-------|
| Files analyzed | 40 |
| Total lines | 5,738 |
| Bugs found | 13 |
| !! High | 2 |
| ! Medium | 1 |
| ~ Low | 10 |

### Languages Detected

- **solidity**: 40 files

## Logic (3)

### [!!] block.number For Randomness

- **File:** `test\HedgerCalibration.t.sol:97`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
      95 |         // Hyperliquid rejects prices with > 5 significant figures; verify the rounding was applied.
      96 |         uint256 p = uint256(limitPx);
>>>   97 |         while (p % 10 == 0 && p > 0) p /= 10;
      98 |         uint256 sigFigs;
      99 |         uint256 tmp2 = p;
```
</details>

---

### [!!] block.number For Randomness

- **File:** `test\LambdaHedger.t.sol:211`
- **Severity:** HIGH
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Using block.number as a randomness source is predictable and exploitable.

**Fix:** Use Chainlink VRF or a commit-reveal scheme for randomness.

<details>
<summary>Code</summary>

```
     209 |         // Count significant figures: divide out trailing zeros, count remaining digits.
     210 |         uint256 p = uint256(px);
>>>  211 |         while (p % 10 == 0 && p > 0) p /= 10;
     212 |         uint256 sigFigs = 0;
     213 |         uint256 tmp = p;
```
</details>

---

### [!] Balance Comparison

- **File:** `src\LambdaHook.sol:437`
- **Severity:** MEDIUM
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Comparing contract balance to determine behavior can be exploited by forced ETH sends.

**Fix:** Track balances internally instead of relying on contract.balance.

<details>
<summary>Code</summary>

```
     435 | 
     436 |         // Refund any native surplus (token0 paid from msg.value).
>>>  437 |         if (address(this).balance > 0) SafeTransferLib.safeTransferETH(msg.sender, address(this).balance);
     438 | 
     439 |         emit Deposited(id, to, liquidity, shares, amount0, amount1);
```
</details>

---

## Performance (9)

### [~] Unoptimized Loop

- **File:** `test\CoreWriterLib.t.sol:51`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      49 | 
      50 |         bytes memory body = new bytes(data.length - 4);
>>>   51 |         for (uint256 i = 0; i < body.length; i++) {
      52 |             body[i] = data[i + 4];
      53 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\CoreWriterLib.t.sol:95`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      93 |         bytes memory data = CoreWriterLib.encodeUsdClassTransfer(t);
      94 |         bytes memory body = new bytes(data.length - 4);
>>>   95 |         for (uint256 i = 0; i < body.length; i++) body[i] = data[i + 4];
      96 |         (uint64 ntl, bool toPerp) = abi.decode(body, (uint64, bool));
      97 |         assertEq(ntl, t.ntl, "ntl round-trips");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\HedgerCalibration.t.sol:117`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     115 |     {
     116 |         bytes memory body = new bytes(action.length - 4);
>>>  117 |         for (uint256 i = 0; i < body.length; i++) {
     118 |             body[i] = action[i + 4];
     119 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\LambdaHedger.t.sol:59`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
      57 |         bytes memory data = MockCoreWriter(CORE_WRITER).lastAction();
      58 |         bytes memory body = new bytes(data.length - 4);
>>>   59 |         for (uint256 i = 0; i < body.length; i++) {
      60 |             body[i] = data[i + 4];
      61 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\LambdaHedger.t.sol:262`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     260 |         // Decode body: (uint64 ntl, bool toPerp)
     261 |         bytes memory body = new bytes(sent.length - 4);
>>>  262 |         for (uint256 i = 0; i < body.length; i++) body[i] = sent[i + 4];
     263 |         (uint64 ntl, bool toPerp) = abi.decode(body, (uint64, bool));
     264 |         assertEq(ntl, 5_000_000, "ntl");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\LambdaHedger.t.sol:272`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     270 |         bytes memory sent = MockCoreWriter(CORE_WRITER).lastAction();
     271 |         bytes memory body = new bytes(sent.length - 4);
>>>  272 |         for (uint256 i = 0; i < body.length; i++) body[i] = sent[i + 4];
     273 |         (, bool toPerp) = abi.decode(body, (uint64, bool));
     274 |         assertFalse(toPerp, "toPerp=false for withdrawMargin");
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\LambdaReactive.t.sol:113`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     111 |     {
     112 |         bytes memory body = new bytes(payload.length - 4);
>>>  113 |         for (uint256 i = 0; i < body.length; i++) {
     114 |             body[i] = payload[i + 4];
     115 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\fork\LambdaForkE2E.t.sol:263`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     261 |     {
     262 |         bytes memory body = new bytes(payload.length - 4);
>>>  263 |         for (uint256 i = 0; i < body.length; i++) {
     264 |             body[i] = payload[i + 4];
     265 |         }
```
</details>

---

### [~] Unoptimized Loop

- **File:** `test\fork\LambdaHedgerForkHyperEVM.t.sol:156`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** Loops in Solidity cost gas per iteration. Consider bounds and caching state variables in memory.

**Fix:** Cache state variables in memory before the loop, and consider if the loop can be avoided.

<details>
<summary>Code</summary>

```
     154 |     {
     155 |         bytes memory body = new bytes(action.length - 4);
>>>  156 |         for (uint256 i = 0; i < body.length; i++) {
     157 |             body[i] = action[i + 4];
     158 |         }
```
</details>

---

## Code Quality (1)

### [~] Address Is Contract Check

- **File:** `script\HookMiner.sol:37`
- **Severity:** LOW
- **Confidence:** 70%
- **Analyzer:** static

**Problem:** .code.length == 0 is unreliable for confirming an address is EOA, especially after deployment.

**Fix:** Consider upgrading to a better EOA detection or avoiding this check entirely.

<details>
<summary>Code</summary>

```
      35 |             salt = bytes32(i);
      36 |             hookAddress = computeAddress(deployer, salt, initCodeHash);
>>>   37 |             if (uint160(hookAddress) & FLAG_MASK == flags && hookAddress.code.length == 0) {
      38 |                 return (hookAddress, salt);
      39 |             }
```
</details>

---


---
*Generated by BugHunter*