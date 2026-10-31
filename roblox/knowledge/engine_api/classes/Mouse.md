---
name: Mouse
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Legacy object that contains members useful for pointer input."
---

# Class: Mouse

> Legacy object that contains members useful for pointer input.

## Description

**Mouse** has been superseded by [UserInputService](/docs/reference/engine/classes/UserInputService.md) and
[ContextActionService](/docs/reference/engine/classes/ContextActionService.md), which cover a broader scope, are more feature
rich, and support **cross-platform** patterns better. It remains supported
because of its widespread use, but you should strongly consider using these
alternatives.

The **Mouse** object houses various API for pointers, primarily for buttons
and raycasting. It can be accessed through [Player:GetMouse()](/docs/reference/engine/classes/Player.md) called on
the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) in a [LocalScript](/docs/reference/engine/classes/LocalScript.md). It is also passed by
the [Tool.Equipped](/docs/reference/engine/classes/Tool.md) event.

- It is most notable for the [Icon](/docs/reference/engine/classes/Mouse.md) property, which changes
  the cursor's appearance.
- It continually raycasts the screen mouse position into the 3D world using
  the [TargetFilter](/docs/reference/engine/classes/Mouse.md) property, storing the results of
  the raycast in the [Hit](/docs/reference/engine/classes/Mouse.md), [Target](/docs/reference/engine/classes/Mouse.md), and
  [TargetSurface](/docs/reference/engine/classes/Mouse.md) properties. These can be useful
  for simple cases, but [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) should be used in more
  complicated [raycasting](/docs/en-us/workspace/raycasting.md) scenarios.
- [Plugins](/docs/reference/engine/classes/Plugin.md) can use [Plugin:GetMouse()](/docs/reference/engine/classes/Plugin.md) to get a
  [PluginMouse](/docs/reference/engine/classes/PluginMouse.md), which behaves similarly.

```lua
-- From a LocalScript:
local Players = game:GetService("Players")
local player = Players.LocalPlayer
local mouse = player:GetMouse()
-- Setting the mouse icon
mouse.Icon = "rbxasset://SystemCursors/Wait"
```

Note:

- This object does not control/restrict pointer movement. For this, see
  [UserInputService.MouseBehavior](/docs/reference/engine/classes/UserInputService.md) and
  [UserInputService.MouseDeltaSensitivity](/docs/reference/engine/classes/UserInputService.md).
- If two functions are connected to same input event, such as
  [Button1Down](/docs/reference/engine/classes/Mouse.md), **both** functions will run when the
  event fires. There is no concept of sinking/passing input, as events don't
  support this behavior. However, [ContextActionService](/docs/reference/engine/classes/ContextActionService.md) does have this
  behavior through [BindAction](/docs/reference/engine/classes/ContextActionService.md).
- While a mouse may not be available on all platforms, Mouse will still
  function on mobile (touch) and console (gamepad), which don't typically have
  mice or pointer hardware. For explicit cross-platform behaviors, use
  [UserInputService](/docs/reference/engine/classes/UserInputService.md) and [ContextActionService](/docs/reference/engine/classes/ContextActionService.md).

  See [Input and Camera](/docs/en-us/input.md) for more information on
  customizing inputs in your experience.

## Properties

### Property: Mouse.Hit

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property indicates [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the mouse's position in 3D
space. Note that [Mouse.TargetFilter](/docs/reference/engine/classes/Mouse.md) and its descendants will be
ignored.

Developers can get obtain the position of Hit like so:

```
local position = mouse.Hit.Position
```

Hit is often used by [Tools](/docs/reference/engine/classes/Tool.md) to fire a weapon towards the mouse
in third person.

Developers looking for the [BasePart](/docs/reference/engine/classes/BasePart.md) the mouse is pointing at
should use [Mouse.Target](/docs/reference/engine/classes/Mouse.md).

#### How is Mouse.Hit calculated?

The position of the Hit CFrame is calculated as the point of intersection
between the mouse's internal [Ray](/docs/reference/engine/datatypes/Ray.md) (an extended version of
[Mouse.UnitRay](/docs/reference/engine/classes/Mouse.md)) and an object in 3D space (such as a part).

The orientation of the Hit CFrame corresponds with the direction of the
[Mouse.UnitRay](/docs/reference/engine/classes/Mouse.md).

```
local unitRayDirection = mouse.UnitRay.Direction
local mouseHitDirection = mouse.Hit.lookVector
-- unitRayDirection ≈ mouseHitDirection
-- the vectors are approximately equal
```

Note, the roll of the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) is not used when
calculating the orientation of the Hit [CFrame](/docs/reference/engine/datatypes/CFrame.md).

The mouse's internal ray extends for 1,000 studs. If the mouse is not
pointing at an object in 3D space (for example when pointing at the sky),
this property will be 1,000 studs away from the
[Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md).

**Mouse.Hit Laser Beam**

The code in this sample, when placed inside a `LocalScript` within
`StarterPlayerScripts` will draw a red laser beam between the character's head
and [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) at all times.

Note, this beam will pass directly through obstructions in third person as the
`Mouse`'s raycasting is done from the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) not the
head.

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local beam = Instance.new("Beam")
beam.Segments = 1
beam.Width0 = 0.2
beam.Width1 = 0.2
beam.Color = ColorSequence.new(Color3.new(1, 0, 0))
beam.FaceCamera = true

local attachment0 = Instance.new("Attachment")
local attachment1 = Instance.new("Attachment")
beam.Attachment0 = attachment0
beam.Attachment1 = attachment1

beam.Parent = workspace.Terrain
attachment0.Parent = workspace.Terrain
attachment1.Parent = workspace.Terrain

local function onRenderStep()
	local character = player.Character
	if not character then
		beam.Enabled = false
		return
	end

	local head = character:FindFirstChild("Head")
	if not head then
		beam.Enabled = false
		return
	end

	beam.Enabled = true

	local origin = head.Position
	local finish = mouse.Hit.Position

	attachment0.Position = origin
	attachment1.Position = finish
end

RunService.RenderStepped:Connect(onRenderStep)
```

**Mouse Origin vs Mouse Hit vs CurrentCamera Position**

The code below visualizes the difference between [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) and
[Mouse.Origin](/docs/reference/engine/classes/Mouse.md). In order to do this, the code uses the
[Vector3](/docs/reference/engine/datatypes/Vector3.md) positions of the hit and origin [CFrame](/docs/reference/engine/datatypes/CFrame.md) values
using `.p`.

The difference is that the origin is "where the mouse came from" (its origin)
and the hit is the position where the mouse hits (is when the player presses
their mouse).

This example also visualizes that the mouse origin is very similar to the
position of the `CurrentCamera` by printing the magnitude (distance) between
the two positions.

```lua
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local player = Players.LocalPlayer
local camera = Workspace.CurrentCamera
local mouse = player:GetMouse()
local camPos = camera.CFrame.Position

local function onButton1Down()
	print("Mouse.Hit:", mouse.Hit.Position)
	print("camPos:", camPos)
	print("Mouse.Origin:", mouse.Origin.Position)
	print("Magnitude:", (mouse.Origin.Position - camPos).Magnitude)
end

mouse.Button1Down:Connect(onButton1Down)
```

### Property: Mouse.Icon

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

**Icon** is a property that determines the image used as the pointer. If
blank, a default arrow is used. While the cursor hovers over a
[GuiButton](/docs/reference/engine/classes/GuiButton.md), this property is temporarily ignored.

To hide the cursor entirely, **do not** use a transparent image &ndash;
instead, set [UserInputService.MouseIconEnabled](/docs/reference/engine/classes/UserInputService.md) to false.

For getting/setting the user mouse icon in experiences, you should use
[UserInputService.MouseIcon](/docs/reference/engine/classes/UserInputService.md). [Mouse.Icon](/docs/reference/engine/classes/Mouse.md) will be deprecated
after the new API for plugins to set the mouse cursor is released.

##### Designing a Cursor

The following guidelines may prove useful when creating your own mouse
cursors:

- The dimensions of the image used determines the size of the cursor.
- The dimensions of the image should not exceed 256 pixels on any axis.
- The **center** of the image is where mouse inputs are issued.
- The default mouse image is 64x64 pixels, with the mouse taking up 17x24
  pixels of space.

##### System Cursors

When using a [PluginMouse](/docs/reference/engine/classes/PluginMouse.md) retrieved from [Plugin:GetMouse()](/docs/reference/engine/classes/Plugin.md),
you can use the following icons similar to your system's default cursors,
such as hands, arrows, I-beams, etc. You can use these with GUI events
like [MouseEnter](/docs/reference/engine/classes/GuiObject.md),
[MouseLeave](/docs/reference/engine/classes/GuiObject.md), and
[MouseButton1Down](/docs/reference/engine/classes/GuiButton.md) to provide a
consistent Studio experience when interacting with certain kinds of GUI
components. Note that these only work for Studio plugins; they will not
work for other [Mouse](/docs/reference/engine/classes/Mouse.md) objects.

| Look* | Asset | Suggested Use |
| --- | --- | --- |
|  | `rbxasset://SystemCursors/Arrow` | Default clicking and selection. |
|  | `rbxasset://SystemCursors/PointingHand` | Hovering over an active link/button. |
|  | `rbxasset://SystemCursors/OpenHand` | Hovering over a draggable item. |
|  | `rbxasset://SystemCursors/ClosedHand` | Dragging an item. |
|  | `rbxasset://SystemCursors/IBeam` | Hovering in a text field. |
|  | `rbxasset://SystemCursors/SizeNS` | Hovering over a vertical resize handle. |
|  | `rbxasset://SystemCursors/SizeEW` | Hovering over a horizontal resize handle. |
|  | `rbxasset://SystemCursors/SizeNESW` | Hovering over a corner resize handle. |
|  | `rbxasset://SystemCursors/SizeNWSE` | Hovering over a corner resize handle. |
|  | `rbxasset://SystemCursors/SizeAll` | Hovering over a multi-direction resize handle. |
|  | `rbxasset://SystemCursors/SplitNS` | Hovering over a vertical "split" handle. |
|  | `rbxasset://SystemCursors/SplitEW` | Hovering over a horizontal "split" handle. |
|  | `rbxasset://SystemCursors/Forbidden` | Hovering over a locked/forbidden item. |
|  | `rbxasset://SystemCursors/Wait` | Indicating an action is in progress. |
|  | `rbxasset://SystemCursors/Busy` | Indicating the system is busy. |
|  | `rbxasset://SystemCursors/Cross` | Hovering over a pinpoint selection area. |

<figcaption>* These appearances are approximations &mdash; the actual look is dependent on your operating system.</figcaption>

**Dragon Mouse Icon**

This example changes the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) mouse icon to look like a
dragon image.

```lua
local Players = game:GetService("Players")

local mouse = Players.LocalPlayer:GetMouse()
mouse.Icon = "http://www.roblox.com/asset?id=163023520"
```

### Property: Mouse.IconContent

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

**Icon** is a property that determines the image used as the pointer. If
blank, a default arrow is used. While the cursor hovers over a
[GuiButton](/docs/reference/engine/classes/GuiButton.md), this property is temporarily ignored. This property
only supports asset URIs.

To hide the cursor entirely, **do not** use a transparent image &ndash;
instead, set [UserInputService.MouseIconEnabled](/docs/reference/engine/classes/UserInputService.md) to false.

For getting/setting the user mouse icon in experiences, you should use
[UserInputService.MouseIcon](/docs/reference/engine/classes/UserInputService.md). [Mouse.Icon](/docs/reference/engine/classes/Mouse.md) will be deprecated
after the new API for plugins to set the mouse cursor is released.

##### Designing a Cursor

The following guidelines may prove useful when creating your own mouse
cursors:

- The dimensions of the image used determines the size of the cursor.
- The dimensions of the image should not exceed 256 pixels on any axis.
- The **center** of the image is where mouse inputs are issued.
- The default mouse image is 64x64 pixels, with the mouse taking up 17x24
  pixels of space.

##### System Cursors

When using a [PluginMouse](/docs/reference/engine/classes/PluginMouse.md) retrieved from [Plugin:GetMouse()](/docs/reference/engine/classes/Plugin.md),
you can use the following icons similar to your system's default cursors,
such as hands, arrows, I-beams, etc. You can use these with GUI events
like [MouseEnter](/docs/reference/engine/classes/GuiObject.md),
[MouseLeave](/docs/reference/engine/classes/GuiObject.md), and
[MouseButton1Down](/docs/reference/engine/classes/GuiButton.md) to provide a
consistent Studio experience when interacting with certain kinds of GUI
components. Note that these only work for Studio plugins; they will not
work for other [Mouse](/docs/reference/engine/classes/Mouse.md) objects.

| Look* | Asset | Suggested Use |
| --- | --- | --- |
|  | `rbxasset://SystemCursors/Arrow` | Default clicking and selection. |
|  | `rbxasset://SystemCursors/PointingHand` | Hovering over an active link/button. |
|  | `rbxasset://SystemCursors/OpenHand` | Hovering over a draggable item. |
|  | `rbxasset://SystemCursors/ClosedHand` | Dragging an item. |
|  | `rbxasset://SystemCursors/IBeam` | Hovering in a text field. |
|  | `rbxasset://SystemCursors/SizeNS` | Hovering over a vertical resize handle. |
|  | `rbxasset://SystemCursors/SizeEW` | Hovering over a horizontal resize handle. |
|  | `rbxasset://SystemCursors/SizeNESW` | Hovering over a corner resize handle. |
|  | `rbxasset://SystemCursors/SizeNWSE` | Hovering over a corner resize handle. |
|  | `rbxasset://SystemCursors/SizeAll` | Hovering over a multi-direction resize handle. |
|  | `rbxasset://SystemCursors/SplitNS` | Hovering over a vertical "split" handle. |
|  | `rbxasset://SystemCursors/SplitEW` | Hovering over a horizontal "split" handle. |
|  | `rbxasset://SystemCursors/Forbidden` | Hovering over a locked/forbidden item. |
|  | `rbxasset://SystemCursors/Wait` | Indicating an action is in progress. |
|  | `rbxasset://SystemCursors/Busy` | Indicating the system is busy. |
|  | `rbxasset://SystemCursors/Cross` | Hovering over a pinpoint selection area. |

<figcaption>* These appearances are approximations &mdash; the actual look is dependent on your operating system.</figcaption>

**Dragon Mouse Icon**

This example changes the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) mouse icon to look like a
dragon image.

```lua
local Players = game:GetService("Players")

local mouse = Players.LocalPlayer:GetMouse()
mouse.Icon = "http://www.roblox.com/asset?id=163023520"
```

### Property: Mouse.Origin

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

The origin [Mouse](/docs/reference/engine/classes/Mouse.md) property is a [CFrame](/docs/reference/engine/datatypes/CFrame.md) indicating where
the mouse originated from. It is positioned at the
[Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) and oriented toward the mouse's 3D
position.

[Mouse.UnitRay](/docs/reference/engine/classes/Mouse.md) starts at the same position as Origin, and extends
for a stud in the same direction.

```lua
local unitRay = mouse.UnitRay
local origin = mouse.Origin
-- unitRay.Direction = origin.p
-- unitRay.Direction ≈ origin.lookVector
```

For the position of the [Mouse](/docs/reference/engine/classes/Mouse.md) in 3D space, see [Mouse.Hit](/docs/reference/engine/classes/Mouse.md).

**Mouse Origin vs Mouse Hit vs CurrentCamera Position**

The code below visualizes the difference between [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) and
[Mouse.Origin](/docs/reference/engine/classes/Mouse.md). In order to do this, the code uses the
[Vector3](/docs/reference/engine/datatypes/Vector3.md) positions of the hit and origin [CFrame](/docs/reference/engine/datatypes/CFrame.md) values
using `.p`.

The difference is that the origin is "where the mouse came from" (its origin)
and the hit is the position where the mouse hits (is when the player presses
their mouse).

This example also visualizes that the mouse origin is very similar to the
position of the `CurrentCamera` by printing the magnitude (distance) between
the two positions.

```lua
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local player = Players.LocalPlayer
local camera = Workspace.CurrentCamera
local mouse = player:GetMouse()
local camPos = camera.CFrame.Position

local function onButton1Down()
	print("Mouse.Hit:", mouse.Hit.Position)
	print("camPos:", camPos)
	print("Mouse.Origin:", mouse.Origin.Position)
	print("Magnitude:", (mouse.Origin.Position - camPos).Magnitude)
end

mouse.Button1Down:Connect(onButton1Down)
```

### Property: Mouse.Target

```json
{
  "type": "BasePart",
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

The object in 3D space the [mouse](/docs/reference/engine/classes/Mouse.md) is pointing to.

Note:

- If [Mouse.TargetFilter](/docs/reference/engine/classes/Mouse.md) has been set, the target filter and its
  descendants will be ignored.
- When the mouse is not pointing at a [BasePart](/docs/reference/engine/classes/BasePart.md), for example when
  it is pointing at the sky, Target will be `nil`.
- Developers looking for the position of the mouse in 3D space should use
  [Mouse.Hit](/docs/reference/engine/classes/Mouse.md).

**Color Randomizer Tool**

When placed in a `LocalScript` in `StarterPlayerScripts`, the following code
changes the [BasePart.BrickColor](/docs/reference/engine/classes/BasePart.md) of every `BasePart` the player clicks
on, such as the spawn location or baseplate.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local mouse = player:GetMouse()

mouse.Button1Down:Connect(function()
	local target = mouse.Target

	if target then
		print("Clicked:", target:GetFullName())

		if target:IsA("BasePart") then
			target.BrickColor = BrickColor.random()
		end
	end
end)
```

### Property: Mouse.TargetFilter

```json
{
  "type": "Instance",
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

This property determines an object to be ignored by the mouse when
calculating [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) and [Mouse.Target](/docs/reference/engine/classes/Mouse.md). The descendants of
the object are also ignored, so it is possible to ignore multiple objects
so long as they are a descendant of the object to which this property is
set. This property is useful when filtering models containing special
effects or decorations that should not affect [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) or
[Mouse.Target](/docs/reference/engine/classes/Mouse.md).

This property can be set to any [Instance](/docs/reference/engine/classes/Instance.md) or `nil`, for example:

```lua
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

local player = Players.LocalPlayer
local mouse = player:GetMouse()
mouse.TargetFilter = Workspace.Model
```

Note that the [Character](/docs/reference/engine/classes/Player.md) of the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md) is ignored by the mouse automatically.

### Property: Mouse.TargetSurface

```json
{
  "type": "NormalId",
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

This property indicates the [NormalId](/docs/reference/engine/enums/NormalId.md) of the [BasePart](/docs/reference/engine/classes/BasePart.md)
surface at which the mouse is pointing. This property is derived from the
world position of mouse ([Mouse.Hit](/docs/reference/engine/classes/Mouse.md)) and the part toward which the
mouse is pointing ([Mouse.Target](/docs/reference/engine/classes/Mouse.md)).

This property isn't meaningful when the mouse is not pointing at a part,
for example when the mouse is pointing at the sky. At the moment, this
property is set to 'Right' under these circumstances. Before using this
property, check that the mouse's target is not `nil`.

**Surface Randomizer**

The code in this sample, when placed in a `LocalScript` inside
`StarterPlayerScripts` will set the surface of any `BasePart` clicked on to a
random surface.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local surfaceTypes = {
	Enum.SurfaceType.Smooth,
	Enum.SurfaceType.Glue,
	Enum.SurfaceType.Weld,
	Enum.SurfaceType.Studs,
	Enum.SurfaceType.Inlet,
	Enum.SurfaceType.Universal,
	Enum.SurfaceType.Hinge,
	Enum.SurfaceType.Motor,
}

local function onMouseClick()
	-- make sure the mouse is pointing at a part
	local target = mouse.Target
	if not target then
		return
	end

	local surfaceType = surfaceTypes[math.random(1, #surfaceTypes)]

	local surface = mouse.TargetSurface
	local propertyName = surface.Name .. "Surface"

	mouse.Target[propertyName] = surfaceType
end

mouse.Button1Down:Connect(onMouseClick)
```

**Target Surface**

Demonstrates [Mouse.TargetSurface](/docs/reference/engine/classes/Mouse.md).

```lua
local Players = game:GetService("Players")
local player = Players.LocalPlayer
local mouse = player:GetMouse()
-- Check that there exists a part at which the mouse is pointing
if mouse.Target then
	print("The mouse is pointing to the " .. mouse.TargetSurface.Name .. " side of " .. mouse.Target.Name)
else
	print("The mouse is not pointing at anything.")
end
```

### Property: Mouse.UnitRay

```json
{
  "type": "Ray",
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

The UnitRay property is a [Ray](/docs/reference/engine/datatypes/Ray.md) directed toward the mouse's
position in 3D space (described by [Mouse.Hit](/docs/reference/engine/classes/Mouse.md)). It originates from
the [CFrame](/docs/reference/engine/classes/Camera.md) of the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md).
Like all unit rays, it has a distance of 1.

**Unit Ray**

Demonstrates [Mouse.UnitRay](/docs/reference/engine/classes/Mouse.md).

```lua
local Players = game:GetService("Players")
local player = Players.LocalPlayer
local mouse = player:GetMouse()
print(mouse.UnitRay.Direction.Magnitude) -- Always 1
```

### Property: Mouse.ViewSizeX

```json
{
  "type": "int",
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

The ViewSizeX property describes the horizontal component of the game
window's size in pixels.

**Normalized Mouse Position**

This code sample shows how you can create a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing
the `Mouse` object's position on screen ([X()](/docs/reference/engine/classes/Mouse.md) and
[Y()](/docs/reference/engine/classes/Mouse.md)) and the size of the screen itself
([ViewSizeX()](/docs/reference/engine/classes/Mouse.md) and [ViewSizeY()](/docs/reference/engine/classes/Mouse.md)).
Using these, you can normalize the position of the mouse on-screen such that
the top-left just under the topbar maps to (0, 0) and the bottom-right maps to
(1, 1). This normalized position is calculated and printed as the mouse moves
using the [Move()](/docs/reference/engine/classes/Mouse.md) event.

```lua
local Players = game:GetService("Players")

-- Note: You should use ContextActionService or UserInputService instead of
-- the Mouse object for accomplishing this task.
local player = Players.LocalPlayer
local mouse = player:GetMouse()

local function onMouseMove()
	-- Construct Vector2 objects for the mouse's position and screen size
	local position = Vector2.new(mouse.X, mouse.Y)
	local size = Vector2.new(mouse.ViewSizeX, mouse.ViewSizeY)
	-- A normalized position will map the top left (just under the topbar)
	-- to (0, 0) the bottom right to (1, 1), and the center to (0.5, 0.5).
	-- This is calculated by dividing the position by the total size.
	local normalizedPosition = position / size
	print(normalizedPosition)
end
mouse.Move:Connect(onMouseMove)
```

**Expected output:** When run, moving your mouse will print its normalized position on-screen. Move your mouse toward the top left and you'll notice it gets closer to (0, 0). Move to the bottom right will get closer to (1, 1).

### Property: Mouse.ViewSizeY

```json
{
  "type": "int",
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

The ViewSizeY property describes the vertical component of the game
window's size in pixels. This length includes the space used by the
topbar.

**Normalized Mouse Position**

This code sample shows how you can create a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing
the `Mouse` object's position on screen ([X()](/docs/reference/engine/classes/Mouse.md) and
[Y()](/docs/reference/engine/classes/Mouse.md)) and the size of the screen itself
([ViewSizeX()](/docs/reference/engine/classes/Mouse.md) and [ViewSizeY()](/docs/reference/engine/classes/Mouse.md)).
Using these, you can normalize the position of the mouse on-screen such that
the top-left just under the topbar maps to (0, 0) and the bottom-right maps to
(1, 1). This normalized position is calculated and printed as the mouse moves
using the [Move()](/docs/reference/engine/classes/Mouse.md) event.

```lua
local Players = game:GetService("Players")

-- Note: You should use ContextActionService or UserInputService instead of
-- the Mouse object for accomplishing this task.
local player = Players.LocalPlayer
local mouse = player:GetMouse()

local function onMouseMove()
	-- Construct Vector2 objects for the mouse's position and screen size
	local position = Vector2.new(mouse.X, mouse.Y)
	local size = Vector2.new(mouse.ViewSizeX, mouse.ViewSizeY)
	-- A normalized position will map the top left (just under the topbar)
	-- to (0, 0) the bottom right to (1, 1), and the center to (0.5, 0.5).
	-- This is calculated by dividing the position by the total size.
	local normalizedPosition = position / size
	print(normalizedPosition)
end
mouse.Move:Connect(onMouseMove)
```

**Expected output:** When run, moving your mouse will print its normalized position on-screen. Move your mouse toward the top left and you'll notice it gets closer to (0, 0). Move to the bottom right will get closer to (1, 1).

### Property: Mouse.X

```json
{
  "type": "int",
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

When detecting changes in the mouse's position on-screen, it is
recommended that you use [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) with
[UserInputType.MouseMovement](/docs/reference/engine/enums/UserInputType.md) or
[UserInputService.InputChanged](/docs/reference/engine/classes/UserInputService.md), which both describe the position of
the mouse using the [Position](/docs/reference/engine/classes/InputObject.md) (a
[Vector3](/docs/reference/engine/datatypes/Vector3.md)) of an [InputObject](/docs/reference/engine/classes/InputObject.md), instead of using this and
related properties.

The X property describes the horizontal component of the mouse's position
on the screen. The position is measured in pixels relative to the top left
corner, under the topbar. This property can be used in conjunction with
[Mouse.Y](/docs/reference/engine/classes/Mouse.md) to produce a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the mouse's
position:

```lua
local position = Vector2.new(mouse.X, mouse.Y)
```

This property does not fire [Changed](/docs/reference/engine/classes/Object.md) or the signal
returned from
[GetPropertyChangedSignal](/docs/reference/engine/classes/Object.md). Use
the [Mouse.Move](/docs/reference/engine/classes/Mouse.md) event instead.

**Normalized Mouse Position**

This code sample shows how you can create a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing
the `Mouse` object's position on screen ([X()](/docs/reference/engine/classes/Mouse.md) and
[Y()](/docs/reference/engine/classes/Mouse.md)) and the size of the screen itself
([ViewSizeX()](/docs/reference/engine/classes/Mouse.md) and [ViewSizeY()](/docs/reference/engine/classes/Mouse.md)).
Using these, you can normalize the position of the mouse on-screen such that
the top-left just under the topbar maps to (0, 0) and the bottom-right maps to
(1, 1). This normalized position is calculated and printed as the mouse moves
using the [Move()](/docs/reference/engine/classes/Mouse.md) event.

```lua
local Players = game:GetService("Players")

-- Note: You should use ContextActionService or UserInputService instead of
-- the Mouse object for accomplishing this task.
local player = Players.LocalPlayer
local mouse = player:GetMouse()

local function onMouseMove()
	-- Construct Vector2 objects for the mouse's position and screen size
	local position = Vector2.new(mouse.X, mouse.Y)
	local size = Vector2.new(mouse.ViewSizeX, mouse.ViewSizeY)
	-- A normalized position will map the top left (just under the topbar)
	-- to (0, 0) the bottom right to (1, 1), and the center to (0.5, 0.5).
	-- This is calculated by dividing the position by the total size.
	local normalizedPosition = position / size
	print(normalizedPosition)
end
mouse.Move:Connect(onMouseMove)
```

**Expected output:** When run, moving your mouse will print its normalized position on-screen. Move your mouse toward the top left and you'll notice it gets closer to (0, 0). Move to the bottom right will get closer to (1, 1).

### Property: Mouse.Y

```json
{
  "type": "int",
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

When detecting changes in the mouse's position on-screen, it is
recommended that you use [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) with
[UserInputType.MouseMovement](/docs/reference/engine/enums/UserInputType.md) or
[UserInputService.InputChanged](/docs/reference/engine/classes/UserInputService.md), which both describe the position of
the mouse using the [Position](/docs/reference/engine/classes/InputObject.md) (a
[Vector3](/docs/reference/engine/datatypes/Vector3.md)) of an [InputObject](/docs/reference/engine/classes/InputObject.md), instead of using this and
related properties.

The Y property describes the vertical component of the mouse's position on
the screen. The position is measured in pixels relative to the top left
corner, under the topbar. This property can be used in conjunction with
[Mouse.X](/docs/reference/engine/classes/Mouse.md) to produce a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the mouse's
position:

```lua
local position = Vector2.new(mouse.X, mouse.Y)
```

This property does not fire [Changed](/docs/reference/engine/classes/Object.md) or the signal
returned from
[GetPropertyChangedSignal](/docs/reference/engine/classes/Object.md). Use
the [Mouse.Move](/docs/reference/engine/classes/Mouse.md) event instead.

**Normalized Mouse Position**

This code sample shows how you can create a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing
the `Mouse` object's position on screen ([X()](/docs/reference/engine/classes/Mouse.md) and
[Y()](/docs/reference/engine/classes/Mouse.md)) and the size of the screen itself
([ViewSizeX()](/docs/reference/engine/classes/Mouse.md) and [ViewSizeY()](/docs/reference/engine/classes/Mouse.md)).
Using these, you can normalize the position of the mouse on-screen such that
the top-left just under the topbar maps to (0, 0) and the bottom-right maps to
(1, 1). This normalized position is calculated and printed as the mouse moves
using the [Move()](/docs/reference/engine/classes/Mouse.md) event.

```lua
local Players = game:GetService("Players")

-- Note: You should use ContextActionService or UserInputService instead of
-- the Mouse object for accomplishing this task.
local player = Players.LocalPlayer
local mouse = player:GetMouse()

local function onMouseMove()
	-- Construct Vector2 objects for the mouse's position and screen size
	local position = Vector2.new(mouse.X, mouse.Y)
	local size = Vector2.new(mouse.ViewSizeX, mouse.ViewSizeY)
	-- A normalized position will map the top left (just under the topbar)
	-- to (0, 0) the bottom right to (1, 1), and the center to (0.5, 0.5).
	-- This is calculated by dividing the position by the total size.
	local normalizedPosition = position / size
	print(normalizedPosition)
end
mouse.Move:Connect(onMouseMove)
```

**Expected output:** When run, moving your mouse will print its normalized position on-screen. Move your mouse toward the top left and you'll notice it gets closer to (0, 0). Move to the bottom right will get closer to (1, 1).

### Property: Mouse.target

```json
{
  "type": "BasePart",
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

> **Deprecated:** This property is a deprecated variant of [Mouse.Target](/docs/reference/engine/classes/Mouse.md) which should be used instead.

### Property: Mouse.hit *(hidden)*

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

> **Deprecated:** This property is a deprecated variant of [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) which should be used instead.

## Events

### Event: Mouse.Button1Down

**Signature:** `Mouse.Button1Down()`

This event fires when the player presses their left mouse button. Note
that this can be accessed from a [Tool](/docs/reference/engine/classes/Tool.md); for example, when placed in
a [LocalScript](/docs/reference/engine/classes/LocalScript.md), the code below prints `Button1Down` whenever the
left mouse button is pressed.

```lua
local tool = script.Parent  -- Make sure this is a Tool object

tool.Equipped:Connect(function(mouse)
	mouse.Button1Down:Connect(function()
		print("Button1Down")
	end)
end)
```

You can find out the position of the mouse in world space and if it's
pointing at any [BasePart](/docs/reference/engine/classes/BasePart.md) using the [Hit](/docs/reference/engine/classes/Mouse.md) and
[Target](/docs/reference/engine/classes/Mouse.md) properties.

*Security: None · Capabilities: Input*

### Event: Mouse.Button1Up

**Signature:** `Mouse.Button1Up()`

This event fires when the player releases their left mouse button. Note
that this can be accessed from a [Tool](/docs/reference/engine/classes/Tool.md); for example, when placed in
a [LocalScript](/docs/reference/engine/classes/LocalScript.md), the code below prints `Button1Up` whenever the left
mouse button is released.

```lua
local tool = script.Parent  -- Make sure this is a Tool object

tool.Equipped:Connect(function(mouse)
	mouse.Button1Up:Connect(function()
		print("Button1Up")
	end)
end)
```

You can find out the position of the mouse in world space and if it's
pointing at any [BasePart](/docs/reference/engine/classes/BasePart.md) using the [Hit](/docs/reference/engine/classes/Mouse.md) and
[Target](/docs/reference/engine/classes/Mouse.md) properties.

*Security: None · Capabilities: Input*

### Event: Mouse.Button2Down

**Signature:** `Mouse.Button2Down()`

This event fires when the player presses their right mouse button. Note
that this can be accessed from a [Tool](/docs/reference/engine/classes/Tool.md); for example, when placed in
a [LocalScript](/docs/reference/engine/classes/LocalScript.md), the code below prints `Button2Down` whenever the
right mouse button is pressed.

```lua
local tool = script.Parent  -- Make sure this is a Tool object

tool.Equipped:Connect(function(mouse)
	mouse.Button2Down:Connect(function()
		print("Button2Down")
	end)
end)
```

You can find out the position of the mouse in world space and if it's
pointing at any [BasePart](/docs/reference/engine/classes/BasePart.md) using the [Hit](/docs/reference/engine/classes/Mouse.md) and
[Target](/docs/reference/engine/classes/Mouse.md) properties.

*Security: None · Capabilities: Input*

### Event: Mouse.Button2Up

**Signature:** `Mouse.Button2Up()`

This event fires when the player releases their right mouse button. Note
that this can be accessed from a [Tool](/docs/reference/engine/classes/Tool.md); for example, when placed in
a [LocalScript](/docs/reference/engine/classes/LocalScript.md), the code below prints `Button2Up` whenever the
right mouse button is released.

```lua
local tool = script.Parent  -- Make sure this is a Tool object

tool.Equipped:Connect(function(mouse)
	mouse.Button2Up:Connect(function()
		print("Button2Up")
	end)
end)
```

You can find out the position of the mouse in world space and if it's
pointing at any [BasePart](/docs/reference/engine/classes/BasePart.md) using the [Hit](/docs/reference/engine/classes/Mouse.md) and
[Target](/docs/reference/engine/classes/Mouse.md) properties.

*Security: None · Capabilities: Input*

### Event: Mouse.Idle

**Signature:** `Mouse.Idle()`

Fired during every heartbeat that the mouse isn't being passed to another
mouse event.

Note, this event should not be used to determine when the mouse is still.
As it fires every heartbeat it will fire between [Mouse.Move](/docs/reference/engine/classes/Mouse.md)
events.

For information on how to obtain the [Mouse](/docs/reference/engine/classes/Mouse.md) object, please see the
[Mouse](/docs/reference/engine/classes/Mouse.md) page.

Developers can find out the position of the mouse in world-space, and if
it is pointing at any [BasePart](/docs/reference/engine/classes/BasePart.md) using the [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) and
[Mouse.Target](/docs/reference/engine/classes/Mouse.md) properties.

Note, developers are recommended to use [UserInputService](/docs/reference/engine/classes/UserInputService.md) instead
of the [Mouse](/docs/reference/engine/classes/Mouse.md) object in new work.

*Security: None · Capabilities: Input*

**Mouse.Idle**

This example demonstrates how mouse events are passed during each frame

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local events = {
	"Button1Down",
	"Button1Up",
	"Button2Down",
	"Button2Up",
	"Idle",
	"Move",
	"WheelBackward",
	"WheelForward",
	"KeyDown",
	"KeyUp",
}

local currentEvent
local frame = 0

local function processInput()
	frame = frame + 1
	print("Frame", frame, "- mouse event was passed to", currentEvent)
end

for _, event in pairs(events) do
	mouse[event]:Connect(function()
		currentEvent = event
	end)
end

RunService:BindToRenderStep("ProcessInput", Enum.RenderPriority.Input.Value, processInput)
```

### Event: Mouse.Move

**Signature:** `Mouse.Move()`

Fired when the mouse is moved.

Note, this event is fired when the mouse's position is updated, therefore
it will fire repeatedly while being moved.

For information on how to obtain the [Mouse](/docs/reference/engine/classes/Mouse.md) object, please see the
[Mouse](/docs/reference/engine/classes/Mouse.md) page.

Developers can find out the position of the mouse in world-space, and if
it is pointing at any [BasePart](/docs/reference/engine/classes/BasePart.md) using the [Mouse.Hit](/docs/reference/engine/classes/Mouse.md) and
[Mouse.Target](/docs/reference/engine/classes/Mouse.md) properties.

```
mouse.Move:Connect(function()
	local position = mouse.Hit.p
	local target = mouse.Target
	print(target, position)
end)
```

Note, developers are recommended to use [UserInputService](/docs/reference/engine/classes/UserInputService.md) instead
of the [Mouse](/docs/reference/engine/classes/Mouse.md) object in new work.

*Security: None · Capabilities: Input*

**Move Parts with the Mouse**

The example below allows the [local player](/docs/reference/engine/classes/Players.md) to move
parts with their mouse.

When the player presses their left mouse button over a part, that part is the
[mouse's target](/docs/reference/engine/classes/Mouse.md) and becomes the _point_. Until the player
releases their left mouse button, that part will move to the mouse's world
position when the player moves their mouse.

Note that the [Mouse.TargetFilter](/docs/reference/engine/classes/Mouse.md) property allows the code to ignore
the part being moved when determining the mouse's world position.

The code should work as expected when placed in a `LocalScript`.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local point
local down

local function selectPart()
	if mouse.Target and not mouse.Target.Locked then
		point = mouse.Target
		mouse.TargetFilter = point
		down = true
	end
end

local function movePart()
	if down and point then
		local posX, posY, posZ = mouse.Hit.X, mouse.Hit.Y, mouse.Hit.Z
		point.Position = Vector3.new(posX, posY, posZ)
	end
end

local function deselectPart()
	down = false
	point = nil
	mouse.TargetFilter = nil
end

mouse.Button1Down:Connect(selectPart)
mouse.Button1Up:Connect(deselectPart)
mouse.Move:Connect(movePart)
```

### Event: Mouse.WheelBackward

**Signature:** `Mouse.WheelBackward()`

The WheelBackward event fires when the mouse wheel is scrolled backwards.
Possible uses for this event include toggling a gun's scope in a first
person shooter (FPS) or zooming the player's camera.

This can be used alongside the scrolling forward event,
[Mouse.WheelForward](/docs/reference/engine/classes/Mouse.md).

For information on how to obtain the [Mouse](/docs/reference/engine/classes/Mouse.md) object, please see the
[Mouse](/docs/reference/engine/classes/Mouse.md) page.

Note, developers are recommended to use [UserInputService](/docs/reference/engine/classes/UserInputService.md) instead
of the [Mouse](/docs/reference/engine/classes/Mouse.md) object in new work.

*Security: None · Capabilities: Input*

**Mouse.WheelBackward**

The below example assumes that you have already got the player's mouse (and
set it as a variable named 'mouse'), whether by use of a [Tool](/docs/reference/engine/classes/Tool.md),
[HopperBin](/docs/reference/engine/classes/HopperBin.md) or the [Player:GetMouse()](/docs/reference/engine/classes/Player.md) method. It will print
"Wheel went backwards!" when the player scrolls backwards.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local function onWheelBackward()
	print("Wheel went backwards!")
end

mouse.WheelBackward:Connect(onWheelBackward)
```

### Event: Mouse.WheelForward

**Signature:** `Mouse.WheelForward()`

The WheelForward event fires when the mouse wheel is scrolled forwards.
Possible uses for this event include toggling a gun's scope in a first
person shooter (FPS) or zooming the player's camera.

This can be used alongside the scrolling backward event,
[Mouse.WheelBackward](/docs/reference/engine/classes/Mouse.md).

For information on how to obtain the [Mouse](/docs/reference/engine/classes/Mouse.md) object, please see the
[Mouse](/docs/reference/engine/classes/Mouse.md) page.

Note, developers are recommended to use [UserInputService](/docs/reference/engine/classes/UserInputService.md) instead
of the [Mouse](/docs/reference/engine/classes/Mouse.md) object in new work.

*Security: None · Capabilities: Input*

**Mouse.WheelForward**

The below example assumes that you have already got the player's mouse (and
set it as a variable named 'mouse'), whether by use of a `Tool`, `HopperBin`
or the [Player:GetMouse()](/docs/reference/engine/classes/Player.md) method. It will print "Wheel went forward!"
when the player scrolls forwards.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local function onWheelForward()
	print("Wheel went forward!")
end

mouse.WheelForward:Connect(onWheelForward)
```

### Event: Mouse.KeyDown

**Signature:** `Mouse.KeyDown(key: string)`

> **Deprecated:** Mouse events have been superseded by [UserInputService](/docs/reference/engine/classes/UserInputService.md) which should be used in all new work.

This event fires when a Key is pressed, with the passed argument being the
key that was pressed.

Note:

- Not all keys generate this event. However, you can get around this with
  a few of the keys, "/" for example, by using the [Mouse.KeyUp](/docs/reference/engine/classes/Mouse.md)
  event.
- Some keys generate the same string as other keys.
- It's possible for the string to be empty (possibly due to "\0" key
  code).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `key` | `string` |  |

**Mouse.KeyDown**

The below example, assuming that 'mouse' was defined, would print the key that
was pressed (e.g. "q") along with the ascii value for that key (e.g. 113).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local function onKeyDown(key)
	print("Key:", key, "Code:", string.byte(key))
end

mouse.KeyDown:Connect(onKeyDown)
```

### Event: Mouse.keyDown

**Signature:** `Mouse.keyDown(key: string)`

> **Deprecated:** This event is a deprecated variant of [Mouse.KeyDown](/docs/reference/engine/classes/Mouse.md) which has also been deprecated. Neither event should be used in new work.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `key` | `string` |  |

### Event: Mouse.KeyUp

**Signature:** `Mouse.KeyUp(key: string)`

> **Deprecated:** Mouse events have been superseded by [UserInputService](/docs/reference/engine/classes/UserInputService.md) which should be used in all new work.

This event is fired when a Key is released, with the passed argument being
the key that was released.

Note:

- Not all keys generate this event. However, you can get around this with
  a few of the keys, "/" for example, by using the
  [[API:Class/Mouse/KeyUp|KeyUp]] event.
- Some keys generate the same string as other keys.
- It's possible for the string to be empty (possibly due to "\0" key
  code).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `key` | `string` |  |

**Mouse KeyUp**

The below example, assuming that 'mouse' was defined, would print the key that
was released (e.g. "q") along with the ascii value for that key (e.g. 113).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local function onKeyUp(key)
	print("Key:", key, "Code:", string.byte(key))
end

mouse.KeyUp:Connect(onKeyUp)
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