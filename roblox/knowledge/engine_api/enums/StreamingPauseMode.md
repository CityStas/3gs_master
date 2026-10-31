---
name: StreamingPauseMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how a client should handle not having enough content streamed in to continue playing properly."
---

# StreamingPauseMode

Determines how a client should handle not having enough content streamed in to
continue playing properly.

**Type:** enum

## Description

This enum is used to control [Workspace.StreamingPauseMode](/docs/reference/engine/classes/Workspace.md) behavior.
The `Disabled` mode indicates that gameplay continues unchanged even if player
does not have the minimum streaming radius available. In `ClientPhysicsPause`
mode, client-side physics is paused when the player doesn't have the minimum
radius present and resumed when the minimum radius is available.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior (subject to change). |
| `Disabled` | 1 | No change to gameplay due to streaming region availability. |
| `ClientPhysicsPause` | 2 | Client owned physics is paused. |