---
name: ReplicateInstanceDestroySetting
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how `Instance:Destroy()` calls are replicated from server to clients."
---

# ReplicateInstanceDestroySetting

Controls how `Instance:Destroy()` calls are replicated from server to clients.

**Type:** enum

## Description

Determines the replication behavior the server uses when `Instance:Destroy()`
is called. This enum is used by
[Workspace.ReplicateInstanceDestroySetting](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default instance destroy replication behavior. |
| `Disabled` | 1 | Uses legacy instance destroy replication behavior. |
| `Enabled` | 2 | Uses improved instance destroy replication behavior. |