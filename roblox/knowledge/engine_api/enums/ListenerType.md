---
name: ListenerType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Defines where and how the listener is positioned when picking up spatial audio."
---

# ListenerType

Defines where and how the listener is positioned when picking up spatial
audio.

**Type:** enum

## Description

Defines where and how the listener is positioned when picking up spatial
audio. Used in [SoundService.SetListener](/docs/reference/engine/classes/SoundService.md) and
[SoundService.GetListener](/docs/reference/engine/classes/SoundService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Camera` | 0 | Uses the world CFrame of `workspace.CurrentCamera`. |
| `CFrame` | 1 | Uses a specified world CFrame. |
| `ObjectPosition` | 2 | Uses the world position of an instance and the rotation of `workspace.CurrentCamera`. |
| `ObjectCFrame` | 3 | Uses the world CFrame from an instance. |