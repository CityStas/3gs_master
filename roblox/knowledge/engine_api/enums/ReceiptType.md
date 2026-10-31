---
name: ReceiptType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "`ReceiptType` is used to work with server-sided receipt processing."
---

# ReceiptType

`ReceiptType` is used to work with server-sided receipt processing.

**Type:** enum

## Description

`ReceiptType` works with [MarketplaceService:BindReceiptHandler()](/docs/reference/engine/classes/MarketplaceService.md) to
indicate the different type of receipts a developer can bind to for
processing. When you call
[BindReceiptHandler](/docs/reference/engine/classes/MarketplaceService.md), you pass a
`ReceiptType` to specify which kind of receipt your handler should process.

`DeveloperProduct` is used for developer product purchases and provides a
`BindReceiptHandler`-based alternative to the legacy
[ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) callback.
`RobuxTransferSender` and `RobuxTransferReceiver` are used for Robux
transfers, described below.

For Robux transfers initiated with
[PromptRobuxTransferAsync](/docs/reference/engine/classes/MarketplaceService.md),
two receipts are generated: one for the sender (`RobuxTransferSender`) and one
for the receiver (`RobuxTransferReceiver`). You should register handlers for
both types to fully process a transfer.

Transfer receipts are delivered to whichever server the user is currently in
once the transfer settles (the user does not need to rejoin). If the user is
offline when the transfer settles, the receipt is delivered the next time they
join a server. See
[BindReceiptHandler](/docs/reference/engine/classes/MarketplaceService.md) for
details.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `DeveloperProduct` | 0 | Used for processing receipts from developer product purchases made with [PromptProductPurchase](/docs/reference/engine/classes/MarketplaceService.md). The receipt includes `ProductId`, `CurrencyType`, and `CurrencySpent` fields. A handler bound for this type processes developer product receipts in place of the legacy [ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) callback; receipts with no matching bound handler fall through to `ProcessReceipt`. |
| `RobuxTransferSender` | 1 | Used for processing receipts for the user who initiated a Robux transfer. The receipt's `PlayerId` is the sender's user ID and includes a `TransferRequestId` field. Delivered immediately if the transfer settles synchronously. If receiver approval is required, delivered to the server the sender is currently in once the receiver accepts, or on the sender's next session join if they are offline. |
| `RobuxTransferReceiver` | 2 | Used for processing receipts for the user who received Robux via a transfer. The receipt's `PlayerId` is the receiver's user ID and includes a `TransferRequestId` field. Delivered to the server the receiver is currently in once the transfer settles, or on their next session join if they are offline. |