---
name: StreamingIntegrityMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how a user's client should handle not having enough content streamed in."
---

# StreamingIntegrityMode

Determines how a user's client should handle not having enough content
streamed in.

**Type:** enum

## Description

This enum is used to control [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md)
behavior. For all modes, the replication focus defaults to be the local
character model unless explicitly set via [Player.ReplicationFocus](/docs/reference/engine/classes/Player.md).

Note that `MinimumRadiusPause` and `PauseOutsideLoadedArea` both set the
[Player.GameplayPaused](/docs/reference/engine/classes/Player.md) property when their respective pause logic is
triggered, and a default message is displayed on the client.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior (subject to change). |
| `Disabled` | 1 | Simulation of the replication focus is never paused, regardless of the amount of content streamed in on the client. |
| `MinimumRadiusPause` | 2 | All client-side simulation is paused when content is not streamed in up to the minimum radius. |
| `PauseOutsideLoadedArea` | 3 | Simulation of the replication focus is paused when any part of its bounding box is not in a streamed-in area. |