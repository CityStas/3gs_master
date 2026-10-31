---
name: OrthographicMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Sets which screen axis OrthographicSize is applied to."
---

# OrthographicMode

Sets which screen axis [OrthographicSize](/docs/reference/engine/classes/Camera.md) is
applied to.

**Type:** enum

## Description

Used by [Camera](/docs/reference/engine/classes/Camera.md) to set which aspect of the
[ViewportSize](/docs/reference/engine/classes/Camera.md) is controlled by
[OrthographicSize](/docs/reference/engine/classes/Camera.md).

For example, when this property is set to [OrthographicMode.Vertical](/docs/reference/engine/enums/OrthographicMode.md),
the orthographic projection is scaled such that the vertical dimension spans
exactly [OrthographicSize](/docs/reference/engine/classes/Camera.md) studs, and the
horizontal dimension spans however many studs are needed to match.

This also controls which axis [ViewStretch](/docs/reference/engine/classes/Camera.md) will
stretch for orthographic cameras.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Vertical` | 0 | The screen's vertical axis will span exactly [OrthographicSize](/docs/reference/engine/classes/Camera.md) studs. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the horizontal axis. |
| `Horizontal` | 1 | The screen's horizontal axis will span exactly [OrthographicSize](/docs/reference/engine/classes/Camera.md) studs. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the vertical axis. |
| `Diagonal` | 2 | The screen diagonal will span exactly [OrthographicSize](/docs/reference/engine/classes/Camera.md) studs. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the horizontal axis. (In the initial beta, a bug makes it apply to both axes in a complex way.) |
| `MaxAxis` | 3 | The screen's longer axis will span exactly [OrthographicSize](/docs/reference/engine/classes/Camera.md) studs. The [ViewStretch](/docs/reference/engine/classes/Camera.md) will apply to the shorter axis. If both dimensions are identical, it will apply to the horizontal axis. |