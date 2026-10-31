---
name: InputSink
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how a GuiObject or GuiButton absorbs pointer and activation input events relative to GUI elements beneath it."
---

# InputSink

Controls how a [GuiObject](/docs/reference/engine/classes/GuiObject.md) or [GuiButton](/docs/reference/engine/classes/GuiButton.md) absorbs pointer and
activation input events relative to GUI elements beneath it.

**Type:** enum

## Description

Controls how a [GuiObject](/docs/reference/engine/classes/GuiObject.md) or [GuiButton](/docs/reference/engine/classes/GuiButton.md) absorbs pointer and
activation input events relative to GUI elements layered beneath it. Use this
enum with the [GuiObject.InputSink](/docs/reference/engine/classes/GuiObject.md) property, which defaults to
[InputSink.None](/docs/reference/engine/enums/InputSink.md) on [GuiObject](/docs/reference/engine/classes/GuiObject.md) and [InputSink.Activate](/docs/reference/engine/enums/InputSink.md) on
[GuiButton](/docs/reference/engine/classes/GuiButton.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The element does not sink any input events; pointer and activation events pass through to elements beneath it. |
| `Activate` | 1 | The element sinks activation input (button presses and taps) but allows hover, `MouseEnter`, and `MouseLeave` events to pass through to elements beneath it. |
| `All` | 100 | The element sinks all input events, preventing them from reaching any GUI element beneath it. |