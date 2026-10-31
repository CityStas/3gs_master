---
name: UIFlexMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with UIFlexItem.FlexMode to define how the parent GuiObject grows or shrinks."
---

# UIFlexMode

Used with [UIFlexItem.FlexMode](/docs/reference/engine/classes/UIFlexItem.md) to define how the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md) grows or shrinks.

**Type:** enum

## Description

Used with [UIFlexItem.FlexMode](/docs/reference/engine/classes/UIFlexItem.md) to define how the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md) grows or shrinks with available space in the container.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) is unaffected and neither shrinks nor grows. |
| `Grow` | 1 | Sets an effective `1:0` grow‑shrink ratio on the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). Objects set to `Grow` never shrink below their basis size, so overflow may occur if the container becomes smaller than the flex line's combined basis size. |
| `Shrink` | 2 | Sets an effective `0:1` grow‑shrink ratio on the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). Objects set to `Shrink` never grow above their basis size, so underflow may occur if the container becomes larger than the flex line's combined basis size. |
| `Fill` | 3 | Sets an effective `1:1` grow‑shrink ratio on the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). This setting ensures the flex line always fills the container, even if the container size changes. |
| `Custom` | 4 | Enables the [GrowRatio](/docs/reference/engine/classes/UIFlexItem.md) and [ShrinkRatio](/docs/reference/engine/classes/UIFlexItem.md) properties for the [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md), allowing for relative growth or shrinking of the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) in a ratio compared to other flex objects also under control of a [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md). |