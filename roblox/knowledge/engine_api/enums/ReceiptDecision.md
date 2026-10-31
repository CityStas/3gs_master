---
name: ReceiptDecision
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "`ReceiptDecision` works with MarketplaceService to indicate the acknowledgement of receipts."
---

# ReceiptDecision

`ReceiptDecision` works with [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) to indicate the
acknowledgement of receipts.

**Type:** enum

## Description

`ReceiptDecision` is the required return type for callbacks registered with
[MarketplaceService:BindReceiptHandler()](/docs/reference/engine/classes/MarketplaceService.md). The value you return
determines whether the receipt is marked as complete or remains unresolved for
future processing.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NotProcessedYet` | 0 | The receipt has not been processed yet. Returning this value keeps the receipt unresolved so it will be redelivered to the user's handler later, either during their existing session or the next time they join a server if they have disconnected. |
| `Processed` | 1 | The receipt has been processed and all benefits have been granted. The receipt is marked as complete and will not be delivered again. |