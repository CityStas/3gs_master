---
name: PropertyStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the validation state of a property as displayed in Roblox Studio's Properties panel."
---

# PropertyStatus

Indicates the validation state of a property as displayed in Roblox Studio's
Properties panel.

**Type:** enum

## Description

Indicates the validation state of a property as displayed in Roblox Studio's
Properties panel. This enum is returned by the `PropertyStatusStudio` property
on [Instance](/docs/reference/engine/classes/Instance.md) and by `GetOverrideStatus()` on [MaterialService](/docs/reference/engine/classes/MaterialService.md) to
communicate whether a property's current value is valid, has a recoverable
issue, or is in an error state.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Ok` | 0 | The property value is valid; no status indicator is shown in Studio. |
| `Warning` | 1 | The property value has a recoverable issue; Studio displays a warning indicator on the instance. |
| `Error` | 2 | The property value is invalid and cannot be resolved; Studio displays an error indicator on the instance. |