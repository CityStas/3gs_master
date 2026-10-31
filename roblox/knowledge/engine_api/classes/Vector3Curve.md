---
name: Vector3Curve
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Represents a 3D vector curve, grouping three FloatCurve instances."
---

# Class: Vector3Curve

> Represents a 3D vector curve, grouping three [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) instances.

## Description

Represents a 3D vector curve, grouping three [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) instances.
Each child [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) can be accessed via the
[Vector3Curve:X()](/docs/reference/engine/classes/Vector3Curve.md), [Vector3Curve:Y()](/docs/reference/engine/classes/Vector3Curve.md), and
[Vector3Curve:Z()](/docs/reference/engine/classes/Vector3Curve.md) methods. The three axes can be sampled simultaneously
via the method [Vector3Curve:GetValueAtTime()](/docs/reference/engine/classes/Vector3Curve.md).

## Code Samples

**Creating a Vector3Curve**

```lua
--- Vector3Curve
local function createVector3Curve()
	local vectorCurve = Instance.new("Vector3Curve")
	local curveX = vectorCurve:X() -- creates and returns a FloatCurve animating the X channel
	local curveY = vectorCurve:Y() -- creates and returns a FloatCurve animating the Y channel
	-- Not setting the Z channel will leave the Z channel not animated.
	-- A missing curve or a curve with no keys don't participate in the animation

	local key = FloatCurveKey.new(0, 1) -- creates a key at time 0 and with value 1
	curveX:InsertKey(key)
	curveY:InsertKey(key)
	local key2 = FloatCurveKey.new(1, 2) -- creates a key at time 1 and with value 2
	curveX:InsertKey(key2)
	curveY:InsertKey(key2)
	return vectorCurve
end

local function testVector3Curve()
	local curve = createVector3Curve()

	-- sampling the curve at a given time (returns a vector3)
	print(curve:GetValueAtTime(0)) -- returns 1, 1, void
	print(curve:GetValueAtTime(0.5)) -- returns 1.5, 1.5, void (result of cubic interpolation with auto tangents)

	curve:X():RemoveKeyAtIndex(1)
	curve:X():RemoveKeyAtIndex(1)
	print(curve:X().Length) -- number of keys = 0
	print(curve:GetValueAtTime(0.5)) -- returns void, 1.5, void
end

testVector3Curve()
```

## Methods

### Method: Vector3Curve:GetValueAtTime

**Signature:** `Vector3Curve:GetValueAtTime(time: float): Array`

Returns the three [FloatCurves](/docs/reference/engine/classes/FloatCurve.md) (X, Y, Z) at the passed
time argument as an array of three numbers. If a channel curve is missing
or no key is found in the curve, the channel is evaluated as `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `float` |  | Time at which to get the value. |

**Returns:** `Array` — The three [FloatCurves](/docs/reference/engine/classes/FloatCurve.md) (X, Y, Z) at the passed time
argument.

### Method: Vector3Curve:X

**Signature:** `Vector3Curve:X(): FloatCurve`

Returns the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the X channel (the first child
instance of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `X`). If none is found, an empty
[FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is created.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `FloatCurve` — The [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the X channel, or a newly created
empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) if none exists yet.

### Method: Vector3Curve:Y

**Signature:** `Vector3Curve:Y(): FloatCurve`

Returns the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the Y channel (the first child
instance of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `Y`). If none is found, an empty
[FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is created.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `FloatCurve` — The [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the Y channel, or a newly created
empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) if none exists yet.

### Method: Vector3Curve:Z

**Signature:** `Vector3Curve:Z(): FloatCurve`

Returns the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the Z channel (the first child
instance of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `Z`). If none is found, an empty
[FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is created.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `FloatCurve` — The [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the Z channel, or a newly created
empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) if none exists yet.

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