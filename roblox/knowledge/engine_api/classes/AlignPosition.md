---
name: AlignPosition
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Constraint which applies force to move two attachments together, or to move one attachment to a goal position."
---

# Class: AlignPosition

> Constraint which applies force to move two attachments together, or to move
> one attachment to a goal position.

## Description

The `AlignPosition` constraint applies force to move two attachments together,
or to move one attachment to a goal position. As indicated by the name, it
only affects the **position** of the attachments, not their orientation (to
align attachments by **orientation**, see [AlignOrientation](/docs/reference/engine/classes/AlignOrientation.md)).

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Force Location

By default, force is applied to the parent of
[Attachment0](/docs/reference/engine/classes/Constraint.md) at that attachment's location,
meaning that if the parent's center of mass is not aligned with the direction
of the force, torque will be applied as well as force. Alternatively, force
can be applied to the parents' center of mass by toggling on
[ApplyAtCenterOfMass](/docs/reference/engine/classes/AlignPosition.md).

#### Reactionary Force

By default, the constraint only applies force to
[Attachment0](/docs/reference/engine/classes/Constraint.md) while
[Attachment1](/docs/reference/engine/classes/Constraint.md) remains unaffected. If desired,
force can be applied to both attachments in **equal and opposite directions**
by enabling [ReactionForceEnabled](/docs/reference/engine/classes/AlignPosition.md).

#### Force Limits

You can configure this constraint to apply the maximum force that constraints
allow through the [RigidityEnabled](/docs/reference/engine/classes/AlignPosition.md)
property. When `true`, the physics solver reacts as quickly as possible to
complete the alignment. When `false`, the force applied by the constraint is
limited based on [ForceLimitMode](/docs/reference/engine/classes/AlignPosition.md),
[MaxVelocity](/docs/reference/engine/classes/AlignPosition.md), and
[Responsiveness](/docs/reference/engine/classes/AlignPosition.md). See
[ForceLimitMode](/docs/reference/engine/classes/AlignPosition.md) for further details.

#### Attachment Mode

This constraint can use either **one** or **two** attachments in calculating
its goal. See [Mode](/docs/reference/engine/classes/AlignPosition.md) for details.

## Properties

### Property: AlignPosition.ApplyAtCenterOfMass

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
  "category": "AlignPosition",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

When `false` (default), force is applied to the parent of
[Attachment0](/docs/reference/engine/classes/Constraint.md) at that attachment's location,
meaning that if the parent's center of mass is not aligned with the
direction of the force, torque will be applied as well as force. When
`true`, force is applied at the parents' center of mass.

### Property: AlignPosition.ForceLimitMode

```json
{
  "type": "ForceLimitMode",
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
  "category": "Compliance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Determines how the constraint force will be limited when
[RigidityEnabled](/docs/reference/engine/classes/AlignPosition.md) is `false`. When set
to [Magnitude](/docs/reference/engine/enums/ForceLimitMode.md), the constraint force will be limited
such that the magnitude is less than
[MaxForce](/docs/reference/engine/classes/AlignPosition.md). When set to
[PerAxis](/docs/reference/engine/enums/ForceLimitMode.md), the constraint force along each axis will
be limited by [MaxAxesForce](/docs/reference/engine/classes/AlignPosition.md). The axes
along which the force will be limited are based on the
[ForceRelativeTo](/docs/reference/engine/classes/AlignPosition.md) property.

### Property: AlignPosition.ForceRelativeTo

```json
{
  "type": "ActuatorRelativeTo",
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
  "category": "Compliance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Determines the axes that the constraint uses to limit the force. Only
applies when [RigidityEnabled](/docs/reference/engine/classes/AlignPosition.md) is
`false` and [AlignPosition.ForceLimitMode](/docs/reference/engine/classes/AlignPosition.md) is
[PerAxis](/docs/reference/engine/enums/ForceLimitMode.md). When set to
[World](/docs/reference/engine/enums/ActuatorRelativeTo.md), the constraint force is computed in the
world reference frame and the force limits specified in
[MaxAxesForce](/docs/reference/engine/classes/AlignPosition.md) refer to the axes of the
world coordinate system. When set to [Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md)
or [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md), the force limits specified in
[MaxAxesForce](/docs/reference/engine/classes/AlignPosition.md) refer to the axes of the
specified attachment coordinate system.

### Property: AlignPosition.MaxAxesForce

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
  "category": "Compliance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum force along each axis that the constraint can apply to achieve its
goal. Only used if [RigidityEnabled](/docs/reference/engine/classes/AlignPosition.md)
is `false` and [ForceLimitMode](/docs/reference/engine/classes/AlignPosition.md) is
[PerAxis](/docs/reference/engine/enums/ForceLimitMode.md). The axes used to apply to the limit are
specified using the [ForceRelativeTo](/docs/reference/engine/classes/AlignPosition.md)
property.

### Property: AlignPosition.MaxForce

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
  "category": "Compliance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum force magnitude the constraint can apply to achieve its goal. Only
used if [RigidityEnabled](/docs/reference/engine/classes/AlignPosition.md) is `false`
and [ForceLimitMode](/docs/reference/engine/classes/AlignPosition.md) is
[Magnitude](/docs/reference/engine/enums/ForceLimitMode.md).

Note that [MaxForce](/docs/reference/engine/classes/AlignPosition.md), as well as
[MaxVelocity](/docs/reference/engine/classes/AlignPosition.md), are **caps** to the force
and velocity respectively. The actual scale is determined by
[Responsiveness](/docs/reference/engine/classes/AlignPosition.md).

### Property: AlignPosition.MaxVelocity

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
  "category": "Compliance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum speed the attachments can move when converging. Only used if
[RigidityEnabled](/docs/reference/engine/classes/AlignPosition.md) is `false`.

Note that [MaxVelocity](/docs/reference/engine/classes/AlignPosition.md), as well as
[MaxForce](/docs/reference/engine/classes/AlignPosition.md), are **caps** to the velocity and
force respectively. The actual scale is determined by
[Responsiveness](/docs/reference/engine/classes/AlignPosition.md).

### Property: AlignPosition.Mode

```json
{
  "type": "PositionAlignmentMode",
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
  "category": "AlignmentMode",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Whether the constraint uses **one** or **two** attachments in calculating
its goal. By default, this is [TwoAttachment](/docs/reference/engine/enums/PositionAlignmentMode.md),
meaning that the constraint disregards
[Position](/docs/reference/engine/classes/AlignPosition.md) and attempts to move
[Attachment0](/docs/reference/engine/classes/Constraint.md) to the position of
[Attachment1](/docs/reference/engine/classes/Constraint.md).

If set to [OneAttachment](/docs/reference/engine/enums/PositionAlignmentMode.md), the constraint
disregards [Attachment1](/docs/reference/engine/classes/Constraint.md) and attempts to move
[Attachment0](/docs/reference/engine/classes/Constraint.md) to
[Position](/docs/reference/engine/classes/AlignPosition.md).

### Property: AlignPosition.Position

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
  "category": "AlignPosition",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The position to which the constraint should move its
[Attachment0](/docs/reference/engine/classes/Constraint.md). Only used if
[Mode](/docs/reference/engine/classes/AlignPosition.md) is set to
[OneAttachment](/docs/reference/engine/enums/PositionAlignmentMode.md), in which case
[Attachment1](/docs/reference/engine/classes/Constraint.md) is disregarded.

### Property: AlignPosition.ReactionForceEnabled

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
  "category": "AlignPosition",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

If `false` (default), the constraint only applies force to
[Attachment0](/docs/reference/engine/classes/Constraint.md) while
[Attachment1](/docs/reference/engine/classes/Constraint.md) remains unaffected. If `true`,
the constraint applies force to both attachments in **equal and opposite
directions**.

### Property: AlignPosition.Responsiveness

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
  "category": "Compliance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Controls how quickly the constraint reaches its goal. Higher values cause
the attachment(s) to align more rapidly. Value can be between 5 and 200.

### Property: AlignPosition.RigidityEnabled

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
  "category": "AlignPosition",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Whether force is dependent on other properties, or if the physics solver
reacts as quickly as possible to complete the alignment. If `false`
(default), the force is determined by
[MaxForce](/docs/reference/engine/classes/AlignPosition.md),
[MaxVelocity](/docs/reference/engine/classes/AlignPosition.md), and
[Responsiveness](/docs/reference/engine/classes/AlignPosition.md). If `true`, the
physics solver reacts as quickly as possible to complete the alignment.

## Inherited Members

### From [Constraint](/docs/reference/engine/classes/Constraint.md)

- **Property `Active`** (`boolean`): Indicates if the constraint is currently active in the world.
- **Property `Attachment0`** (`Attachment`): The Attachment that is connected to
- **Property `Attachment1`** (`Attachment`): The Attachment that is connected to
- **Property `Color`** (`BrickColor`): The color of the constraint.
- **Property `Enabled`** (`boolean`): Toggles whether or not the constraint is enabled.
- **Property `Visible`** (`boolean`): Toggles the constraint's visibility.
- **Method `GetDebugAppliedForce(bodyId: int): Vector3`**:  *(deprecated)*
- **Method `GetDebugAppliedTorque(bodyId: int): Vector3`**:  *(deprecated)*

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