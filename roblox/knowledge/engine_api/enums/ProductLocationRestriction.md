---
name: ProductLocationRestriction
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the purchase locations permitted for an avatar item."
---

# ProductLocationRestriction

Specifies the purchase locations permitted for an avatar item.

**Type:** enum

## Description

Specifies the purchase locations permitted for an avatar item, as returned in
the `AllowedSaleLocations` field of the product info table from
[MarketplaceService:GetProductInfo()](/docs/reference/engine/classes/MarketplaceService.md). The item creator sets the
restriction on the Marketplace; it controls whether the item can be sold
in-experience and in which experiences. See [ProductLocationRestriction](/docs/reference/engine/enums/ProductLocationRestriction.md)
items for each restriction.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AvatarShop` | 0 | Item is purchasable only in the Marketplace. |
| `AllowedGames` | 1 | Item is purchasable in the Marketplace and experiences owned by the item creator. |
| `AllGames` | 2 | (Default) Item is purchasable in the Marketplace and all experiences. |