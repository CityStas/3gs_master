---
name: StrokeSizingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by UIStroke.StrokeSizingMode to determine whether the stroke's Thickness will be measured in pixels or be relative to the parent."
---

# StrokeSizingMode

Used by [UIStroke.StrokeSizingMode](/docs/reference/engine/classes/UIStroke.md) to determine whether the stroke's
[Thickness](/docs/reference/engine/classes/UIStroke.md) will be measured in pixels or be relative
to the parent.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `FixedSize` | 0 | [Thickness](/docs/reference/engine/classes/UIStroke.md) is measured in pixels. |
| `ScaledSize` | 1 | [Thickness](/docs/reference/engine/classes/UIStroke.md) is relative to minimum parent width or height. If stroke is on text, thickness is relative to font size. |