---
name: SwimController
last_updated: 2026-10-30T19:55:53Z
inherits:
  - ControllerBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The ControllerBase that moves a ControllerManager character while it is swimming."
---

# Class: SwimController

> The [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) that moves a [ControllerManager](/docs/reference/engine/classes/ControllerManager.md) character
> while it is swimming.

## Description

[SwimController](/docs/reference/engine/classes/SwimController.md) is the [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) that a
[ControllerManager](/docs/reference/engine/classes/ControllerManager.md) activates to move a physics-based character while it
is swimming. When it is the manager's
[ControllerManager.ActiveController](/docs/reference/engine/classes/ControllerManager.md), it drives the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) toward the manager's target velocity
(scaled by [ControllerBase.MoveSpeedFactor](/docs/reference/engine/classes/ControllerBase.md)), pitches the character to
face the [ControllerManager.FacingDirection](/docs/reference/engine/classes/ControllerManager.md), and rolls it to keep it
oriented in the water. Pitch rotation is tuned with
[SwimController.PitchMaxTorque](/docs/reference/engine/classes/SwimController.md) and
[SwimController.PitchSpeedFactor](/docs/reference/engine/classes/SwimController.md), and roll with
[SwimController.RollMaxTorque](/docs/reference/engine/classes/SwimController.md) and
[SwimController.RollSpeedFactor](/docs/reference/engine/classes/SwimController.md), with the speed factors scaled by
[ControllerManager.BaseTurnSpeed](/docs/reference/engine/classes/ControllerManager.md). A [SwimController](/docs/reference/engine/classes/SwimController.md) only
functions when parented to a [ControllerManager](/docs/reference/engine/classes/ControllerManager.md).

## Properties

### Property: SwimController.PitchMaxTorque

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
  "category": "Balance",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The maximum torque used to rotate on the local **X** axis to the desired
pitch orientation. Has no effect if [ControllerBase.RigidityEnabled](/docs/reference/engine/classes/ControllerBase.md)
is true.

### Property: SwimController.PitchSpeedFactor

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
  "category": "Balance",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Multiplied by [ControllerManager.BaseTurnSpeed](/docs/reference/engine/classes/ControllerManager.md) to determine the
maximum angular velocity rotating on the local **X** axis. Has no effect
if [ControllerBase.RigidityEnabled](/docs/reference/engine/classes/ControllerBase.md) is true.

### Property: SwimController.RollMaxTorque

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
  "category": "Balance",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The maximum torque applied to rotate on the local **Z** axis to the
desired roll orientation. Has no effect if
[ControllerBase.RigidityEnabled](/docs/reference/engine/classes/ControllerBase.md) is true.

### Property: SwimController.RollSpeedFactor

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
  "category": "Balance",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Multiplied by [ControllerManager.BaseTurnSpeed](/docs/reference/engine/classes/ControllerManager.md) to determine the
maximum angular velocity rotating on the local **Z** axis. Has no effect
if [ControllerBase.RigidityEnabled](/docs/reference/engine/classes/ControllerBase.md) is true.

## Inherited Members

### From [ControllerBase](/docs/reference/engine/classes/ControllerBase.md)

- **Property `Active`** (`boolean`): Whether this controller is currently the active controller of its
- **Property `BalanceRigidityEnabled`** (`boolean`): Whether the controller holds its balance orientation rigidly instead of
- **Property `MoveSpeedFactor`** (`float`): The value multiplied by the ControllerManager.BaseMoveSpeed.

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