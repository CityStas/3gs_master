---
name: AspectType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by UIAspectRatioConstraint.AspectType to control sizing behavior."
---

# AspectType

Used by [UIAspectRatioConstraint.AspectType](/docs/reference/engine/classes/UIAspectRatioConstraint.md) to control sizing behavior.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `FitWithinMaxSize` | 0 | The object will be the maximum size possible within its own [AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md). |
| `ScaleWithParentSize` | 1 | The object's maximum size will be the size of the parent while still maintaining the aspect ratio. |