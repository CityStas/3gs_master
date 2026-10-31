---
name: ViewMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls which debug rendering visualization overlay is displayed in the Studio viewport via RenderSettings.ViewMode."
---

# ViewMode

Controls which debug rendering visualization overlay is displayed in the
Studio viewport via [RenderSettings.ViewMode](/docs/reference/engine/classes/RenderSettings.md).

**Type:** enum

## Description

Controls which debug rendering visualization overlay is drawn over the Studio
viewport. The visualization highlights overdraw for geometry, transparency, or
decals, or disables the overlay entirely. Assigned through
[RenderSettings.ViewMode](/docs/reference/engine/classes/RenderSettings.md), which defaults to [ViewMode.None](/docs/reference/engine/enums/ViewMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Disables the debug rendering visualization overlay; the default value of [RenderSettings.ViewMode](/docs/reference/engine/classes/RenderSettings.md). |
| `GeometryComplexity` | 1 | Displays an overdraw visualization highlighting geometric complexity across rendered surfaces. |
| `Transparent` | 2 | Displays an overdraw visualization highlighting surfaces rendered with transparency. |
| `Decal` | 3 | Displays an overdraw visualization highlighting surfaces rendered with decals. |