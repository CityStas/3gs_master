---
name: UserInputService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "`UserInputService` is primarily used to detect the input types available on a user's device, as well as detect input events."
---

# Class: UserInputService

> `UserInputService` is primarily used to detect the input types available on a
> user's device, as well as detect input events.

## Description

`UserInputService` is primarily used to detect the input types available on a
user's device, as well as detect input events. It allows you to perform
different actions depending on the device and, in turn, provide the best
experience for the end user.

As this service is intended for client-side usage only, its properties,
methods, and events can only be used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md), a
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) required by a [LocalScript](/docs/reference/engine/classes/LocalScript.md), or a [Script](/docs/reference/engine/classes/Script.md)
with [RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md).

## Properties

### Property: UserInputService.AccelerometerEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user's device has an accelerometer, a
component found in most mobile devices that measures acceleration (change
in speed).

If the device has an enabled accelerometer, you can get its current
acceleration by using the
[GetDeviceAcceleration()](/docs/reference/engine/classes/UserInputService.md)
method or track when the device's acceleration changes through the
[DeviceAccelerationChanged](/docs/reference/engine/classes/UserInputService.md)
event.

**Move a Ball using the Accelerometer**

This code adds a force on a part so that it falls in the direction of actual
gravity relative to the user's device. In order for this example to work as
expected, it must be placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) and the user's device
must have an accelerometer.

```lua
local Workspace = game:GetService("Workspace")
local UserInputService = game:GetService("UserInputService")

local ball = script.Parent:WaitForChild("Ball")
local mass = ball:GetMass()
local gravityForce = ball:WaitForChild("GravityForce")

local function moveBall(gravity)
	gravityForce.Force = gravity.Position * Workspace.Gravity * mass
end

if UserInputService.AccelerometerEnabled then
	UserInputService.DeviceGravityChanged:Connect(moveBall)
end
```

### Property: UserInputService.GamepadEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user's device has an available
gamepad. If `true`, you can use gamepad‑related methods such as
[GetConnectedGamepads()](/docs/reference/engine/classes/UserInputService.md).

For seamless cross-platform compatibility on mixed-input devices, see
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input.

### Property: UserInputService.GyroscopeEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user's device has a gyroscope, a
component found in most mobile devices that detects orientation and
rotational speed.

If the device has a gyroscope, you can incorporate it into your experience
using the [GetDeviceRotation()](/docs/reference/engine/classes/UserInputService.md)
method or track when the device's rotation changes through the
[DeviceRotationChanged](/docs/reference/engine/classes/UserInputService.md)
event.

### Property: UserInputService.KeyboardEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user's device has a keyboard
available. If `true`, you can use key‑related methods such as
[IsKeyDown()](/docs/reference/engine/classes/UserInputService.md) or
[GetKeysPressed()](/docs/reference/engine/classes/UserInputService.md).

For seamless cross-platform compatibility on mixed-input devices, see
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input.

### Property: UserInputService.MouseBehavior

```json
{
  "type": "MouseBehavior",
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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property sets how the user's mouse behaves based on the
[MouseBehavior](/docs/reference/engine/enums/MouseBehavior.md) enum. It can be set to three values:

- [MouseBehavior.Default](/docs/reference/engine/enums/MouseBehavior.md) &mdash; The mouse moves freely around the
  user's screen.
- [MouseBehavior.LockCenter](/docs/reference/engine/enums/MouseBehavior.md) &mdash; The mouse is locked and cannot
  move from the center of the user's screen.
- [MouseBehavior.LockCurrentPosition](/docs/reference/engine/enums/MouseBehavior.md) &mdash; The mouse is locked and
  cannot move from its current position on the user's screen at the time
  of locking.

The value of this property does not affect the sensitivity of events
tracking mouse movement. For example,
[GetMouseDelta](/docs/reference/engine/classes/UserInputService.md) returns the same
[Vector2](/docs/reference/engine/datatypes/Vector2.md) screen position in pixels regardless of whether the
mouse is locked or able to move freely around the user's screen. As a
result, default scripts like those controlling the camera are not impacted
by this property.

This property is overridden if a [GuiButton](/docs/reference/engine/classes/GuiButton.md) with
[Modal](/docs/reference/engine/classes/GuiButton.md) enabled is [Visible](/docs/reference/engine/classes/GuiButton.md)
unless the player's right mouse button is down.

Note that if the mouse is locked,
[InputChanged](/docs/reference/engine/classes/UserInputService.md) will still fire when
the player moves the mouse and will pass in the delta that the mouse
attempted to move by. Additionally, if the player is kicked from the
experience, the mouse will be forcefully unlocked.

### Property: UserInputService.MouseDeltaSensitivity

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property determines the sensitivity of the user's [Mouse](/docs/reference/engine/classes/Mouse.md). It
can be used to adjust the sensitivity of events tracking mouse movement,
such as [GetMouseDelta()](/docs/reference/engine/classes/UserInputService.md).

This property does not affect the movement of the mouse icon, nor the
camera sensitivity that the user has selected for their client.

This property has a maximum value of `10` and a minimum value of `0`. When
sensitivity is `0`, events that track the mouse's movement will still fire
but all parameters and properties indicating the change in mouse position
will return `0`.

### Property: UserInputService.MouseEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user's device has a mouse available.
If `true`, you can use mouse‑related methods such as
[GetMouseLocation()](/docs/reference/engine/classes/UserInputService.md).

For seamless cross-platform compatibility on mixed-input devices, see
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input.

### Property: UserInputService.MouseIcon

```json
{
  "type": "ContentId",
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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property determines the content ID of the image for the user's mouse
icon. If blank, a default arrow pointer is used. While the cursor hovers
over certain UI objects such as an [ImageButton](/docs/reference/engine/classes/ImageButton.md),
[TextButton](/docs/reference/engine/classes/TextButton.md), [TextBox](/docs/reference/engine/classes/TextBox.md), or [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md), this
image will be overridden and temporarily ignored.

To hide the cursor entirely, do **not** use a transparent image; instead,
set [MouseIconEnabled](/docs/reference/engine/classes/UserInputService.md) to `false`.

**Custom Mouse Icon**

This example changes the user mouse icon to look like a dragon image.

```lua
local UserInputService = game:GetService("UserInputService")

-- In order to restore the cursor to what it was set to previously, it will need to be saved to a variable
local savedCursor = nil
local function setTemporaryCursor(cursor: string)
	-- Only update the saved cursor if it's not currently saved
	if not savedCursor then
		savedCursor = UserInputService.MouseIcon
	end
	UserInputService.MouseIcon = cursor
end

local function clearTemporaryCursor()
	-- Only restore the mouse cursor if there's a saved cursor to restore
	if savedCursor then
		UserInputService.MouseIcon = savedCursor
		-- Don't restore the same cursor twice (might overwrite another script)
		savedCursor = nil
	end
end

setTemporaryCursor("http://www.roblox.com/asset?id=163023520")
print(UserInputService.MouseIcon)

clearTemporaryCursor()
```

### Property: UserInputService.MouseIconContent

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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property determines the content ID of the image for the user's mouse
icon. If blank, a default arrow pointer is used. While the cursor hovers
over certain UI objects such as an [ImageButton](/docs/reference/engine/classes/ImageButton.md),
[TextButton](/docs/reference/engine/classes/TextButton.md), [TextBox](/docs/reference/engine/classes/TextBox.md), or [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md), this
image will be overridden and temporarily ignored. Only asset URIs are
supported for this property.

To hide the cursor entirely, do **not** use a transparent image; instead,
set [MouseIconEnabled](/docs/reference/engine/classes/UserInputService.md) to `false`.

**Custom Mouse Icon**

This example changes the user mouse icon to look like a dragon image.

```lua
local UserInputService = game:GetService("UserInputService")

-- In order to restore the cursor to what it was set to previously, it will need to be saved to a variable
local savedCursor = nil
local function setTemporaryCursor(cursor: string)
	-- Only update the saved cursor if it's not currently saved
	if not savedCursor then
		savedCursor = UserInputService.MouseIcon
	end
	UserInputService.MouseIcon = cursor
end

local function clearTemporaryCursor()
	-- Only restore the mouse cursor if there's a saved cursor to restore
	if savedCursor then
		UserInputService.MouseIcon = savedCursor
		-- Don't restore the same cursor twice (might overwrite another script)
		savedCursor = nil
	end
end

setTemporaryCursor("http://www.roblox.com/asset?id=163023520")
print(UserInputService.MouseIcon)

clearTemporaryCursor()
```

### Property: UserInputService.MouseIconEnabled

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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property determines whether the mouse icon is visible. To detect when
this property changes, you must listen to when the
[MouseEnabled](/docs/reference/engine/classes/UserInputService.md) property changes.

### Property: UserInputService.OnScreenKeyboardPosition

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes the position of the on-screen keyboard in pixels.
The keyboard's position is [Vector2.new(0, 0)](/docs/reference/engine/datatypes/Vector2.md) when it is
not visible.

See also
[OnScreenKeyboardVisible](/docs/reference/engine/classes/UserInputService.md)
and [OnScreenKeyboardSize](/docs/reference/engine/classes/UserInputService.md).

### Property: UserInputService.OnScreenKeyboardSize

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes the size of the on-screen keyboard in pixels. The
keyboard's size is [Vector2.new(0, 0)](/docs/reference/engine/datatypes/Vector2.md) when it is not
visible.

See also
[OnScreenKeyboardVisible](/docs/reference/engine/classes/UserInputService.md)
and
[OnScreenKeyboardPosition](/docs/reference/engine/classes/UserInputService.md).

### Property: UserInputService.OnScreenKeyboardVisible

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether an on-screen keyboard is currently visible
on the user's screen.

See also
[OnScreenKeyboardSize](/docs/reference/engine/classes/UserInputService.md) and
[OnScreenKeyboardPosition](/docs/reference/engine/classes/UserInputService.md).

### Property: UserInputService.PreferredInput

```json
{
  "type": "PreferredInput",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This read-only property lets you query the **primary** input type a player
is likely using, based on anticipated user behavior, to ensure UI elements
like on‑screen buttons and menus work elegantly across devices. For
example, a touch‑enabled device assumes touch is the default input and
that touch buttons may appear for actions, but if a player connects an
additional bluetooth keyboard/mouse or gamepad, you can assume they want
to switch to that as the primary input type and possibly use touch as a
backup input for on‑screen UI.

The value of `PreferredInput` changes based on built‑in device inputs and
the player's most recent interaction with a connected gamepad or
keyboard/mouse. Examples include:

| Real-World Scenario | `PreferredInput` |
| --- | --- |
| Player is using a phone with no other connected input devices; no possibility of an input type change. | [Touch](/docs/reference/engine/enums/PreferredInput\.md) |
| Player is using a mobile device with a bluetooth keyboard & mouse connected, but no gamepad is connected. | [KeyboardAndMouse](/docs/reference/engine/enums/PreferredInput\.md) |
| Player is using a tablet with a bluetooth gamepad connected, but no keyboard or mouse is connected. | [Gamepad](/docs/reference/engine/enums/PreferredInput\.md) |
| Player is using an Xbox or PlayStation with a bluetooth keyboard & mouse connected and has most recently interacted with the keyboard or mouse. | [KeyboardAndMouse](/docs/reference/engine/enums/PreferredInput\.md) |
| Player is on a Windows or Mac PC with a gamepad connected and has most recently interacted with the gamepad. | [Gamepad](/docs/reference/engine/enums/PreferredInput\.md) |

**Preferred Input Detection**

The following [LocalScript](/docs/reference/engine/classes/LocalScript.md) is a template for initially detecting the
preferred input and responding to changes during gameplay.

```lua
local UserInputService = game:GetService("UserInputService")

local function preferredInputChanged()
	local preferredInput = UserInputService.PreferredInput

	if preferredInput == Enum.PreferredInput.Touch then
		-- Player is on touch-enabled device with no other input types available/connected
		print("Touch")
	elseif preferredInput == Enum.PreferredInput.Gamepad then
		-- Player has connected or most recently interacted with a gamepad
		print("Gamepad")
	elseif preferredInput == Enum.PreferredInput.KeyboardAndMouse then
		-- Player has connected or most recently interacted with a keyboard or mouse
		print("KeyboardAndMouse")
	end
end

preferredInputChanged()

UserInputService:GetPropertyChangedSignal("PreferredInput"):Connect(function()
	preferredInputChanged()
end)
```

### Property: UserInputService.TouchEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user's device has a touch screen
available. If `true`, you can use touch‑related events such as
[TouchStarted](/docs/reference/engine/classes/UserInputService.md) and
[TouchMoved](/docs/reference/engine/classes/UserInputService.md).

For seamless cross-platform compatibility on mixed-input devices, see
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input.

### Property: UserInputService.TouchScreenEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

Read-only. Whether the user's device has a touch screen. Defaults to
`false`; the engine sets it to `true` on devices with a physical touch
screen.

Unlike [TouchEnabled](/docs/reference/engine/classes/UserInputService.md), which reports
`false` on some touch-capable desktop hardware (such as a Windows laptop
with a touch screen) to avoid switching those devices to mobile-style
controls, `TouchScreenEnabled` reflects the device's true touch
capability.

### Property: UserInputService.VREnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes whether the user is using a virtual reality (VR)
device. If `true`, you can use VR‑related properties, methods, and events
in [VRService](/docs/reference/engine/classes/VRService.md).

### Property: UserInputService.ModalEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

> **Deprecated:** This item has been superseded by [GuiService.TouchControlsEnabled](/docs/reference/engine/classes/GuiService.md) which should be used in all new work.

The `ModalEnabled` property determines whether character controls are
hidden on [TouchEnabled](/docs/reference/engine/classes/UserInputService.md) devices. By
default, this property is `false` and controls are visible.

This property will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) running
for the player whose character controls are to be hidden.

Even if mobile controls are hidden for a player on a touch‑enabled device,
other events such as [InputBegan](/docs/reference/engine/classes/UserInputService.md) and
[TouchSwipe](/docs/reference/engine/classes/UserInputService.md) can still be used to
process other forms of input.

### Property: UserInputService.UserHeadCFrame

```json
{
  "type": "CFrame",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

> **Deprecated:** This item has been superseded by [UserInputService:GetUserCFrame()](/docs/reference/engine/classes/UserInputService.md) which should be used in all new work.

The UserHeadCFrame used to describe the orientation and position of a
user's head, if they are actively using a virtual reality headset.

## Methods

### Method: UserInputService:CreateVirtualInput

**Signature:** `UserInputService:CreateVirtualInput(): Object`

This method creates a [VirtualInput](/docs/reference/engine/classes/VirtualInput.md) object for simulating mouse,
keyboard, and pointer input as if it were performed by a real user. It is
intended for testing and automation workflows that need to simulate user
interaction inside a running experience. Simulated input is restricted to
the experience's own UI elements and cannot interact with arbitrary or
system-level GUI.

Always check that the returned value is not `nil` before calling any
methods on it.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Object` — A new [VirtualInput](/docs/reference/engine/classes/VirtualInput.md) object, or `nil` if the feature is not
available.

### Method: UserInputService:GamepadSupports

**Signature:** `UserInputService:GamepadSupports(gamepadNum: UserInputType, gamepadKeyCode: KeyCode): boolean`

This method returns whether the given [UserInputType](/docs/reference/engine/enums/UserInputType.md) gamepad
supports a button corresponding with the given [KeyCode](/docs/reference/engine/enums/KeyCode.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadNum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the gamepad. |
| `gamepadKeyCode` | `KeyCode` |  | The [KeyCode](/docs/reference/engine/enums/KeyCode.md) of the button in question. |

**Returns:** `boolean` — Whether the given gamepad supports a button corresponding with the
given [KeyCode](/docs/reference/engine/enums/KeyCode.md).

### Method: UserInputService:GetConnectedGamepads

**Signature:** `UserInputService:GetConnectedGamepads(): Array`

This method returns an array of [UserInputType](/docs/reference/engine/enums/UserInputType.md) gamepads currently
connected. If no gamepads are connected, the array will be empty.

Alternatively to detecting all gamepads, the
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) property can be
used to more accurately reflect which input (mouse/keyboard, touch,
gamepad, etc.) the player is likely using as the **primary** input.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Array` — An array of [UserInputTypes](/docs/reference/engine/enums/UserInputType.md) corresponding with the
gamepads connected to the user's device.

### Method: UserInputService:GetDeviceAcceleration

**Signature:** `UserInputService:GetDeviceAcceleration(): InputObject`

This method returns an [InputObject](/docs/reference/engine/classes/InputObject.md) that describes the device's
current acceleration. For this to function, the user's device must have an
enabled accelerometer as queried through the
[AccelerometerEnabled](/docs/reference/engine/classes/UserInputService.md)
property.

To track when the device's acceleration changes, use the
[DeviceAccelerationChanged](/docs/reference/engine/classes/UserInputService.md)
event.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `InputObject` — An [InputObject](/docs/reference/engine/classes/InputObject.md) describing the device's current acceleration,
with [Position](/docs/reference/engine/classes/InputObject.md) representing the
acceleration force on each local device axis.

**Output Device Acceleration**

This example checks if a user's device has an enabled accelerometer and, if
`true`, it outputs the current acceleration.

```lua
local UserInputService = game:GetService("UserInputService")

if UserInputService.AccelerometerEnabled then
	local acceleration = UserInputService:GetDeviceAcceleration().Position
	print(acceleration)
else
	warn("Cannot get device acceleration because device does not have an enabled accelerometer!")
end
```

**Expected output:** Output may vary depending on whether the user's device has an enabled accelerometer during testing.

### Method: UserInputService:GetDeviceGravity

**Signature:** `UserInputService:GetDeviceGravity(): InputObject`

This method returns an [InputObject](/docs/reference/engine/classes/InputObject.md) describing the device's current
gravity vector. The vector is determined by the device's orientation
relative to the real-world force of gravity. For example:

- [Vector3.new(0, 0, -9.81)](/docs/reference/engine/datatypes/Vector3.md) if the device is perfectly
  upright (portrait)
- [Vector3.new(9.81, 0, 0)](/docs/reference/engine/datatypes/Vector3.md) if the left side of the
  device is pointing down
- [Vector3.new(0, -9.81, 0)](/docs/reference/engine/datatypes/Vector3.md) if the back of the device is
  pointing down

Gravity is only tracked for devices with an enabled gyroscope as queried
through [GyroscopeEnabled](/docs/reference/engine/classes/UserInputService.md).

To track when the device's gravity changes, use the
[DeviceGravityChanged](/docs/reference/engine/classes/UserInputService.md) event.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `InputObject` — An [InputObject](/docs/reference/engine/classes/InputObject.md) describing the device's current gravity vector,
with [Position](/docs/reference/engine/classes/InputObject.md) representing the force of
gravity on each local device axis.

**Moving Objects with the Gyroscope**

This example implements a level where the bubble will move along the **X** and
**Z** axes depending on the device's current gryoscope position.

```lua
local UserInputService = game:GetService("UserInputService")

local bubble = script.Parent:WaitForChild("Bubble")
local camera = workspace.CurrentCamera

camera.CameraType = Enum.CameraType.Scriptable
camera.CFrame = CFrame.new(0, 20, 0) * CFrame.Angles(-math.pi / 2, 0, 0)

if UserInputService.GyroscopeEnabled then
	-- Bind event to when gyroscope detects change
	UserInputService.DeviceGravityChanged:Connect(function(accel)
		-- Move the bubble in the world based on the gyroscope data
		bubble.Position = Vector3.new(-8 * accel.Position.X, 1.8, -8 * accel.Position.Z)
	end)
end
```

### Method: UserInputService:GetDeviceRotation

**Signature:** `UserInputService:GetDeviceRotation(): Tuple`

This method returns an [InputObject](/docs/reference/engine/classes/InputObject.md) and a [CFrame](/docs/reference/engine/datatypes/CFrame.md)
describing the device's current rotation vector.

Device rotation is only tracked for devices with an enabled gyroscope as
queried through
[GyroscopeEnabled](/docs/reference/engine/classes/UserInputService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Tuple` — A tuple containing two properties: The delta describing the amount of
rotation that last happened, and the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the device's
current rotation relative to its default reference frame.

**Output Device Rotation**

This example checks if a user's device has an enabled gyroscope and, if
`true`, it outputs the device's current [CFrame](/docs/reference/engine/datatypes/CFrame.md).

```lua
local UserInputService = game:GetService("UserInputService")

if UserInputService.GyroscopeEnabled then
	local _, cf = UserInputService:GetDeviceRotation()
	print(cf)
else
	warn("Cannot get device rotation because device does not have an enabled gyroscope!")
end
```

### Method: UserInputService:GetFocusedTextBox

**Signature:** `UserInputService:GetFocusedTextBox(): TextBox`

This method returns the [TextBox](/docs/reference/engine/classes/TextBox.md) the client is currently focused
on. A [TextBox](/docs/reference/engine/classes/TextBox.md) can be manually selected by the user, or selection
can be forced using the [TextBox:CaptureFocus()](/docs/reference/engine/classes/TextBox.md) method. If no
[TextBox](/docs/reference/engine/classes/TextBox.md) is selected, this method will return `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `TextBox` — The currently focused [TextBox](/docs/reference/engine/classes/TextBox.md), or `nil` if no [TextBox](/docs/reference/engine/classes/TextBox.md)
is focused.

### Method: UserInputService:GetGamepadConnected

**Signature:** `UserInputService:GetGamepadConnected(gamepadNum: UserInputType): boolean`

This method returns whether a gamepad with the given [UserInputType](/docs/reference/engine/enums/UserInputType.md)
is connected.

Alternatively to detecting a specific gamepad by [UserInputType](/docs/reference/engine/enums/UserInputType.md), the
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) property can be
used to more accurately reflect which input (mouse/keyboard, touch,
gamepad, etc.) the player is likely using as the **primary** input.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadNum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the gamepad in question. |

**Returns:** `boolean` — Whether a gamepad associated with [UserInputType](/docs/reference/engine/enums/UserInputType.md) is connected.

### Method: UserInputService:GetGamepadState

**Signature:** `UserInputService:GetGamepadState(gamepadNum: UserInputType): List<InputObject>`

This method returns an array of [InputObjects](/docs/reference/engine/classes/InputObject.md) for all
available inputs on the given [UserInputType](/docs/reference/engine/enums/UserInputType.md) gamepad, representing
each input's last input state.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadNum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) corresponding with the gamepad in question. |

**Returns:** `List<InputObject>` — An array of [InputObjects](/docs/reference/engine/classes/InputObject.md) representing the current
state of all available inputs for the given gamepad.

### Method: UserInputService:GetImageForKeyCode

**Signature:** `UserInputService:GetImageForKeyCode(keyCode: KeyCode): ContentId`

This method takes the requested [KeyCode](/docs/reference/engine/enums/KeyCode.md) and returns the associated
image for the currently connected gamepad device (limited to Xbox,
PlayStation, and Windows). This means that if the connected controller is
an Xbox&nbsp;One controller, the user sees Xbox assets. Similarly, if the
connected device is a PlayStation controller, the user sees PlayStation
assets. If you want to use custom assets, see
[GetStringForKeyCode()](/docs/reference/engine/classes/UserInputService.md).

For most use cases, consider using [InputActionLabel](/docs/reference/engine/classes/InputActionLabel.md) instead. It is
a [GuiObject](/docs/reference/engine/classes/GuiObject.md) that automatically displays the correct key icon for
an [InputAction](/docs/reference/engine/classes/InputAction.md) and updates when the player switches input devices
or rebinds the action, without any scripting. `GetImageForKeyCode()`
remains useful for advanced or fully custom interfaces where you need
direct access to the underlying image asset.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyCode` | `KeyCode` |  | The [KeyCode](/docs/reference/engine/enums/KeyCode.md) for which to fetch the associated image. |

**Returns:** `ContentId` — The returned image asset ID.

**UserInputService - Get Image For KeyCode**

This API returns the requested image for the given [KeyCode](/docs/reference/engine/enums/KeyCode.md).

```lua
local UserInputService = game:GetService("UserInputService")

local imageLabel = script.Parent
local key = Enum.KeyCode.ButtonA

local mappedIconImage = UserInputService:GetImageForKeyCode(key)
imageLabel.Image = mappedIconImage
```

### Method: UserInputService:GetKeysPressed

**Signature:** `UserInputService:GetKeysPressed(): List<InputObject>`

This method returns an array of [InputObjects](/docs/reference/engine/classes/InputObject.md)
associated with the keys currently being pressed down. The array can be
iterated through to determine which keys are currently being pressed,
using the [InputObject.KeyCode](/docs/reference/engine/classes/InputObject.md) names or values.

To check if a specific key is being pressed, use
[IsKeyDown()](/docs/reference/engine/classes/UserInputService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `List<InputObject>` — An array of [InputObjects](/docs/reference/engine/classes/InputObject.md) associated with the keys
currently being pressed.

### Method: UserInputService:GetLastInputType

**Signature:** `UserInputService:GetLastInputType(): UserInputType`

This method returns the [UserInputType](/docs/reference/engine/enums/UserInputType.md) associated with the user's
most recent input. For example, if the user's previous input had been
pressing the <kbd>A</kbd> key, the returned [UserInputType](/docs/reference/engine/enums/UserInputType.md) value
would be [Keyboard](/docs/reference/engine/enums/UserInputType.md).

For seamless cross-platform compatibility on mixed-input devices, see
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input. `GetLastInputType()`
remains for advanced workflows or control schemes that rely on detecting
and responding to the player's specific most recent [UserInputType](/docs/reference/engine/enums/UserInputType.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `UserInputType` — The [UserInputType](/docs/reference/engine/enums/UserInputType.md) associated with the user's most recent input.

**Detect Last Input Type**

This example gets the last [UserInputType](/docs/reference/engine/enums/UserInputType.md) and outputs if it was keyboard
input.

```lua
local UserInputService = game:GetService("UserInputService")

if UserInputService:GetLastInputType() == Enum.UserInputType.Keyboard then
	print("Most recent input was keyboard!")
end
```

### Method: UserInputService:GetMouseButtonsPressed

**Signature:** `UserInputService:GetMouseButtonsPressed(): List<InputObject>`

This method returns an array of [InputObjects](/docs/reference/engine/classes/InputObject.md)
associated with the mouse buttons currently being held down. The array can
be iterated through to determine which buttons are currently being held,
using the [InputObject.KeyCode](/docs/reference/engine/classes/InputObject.md) names or values.

Mouse buttons that are tracked by this method include `MouseButton1`
(left), `MouseButton2` (right), and `MouseButton3` (middle).

If the user is not pressing any mouse button down when the method is
called, it will return an empty array.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `List<InputObject>` — An array of [InputObjects](/docs/reference/engine/classes/InputObject.md) corresponding to the
mouse buttons currently being currently held down.

**Check Pressed Mouse Buttons**

This example checks if the user pressed `MouseButton1` (left), `MouseButton2`
(right), or both mouse buttons. This can be extended to behave differently
depending on which mouse buttons are pressed, including `MouseButton3`
(middle).

```lua
local UserInputService = game:GetService("UserInputService")

UserInputService.InputBegan:Connect(function(input, gameProcessedEvent)
	-- Return an array of the pressed mouse buttons
	local buttonsPressed = UserInputService:GetMouseButtonsPressed()

	local m1, m2 = false, false
	for _, button in buttonsPressed do
		if button.UserInputType == Enum.UserInputType.MouseButton1 then
			print("MouseButton1 pressed!")
			m1 = true
		end

		if button.UserInputType == Enum.UserInputType.MouseButton2 then
			print("MouseButton2 pressed!")
			m2 = true
		end

		if m1 and m2 then
			print("Both mouse buttons pressed!")
		end
	end
end)
```

### Method: UserInputService:GetMouseDelta

**Signature:** `UserInputService:GetMouseDelta(): Vector2`

This method returns the change, in pixels, of the position of the player's
[Mouse](/docs/reference/engine/classes/Mouse.md) in the last rendered frame, only if the mouse has been
locked using the [MouseBehavior](/docs/reference/engine/classes/UserInputService.md)
property; otherwise the returned [Vector2](/docs/reference/engine/datatypes/Vector2.md) values will be `0`.

The sensitivity of the mouse, determined in the client's settings and
[MouseDeltaSensitivity](/docs/reference/engine/classes/UserInputService.md), will
influence the result.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Vector2` — Change in movement of the mouse.

**Getting Mouse Delta**

The following example measures any mouse movement in pixels from the last
render step to the current render step. If the user has set their camera
sensitivity to be higher or lower than `1` in the experience's menu, it will
affect the returned value.

```lua
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

UserInputService.MouseBehavior = Enum.MouseBehavior.LockCenter

local function onRenderStep()
	local delta = UserInputService:GetMouseDelta()
	if delta ~= Vector2.new(0, 0) then
		print("The mouse has moved", delta, "since the last step")
	end
end

RunService:BindToRenderStep("MeasureMouseMovement", Enum.RenderPriority.Input.Value, onRenderStep)
```

### Method: UserInputService:GetMouseLocation

**Signature:** `UserInputService:GetMouseLocation(): Vector2`

This method returns a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the current screen
location of the player's [Mouse](/docs/reference/engine/classes/Mouse.md) in pixels relative to the top‑left
corner. This does not account for the [ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md); to get the
top‑left and bottom‑right insets, call [GuiService:GetGuiInset()](/docs/reference/engine/classes/GuiService.md).

If the location of the mouse pointer is offscreen or the player's device
does not have a mouse, the returned value will be undetermined.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Vector2` — A [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the current screen location of the
mouse, in pixels.

### Method: UserInputService:GetNavigationGamepads

**Signature:** `UserInputService:GetNavigationGamepads(): Array`

This method returns an array of gamepads that are connected and enabled
for [GuiObject](/docs/reference/engine/classes/GuiObject.md) navigation, but does not influence navigation
controls. This list is in descending order of priority, meaning it can be
iterated over to determine which gamepad should have navigation control.

See also
[SetNavigationGamepad()](/docs/reference/engine/classes/UserInputService.md),
[IsNavigationGamepad()](/docs/reference/engine/classes/UserInputService.md), and
[GetConnectedGamepads()](/docs/reference/engine/classes/UserInputService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `Array` — An array of [UserInputTypes](/docs/reference/engine/enums/UserInputType.md) that can be used for
navigation, in descending order of priority.

### Method: UserInputService:GetStringForKeyCode

**Signature:** `UserInputService:GetStringForKeyCode(keyCode: KeyCode, format?: KeyCodeStringFormat): string`

This method returns a string representing a key the user should press in
order to input a given [KeyCode](/docs/reference/engine/enums/KeyCode.md), keeping in mind their keyboard
layout. For key codes that require some modifier to be held, this method
returns the key to be pressed in addition to the modifier. See the
examples below for further explanation.

For most use cases, consider using [InputActionLabel](/docs/reference/engine/classes/InputActionLabel.md) instead. It is
a [GuiObject](/docs/reference/engine/classes/GuiObject.md) that automatically displays the correct key text or
icon for an [InputAction](/docs/reference/engine/classes/InputAction.md) and updates when the player switches input
devices or rebinds the action, without any scripting.
`GetStringForKeyCode()` remains useful for advanced or fully custom
interfaces where you need the raw display string.

When using Roblox with a non‑QWERTY keyboard layout, key codes are mapped
to equivalent QWERTY positions. For example, pressing <kbd>A</kbd> on an
AZERTY keyboard results in [KeyCode.Q](/docs/reference/engine/enums/KeyCode.md), potentially leading to
mismatched information on experience UI elements. This method solves the
issue by providing the actual key to be pressed while using non‑QWERTY
keyboard layouts.

| KeyCode | QWERTY Return | AZERTY Return |
| --- | --- | --- |
| [KeyCode.Q](/docs/reference/engine/enums/KeyCode.md) | `Q` | `A` |
| [KeyCode.W](/docs/reference/engine/enums/KeyCode.md) | `W` | `Z` |
| [KeyCode.Equals](/docs/reference/engine/enums/KeyCode.md) | `=` | `=` |
| [KeyCode.At](/docs/reference/engine/enums/KeyCode.md) | `2` because `@` is typed with `Shift``2` | `É` |

#### Abbreviated Format

When `format` is set to [KeyCodeStringFormat.Abbreviated](/docs/reference/engine/enums/KeyCodeStringFormat.md), the method
returns shortened key names suitable for compact UI elements, for example
`"LCtrl"` instead of `"LeftControl"`, `"Bksp"` instead of `"Backspace"`,
or `"Esc"` instead of `"Escape"`. If no abbreviation exists for the given
key code, the default string is returned.

#### Gamepad Usage

`GetStringForKeyCode()` returns the string mapping for the [KeyCode](/docs/reference/engine/enums/KeyCode.md)
for the most recently connected gamepad. If the connected controller is
not supported, the method returns the default string conversion for the
requested key code.

The following example shows how you can map custom assets for
[ButtonA](/docs/reference/engine/enums/KeyCode.md):

```
local UserInputService = game:GetService("UserInputService")

local imageLabel = script.Parent
local key = Enum.KeyCode.ButtonA

local mappings = {
	ButtonA = "rbxasset://BUTTON_A_ASSET", -- Replace with the desired ButtonA asset
	ButtonCross = "rbxasset://BUTTON_CROSS_ASSET"  -- Replace with the desired ButtonCross asset
}

local mappedKey = UserInputService:GetStringForKeyCode(key)
local image = mappings[mappedKey]

imageLabel.Image = image
```

#### Gamepad Mappings

The directional pad key codes do not have any differences based on device.
[KeyCode.ButtonSelect](/docs/reference/engine/enums/KeyCode.md) has slightly different behavior in some cases.
Use both PlayStation mappings to ensure users see the correct buttons.

| KeyCode | PlayStation Return Value | Xbox Return Value |
| --- | --- | --- |
| [KeyCode.ButtonA](/docs/reference/engine/enums/KeyCode.md) | `ButtonCross` | `ButtonA` |
| [KeyCode.ButtonB](/docs/reference/engine/enums/KeyCode.md) | `ButtonCircle` | `ButtonB` |
| [KeyCode.ButtonX](/docs/reference/engine/enums/KeyCode.md) | `ButtonSquare` | `ButtonX` |
| [KeyCode.ButtonY](/docs/reference/engine/enums/KeyCode.md) | `ButtonTriangle` | `ButtonY` |
| [KeyCode.ButtonL1](/docs/reference/engine/enums/KeyCode.md) | `ButtonL1` | `ButtonLB` |
| [KeyCode.ButtonL2](/docs/reference/engine/enums/KeyCode.md) | `ButtonL2` | `ButtonLT` |
| [KeyCode.ButtonL3](/docs/reference/engine/enums/KeyCode.md) | `ButtonL3` | `ButtonLS` |
| [KeyCode.ButtonR1](/docs/reference/engine/enums/KeyCode.md) | `ButtonR1` | `ButtonRB` |
| [KeyCode.ButtonR2](/docs/reference/engine/enums/KeyCode.md) | `ButtonR2` | `ButtonRT` |
| [KeyCode.ButtonR3](/docs/reference/engine/enums/KeyCode.md) | `ButtonR3` | `ButtonRS` |
| [KeyCode.ButtonStart](/docs/reference/engine/enums/KeyCode.md) | `ButtonOptions` | `ButtonStart` |
| [KeyCode.ButtonSelect](/docs/reference/engine/enums/KeyCode.md) | `ButtonTouchpad` and `ButtonShare` | `ButtonSelect` |

#### Legacy System Images

When using a [KeyCode](/docs/reference/engine/enums/KeyCode.md) that may be better represented as an image,
such as for an [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) in a user interface, you can use the
following legacy icons. However, it's recommended that you use
[GetImageForKeyCode()](/docs/reference/engine/classes/UserInputService.md) as a
more modern, cross‑platform method to retrieve Xbox and PlayStation
controller icons.

| KeyCode | Asset ID |
| --- | --- |
| [KeyCode.ButtonX](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxX.png` |
| [KeyCode.ButtonY](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxY.png` |
| [KeyCode.ButtonA](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxA.png` |
| [KeyCode.ButtonB](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxB.png` |
| [KeyCode.DPadLeft](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/dpadLeft.png` |
| [KeyCode.DPadRight](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/dpadRight.png` |
| [KeyCode.DPadUp](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/dpadUp.png` |
| [KeyCode.DPadDown](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/dpadDown.png` |
| [KeyCode.ButtonSelect](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxView.png` |
| [KeyCode.ButtonStart](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxmenu.png` |
| [KeyCode.ButtonL1](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxLB.png` |
| [KeyCode.ButtonR1](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxRB.png` |
| [KeyCode.ButtonL2](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxLT.png` |
| [KeyCode.ButtonR2](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxRT.png` |
| [KeyCode.ButtonL3](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxLS.png` |
| [KeyCode.ButtonR3](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxRS.png` |
| [KeyCode.Thumbstick1](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxLSDirectional.png` |
| [KeyCode.Thumbstick2](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/xboxRSDirectional.png` |
| [KeyCode.Backspace](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/backspace.png` |
| [KeyCode.Return](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/return.png` |
| [KeyCode.LeftShift](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/shift.png` |
| [KeyCode.RightShift](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/shift.png` |
| [KeyCode.Tab](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/tab.png` |
| [KeyCode.Quote](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/apostrophe.png` |
| [KeyCode.Comma](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/comma.png` |
| [KeyCode.Backquote](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/graveaccent.png` |
| [KeyCode.Period](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/period.png` |
| [KeyCode.Space](/docs/reference/engine/enums/KeyCode.md) | `rbxasset://textures/ui/Controls/spacebar.png` |

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyCode` | `KeyCode` |  | The [KeyCode](/docs/reference/engine/enums/KeyCode.md) to get the display string for. |
| `format` | `KeyCodeStringFormat` | `Default` | An [KeyCodeStringFormat](/docs/reference/engine/enums/KeyCodeStringFormat.md) value that controls the format of the returned string. Defaults to [KeyCodeStringFormat.Default](/docs/reference/engine/enums/KeyCodeStringFormat.md). Pass [KeyCodeStringFormat.Abbreviated](/docs/reference/engine/enums/KeyCodeStringFormat.md) to get shortened labels suitable for compact UI such as `"Bksp"`, `"LCtrl"`, or `"Esc"`. |

**Returns:** `string` — A string representing the key the user should press for the given key
code, formatted according to the specified [KeyCodeStringFormat](/docs/reference/engine/enums/KeyCodeStringFormat.md).

### Method: UserInputService:GetSupportedGamepadKeyCodes

**Signature:** `UserInputService:GetSupportedGamepadKeyCodes(gamepadNum: UserInputType): Array`

This method returns an array of [KeyCodes](/docs/reference/engine/enums/KeyCode.md) that the gamepad
associated with the given [UserInputType](/docs/reference/engine/enums/UserInputType.md) supports. If called on a
non‑connected gamepad, returns an empty array.

To determine if a specific [KeyCode](/docs/reference/engine/enums/KeyCode.md) is supported, use
[GamepadSupports()](/docs/reference/engine/classes/UserInputService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadNum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the gamepad. |

**Returns:** `Array` — An array of [KeyCodes](/docs/reference/engine/enums/KeyCode.md) supported by the given gamepad.

### Method: UserInputService:IsGamepadButtonDown

**Signature:** `UserInputService:IsGamepadButtonDown(gamepadNum: UserInputType, gamepadKeyCode: KeyCode): boolean`

This method returns `true` if a particular button is pressed on a gamepad,
otherwise returns `false`.

See also [InputBinding](/docs/reference/engine/classes/InputBinding.md) as a way to hook gamepad and other input
interactions to [InputActions](/docs/reference/engine/classes/InputAction.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadNum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the given gamepad. |
| `gamepadKeyCode` | `KeyCode` |  | The [KeyCode](/docs/reference/engine/enums/KeyCode.md) of the specified gamepad button. |

**Returns:** `boolean` — Whether the specified button on the given gamepad is pressed is
pressed.

### Method: UserInputService:IsKeyDown

**Signature:** `UserInputService:IsKeyDown(keyCode: KeyCode): boolean`

This method returns `true` if a particular key is pressed on a keyboard,
otherwise returns `false`.

See also [InputBinding](/docs/reference/engine/classes/InputBinding.md) as a way to hook key and other input
interactions to [InputActions](/docs/reference/engine/classes/InputAction.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyCode` | `KeyCode` |  | The [KeyCode](/docs/reference/engine/enums/KeyCode.md) of the key. |

**Returns:** `boolean` — Whether the specified key is being held down.

### Method: UserInputService:IsMouseButtonPressed

**Signature:** `UserInputService:IsMouseButtonPressed(mouseButton: UserInputType): boolean`

This method returns `true` if a particular mouse button is pressed,
otherwise returns `false`.

See also [InputBinding](/docs/reference/engine/classes/InputBinding.md) as a way to hook mouse button and other
input interactions to [InputActions](/docs/reference/engine/classes/InputAction.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `mouseButton` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the mouse button. |

**Returns:** `boolean` — Whether the given mouse button is currently held down.

### Method: UserInputService:IsNavigationGamepad

**Signature:** `UserInputService:IsNavigationGamepad(gamepadEnum: UserInputType): boolean`

This method returns `true` if the specified gamepad is allowed to control
navigation and selection [GuiObjects](/docs/reference/engine/classes/GuiObject.md).

Use [SetNavigationGamepad()](/docs/reference/engine/classes/UserInputService.md)
to set a navigation gamepad, or
[GetNavigationGamepads()](/docs/reference/engine/classes/UserInputService.md)
to get a list of all navigation gamepads.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadEnum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the specified gamepad. |

**Returns:** `boolean` — Whether the specified gamepad is a navigation gamepad.

### Method: UserInputService:RecenterUserHeadCFrame

**Signature:** `UserInputService:RecenterUserHeadCFrame(): ()`

This method recenters the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the VR headset to the
current orientation of the headset worn by the user. This means that the
headset's current orientation is set to [CFrame.new()](/docs/reference/engine/datatypes/CFrame.md).

This method behaves identically to the [VRService](/docs/reference/engine/classes/VRService.md) method
[RecenterUserHeadCFrame()](/docs/reference/engine/classes/VRService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

### Method: UserInputService:SetNavigationGamepad

**Signature:** `UserInputService:SetNavigationGamepad(gamepadEnum: UserInputType, enabled: boolean): ()`

This method sets whether the specified gamepad can move the
[GuiObject](/docs/reference/engine/classes/GuiObject.md) navigator.

Use [IsNavigationGamepad()](/docs/reference/engine/classes/UserInputService.md)
to check if a specified gamepad is a set to be a navigation gamepad, or
[GetNavigationGamepads()](/docs/reference/engine/classes/UserInputService.md)
to retrieve a list of all navigation gamepads.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `gamepadEnum` | `UserInputType` |  | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the specified gamepad. |
| `enabled` | `boolean` |  | Whether the specified gamepad can move the GUI navigator. |

**Returns:** `()`

### Method: UserInputService:GetUserCFrame

**Signature:** `UserInputService:GetUserCFrame(type: UserCFrame): CFrame`

> **Deprecated:** Use [VRService:GetUserCFrame()](/docs/reference/engine/classes/VRService.md) instead.

The [UserInputService:GetUserCFrame()](/docs/reference/engine/classes/UserInputService.md) method returns a
[CFrame](/docs/reference/engine/datatypes/CFrame.md) describing the position and orientation of a specified
[UserCFrame](/docs/reference/engine/enums/UserCFrame.md) virtual reality (VR) device. If the specified device is
not connected, the method returns [CFrame.new()](/docs/reference/engine/datatypes/CFrame.md).

For example, the code snippet below prints the CFrame of the user's VR
headset.

```lua
local UserInputService = game:GetService("UserInputService")
local cframe = UserInputService:GetUserCFrame(Enum.UserCFrame.Head)

print(cframe)
```

By using the method, players can implement features such as re-positioning
the user's in-game character corresponding to the location of a connected
VR device. This can be done by changing the _CFrame_ of the user's in-game
body parts to match the _CFrame_ of the specified VR device using
[UserCFrame](/docs/reference/engine/enums/UserCFrame.md) and [CFrame](/docs/reference/engine/datatypes/CFrame.md) value arguments passed by the
event.

See also:

- [UserInputService.UserCFrameChanged](/docs/reference/engine/classes/UserInputService.md), an event which fires when
  the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of a VR device changes
- [VRService](/docs/reference/engine/classes/VRService.md), a service used to implement VR support

As this event only fires locally, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `UserCFrame` |  | The [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) corresponding to the VR device. |

**Returns:** `CFrame` — A [CFrame](/docs/reference/engine/datatypes/CFrame.md) describing the position and orientation of the
specified VR device.

**VR Head Tracking**

This example demonstrates how to implement a head tracking script that mirrors
the movement of a virtual reality (VR) headset (the user's actual head) to
their in-game character's head.

The example first check if the user is using a VR device by checking the value
of the [VREnabled()](/docs/reference/engine/classes/VRService.md) property. This example only
works if the user is using a VR headset.

To determine the initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the character's head, the code
sample calls [GetUserCFrame()](/docs/reference/engine/classes/VRService.md) and passes
[UserCFrame.Head](/docs/reference/engine/enums/UserCFrame.md) as the argument.

To update the head's CFrame whenever the user's VR headset moves, the example
connects the [VRService.UserCFrameChanged](/docs/reference/engine/classes/VRService.md) event to the _TrackHead()_
function. When the event fires to indicate that a VR device moved, TrackHead()
checks if the headset moved. If the headset moved, the function updates the
CFrame of the character's head to the [CFrame](/docs/reference/engine/datatypes/CFrame.md) _value_ provided as an
argument.

As the UserCFrame enum also tracks VR left and right hand devices, the concept
of VR device tracking can be expanded to other character bodyparts.

In order for the example to work as expected, it must be placed in a
`LocalScript`.

```lua
local VRService = game:GetService("VRService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.CharacterAdded:Wait()
local head = character:WaitForChild("Head")

local function TrackHead(inputType, value)
	if inputType == Enum.UserCFrame.Head then
		head.CFrame = value
	end
end

if VRService.VREnabled then
	-- Set the initial CFrame
	head.CFrame = VRService:GetUserCFrame(Enum.UserCFrame.Head)

	-- Track VR headset movement and mirror for character's head
	VRService.UserCFrameChanged:Connect(TrackHead)
end
```

## Events

### Event: UserInputService.DeviceAccelerationChanged

**Signature:** `UserInputService.DeviceAccelerationChanged(acceleration: InputObject)`

This event fires when a user moves a device that has an accelerometer, a
component found in most mobile devices that measures acceleration (change
in speed). To determine whether a user's device has an accelerometer
enabled, use
[AccelerometerEnabled](/docs/reference/engine/classes/UserInputService.md).

This event can be used along with
[GetDeviceAcceleration()](/docs/reference/engine/classes/UserInputService.md)
to determine the current movement of a user's device.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md), with a [UserInputType](/docs/reference/engine/classes/InputObject.md) of [Accelerometer](/docs/reference/engine/enums/UserInputType.md) and [Position](/docs/reference/engine/classes/InputObject.md) that shows the force of gravity on each local device axis. |

**Control Players Using the Accelerometer**

This example uses the accelerometer to move the player character when a mobile
device is accelerated. The character will move along the axis that the device
was moved.

```lua
local UserInputService = game:GetService("UserInputService")
local Players = game:GetService("Players")

local SENSITIVITY = 0.2

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

local ready = true

local function changeAcceleration(acceleration)
	if ready then
		ready = false
		local accel = acceleration.Position

		if accel.Y >= SENSITIVITY then
			humanoid.Jump = true
		end

		if accel.Z <= -SENSITIVITY then
			humanoid:Move(Vector3.new(-1, 0, 0))
		end
		if accel.Z >= SENSITIVITY then
			humanoid:Move(Vector3.new(1, 0, 0))
		end
		if accel.X <= -SENSITIVITY then
			humanoid:Move(Vector3.new(0, 0, 1))
		end
		if accel.X >= SENSITIVITY then
			humanoid:Move(Vector3.new(0, 0, -1))
		end
		task.wait(1)
		ready = true
	end
end

if UserInputService.AccelerometerEnabled then
	UserInputService.DeviceAccelerationChanged:Connect(changeAcceleration)
end
```

### Event: UserInputService.DeviceGravityChanged

**Signature:** `UserInputService.DeviceGravityChanged(gravity: InputObject)`

This event fires when the device's gravity [Vector3](/docs/reference/engine/datatypes/Vector3.md) changes on a
device that has an accelerometer. To determine whether a user's device has
an accelerometer enabled, use
[AccelerometerEnabled](/docs/reference/engine/classes/UserInputService.md).

A device's gravity vector represent the force of gravity on each of the
device's **X**, **Y**, and **Z** axes. While gravity never changes, the
force it exerts on each axis changes when the device rotates and changes
orientation. The force value exerted on each axis is a unit vector ranging
from `-1` to `1`.

If the device has an enabled accelerometer, you can use the
[GetDeviceGravity()](/docs/reference/engine/classes/UserInputService.md) method to
get the current force of gravity on the user's device.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `gravity` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) with a [Position](/docs/reference/engine/classes/InputObject.md) property that shows the force of gravity on each local device axis. This position can be used as a direction to determine the direction of gravity relative to the device. |

**Move a Ball using the Accelerometer**

This code adds a force on a part so that it falls in the direction of actual
gravity relative to the user's device. In order for this example to work as
expected, it must be placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) and the user's device
must have an accelerometer.

```lua
local Workspace = game:GetService("Workspace")
local UserInputService = game:GetService("UserInputService")

local ball = script.Parent:WaitForChild("Ball")
local mass = ball:GetMass()
local gravityForce = ball:WaitForChild("GravityForce")

local function moveBall(gravity)
	gravityForce.Force = gravity.Position * Workspace.Gravity * mass
end

if UserInputService.AccelerometerEnabled then
	UserInputService.DeviceGravityChanged:Connect(moveBall)
end
```

### Event: UserInputService.DeviceRotationChanged

**Signature:** `UserInputService.DeviceRotationChanged(rotation: InputObject, cframe: CFrame)`

This event fires when a user rotates a device that has a gyroscope, a
component found in most mobile devices that detects orientation and
rotational speed. To check if a user's device has an enabled gyroscope,
use [GyroscopeEnabled](/docs/reference/engine/classes/UserInputService.md).

To query the current device rotation, use the
[GetDeviceRotation()](/docs/reference/engine/classes/UserInputService.md) method.

Note that this event only fires when the Roblox client window is in focus.
Inputs will not be captured when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `rotation` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) providing info about the device's rotation. [Position](/docs/reference/engine/classes/InputObject.md) represents the new rotation a [Vector3](/docs/reference/engine/datatypes/Vector3.md) positional value and [Delta](/docs/reference/engine/classes/InputObject.md) represents the change in rotation in a [Vector3](/docs/reference/engine/datatypes/Vector3.md) positional value. |
| `cframe` | `CFrame` | A [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing the device's current orientation. |

### Event: UserInputService.GamepadConnected

**Signature:** `UserInputService.GamepadConnected(gamepadNum: UserInputType)`

This event fires when a gamepad is connected to the client. You can also
use [GetConnectedGamepads()](/docs/reference/engine/classes/UserInputService.md)
to find the correct gamepad to use.

Alternatively, you can detect value changes to the
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) property which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input.

See also [GamepadDisconnected](/docs/reference/engine/classes/UserInputService.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `gamepadNum` | `UserInputType` | The [UserInputType](/docs/reference/engine/enums/UserInputType.md) of the connected gamepad. |

### Event: UserInputService.GamepadDisconnected

**Signature:** `UserInputService.GamepadDisconnected(gamepadNum: UserInputType)`

This event fires when a gamepad is disconnected from the client.

Alternatively, you can detect value changes to the
[PreferredInput](/docs/reference/engine/classes/UserInputService.md) property which more
accurately reflects which input (mouse/keyboard, touch, gamepad, etc.) the
player is likely using as the **primary** input.

See also [GamepadConnected](/docs/reference/engine/classes/UserInputService.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `gamepadNum` | `UserInputType` | The[UserInputType](/docs/reference/engine/enums/UserInputType.md) of the disconnected gamepad. |

### Event: UserInputService.InputBegan

**Signature:** `UserInputService.InputBegan(input: InputObject, gameProcessedEvent: boolean)`

This event fires when a user begins interacting with an input device such
as a mouse or gamepad, such as when they first interact with a gamepad
button, although it does not capture mouse wheel movements. Can be used
along with [InputChanged](/docs/reference/engine/classes/UserInputService.md) and
[InputEnded](/docs/reference/engine/classes/UserInputService.md) to track when user input
begins, changes, and ends.

See also [InputBinding](/docs/reference/engine/classes/InputBinding.md) as a way to hook input device interactions
to [InputActions](/docs/reference/engine/classes/InputAction.md).

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `input` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance containing information about the user's input. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.InputChanged

**Signature:** `UserInputService.InputChanged(input: InputObject, gameProcessedEvent: boolean)`

This event fires when a user changes how they're interacting with an input
device such as a mouse or gamepad. Can be used along with
[InputBegan](/docs/reference/engine/classes/UserInputService.md) and
[InputEnded](/docs/reference/engine/classes/UserInputService.md) to track when user input
begins, changes, and ends.

See also [InputBinding](/docs/reference/engine/classes/InputBinding.md) as a way to hook input device interactions
to [InputActions](/docs/reference/engine/classes/InputAction.md).

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `input` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance containing information about the user's input. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. To ignore events that are automatically handled by Roblox like scrolling in a [ScrollingFrame](/docs/reference/engine/classes/ScrollingFrame.md), check that `gameProcessedEvent` is `false`. |

### Event: UserInputService.InputEnded

**Signature:** `UserInputService.InputEnded(input: InputObject, gameProcessedEvent: boolean)`

This event fires when a user stops interacting with an input device such
as a mouse or gamepad, such as when they release a gamepad button. Can be
used along with [InputBegan](/docs/reference/engine/classes/UserInputService.md) and
[InputChanged](/docs/reference/engine/classes/UserInputService.md) to track when user
input begins, changes, and ends.

See also [InputBinding](/docs/reference/engine/classes/InputBinding.md) as a way to hook input device interactions
to [InputActions](/docs/reference/engine/classes/InputAction.md).

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `input` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance containing information about the user input. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.JumpRequest

**Signature:** `UserInputService.JumpRequest()`

This event fires when there is a jump request from the client, for example
when the client presses the spacebar or jump button on mobile. Default
behavior is to set the player's [Humanoid.Jump](/docs/reference/engine/classes/Humanoid.md) property to `true`
which makes the player's character jump.

Since this event fires multiple times for a single jump request, using a
[debounce](/docs/en-us/scripting/debounce.md) is recommended. This event does
not fire if [Player.Character](/docs/reference/engine/classes/Player.md) is set to nil.

*Security: None · Capabilities: Input*

**Disable Default Jumping**

This code sample disables default jumping for the player's character by
setting the [HumanoidStateType.Jumping](/docs/reference/engine/enums/HumanoidStateType.md) state to `false` and connects the
[JumpRequest](/docs/reference/engine/classes/UserInputService.md) event for handling custom
behavior upon jump request.

```lua
local UserInputService = game:GetService("UserInputService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

humanoid:SetStateEnabled(Enum.HumanoidStateType.Jumping, false)

local processJumpRequest = false

local COOLDOWN_TIME = 0.5

local function jumpRequest()
	if processJumpRequest == false then
		processJumpRequest = true
		-- Process custom jump request
		print("Jump requested!")
		-- Reset debounce variable after cooldown
		task.wait(COOLDOWN_TIME)
		processJumpRequest = false
	end
end

UserInputService.JumpRequest:Connect(jumpRequest)
```

### Event: UserInputService.LastInputTypeChanged

**Signature:** `UserInputService.LastInputTypeChanged(lastInputType: UserInputType)`

This event fires whenever the client's [UserInputType](/docs/reference/engine/enums/UserInputType.md) is changed.

To get the value of the last input type, regardless of whether it has
changed, use the
[GetLastInputType()](/docs/reference/engine/classes/UserInputService.md) method.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `lastInputType` | `UserInputType` | A [UserInputType](/docs/reference/engine/enums/UserInputType.md) indicating the last input type. |

### Event: UserInputService.PointerAction

**Signature:** `UserInputService.PointerAction(wheel: float, pan: Vector2, pinch: float, gameProcessedEvent: boolean)`

This event fires when the user performs a specific pointer action
(`wheel`, `pan`, `pitch`).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `wheel` | `float` | The mouse scroll wheel delta. Positive values indicate scrolling up and negative values indicate scrolling down. |
| `pan` | `Vector2` | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the trackpad pan movement delta in pixels. Touch pan is handled separately via [UserInputService.TouchPan](/docs/reference/engine/classes/UserInputService.md). |
| `pinch` | `float` | The pinch-to-zoom gesture delta from a trackpad. Touch pinch is handled separately via [UserInputService.TouchPinch](/docs/reference/engine/classes/UserInputService.md). |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. |

### Event: UserInputService.TextBoxFocused

**Signature:** `UserInputService.TextBoxFocused(textboxFocused: TextBox)`

This event fires when the client gains focus on a [TextBox](/docs/reference/engine/classes/TextBox.md),
typically when a user clicks/taps it to begin inputting text. Also fires
if the [TextBox](/docs/reference/engine/classes/TextBox.md) is focused using [TextBox:CaptureFocus()](/docs/reference/engine/classes/TextBox.md).
Can be used alongside
[TextBoxFocusReleased](/docs/reference/engine/classes/UserInputService.md) to
track when a [TextBox](/docs/reference/engine/classes/TextBox.md) loses focus.

See also [GetFocusedTextBox()](/docs/reference/engine/classes/UserInputService.md),
[TextBox.Focused](/docs/reference/engine/classes/TextBox.md), and [TextBox.FocusLost](/docs/reference/engine/classes/TextBox.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `textboxFocused` | `TextBox` | The [TextBox](/docs/reference/engine/classes/TextBox.md) that gained focus. |

**TextBox Modification on Focused and FocusReleased**

This example adjusts the [GuiObject.Transparency](/docs/reference/engine/classes/GuiObject.md) of [TextBox](/docs/reference/engine/classes/TextBox.md)
objects when they gain/lose focus.

```lua
local UserInputService = game:GetService("UserInputService")

local function textBoxFocused(textBox)
	textBox.BackgroundTransparency = 0
end

local function textBoxFocusReleased(textBox)
	textBox.BackgroundTransparency = 0.5
end

UserInputService.TextBoxFocused:Connect(textBoxFocused)
UserInputService.TextBoxFocusReleased:Connect(textBoxFocusReleased)
```

### Event: UserInputService.TextBoxFocusReleased

**Signature:** `UserInputService.TextBoxFocusReleased(textboxReleased: TextBox)`

This event fires when the client loses focus on a [TextBox](/docs/reference/engine/classes/TextBox.md),
typically when a user stops text entry by pressing <kbd>Enter</kbd> or
clicking/touching elsewhere on the screen. Can be used alongside
[TextBoxFocused](/docs/reference/engine/classes/UserInputService.md) to track when a
[TextBox](/docs/reference/engine/classes/TextBox.md) gains focus.

See also [GetFocusedTextBox()](/docs/reference/engine/classes/UserInputService.md),
[TextBox.Focused](/docs/reference/engine/classes/TextBox.md), and [TextBox.FocusLost](/docs/reference/engine/classes/TextBox.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `textboxReleased` | `TextBox` | The [TextBox](/docs/reference/engine/classes/TextBox.md) that lost focus. |

**TextBox Modification on Focused and FocusReleased**

This example adjusts the [GuiObject.Transparency](/docs/reference/engine/classes/GuiObject.md) of [TextBox](/docs/reference/engine/classes/TextBox.md)
objects when they gain/lose focus.

```lua
local UserInputService = game:GetService("UserInputService")

local function textBoxFocused(textBox)
	textBox.BackgroundTransparency = 0
end

local function textBoxFocusReleased(textBox)
	textBox.BackgroundTransparency = 0.5
end

UserInputService.TextBoxFocused:Connect(textBoxFocused)
UserInputService.TextBoxFocusReleased:Connect(textBoxFocusReleased)
```

### Event: UserInputService.TouchDrag

**Signature:** `UserInputService.TouchDrag(dragDirection: SwipeDirection, numberOfTouches: int, gameProcessedEvent: boolean)`

This event fires when the user drags on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. Use this event
to detect the start of a deliberate directional gesture (for example,
sliding an element left or right to reveal contextual actions) before the
user commits to a direction; for detecting a completed swipe or fling
gesture, use [TouchSwipe](/docs/reference/engine/classes/UserInputService.md) instead.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `dragDirection` | `SwipeDirection` | The predominant drag direction for the event ([Up](/docs/reference/engine/enums/SwipeDirection.md), [Down](/docs/reference/engine/enums/SwipeDirection.md), [Left](/docs/reference/engine/enums/SwipeDirection.md), or [Right](/docs/reference/engine/enums/SwipeDirection.md)). |
| `numberOfTouches` | `int` | Currently only supports one touch for a value of `1`. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchEnded

**Signature:** `UserInputService.TouchEnded(touch: InputObject, gameProcessedEvent: boolean)`

This event fires when a user releases their finger from the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. Can be paired
with [TouchStarted](/docs/reference/engine/classes/UserInputService.md) to determine when
a user starts and stops touching the screen.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touch` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance containing information about the user's input. This is the same object throughout the lifetime of the touch, so comparing [InputObjects](/docs/reference/engine/classes/InputObject.md) when they are touch objects is valid to determine if it's the same finger. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchLongPress

**Signature:** `UserInputService.TouchLongPress(touchPositions: Array, state: UserInputState, gameProcessedEvent: boolean)`

This event fires when a user holds at least one finger for a short amount
of time on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects indicating the position of the fingers involved in the gesture. |
| `state` | `UserInputState` | The [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchMoved

**Signature:** `UserInputService.TouchMoved(touch: InputObject, gameProcessedEvent: boolean)`

This event fires when a user moves their finger on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device, useful for
tracking whether a user is moving their finger on the screen and where
they're moving it. Can be paired with
[TouchStarted](/docs/reference/engine/classes/UserInputService.md) and
[TouchEnded](/docs/reference/engine/classes/UserInputService.md) to determine when a user
starts touching the screen, how their finger moves while touching it, and
when the they stop touching the screen.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touch` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance containing information about the user's input. Note that its [Position](/docs/reference/engine/classes/InputObject.md) is a [Vector3](/docs/reference/engine/datatypes/Vector3.md) but only includes **X** and **Y** coordinates (**Z** is always `0`). |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchPan

**Signature:** `UserInputService.TouchPan(touchPositions: Array, totalTranslation: Vector2, velocity: Vector2, state: UserInputState, gameProcessedEvent: boolean)`

This event fires when the user drags at least one finger on the screen of
a [TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2s](/docs/reference/engine/datatypes/Vector2.md) indicating the positions of the touches involved in the gesture. |
| `totalTranslation` | `Vector2` | The size of the pan gesture from start to end, in pixels. |
| `velocity` | `Vector2` | The speed of the pan gesture in pixels per second. |
| `state` | `UserInputState` | The [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchPinch

**Signature:** `UserInputService.TouchPinch(touchPositions: Array, scale: float, velocity: float, state: UserInputState, gameProcessedEvent: boolean)`

This event fires when a user performs a pinch gesture on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2s](/docs/reference/engine/datatypes/Vector2.md) indicating the screen position, in pixels, of the fingers involved in the pinch gesture. |
| `scale` | `float` | The magnitude of the pinch from start to finish (in pixels) divided by the starting pinch positions. |
| `velocity` | `float` | The speed of the pinch gesture in pixels per second. |
| `state` | `UserInputState` | The [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchRotate

**Signature:** `UserInputService.TouchRotate(touchPositions: Array, rotation: float, velocity: float, state: UserInputState, gameProcessedEvent: boolean)`

This event fires when a user rotates two fingers on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2s](/docs/reference/engine/datatypes/Vector2.md) indicating the positions of the fingers involved in the gesture. |
| `rotation` | `float` | The number of degree the gesture has rotated since the start of the gesture. |
| `velocity` | `float` | The change in rotation (in degrees) divided by the duration of the change (in seconds). |
| `state` | `UserInputState` | The [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchStarted

**Signature:** `UserInputService.TouchStarted(touch: InputObject, gameProcessedEvent: boolean)`

This event fires when a user places their finger on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. Can be paired
with [TouchEnded](/docs/reference/engine/classes/UserInputService.md) to determine when a
user starts and stops touching the screen.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touch` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance, which contains information about the user's input. This is the same object throughout the lifetime of the touch, so comparing [InputObjects](/docs/reference/engine/classes/InputObject.md) when they are touch objects is valid to determine if it's the same finger. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchSwipe

**Signature:** `UserInputService.TouchSwipe(swipeDirection: SwipeDirection, numberOfTouches: int, gameProcessedEvent: boolean)`

This event fires on a [TouchEnabled](/docs/reference/engine/classes/UserInputService.md)
device when a user places their finger(s) down on the screen, pans across
the screen, and lifts their finger(s) off with a certain speed of
movement.

For more precise tracking of touch input movement, use
[TouchMoved](/docs/reference/engine/classes/UserInputService.md).

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `swipeDirection` | `SwipeDirection` | An [SwipeDirection](/docs/reference/engine/enums/SwipeDirection.md) indicating the direction the user swiped. |
| `numberOfTouches` | `int` | Number of touches involved in the swipe gesture. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchTap

**Signature:** `UserInputService.TouchTap(touchPositions: Array, gameProcessedEvent: boolean)`

This event fires when a user taps their finger on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device, regardless of
whether the user taps in the 3D world or on a [GuiObject](/docs/reference/engine/classes/GuiObject.md) element.
If you're looking for an event that only fires when the user taps in the
3D world, use [TouchTapInWorld](/docs/reference/engine/classes/UserInputService.md).

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects indicating the position of the fingers involved in the tap gesture. |
| `gameProcessedEvent` | `boolean` | Indicates whether the engine internally observed this input and acted on it. Generally this refers to UI processing, so if a button was touched or clicked from this input, `gameProcessedEvent` will be `true`. |

### Event: UserInputService.TouchTapInWorld

**Signature:** `UserInputService.TouchTapInWorld(position: Vector2, processedByUI: boolean)`

This event fires when a user taps their finger on the screen of a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device and the tap
location is in the 3D world rather than on a [GuiObject](/docs/reference/engine/classes/GuiObject.md) element.

Note that this event only fires when the Roblox client window is in focus.
It will not fire when the window is minimized.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `position` | `Vector2` | A [Vector2](/docs/reference/engine/datatypes/Vector2.md) indicating the position of the tap. |
| `processedByUI` | `boolean` | Whether the user tapped a UI element. |

### Event: UserInputService.WindowFocused

**Signature:** `UserInputService.WindowFocused()`

This event fires when the window of the Roblox client gains focus,
typically when it is maximized or actively opened by the user. Can be used
alongside [WindowFocusReleased](/docs/reference/engine/classes/UserInputService.md)
to track when the client loses focus on a user's screen.

*Security: None · Capabilities: Input*

### Event: UserInputService.WindowFocusReleased

**Signature:** `UserInputService.WindowFocusReleased()`

This event fires when the window of the Roblox client loses focus,
typically when it is minimized by the user. Can be used alongside
[WindowFocused](/docs/reference/engine/classes/UserInputService.md) to track when the
client gains focus on a user's screen.

*Security: None · Capabilities: Input*

**Window Focus Away Script (LocalScript)**

The purpose of this code sample is to fire a server-side [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md)
to indicate when the player is "away" based on their client window being
minimized. When mimimized, the server creates a [ForceField](/docs/reference/engine/classes/ForceField.md) around the
player's character to shield them from damage.

The code below should be placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) within
[StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md) with the intention of running it in conjunction
with the server-side [Script](/docs/reference/engine/classes/Script.md) that follows it.

```lua
local UserInputService = game:GetService("UserInputService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local awayEvent = ReplicatedStorage:WaitForChild("AwayEvent")

local function focusGained()
	awayEvent:FireServer(false)
end

local function focusReleased()
	awayEvent:FireServer(true)
end

UserInputService.WindowFocused:Connect(focusGained)
UserInputService.WindowFocusReleased:Connect(focusReleased)
```

**Window Focus Away Script (Script)**

The following [Script](/docs/reference/engine/classes/Script.md), placed within [ServerScriptService](/docs/reference/engine/classes/ServerScriptService.md),
completes the [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) connection triggered by the
[LocalScript](/docs/reference/engine/classes/LocalScript.md) above.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local awayEvent = Instance.new("RemoteEvent")
awayEvent.Name = "AwayEvent"
awayEvent.Parent = ReplicatedStorage

local function manageForceField(player, away)
	if away then
		local forceField = Instance.new("ForceField")
		forceField.Parent = player.Character
	else
		local forceField = player.Character:FindFirstChildOfClass("ForceField")
		if forceField then
			forceField:Destroy()
		end
	end
end

awayEvent.OnServerEvent:Connect(manageForceField)
```

### Event: UserInputService.UserCFrameChanged

**Signature:** `UserInputService.UserCFrameChanged(type: UserCFrame, value: CFrame)`

> **Deprecated:** Use [VRService.UserCFrameChanged](/docs/reference/engine/classes/VRService.md) instead.

The UserCFrameChanged event fires when the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of a VR
device changes.

This event can be used to track the movement of a connected VR device.

Using the event, you can implement features such as moving the user's
in-game character limbs as the user moves their VR device. This can be
done by changing the CFrame of the user's in-game limbs to match the
CFrame changes of the VR device using the [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) enum and
_CFrame_ value arguments passed by the event.

To retrieve the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of a connected VR device, use
[UserInputService:GetUserCFrame()](/docs/reference/engine/classes/UserInputService.md).

As the event fires locally, it can only be used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

See also:

- [VRService](/docs/reference/engine/classes/VRService.md), used to implement support, including an identical
  event [VRService.UserHeadCFrameChanged](/docs/reference/engine/classes/VRService.md)
- [Camera.HeadLocked](/docs/reference/engine/classes/Camera.md), when this property is `true` the
  [Camera](/docs/reference/engine/classes/Camera.md) will automatically track the head motion of a player
  using a VR device
- [Camera:GetRenderCFrame()](/docs/reference/engine/classes/Camera.md), a method which retrieves the
  [CFrame](/docs/reference/engine/datatypes/CFrame.md) the [Camera](/docs/reference/engine/classes/Camera.md) is being orientated at, including
  the impact of VR devices

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `type` | `UserCFrame` | A [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) value indicating which body part moved. |
| `value` | `CFrame` | A [CFrame](/docs/reference/engine/datatypes/CFrame.md) value indicating the updated CFrame of the body part that moved. |

**VR Head Tracking**

This example demonstrates how to implement a head tracking script that mirrors
the movement of a virtual reality (VR) headset (the user's actual head) to
their in-game character's head.

The example first check if the user is using a VR device by checking the value
of the [VREnabled()](/docs/reference/engine/classes/VRService.md) property. This example only
works if the user is using a VR headset.

To determine the initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the character's head, the code
sample calls [GetUserCFrame()](/docs/reference/engine/classes/VRService.md) and passes
[UserCFrame.Head](/docs/reference/engine/enums/UserCFrame.md) as the argument.

To update the head's CFrame whenever the user's VR headset moves, the example
connects the [VRService.UserCFrameChanged](/docs/reference/engine/classes/VRService.md) event to the _TrackHead()_
function. When the event fires to indicate that a VR device moved, TrackHead()
checks if the headset moved. If the headset moved, the function updates the
CFrame of the character's head to the [CFrame](/docs/reference/engine/datatypes/CFrame.md) _value_ provided as an
argument.

As the UserCFrame enum also tracks VR left and right hand devices, the concept
of VR device tracking can be expanded to other character bodyparts.

In order for the example to work as expected, it must be placed in a
`LocalScript`.

```lua
local VRService = game:GetService("VRService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.CharacterAdded:Wait()
local head = character:WaitForChild("Head")

local function TrackHead(inputType, value)
	if inputType == Enum.UserCFrame.Head then
		head.CFrame = value
	end
end

if VRService.VREnabled then
	-- Set the initial CFrame
	head.CFrame = VRService:GetUserCFrame(Enum.UserCFrame.Head)

	-- Track VR headset movement and mirror for character's head
	VRService.UserCFrameChanged:Connect(TrackHead)
end
```

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