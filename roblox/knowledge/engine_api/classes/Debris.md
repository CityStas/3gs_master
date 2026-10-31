---
name: Debris
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Allows scheduling the guaranteed destruction of an object without yielding."
---

# Class: Debris

> Allows scheduling the guaranteed destruction of an object without yielding.

## Description

The **Debris** service allows scheduling guaranteed destruction of an object
without yielding.

#### Advantages

Besides creating a bit of a mess, objects that are no longer required can use
up system memory and cause an experience to run slower over time. For this
reason, it's always advised to call [Instance:Destroy()](/docs/reference/engine/classes/Instance.md) on objects you
no longer need. In some cases, however, an object may have a specific period
of utility before it can be destroyed.

Consider a wall being smashed into individual bricks. If you want a brick to
linger for 3 seconds before being destroyed, you can use the following code:

```lua
task.wait(3)
brick:Destroy()
```

However, waiting causes the thread to yield which may be undesired. To avoid
yielding, a callback function can be scheduled to run on a new thread after 3
seconds:

```lua
task.delay(3, function()
	brick:Destroy()
end)
```

Or in one line:

```lua
task.delay(3, brick.Destroy, brick)
```

While this now avoids yielding, it has a potential drawback in that the
scheduled callback will never run if the script is disabled or destroyed
before the callback runs.

This is where [Debris](/docs/reference/engine/classes/Debris.md) has a specific advantage, as it does not yield
the current thread and runs outside the context of the script, guaranteeing
the instance is eventually destroyed even if the script is disabled or
destroyed. The following code does not yield and guarantees the instance will
be destroyed:

```lua
Debris:AddItem(brick, 3)
```

Note that [Debris](/docs/reference/engine/classes/Debris.md) has a hardcoded maximum of 1,000 objects, so if more
than 1,000 items are added, the oldest debris will be destroyed instantly to
make room for new debris.

## Code Samples

**Debris AddItem**

Creates parts on a loop and parents them to the Workspace, then uses
Debris.AddItem to clean them up.

```lua
local Debris = game:GetService("Debris")

local ball = Instance.new("Part")
ball.Anchored = false
ball.Shape = Enum.PartType.Ball
ball.TopSurface = Enum.SurfaceType.Smooth
ball.BottomSurface = Enum.SurfaceType.Smooth
ball.Size = Vector3.new(1, 1, 1)

local RNG = Random.new()
local MAX_VELOCITY = 10

while true do
	local newBall = ball:Clone()
	newBall.BrickColor = BrickColor.random()
	newBall.CFrame = CFrame.new(0, 30, 0)
	newBall.Velocity =
		Vector3.new(RNG:NextNumber(-MAX_VELOCITY, MAX_VELOCITY), 0, RNG:NextNumber(-MAX_VELOCITY, MAX_VELOCITY))
	newBall.Parent = game.Workspace
	Debris:AddItem(newBall, 2)
	task.wait(0.1)
end
```

## Properties

### Property: Debris.MaxItems

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is deprecated and should not be used in new work.

The maximum number of items that can be assigned to the Debris service at
one time.

If this number is exceeded, objects are automatically destroyed in order
from oldest to newest until the amount is less than or equal to MaxItems.

This property is currently restricted and will error if set. The value is
hardcoded to 1,000 items.

## Methods

### Method: Debris:AddItem

**Signature:** `Debris:AddItem(item: Instance, lifetime?: double): ()`

Schedules a given [Instance](/docs/reference/engine/classes/Instance.md) for destruction within the specified
lifetime. After the `lifetime` argument has elapsed, the object is
destroyed in the same manner as [Instance:Destroy()](/docs/reference/engine/classes/Instance.md). Note that the
`lifetime` argument is optional and defaults to 10 seconds.

Note that [Debris](/docs/reference/engine/classes/Debris.md) has a hardcoded maximum of 1,000 objects, so if
more than 1,000 items are added, the oldest debris will be destroyed
instantly to make room for new debris. This means you should treat the
`lifetime` parameter as a **maximum** lifetime, not an exact lifetime.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `item` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) to add to [Debris](/docs/reference/engine/classes/Debris.md). |
| `lifetime` | `double` | `10` | Number of seconds before the [Instance](/docs/reference/engine/classes/Instance.md) should be destroyed. |

**Returns:** `()`

**Debris AddItem**

Creates parts on a loop and parents them to the Workspace, then uses
Debris.AddItem to clean them up.

```lua
local Debris = game:GetService("Debris")

local ball = Instance.new("Part")
ball.Anchored = false
ball.Shape = Enum.PartType.Ball
ball.TopSurface = Enum.SurfaceType.Smooth
ball.BottomSurface = Enum.SurfaceType.Smooth
ball.Size = Vector3.new(1, 1, 1)

local RNG = Random.new()
local MAX_VELOCITY = 10

while true do
	local newBall = ball:Clone()
	newBall.BrickColor = BrickColor.random()
	newBall.CFrame = CFrame.new(0, 30, 0)
	newBall.Velocity =
		Vector3.new(RNG:NextNumber(-MAX_VELOCITY, MAX_VELOCITY), 0, RNG:NextNumber(-MAX_VELOCITY, MAX_VELOCITY))
	newBall.Parent = game.Workspace
	Debris:AddItem(newBall, 2)
	task.wait(0.1)
end
```

### Method: Debris:addItem

**Signature:** `Debris:addItem(item: Instance, lifetime?: double): ()`

> **Deprecated:** This function is a deprecated variant of [Debris:AddItem()](/docs/reference/engine/classes/Debris.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `item` | `Instance` |  |  |
| `lifetime` | `double` | `10` |  |

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