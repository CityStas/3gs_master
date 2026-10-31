---
name: HighlightDepthMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the Highlight effect displays with respect to other objects in the world."
---

# HighlightDepthMode

Controls how the [Highlight](/docs/reference/engine/classes/Highlight.md) effect displays with respect to other
objects in the world.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AlwaysOnTop` | 0 | Allows the [Highlight](/docs/reference/engine/classes/Highlight.md) to display regardless if there are objects between the camera and the highlighted object. This means the viewer is always able to see the highlight regardless of what is between the highlighted object and the camera. |
| `Occluded` | 1 | Hides the [Highlight](/docs/reference/engine/classes/Highlight.md) if there are objects between the camera and the highlighted object. This means the viewer is only able to see the object if there are no obstructing objects between the highlighted object and the camera's view. |