---
name: SubscriptionPaymentStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the payment outcome for a single entry in a user's subscription payment history."
---

# SubscriptionPaymentStatus

Describes the payment outcome for a single entry in a user's subscription
payment history.

**Type:** enum

## Description

The `SubscriptionPaymentStatus` enum describes whether a billing cycle for a
[MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) subscription was successfully charged or
subsequently refunded. It appears as the `subscriptionPaymentStatus` field on
each record returned by
[MarketplaceService:GetUserSubscriptionPaymentHistoryAsync()](/docs/reference/engine/classes/MarketplaceService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Paid` | 0 | Payment for the subscription has been received. |
| `Refunded` | 1 | Payment for the subscription has been refunded. |