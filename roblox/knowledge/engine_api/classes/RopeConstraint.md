---
name: RopeConstraint
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Simulates rope dynamics, preventing two attachments from separating further than a defined length."
---

# Class: RopeConstraint

> Simulates rope dynamics, preventing two attachments from separating further
> than a defined length.

## Description

A **RopeConstraint** prevents two attachments from separating further than a
defined [Length](/docs/reference/engine/classes/RopeConstraint.md). The attachments can move closer
together than this length and both can freely rotate. This constraint can also
be powered to behave as a motorized winch.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Winch

If a rope's [WinchEnabled](/docs/reference/engine/classes/RopeConstraint.md) property is
enabled, it attempts to translate the attachments to a set separation
specified by [WinchTarget](/docs/reference/engine/classes/RopeConstraint.md), effectively the
target length of the rope in studs. This translation is controlled by
[WinchSpeed](/docs/reference/engine/classes/RopeConstraint.md),
[WinchResponsiveness](/docs/reference/engine/classes/RopeConstraint.md), and
[WinchForce](/docs/reference/engine/classes/RopeConstraint.md).

Note that [WinchSpeed](/docs/reference/engine/classes/RopeConstraint.md) must be a **positive**
value, used to either contract or extend the rope length to
[WinchTarget](/docs/reference/engine/classes/RopeConstraint.md). Setting a negative speed will
revert to 0, not reverse the winch servo direction.

## Properties

### Property: RopeConstraint.CurrentDistance

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

The current distance between the constraint's
[Attachments](/docs/reference/engine/classes/Attachment.md).

### Property: RopeConstraint.Length

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
  "category": "Rope",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The maximum distance apart the two [Attachments](/docs/reference/engine/classes/Attachment.md) can be.
Measured in studs.

### Property: RopeConstraint.Restitution

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
  "category": "Rope",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Elasticity of the [Attachments](/docs/reference/engine/classes/Attachment.md) connected by the
constraint when reaching the maximum defined
[Length](/docs/reference/engine/classes/RopeConstraint.md). Constrained between 0 and 1.

### Property: RopeConstraint.Thickness

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

The visualized thickness of the [RopeConstraint](/docs/reference/engine/classes/RopeConstraint.md).

### Property: RopeConstraint.WinchEnabled

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
  "category": "Rope",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Enables the winch motor which has the effect or reeling in/out the length
of the rope to [WinchTarget](/docs/reference/engine/classes/RopeConstraint.md).

### Property: RopeConstraint.WinchForce

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
  "category": "Winch",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The maximum force that the winch motor can apply.

### Property: RopeConstraint.WinchResponsiveness

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
  "category": "Winch",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The sharpness of the winch motor in reaching the
[WinchTarget](/docs/reference/engine/classes/RopeConstraint.md).

### Property: RopeConstraint.WinchSpeed

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
  "category": "Winch",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

A positive desired velocity at which the winch motor changes the rope
length.

### Property: RopeConstraint.WinchTarget

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
  "category": "Winch",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The target length for the winch motor.

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