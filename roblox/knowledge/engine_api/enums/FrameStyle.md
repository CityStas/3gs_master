---
name: FrameStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to set the style of a Frame."
---

# FrameStyle

Used to set the style of a [Frame](/docs/reference/engine/classes/Frame.md).

**Type:** enum

## Description

The **FrameStyle** enum is used to set the style of a [Frame](/docs/reference/engine/classes/Frame.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Custom` | 0 | Uses the frame's [GuiObject.BackgroundColor3](/docs/reference/engine/classes/GuiObject.md), [GuiObject.BorderColor3](/docs/reference/engine/classes/GuiObject.md), and [GuiObject.BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md) properties to determine the frame's appearance. It has no padding; elements with the position [UDim2.new(0, 0, 0, 0)](/docs/reference/engine/datatypes/UDim2.md) will appear at the frame's top-left corner. |
| `ChatBlue` | 1 | Causes the frame to appear similar to a [Dialog](/docs/reference/engine/classes/Dialog.md) with its [Tone](/docs/reference/engine/classes/Dialog.md) property set to [DialogTone.Neutral](/docs/reference/engine/enums/DialogTone.md). Like **ChatGreen** and **ChatRed**, this has a padding of fifteen pixels on all sides. |
| `RobloxSquare` | 2 | Causes the frame to appear as a translucent dark gray rectangle with a padding of five pixels on all sides. |
| `RobloxRound` | 3 | Causes the frame to appear as a translucent dark gray rectangle with rounded edges. Like **RobloxSquare**, this has a padding of five pixels on all sides. |
| `ChatGreen` | 4 | Causes the frame to appear similar to a [Dialog](/docs/reference/engine/classes/Dialog.md) with its [Tone](/docs/reference/engine/classes/Dialog.md) property set to [DialogTone.Friendly](/docs/reference/engine/enums/DialogTone.md). Like **ChatBlue** and **ChatRed**, this has a padding of fifteen pixels on all sides. |
| `ChatRed` | 5 | Causes the frame to appear similar to a [Dialog](/docs/reference/engine/classes/Dialog.md) with its [Tone](/docs/reference/engine/classes/Dialog.md) property set to [DialogTone.Enemy](/docs/reference/engine/enums/DialogTone.md). Like **ChatBlue** and **ChatGreen**, this has a padding of fifteen pixels on all sides. |
| `DropShadow` | 6 | Causes the frame to appear as a translucent gray rectangle with blurred sides. The blur is more apparent on the bottom edge. It has a padding of eight pixels on all sides. |