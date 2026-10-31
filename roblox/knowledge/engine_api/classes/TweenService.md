---
name: TweenService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Used to create Tweens which interpolate, or tween, the properties of instances."
---

# Class: TweenService

> Used to create [Tweens](/docs/reference/engine/classes/Tween.md) which interpolate, or tween, the
> properties of instances.

## Description

[TweenService](/docs/reference/engine/classes/TweenService.md) is used to create [Tweens](/docs/reference/engine/classes/Tween.md) which interpolate,
or tween, the properties of instances. [Tweens](/docs/reference/engine/classes/Tween.md) can be used on any
object with compatible property types, including:

- [number](/docs/en-us/luau/numbers.md)
- [boolean](/docs/en-us/luau/booleans.md)
- [CFrame](/docs/reference/engine/datatypes/CFrame.md)
- [Rect](/docs/reference/engine/datatypes/Rect.md)
- [Color3](/docs/reference/engine/datatypes/Color3.md)
- [UDim](/docs/reference/engine/datatypes/UDim.md)
- [UDim2](/docs/reference/engine/datatypes/UDim2.md)
- [Vector2](/docs/reference/engine/datatypes/Vector2.md)
- [Vector2int16](/docs/reference/engine/datatypes/Vector2int16.md)
- [Vector3](/docs/reference/engine/datatypes/Vector3.md)
- [EnumItem](/docs/reference/engine/datatypes/EnumItem.md)

[TweenService:Create()](/docs/reference/engine/classes/TweenService.md), the primary constructor function, takes
[TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) specifications about the tween and generates the
[Tween](/docs/reference/engine/classes/Tween.md) object which can then be used to play the tween.

Note that [Tweens](/docs/reference/engine/classes/Tween.md) can interpolate multiple properties at the same
time, but they must not be interpolating the same property. If two tweens
attempt to modify the same property, the initial tween will be cancelled and
overwritten by the most recent tween.

## Code Samples

**Tween Creation**

In this example a Tween is created to animate the position and color of a
Part. Because the position and color are part of the same tween, they will
change at the exact same rate and will reach their goal at the same time.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Color = Color3.new(1, 0, 0)
part.Anchored = true
part.Parent = game.Workspace

local goal = {}
goal.Position = Vector3.new(10, 10, 0)
goal.Color = Color3.new(0, 1, 0)

local tweenInfo = TweenInfo.new(5)

local tween = TweenService:Create(part, tweenInfo, goal)

tween:Play()
```

**Looping a Tween**

This code sample includes an example of how a looped tween can be created. A
part is instanced in the [Workspace](/docs/reference/engine/classes/Workspace.md) and a [Tween](/docs/reference/engine/classes/Tween.md) is created
using [TweenService:Create()](/docs/reference/engine/classes/TweenService.md) that is set to animate its position along
the **Y** axis.

The looped effect is achieved by modifying the [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) used in
[TweenService:Create()](/docs/reference/engine/classes/TweenService.md). Specifically, when `RepeatCount` is set to less
than `0`, the tween will play indefinitely. Also, setting `Reverses` to `true`
will cause the tween to play in reverse once it has reached its destination.
In combination this creates a looped effect.

The correct way to make a tween play indefinitely is to set `RepeatCount` to
`-1`. You should avoid using large numbers or [math.huge](/docs/reference/engine/globals/math.md) as a
substitute as this is unstable and may stop working at any point.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.Parent = workspace

local tweenInfo = TweenInfo.new(
	2, -- Time
	Enum.EasingStyle.Linear, -- EasingStyle
	Enum.EasingDirection.Out, -- EasingDirection
	-1, -- RepeatCount (when less than zero the tween will loop indefinitely)
	true, -- Reverses (tween will reverse once reaching its goal)
	0 -- DelayTime
)

local tween = TweenService:Create(part, tweenInfo, { Position = Vector3.new(0, 30, 0) })

tween:Play()
task.wait(10)
tween:Cancel() -- cancel the animation after 10 seconds
```

**Pausing a Tween**

This sample demonstrates how the playback of a tween can be paused and
resumed.

A part is instanced in the Workspace and a tween is setup that will move it 50
studs along the X axis. However during playback the tween is briefly paused,
then resumed. To further illustrate this the BrickColor of the part changes
from red to green while it is paused.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.BrickColor = BrickColor.new("Bright green")
part.Parent = workspace

local goal = {}
goal.Position = Vector3.new(50, 10, 0)

local tweenInfo = TweenInfo.new(10, Enum.EasingStyle.Linear)

local tween = TweenService:Create(part, tweenInfo, goal)

tween:Play()

task.wait(3)
part.BrickColor = BrickColor.new("Bright red")
tween:Pause()

task.wait(2)
part.BrickColor = BrickColor.new("Bright green")
tween:Play()
```

## Methods

### Method: TweenService:Create

**Signature:** `TweenService:Create(instance: Instance, tweenInfo: TweenInfo, propertyTable: Dictionary): Tween`

This constructor creates a new [Tween](/docs/reference/engine/classes/Tween.md) from three arguments: the
object to tween, the [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) specifications, and a table
containing the properties to tween and values to tween to.

The `propertyTable` parameter needs to be a dictionary where the keys are
the string names of the property (for example `Position`, `Transparency`,
or `Color`), and the values are the property targets at the end of the
tween.

The [Tween](/docs/reference/engine/classes/Tween.md) created using this function is unique to the object
given as the `instance` parameter. To apply the same tween to another
object, call this function again with the new object.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) whose properties are to be tweened. |
| `tweenInfo` | `TweenInfo` |  | The [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) to be used. |
| `propertyTable` | `Dictionary` |  | A dictionary of properties, and their target values, to be tweened. |

**Returns:** `Tween` — The newly created [Tween](/docs/reference/engine/classes/Tween.md) configured to interpolate the given
properties toward their target values. Call [TweenBase:Play()](/docs/reference/engine/classes/TweenBase.md)
on the returned object to start the tween.

**Tween Creation**

In this example a Tween is created to animate the position and color of a
Part. Because the position and color are part of the same tween, they will
change at the exact same rate and will reach their goal at the same time.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Color = Color3.new(1, 0, 0)
part.Anchored = true
part.Parent = game.Workspace

local goal = {}
goal.Position = Vector3.new(10, 10, 0)
goal.Color = Color3.new(0, 1, 0)

local tweenInfo = TweenInfo.new(5)

local tween = TweenService:Create(part, tweenInfo, goal)

tween:Play()
```

**Looping a Tween**

This code sample includes an example of how a looped tween can be created. A
part is instanced in the [Workspace](/docs/reference/engine/classes/Workspace.md) and a [Tween](/docs/reference/engine/classes/Tween.md) is created
using [TweenService:Create()](/docs/reference/engine/classes/TweenService.md) that is set to animate its position along
the **Y** axis.

The looped effect is achieved by modifying the [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) used in
[TweenService:Create()](/docs/reference/engine/classes/TweenService.md). Specifically, when `RepeatCount` is set to less
than `0`, the tween will play indefinitely. Also, setting `Reverses` to `true`
will cause the tween to play in reverse once it has reached its destination.
In combination this creates a looped effect.

The correct way to make a tween play indefinitely is to set `RepeatCount` to
`-1`. You should avoid using large numbers or [math.huge](/docs/reference/engine/globals/math.md) as a
substitute as this is unstable and may stop working at any point.

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Position = Vector3.new(0, 10, 0)
part.Anchored = true
part.Parent = workspace

local tweenInfo = TweenInfo.new(
	2, -- Time
	Enum.EasingStyle.Linear, -- EasingStyle
	Enum.EasingDirection.Out, -- EasingDirection
	-1, -- RepeatCount (when less than zero the tween will loop indefinitely)
	true, -- Reverses (tween will reverse once reaching its goal)
	0 -- DelayTime
)

local tween = TweenService:Create(part, tweenInfo, { Position = Vector3.new(0, 30, 0) })

tween:Play()
task.wait(10)
tween:Cancel() -- cancel the animation after 10 seconds
```

### Method: TweenService:GetValue

**Signature:** `TweenService:GetValue(alpha: float, easingStyle: EasingStyle, easingDirection: EasingDirection): float`

Returns a new alpha value for interpolating using the given alpha value,
[EasingStyle](/docs/reference/engine/enums/EasingStyle.md), and [EasingDirection](/docs/reference/engine/enums/EasingDirection.md). The provided `alpha` value
will be clamped between `0` and `1`. This method raises an error if
`easingStyle` is [EasingStyle.Bezier](/docs/reference/engine/enums/EasingStyle.md) or [EasingStyle.Spring](/docs/reference/engine/enums/EasingStyle.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `alpha` | `float` |  | An interpolation value between `0` and `1`. |
| `easingStyle` | `EasingStyle` |  | The easing style to use. |
| `easingDirection` | `EasingDirection` |  | The easing direction to use. |

**Returns:** `float` — A new alpha value generated from the given easing style and direction.

### Method: TweenService:SmoothDamp

**Signature:** `TweenService:SmoothDamp(current: Variant, target: Variant, velocity: Variant, smoothTime: float, maxSpeed: float?, dt: float?): Tuple`

Smoothly interpolates a value towards a target, simulating a critically
damped spring. Returns a tuple with `(newValue, newVelocity`).
`newVelocity` needs to be fed to the next call of SmoothDamp to ensure
smooth results. Supports [number](/docs/reference/engine/datatypes/number.md), [Vector2](/docs/reference/engine/datatypes/Vector2.md),
[Vector3](/docs/reference/engine/datatypes/Vector3.md), and [CFrame](/docs/reference/engine/datatypes/CFrame.md).

*Security: None · Thread Safety: Safe · Capabilities: Basic · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `current` | `Variant` |  | The current value to smooth. |
| `target` | `Variant` |  | The target value to reach. |
| `velocity` | `Variant` |  | The current velocity with which the current value should approach the target value. You shouldn't modify this value between calls yourself, it's used to store the stateful velocity. In most cases, initialize this with `0`, `Vector2.zero`, `Vector3.zero`, or `CFrame.identity` depending on the type, or if needed, with your initial velocity. |
| `smoothTime` | `float` |  | The duration over which the total smoothing operation should take place. Note that since this is a damped spring, there's no guarantee `current` will be exactly `target` after this time, but it will be close. Smaller values result in quicker smoothing. |
| `maxSpeed` | `float?` |  | The maximum speed at which the current value should approach the target value. Leaving this nil defaults to `math.huge`, meaning the velocity isn't clamped. |
| `dt` | `float?` |  | The rate at which the smoothing operation should be applied. If left nil, the current engine delta time will be used. |

**Returns:** `Tuple` — The new value and new velocity calculated from the smoothing
operation.

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