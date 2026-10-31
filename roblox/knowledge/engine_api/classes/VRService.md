---
name: VRService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Service responsible for handling interactions between Roblox and Virtual Reality (VR)."
---

# Class: VRService

> Service responsible for handling interactions between Roblox and Virtual
> Reality (VR).

## Description

**VRService** is responsible for handling interactions between Roblox and
Virtual Reality (VR). Its methods, properties, and events help you provide the
best experience for end users seeking to experience Roblox on VR devices.

See [VR Guidelines](/docs/en-us/production/publishing/vr-guidelines.md) for more
information on publishing an experience for VR devices.

## Code Samples

**VRService**

The following example demonstrates how to get the [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) of the
left controller and place a part at that point in real world space. The
[CFrame](/docs/reference/engine/datatypes/CFrame.md) of the controller changes whenever the device moves, so you
should update the necessary parts whenever [VRService.UserCFrameChanged](/docs/reference/engine/classes/VRService.md)
fires.

```lua
local VRService = game:GetService("VRService")

local part = workspace.Part

local handOffset = VRService:GetUserCFrame(Enum.UserCFrame.LeftHand)
-- Account for headscale
handOffset = handOffset.Rotation + handOffset.Position * workspace.CurrentCamera.HeadScale

part.CFrame = workspace.CurrentCamera.CFrame * handOffset
```

## Properties

### Property: VRService.AutomaticScaling

```json
{
  "type": "VRScaling",
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

When set to [VRScaling.World](/docs/reference/engine/enums/VRScaling.md), [Camera.HeadScale](/docs/reference/engine/classes/Camera.md) adjusts so
that the scale of the world is seen from the avatar's perspective. A
player with a small avatar will perceive the objects around them as larger
than a player with a large avatar will.

### Property: VRService.AvatarGestures

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
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

When set to true, a VR player will be able to animate their hands and head
using their controllers and headset. Set this to `false` for experiences
where VR hand and head tracking conflicts with custom game mechanics, such
as bespoke avatar rigs or weapon systems incompatible with IK-driven
gestures.

This property must be set on the server.

### Property: VRService.ControllerModels

```json
{
  "type": "VRControllerModelMode",
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

Controls how the models representing the player's VR hand controllers are
displayed ([VRControllerModelMode](/docs/reference/engine/enums/VRControllerModelMode.md)). When set to
[Transparent](/docs/reference/engine/enums/VRControllerModelMode.md), the controller
models are shown with transparency; when set to
[Disabled](/docs/reference/engine/enums/VRControllerModelMode.md), the controller models are
not rendered.

Defaults to [Transparent](/docs/reference/engine/enums/VRControllerModelMode.md).

### Property: VRService.FadeOutViewOnCollision

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
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

When true, a VR player's view fades to black when their head collides with
an object. This property prevents players from being able to see through
walls while in VR. The default value is true.

### Property: VRService.GuiInputUserCFrame

```json
{
  "type": "UserCFrame",
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
  "category": "Behavior",
  "capabilities": [
    "Input"
  ]
}
```

This property describes what [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) is responsible for input in
VR. For instance, if a VR headset is responsible, the value of this
property will be [UserCFrame.Head](/docs/reference/engine/enums/UserCFrame.md).

To check if Roblox detects any VR devices, which would be responsible for
input in VR, you can check the [VREnabled](/docs/reference/engine/classes/VRService.md)
property.

**VRService.GuiInputUserCFrame**

This example checks if Roblox detects a VR device. If a VR device is detected,
this prints the name of the UserCFrame responsible for VR input. If not, this
example prints "No VR device detected!".

```lua
local VRService = game:GetService("VRService")

if VRService.VREnabled then
	print(VRService.GuiInputUserCFrame.Name)
else
	print("No VR device detected!")
end
```

### Property: VRService.LaserPointer

```json
{
  "type": "VRLaserPointerMode",
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

Controls the mode of the laser pointer that a VR player uses to point at
and interact with the user interface ([VRLaserPointerMode](/docs/reference/engine/enums/VRLaserPointerMode.md)). Set it
to [Disabled](/docs/reference/engine/enums/VRLaserPointerMode.md) to hide the laser pointer,
[Pointer](/docs/reference/engine/enums/VRLaserPointerMode.md) to show a single pointer, or
[DualPointer](/docs/reference/engine/enums/VRLaserPointerMode.md) to show a pointer for
each hand.

Defaults to [Pointer](/docs/reference/engine/enums/VRLaserPointerMode.md).

### Property: VRService.ThirdPersonFollowCamEnabled

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

Read-only. Indicates whether the third-person follow camera is enabled for
the VR user. Its value mirrors the user's VR comfort setting and updates
automatically whenever the user changes that setting, firing a changed
signal so that scripts can respond. It cannot be set from a script.

### Property: VRService.VREnabled

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

This property describes whether the user is using a virtual reality (VR)
device.

If a VR device is enabled, you can interact with its location and movement
through methods such as [UserInputService:GetUserCFrame()](/docs/reference/engine/classes/UserInputService.md). You can
also react to VR device movement using the
[UserInputService.UserCFrameChanged](/docs/reference/engine/classes/UserInputService.md) event.

```lua
local VRService = game:GetService("VRService")

local isUsingVR = VRService.VREnabled
if isUsingVR then
	print("User is using a VR headset!")
else
	print("User is not using a VR headset!")
end
```

This property can only be used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

#### See Also

- [Camera.HeadLocked](/docs/reference/engine/classes/Camera.md)
- [UserInputService:GetUserCFrame()](/docs/reference/engine/classes/UserInputService.md)
- [UserInputService.UserCFrameChanged](/docs/reference/engine/classes/UserInputService.md)

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

## Methods

### Method: VRService:GetTouchpadMode

**Signature:** `VRService:GetTouchpadMode(pad: VRTouchpad): VRTouchpadMode`

This method returns the [VRTouchpadMode](/docs/reference/engine/enums/VRTouchpadMode.md) indicating the mode of a
specified [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md). The returned mode indicates how the user
interacts with their touchpad to play the game.

This can also be used alongside the several [UserInputService](/docs/reference/engine/classes/UserInputService.md) VR
methods and events.

This method will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pad` | `VRTouchpad` |  | The specified [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md). |

**Returns:** `VRTouchpadMode` — The mode of the specified [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md).

**VRService:GetTouchpadMode**

This example retrieves and prints the name of the user's current
VRTouchpad.Left touchpad mode.

```lua
local VRService = game:GetService("VRService")

VRService:GetTouchpadMode(Enum.VRTouchpad.Left)
```

### Method: VRService:GetUserCFrame

**Signature:** `VRService:GetUserCFrame(type: UserCFrame): CFrame`

This method returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) describing the position and
orientation of a specified virtual reality (VR) device as an offset from a
point in real world space. This method should be used when implementing VR
compatibility into a game to obtain and track the movement of a connected
VR device.

By using the method, developers can implement features such as
re-positioning the user's in-game character corresponding to the location
of a connected VR device. This can be done by changing the _CFrame_ of the
user's in-game character to match the _CFrame_ of the specified VR device
using the UserCFrame enum and _CFrame_ value arguments passed by the
event.

[VRService](/docs/reference/engine/classes/VRService.md) also provides a
[UserCFrameChanged](/docs/reference/engine/classes/VRService.md) event that
automatically fires when the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of connected VR device
changes, so long it is used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

This method will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `UserCFrame` |  | The specified [UserCFrame](/docs/reference/engine/enums/UserCFrame.md). |

**Returns:** `CFrame` — A [CFrame](/docs/reference/engine/datatypes/CFrame.md) describing the position and orientation of the
specified VR device as an offset from a point in real-world space.

**VRService:GetUserCFrame**

This example positions a part at the player's left hand, assuming
Camera.HeadLocked = true

```lua
local Workspace = game:GetService("Workspace")
local VRService = game:GetService("VRService")

local camera = Workspace.CurrentCamera
local part = script.Parent.Part
local handOffset = VRService:GetUserCFrame(Enum.UserCFrame.LeftHand)

-- Account for headscale
handOffset = handOffset.Rotation + handOffset.Position * camera.HeadScale
part.CFrame = camera.CFrame * handOffset
```

### Method: VRService:GetUserCFrameEnabled

**Signature:** `VRService:GetUserCFrameEnabled(type: UserCFrame): boolean`

This method returns true if the specified [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) virtual
reality device (VR) is available to be listened to. It can be used to
determine whether a specified VR device, such as [UserCFrame.Head](/docs/reference/engine/enums/UserCFrame.md),
is connected to the user's game.

This can also be used alongside the several [UserInputService](/docs/reference/engine/classes/UserInputService.md) VR
methods and events.

This method will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `UserCFrame` |  | The specified type of VR device. |

**Returns:** `boolean` — A boolean indicating whether the specified VR device is enabled
(`true`) or disabled (`false`).

**VRService:GetUserCFrameEnabled**

This example indicates whether the UserCFrame.Head VR device is enabled or
disabled for the user. If the device is enabled, this prints "VR device is
enabled!". If the device is disabled, this prints "VR device is disabled!".

```lua
local VRService = game:GetService("VRService")

local isEnabled = VRService:GetUserCFrameEnabled(Enum.UserCFrame.Head)
if isEnabled then
	print("VR device is enabled!")
else
	print("VR device is disabled!")
end
```

### Method: VRService:RecenterUserHeadCFrame

**Signature:** `VRService:RecenterUserHeadCFrame(): ()`

This method re-centers the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the user's head to the
current location of the VR headset being worn by the user. It can be used
to ensure that the user's in-game head is positioned according to the
location of the user's VR headset.

This behaves identically to
[UserInputService:RecenterUserHeadCFrame()](/docs/reference/engine/classes/UserInputService.md).

This method will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

**VRService:RecenterUserHeadCFrame**

This example fires the function to recenter the CFrame of the user's head to
the current location of the VR headset being worn by the user.

```lua
local VRService = game:GetService("VRService")

VRService:RecenterUserHeadCFrame()
```

### Method: VRService:RequestNavigation

**Signature:** `VRService:RequestNavigation(cframe: CFrame, inputUserCFrame: UserCFrame): ()`

This method requests navigation to the specified [CFrame](/docs/reference/engine/datatypes/CFrame.md) using
the specified [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) as the origin for the visualizer parabola.
It can be used to incorporate virtual reality (VR) into your game by
providing a means to visualize a navigation path from the user's VR device
to a destination.

[VRService](/docs/reference/engine/classes/VRService.md) has a similar event,
[NavigationRequested](/docs/reference/engine/classes/VRService.md), used to detect
such requests. This can also be used alongside the several
[UserInputService](/docs/reference/engine/classes/UserInputService.md) VR methods and events.

This method will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cframe` | `CFrame` |  | The specified [CFrame](/docs/reference/engine/datatypes/CFrame.md) coordinates. |
| `inputUserCFrame` | `UserCFrame` |  | The VR device for which the navigation is requested. |

**Returns:** `()`

**VRService:RequestNavigation**

This example requests navigation from the user's **UserCFrame.Head**
coordinates to the CFrame coordinates of a `Part` named
_NavigationDestination_.

_Note:_ In order for this to work, a Part named _NavigationDestination_ must
exist in the game's Workspace.

```lua
local VRService = game:GetService("VRService")

local destination = workspace:FindFirstChild("NavigationDestination")

VRService:RequestNavigation(Enum.UserCFrame.Head, destination.CFrame)
```

### Method: VRService:SetTouchpadMode

**Signature:** `VRService:SetTouchpadMode(pad: VRTouchpad, mode: VRTouchpadMode): ()`

This method sets the mode of the specified [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md) to the
specified [VRTouchpadMode](/docs/reference/engine/enums/VRTouchpadMode.md). It can be used to change the user's
virtual reality (VR) touchpad mode so that the user interacts with the
game differently using the touchpad.

This can also be used alongside the several [UserInputService](/docs/reference/engine/classes/UserInputService.md) VR
methods and events.

This method will only work when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pad` | `VRTouchpad` |  | The specified [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md) you want to set the mode of. |
| `mode` | `VRTouchpadMode` |  | The mode you want to set the specified [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md) to. |

**Returns:** `()`

**VRService:SetTouchpadMode**

This example sets the user's VRTouchpad.Left touchpad mode to TouchMode.Touch.
This means that the left touchpad is treated as ButtonB.

```lua
local VRService = game:GetService("VRService")

VRService:SetTouchpadMode(Enum.VRTouchpad.Left, Enum.VRTouchpadMode.Touch)
```

## Events

### Event: VRService.NavigationRequested

**Signature:** `VRService.NavigationRequested(cframe: CFrame, inputUserCFrame: UserCFrame)`

This event fires when navigation is requested from [VRService](/docs/reference/engine/classes/VRService.md) for a
specified [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) VR device. It fires with a [CFrame](/docs/reference/engine/datatypes/CFrame.md)
coordinate and the specified [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) indicating the device
requesting the navigation.

This event can be used alongside [UserInputService](/docs/reference/engine/classes/UserInputService.md) service events
and methods.

Since this event fires locally, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cframe` | `CFrame` | The requested [CFrame](/docs/reference/engine/datatypes/CFrame.md) coordinates. |
| `inputUserCFrame` | `UserCFrame` | Indicates the VR device for which navigation is requested. |

**VRService.NavigationRequested**

This example prints the name of the UserCFrame VR device making the request,
and the CFrame coordinates passed.

```lua
local VRService = game:GetService("VRService")

VRService.NavigationRequested:Connect(function(cframe, inputUserCFrame)
	print(inputUserCFrame.Name .. " made request with CFrame: " .. cframe)
end)
```

### Event: VRService.TouchpadModeChanged

**Signature:** `VRService.TouchpadModeChanged(pad: VRTouchpad, mode: VRTouchpadMode)`

This event fires if the [VRTouchpadMode](/docs/reference/engine/enums/VRTouchpadMode.md) of a [VRTouchpad](/docs/reference/engine/enums/VRTouchpad.md) is
changed. You can use this event to track the states of VR touchpads
connected via the user's client.

This event can be used alongside [UserInputService](/docs/reference/engine/classes/UserInputService.md) service events
and methods.

Since this event fires locally, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `pad` | `VRTouchpad` | The touchpad that changed mode. |
| `mode` | `VRTouchpadMode` | The new mode. |

**VRService.TouchpadModeChanged**

This example fires when the state of a VRTouchpad changes. It prints the name
of the Touchpad that changed, and the state that it changed to.

```lua
local VRService = game:GetService("VRService")

VRService.TouchpadModeChanged:Connect(function(pad, mode)
	print(pad.Name .. " Touchpad changed to state: " .. mode.Name)
end)
```

### Event: VRService.UserCFrameChanged

**Signature:** `VRService.UserCFrameChanged(type: UserCFrame, value: CFrame)`

This event fires when a [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) is changed, for instance when
the user moves a connected VR device. It can be used alongside
[GetUserCFrame()](/docs/reference/engine/classes/VRService.md) to track the
[CFrame](/docs/reference/engine/datatypes/CFrame.md) coordinates of a VR device, and when it changes/moves.
It can also be used alongside [UserInputService](/docs/reference/engine/classes/UserInputService.md) service events and
methods.

Since this event fires locally, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `type` | `UserCFrame` | The type of VR device that changed. |
| `value` | `CFrame` | The updated [CFrame](/docs/reference/engine/datatypes/CFrame.md) coordinates of the VR device after the change. |

**VRService.UserCFrameChanged**

This event fires when the user moves a connected VR device. When the event
fires, this prints the name of the VR device type that changed, and the
updated CFrame coordinates.

```lua
local VRService = game:GetService("VRService")

VRService.UserCFrameChanged:Connect(function(userCFrameType, cframeValue)
	print(userCFrameType.Name .. " changed. Updated Frame: " .. tostring(cframeValue))
end)
```

### Event: VRService.UserCFrameEnabled

**Signature:** `VRService.UserCFrameEnabled(type: UserCFrame, enabled: boolean)`

This event fires when a [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) is enabled or disabled. It can
be used alongside
[GetUserCFrameEnabled()](/docs/reference/engine/classes/VRService.md) to track
whether a specified [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) is enabled, and when its
state changes. It can also be used alongside [UserInputService](/docs/reference/engine/classes/UserInputService.md)
service events and methods.

Since this event fires locally, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `type` | `UserCFrame` | The [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) getting enabled or disabled. |
| `enabled` | `boolean` | A boolean indicating whether the [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) is enabled (`true`) or disabled (`false`). |

**VRService.UserCFrameEnabled**

This example fires when a UserCFrame changes state, printing the name of the
changed UserCFrame and whether it changed got enabled or disabled.

```lua
local VRService = game:GetService("VRService")

VRService.UserCFrameEnabled:Connect(function(type, enabled)
	if enabled then
		print(type.Name .. " got enabled!")
	else
		print(type.Name .. " got disabled!")
	end
end)
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