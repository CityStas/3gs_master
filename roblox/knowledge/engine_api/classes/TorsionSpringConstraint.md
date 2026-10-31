---
name: TorsionSpringConstraint
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "A rotational spring that opposes the angular motion between two axes."
---

# Class: TorsionSpringConstraint

> A rotational spring that opposes the angular motion between two axes.

## Description

A **TorsionSpringConstraint** applies a torque based on a relative angle and a
relative angular velocity. Specifically, torsion springs try to bring two axes
from two parts together in a compliant way.

Correct orientation of a torsion spring's attachments is important. The
constraint will attempt to bring the
[SecondaryAxis](/docs/reference/engine/classes/Attachment.md) of each attachment into
alignment. When building mechanisms like swinging doors, ensure that the
secondary axes are **perpendicular** to the intended axis of rotation.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Damping

The [Damping](/docs/reference/engine/classes/TorsionSpringConstraint.md) value controls how fast
the spring's oscillation dies down. A value of 0 allows the spring to
oscillate endlessly, while higher values bring the spring to a rest more
quickly.

#### Stiffness

[Stiffness](/docs/reference/engine/classes/TorsionSpringConstraint.md) sets the torsional
strength of the spring. Higher values create a spring that responds with more
force.

#### Limits

Enabling the [LimitsEnabled](/docs/reference/engine/classes/TorsionSpringConstraint.md)
property exposes the [MaxAngle](/docs/reference/engine/classes/TorsionSpringConstraint.md) value
to restrict the spring's range within a cone; it also exposes the
[Restitution](/docs/reference/engine/classes/TorsionSpringConstraint.md) value which defines
the elasticity of the attachments when they reach their limit.

## Properties

### Property: TorsionSpringConstraint.Coils

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

This property indicates the number of spring coils for visualization.
Default value is 8.

### Property: TorsionSpringConstraint.CurrentAngle

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Derived",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The current angle, in degrees, of the torsion spring's limiting cone. The
limiting cone is formed at the position of the constraint's
[Attachment0](/docs/reference/engine/classes/Constraint.md) around its secondary axis with
an angle equal to [MaxAngle](/docs/reference/engine/classes/TorsionSpringConstraint.md).

### Property: TorsionSpringConstraint.Damping

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
  "category": "Spring",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Damping constant for the [TorsionSpringConstraint](/docs/reference/engine/classes/TorsionSpringConstraint.md). Multiplied to
the velocity of the constraint's [Attachments](/docs/reference/engine/classes/Attachment.md) to reduce
the spring force applied.

### Property: TorsionSpringConstraint.LimitsEnabled

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
  "category": "Spring",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

This property, when enabled, limits the relative angular motion of the
secondary axes of attachments through a cone constraint. The default value
is false.

### Property: TorsionSpringConstraint.MaxAngle

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

This property determines the maximum angle (in degrees) of the torsion
spring's limiting cone. The limiting cone is formed at the position of the
constraint's [Attachment0](/docs/reference/engine/classes/Constraint.md) around its
secondary axis with an angle equal to
[MaxAngle](/docs/reference/engine/classes/TorsionSpringConstraint.md). Default value is 45
degrees.

### Property: TorsionSpringConstraint.MaxTorque

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
  "category": "Spring",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

This property determines the maximum torque supported by the torsion
spring. Defaults to 1000.

### Property: TorsionSpringConstraint.Radius

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

This property indicates the visualization radius of the spring, in studs.
Default value is 0.4.

### Property: TorsionSpringConstraint.Restitution

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

This property defines how elastic [Attachments](/docs/reference/engine/classes/Attachment.md) connected
by a [TorsionSpringConstraint](/docs/reference/engine/classes/TorsionSpringConstraint.md) are when they reach the end of the
range specified by [MaxAngle](/docs/reference/engine/classes/TorsionSpringConstraint.md), when
[LimitEnabled](/docs/reference/engine/classes/TorsionSpringConstraint.md) is true. The
value defaults to 0 and can be any floating number within the range of 0
and 1.

### Property: TorsionSpringConstraint.Stiffness

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
  "category": "Spring",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

In the absence of damping, this property is proportional to the opposing
torque of the spring. For instance, higher stiffness results in a larger
opposing torque, and smaller stiffness results in a smaller opposing
torque. The larger the torque value, the faster the axes are pushed
together when the relative angle is positive (or away from each other if
the relative angle is negative). The value defaults to 100.

### Property: TorsionSpringConstraint.LimitEnabled *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Spring",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

> **Deprecated:** This property is deprecated. Use [LimitsEnabled](/docs/reference/engine/classes/TorsionSpringConstraint.md) instead.

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