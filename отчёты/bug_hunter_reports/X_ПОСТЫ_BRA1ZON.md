# X (Twitter) — посты bra1zon / @XbMorty

Хэндл X: **@XbMorty**
CodeHawks: **bra1zon**
Рассылка (аудиты на продажу): **iskra.mod** — НЕ мешать с публичным hunt-брендом.

⚠️ Правило ответственного раскрытия: Lambda-находка отправлена через приватный GitHub Security tab, подтверждения/фикса ещё нет. В публичных постах **не называем протокол**, пока не подтвердили и не закрыли. Follow-up с названием — только после подтверждения проектом.

---

## Пост 1 — интро «я начал» (короткий, отдельный твит)

EN:
```
Started my journey as a smart-contract security researcher.

Focus: Solidity + EVM DeFi — vaults, hooks, accounting.

My first real finding is already in — a fee-escrow drain in a live DeFi hook (deposit path refunds the contract's whole native balance back to the caller).

Now: CodeHawks contests + building a verifiable track record, one finding at a time.
```

## Пост 2 — разбор находки (технический, имен не называем)

EN:
```
Found: fee-escrow drain via a refund-all pattern.

A `deposit()` path did:
  if (address(this).balance > 0) safeTransferETH(msg.sender, address(this).balance);

It refunds the CONTRACT's entire native balance to the caller — not just the caller's own surplus. A crafted call sweeps every fee/ETH the hook was holding in escrow.

Class: careless "refund surplus" logic -> whole-balance withdrawal.
Lessons I keep at front of mind:
  • refund only what the caller paid (track accounting), not balanceOf(this)
  • never let a user-facing refund touch accumulated protocol fees
```
(Follow-up с именем проекта — после подтверждения/фикса.)

## Пост 3 — прогресс на CodeHawks (после первого завершённого контеста)

EN:
```
First contest on CodeHawks 💪
Entered as bra1zon, submitted findings, judges agreed on one — placed.

Solidity/DeFi, small scope, big lessons:
  • write a PoC BEFORE you believe the finding
  • read the accounting invariants first, the math second

Grinding to the next one.
```

## Пост 4 — «строю трек-рекорд» (через несколько недель, когда есть 1-2 закрытых кейса)

EN:
```
Building a public track record in web3 security, one valid finding at a time.

• reported a fee-escrow drain in a live hook
• [X] contests on CodeHawks
• hunting in public audits + First Flights

If you're a protocol looking for an extra pair of eyes — I review the boring parts others skip. DMs open.
```

---

## Рекомендации
- Пины: закрепить Пост 1 (интро) или Пост 2 (разбор) — лучше Пост 2, он уникален и продаёт навык.
- Публиковать в моменты, когда аудитория США (13-19 UTC) для DeFi — больше откликов.
- Не смешивать iskra.mod (платные аудиты) и bra1zon/@XbMorty (публичная репутация) в одном треде.
- Когда Lambda подтвердит + зафиксит + (если повезёт) заплатит — выпустить Пост 2b с именем и статусом. Это самый сильный контент.