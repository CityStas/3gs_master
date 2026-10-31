---
name: CurrencyType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The CurrencyType Enum is used with MarketplaceService to set the currency used."
---

# CurrencyType

The CurrencyType Enum is used with [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) to set the
currency used.

**Type:** enum

## Description

The CurrencyType Enum is used with [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) to set the
currency used. As tickets no longer exist on the Roblox platform, this enum is
**ignored** in most API that previously used it, such as
[PromptPurchase](/docs/reference/engine/classes/MarketplaceService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Use the default currency (Robux), equivalent to not specifying a currency. |
| `Robux` | 1 | Use Robux. |
| `Tix` | 2 | Use Tickets. |