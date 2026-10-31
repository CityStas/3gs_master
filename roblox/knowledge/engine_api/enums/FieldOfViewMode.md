---
name: FieldOfViewMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines which field-of-view angle a Camera holds constant when the viewport is resized."
---

# FieldOfViewMode

Determines which field-of-view angle a [Camera](/docs/reference/engine/classes/Camera.md) holds constant when the
viewport is resized.

**Type:** enum

## Description

[FieldOfViewMode](/docs/reference/engine/enums/FieldOfViewMode.md) controls which field-of-view (FOV) measurement the
[Camera](/docs/reference/engine/classes/Camera.md) treats as invariant when the viewport dimensions change. When
the viewport is resized, the engine recalculates the other FOV values to keep
the chosen axis constant. Used by
[FieldOfViewMode](/docs/reference/engine/classes/Camera.md), which defaults to
[FieldOfViewMode.Vertical](/docs/reference/engine/enums/FieldOfViewMode.md).

This also controls which axis [ViewStretch](/docs/reference/engine/classes/Camera.md) will
stretch for perspective cameras (which is currently always the horizontal
axis).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Vertical` | 0 | The camera holds its vertical field of view constant when the viewport is resized. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the horizontal axis. |
| `Diagonal` | 1 | The camera holds its diagonal field of view constant when the viewport is resized. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the horizontal axis. |
| `MaxAxis` | 2 | The camera holds the field of view along the longer viewport axis constant when the viewport is resized. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the horizontal axis. |