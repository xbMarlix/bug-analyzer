# HackenProof — стратегия и цели

## Решение (2026-09-06)
**Стратегия: сначала накрутка репутации, выплату отложить.**
Причина: все свежие Solidity-SC программы (Hinkal, Arcadia, ADI Predictstreet) требуют KYC для выплаты. Профиль зарегистрирован как **Brazil** (ложно), реально клиент из РФ/OFAC-зоны. KYC на выплате вскроет несоответствие и может заблокировать выплату. Поэтому HackenProof используется только для **построения репутации** (Rep 60 -> 150+), выплата — далёкий бонус, не трогаем KYC сейчас.

## Текущий профиль
- URL: https://hackenproof.com/hackers/iskramod
- Rank: 20506 | Reputation: 60 | Reports: 0
- Страна: Brazil (ложно) — риск при KYC/выплате, не обострять.

## Цель по репутации
- Сейчас: **60**
- Порог для следующих целей: **150** (Hinkal, ADI Predictstreet).
- Достаточно 1–2 валидных репорта (M/L) для роста репутации.

## Кандидаты (отсортировано по пригодности для новичка)

### ▶️ Primary: Arcadia Finance (accounts-v2 / lending-v2 / asset-managers)
- URL: https://hackenproof.com/programs/arcadia-finance-company-smart-contracts
- Порог репутации: **50** — клиент проходит (60). ✅
- KYC: требуется (для выплаты — отложено). POC: требуется. Взнос: $5.
- Bounty: до $25,000. Оплачено: $1,250 (очень мало — низкая конкуренция). Submissions: 124.
- Scope (репо скачаны в `протоколы\`):
  - `accounts-v2` — система маржинальных аккаунтов (AccountV3 73KB — ядро), 87 .sol
  - `lending-v2` — кредитование, 18 .sol
  - `asset-managers` — менеджеры активов, 50 .sol
- Deployed: Base, Optimism, Unichain. Только arcadia-код в скоупе (тесты/моки/скрипты/чужые импорты — вне скоупа).
- Вне скоупа: `SpotToMarginMigrator.sol` (Low).
- **Строгие правила северити (Primacy of Impact):**
  - Класс бага (reentrancy, overflow, reordering) — корневая причина, НЕ импакт.
  - Исход, который протокол спроектирован производить, — не уязвимость.
  - Trusted roles/admin/guardian/keeper/risk manager и CoW-солверы — вне скоупа (trusted third party).
  - Chainlink оракулы/sequencer — вне скоупа.
  - Exposure caps (maxExposure/maxUsdExposure) — риск-контроль, не солвенси-инвариант → Low/вне скоупа без realized loss.
  - Восстановимый/обратимый — никогда не Critical; временный DoS — Low.
  - Protocol/treasury-controlled funds — не user funds: разовый loss = Low, постоянный = Medium max.
  - Auction (Dutch) движки работают как спроектировано — не дефект.

### ⤴️ Secondary (после репутации 150): Hinkal
- URL: https://hackenproof.com/programs/hinkal-bug-bounty
- Порог: **150**. KYC: да. POC: да. Взнос: $5.
- Bounty: до $10,000. Оплачено: $0. Живой с 2026-09-03 (дней 3). Submissions: 58.
- Privacy-инфра для стабильных монет, ZK-цирки (Circom). Ищем: loss of funds, unauth minting/withdrawal, bypass proof, break privacy guarantees.

### ⤴️ Secondary (после репутации 150): ADI Predictstreet
- URL: https://hackenproof.com/programs/adi-predictstreet-smart-contracts
- Порог: **150**. KYC: да. POC: да. Взнос: $7.
- Bounty: до $10,000. Оплачено: $0. Prediction market (FIFA World Cup 2026). Submissions: 37.
- ⚠️ Репо `predictstreet-dd` — **invite-only** (запрос доступа на платформе). Связь с командой только через платформу (прямой контакт запрещён).

## Статус (2026-09-06) — пауза гринда HackenProof
Решение: публичное имя строим сейчас на **CodeHawks (ник bra1zon)** — участие в First Flights без KYC (только XP/лидерборд), профиль виден в X/GitHub. HackenProof НА ПАУЗЕ до появления реально валидной находки (не слать слабые репорты: $5 взнос + риск отказа без прироста репутации).

Цель по репутации 60 → 150+ сохраняется, но переносится: сначала закрываемся на конкурсах (CodeHawks First Flights / Cantina / Code4rena), где публичный трек-рекорд строится без KYC. Затем, имея 1-2 валидных H/M из конкурсов, возвращаемся с реальным кейсом.

## Результат аудита Arcadia (2026-09-06)
Прочесаны все 3 репо (accounts-v2 87 .sol, lending-v2 18 .sol, asset-managers 50 .sol). **Честный вывод: явных, защищаемых, in-scope находок High/Critical нет.** Код хорошо захарден (Pragma Labs + внешние аудиты; pool-balance-проверки до/после свопов, minLiquidity-гарды, капы комиссий initiator, консервативное округление, transient-storage reentrancy-гарды, версионирование).

Сильнейшие кандидаты и почему спорны (Arcadia = строгий Primacy of Impact):
1. **lending-v2 LendingPool.sol:1201-1221 `_calculateRewards`** — floor наград (init+term до 50% minimumMargin каждый) может превысить задуманный кап MAX_TOTAL_PENALTY (11% долга) для мелких долгов, экстракция из junior tranche. НО: ограничено owner-set `maxReward`, `minRewardWeight` капнут 50%, установка — привилегия trusted-роли → **класс "trusted/parameter risk" = вне скоупа**. Medium, low-med confidence, будут оспаривать.
2. **accounts-v2 Factory.sol:249 `safeTransferAccount` CEI** — стандартный OZ ERC721 паттерн, реентрансии нет из-за balance 0/1; скорее отклонят (класс-не-импакт).
3. **accounts-v2 StakedSlipstreamAM.sol:455/485 `balanceOf(this)` sweep** — подходит только для донат-токенов или дрейфа между позициями; под их правилами донат собственных токенов = не loss. Ниже Medium.
4. **accounts-v2 SlipstreamAM liquidity desync** + asset-managers CoW EIP-1271 — last-but: CoW требует злого solver-a = **trusted 3rd party = вне скоупа**.
5. Остальное (v4-ETH-учёт, Merkl balance-delta, rebalance initiator) — near-miss/вне скоупа/восстановимо.

**Практический вывод:** отправлять слабый/спорный репорт на Arcadia = $5 взнос + риск отклонения без прироста репутации. Не рекомендуется без PoC.

## Исключено
- Cetus/FlowX/Turbos — **Move (Sui)**, не Solidity. | Snowbridge — Rust/Substrate. | Starknet-трио — **Cairo**. | Zynk — Rust/Anchor + PAUSED. | SuperEarn — Solidity но PAUSED + 249 submissions. | Zeko — TypeScript + PAUSED. | LCX/Pionex/Poloniex/WEEX/NonKyc — web/CEX/API. | ADI zkVM — Rust/ZK-prover.
