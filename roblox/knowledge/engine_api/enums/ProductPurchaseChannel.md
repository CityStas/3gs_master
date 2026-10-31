---
name: ProductPurchaseChannel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum which works with MarketplaceService to represent how the   user acquired the developer product."
---

# ProductPurchaseChannel

Enum which works with [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) to represent how the  
user acquired the developer product.

**Type:** enum

## Description

The `ProductPurchaseChannel` enum works with [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) and
represents how the user acquired the developer product.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `InExperience` | 1 | The purchase was made inside of an experience. |
| `ExperienceDetailsPage` | 2 | The purchase was made outside of an experience, on the **Store** tab of the experience details page. |
| `AdReward` | 3 | The product was rewarded to the user when they watched a video ad to completion. |
| `CommerceProduct` | 4 | The user acquired the product as a benefit of purchasing commerce merchandise from the developer of the experience. |