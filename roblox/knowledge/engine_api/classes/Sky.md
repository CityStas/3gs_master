---
name: Sky
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Changes the default appearance of the experience's sky."
---

# Class: Sky

> Changes the default appearance of the experience's sky.

## Description

The `Sky` object, when placed inside [Lighting](/docs/reference/engine/classes/Lighting.md), changes the default
appearance of the experience's sky. This object's
[skybox](/docs/en-us/environment/skybox.md) is composed of six sides, like a
cube. Rotation of the skybox can be changed through
[SkyboxOrientation](/docs/reference/engine/classes/Sky.md).

The skybox sun, moon, and other celestial objects remain visible unless you
turn off the [CelestialBodiesShown](/docs/reference/engine/classes/Sky.md) property.
By adjusting the [StarCount](/docs/reference/engine/classes/Sky.md) property, you can change how
many stars appear in the sky at night.

This object can also be used as a cubemap for reflections in
[ViewportFrames](/docs/reference/engine/classes/ViewportFrame.md), in which case only the [Sky](/docs/reference/engine/classes/Sky.md)
object's six‑side `Skybox[…]` properties are used. For details, see
[viewport frames](/docs/en-us/ui/viewport-frames.md).

## Properties

### Property: Sky.CelestialBodiesShown

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

Determines whether the sun, moon, and stars are rendered in the skybox.
Defaults to `true`. When set to `false`, the sun, moon, and stars are
hidden, regardless of the values of other properties.

### Property: Sky.MoonAngularSize

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The perceived angular size of the moon while using this skybox, measured
in degrees.

### Property: Sky.MoonTextureContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed for the moon while using this
skybox. Defaults to `rbxasset://sky/moon.jpg`.

### Property: Sky.MoonTextureId

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the moon while using this skybox. Defaults to
`rbxasset://sky/moon.jpg`.

### Property: Sky.SkyboxBackContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed on the back surface of the skybox.
Defaults to `rbxasset://textures/sky/sky512_bk.tex`.

### Property: Sky.SkyboxBk

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the back surface of the skybox. Defaults to
`rbxasset://textures/sky/sky512_bk.tex`.

### Property: Sky.SkyboxDn

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the bottom surface of the skybox. Defaults to
`rbxasset://textures/sky/sky512_dn.tex`.

### Property: Sky.SkyboxDownContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed on the bottom surface of the
skybox. Defaults to `rbxasset://textures/sky/sky512_dn.tex`.

### Property: Sky.SkyboxFrontContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed on the front surface of the skybox.
Defaults to `rbxasset://textures/sky/sky512_ft.tex`.

### Property: Sky.SkyboxFt

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the front surface of the skybox. Defaults to
`rbxasset://textures/sky/sky512_ft.tex`.

### Property: Sky.SkyboxLeftContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed on the left surface of the skybox.
Defaults to `rbxasset://textures/sky/sky512_lf.tex`.

### Property: Sky.SkyboxLf

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the left surface of the skybox. Defaults to
`rbxasset://textures/sky/sky512_lf.tex`.

### Property: Sky.SkyboxOrientation

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

Changes the orientation of the skybox surfaces. This property takes a
[Vector3](/docs/reference/engine/datatypes/Vector3.md) of degree values in the typical **XYZ** order, but
applies rotation **first** around the **Y** axis. After applying the Y
axis rotation, the orientation is applied to the **X** and **Z** axes to
allow for predictable control over complex movements. Your camera and
object orientation can affect how this rotation appears to be applied.

An easy way to script an orientation animation is to spin around the **Y**
axis (keeping the horizon level), then tilt this axis by setting **X** and
**Z** to a fixed value:

```lua
local Lighting = game:GetService("Lighting")
local RunService = game:GetService("RunService")

local sky = Lighting:FindFirstChild("Sky")

local ROTATION_SPEED = 5  -- In degrees per second

RunService.Heartbeat:Connect(function(deltaTime)
	sky.SkyboxOrientation = Vector3.new(
		30,
		(sky.SkyboxOrientation.Y + ROTATION_SPEED * deltaTime) % 360,
		0
	)
end)
```

See [here](/docs/en-us/environment/skybox.md#orientation) for further info
and limitations.

**Skybox Orientation with Tween**

This script uses [TweenService](/docs/reference/engine/classes/TweenService.md) to create an oscillating tween on the
**X** axis and [RunService](/docs/reference/engine/classes/RunService.md) to apply the tween's motion plus rotation
around the **Y** axis.

```lua
local Lighting = game:GetService("Lighting")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")

local sky = Lighting:FindFirstChild("Sky")

local ROTATION_SPEED = 4 -- In degrees per second
local MAX_TILT = 2 -- In degrees
local TILT_SPEED = 4

local currentTilt = Instance.new("NumberValue")
currentTilt.Value = -MAX_TILT

local tweenGoal = { Value = MAX_TILT }
local tweenInfo = TweenInfo.new(TILT_SPEED, Enum.EasingStyle.Cubic, Enum.EasingDirection.InOut, -1, true)
local tween = TweenService:Create(currentTilt, tweenInfo, tweenGoal)
tween:Play()

RunService.Heartbeat:Connect(function(deltaTime)
	sky.SkyboxOrientation =
		Vector3.new(currentTilt.Value, (sky.SkyboxOrientation.Y + ROTATION_SPEED * deltaTime) % 360, 0)
end)
```

### Property: Sky.SkyboxRightContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed on the right surface of the skybox.
Defaults to `rbxasset://textures/sky/sky512_rt.tex`.

### Property: Sky.SkyboxRt

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the right surface of the skybox. Defaults to
`rbxasset://textures/sky/sky512_rt.tex`.

### Property: Sky.SkyboxUp

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the top surface of the skybox. Defaults to
`rbxasset://textures/sky/sky512_up.tex`.

### Property: Sky.SkyboxUpContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed on the top surface of the skybox.
Defaults to `rbxasset://textures/sky/sky512_up.tex`.

### Property: Sky.StarCount

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

How many stars are shown in the skybox. Only works if
[CelestialBodiesShown](/docs/reference/engine/classes/Sky.md) is `true`.

### Property: Sky.SunAngularSize

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The perceived angular size of the sun while using this skybox, in degrees.
Defaults to `21` and is clamped to the range `[0, 60]`.

### Property: Sky.SunTextureContent

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The [Content](/docs/reference/engine/datatypes/Content.md) image displayed for the sun while using this
skybox. Defaults to `rbxasset://sky/sun.jpg`.

### Property: Sky.SunTextureId

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
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

The texture asset ID for the sun while using this skybox. Defaults to
`rbxasset://sky/sun.jpg`.

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