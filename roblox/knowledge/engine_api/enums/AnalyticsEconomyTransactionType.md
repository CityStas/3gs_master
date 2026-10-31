---
name: AnalyticsEconomyTransactionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Categorizes the context of an in-experience economic transaction for use with AnalyticsService:LogEconomyEvent()."
---

# AnalyticsEconomyTransactionType

Categorizes the context of an in-experience economic transaction for use with
[AnalyticsService:LogEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md).

**Type:** enum

## Description

This enum provides recommended values for the `transactionType` parameter of
[AnalyticsService:LogEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md). Because `transactionType` is typed
as a string, pass the `Name` property of the enum item (for example,
[AnalyticsEconomyTransactionType.IAP.Name](/docs/reference/engine/enums/AnalyticsEconomyTransactionType.md)). Using these standard values
enables Roblox-provided analytics charts to break down economy data by
transaction context. Custom strings are also accepted; the experience is
limited to 20 unique transaction types total.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `IAP` | 0 | Represents a source of currency purchased via Robux, for example in-experience "gold" purchased for Robux. |
| `Shop` | 1 | Purchases within a shop, for example in-experience "coins" used to buy an item within the experience. |
| `Gameplay` | 2 | Currency earned or paid through gameplay, for example in-experience "gold" earned from winning a match. |
| `ContextualPurchase` | 3 | Purchase with direct context to a reward, for example in-experience "gold" used to purchase an extra life. |
| `TimedReward` | 4 | Time-based reward, for example in-experience "gold" rewarded for logging in daily. |
| `Onboarding` | 5 | Transaction related to onboarding, for example in-experience "gold" rewarded for completing the tutorial. |