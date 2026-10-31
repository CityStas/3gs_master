---
name: TeleportMethod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies which TeleportService API method initiated a teleport."
---

# TeleportMethod

Identifies which [TeleportService](/docs/reference/engine/classes/TeleportService.md) API method initiated a teleport.

**Type:** enum

## Description

`TeleportMethod` identifies the [TeleportService](/docs/reference/engine/classes/TeleportService.md) call that initiated a
given teleport. Each enum item corresponds to a specific public
[TeleportService](/docs/reference/engine/classes/TeleportService.md) method.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `TeleportToSpawnByName` | 0 | Teleport was initiated by [TeleportService:TeleportToSpawnByName()](/docs/reference/engine/classes/TeleportService.md), which sends a player to a named [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) in a place. |
| `TeleportToPlaceInstance` | 1 | Teleport was initiated by [TeleportService:TeleportToPlaceInstance()](/docs/reference/engine/classes/TeleportService.md), which sends a player to a specific running server instance identified by its `instanceId`. |
| `TeleportToPrivateServer` | 2 | Teleport was initiated by [TeleportService:TeleportToPrivateServer()](/docs/reference/engine/classes/TeleportService.md), a deprecated method that sends players to a reserved server using a legacy access code. |
| `TeleportPartyAsync` | 3 | Teleport was initiated by [TeleportService:TeleportPartyAsync()](/docs/reference/engine/classes/TeleportService.md), which sends a group of players to a place together. |
| `TeleportToVIPServer` | 4 | Teleport was initiated to a VIP (creator-owned private) server; the engine upgrades the method tag to this value when VIP server credentials are present at teleport time. |
| `TeleportToInstanceBack` | 5 | Teleport was initiated by back-navigation, returning a player to a specific prior place instance. |
| `TeleportUnknown` | 6 | Fallback value used when the teleport method cannot be determined. |