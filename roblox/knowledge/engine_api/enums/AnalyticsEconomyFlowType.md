---
name: AnalyticsEconomyFlowType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the direction of currency flow in an economy event logged by AnalyticsService:LogEconomyEvent()."
---

# AnalyticsEconomyFlowType

Specifies the direction of currency flow in an economy event logged by
[AnalyticsService:LogEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md).

**Type:** enum

## Description

Passed as the `flowType` argument to
[AnalyticsService:LogEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md) to indicate whether an
in-experience currency transaction is adding currency to or removing currency
from a player's balance. Use [Source](/docs/reference/engine/enums/AnalyticsEconomyFlowType.md)
when the player gains currency (for example, purchasing coins with Robux or
earning gold from gameplay) and [Sink](/docs/reference/engine/enums/AnalyticsEconomyFlowType.md) when
the player spends currency (for example, buying an item from a shop).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Sink` | 0 | Currency is being removed from the player's account. |
| `Source` | 1 | Currency is being added to the player's account. |