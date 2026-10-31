---
name: SubscriptionExpirationReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the reason a user's subscription has expired."
---

# SubscriptionExpirationReason

Describes the reason a user's subscription has expired.

**Type:** enum

## Description

[SubscriptionExpirationReason](/docs/reference/engine/enums/SubscriptionExpirationReason.md) describes why a subscription entered the
[Expired](/docs/reference/engine/enums/SubscriptionState.md) state. It appears under the
`ExpirationReason` key in the `ExpirationDetails` table returned by
[MarketplaceService:GetUserSubscriptionDetailsAsync()](/docs/reference/engine/classes/MarketplaceService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ProductInactive` | 0 | The subscription product is inactive. |
| `ProductDeleted` | 1 | The subscription product was deleted. |
| `SubscriberCancelled` | 2 | The subscriber cancelled the subscription. |
| `SubscriberRefunded` | 3 | The subscriber received a refund that ended the subscription. |
| `Lapsed` | 4 | The subscription expired because payment lapsed. |