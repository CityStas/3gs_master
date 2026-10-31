---
name: AnimationConstraint
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Aligns two BaseParts with an animate-able kinematic or force-based joint that supports physical simulation (ragdoll, arm strength). The default joint type for R15 avatar rigs."
---

# Class: AnimationConstraint

> Aligns two [BaseParts](/docs/reference/engine/classes/BasePart.md) with an animate-able kinematic or
> force-based joint that supports physical simulation (ragdoll, arm strength).
> The default joint type for R15 avatar rigs.

## Description

#### Replaces Motor6D for Avatar rigs

As part of the
[Avatar Joint Upgrade](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561),
`AnimationConstraint` is the **replacement for [Motor6D](/docs/reference/engine/classes/Motor6D.md)** in
[R15 player character rigs](/docs/en-us/avatar/character-bodies/specifications.md#rigging).
When [AvatarJointUpgrade](/docs/reference/engine/classes/StarterPlayer.md) is enabled
(the default for new experiences), player characters spawn with
AnimationConstraints instead of Motor6Ds. Unlike Motor6D, AnimationConstraint
supports both kinematic animation and force-based physical simulation —
enabling ragdoll physics, arm strength, and other physically simulated
character movement without rebuilding the rig.

#### Migrating from Motor6D

If you have existing code that uses Motor6D for character rigs, note these key
differences. See also the
[Phase 2 migration recommendations](https://devforum.roblox.com/t/avatar-joint-upgrade-aju-phase-2-rollout-updated-migration-recommendations/4656414).

- **Finding joints**: Use `:FindFirstChildWhichIsA("AnimationConstraint")`
  instead of `:FindFirstChildOfClass("Motor6D")`. For code that must support
  both old and new rigs, check for AnimationConstraint first, then fall back
  to Motor6D.
- **C0, C1, Part0, Part1**: These properties exist on AnimationConstraint as
  **read-only** aliases for backwards compatibility. They map to
  `Attachment0.CFrame`, `Attachment1.CFrame`, `Attachment0.Parent`, and
  `Attachment1.Parent` respectively. Do not attempt to write to them.
- **Do not modify RigAttachment.CFrame directly** — this disrupts animation
  retargeting and causes performance issues.
- **Transform**: Works identically to [Motor6D.Transform](/docs/reference/engine/classes/Motor6D.md) — the
  [Animator](/docs/reference/engine/classes/Animator.md) writes to it each frame. Layer procedural animations by
  multiplying into `Transform` during [RunService.PreSimulation](/docs/reference/engine/classes/RunService.md), which
  stacks with active animation tracks without breaking retargeting.
- **IsKinematic**: When `true` (default), behavior is equivalent to Motor6D.
  Set to `false` to enable force-based physical simulation.
- **Type checks**: `animConstraint:IsA("Motor6D")` returns `false`. Update any
  `IsA("Motor6D")` guards to also accept `"AnimationConstraint"`.
- **Server replication**: Instead of setting C0 on the server, use client-side
  animation evaluation and synchronize data through custom Attributes or
  [UnreliableRemoteEvent](/docs/reference/engine/classes/UnreliableRemoteEvent.md).

##### Example: Procedural neck rotation

```lua
-- Before (Motor6D): writing to C0 directly
local originalC0 = neck.C0
RunService.RenderStepped:Connect(function()
    neck.C0 = originalC0 * computeNeckRotation()
end)

-- After (AnimationConstraint): multiplying into Transform during PreSimulation
RunService.PreSimulation:Connect(function()
    if not animator.EvaluationThrottled then
        neck.Transform = computeNeckRotation() * neck.Transform
    end
end)
```

#### Description

An `AnimationConstraint` constrains its [Attachments](/docs/reference/engine/classes/Attachment.md) so that
they're offset by [Transform](/docs/reference/engine/classes/AnimationConstraint.md). When
[IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is `true`, the parts
follow the transform perfectly (identical to Motor6D behavior). When `false`,
the constraint applies forces and torques limited by
[MaxForce](/docs/reference/engine/classes/AnimationConstraint.md) and
[MaxTorque](/docs/reference/engine/classes/AnimationConstraint.md), enabling physically simulated
character movement.

## Properties

### Property: AnimationConstraint.AngularDamping

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
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

The damping ratio (ζ) applied to the rotational part of the constraint.
Only used if [IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is
`false`.

A value of `1` corresponds to **critical damping**, where the constraint
reaches its target orientation as fast as possible without overshoot in
the absence of other forces or constraints. Values less than `1` are
under-damped and oscillate around the target before settling. Values
greater than `1` are over-damped and approach the target more slowly
without oscillation. A value of `0` applies no angular damping, causing
the constraint to oscillate.

Even with this property set to `1`, an `AnimationConstraint` at the root
of a multi-body mechanism may still exhibit low-frequency oscillation
because it does not "see" the full effective mass of the downstream chain.
You can compensate by increasing both
[AngularStrength](/docs/reference/engine/classes/AnimationConstraint.md) and
`AngularDamping` beyond their defaults.

### Property: AnimationConstraint.AngularStrength

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
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

Controls how rigidly the constraint enforces the rotational part of its
target [Transform](/docs/reference/engine/classes/AnimationConstraint.md). Only used if
[IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is `false`. The
resulting torque is capped by
[MaxTorque](/docs/reference/engine/classes/AnimationConstraint.md).

`AngularStrength` is defined as a normalized natural frequency,
`AngularStrength = f / 60`, where `f` is the target natural frequency in
Hz. The default value of `1` corresponds to a target frequency of 60 Hz
and produces strong tracking of the target orientation. A value of `0`
applies no torque. Values less than `1` produce a softer, more compliant
rotational response, and values greater than `1` produce a stiffer
response.

Use values significantly greater than `1` with caution, as they may cause
the simulation to become unstable.

### Property: AnimationConstraint.IsKinematic

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
  "category": "Data",
  "capabilities": [
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

When `true`, the connected parts follow the
[Transform](/docs/reference/engine/classes/AnimationConstraint.md) perfectly without
participating in physics simulation. When `false`, the connected parts
follow the trajectory using forces and torques limited by
[MaxForce](/docs/reference/engine/classes/AnimationConstraint.md) and
[MaxTorque](/docs/reference/engine/classes/AnimationConstraint.md).

### Property: AnimationConstraint.LinearDamping

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
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

The damping ratio (ζ) applied to the translational part of the constraint.
Only used if [IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is
`false`.

A value of `1` corresponds to **critical damping**, where the constraint
reaches its target position as fast as possible without overshoot in the
absence of other forces or constraints. Values less than `1` are
under-damped and oscillate around the target before settling. Values
greater than `1` are over-damped and approach the target more slowly
without oscillation. A value of `0` applies no linear damping, causing the
constraint to oscillate.

`LinearDamping` has no effect when
[LinearStrength](/docs/reference/engine/classes/AnimationConstraint.md) is `0`.

### Property: AnimationConstraint.LinearStrength

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
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

Controls how rigidly the constraint enforces the translational part of its
target [Transform](/docs/reference/engine/classes/AnimationConstraint.md). Only used if
[IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is `false`. The
resulting force is capped by
[MaxForce](/docs/reference/engine/classes/AnimationConstraint.md).

`LinearStrength` uses the same normalized natural frequency definition as
[AngularStrength](/docs/reference/engine/classes/AnimationConstraint.md),
`LinearStrength = f / 60`, where `f` is the target natural frequency in
Hz. The default value of `1` corresponds to a target frequency of 60 Hz
and produces strong tracking of the target position. A value of `0`
applies no force. Values less than `1` produce a softer, more compliant
positional response, and values greater than `1` produce a stiffer
response.

Splitting angular and linear parameters lets you make orientation tracking
stiff while keeping positional tracking soft, or vice-versa. As with
[AngularStrength](/docs/reference/engine/classes/AnimationConstraint.md), use values
significantly greater than `1` with caution, as they may cause the
simulation to become unstable.

### Property: AnimationConstraint.MaxForce

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
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

Maximum force magnitude the constraint can apply to achieve its goal. Only
used if [IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is `false`.

### Property: AnimationConstraint.MaxTorque

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
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

Maximum torque the constraint can use to reach its goal. Only used if
[IsKinematic](/docs/reference/engine/classes/AnimationConstraint.md) is `false`.

### Property: AnimationConstraint.Transform

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
  "category": "Data",
  "capabilities": [
    "Physics",
    "Animation"
  ],
  "simulationAccess": true
}
```

The internal [CFrame](/docs/reference/engine/datatypes/CFrame.md) that is manipulated when the constraint is
being animated.

Note that `AnimationConstraint` transforms are not applied immediately,
but rather as a batch in a parallel job after
[RunService.PreSimulation](/docs/reference/engine/classes/RunService.md), immediately before physics steps. The
deferred batch update is much more efficient than many immediate updates.
If the `AnimationConstraint` is part of an animated model with an
[Animator](/docs/reference/engine/classes/Animator.md), then [Transform](/docs/reference/engine/classes/AnimationConstraint.md) is
usually overwritten every frame by the [Animator](/docs/reference/engine/classes/Animator.md) after
[RunService.PreAnimation](/docs/reference/engine/classes/RunService.md) and before
[RunService.PreSimulation](/docs/reference/engine/classes/RunService.md).

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