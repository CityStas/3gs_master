---
name: ProductPurchaseDecision
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The `ProductPurchaseDecisionEnum` works with MarketplaceService to indicate the status of the sale of developer products."
---

# ProductPurchaseDecision

The `ProductPurchaseDecisionEnum` works with [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) to
indicate the status of the sale of developer products.

**Type:** enum

## Description

The `ProductPurchaseDecisionEnum` is used to work with
[MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md), and the sale of developer products.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NotProcessedYet` | 0 | The purchase request has been sent but not yet processed. |
| `PurchaseGranted` | 1 | The purchase has been processed and granted to the user who initiated the purchase request. |