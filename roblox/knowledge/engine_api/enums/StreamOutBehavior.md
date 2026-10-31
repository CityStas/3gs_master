---
name: StreamOutBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how content is streamed out from Player clients."
---

# StreamOutBehavior

Determines how content is streamed out from [Player](/docs/reference/engine/classes/Player.md) clients.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior (subject to change). |
| `LowMemory` | 1 | Only stream out when memory is low. |
| `Opportunistic` | 2 | Stream out content that is significantly outside of the current [Workspace.StreamingTargetRadius](/docs/reference/engine/classes/Workspace.md). |