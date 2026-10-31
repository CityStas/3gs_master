---
name: SubscriptionPeriod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the billing period for a MarketplaceService subscription product."
---

# SubscriptionPeriod

Describes the billing period for a [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) subscription
product.

**Type:** enum

## Description

Describes the recurring billing interval of a subscription product sold
through [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md). The value is returned in the
`SubscriptionPeriod` field of the dictionary produced by
[MarketplaceService:GetSubscriptionProductInfoAsync()](/docs/reference/engine/classes/MarketplaceService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Month` | 0 | The subscription renews on a monthly billing cycle. |