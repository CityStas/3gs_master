---
name: Attachment
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Defines a point and orientation relative to an ancestor PVInstance, Bone, or another Attachment."
---

# Class: Attachment

> Defines a point and orientation relative to an ancestor [PVInstance](/docs/reference/engine/classes/PVInstance.md),
> [Bone](/docs/reference/engine/classes/Bone.md), or another [Attachment](/docs/reference/engine/classes/Attachment.md).

## Description

An `Attachment` defines a point and orientation relative to an ancestor
[PVInstance](/docs/reference/engine/classes/PVInstance.md), [Bone](/docs/reference/engine/classes/Bone.md), or another `Attachment`. The offset is
stored in the [CFrame](/docs/reference/engine/classes/Attachment.md) property. The offset can also
be set through other properties, such as
[WorldCFrame](/docs/reference/engine/classes/Attachment.md).

If no ancestral [PVInstance](/docs/reference/engine/classes/PVInstance.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) exists, then
[CFrame](/docs/reference/engine/classes/Attachment.md) and
[WorldCFrame](/docs/reference/engine/classes/Attachment.md) are the same.

Attachments are used by several kinds of [Constraints](/docs/reference/engine/classes/Constraint.md) and
are also valid alternatives to [BasePart](/docs/reference/engine/classes/BasePart.md) as a parent for objects such
as:

- [ParticleEmitters](/docs/reference/engine/classes/ParticleEmitter.md) which will emit particles from the
  attachment's specific position/orientation instead of the [BasePart](/docs/reference/engine/classes/BasePart.md)
  bounds.

- Light-emitting objects like [PointLight](/docs/reference/engine/classes/PointLight.md) and [SpotLight](/docs/reference/engine/classes/SpotLight.md) which
  will shine from the attachment's position/orientation instead of the
  [BasePart](/docs/reference/engine/classes/BasePart.md) center.

- [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) which will use the attachment's position as the audio's
  point of emission.

## Properties

### Property: Attachment.Axis

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Derived Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Direction of the **X** axis of the attachment, represented as a unit
[Vector3](/docs/reference/engine/datatypes/Vector3.md). Together with
[SecondaryAxis](/docs/reference/engine/classes/Attachment.md), this property defines the
orientation of the attachment. Setting `Axis` automatically re-projects
`SecondaryAxis` onto the plane perpendicular to the new axis so the two
always remain orthogonal.

The default value is `(1, 0, 0)`.

### Property: Attachment.CFrame

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
  "category": "Transform",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The [CFrame](/docs/reference/engine/datatypes/CFrame.md) offset of the attachment. Changes to this property
will reflect onto the [Position](/docs/reference/engine/classes/Attachment.md) and
[Rotation](/docs/reference/engine/classes/Attachment.md) properties of this object. Similarly,
a change to either of those properties will reflect onto this property.

### Property: Attachment.SecondaryAxis

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Derived Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Direction of the **Y** axis of the attachment, represented as a unit
[Vector3](/docs/reference/engine/datatypes/Vector3.md). Together with [Axis](/docs/reference/engine/classes/Attachment.md), this
property defines the orientation of the attachment. When set, the value is
projected onto the plane perpendicular to `Axis` so the two axes always
remain orthogonal; the resulting stored value may therefore differ from
the value you assign.

The default value is `(0, 1, 0)`.

### Property: Attachment.Visible

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
    "Basic"
  ]
}
```

Toggles the in-experience visibility of the attachment. When set to
`true`, the attachment renders as a small green sphere at its world
position during gameplay. This is useful for debugging constraint setups
or verifying attachment placement without needing Studio's constraint
detail overlays.

The default value is `false`.

### Property: Attachment.WorldAxis

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Derived World Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Direction of the **X** axis of the attachment relative to the world,
represented as a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a length of 1. This is the
world-space equivalent of [Axis](/docs/reference/engine/classes/Attachment.md), computed by
transforming the local axis through the parent's [CFrame](/docs/reference/engine/datatypes/CFrame.md).
Setting this property converts the supplied direction into the parent's
local space and updates `Axis` accordingly.

### Property: Attachment.WorldCFrame

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
  "thread_safety": "ReadSafe",
  "category": "Derived World Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The exact [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the attachment in world space coordinates,
independent of its parent. The value of this property is equivalent to
multiplying the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the attachment's parent by its own
[CFrame](/docs/reference/engine/datatypes/CFrame.md).

### Property: Attachment.WorldSecondaryAxis

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Derived World Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Direction of the **Y** axis of the attachment relative to the world,
represented as a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) with a length of 1. This is the
world-space equivalent of [SecondaryAxis](/docs/reference/engine/classes/Attachment.md),
computed by transforming the local secondary axis through the parent's
[CFrame](/docs/reference/engine/datatypes/CFrame.md). Setting this property converts the supplied direction
into the parent's local space and updates `SecondaryAxis` accordingly.

### Property: Attachment.Orientation *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Orientation of the attachment relative to the orientation of its parent.
Rotations are in **Z**,&nbsp;**X**,&nbsp;**Y** order.

### Property: Attachment.Position *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Positional offset of the attachment, relative to the position and
orientation of its parent. This value corresponds to the translational
component of [CFrame](/docs/reference/engine/classes/Attachment.md); changing either property
updates the other. The offset is expressed in the local coordinate space
of the parent [BasePart](/docs/reference/engine/classes/BasePart.md), [Bone](/docs/reference/engine/classes/Bone.md), or [Attachment](/docs/reference/engine/classes/Attachment.md).

The default value is `(0, 0, 0)`.

### Property: Attachment.Rotation *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Transform",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

> **Deprecated:** This property is deprecated and should not be used in new work. See [Orientation](/docs/reference/engine/classes/Attachment.md) instead.

Rotation of the attachment relative to the rotation of its parent.
Rotations are in **Z**,&nbsp;**Y**,&nbsp;**X** order.

### Property: Attachment.WorldOrientation *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Derived World Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Orientation of the attachment relative to the world rather than its own
parent. Rotations are in **Z**,&nbsp;**X**,&nbsp;**Y** order.

### Property: Attachment.WorldPosition *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Derived World Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Position of the attachment relative to the world rather than its own
parent. This is the world-space equivalent of
[Position](/docs/reference/engine/classes/Attachment.md), computed by transforming the local
offset through the parent's [CFrame](/docs/reference/engine/datatypes/CFrame.md). Setting this property
converts the supplied position into the parent's local space and updates
`Position` accordingly.

### Property: Attachment.WorldRotation *(hidden)*

```json
{
  "type": "Vector3",
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
  "category": "Derived World Data",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

> **Deprecated:** This item has been superseded by [WorldOrientation](/docs/reference/engine/classes/Attachment.md) which should be used in new work.

Rotation of the attachment relative to the world rather than its own
parent.

## Methods

### Method: Attachment:GetConstraints

**Signature:** `Attachment:GetConstraints(): List<Constraint>`

Returns a list of [Constraints](/docs/reference/engine/classes/Constraint.md) that use this attachment
as either [Attachment0](/docs/reference/engine/classes/Constraint.md) or
[Attachment1](/docs/reference/engine/classes/Constraint.md). The returned array is a
snapshot at the time of the call; subsequent changes to constraint
connections are not reflected in a previously returned array.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `List<Constraint>` — An array of [Constraint](/docs/reference/engine/classes/Constraint.md) objects that are connected to this
attachment.

### Method: Attachment:GetAxis

**Signature:** `Attachment:GetAxis(): Vector3`

> **Deprecated:** This method is deprecated and should not be used in new work.

Returns the value of the attachment's [Axis](/docs/reference/engine/classes/Attachment.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Vector3` — The direction of the X axis as a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) in the
attachment's local space.

### Method: Attachment:GetSecondaryAxis

**Signature:** `Attachment:GetSecondaryAxis(): Vector3`

> **Deprecated:** This method is deprecated and should not be used in new work.

Returns the value of the attachment's
[SecondaryAxis](/docs/reference/engine/classes/Attachment.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Vector3` — The direction of the Y axis as a unit [Vector3](/docs/reference/engine/datatypes/Vector3.md) in the
attachment's local space.

### Method: Attachment:SetAxis

**Signature:** `Attachment:SetAxis(axis: Vector3): ()`

> **Deprecated:** This method is deprecated and should not be used in new work.

Sets the value of the attachment's [Axis](/docs/reference/engine/classes/Attachment.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `axis` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to set as the X-axis direction of the attachment. |

**Returns:** `()`

### Method: Attachment:SetSecondaryAxis

**Signature:** `Attachment:SetSecondaryAxis(axis: Vector3): ()`

> **Deprecated:** This method is deprecated and should not be used in new work.

Sets the value of the attachment's
[SecondaryAxis](/docs/reference/engine/classes/Attachment.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `axis` | `Vector3` |  | The [Vector3](/docs/reference/engine/datatypes/Vector3.md) to set as the Y-axis direction of the attachment. |

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