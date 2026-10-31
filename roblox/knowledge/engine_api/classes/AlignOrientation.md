---
name: AlignOrientation
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Constraint which applies torque to align two attachments, or to align one attachment with a goal orientation."
---

# Class: AlignOrientation

> Constraint which applies torque to align two attachments, or to align one
> attachment with a goal orientation.

## Description

The `AlignOrientation` constraint applies torque to align two attachments, or
to align one attachment with a goal orientation. As indicated by the name, it
only affects the **orientation** of the attachments, not their position (to
align attachments **positionally**, see [AlignPosition](/docs/reference/engine/classes/AlignPosition.md)).

Torque created by `AlignOrientation` is applied about the center of mass of
the parent of the attachments, or the center of mass of parts rigidly
connected to the parents.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Affected Axes

The axes affected by torque are controlled through the constraint's
[AlignType](/docs/reference/engine/classes/AlignOrientation.md) property. When set to
[PrimaryAxisParallel](/docs/reference/engine/enums/AlignType.md),
[PrimaryAxisPerpendicular](/docs/reference/engine/enums/AlignType.md) or
[PrimaryAxisLookAt](/docs/reference/engine/enums/AlignType.md), torque will only occur when the primary
axes become misaligned. Otherwise, the constraint will apply torque about all
3 axes to achieve alignment.

#### Reactionary Torque

By default, the constraint only applies torque to
[Attachment0](/docs/reference/engine/classes/Constraint.md) while
[Attachment1](/docs/reference/engine/classes/Constraint.md) remains unaffected. If desired,
torque can be applied to both attachments in **equal and opposite directions**
by enabling
[ReactionTorqueEnabled](/docs/reference/engine/classes/AlignOrientation.md).

#### Torque Magnitude

You can configure this constraint to apply the maximum torque that constraints
allow through the [RigidityEnabled](/docs/reference/engine/classes/AlignOrientation.md)
property. When `true`, the physics solver reacts as quickly as possible to
complete the alignment. When `false`, the torque is determined by
[MaxTorque](/docs/reference/engine/classes/AlignOrientation.md),
[MaxAngularVelocity](/docs/reference/engine/classes/AlignOrientation.md), and
[Responsiveness](/docs/reference/engine/classes/AlignOrientation.md).

#### Attachment Mode

This constraint can use either **one** or **two** attachments in calculating
its goal. See [Mode](/docs/reference/engine/classes/AlignOrientation.md) for details.

## Properties

### Property: AlignOrientation.AlignType

```json
{
  "type": "AlignType",
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
  "category": "AlignOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Specifies the desired relationship between the primary axes of
[Attachment0](/docs/reference/engine/classes/Constraint.md) and the goal. Available options
are [AllAxes](/docs/reference/engine/enums/AlignType.md), [PrimaryAxisParallel](/docs/reference/engine/enums/AlignType.md),
[PrimaryAxisPerpendicular](/docs/reference/engine/enums/AlignType.md), and
[PrimaryAxisLookAt](/docs/reference/engine/enums/AlignType.md). The constraint will attempt to
maintain the specified relationship, as given by the [AlignType](/docs/reference/engine/enums/AlignType.md), by
applying torques onto the relevant axes.

### Property: AlignOrientation.CFrame

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
  "category": "TargetOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The [CFrame](/docs/reference/engine/datatypes/CFrame.md) orientation (translation component ignored) with
which the constraint will attempt to match the orientation of
[Attachment0](/docs/reference/engine/classes/Constraint.md). Only used when
[Mode](/docs/reference/engine/classes/AlignOrientation.md) is set to
[OneAttachment](/docs/reference/engine/enums/OrientationAlignmentMode.md).

### Property: AlignOrientation.LookAtPosition

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
  "category": "TargetOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

A [Vector3](/docs/reference/engine/datatypes/Vector3.md) world space location toward which the primary axis
will attempt to align. This is only active when
[AlignType](/docs/reference/engine/classes/AlignOrientation.md) is set to
[PrimaryAxisLookAt](/docs/reference/engine/enums/AlignType.md) and [Mode](/docs/reference/engine/classes/AlignOrientation.md)
is set to [OneAttachment](/docs/reference/engine/enums/OrientationAlignmentMode.md).

### Property: AlignOrientation.MaxAngularVelocity

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

Maximum angular velocity the constraint can use to reach its goal. Only
used if [RigidityEnabled](/docs/reference/engine/classes/AlignOrientation.md) is
`false`.

Note that [MaxAngularVelocity](/docs/reference/engine/classes/AlignOrientation.md),
as well as [MaxTorque](/docs/reference/engine/classes/AlignOrientation.md), are **caps** to
the angular velocity and torque respectively. The actual scale is
determined by [Responsiveness](/docs/reference/engine/classes/AlignOrientation.md).

### Property: AlignOrientation.MaxTorque

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

Maximum torque the constraint can use to reach its goal. Only used if
[RigidityEnabled](/docs/reference/engine/classes/AlignOrientation.md) is `false`.

Note that [MaxTorque](/docs/reference/engine/classes/AlignOrientation.md), as well as
[MaxAngularVelocity](/docs/reference/engine/classes/AlignOrientation.md), are
**caps** to the torque and angular velocity respectively. The actual scale
is determined by [Responsiveness](/docs/reference/engine/classes/AlignOrientation.md).

### Property: AlignOrientation.Mode

```json
{
  "type": "OrientationAlignmentMode",
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
its goal. By default, this is
[TwoAttachment](/docs/reference/engine/enums/OrientationAlignmentMode.md), meaning that the constraint
attempts to match the orientation of
[Attachment0](/docs/reference/engine/classes/Constraint.md) with the orientation of
[Attachment1](/docs/reference/engine/classes/Constraint.md), disregarding
[CFrame](/docs/reference/engine/classes/AlignOrientation.md),
[PrimaryAxis](/docs/reference/engine/classes/AlignOrientation.md), and
[SecondaryAxis](/docs/reference/engine/classes/AlignOrientation.md).

If set to [OneAttachment](/docs/reference/engine/enums/OrientationAlignmentMode.md), the constraint
disregards [Attachment1](/docs/reference/engine/classes/Constraint.md) and attempts to
match the orientation of [Attachment0](/docs/reference/engine/classes/Constraint.md) with
the orientation of [CFrame](/docs/reference/engine/classes/AlignOrientation.md), or match the
attachment's [Axis](/docs/reference/engine/classes/Attachment.md) and
[SecondaryAxis](/docs/reference/engine/classes/Attachment.md) with the constraint's
[PrimaryAxis](/docs/reference/engine/classes/AlignOrientation.md) and
[SecondaryAxis](/docs/reference/engine/classes/AlignOrientation.md) properties
respectively.

### Property: AlignOrientation.PrimaryAxis

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
  "category": "TargetOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The direction of the goal's **X** axis, represented as a unit
[Vector3](/docs/reference/engine/datatypes/Vector3.md). Only used when [Mode](/docs/reference/engine/classes/AlignOrientation.md) is
[OneAttachment](/docs/reference/engine/enums/OrientationAlignmentMode.md).

### Property: AlignOrientation.PrimaryAxisOnly

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
  "category": "AlignOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Determines how the constraint's axes are affected by torque. If `false`
(default), the constraint will apply torque about all 3&nbsp;axes to
achieve alignment. If `true`, torque will only occur when the primary axes
become misaligned.

Enabling [PrimaryAxisOnly](/docs/reference/engine/classes/AlignOrientation.md) also
enables the [AlignType](/docs/reference/engine/classes/AlignOrientation.md) property.

### Property: AlignOrientation.ReactionTorqueEnabled

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
  "category": "AlignOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

If `false` (default), the constraint only applies torque to
[Attachment0](/docs/reference/engine/classes/Constraint.md) while
[Attachment1](/docs/reference/engine/classes/Constraint.md) remains unaffected. If `true`,
the constraint applies torque to both attachments in **equal and opposite
directions**.

### Property: AlignOrientation.Responsiveness

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

### Property: AlignOrientation.RigidityEnabled

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
  "category": "AlignOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Whether torque is dependent on other properties, or if the physics solver
reacts as quickly as possible to complete the alignment. If `false`
(default), the torque is determined by
[MaxTorque](/docs/reference/engine/classes/AlignOrientation.md),
[MaxAngularVelocity](/docs/reference/engine/classes/AlignOrientation.md), and
[Responsiveness](/docs/reference/engine/classes/AlignOrientation.md). If `true`, the
physics solver reacts as quickly as possible to complete the alignment.

### Property: AlignOrientation.SecondaryAxis

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
  "category": "TargetOrientation",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The direction of the goal's **Y** axis, represented as a unit
[Vector3](/docs/reference/engine/datatypes/Vector3.md). Only used when [Mode](/docs/reference/engine/classes/AlignOrientation.md) is
[OneAttachment](/docs/reference/engine/enums/OrientationAlignmentMode.md).

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