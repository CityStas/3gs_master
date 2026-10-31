---
name: InputBinding
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Defines which hardware binding should trigger the parent InputAction."
---

# Class: InputBinding

> Defines which hardware binding should trigger the parent [InputAction](/docs/reference/engine/classes/InputAction.md).

## Description

An `InputBinding` defines which hardware binding should trigger the parent
[InputAction](/docs/reference/engine/classes/InputAction.md), for example a key press, gamepad button, or tap on a
touch‑enabled device. There can be multiple `InputBinding` instances parented
to an [InputAction](/docs/reference/engine/classes/InputAction.md).

## Properties

### Property: InputBinding.Backward

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Specifies an alternate [KeyCode](/docs/reference/engine/enums/KeyCode.md) for dispatching directionally
"backward" inputs to [GetState()](/docs/reference/engine/classes/InputAction.md) and the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event of the parent
[InputAction](/docs/reference/engine/classes/InputAction.md). Only applies when the parent action's
[Type](/docs/reference/engine/classes/InputAction.md) is [Direction3D](/docs/reference/engine/enums/InputActionType.md), in
which case the dispatched value will be a [Vector3](/docs/reference/engine/datatypes/Vector3.md) with its
[Z](/docs/reference/engine/datatypes/Vector3.md) component between `0` and `1`.

### Property: InputBinding.ClampMagnitudeToOne

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Determines whether the binding normalizes the combined composite
directional vector to a maximum magnitude of `1` only if it exceeds that
length. This prevents diagonal composite inputs (for example
[Up](/docs/reference/engine/classes/InputBinding.md) and [Right](/docs/reference/engine/classes/InputBinding.md) pressed
simultaneously) from producing a magnitude greater than `1`, ensuring
consistent movement speed regardless of the keys held. Default is `true`.

This property only applies when the parent action's
[Type](/docs/reference/engine/classes/InputAction.md) is [Direction1D](/docs/reference/engine/enums/InputActionType.md),
[Direction2D](/docs/reference/engine/enums/InputActionType.md), or [Direction3D](/docs/reference/engine/enums/InputActionType.md).

Set this to `false` when input axes should remain independent of one
another, such as 3D freecam movement, or when combining inputs whose raw
values can exceed `1` (for example mouse wheel velocity) and you want to
handle scaling yourself.

### Property: InputBinding.DisplayImage

```json
{
  "type": "Content",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display",
  "capabilities": [
    "Input"
  ]
}
```

A custom [Content](/docs/reference/engine/datatypes/Content.md) image asset that represents this binding
visually (for example a gamepad button image or a stylized key graphic).

When empty (the default), no custom image is provided. Developers can use
[UserInputService:GetImageForKeyCode()](/docs/reference/engine/classes/UserInputService.md) to obtain a
platform-appropriate image. Use this together with
[InputAction.PreferredBinding](/docs/reference/engine/classes/InputAction.md) to build keybinding UI that
automatically reflects the player's active input device without manually
resolving which binding image to display.

### Property: InputBinding.DisplayName

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Display",
  "capabilities": [
    "Input"
  ]
}
```

A custom string that overrides the display name shown for this binding in
UI elements such as key prompts (for example "FIGHT" instead of the
default key name "F").

When empty (the default), no custom name is provided. Developers can use
[UserInputService:GetStringForKeyCode()](/docs/reference/engine/classes/UserInputService.md) to obtain the
platform-appropriate key name. Use this together with
[InputAction.PreferredBinding](/docs/reference/engine/classes/InputAction.md) to build keybinding UI that
automatically reflects the player's active input device without manually
resolving which binding name to display.

### Property: InputBinding.Down

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Specifies an alternate [KeyCode](/docs/reference/engine/enums/KeyCode.md) for dispatching directionally "down"
inputs to [GetState()](/docs/reference/engine/classes/InputAction.md) and the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event of the parent
[InputAction](/docs/reference/engine/classes/InputAction.md).

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction1D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a number
between `0` and `-1`.

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction2D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector2](/docs/reference/engine/datatypes/Vector2.md) with its [Y](/docs/reference/engine/datatypes/Vector2.md) component between `0`
and `-1`.

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction3D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector3](/docs/reference/engine/datatypes/Vector3.md) with its [Y](/docs/reference/engine/datatypes/Vector3.md) component between `0`
and `-1`.

Not applicable when the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Bool](/docs/reference/engine/enums/InputActionType.md).

### Property: InputBinding.Forward

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Specifies an alternate [KeyCode](/docs/reference/engine/enums/KeyCode.md) for dispatching directionally
"forward" inputs to [GetState()](/docs/reference/engine/classes/InputAction.md) and the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event of the parent
[InputAction](/docs/reference/engine/classes/InputAction.md). Only applies when the parent action's
[Type](/docs/reference/engine/classes/InputAction.md) is [Direction3D](/docs/reference/engine/enums/InputActionType.md), in
which case the dispatched value will be a [Vector3](/docs/reference/engine/datatypes/Vector3.md) with its
[Z](/docs/reference/engine/datatypes/Vector3.md) component between `0` and `-1`.

### Property: InputBinding.KeyCode

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Specifies the [KeyCode](/docs/reference/engine/enums/KeyCode.md) which triggers the parent
[InputAction](/docs/reference/engine/classes/InputAction.md). The code type should match the input action's
[Type](/docs/reference/engine/classes/InputAction.md), for example [KeyCode.E](/docs/reference/engine/enums/KeyCode.md) for an action
type of [Bool](/docs/reference/engine/enums/InputActionType.md) or [KeyCode.Thumbstick1](/docs/reference/engine/enums/KeyCode.md) for an
action type of [Direction2D](/docs/reference/engine/enums/InputActionType.md). Type mismatches will
either not fire the [InputAction](/docs/reference/engine/classes/InputAction.md) or the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event will receive a
converted value.

### Property: InputBinding.Left

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Specifies an alternate [KeyCode](/docs/reference/engine/enums/KeyCode.md) for dispatching directionally "left"
inputs to [GetState()](/docs/reference/engine/classes/InputAction.md) and the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event of the parent
[InputAction](/docs/reference/engine/classes/InputAction.md).

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction2D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector2](/docs/reference/engine/datatypes/Vector2.md) with its [X](/docs/reference/engine/datatypes/Vector2.md) component between `0`
and `-1`.

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction3D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector3](/docs/reference/engine/datatypes/Vector3.md) with its [X](/docs/reference/engine/datatypes/Vector3.md) component between `0`
and `-1`.

Not applicable when the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction1D](/docs/reference/engine/enums/InputActionType.md) or [Bool](/docs/reference/engine/enums/InputActionType.md).

### Property: InputBinding.PointerIndex

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

### Property: InputBinding.PressedThreshold

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Numerical value above which to fire an [InputAction](/docs/reference/engine/classes/InputAction.md) with a
[Type](/docs/reference/engine/classes/InputAction.md) of [Bool](/docs/reference/engine/enums/InputActionType.md), for example
when a gamepad trigger such as [KeyCode.ButtonL2](/docs/reference/engine/enums/KeyCode.md) exceeds `0.5`
(halfway pressed). Default is `0.5`.

This property must be greater than or equal to
[ReleasedThreshold](/docs/reference/engine/classes/InputBinding.md) or else it will
be clamped to [ReleasedThreshold](/docs/reference/engine/classes/InputBinding.md).

### Property: InputBinding.PrimaryModifier

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Specifies a [KeyCode](/docs/reference/engine/enums/KeyCode.md) that serves as a required modifier for the
binding. The [InputBinding](/docs/reference/engine/classes/InputBinding.md) will only trigger the parent
[InputAction](/docs/reference/engine/classes/InputAction.md) if this input is pressed prior to
[KeyCode](/docs/reference/engine/classes/InputBinding.md),
[UIButton](/docs/reference/engine/classes/InputBinding.md), or composite directions.

There is no ordering requirement between
[PrimaryModifier](/docs/reference/engine/classes/InputBinding.md) and
[SecondaryModifier](/docs/reference/engine/classes/InputBinding.md). If both
properties are set, both modifiers must be pressed to activate the
binding, but the order in which they are pressed does not matter.

If set to [KeyCode.Unknown](/docs/reference/engine/enums/KeyCode.md), no primary modifier is required.

### Property: InputBinding.ReleasedThreshold

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Numerical value below which to fire an [InputAction](/docs/reference/engine/classes/InputAction.md) with a
[Type](/docs/reference/engine/classes/InputAction.md) of [Bool](/docs/reference/engine/enums/InputActionType.md), for example
when a gamepad trigger such as [KeyCode.ButtonL2](/docs/reference/engine/enums/KeyCode.md) falls below `0.5`
(less than halfway pressed). Default is `0.2`.

This property must be less than or equal to
[PressedThreshold](/docs/reference/engine/classes/InputBinding.md) or else it will be
clamped to [PressedThreshold](/docs/reference/engine/classes/InputBinding.md).

### Property: InputBinding.ResponseCurve

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

A numerical value to control the sensitivity of gamepad thumbstick input
by applying a quadratic response curve. Commonly used for camera control
to make small thumbstick inputs more precise, while ramping up quickly to
allow for large movements with higher magnitude input.

Ranges between `1` to `10`, with higher values providing a more intense
curve. Default is `1`, at which input is returned exactly as received.

Only applicable when the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction2D](/docs/reference/engine/enums/InputActionType.md) and the
[KeyCode](/docs/reference/engine/classes/InputBinding.md) is
[Thumbstick1](/docs/reference/engine/enums/KeyCode.md) or
[Thumbstick2](/docs/reference/engine/enums/KeyCode.md).

### Property: InputBinding.Right

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Specifies an alternate [KeyCode](/docs/reference/engine/enums/KeyCode.md) for dispatching directionally
"right" inputs to [GetState()](/docs/reference/engine/classes/InputAction.md) and the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event of the parent
[InputAction](/docs/reference/engine/classes/InputAction.md).

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction2D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector2](/docs/reference/engine/datatypes/Vector2.md) with its [X](/docs/reference/engine/datatypes/Vector2.md) component between `0`
and `1`.

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction3D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector3](/docs/reference/engine/datatypes/Vector3.md) with its [X](/docs/reference/engine/datatypes/Vector3.md) component between `0`
and `1`.

Not applicable when the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction1D](/docs/reference/engine/enums/InputActionType.md) or [Bool](/docs/reference/engine/enums/InputActionType.md).

### Property: InputBinding.Scale

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

A scalar multiplier applied uniformly to every component of the output
value. Applies to [InputAction](/docs/reference/engine/classes/InputAction.md) types
[Direction1D](/docs/reference/engine/enums/InputActionType.md), [Direction2D](/docs/reference/engine/enums/InputActionType.md),
and [Direction3D](/docs/reference/engine/enums/InputActionType.md).

To scale individual components independently, use
[Vector2Scale](/docs/reference/engine/classes/InputBinding.md) (for
[Direction2D](/docs/reference/engine/enums/InputActionType.md)) or
[Vector3Scale](/docs/reference/engine/classes/InputBinding.md) (for
[Direction3D](/docs/reference/engine/enums/InputActionType.md)). When both `Scale` and a vector scale
are set, both are applied.

### Property: InputBinding.SecondaryModifier

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Specifies a [KeyCode](/docs/reference/engine/enums/KeyCode.md) that serves as a required modifier for the
binding. The [InputBinding](/docs/reference/engine/classes/InputBinding.md) will only trigger the parent
[InputAction](/docs/reference/engine/classes/InputAction.md) if this input is pressed prior to
[KeyCode](/docs/reference/engine/classes/InputBinding.md),
[UIButton](/docs/reference/engine/classes/InputBinding.md), or composite directions.

There is no ordering requirement between
[PrimaryModifier](/docs/reference/engine/classes/InputBinding.md) and
[SecondaryModifier](/docs/reference/engine/classes/InputBinding.md). If both
properties are set, both modifiers must be pressed to activate the
binding, but the order in which they are pressed does not matter.

If set to [KeyCode.Unknown](/docs/reference/engine/enums/KeyCode.md), no secondary modifier is required.

### Property: InputBinding.Type

```json
{
  "type": "InputBindingType",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Determines whether this `InputBinding` is triggered by hardware input
([Automatic](/docs/reference/engine/enums/InputBindingType.md)) or programmatically via
[Fire()](/docs/reference/engine/classes/InputBinding.md) ([Scriptable](/docs/reference/engine/enums/InputBindingType.md)).

When set to [Automatic](/docs/reference/engine/enums/InputBindingType.md) (default), the binding
responds to physical input devices (keyboard, mouse, gamepad, touch) based
on its [KeyCode](/docs/reference/engine/classes/InputBinding.md) or composite direction or UI
button properties.

When set to [Scriptable](/docs/reference/engine/enums/InputBindingType.md), the binding ignores
hardware input and instead receives state updates exclusively through the
[Fire()](/docs/reference/engine/classes/InputBinding.md) method.

### Property: InputBinding.UIButton

```json
{
  "type": "GuiButton",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

[GuiButton](/docs/reference/engine/classes/GuiButton.md) to connect to a boolean action.

### Property: InputBinding.UIModifier

```json
{
  "type": "GuiButton",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Specifies a [GuiButton](/docs/reference/engine/classes/GuiButton.md) that must be pressed for the
[InputBinding](/docs/reference/engine/classes/InputBinding.md) to trigger the parent [InputAction](/docs/reference/engine/classes/InputAction.md). Behaves
similarly to [PrimaryModifier](/docs/reference/engine/classes/InputBinding.md) and
[SecondaryModifier](/docs/reference/engine/classes/InputBinding.md), but accepts a UI
button reference rather than a [KeyCode](/docs/reference/engine/enums/KeyCode.md).

This is particularly useful for touch input where the relevant interaction
is defined by where on screen the touch originates, for example a dynamic
thumbstick that should only respond to touches that begin within a
specific UI region.

If `nil`, no modifier is required.

### Property: InputBinding.Up

```json
{
  "type": "KeyCode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Composite Directions",
  "capabilities": [
    "Input"
  ]
}
```

Specifies an alternate [KeyCode](/docs/reference/engine/enums/KeyCode.md) for dispatching directionally "up"
inputs to [GetState()](/docs/reference/engine/classes/InputAction.md) and the
[StateChanged](/docs/reference/engine/classes/InputAction.md) event of the parent
[InputAction](/docs/reference/engine/classes/InputAction.md).

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction1D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a number
between `0` and `1`.

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction2D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector2](/docs/reference/engine/datatypes/Vector2.md) with its [Y](/docs/reference/engine/datatypes/Vector2.md) component between `0`
and `1`.

When the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Direction3D](/docs/reference/engine/enums/InputActionType.md), the dispatched value will be a
[Vector3](/docs/reference/engine/datatypes/Vector3.md) with its [Y](/docs/reference/engine/datatypes/Vector3.md) component between `0`
and `1`.

Not applicable when the parent action's [Type](/docs/reference/engine/classes/InputAction.md) is
[Bool](/docs/reference/engine/enums/InputActionType.md).

### Property: InputBinding.Vector2Scale

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Amount by which each component of the output is independently linearly
scaled. Only applies when the parent action's
[Type](/docs/reference/engine/classes/InputAction.md) is [Direction2D](/docs/reference/engine/enums/InputActionType.md).

### Property: InputBinding.Vector3Scale

```json
{
  "type": "Vector3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

Amount by which each component of the output is independently linearly
scaled. Only applies when the parent action's
[Type](/docs/reference/engine/classes/InputAction.md) is [Direction3D](/docs/reference/engine/enums/InputActionType.md).

## Methods

### Method: InputBinding:Fire

**Signature:** `InputBinding:Fire(state: Variant): ()`

Programmatically updates the parent [InputAction](/docs/reference/engine/classes/InputAction.md) to the given state
and fires the appropriate signals ([Pressed](/docs/reference/engine/classes/InputAction.md),
[Released](/docs/reference/engine/classes/InputAction.md),
[StateChanged](/docs/reference/engine/classes/InputAction.md)).

This method can only be called on bindings with
[Type](/docs/reference/engine/classes/InputBinding.md) set to [Scriptable](/docs/reference/engine/enums/InputBindingType.md).
Calling it on an [Automatic](/docs/reference/engine/enums/InputBindingType.md) binding will throw an
error.

The `state` parameter must match the [Type](/docs/reference/engine/classes/InputAction.md) of the
parent [InputAction](/docs/reference/engine/classes/InputAction.md):

- [Bool](/docs/reference/engine/enums/InputActionType.md) expects a `boolean`
- [Direction1D](/docs/reference/engine/enums/InputActionType.md) expects a `number`
- [Direction2D](/docs/reference/engine/enums/InputActionType.md) expects a [Vector2](/docs/reference/engine/datatypes/Vector2.md)
- [Direction3D](/docs/reference/engine/enums/InputActionType.md) expects a [Vector3](/docs/reference/engine/datatypes/Vector3.md)
- [ViewportPosition](/docs/reference/engine/enums/InputActionType.md) expects a [Vector2](/docs/reference/engine/datatypes/Vector2.md)

Passing a mismatched type will cause an error. This method respects the
same deduplication rules as hardware input, as in consecutive calls with
the same state value will not re‑fire events.

The parent [InputAction](/docs/reference/engine/classes/InputAction.md) must be [Enabled](/docs/reference/engine/classes/InputAction.md)
and its ancestor [InputContext](/docs/reference/engine/classes/InputContext.md) must also be
[Enabled](/docs/reference/engine/classes/InputContext.md), otherwise the call is silently
ignored.

*Security: None · Thread Safety: Unsafe · Capabilities: Input · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `state` | `Variant` |  | The state value to apply; must match the parent action's [Type](/docs/reference/engine/classes/InputAction.md). |

**Returns:** `()`

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some