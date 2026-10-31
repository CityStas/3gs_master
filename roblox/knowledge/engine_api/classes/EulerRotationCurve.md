---
name: EulerRotationCurve
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Represents a 3D rotation curve through a group of three FloatCurves."
---

# Class: EulerRotationCurve

> Represents a 3D rotation curve through a group of three
> [FloatCurves](/docs/reference/engine/classes/FloatCurve.md).

## Description

A **EulerRotationCurve** represents a 3D rotation curve through a group of
three [FloatCurves](/docs/reference/engine/classes/FloatCurve.md). The rotation is decomposed in three
Euler angles channels that can be accessed via [EulerRotationCurve:X()](/docs/reference/engine/classes/EulerRotationCurve.md),
[EulerRotationCurve:Y()](/docs/reference/engine/classes/EulerRotationCurve.md), and [EulerRotationCurve:Z()](/docs/reference/engine/classes/EulerRotationCurve.md). The three
axes can be sampled simultaneously via
[EulerRotationCurve:GetAnglesAtTime()](/docs/reference/engine/classes/EulerRotationCurve.md), returning the three Euler angles
as a [Vector3](/docs/reference/engine/datatypes/Vector3.md). Similarly,
[EulerRotationCurve:GetRotationAtTime()](/docs/reference/engine/classes/EulerRotationCurve.md) samples all channels
simultaneously but returns a [CFrame](/docs/reference/engine/datatypes/CFrame.md) rotated by `X`, `Y`, and `Z`
according to the specified rotation order.

## Properties

### Property: EulerRotationCurve.RotationOrder

```json
{
  "type": "RotationOrder",
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

Euler angles rotation order

## Methods

### Method: EulerRotationCurve:GetAnglesAtTime

**Signature:** `EulerRotationCurve:GetAnglesAtTime(time: float): Array`

Samples the three [FloatCurves](/docs/reference/engine/classes/FloatCurve.md) (`X`, `Y`, `Z`) at the
passed `time` argument and returns the result as three Euler angles. If a
channel curve is missing or no key is found in the curve, the channel is
evaluated as `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `float` |  | The time, in seconds, at which to sample the three channel curves. |

**Returns:** `Array` — An array of three values holding the sampled `X`, `Y`, and `Z` Euler
angles; any channel whose curve is missing or has no key at `time` is
returned as `nil`.

### Method: EulerRotationCurve:GetRotationAtTime

**Signature:** `EulerRotationCurve:GetRotationAtTime(time: float): CFrame`

Samples the [EulerRotationCurve](/docs/reference/engine/classes/EulerRotationCurve.md) at a given `time` and returns the
corresponding rotation. Empty Euler angles channels are interpreted as
zero.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `float` |  | The time, in seconds, at which to sample the curve. |

**Returns:** `CFrame` — A [CFrame](/docs/reference/engine/datatypes/CFrame.md) whose rotation is composed from the `X`, `Y`, and
`Z` Euler angles sampled at `time`, applied in the order given by
[EulerRotationCurve.RotationOrder](/docs/reference/engine/classes/EulerRotationCurve.md); empty channels are treated
as zero.

### Method: EulerRotationCurve:X

**Signature:** `EulerRotationCurve:X(): FloatCurve`

Returns the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the `X` Euler angle channel. It
is the first child instance of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `X`. If none
is found, an empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is created.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `FloatCurve` — The [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the `X` Euler angle channel.

### Method: EulerRotationCurve:Y

**Signature:** `EulerRotationCurve:Y(): FloatCurve`

Returns the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the `Y` Euler angle channel. It
is the first child instance of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `Y`. If none
is found, an empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is created.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `FloatCurve` — The [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the `Y` Euler angle channel.

### Method: EulerRotationCurve:Z

**Signature:** `EulerRotationCurve:Z(): FloatCurve`

Returns the [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the `Z` Euler angle channel. It
is the first child instance of type [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) named `Z`. If none
is found, an empty [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) is created.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `FloatCurve` — The [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) controlling the `Z` Euler angle channel.

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