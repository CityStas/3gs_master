---
name: BenefitType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the type of virtual benefit granted to a user when they purchase a commerce product through CommerceService."
---

# BenefitType

Indicates the type of virtual benefit granted to a user when they purchase a
commerce product through [CommerceService](/docs/reference/engine/classes/CommerceService.md).

**Type:** enum

## Description

The `BenefitType` enum classifies the virtual items that a user receives as
part of a [CommerceService](/docs/reference/engine/classes/CommerceService.md) commerce product purchase. Each benefit
entry returned by [CommerceService:GetCommerceProductInfoAsync()](/docs/reference/engine/classes/CommerceService.md)
includes a `BenefitType` field that identifies whether the granted item is a
developer product, an individual avatar asset, or an avatar bundle.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `DeveloperProduct` | 0 | The benefit is a developer product whose receipt is delivered through [MarketplaceService:BindReceiptHandler()](/docs/reference/engine/classes/MarketplaceService.md) upon purchase of a commerce product. |
| `AvatarAsset` | 1 | The benefit is a single avatar asset granted to the user's inventory upon purchase of a commerce product. |
| `AvatarBundle` | 2 | The benefit is an avatar bundle granted to the user's inventory upon purchase of a commerce product. |