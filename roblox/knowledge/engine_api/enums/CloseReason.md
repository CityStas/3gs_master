---
name: CloseReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the reason for the experience server shutdown."
---

# CloseReason

Specifies the reason for the experience server shutdown.

**Type:** enum

## Description

Specifies the reason for the experience server shutdown. This enum value is
the first parameter passed to functions bound by
[BindToClose()](/docs/reference/engine/classes/DataModel.md).

The **DeveloperShutdown** value must always be passed to functions bound by
[BindToClose()](/docs/reference/engine/classes/DataModel.md) when they're called in Studio.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | The server shut down for an unknown reason. |
| `RobloxMaintenance` | 1 | The server shut down for maintenance. |
| `DeveloperShutdown` | 2 | The experience developer has shut down the server, or functions bound by [BindToClose()](/docs/reference/engine/classes/DataModel.md) have been called inside Studio. |
| `DeveloperUpdate` | 3 | The experience developer has migrated the server to a new place version. |
| `ServerEmpty` | 4 | The last player has left and the experience is empty. |
| `OutOfMemory` | 5 | The experience has hit the memory limit for the game server. |
| `Moderation` | 6 | The server was shut down because the experience or place was taken down for moderation. |