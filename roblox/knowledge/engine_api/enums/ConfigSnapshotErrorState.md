---
name: ConfigSnapshotErrorState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the error state of a ConfigSnapshot object."
---

# ConfigSnapshotErrorState

Describes the error state of a [ConfigSnapshot](/docs/reference/engine/classes/ConfigSnapshot.md) object.

**Type:** enum

## Description

Indicates whether a [ConfigSnapshot](/docs/reference/engine/classes/ConfigSnapshot.md) loaded its configuration data
successfully. Read the [ConfigSnapshot.Error](/docs/reference/engine/classes/ConfigSnapshot.md) property (which defaults
to [ConfigSnapshotErrorState.None](/docs/reference/engine/enums/ConfigSnapshotErrorState.md)) to check for errors before calling
[ConfigSnapshot:GetValue()](/docs/reference/engine/classes/ConfigSnapshot.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Indicates the snapshot loaded successfully with no error; this is the default state. |
| `LoadFailed` | 1 | Indicates the snapshot failed to load because the underlying config service was unavailable at construction time. |