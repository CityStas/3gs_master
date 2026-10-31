---
name: InfoType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the type of product information returned by MarketplaceService:GetProductInfoAsync()."
---

# InfoType

Specifies the type of product information returned by
[MarketplaceService:GetProductInfoAsync()](/docs/reference/engine/classes/MarketplaceService.md).

**Type:** enum

## Description

Used to represent the possible information formats returnable by
[MarketplaceService:GetProductInfoAsync()](/docs/reference/engine/classes/MarketplaceService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Asset` | 0 | The product is an asset. |
| `Product` | 1 | Product such as a [Developer Product](/docs/en-us/production/monetization/developer-products.md). |
| `GamePass` | 2 | The product is a game pass. |
| `Subscription` | 3 | The product is a subscription. |
| `Bundle` | 4 | The product is a bundle. |