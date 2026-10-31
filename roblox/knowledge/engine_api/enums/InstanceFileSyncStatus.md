---
name: InstanceFileSyncStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the file sync status of an Instance."
---

# InstanceFileSyncStatus

Describes the file sync status of an Instance.

**Type:** enum

## Description

Describes the file sync status of an [Instance](/docs/reference/engine/classes/Instance.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NotSynced` | 0 | The [Instance](/docs/reference/engine/classes/Instance.md) is not being synced or errored. |
| `Errored` | 1 | The [Instance](/docs/reference/engine/classes/Instance.md) is a sync root that has errored and stopped syncing. |
| `SyncedAsRoot` | 2 | The [Instance](/docs/reference/engine/classes/Instance.md) is being synced as the root of a sync tree. |
| `SyncedAsDescendant` | 3 | The [Instance](/docs/reference/engine/classes/Instance.md) is being synced because it is a descendant of a sync root. |
| `AncestorErrored` | 4 | The [Instance](/docs/reference/engine/classes/Instance.md) is not currently being synced because the root of its sync tree is `Errored`. |