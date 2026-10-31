---
name: PluginConnectionTargetType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the data model type that the remote end of a PluginConnection runs in."
---

# PluginConnectionTargetType

Describes the data model type that the remote end of a
[PluginConnection](/docs/reference/engine/classes/PluginConnection.md) runs in.

**Type:** enum

## Description

An enum describing the possible relationships a target data model of a
[PluginConnection](/docs/reference/engine/classes/PluginConnection.md) can have to the current data model.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Edit` | 0 | The target data model is an edit-session data model which spawned this test data model. |
| `Test` | 1 | The target data model is a test (simulation/playtest) data model spawned from this edit data model. |