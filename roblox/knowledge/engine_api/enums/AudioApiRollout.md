---
name: AudioApiRollout
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to determine whether voice chat is represented and controlled by AudioDeviceInput objects."
---

# AudioApiRollout

Used to determine whether voice chat is represented and controlled by
[AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) objects.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Disabled` | 0 | Voice chat will use an internal voice chat implementation that is automatic and hidden. |
| `Automatic` | 1 | Currently means the same thing as `Disabled`, but will be updated to mean `Enabled` in the future. |
| `Enabled` | 2 | Voice chat can be customized or controlled via [AudioDeviceInputs](/docs/reference/engine/classes/AudioDeviceInput.md). |