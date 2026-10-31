---
name: Tween
last_updated: 2026-10-30T19:55:53Z
inherits:
  - TweenBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The Tween object controls the playback of an interpolation."
---

# Class: Tween

> The [Tween](/docs/reference/engine/classes/Tween.md) object controls the playback of an interpolation.

## Description

The [Tween](/docs/reference/engine/classes/Tween.md) object controls the playback of an interpolation. Creating
and configuring a [Tween](/docs/reference/engine/classes/Tween.md) is done with the [TweenService:Create()](/docs/reference/engine/classes/TweenService.md)
function; [Instance.new()](/docs/reference/engine/datatypes/Instance.md) cannot be used for this particular object.

Note that while the configuration of a tween can be accessed after a tween has
been created, it can not be modified. If new goals are needed for an
interpolation, a new [Tween](/docs/reference/engine/classes/Tween.md) must be created.

Also note that multiple tweens can be played on the same object at the same
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

## Properties

### Property: Tween.Instance

```json
{
  "type": "Instance",
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
    "Basic"
  ]
}
```

This property of a [Tween](/docs/reference/engine/classes/Tween.md) (read-only) points to the
[Instance](/docs/reference/engine/classes/Instance.md) whose properties are being interpolated.

**Tween Instance**

This code sample includes a simple function that will return true if the
instance of a tween is a Part.

```lua
local TweenService = game:GetService("TweenService")

local function isInstanceAPart(tween)
	local instance = tween.Instance
	return instance:IsA("BasePart")
end

local tweenInfo = TweenInfo.new()
local instance = Instance.new("Part")

local tween = TweenService:Create(instance, tweenInfo, {
	Transparency = 1,
})

print(isInstanceAPart(tween))
```

### Property: Tween.TweenInfo

```json
{
  "type": "TweenInfo",
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
    "Basic"
  ]
}
```

Read-only property that includes information on how the interpolation of
the [Tween](/docs/reference/engine/classes/Tween.md) is to be carried out, using the [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md)
data type.

**TweenInfo Examples**

An example of the range of different interpolation effects that can be used in
Tweens.

```lua
-- A TweenInfo with all default parameters
TweenInfo.new()

-- A TweenInfo with its time set to 0.5 seconds.
TweenInfo.new(0.5)

-- A TweenInfo with its easing style set to Back.
TweenInfo.new(0.5, Enum.EasingStyle.Back)

-- A TweenInfo with its easing direction set to In.
TweenInfo.new(0.5, Enum.EasingStyle.Back, Enum.EasingDirection.In)

-- A TweenInfo that repeats itself 4 times.
TweenInfo.new(0.5, Enum.EasingStyle.Back, Enum.EasingDirection.In, 4)

-- A TweenInfo that reverses its interpolation after reaching its goal.
TweenInfo.new(0.5, Enum.EasingStyle.Back, Enum.EasingDirection.In, 4, true)

-- A TweenInfo that loops indefinitely.
TweenInfo.new(0.5, Enum.EasingStyle.Back, Enum.EasingDirection.In, -1, true)

-- A TweenInfo with a delay of 1 second between each interpolation.
TweenInfo.new(0.5, Enum.EasingStyle.Back, Enum.EasingDirection.In, 4, true, 1)
```

## Inherited Members

### From [TweenBase](/docs/reference/engine/classes/TweenBase.md)

- **Property `PlaybackState`** (`PlaybackState`): Read-only property that shows the current state for the Tween
- **Method `Cancel(): ()`**: Halts playback and resets the tween variables. If you then call
- **Method `Pause(): ()`**: Halts playback of the tween. Doesn't reset its progress variables, meaning
- **Method `Play(): ()`**: Starts playback of a tween. Note that if playback has already started,
- **Event `Completed`**: Fires when the tween finishes playing or when stopped with

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