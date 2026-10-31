---
name: BorderMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by GuiObject.BorderMode to determine where borders are placed."
---

# BorderMode

Used by [GuiObject.BorderMode](/docs/reference/engine/classes/GuiObject.md) to determine where borders are placed.

**Type:** enum

## Description

Determines in what matter the border of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) is laid out
relative to its actual dimensions. It is used by the property of the same
name, [GuiObject.BorderMode](/docs/reference/engine/classes/GuiObject.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Outline` | 0 | As [GuiObject.BorderSizePixel](/docs/reference/engine/classes/GuiObject.md) increases, the border grows outward. The dimensions of the GuiObject's contents do not change. |
| `Middle` | 1 | As [GuiObject.BorderSizePixel](/docs/reference/engine/classes/GuiObject.md) increases, the border grows evenly inward and outward. The dimensions of the GuiObject's contents are reduced at a 1:1 ratio. |
| `Inset` | 2 | As [GuiObject.BorderSizePixel](/docs/reference/engine/classes/GuiObject.md) increases, the border grows evenly inward only. The dimensions of the GuiObject's contents are reduced at a 1:2 ratio. |