---
name: Camera
last_updated: 2026-10-30T19:55:52Z
inherits:
  - PVInstance
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotReplicated
summary: "A class which defines a view of the 3D world."
---

# Class: Camera

> A class which defines a view of the 3D world.

## Description

The `Camera` object defines a view of the 3D world. In a running experience,
each client has its own `Camera` object which resides in that client's local
[Workspace](/docs/reference/engine/classes/Workspace.md), accessible through the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md)
property.

The most important camera properties are:

- [CFrame](/docs/reference/engine/classes/Camera.md) which represents the position and orientation
  of the camera.

- [CameraType](/docs/reference/engine/classes/Camera.md) which is read by the experience's
  camera scripts and determines how the camera should update each frame.

- [CameraSubject](/docs/reference/engine/classes/Camera.md) which is read by the experience's
  camera scripts and determines what object the camera should follow.

- [FieldOfView](/docs/reference/engine/classes/Camera.md) which represents the visible extent
  of the observable world.

- [Focus](/docs/reference/engine/classes/Camera.md) which represents the point the camera is looking
  at. It's important this property is set, as certain visuals will be more
  detailed and will update more frequently depending on how close they are to
  the focus point.

See [Customizing the Camera](/docs/en-us/workspace/camera.md) for more
information on how to adjust and customize the camera's behavior.

#### Storing Multiple Cameras

Note that when changing [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) to a new
[Camera](/docs/reference/engine/classes/Camera.md), all other [Cameras](/docs/reference/engine/classes/Camera.md) directly descending from
[Workspace](/docs/reference/engine/classes/Workspace.md) will be destroyed. If you need to store multiple cameras and
swap between them on demand, it's recommended that you store them in a
[Folder](/docs/reference/engine/classes/Folder.md) or [Model](/docs/reference/engine/classes/Model.md) under [Workspace](/docs/reference/engine/classes/Workspace.md), inside which they
will remain even when [CurrentCamera](/docs/reference/engine/classes/Workspace.md) is
changed.

## Properties

### Property: Camera.CameraSubject

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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

`CameraSubject` accepts a variety of [Instances](/docs/reference/engine/classes/Instance.md). The
default camera scripts respond differently to the available settings:

- By default, the camera scripts follow the local character's
  [Humanoid](/docs/reference/engine/classes/Humanoid.md), factoring in the humanoid's current state and
  [Humanoid.CameraOffset](/docs/reference/engine/classes/Humanoid.md).

- When set to a [BasePart](/docs/reference/engine/classes/BasePart.md), the camera scripts follow its position,
  with a vertical offset in the case of [VehicleSeats](/docs/reference/engine/classes/VehicleSeat.md).

`CameraSubject` cannot be set to `nil`. Attempting to do so will revert it
to its previous value.

To restore `CameraSubject` to its default value, set it to the local
character's [Humanoid](/docs/reference/engine/classes/Humanoid.md):

**Camera Subject**

Demonstrates [Camera.CameraSubject](/docs/reference/engine/classes/Camera.md).

```lua
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer
local camera = workspace.CurrentCamera

local function resetCameraSubject()
	if camera and localPlayer.Character then
		local humanoid = localPlayer.Character:FindFirstChildWhichIsA("Humanoid")
		if humanoid then
			camera.CameraSubject = humanoid
		end
	end
end
```

### Property: Camera.CameraType

```json
{
  "type": "CameraType",
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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

The default Roblox camera scripts have several built-in behaviors. Setting
this property toggles between the various [CameraType](/docs/reference/engine/enums/CameraType.md) behaviors.
Note that some camera types require a valid
[CameraSubject](/docs/reference/engine/classes/Camera.md) to work correctly.

The default camera scripts will not move or update the camera if
`CameraType` is set to [CameraType.Scriptable](/docs/reference/engine/enums/CameraType.md). For more information
on positioning and orienting the camera manually, see
[CFrame](/docs/reference/engine/classes/Camera.md).

For all `CameraType` settings **except** [CameraType.Scriptable](/docs/reference/engine/enums/CameraType.md), the
[CameraSubject](/docs/reference/engine/classes/Camera.md) property represents the object
whose position the camera's [Focus](/docs/reference/engine/classes/Camera.md) is set to.

### Property: Camera.CFrame

```json
{
  "type": "CFrame",
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
    "Basic"
  ],
  "simulationAccess": true
}
```

This property is the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the [Camera](/docs/reference/engine/classes/Camera.md), defining its
position and orientation in the 3D world. Note that some transformations,
such as the rotation of the head when using VR devices, are not reflected
in this property, so you should use
[GetRenderCFrame()](/docs/reference/engine/classes/Camera.md) to obtain the "true"
[CFrame](/docs/reference/engine/datatypes/CFrame.md) of the camera.

You can move the camera by setting this property. However, the default
camera scripts also set it, so you should either:

- Set the camera [CameraType](/docs/reference/engine/classes/Camera.md) to
  [CameraType.Scriptable](/docs/reference/engine/enums/CameraType.md) so that the default camera scripts will not
  update the camera's [CFrame](/docs/reference/engine/datatypes/CFrame.md). This method is simplest and
  recommended in most cases.

- Completely replace the default camera scripts with alternatives. This
  approach is only recommended if you do not need any default camera
  functionality.

The most intuitive way to position and orient the [Camera](/docs/reference/engine/classes/Camera.md) is by
using the [CFrame.lookAt()](/docs/reference/engine/datatypes/CFrame.md) constructor. In the following
example, the [Camera](/docs/reference/engine/classes/Camera.md) is positioned at
[Vector3.new(0, 10, 0)](/docs/reference/engine/datatypes/Vector3.md) and is oriented to be looking towards
[Vector3.new(10, 0, 0)](/docs/reference/engine/datatypes/Vector3.md).

```lua
local camera = workspace.CurrentCamera
camera.CameraType = Enum.CameraType.Scriptable

local pos = Vector3.new(0, 10, 0)
local lookAtPos = Vector3.new(10, 0, 0)

camera.CFrame = CFrame.lookAt(pos, lookAtPos)
```

Although the camera can be placed in the manner demonstrated above, you
may want to animate it to move smoothly from one [CFrame](/docs/reference/engine/datatypes/CFrame.md) to
another. For this, you can either:

- Set the camera's position/orientation every frame with
  [RunService:BindToRenderStep()](/docs/reference/engine/classes/RunService.md) and the [CFrame:Lerp()](/docs/reference/engine/datatypes/CFrame.md)
  method.
- Create and play a [Tween](/docs/reference/engine/classes/Tween.md) that animates the position/orientation
  of the camera:

  ```lua
  local Players = game:GetService("Players")
  local TweenService = game:GetService("TweenService")

  local camera = workspace.CurrentCamera
  camera.CameraType = Enum.CameraType.Scriptable

  local player = Players.LocalPlayer
  local character = player.Character
  if not character or character.Parent == nil then
  	character = player.CharacterAdded:Wait()
  end

  local pos = camera.CFrame * Vector3.new(0, 20, 0)
  local lookAtPos = character.PrimaryPart.Position
  local targetCFrame = CFrame.lookAt(pos, lookAtPos)

  local tween = TweenService:Create(camera, TweenInfo.new(2), {CFrame = targetCFrame})

  tween:Play()
  ```

### Property: Camera.DiagonalFieldOfView

```json
{
  "type": "float",
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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

Sets how many degrees in the diagonal direction (from one corner of the
viewport to its opposite corner) the camera can view. See
[FieldOfView](/docs/reference/engine/classes/Camera.md) for a more general explanation of
field of view.

Note that `DiagonalFieldOfView` represents the field of view that is
visible by the [Camera](/docs/reference/engine/classes/Camera.md) rendering into the fullscreen area which may
be occluded by notches or screen cutouts on some devices. See
[ViewportSize](/docs/reference/engine/classes/Camera.md) for more information.

### Property: Camera.FieldOfView

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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

The `FieldOfView` (FOV) property sets how many degrees in the vertical
direction the camera can view. This property is clamped between `1` and
`120` degrees and defaults at `70`. Very low or very high fields of view
are not recommended as they can be disorientating to players.

Note that uniform scaling is enforced, meaning the vertical and horizontal
field of view are always related by the aspect ratio of the screen.

Suggested uses for `FieldOfView` include:

- Reducing FOV to give the impression of magnification, for example when
  using binoculars.
- Increasing FOV when the player is "sprinting" to give the impression of
  a lack of control.

Note that `FieldOfView` represents the field of view that is visible by
the [Camera](/docs/reference/engine/classes/Camera.md) rendering into the fullscreen area which may be
occluded by notches or screen cutouts on some devices. See
[ViewportSize](/docs/reference/engine/classes/Camera.md) for more information.

### Property: Camera.FieldOfViewMode

```json
{
  "type": "FieldOfViewMode",
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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

The camera's [FieldOfView](/docs/reference/engine/classes/Camera.md) (FOV) must be updated
to reflect [ViewportSize](/docs/reference/engine/classes/Camera.md) changes. The value of
`FieldOfViewMode` determines which FOV value will be kept constant.

For example, when this property is set to [FieldOfViewMode.Vertical](/docs/reference/engine/enums/FieldOfViewMode.md),
the horizontal FOV is updated when the viewport is resized, but the
vertical FOV is kept constant. If this property is set to
[FieldOfViewMode.Diagonal](/docs/reference/engine/enums/FieldOfViewMode.md), both horizontal and vertical FOV might be
changed to keep the diagonal FOV constant.

### Property: Camera.Focus

```json
{
  "type": "CFrame",
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
    "Basic"
  ],
  "simulationAccess": true
}
```

Certain graphical operations the engine performs, such as updating
lighting, can take time or computational effort to complete. The camera's
`Focus` property tells the engine which area in 3D space to prioritize
when performing such operations. For example, dynamic lighting from
objects such as [PointLights](/docs/reference/engine/classes/PointLight.md) may not render at distances
far from the focus.

The default Roblox camera scripts automatically set `Focus` to follow the
[CameraSubject](/docs/reference/engine/classes/Camera.md) (usually a [Humanoid](/docs/reference/engine/classes/Humanoid.md)).
However, `Focus` will **not** automatically update when
[CameraType](/docs/reference/engine/classes/Camera.md) is set to
[CameraType.Scriptable](/docs/reference/engine/enums/CameraType.md) or when the default camera scripts are not
being used. In these cases, you should update `Focus` every frame, using
[RunService:BindToRenderStep()](/docs/reference/engine/classes/RunService.md) method at the
[RenderPriority.Camera](/docs/reference/engine/enums/RenderPriority.md) priority.

`Focus` has no bearing on the position or orientation of the camera; see
[CFrame](/docs/reference/engine/classes/Camera.md) for this.

### Property: Camera.HeadLocked

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
    "Basic"
  ]
}
```

Toggles whether the camera will automatically track the head motion of a
player using a VR device. When `true` (default), the engine combines
[CFrame](/docs/reference/engine/classes/Camera.md) with the [UserCFrame](/docs/reference/engine/enums/UserCFrame.md) of the user's head
to render the player's view with head tracking factored in. The view will
be rendered at the following [CFrame](/docs/reference/engine/datatypes/CFrame.md):

```lua
local UserInputService = game:GetService("UserInputService")

local camera = workspace.CurrentCamera

local headCFrame = UserInputService:GetUserCFrame(Enum.UserCFrame.Head)
headCFrame = headCFrame.Rotation + headCFrame.Position * camera.HeadScale

-- This will be equivalent to Camera:GetRenderCFrame()
local renderCFrame = camera.CFrame * headCFrame
```

It is recommended to **not** disable this property for the following
reasons:

- Players may experience motion sickness if an equivalent head tracking
  solution is not added.
- The Roblox Engine performs latency optimizations when `HeadLocked` is
  true.

##### See Also

- [VRService:GetUserCFrame()](/docs/reference/engine/classes/VRService.md) which can be used to obtain the
  [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the head.
- [VRService:RecenterUserHeadCFrame()](/docs/reference/engine/classes/VRService.md) which is used to recenter the
  head to the current position and orientation of the VR device.
- The [GetRenderCFrame()](/docs/reference/engine/classes/Camera.md) method which
  returns the [CFrame](/docs/reference/engine/classes/Camera.md) combined with the
  [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the user's head.

### Property: Camera.HeadScale

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
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

`HeadScale` is the scale of the user's perspective of the world when using
VR.

The size of 1 stud in VR is `0.3 meters / HeadScale`, meaning that larger
`HeadScale` values equate to the world looking smaller from the user's
perspective when using VR devices. For example, a part that's 1 stud tall
appears to be 0.6 meters tall to a VR player with a `HeadScale` of `0.5`.

This property is automatically controlled by
[VRService.AutomaticScaling](/docs/reference/engine/classes/VRService.md) to align the player's perspective with
the size of their avatar. If you intend to control `HeadScale` yourself or
use custom characters, toggle [VRService.AutomaticScaling](/docs/reference/engine/classes/VRService.md) to
[VRScaling.Off](/docs/reference/engine/enums/VRScaling.md).

This property should not be confused with [Humanoid.HeadScale](/docs/reference/engine/classes/Humanoid.md) which
is a [NumberValue](/docs/reference/engine/classes/NumberValue.md) parented to a [Humanoid](/docs/reference/engine/classes/Humanoid.md) to control its
scaling.

### Property: Camera.MaxAxisFieldOfView

```json
{
  "type": "float",
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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

The `MaxAxisFieldOfView` property sets how many degrees along the longest
viewport axis the camera can view.

When the longest axis is the vertical axis, this property will behave
similar to the [FieldOfView](/docs/reference/engine/classes/Camera.md) property. This is
generally the case when a device is in a portrait orientation. In a
landscape orientation, the longest axis will be the horizontal axis; in
this case, the property describes the horizontal field of view of the
[Camera](/docs/reference/engine/classes/Camera.md).

### Property: Camera.NearPlaneZ

```json
{
  "type": "float",
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
    "Basic"
  ]
}
```

The `NearPlaneZ` property describes how far away the camera's near
clipping plane is, in studs. The near clipping plane is a geometric plane
that sits in front of the camera's [CFrame](/docs/reference/engine/classes/Camera.md). Anything
between this plane and the camera will not render, creating a cutaway view
when viewing objects at very short distances. The value of `NearPlaneZ`
varies across different platforms and is currently always between `-0.1`
and `-0.5`.

![Diagram showing how the NearPlaneZ clips (does not render) 3D content between the plane and the camera.](/assets/engine-api/classes/Camera/NearPlaneZ.jpg)

### Property: Camera.OrthographicMode

```json
{
  "type": "OrthographicMode",
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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

Specifies which aspect of [ViewportSize](/docs/reference/engine/classes/Camera.md) is
controlled by [OrthographicSize](/docs/reference/engine/classes/Camera.md).

For example, when this property is set to
[OrthographicMode.Vertical](/docs/reference/engine/enums/OrthographicMode.md), the orthographic projection is scaled
such that the vertical dimension spans exactly
[OrthographicSize](/docs/reference/engine/classes/Camera.md) studs, and the horizontal
dimension spans however many studs are needed to match.

### Property: Camera.OrthographicSize

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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

[OrthographicMode](/docs/reference/engine/classes/Camera.md) chooses the dimension of
the viewport you want to control.
[OrthographicSize](/docs/reference/engine/classes/Camera.md) sets the extent in studs
spanned by that viewport dimension.

For example, if [OrthographicMode](/docs/reference/engine/classes/Camera.md) is set to
[OrthographicMode.MaxAxis](/docs/reference/engine/enums/OrthographicMode.md), then the larger dimension of the viewport
will span [OrthographicSize](/docs/reference/engine/classes/Camera.md) studs.

### Property: Camera.ProjectionType

```json
{
  "type": "ProjectionType",
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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

Set to [ProjectionType.Perspective](/docs/reference/engine/enums/ProjectionType.md) (default) to use a perspective
camera, where parallel lines in 3D converge on the screen and objects get
smaller in the distance. Set to [ProjectionType.Orthographic](/docs/reference/engine/enums/ProjectionType.md) to use
an orthographic camera, where parallel lines stay parallel and objects are
the same size at any distance. This is useful for things like 2D games,
isometric games, and minimaps.

### Property: Camera.ViewportSize

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

`ViewportSize` returns the dimensions of the device safe area on the
current screen. This area is a rectangle which includes the Roblox top bar
area but does not include any device notches or screen cutouts. The units
of `ViewportSize` are Roblox UI offset units which may be different from
native display pixels.

![Mobile device screen with cutout showing device safe area.](../../../assets/engine-api/classes/Camera/DeviceSafeAreaVsFullscreen.png)

As noted above, `ViewportSize` is not equal to the fullscreen area size on
displays with cutouts or notches. To obtain the fullscreen area size on
all displays, you can query the
[AbsoluteSize](/docs/reference/engine/classes/ScreenGui.md) property of a
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) with [ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) set to
[None](/docs/reference/engine/enums/ScreenInsets.md). See [ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md) for a more
information about how screen areas are defined.

Finally, note that `ViewportSize` is not the actual viewport size the
camera uses for rendering (the camera renders in the fullscreen area).
Also, the [FieldOfView](/docs/reference/engine/classes/Camera.md) and
[DiagonalFieldOfView](/docs/reference/engine/classes/Camera.md) properties are
based on the fullscreen area, not `ViewportSize`.

##### Camera Updates

Only the [Camera](/docs/reference/engine/classes/Camera.md) currently referred to by
[Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) has its `ViewportSize` updated each frame
during the [PreRender](/docs/reference/engine/classes/RunService.md) step. The `ViewportSize`
of all other cameras in your experience won't be updated, including those
used for [ViewportFrames](/docs/reference/engine/classes/ViewportFrame.md).

### Property: Camera.ViewStretch

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
  "category": "Camera",
  "capabilities": [
    "Basic"
  ]
}
```

The field of view and the orthographic size are specified for one axis of
the viewport, either horizontal or vertical. Normally, the other axis
automatically adjusts itself to keep pixels square. This lets you stretch
the other axis so that pixels are not square, by a ratio of up to 2:1.
This can be animated to make the view feel not quite right, such as when
stunned.

This works for both orthographic and perspective cameras.

### Property: Camera.VRTiltAndRollEnabled

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
    "Basic"
  ]
}
```

This property toggles whether to apply tilt and roll from the
[CFrame](/docs/reference/engine/classes/Camera.md) property while the player is using a VR
device.

To prevent motion sickness, the horizon should remain level. Tilting and
rolling the player's view while using a VR device can cause a disconnect
between the player's physical space and the virtual space they are
viewing. Changing the apparent downwards direction can cause players to
lose balance or experience dizziness.

For these reasons, it is generally advisable to leave this property
disabled, unless you have extensively tested your experience for these
effects. Even with tilt and roll enabled, you may want to ensure the
player always has a stable reference frame, such as the interior of a
vehicle or a floor that can help the player ground themselves in their
physical space.

### Property: Camera.focus

```json
{
  "type": "CFrame",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is a deprecated variant of [Focus](/docs/reference/engine/classes/Camera.md) which should be used instead.

### Property: Camera.CoordinateFrame *(hidden)*

```json
{
  "type": "CFrame",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

> **Deprecated:** This item has been superseded by [Camera.CFrame](/docs/reference/engine/classes/Camera.md) which should be used in all new work.

The old version of the [CFrame](/docs/reference/engine/classes/Camera.md) property which
functions identically to it.

This item should be used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) in order to work as
expected online.

## Methods

### Method: Camera:GetPartsObscuringTarget

**Signature:** `Camera:GetPartsObscuringTarget(castPoints: Array, ignoreList: Instances): Instances`

This method returns an array of [BaseParts](/docs/reference/engine/classes/BasePart.md) that are
obscuring the lines of sight between the camera's
[CFrame](/docs/reference/engine/classes/Camera.md) and [Vector3](/docs/reference/engine/datatypes/Vector3.md) positions in the
`castPoints` array. Any [Instances](/docs/reference/engine/classes/Instance.md) included in the
`ignoreList` array will be ignored, along with their descendants.

The `castPoints` parameter is given as an array of [Vector3](/docs/reference/engine/datatypes/Vector3.md)
positions. Note that the array of [BaseParts](/docs/reference/engine/classes/BasePart.md) returned is
in an arbitrary order, and no additional raycast data is provided. If you
need data such as hit position, hit material, or surface normal, you
should opt for the [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) method.

```lua
local camera = workspace.CurrentCamera

local castPoints = {
	Vector3.new(0, 10, 0),
	Vector3.new(0, 15, 0)
}
local ignoreList = {}

local partsObscuringTarget = camera:GetPartsObscuringTarget(castPoints, ignoreList)
```

If [Terrain](/docs/reference/engine/classes/Terrain.md) obscures a cast point, [BaseParts](/docs/reference/engine/classes/BasePart.md)
obscuring the cast point between the obscuring [Terrain](/docs/reference/engine/classes/Terrain.md) and the
cast point will not be returned.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `castPoints` | `Array` |  | An array of [Vector3](/docs/reference/engine/datatypes/Vector3.md) positions of cast points. |
| `ignoreList` | `Instances` |  | An array of [Instances](/docs/reference/engine/classes/Instance.md) that should be ignored, along with their descendants. |

**Returns:** `Instances` — An array of [BaseParts](/docs/reference/engine/classes/BasePart.md) that obscure the lines of sight
between the camera's [CFrame](/docs/reference/engine/classes/Camera.md) and the
`castPoints`.

### Method: Camera:GetRenderCFrame

**Signature:** `Camera:GetRenderCFrame(): CFrame`

This method returns the actual [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the [Camera](/docs/reference/engine/classes/Camera.md) as
it is rendered, including the impact of VR (VR head transformations are
not applied to the [CFrame](/docs/reference/engine/classes/Camera.md) property, so it is best
practice to use [GetRenderCFrame()](/docs/reference/engine/classes/Camera.md) to
obtain the "true" [CFrame](/docs/reference/engine/datatypes/CFrame.md) of a player's view).

For example, when using VR, the [Camera](/docs/reference/engine/classes/Camera.md) is actually rendered at the
following [CFrame](/docs/reference/engine/datatypes/CFrame.md):

```lua
local UserInputService = game:GetService("UserInputService")

local camera = workspace.CurrentCamera

local headCFrame = UserInputService:GetUserCFrame(Enum.UserCFrame.Head)
headCFrame = headCFrame.Rotation + headCFrame.Position * camera.HeadScale
renderCFrame = camera.CFrame * headCFrame
```

The camera's render [CFrame](/docs/reference/engine/datatypes/CFrame.md) will only be changed to account for
the head when the [HeadLocked](/docs/reference/engine/classes/Camera.md) property is true.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `CFrame` — The [CFrame](/docs/reference/engine/datatypes/CFrame.md) the [Camera](/docs/reference/engine/classes/Camera.md) is being rendered at.

### Method: Camera:GetRoll

**Signature:** `Camera:GetRoll(): float`

This method returns, in radians, the current roll applied to the
[Camera](/docs/reference/engine/classes/Camera.md) using [SetRoll()](/docs/reference/engine/classes/Camera.md). Roll is defined
as rotation around the camera's Z-axis.

This method only returns roll applied using the
[SetRoll()](/docs/reference/engine/classes/Camera.md) method. Roll manually applied to the
camera's [CFrame](/docs/reference/engine/classes/Camera.md) is not accounted for. To obtain the
actual roll of the [Camera](/docs/reference/engine/classes/Camera.md), including roll manually applied, you
can use the following snippet:

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `float` — The current roll applied by [SetRoll()](/docs/reference/engine/classes/Camera.md), in
radians.

**Camera:GetRoll**

This example, when used in a [LocalScript](/docs/reference/engine/classes/LocalScript.md), will retrieve the current
roll of the camera in degrees. Then, if the camera roll angle is not 20
degrees, the camera roll angle is set to 20 degrees.

```lua
local currentRoll = math.deg(workspace.CurrentCamera:GetRoll()) -- Gets the current roll of the camera in degrees.

if currentRoll ~= 20 then
	workspace.CurrentCamera:SetRoll(math.rad(20)) -- If the camera isn't at 20 degrees roll, the roll is set to 20 degrees.
end
```

**Get Roll**

Demonstrates [Camera:GetRoll()](/docs/reference/engine/classes/Camera.md).

```lua
local function getActualRoll()
	local camera = workspace.CurrentCamera

	local trueUp = Vector3.new(0, 1, 0)
	local cameraUp = camera:GetRenderCFrame().upVector

	return math.acos(trueUp:Dot(cameraUp))
end
```

### Method: Camera:ScreenPointToRay

**Signature:** `Camera:ScreenPointToRay(x: float, y: float, depth?: float): Ray`

This method creates a unit [Ray](/docs/reference/engine/datatypes/Ray.md) from a 2D position on the screen
(defined in pixels), accounting for the GUI inset. The [Ray](/docs/reference/engine/datatypes/Ray.md)
originates from the [Vector3](/docs/reference/engine/datatypes/Vector3.md) equivalent of the 2D position in
the world at the given depth (in studs) away from the [Camera](/docs/reference/engine/classes/Camera.md).

As this method acknowledges the GUI inset, the offset applied to GUI
elements (such as from the top bar) is accounted for. This means the
screen position specified will start in the top left corner below the top
bar. For an otherwise identical method that does not account for the GUI
offset, use [ViewportPointToRay()](/docs/reference/engine/classes/Camera.md).

As the [Ray](/docs/reference/engine/datatypes/Ray.md) created is a unit ray, it is only one stud long. To
create a longer ray, you can do the following:

```lua
local camera = workspace.CurrentCamera
local length = 500
local unitRay = camera:ScreenPointToRay(100, 100)
local extendedRay = Ray.new(unitRay.Origin, unitRay.Direction * length)
```

This method only works for the current [Workspace](/docs/reference/engine/classes/Workspace.md) camera. Other
cameras, such as those you create for a [ViewportFrame](/docs/reference/engine/classes/ViewportFrame.md), have an
initial viewport size of <Typography noWrap>`(1, 1)`</Typography> and are
only updated after you set them to [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md). The
mismatch in viewport size causes the camera to return a ray with an
incorrect [Ray.Direction](/docs/reference/engine/datatypes/Ray.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `float` |  | The position on the **X** axis, in pixels, of the screen point at which to originate the [Ray](/docs/reference/engine/datatypes/Ray.md). This position accounts for the GUI inset. |
| `y` | `float` |  | The position on the **Y** axis, in pixels, of the screen point at which to originate the [Ray](/docs/reference/engine/datatypes/Ray.md). This position accounts for the GUI inset. |
| `depth` | `float` | `0` | The depth from the [Camera](/docs/reference/engine/classes/Camera.md), in studs, from which to offset the origin of the [Ray](/docs/reference/engine/datatypes/Ray.md). |

**Returns:** `Ray` — A unit [Ray](/docs/reference/engine/datatypes/Ray.md), originating from the equivalent
[Vector3](/docs/reference/engine/datatypes/Vector3.md) world position of the given screen coordinates at
the given depth away from the [Camera](/docs/reference/engine/classes/Camera.md). This ray is orientated
in the direction of the [Camera](/docs/reference/engine/classes/Camera.md).

### Method: Camera:SetRoll

**Signature:** `Camera:SetRoll(rollAngle: float): ()`

This method is outdated and no longer considered best practice.

This method sets the current roll, in radians, of the [Camera](/docs/reference/engine/classes/Camera.md). The
roll is applied after the [CFrame](/docs/reference/engine/classes/Camera.md) and represents the
rotation around the camera's Z-axis.

For example, the following would invert the [Camera](/docs/reference/engine/classes/Camera.md):

```lua
workspace.CurrentCamera:SetRoll(math.pi) -- math.pi radians = 180 degrees
```

SetRoll has no effect on any roll applied using the
[CFrame](/docs/reference/engine/classes/Camera.md) property. Roll applied using SetRoll is not
reflected in the [CFrame](/docs/reference/engine/classes/Camera.md) property but is reflected in
the [CFrame](/docs/reference/engine/datatypes/CFrame.md) returned
by[GetRenderCFrame()](/docs/reference/engine/classes/Camera.md).

This method can only be used when the [CameraType](/docs/reference/engine/classes/Camera.md)
is set to `Scriptable`, regardless of whether the default camera scripts
are being used. If it is used with any other
[CameraType](/docs/reference/engine/classes/Camera.md) a warning is given in the output.

Any roll applied using this method will be lost when the
[CameraType](/docs/reference/engine/classes/Camera.md) is changed from `Scriptable`.

To obtain the roll set using this method use
[GetRoll()](/docs/reference/engine/classes/Camera.md).

As this method is outdated, you are advised to instead apply roll to the
[Camera](/docs/reference/engine/classes/Camera.md) using the [CFrame](/docs/reference/engine/classes/Camera.md) property. For
example:

```lua
local currentCFrame = workspace.CurrentCamera.CFrame
local rollCFrame = CFrame.Angles(0, 0, roll)
workspace.CurrentCamera.CFrame = currentCFrame * rollCFrame
```

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rollAngle` | `float` |  | The roll angle, in radians, to be applied to the [Camera](/docs/reference/engine/classes/Camera.md). |

**Returns:** `()`

### Method: Camera:ViewportPointToRay

**Signature:** `Camera:ViewportPointToRay(x: float, y: float, depth?: float): Ray`

This method creates a unit [Ray](/docs/reference/engine/datatypes/Ray.md) from a 2D position in device
safe viewport coordinates, defined in pixels. The ray originates from the
[Vector3](/docs/reference/engine/datatypes/Vector3.md) equivalent of the 2D position in the world at the given
depth (in studs) away from the [Camera](/docs/reference/engine/classes/Camera.md).

As illustrated below, `(0, 0)` corresponds to the top‑left point of the
Roblox top bar. This means that the input 2D position does **not** account
for the [CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md) inset, but it does account
for any [DeviceSafeInsets](/docs/reference/engine/enums/ScreenInsets.md).

![Diagram showing the origin of the device safe area viewport coordinate system.](../../../assets/engine-api/classes/Camera/ViewportPointToRayOrigin.png)

Note that UI instances use a different coordinate system
([GuiObject.AbsolutePosition](/docs/reference/engine/classes/GuiObject.md) uses the
[CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md) viewport coordinate system while this
method uses the [DeviceSafeInsets](/docs/reference/engine/enums/ScreenInsets.md) viewport coordinate
system). If you would like to specify position in core UI coordinates,
please use [ScreenPointToRay()](/docs/reference/engine/classes/Camera.md).

Also note that this method only works for the
[Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) camera. Other cameras, such as those you
create for a [ViewportFrame](/docs/reference/engine/classes/ViewportFrame.md), have an initial viewport size of
`(1, 1)` and are only updated after you set them to
[CurrentCamera](/docs/reference/engine/classes/Workspace.md). The mismatch in viewport
size causes the camera to return a ray with an incorrect
[Ray.Direction](/docs/reference/engine/datatypes/Ray.md).

This method can be used in conjunction with the
[ViewportSize](/docs/reference/engine/classes/Camera.md) property to create a ray from the
centre of the screen, for example:

```lua
local camera = workspace.CurrentCamera

local viewportPoint = camera.ViewportSize / 2
local unitRay = camera:ViewportPointToRay(viewportPoint.X, viewportPoint.Y, 0)
```

As the [Ray](/docs/reference/engine/datatypes/Ray.md) created is a unit ray, it is only one stud long. To
create a longer ray, you can do the following:

```lua
local camera = workspace.CurrentCamera

local length = 500
local viewportPoint = camera.ViewportSize / 2
local unitRay = camera:ViewportPointToRay(viewportPoint.X, viewportPoint.Y, 0)
local extendedRay = Ray.new(unitRay.Origin, unitRay.Direction * length)
```

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `float` |  | The position on the **X** axis, in pixels, of the viewport point at which to originate the [Ray](/docs/reference/engine/datatypes/Ray.md), in device safe area coordinates. |
| `y` | `float` |  | The position on the **Y** axis, in pixels, of the viewport point at which to originate the [Ray](/docs/reference/engine/datatypes/Ray.md), in device safe area coordinates. |
| `depth` | `float` | `0` | The depth from the [Camera](/docs/reference/engine/classes/Camera.md), in studs, from which to offset the origin of the [Ray](/docs/reference/engine/datatypes/Ray.md). |

**Returns:** `Ray` — A unit [Ray](/docs/reference/engine/datatypes/Ray.md), originating from the equivalent
[Vector3](/docs/reference/engine/datatypes/Vector3.md) world position of the given viewport coordinates at
the given depth away from the [Camera](/docs/reference/engine/classes/Camera.md). This ray is orientated
in the direction of the [Camera](/docs/reference/engine/classes/Camera.md).

### Method: Camera:WorldToScreenPoint

**Signature:** `Camera:WorldToScreenPoint(worldPoint: Vector3): Tuple`

This method returns the screen location and depth of a [Vector3](/docs/reference/engine/datatypes/Vector3.md)
`worldPoint` and whether this point is within the bounds of the screen.

This method takes in account the current GUI inset, such as the space
occupied by the top bar, meaning that the 2D position returned is in the
same term as GUI positions and can be used to place GUI elements. For an
otherwise identical method that ignores the GUI inset, see
[WorldToViewportPoint()](/docs/reference/engine/classes/Camera.md).

```lua
local camera = workspace.CurrentCamera

local worldPoint = Vector3.new(0, 10, 0)
local vector, onScreen = camera:WorldToScreenPoint(worldPoint)

local screenPoint = Vector2.new(vector.X, vector.Y)
local depth = vector.Z
```

Note this method does not perform any raycasting and the boolean
indicating whether `worldPoint` is within the bounds of the screen will be
`true` regardless of whether the point is obscured by
[BaseParts](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `worldPoint` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) world position. |

**Returns:** `Tuple` — A tuple containing, in order:

- A [Vector3](/docs/reference/engine/datatypes/Vector3.md) whose **X** and **Y** components represent the
  offset of the `worldPoint` from the top left corner of the screen,
  in pixels. The [Vector3](/docs/reference/engine/datatypes/Vector3.md) **Z** component represents the
  depth of the `worldPoint` from the screen (in studs).

- A boolean indicating if the `worldPoint` is within the bounds of the
  screen.

### Method: Camera:WorldToViewportPoint

**Signature:** `Camera:WorldToViewportPoint(worldPoint: Vector3): Tuple`

This method returns the screen location and depth of a [Vector3](/docs/reference/engine/datatypes/Vector3.md)
`worldPoint` and whether this point is within the bounds of the screen.

This method does not take in account the current GUI inset, such as the
space occupied by the top bar, meaning that the 2D position returned is
taken from the top left corner of the viewport. Unless you are using
[ScreenGui.IgnoreGuiInset](/docs/reference/engine/classes/ScreenGui.md), this position is not appropriate for
placing GUI elements.

For an otherwise identical method that accounts for the GUI inset, see
[WorldToScreenPoint()](/docs/reference/engine/classes/Camera.md).

```lua
local camera = workspace.CurrentCamera

local worldPoint = Vector3.new(0, 10, 0)
local vector, onScreen = camera:WorldToViewportPoint(worldPoint)

local viewportPoint = Vector2.new(vector.X, vector.Y)
local depth = vector.Z
```

Note this method does not perform any raycasting and the boolean
indicating whether `worldPoint` is within the bounds of the screen will be
`true` regardless of whether the point is obscured by
[BaseParts](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md).

##### ViewportFrame Cameras

Only [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md) has its internal viewport dimensions
updated by the engine each frame. Cameras used inside a
[ViewportFrame](/docs/reference/engine/classes/ViewportFrame.md) do not receive viewport updates, so the X and Y
components returned by this method will be in the range [0, 1] rather than
in pixels. In practice, this means the returned values can be used as
scale coordinates (for example,
[UDim2.fromScale(vector.X, vector.Y)](/docs/reference/engine/datatypes/UDim2.md)) to position GUI
elements relative to the ViewportFrame.

*Security: None · Thread Safety: Safe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `worldPoint` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) world position. |

**Returns:** `Tuple` — A tuple containing, in order:

- A [Vector3](/docs/reference/engine/datatypes/Vector3.md) whose **X** and **Y** components represent the
  offset of the `worldPoint` from the top left corner of the viewport,
  in pixels for [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md). For cameras inside a
  [ViewportFrame](/docs/reference/engine/classes/ViewportFrame.md), the values are normalized to [0, 1]. The
  [Vector3](/docs/reference/engine/datatypes/Vector3.md) **Z** component represents the depth of the
  `worldPoint` from the screen (in studs).

- A boolean indicating if the `worldPoint` is within the bounds of the
  screen.

### Method: Camera:ZoomToExtents

**Signature:** `Camera:ZoomToExtents(boundingBoxCFrame: CFrame, boundingBoxSize: Vector3): ()`

This method adjusts the [CFrame](/docs/reference/engine/classes/Camera.md) so that a specified
bounding box is fully visible within the camera's viewport, without
cropping any part of the box.

The bounding box is defined by its center and orientation
(`boundingBoxCFrame`) and its size (`boundingBoxSize`).

This can be used to focus the camera on a 3D object or model, such as when
framing content in a [ViewportFrame](/docs/reference/engine/classes/ViewportFrame.md), taking screenshots, or
smoothly transitioning the camera to highlight specific content.

The method automatically accounts for the camera's field of view and
viewport aspect ratio to ensure the entire bounding box fits.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boundingBoxCFrame` | `CFrame` |  | The [CFrame](/docs/reference/engine/datatypes/CFrame.md) representing the center and orientation of the bounding box to fit into the viewport. |
| `boundingBoxSize` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) size of the bounding box to fit into the viewport. |

**Returns:** `()`

**Zoom To Extents**

Demonstrates [Camera:ZoomToExtents()](/docs/reference/engine/classes/Camera.md).

```lua
local camera = workspace.CurrentCamera
local model = workspace:FindFirstChild("MyModel")

if model then
	local modelCFrame = model:GetModelCFrame()
	local extentsSize = model:GetExtentsSize()
	camera:ZoomToExtents(modelCFrame, extentsSize)
end
```

### Method: Camera:GetLargestCutoffDistance

**Signature:** `Camera:GetLargestCutoffDistance(ignoreList: Instances): float`

> **Deprecated:** This method is deprecated. Do not use it for new work.

This method is used by `PopperCam` in the default camera scripts to ensure
obstructions do not come between the [Camera](/docs/reference/engine/classes/Camera.md) and its subject.

This method will check all [BaseParts](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md)
in the [Workspace](/docs/reference/engine/classes/Workspace.md) with the following exceptions:

- Any [Instance](/docs/reference/engine/classes/Instance.md) specified in the `ignoreList` (including its
  descendants) will be ignored
- [BaseParts](/docs/reference/engine/classes/BasePart.md) with [BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) set to false
  are ignored
- [BaseParts](/docs/reference/engine/classes/BasePart.md) with a [BasePart.Transparency](/docs/reference/engine/classes/BasePart.md) greater
  than 0.95 will be ignored Water [Terrain](/docs/reference/engine/classes/Terrain.md) is ignored

Note, as this method requires an `ignoreList` to run, you should pass an
empty table when none is required.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ignoreList` | `Instances` |  | An array of [Instances](/docs/reference/engine/classes/Instance.md) to ignore. Descendants of these instances will also be ignored. |

**Returns:** `float` — The distance, in studs, that the [Camera](/docs/reference/engine/classes/Camera.md) needs to be pushed
towards its [Focus](/docs/reference/engine/classes/Camera.md) to ensure there are no
obstructions between the [Focus](/docs/reference/engine/classes/Camera.md) and
[CFrame](/docs/reference/engine/classes/Camera.md) of the [Camera](/docs/reference/engine/classes/Camera.md).

### Method: Camera:GetPanSpeed

**Signature:** `Camera:GetPanSpeed(): float`

> **Deprecated:** This method has been deprecated and no longer works. It should not be used in new work.

This method is broken and should not be used.

This method returns the current pan speed of the [Camera](/docs/reference/engine/classes/Camera.md).

The pan speed of the [Camera](/docs/reference/engine/classes/Camera.md) describes the speed at which the
[Camera](/docs/reference/engine/classes/Camera.md) is rotating around its [Focus](/docs/reference/engine/classes/Camera.md) around
the **Y** axis.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `float` — The speed at which the [Camera](/docs/reference/engine/classes/Camera.md) is rotating around its
[Focus](/docs/reference/engine/classes/Camera.md) on the **Y** axis.

### Method: Camera:GetTiltSpeed

**Signature:** `Camera:GetTiltSpeed(): float`

> **Deprecated:** This method has been deprecated and no longer works.

This method is broken and should not be used.

This method returns the current tilt speed of the [Camera](/docs/reference/engine/classes/Camera.md).

The tilt speed of the [Camera](/docs/reference/engine/classes/Camera.md) describes the speed at which the
[Camera](/docs/reference/engine/classes/Camera.md) is rotating around its [Focus](/docs/reference/engine/classes/Camera.md) around
the camera's **X** axis.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `float` — The speed at which the [Camera](/docs/reference/engine/classes/Camera.md) is rotating around its
[Focus](/docs/reference/engine/classes/Camera.md) around the camera's **X** axis.

### Method: Camera:Interpolate

**Signature:** `Camera:Interpolate(endPos: CFrame, endFocus: CFrame, duration: float): ()`

> **Deprecated:** This method has been deprecated. Instead use [TweenService](/docs/reference/engine/classes/TweenService.md) to smoothly animate the [Camera](/docs/reference/engine/classes/Camera.md), see the code snippets below for an example.

This method tweens the [Camera](/docs/reference/engine/classes/Camera.md) in a linear fashion towards a new
[CFrame](/docs/reference/engine/classes/Camera.md) and [Focus](/docs/reference/engine/classes/Camera.md) over a given
duration, for example:

```lua
local camera = workspace.CurrentCamera
camera.CameraType = Enum.CameraType.Scriptable

camera:Interpolate(
	CFrame.new(0, 10, 100),
	CFrame.new(0, 0, 100),
	5
)
```

Throughout the tween, the camera's [CFrame](/docs/reference/engine/classes/Camera.md) will be
orientated towards the camera's [Focus](/docs/reference/engine/classes/Camera.md).

When the tween has completed, the camera's
[InterpolationFinished](/docs/reference/engine/classes/Camera.md) event will
fire.

If this method is called while the [Camera](/docs/reference/engine/classes/Camera.md) is already tweening, the
older tween will be stopped (without firing
[InterpolationFinished](/docs/reference/engine/classes/Camera.md)) and overridden
by the new tween.

Interpolate can only be used if the current
[CameraType](/docs/reference/engine/classes/Camera.md) is `Scriptable`, regardless of
whether the default camera scripts are being used. If it is used with any
other [CameraType](/docs/reference/engine/classes/Camera.md) an error will be thrown.

You are advised to use [TweenService](/docs/reference/engine/classes/TweenService.md) to tween the [Camera](/docs/reference/engine/classes/Camera.md)
instead as it is more reliable and offers a variety of easing styles. See
below for an example:

```lua
local TweenService = game:GetService("TweenService")

local camera = workspace.CurrentCamera
camera.CameraType = Enum.CameraType.Scriptable

local tween = TweenService:Create(
	camera,
	TweenInfo.new(5, Enum.EasingStyle.Quad, Enum.EasingDirection.Out),
	{
		CFrame = CFrame.new(0, 10, 100),
		Focus = CFrame.new(0, 0, 100)
	}
)

tween:Play()
```

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `endPos` | `CFrame` |  | The [CFrame](/docs/reference/engine/datatypes/CFrame.md) for the [Camera](/docs/reference/engine/classes/Camera.md) to tween to. |
| `endFocus` | `CFrame` |  | The [CFrame](/docs/reference/engine/datatypes/CFrame.md) for the camera's [Focus](/docs/reference/engine/classes/Camera.md) to tween to. |
| `duration` | `float` |  | The duration, in seconds, of the tween. |

**Returns:** `()`

### Method: Camera:PanUnits

**Signature:** `Camera:PanUnits(units: int): ()`

> **Deprecated:** This method was used for legacy camera controls and has since been deprecated. Do not use in new work.

This method pans the [Camera](/docs/reference/engine/classes/Camera.md) around the [Focus](/docs/reference/engine/classes/Camera.md)
in 45 degree increments around the **Y** axis.

The rotation is applied to the camera's [CFrame](/docs/reference/engine/classes/Camera.md)
property.

This method pans the [Camera](/docs/reference/engine/classes/Camera.md) in 45 degree increments, for example:

```lua
workspace.CurrentCamera:PanUnits(1) -- 45 degrees
workspace.CurrentCamera:PanUnits(-2) -- -90 degrees
```

PanUnits does not require the [CameraType](/docs/reference/engine/classes/Camera.md) to be
`Scriptable`.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `units` | `int` |  | The number of 45 degree increments by which to pan the [Camera](/docs/reference/engine/classes/Camera.md). |

**Returns:** `()`

### Method: Camera:SetCameraPanMode

**Signature:** `Camera:SetCameraPanMode(mode?: CameraPanMode): ()`

> **Deprecated:** This method has been deprecated and should not be used in new work.

This method sets the [CameraPanMode](/docs/reference/engine/enums/CameraPanMode.md) to be used by the [Camera](/docs/reference/engine/classes/Camera.md)
on mobile devices.

When the \*'EdgeBump' [CameraPanMode](/docs/reference/engine/enums/CameraPanMode.md) is used, swipe to pan is
disabled and the edge bump camera controls are enabled.

SetCameraPan mode has no effect on Windows or Mac users.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `mode` | `CameraPanMode` | `Classic` | The [CameraPanMode](/docs/reference/engine/enums/CameraPanMode.md) to set the [Camera](/docs/reference/engine/classes/Camera.md) to. |

**Returns:** `()`

### Method: Camera:TiltUnits

**Signature:** `Camera:TiltUnits(units: int): boolean`

> **Deprecated:** This method was used for legacy camera controls and has been deprecated. Do not use in new work.

This method tilts the [Camera](/docs/reference/engine/classes/Camera.md) by rotating it around the
[Focus](/docs/reference/engine/classes/Camera.md) around the camera's **X** axis by a given
multiple of 10 degrees.

The rotation is applied to the camera's [CFrame](/docs/reference/engine/classes/Camera.md)
property and is constrained between `-81.05` and `81.05` degrees.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `units` | `int` |  | The number of 10 degree units by which to tilt the [Camera](/docs/reference/engine/classes/Camera.md). |

**Returns:** `boolean` — Whether the [Camera](/docs/reference/engine/classes/Camera.md) tilt applied was constrained.

## Events

### Event: Camera.InterpolationFinished

**Signature:** `Camera.InterpolationFinished()`

This event fires when the [Camera](/docs/reference/engine/classes/Camera.md) has finished interpolating using
the [Camera:Interpolate()](/docs/reference/engine/classes/Camera.md) method. It will not fire if a tween is
interrupted due to [Camera:Interpolate()](/docs/reference/engine/classes/Camera.md) being called again.

You are advised to use [TweenService](/docs/reference/engine/classes/TweenService.md) to animate the [Camera](/docs/reference/engine/classes/Camera.md)
instead, as it is more reliable and provides more options for easing
styles.

*Security: None · Capabilities: Basic*

## Inherited Members

### From [PVInstance](/docs/reference/engine/classes/PVInstance.md)

- **Property `Origin`** (`CFrame`): Editor-only property that reads and sets the world CFrame of
- **Property `Pivot Offset`** (`CFrame`): Editor-only property that displays and edits the pivot's CFrame
- **Method `GetPivot(): CFrame`**: Gets the pivot of a PVInstance.
- **Method `PivotTo(targetCFrame: CFrame): ()`**: Transforms the PVInstance along with all of its descendant

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