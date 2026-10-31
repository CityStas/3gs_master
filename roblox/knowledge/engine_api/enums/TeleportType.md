---
name: TeleportType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the type of teleport destination for a TeleportService teleport call."
---

# TeleportType

Determines the type of teleport destination for a [TeleportService](/docs/reference/engine/classes/TeleportService.md)
teleport call.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ToPlace` | 0 | The teleport destination is a place (no specific instance). |
| `ToInstance` | 1 | The teleport destination is an instance of a place. |
| `ToReservedServer` | 2 | The destination of the teleport is a reserved server (a place instance that is reserved for a select group of players). |
| `ToVIPServer` | 3 | The teleport destination is a VIP (player-owned private) server instance. |
| `ToInstanceBack` | 4 | The teleport destination is a previously-visited place instance (back navigation). |