---
name: MarketplaceBulkPurchasePromptStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The status of the BulkPurchasePrompt after player interaction."
---

# MarketplaceBulkPurchasePromptStatus

The status of the BulkPurchasePrompt after player interaction.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Completed` | 1 | User confirmed the purchase and the transaction has been processed. |
| `Aborted` | 2 | User closed the prompt. |
| `Error` | 3 | User confirmed the purchase, but the transaction cannot be sent to the backend for processing. |