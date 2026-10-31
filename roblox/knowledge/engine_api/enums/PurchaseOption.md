---
name: PurchaseOption
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the type of purchase option in a bulk purchase prompt."
---

# PurchaseOption

Specifies the type of purchase option in a bulk purchase prompt.

**Type:** enum

## Description

The [PurchaseOption](/docs/reference/engine/enums/PurchaseOption.md) enum specifies the type of purchase option when
building the `PurchaseOptions` array for
[MarketplaceService:PromptBulkPurchase()](/docs/reference/engine/classes/MarketplaceService.md).

Use `TimedOption` for timed option durations and `Permanent` for standard
full-price purchase. Only one entry is allowed in `PurchaseOptions`; providing
more than one throws an error.

Do not hardcode duration values when using `TimedOption`. Always retrieve
available durations from the backend APIs and pass them through, as they may
change at any time.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `TimedOption` | 1 | A timed ownership option. The `Value` field specifies the duration in seconds. |
| `Permanent` | 2 | A permanent ownership purchase option. |