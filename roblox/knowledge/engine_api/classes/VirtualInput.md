---
name: VirtualInput
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Simulates mouse, keyboard, and pointer input as if it were performed by a real player."
---

# Class: VirtualInput

> Simulates mouse, keyboard, and pointer input as if it were performed by a real
> player.

## Description

[VirtualInput](/docs/reference/engine/classes/VirtualInput.md) simulates mouse, keyboard, and pointer input as if it
were performed by a real player. It is intended for **testing purposes only**
and can only be obtained by calling
[UserInputService:CreateVirtualInput()](/docs/reference/engine/classes/UserInputService.md).

All input methods throw a runtime error if the simulated input would interact
with Roblox's built-in UI ([CoreGui](/docs/reference/engine/classes/CoreGui.md)), such as the top bar, chat window,
or escape menu. This prevents automation tests from accidentally interfering
with system UI that players depend on.

## Methods

### Method: VirtualInput:SendKey

**Signature:** `VirtualInput:SendKey(isPressed: boolean, keyCode: KeyCode, isRepeatedKey?: boolean): ()`

This method injects a keyboard key press or release event, processed
identically to a real hardware key event.

This method throws a runtime error if [CoreGui](/docs/reference/engine/classes/CoreGui.md) has keyboard focus,
which includes a [TextBox](/docs/reference/engine/classes/TextBox.md) inside [CoreGui](/docs/reference/engine/classes/CoreGui.md) being focused, a
[CoreGui](/docs/reference/engine/classes/CoreGui.md) element selected for keyboard or gamepad navigation, or
the in-game escape menu being open. It also throws if the requested key is
permanently bound to a Roblox core action (for example, the
<kbd>Escape</kbd> key).

#### isRepeatedKey

Set `isRepeatedKey` to `true` only when simulating the OS auto-repeat
behavior that occurs while a player physically holds a key down which
fires a stream of repeated events after the initial key press. This is
meaningful only for text-manipulation keys: [KeyCode.Backspace](/docs/reference/engine/enums/KeyCode.md),
[KeyCode.Delete](/docs/reference/engine/enums/KeyCode.md), and the arrow keys ([KeyCode.Left](/docs/reference/engine/enums/KeyCode.md),
[KeyCode.Right](/docs/reference/engine/enums/KeyCode.md), [KeyCode.Up](/docs/reference/engine/enums/KeyCode.md), and [KeyCode.Down](/docs/reference/engine/enums/KeyCode.md)). Passing
`true` for any other key throws a runtime error.

For example, to simulate holding <kbd>Backspace</kbd> to delete multiple
characters, call:

- `SendKey(true, Enum.KeyCode.Backspace, false)` for the initial press
- `SendKey(true, Enum.KeyCode.Backspace, true)` in a loop for each
  repeated event
- `SendKey(false, Enum.KeyCode.Backspace, false)` for the release

Do **not** pass `isRepeatedKey` as `true` for the initial press or the
release. For any key that does not involve text editing (game action keys,
modifier keys, function keys, etc.), always pass `false`.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `isPressed` | `boolean` |  | Whether to simulate a key press (`true`) or a key release (`false`). |
| `keyCode` | `KeyCode` |  | The [KeyCode](/docs/reference/engine/enums/KeyCode.md) of the key to inject. |
| `isRepeatedKey` | `boolean` | `false` | Whether this is an auto-repeat event, as occurs when a key is held down. Only valid for text-manipulation keys such as [KeyCode.Backspace](/docs/reference/engine/enums/KeyCode.md), [KeyCode.Delete](/docs/reference/engine/enums/KeyCode.md), and the arrow keys. Defaults to `false`. |

**Returns:** `()`

### Method: VirtualInput:SendMouseButton

**Signature:** `VirtualInput:SendMouseButton(position: Vector2, button: UserInputType, isDown: boolean, repeatCount?: int): ()`

This method injects a mouse button press or release event at the given
screen-space position, processed identically to a real hardware mouse
event.

Only [UserInputType.MouseButton1](/docs/reference/engine/enums/UserInputType.md), [UserInputType.MouseButton2](/docs/reference/engine/enums/UserInputType.md),
and [UserInputType.MouseButton3](/docs/reference/engine/enums/UserInputType.md) are supported; passing any other
value throws a runtime error.

This method throws a runtime error if the specified position overlaps an
interactive [CoreGui](/docs/reference/engine/classes/CoreGui.md) element such as a button or an active overlay
in the top bar, chat window, or escape menu. It also throws if the
specified button is already in the requested state, for example pressing a
button that is already pressed.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | The screen-space position in pixels at which to inject the event. |
| `button` | `UserInputType` |  | The mouse button to use. Supported values are [UserInputType.MouseButton1](/docs/reference/engine/enums/UserInputType.md), [UserInputType.MouseButton2](/docs/reference/engine/enums/UserInputType.md), and [UserInputType.MouseButton3](/docs/reference/engine/enums/UserInputType.md). |
| `isDown` | `boolean` |  | Whether to simulate a button press (`true`) or a button release (`false`). |
| `repeatCount` | `int` | `0` | The consecutive-click count for multi-click detection, such as a double- or triple-click. Defaults to `0`. |

**Returns:** `()`

### Method: VirtualInput:SendMouseDelta

**Signature:** `VirtualInput:SendMouseDelta(positionDelta: Vector2): ()`

This method injects a relative mouse movement event, representing how far
the mouse moved rather than where it is on screen. This is intended for
use while the player's cursor is locked, such as in first-person camera
mode.

This method throws a runtime error when the cursor is not locked. To move
the cursor to an absolute screen position instead, use
[SendMousePosition()](/docs/reference/engine/classes/VirtualInput.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `positionDelta` | `Vector2` |  | The relative mouse movement in pixels along each axis. |

**Returns:** `()`

### Method: VirtualInput:SendMousePosition

**Signature:** `VirtualInput:SendMousePosition(position: Vector2): ()`

This method moves the virtual mouse cursor to the specified absolute
screen-space position, processed identically to a real hardware mouse-move
event.

This method throws a runtime error when the specified position overlaps an
interactive Roblox UI element (such as a button or active overlay in the
top bar, chat window, or escape menu).

To inject relative mouse movement while the cursor is locked, use
[SendMouseDelta()](/docs/reference/engine/classes/VirtualInput.md) instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | The target screen-space position in pixels. |

**Returns:** `()`

### Method: VirtualInput:SendPointerAction

**Signature:** `VirtualInput:SendPointerAction(position: Vector2, pointerAction: Dictionary): ()`

This method injects a pointer action event at the given screen-space
position. The `pointerAction` dictionary accepts the following keys:

- `Wheel` (number) — Scroll wheel delta. Positive values scroll forward,
  negative values scroll backward.
- `Pan` ([Vector2](/docs/reference/engine/datatypes/Vector2.md)) — Trackpad pan delta in pixels.
- `Pinch` (number) — Pinch-to-zoom delta. Positive values zoom in,
  negative values zoom out.

This method throws a runtime error if the specified position overlaps an
interactive Roblox UI element (such as a button or active overlay in the
top bar, chat window, or escape menu). If all values in `pointerAction`
are zero, the call returns without injecting any event.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | The screen-space position in pixels at which to inject the event. |
| `pointerAction` | `Dictionary` |  | A dictionary describing the pointer action to inject. Accepted keys are `Wheel` (number), `Pan` ([Vector2](/docs/reference/engine/datatypes/Vector2.md)), and `Pinch` (number). At least one key must have a non-zero value. |

**Returns:** `()`

### Method: VirtualInput:SendTextInput

**Signature:** `VirtualInput:SendTextInput(text: string): ()`

This method injects a text input event, routing the given string directly
to the focused [TextBox](/docs/reference/engine/classes/TextBox.md) or the experience's text input handler as
if the player typed it on a physical keyboard. This is useful for
populating text fields without needing to simulate individual key presses.

This method throws a runtime error if [CoreGui](/docs/reference/engine/classes/CoreGui.md) has keyboard focus,
which includes a [TextBox](/docs/reference/engine/classes/TextBox.md) inside [CoreGui](/docs/reference/engine/classes/CoreGui.md) being focused, a
[CoreGui](/docs/reference/engine/classes/CoreGui.md) element selected for keyboard or gamepad navigation, or
the in-game escape menu being open.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `text` | `string` |  | The string to inject as text input. |

**Returns:** `()`

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some