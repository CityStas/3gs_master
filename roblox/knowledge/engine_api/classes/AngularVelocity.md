---
name: AngularVelocity
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Applies torque on an assembly to maintain a constant angular velocity."
---

# Class: AngularVelocity

> Applies torque on an assembly to maintain a constant angular velocity.

## Description

The `AngularVelocity` constraint applies torque on an assembly to maintain a
**constant** angular velocity. Alternatively:

- If you want to control the amount of torque applied, use a [Torque](/docs/reference/engine/classes/Torque.md)
  constraint.
- If you only need **initial** angular velocity, set the
  [AssemblyAngularVelocity](/docs/reference/engine/classes/BasePart.md) method
  directly on the assembly.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Relativity

Application of velocity can be controlled through the constraint's
[RelativeTo](/docs/reference/engine/classes/AngularVelocity.md) property. If set to
[World](/docs/reference/engine/enums/ActuatorRelativeTo.md), the angular velocity vector is used as is. If
set to [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md) and the constraint's
[Attachment1](/docs/reference/engine/classes/Constraint.md) property is set to another
attachment, the angular velocity will be affected by that of the other
attachment. Setting [RelativeTo](/docs/reference/engine/classes/AngularVelocity.md) to
[Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md) also exposes the
[ReactionTorqueEnabled](/docs/reference/engine/classes/AngularVelocity.md) property.

## Properties

### Property: AngularVelocity.AngularVelocity

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
  "category": "Torque",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

A [Vector3](/docs/reference/engine/datatypes/Vector3.md) that gives the desired or target angular velocity.
This vector is set in the [CFrame](/docs/reference/engine/datatypes/CFrame.md) expressed by the
[RelativeTo](/docs/reference/engine/classes/AngularVelocity.md) property.

### Property: AngularVelocity.MaxTorque

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
  "category": "Torque",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Magnitude of the maximum torque the constraint can apply.

### Property: AngularVelocity.ReactionTorqueEnabled

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
  "category": "Torque",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

This property, when enabled, causes the constraint to apply equal and
opposite reaction forces. This is important if the two attached parts can
collide, since without reaction forces collisions can create energy that
would otherwise be disregarded.

When enabled, the reaction forces cause the constraint to act like an
angular motor between the two attachments.

Only meaningful when [RelativeTo](/docs/reference/engine/classes/AngularVelocity.md) is set
to [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md).

### Property: AngularVelocity.RelativeTo

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
  "category": "Torque",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The coordinate frame in which the
[AngularVelocity](/docs/reference/engine/classes/AngularVelocity.md) vector is
expressed, selected by an [ActuatorRelativeTo](/docs/reference/engine/enums/ActuatorRelativeTo.md) value. If set to
[World](/docs/reference/engine/enums/ActuatorRelativeTo.md), the angular velocity vector is used as
is. If set to [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md), the angular velocity
is transformed by the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the assigned attachment.

[RelativeTo](/docs/reference/engine/classes/AngularVelocity.md) can also be set to
[Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md), but it makes no physical sense and
will lead to unpredictable behaviors.

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