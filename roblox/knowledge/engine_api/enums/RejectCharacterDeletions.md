---
name: RejectCharacterDeletions
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether the server rejects client attempts to delete player characters."
---

# RejectCharacterDeletions

Controls whether the server rejects client attempts to delete player
characters.

**Type:** enum

## Description

Determines whether the server rejects client replication requests that would
delete player character models from the workspace. This enum is used by
[Workspace.RejectCharacterDeletions](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default behavior (currently equivalent to `Enabled`). |
| `Disabled` | 1 | The server does not reject character deletion requests from clients. |
| `Enabled` | 2 | The server rejects client attempts to delete player characters. |