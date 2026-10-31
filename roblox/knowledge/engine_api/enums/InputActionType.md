---
name: InputActionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used by InputAction.Type to determine which input data type the InputAction will receive."
---

# InputActionType

This enum is used by [InputAction.Type](/docs/reference/engine/classes/InputAction.md) to determine which input data
type the [InputAction](/docs/reference/engine/classes/InputAction.md) will receive.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Bool` | 0 | The [InputAction](/docs/reference/engine/classes/InputAction.md) will receive boolean values from button inputs, for example `true`/`false` on press/release from inputs such as [KeyCode.ButtonA](/docs/reference/engine/enums/KeyCode.md) or [KeyCode.E](/docs/reference/engine/enums/KeyCode.md). This setting also exposes the [UIButton](/docs/reference/engine/classes/InputBinding.md) property on child [InputBindings](/docs/reference/engine/classes/InputBinding.md), allowing you to easily hook up press or release of a [GuiButton](/docs/reference/engine/classes/GuiButton.md) for the action. |
| `Direction1D` | 1 | The [InputAction](/docs/reference/engine/classes/InputAction.md) will receive numerical values, generally from analog gamepad triggers such as [KeyCode.ButtonL2](/docs/reference/engine/enums/KeyCode.md) or [KeyCode.ButtonR2](/docs/reference/engine/enums/KeyCode.md). This setting also exposes the [Up](/docs/reference/engine/classes/InputBinding.md) and [Down](/docs/reference/engine/classes/InputBinding.md) properties on child [InputBindings](/docs/reference/engine/classes/InputBinding.md), allowing for boolean inputs or "1D" inputs as composite directions for the action. |
| `Direction2D` | 2 | The [InputAction](/docs/reference/engine/classes/InputAction.md) will receive [Vector2](/docs/reference/engine/datatypes/Vector2.md) values, generally from thumbstick inputs such as [KeyCode.Thumbstick1](/docs/reference/engine/enums/KeyCode.md) and [KeyCode.Thumbstick2](/docs/reference/engine/enums/KeyCode.md). This setting also exposes the [Up](/docs/reference/engine/classes/InputBinding.md), [Down](/docs/reference/engine/classes/InputBinding.md), [Left](/docs/reference/engine/classes/InputBinding.md), and [Right](/docs/reference/engine/classes/InputBinding.md) properties on child [InputBindings](/docs/reference/engine/classes/InputBinding.md), allowing for "2D" inputs as composite directions for the action. |
| `Direction3D` | 3 | The [InputAction](/docs/reference/engine/classes/InputAction.md) will receive [Vector3](/docs/reference/engine/datatypes/Vector3.md) values from inputs assigned to the [Up](/docs/reference/engine/classes/InputBinding.md), [Down](/docs/reference/engine/classes/InputBinding.md), [Left](/docs/reference/engine/classes/InputBinding.md), [Right](/docs/reference/engine/classes/InputBinding.md), [Forward](/docs/reference/engine/classes/InputBinding.md), and/or [Backward](/docs/reference/engine/classes/InputBinding.md) properties on child [InputBindings](/docs/reference/engine/classes/InputBinding.md), allowing for "3D" inputs as composite directions for the action. |
| `ViewportPosition` | 4 | The [InputAction](/docs/reference/engine/classes/InputAction.md) will receive [Vector2](/docs/reference/engine/datatypes/Vector2.md) values representing the absolute pixel (**X**, **Y**) coordinates of a pointer input in the viewport. |