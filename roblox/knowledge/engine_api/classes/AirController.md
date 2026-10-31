---
name: AirController
last_updated: 2026-10-30T19:55:51Z
inherits:
  - ControllerBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A physics character controller that governs movement while a character is airborne."
---

# Class: AirController

> A physics character controller that governs movement while a character is
> airborne.

## Description

An [AirController](/docs/reference/engine/classes/AirController.md) is a [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) that a
[ControllerManager](/docs/reference/engine/classes/ControllerManager.md) uses to drive a character's physics-based movement
while it is airborne, such as while jumping or falling. While it is the
manager's [ActiveController](/docs/reference/engine/classes/ControllerManager.md), it
keeps the character balanced upright, turns it toward the
[ControllerManager.FacingDirection](/docs/reference/engine/classes/ControllerManager.md), and moves it horizontally toward
the [ControllerManager.MovingDirection](/docs/reference/engine/classes/ControllerManager.md). Uprighting is tuned with
[BalanceMaxTorque](/docs/reference/engine/classes/AirController.md) and
[BalanceSpeed](/docs/reference/engine/classes/AirController.md), turning with
[TurnMaxTorque](/docs/reference/engine/classes/AirController.md) and
[TurnSpeedFactor](/docs/reference/engine/classes/AirController.md), and horizontal movement
with [MoveMaxForce](/docs/reference/engine/classes/AirController.md). An [AirController](/docs/reference/engine/classes/AirController.md)
only functions when parented to a [ControllerManager](/docs/reference/engine/classes/ControllerManager.md).

## Properties

### Property: AirController.BalanceMaxTorque

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

The maximum torque the character can use to remain balanced upright. When
misaligned, this amount of torque is applied to reach the
[BalanceSpeed](/docs/reference/engine/classes/AirController.md) and realign the character.
A higher torque means more force is required to cause the character to
tilt. A lower torque means it's easer for the character to flip in the
air. This property is hidden and has no effect when
[ControllerBase.BalanceRigidityEnabled](/docs/reference/engine/classes/ControllerBase.md) is true.

### Property: AirController.BalanceSpeed

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

The maximum angular speed used to align the character upright. A lower
value means it takes longer for the character to recover to the upright
position when misaligned. A higher value results in a quicker recovery.

### Property: AirController.MaintainAngularMomentum

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
  "category": "Turn",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Determines whether angular momentum is preserved when input has stopped.
If false, the character will apply
[TurningMaxTorque](/docs/reference/engine/classes/AirController.md) to bring the
angular velocity toward 0 when there is no input.

### Property: AirController.MaintainLinearMomentum

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Determines whether linear momentum is preserved when input has stopped. If
false, the character will apply
[MoveMaxForce](/docs/reference/engine/classes/AirController.md) to bring the linear
velocity towards 0 when there is no input.

### Property: AirController.MoveMaxForce

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The maximum force that can be applied on the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) for moving in the
[ControllerManager.MovingDirection](/docs/reference/engine/classes/ControllerManager.md). This affects how quickly
different target linear velocities are reached and how quick the linear
acceleration is if
[MaintainLinearMomentum](/docs/reference/engine/classes/AirController.md) is
off.

### Property: AirController.TurnMaxTorque

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
  "category": "Turn",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The maximum torque that can be applied on the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) for turning towards the
[ControllerManager.FacingDirection](/docs/reference/engine/classes/ControllerManager.md). This effects how quickly
different target angular velocities are reached and how quick angular
deceleration is if
[MaintainAngularMomentum](/docs/reference/engine/classes/AirController.md) is
off.

### Property: AirController.TurnSpeedFactor

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
  "category": "Turn",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The value multiplied by the [ControllerManager.BaseTurnSpeed](/docs/reference/engine/classes/ControllerManager.md) to
determine the final target angular velocity while this controller is
active. The angular velocity is applied when turning towards the
[ControllerManager.FacingDirection](/docs/reference/engine/classes/ControllerManager.md).

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