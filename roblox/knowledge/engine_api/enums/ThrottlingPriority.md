---
name: ThrottlingPriority
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Amount of throttling to apply."
---

# ThrottlingPriority

Amount of throttling to apply.

**Type:** enum

## Description

Controls the amount of throttling under the [HttpRbxApiService](/docs/reference/engine/classes/HttpRbxApiService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Standard throttling. |
| `ElevatedOnServer` | 1 | Less throttling if on the server. |
| `Extreme` | 2 | No throttling, absolutely no exceptions. |