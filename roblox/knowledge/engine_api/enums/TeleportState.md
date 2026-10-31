---
name: TeleportState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the current teleportation state of a player."
---

# TeleportState

Determines the current teleportation state of a player.

**Type:** enum

## Description

Represents each stage of a player teleport as reported by the
[Player.OnTeleport](/docs/reference/engine/classes/Player.md) event. Scripts connect to [Player.OnTeleport](/docs/reference/engine/classes/Player.md)
to observe state changes throughout the teleport lifecycle and react
accordingly — for example, showing a loading screen when `InProgress` fires or
displaying an error when `Failed` fires.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `RequestedFromServer` | 0 | The server has requested that the client teleport. |
| `Started` | 1 | The client has started attempting to teleport. |
| `WaitingForServer` | 2 | The client is waiting for the server to respond to the teleport request. |
| `Failed` | 3 | The teleport failed. |
| `InProgress` | 4 | The teleport is currently in progress. The player usually disconnects and teleports to the destination after this. |