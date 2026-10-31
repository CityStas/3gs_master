---
name: Motor6D
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Motor
  - JointInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Creates an animatable joint between two BaseParts. Superseded by AnimationConstraint for avatar/character rigs. Motor6D is no longer used by default for player characters when AvatarJointUpgrade is enabled."
---

# Class: Motor6D

> Creates an animatable joint between two [BaseParts](/docs/reference/engine/classes/BasePart.md). Superseded
> by [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md) for avatar/character rigs. Motor6D is no longer
> used by default for player characters when
> [AvatarJointUpgrade](/docs/reference/engine/classes/StarterPlayer.md) is enabled.

## Description

#### Description

**Motor6D** joins two [BaseParts](/docs/reference/engine/classes/BasePart.md)
([Part0](/docs/reference/engine/classes/JointInstance.md) and [Part1](/docs/reference/engine/classes/JointInstance.md))
together in an animatable way. The [Transform](/docs/reference/engine/classes/Motor6D.md)
property determines the offset between these parts. This can be set manually
using [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md) or through an [Animator](/docs/reference/engine/classes/Animator.md).

Models whose parts are joined by [Motor6D](/docs/reference/engine/classes/Motor6D.md) are usually referred to as
**rigs**, typically for [Humanoids](/docs/reference/engine/classes/Humanoid.md). Motor6D remains
appropriate for non-avatar mechanical rigs (doors, turrets, vehicles) where
physical simulation is not needed.

#### Transitioning to AnimationConstraint for Avatar rigs

As of the
[Avatar Joint Upgrade](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561),
R15 player characters spawn with
[AnimationConstraints](/docs/reference/engine/classes/AnimationConstraint.md) instead of Motor6Ds when
[AvatarJointUpgrade](/docs/reference/engine/classes/StarterPlayer.md) is enabled (the
default for new experiences). Code that assumes character joints are Motor6Ds
— such as `character:FindFirstChildOfClass("Motor6D")` or
`joint:IsA("Motor6D")` — will not find joints on upgraded characters. Use
[AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md) for new avatar rig code. See the migration notes
on the [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md) page.

## Properties

### Property: Motor6D.ChildName

```json
{
  "type": "string",
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
  "category": "Animatable",
  "capabilities": [
    "Physics"
  ]
}
```

A read-only string that reflects the [Name](/docs/reference/engine/classes/Instance.md) of the
part assigned to [Part1](/docs/reference/engine/classes/JointInstance.md) (the joint's child).
The value is derived from `Part1`, so writing to it has no effect. When
[Part1](/docs/reference/engine/classes/JointInstance.md) is not set, this property is an empty
string.

The animation system uses this name to match the joint against the
corresponding pose channel in an animation, so a rig's part names must
line up with the names authored in its animations.

### Property: Motor6D.ParentName

```json
{
  "type": "string",
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
  "category": "Animatable",
  "capabilities": [
    "Physics"
  ]
}
```

A read-only string that reflects the [Name](/docs/reference/engine/classes/Instance.md) of the
part assigned to [Part0](/docs/reference/engine/classes/JointInstance.md) (the joint's parent).
The value is derived from `Part0`, so writing to it has no effect. When
[Part0](/docs/reference/engine/classes/JointInstance.md) is not set, this property is an empty
string.

The animation system uses this name to match the joint against the
corresponding pose channel in an animation, so a rig's part names must
line up with the names authored in its animations.

### Property: Motor6D.Transform *(hidden)*

```json
{
  "type": "CFrame",
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
  "category": "Data",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The internal [CFrame](/docs/reference/engine/datatypes/CFrame.md) that is manipulated when a [Motor6D](/docs/reference/engine/classes/Motor6D.md)
is being animated. It is recommended to use this property for custom
animations rather than [JointInstance.C0](/docs/reference/engine/classes/JointInstance.md) and
[JointInstance.C1](/docs/reference/engine/classes/JointInstance.md).

##### Timing

[Motor6D](/docs/reference/engine/classes/Motor6D.md) transforms are not applied immediately, unlike updating
[C0](/docs/reference/engine/classes/JointInstance.md) and [C1](/docs/reference/engine/classes/JointInstance.md), but rather as
a batch in a parallel job after [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md),
immediately before physics steps. The deferred batch update is much more
efficient than many immediate updates.

If the [Motor6D](/docs/reference/engine/classes/Motor6D.md) is part of an animated model with an
[Animator](/docs/reference/engine/classes/Animator.md), then [Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md) will usually be
overwritten every frame by the [Animator](/docs/reference/engine/classes/Animator.md) after
[RunService.PreAnimation](/docs/reference/engine/classes/RunService.md) and before
[RunService.PreSimulation](/docs/reference/engine/classes/RunService.md).

## Inherited Members

### From [Motor](/docs/reference/engine/classes/Motor.md)

- **Property `CurrentAngle`** (`float`): Displays the current rotation of the motor in radians.
- **Property `DesiredAngle`** (`float`): The desired angle to turn the motor to in radians.
- **Property `MaxVelocity`** (`float`): The maximum velocity the motor can use to reach Motor.DesiredAngle
- **Method `SetDesiredAngle(value: float): ()`**: Sets Motor.DesiredAngle of the motor.

### From [JointInstance](/docs/reference/engine/classes/JointInstance.md)

- **Property `Active`** (`boolean`): Determines if the joint is currently active in the world.
- **Property `C0`** (`CFrame`): Determines how the offset point is attached to
- **Property `C1`** (`CFrame`): Subtracted from the C0 property to create an
- **Property `Enabled`** (`boolean`): Sets whether the joint is active or not.
- **Property `Part0`** (`BasePart`): The first BasePart that the joint connects.
- **Property `Part1`** (`BasePart`): The second BasePart that the joint connects.
- **Property `part1`** (`BasePart`):  *(deprecated, hidden)*

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