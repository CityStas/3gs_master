---
name: AutomaticSize
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "UI objects with AutomaticSize enabled will increase in size up to maximum size allowed by the parent (if there is one) and no smaller than the Size property bounds."
---

# AutomaticSize

UI objects with [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) enabled will
increase in size up to maximum size allowed by the parent (if there is one)
and no smaller than the [Size](/docs/reference/engine/classes/GuiObject.md) property bounds.

**Type:** enum

## Description

UI objects with [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) enabled will
increase in size up to maximum size allowed by the parent (if there is one)
and no smaller than the [Size](/docs/reference/engine/classes/GuiObject.md) property bounds. To enable
[AutomaticSize](/docs/reference/engine/enums/AutomaticSize.md), set the value to an enum value other than `None`.

This enum is used by [GuiObject.AutomaticSize](/docs/reference/engine/classes/GuiObject.md) and
[ScrollingFrame.AutomaticCanvasSize](/docs/reference/engine/classes/ScrollingFrame.md) to determine whether and how
resizing occurs based on child content.

For more information, see
[Automatic Sizing](/docs/en-us/ui/size-modifiers.md#automatic-sizing).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Default sizing behavior. |
| `X` | 1 | Automatically resize element along the **X** axis to fit child contents. |
| `Y` | 2 | Automatically resize element along the **Y** axis to fit child contents. Text objects will only resize along the **Y** axis if their `TextWrapped` property is enabled. |
| `XY` | 3 | Automatically resize element along the **X** and **Y** axes to fit child contents. |