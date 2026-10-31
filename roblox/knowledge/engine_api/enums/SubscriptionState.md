---
name: SubscriptionState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current subscription state of a user's in-experience subscription product."
---

# SubscriptionState

Describes the current subscription state of a user's in-experience
subscription product.

**Type:** enum

## Description

The `SubscriptionState` enum describes the current subscription state of a
user with respect to a specific in-experience subscription product. It is
returned in the `SubscriptionState` key of the table from
[MarketplaceService:GetUserSubscriptionDetailsAsync()](/docs/reference/engine/classes/MarketplaceService.md), which must be
called from a server-side [Script](/docs/reference/engine/classes/Script.md). See [SubscriptionState](/docs/reference/engine/enums/SubscriptionState.md) for the
lifecycle values (never subscribed, active with or without renewal, renewal
payment pending, and expired).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NeverSubscribed` | 0 | User has never subscribed to the product. |
| `SubscribedWillRenew` | 1 | Subscription is active and will renew. |
| `SubscribedWillNotRenew` | 2 | Subscription is active and will not renew. |
| `SubscribedRenewalPaymentPending` | 3 | Subscription is active and renewal payment is pending. |
| `Expired` | 4 | Subscription has expired. |