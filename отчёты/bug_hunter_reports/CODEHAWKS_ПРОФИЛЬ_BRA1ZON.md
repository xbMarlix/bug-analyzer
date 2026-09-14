# CodeHawks профиль — bra1zon

Публичный профиль: https://codehawks.cyfrin.io
Ник: **bra1zon** (единый бренд для hunt-репутации, отделён от iskra.mod в холодной рассылке).

## Должность (Headline — одна строка)

EN:
`Smart-contract security researcher · Solidity · found fee-escrow drain in LambdaHook (reported)`

RU (себе):
`Исследователь безопасности смарт-контрактов · Solidity · нашёл fee-escrow drain в LambdaHook (зарепорчено)`

## О себе (Bio)

EN:
```
Independent smart-contract security researcher, building a public track record one finding at a time. Focused on Solidity and EVM DeFi — vaults, hooks, accounting.

First portfolio finding: identified a fee-escrow drain in the Lambda protocol's hook contract (LambdaHook.sol). The deposit path refunds the contract's entire native balance (`address(this).balance`) back to the caller instead of the caller's own surplus, allowing a crafted call to sweep accumulated fees held in the hook. Reported to the project.

Currently sharpening skills on CodeHawks (First Flights + contests) and hunting in public audits. Long-term: consistently find in-scope issues in live DeFi codebases and grow a verifiable audit track record.
```

RU (себе — для понимания):
```
Независимый исследователь безопасности смарт-контрактов, строю публичный трек-рекорд находка за находкой. Фокус — Solidity и EVM DeFi: ваулты, хуки, бухгалтерия.

Первая находка для портфолио: определил увод fee-escrow в hook-контракте протокола Lambda (LambdaHook.sol). Путь deposit возвращает ВЕСЬ нативный баланс контракта (`address(this).balance`) отправителю вместо его собственного surplus, что позволяет crafted-вызовом вымести накопленные комиссии, удерживаемые в hook. Зарепорчено в проект.

Сейчас оттачиваю навыки на CodeHawks (First Flights + контесты) и охочусь в публичных аудитах. Долгосрочно: находить валидные in-scope баги в живых DeFi-кодбазах и наращивать проверяемый трек-рекорд.
```

## Рекомендации
- Тон честный и конкретный. Не пишем «confirmed»/«paid» — кейс зарепорчен, но не подтверждён/оплачен проектом.
- После первых валидных First Flight / контest — возвращайся сюда, чтобы дописать результаты (место в лидерборде, судьи).
- Lighthouse: обнови bio после 1-го подтверждённого валидного нахождения (H/M).