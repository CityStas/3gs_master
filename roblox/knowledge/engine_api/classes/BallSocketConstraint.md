---
name: BallSocketConstraint
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Forces its two attachments into the same position and allows them to freely rotate about all three axes, with optional limits to restrict both tilt and twist."
---

# Class: BallSocketConstraint

> Forces its two attachments into the same position and allows them to freely
> rotate about all three axes, with optional limits to restrict both tilt and
> twist.

## Description

A `BallSocketConstraint` constrains its [Attachments](/docs/reference/engine/classes/Attachment.md) so that
they occupy the same position. By default it allows both attachments to freely
rotate about all of their axes, but if
[LimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) is `true`, the
attachments can only rotate in a limited cone.

Note that if this constraint attaches one part (**A**) to another part (**B**)
that is anchored or connected to an anchored part (**Z**), part **A** will not
be locally simulated when interacting with a player.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Limits

You can set limits to restrict both **tilt** and **twist** of a ball socket,
similar to how a human's head can tilt and turn within a limited axial range.
Enabling the [LimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) property
exposes the [UpperAngle](/docs/reference/engine/classes/BallSocketConstraint.md) value to
restrict **tilt** within a cone; it also exposes the
[TwistLimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) property
which, when enabled, lets you restrict **twist** rotation through the
[TwistLowerAngle](/docs/reference/engine/classes/BallSocketConstraint.md) and
[TwistUpperAngle](/docs/reference/engine/classes/BallSocketConstraint.md) limits.

## Properties

### Property: BallSocketConstraint.LimitsEnabled

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
  "category": "BallSocket",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets whether the `BallSocketConstraint` has a limit on rotation based on
[UpperAngle](/docs/reference/engine/classes/BallSocketConstraint.md). When `true`, it
enforces that its [Attachment1](/docs/reference/engine/classes/Constraint.md) isn't rotated
more than a set angle from its [Attachment0](/docs/reference/engine/classes/Constraint.md).

### Property: BallSocketConstraint.MaxFrictionTorque

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
  "category": "Friction",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets the maximum frictional torque applied to keep its
[Attachments](/docs/reference/engine/classes/Attachment.md) aligned.

`MaxFrictionTorque` specifies the stiffness of the `BallSocketConstraint`
(how much it resists rotation around its [Attachments](/docs/reference/engine/classes/Attachment.md)).

### Property: BallSocketConstraint.Radius

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
    "Physics"
  ],
  "simulationAccess": true
}
```

The visualized radius of the `BallSocketConstraint`.

### Property: BallSocketConstraint.Restitution

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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

How elastic [Attachments](/docs/reference/engine/classes/Attachment.md) connected by a
`BallSocketConstraint` will be when they reach the end of the range
specified by [UpperAngle](/docs/reference/engine/classes/BallSocketConstraint.md) when
[LimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) is `true`.
Constrained between 0 and 1.

### Property: BallSocketConstraint.TwistLimitsEnabled

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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets whether the `BallSocketConstraint` sets a limit on twist rotation
based on [TwistUpperAngle](/docs/reference/engine/classes/BallSocketConstraint.md) and
[TwistLowerAngle](/docs/reference/engine/classes/BallSocketConstraint.md). The twist
angle is defined as the angle between the **Y** axis of
[Attachment1](/docs/reference/engine/classes/Constraint.md) and the **Y** axis of
[Attachment0](/docs/reference/engine/classes/Constraint.md).

### Property: BallSocketConstraint.TwistLowerAngle

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
  "category": "TwistLimits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets the lower twist rotation limit of the `BallSocketConstraint`, as long
as [TwistLimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) is
`true`.

### Property: BallSocketConstraint.TwistUpperAngle

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
  "category": "TwistLimits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets the upper twist rotation limit of the `BallSocketConstraint`, as long
as [TwistLimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) is
`true`.

### Property: BallSocketConstraint.UpperAngle

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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets the upper rotation limit of the `BallSocketConstraint`, as long as
[LimitsEnabled](/docs/reference/engine/classes/BallSocketConstraint.md) is `true`.

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