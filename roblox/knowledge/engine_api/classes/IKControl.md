---
name: IKControl
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "Specifies a control to generate a procedural animation pose using Inverse Kinematics."
---

# Class: IKControl

> Specifies a control to generate a procedural animation pose using Inverse
> Kinematics.

## Description

**IKControl** instances generate procedural animation poses using Inverse
Kinematics (IK). They allow you to make characters respond realistically to
their environment.

For example, you can make a character place its hand on a door handle exactly,
and the character will do so independently of its position.
[IKControls](/docs/reference/engine/classes/IKControl.md) provide the advantage of needing to create much
fewer animations for your game while giving your experience a more realistic
and polished feel.

[IKControls](/docs/reference/engine/classes/IKControl.md) must be a child of a [Humanoid](/docs/reference/engine/classes/Humanoid.md) or
[AnimationController](/docs/reference/engine/classes/AnimationController.md) with an [Animator](/docs/reference/engine/classes/Animator.md) and have all of their
required properties set properly, otherwise they don't have any effect. The
required properties are [Type](/docs/reference/engine/classes/IKControl.md),
[EndEffector](/docs/reference/engine/classes/IKControl.md), [Target](/docs/reference/engine/classes/IKControl.md),
[ChainRoot](/docs/reference/engine/classes/IKControl.md). As soon as those are set, the
[IKControl](/docs/reference/engine/classes/IKControl.md) modifies the pose of your character as you specify. The
following code sample demonstrates how to set up your first [IKControl](/docs/reference/engine/classes/IKControl.md)
and get started with creating more realistic animations for your game.

You can use [IKControls](/docs/reference/engine/classes/IKControl.md) to make a character:

- Rotate its head and torso to look at a point of interest in the world.
- Modify its feet positions to respond to dynamic terrain. Adjust its legs and
  feet to place them accordingly on terrain with rocks and slopes.
- Hold a gun and place its hands appropriately on the grip without needing to
  create animations for each gun in the game.
- Aim at a point in the world, so that the tip of the gun point exactly at
  what you want to shoot. Especially useful in third person shooters.
- Place its hands on the steering wheel of a car and follow it when it
  rotates.
- Much more!

[IKControl](/docs/reference/engine/classes/IKControl.md) will override the animation for all the parts between the
[ChainRoot](/docs/reference/engine/classes/IKControl.md) and the
[EndEffector](/docs/reference/engine/classes/IKControl.md). You can enable/disable it using
[Enabled](/docs/reference/engine/classes/IKControl.md) or change how much they have an effect over
the underlying animation using the [Weight](/docs/reference/engine/classes/IKControl.md). Be
careful: if you do not set up your [IKControls](/docs/reference/engine/classes/IKControl.md) correctly, you
might generate bad and unrealistic poses!

## Code Samples

**IKControl setup**

This sample shows the basic setup for an [IKControl](/docs/reference/engine/classes/IKControl.md) that moves a
character's left arm to reach for a point in the world.

```lua
local character = script.Parent.Character
local humanoid = character.Humanoid
local root = character.HumanoidRootPart

-- Create a new attachment to use as the IKControl.Target
local target = Instance.new("Attachment")
target.CFrame = CFrame.new(-1, 0, -1)
target.Parent = root

local ikControl = Instance.new("IKControl")
ikControl.Type = Enum.IKControlType.Position
ikControl.EndEffector = character.LeftHand
ikControl.ChainRoot = character.LeftUpperArm
ikControl.Target = target
ikControl.Parent = humanoid
```

## Properties

### Property: IKControl.ChainRoot

```json
{
  "type": "Instance",
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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

By specifying a [ChainRoot](/docs/reference/engine/classes/IKControl.md) and an
[EndEffector](/docs/reference/engine/classes/IKControl.md), you instruct the
[IKControl](/docs/reference/engine/classes/IKControl.md) that it's allowed to move and rotate all parts between
the two to move the [EndEffector](/docs/reference/engine/classes/IKControl.md) to the
[Target](/docs/reference/engine/classes/IKControl.md). For example, if you specify the LeftHand
as [EndEffector](/docs/reference/engine/classes/IKControl.md) and LeftUpperArm as the
[ChainRoot](/docs/reference/engine/classes/IKControl.md), the control moves 3 parts: the
LeftHand, the LeftLowerArm, and the LeftUpperArm. Avoid setting
[ChainRoot](/docs/reference/engine/classes/IKControl.md) as the actual root of the character
because that produces unrealistic results.

### Property: IKControl.Enabled

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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

This property allows you to toggle the IK control on and off. It's on by
default. When [Enabled](/docs/reference/engine/classes/IKControl.md) is false, the IK control
is off and isn't resolved by the underlying solver.

### Property: IKControl.EndEffector

```json
{
  "type": "Instance",
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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

The [EndEffector](/docs/reference/engine/classes/IKControl.md) describes the last part in
the chain of your character that you want to affect. For example, it could
be the hand when you want to move the whole arm to reach a point. It can
be a [BasePart](/docs/reference/engine/classes/BasePart.md) on a character, that has a [Motor6D](/docs/reference/engine/classes/Motor6D.md) as its
child, a [Motor6D](/docs/reference/engine/classes/Motor6D.md) directly, a [Bone](/docs/reference/engine/classes/Bone.md), or a
[Attachment](/docs/reference/engine/classes/Attachment.md). The pivot of the selected
[EndEffector](/docs/reference/engine/classes/IKControl.md) moves to the
[Target](/docs/reference/engine/classes/IKControl.md), so you can use
[Attachments](/docs/reference/engine/classes/Attachment.md) to modify which point of a [BasePart](/docs/reference/engine/classes/BasePart.md)
should reach the [Target](/docs/reference/engine/classes/IKControl.md).

### Property: IKControl.EndEffectorOffset

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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

The end-effector offset is an additional [CFrame](/docs/reference/engine/datatypes/CFrame.md) applied on top
of the [Target](/docs/reference/engine/classes/IKControl.md) [CFrame](/docs/reference/engine/datatypes/CFrame.md) that produces the
final [CFrame](/docs/reference/engine/datatypes/CFrame.md) used to place the
[EndEffector](/docs/reference/engine/classes/IKControl.md). By default, it's the identity
CFrame, so if you don't set it, it has no effect and the
[EndEffector](/docs/reference/engine/classes/IKControl.md) uses the
[Target](/docs/reference/engine/classes/IKControl.md) [CFrame](/docs/reference/engine/datatypes/CFrame.md) directly, which is
specified in the local space of the
[EndEffector](/docs/reference/engine/classes/IKControl.md).

Alternatively, you can use Attachments by setting an Attachment as
[EndEffector](/docs/reference/engine/classes/IKControl.md), which moves it to the
[Target](/docs/reference/engine/classes/IKControl.md) instead of the parts it's attached to,
effectively obtaining the same result.

You can also use [EndEffectorOffset](/docs/reference/engine/classes/IKControl.md) to
modify which axis of the [EndEffector](/docs/reference/engine/classes/IKControl.md) should
point at the [Target](/docs/reference/engine/classes/IKControl.md) when using `LookAt` as
[Type](/docs/reference/engine/classes/IKControl.md).

### Property: IKControl.Offset

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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

The offset is an additional [CFrame](/docs/reference/engine/datatypes/CFrame.md) applied on top of the
[Target](/docs/reference/engine/classes/IKControl.md) [CFrame](/docs/reference/engine/datatypes/CFrame.md) that produces the final
[CFrame](/docs/reference/engine/datatypes/CFrame.md) used to place the
[EndEffector](/docs/reference/engine/classes/IKControl.md). It's identity by default, so if
you don't set it, it has no effect and the
[EndEffector](/docs/reference/engine/classes/IKControl.md) will use the
[Target](/docs/reference/engine/classes/IKControl.md) [CFrame](/docs/reference/engine/datatypes/CFrame.md) directly. You can
animate it to create procedural animations such as typing on a keyboard.
It's useful when the [Target](/docs/reference/engine/classes/IKControl.md) and
[EndEffector](/docs/reference/engine/classes/IKControl.md) aren't aligned and you need to
fix it with an additional rotation or translation.

### Property: IKControl.Pole

```json
{
  "type": "Instance",
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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

The [Pole](/docs/reference/engine/classes/IKControl.md) is an optional [Instance](/docs/reference/engine/classes/Instance.md) that gives
you control over how intermediate parts in your character should bend. It
can be anything that has a position in the world, such as
[BasePart](/docs/reference/engine/classes/BasePart.md), [Attachment](/docs/reference/engine/classes/Attachment.md), [Bone](/docs/reference/engine/classes/Bone.md), [Motor6D](/docs/reference/engine/classes/Motor6D.md). It is
by default `nil`. When you specify it, the underlying solver will make the
parts bend towards it. When it is `nil`, the solver will try to make
elbows and knees bend appropriately based on the limb of the character.
The limb will be "Arm" when you select as
[EndEffector](/docs/reference/engine/classes/IKControl.md) either the _LeftHand_ or
_RightHand_ and as [ChainRoot](/docs/reference/engine/classes/IKControl.md) the corresponding
_LeftUpperArm_ or _RightUpperArm_, and it will be "Leg" when you select as
[EndEffector](/docs/reference/engine/classes/IKControl.md) either the _LeftFoot_ or
_RightFoot_ and as [ChainRoot](/docs/reference/engine/classes/IKControl.md) the corresponding
_LeftUpperLeg_ or _RightUpperLeg_. In all other cases, if you don't
specify a pole, the chain might not bend as you expect.

### Property: IKControl.Priority

```json
{
  "type": "int",
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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

When multiple controls are active on a character, the order in which they
are solved by the underlying system affects the final generated pose. By
changing this value, you specify the ordering in which controls are
satisfied. Higher values have higher priority, and higher-priority
controls are resolved later because their result might override the
previous result of other controls. If you have multiple IK controls on a
character and one is more important than the other, specify a lower
priority for it. It is 0 by default, meaning all controls have the same
priority.

### Property: IKControl.SmoothTime

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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ]
}
```

This value specifies the average number of seconds that it takes for the
[EndEffector](/docs/reference/engine/classes/IKControl.md) to reach the
[Target](/docs/reference/engine/classes/IKControl.md). The behavior is that of a
critically-damped spring, where the rate of change is proportional to the
distance to the target and no oscillations are present when approaching
the target. Smaller values create a quicker convergence, and larger values
create a slower convergence. A value of 0 disables smoothing. The default
value is 0.05 to provide a very slight smoothing that makes the motion
feel realistic.

### Property: IKControl.Target

```json
{
  "type": "Instance",
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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

The [Target](/docs/reference/engine/classes/IKControl.md) represents a point ([CFrame](/docs/reference/engine/datatypes/CFrame.md))
in the world that you want your [EndEffector](/docs/reference/engine/classes/IKControl.md)
to reach. The exact behavior of reaching can be set via the
[Type](/docs/reference/engine/classes/IKControl.md) property, and an additional
[Offset](/docs/reference/engine/classes/IKControl.md) can be applied on top of it to modify it.
If you set a [Target](/docs/reference/engine/classes/IKControl.md) that will be moved either by
physics or a script, at each frame the [IKControl](/docs/reference/engine/classes/IKControl.md) will try to
satisfy it, automatically updating the point to reach.

### Property: IKControl.Type

```json
{
  "type": "IKControlType",
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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

By changing the [Type](/docs/reference/engine/classes/IKControl.md), you can change the behavior
of the control. These are the available options:

- Transform: it's a full 6-DoF constraint. Aligns the
  [EndEffector](/docs/reference/engine/classes/IKControl.md) [CFrame](/docs/reference/engine/datatypes/CFrame.md) to that of
  the [Target](/docs/reference/engine/classes/IKControl.md).
- Position: aligns the [EndEffector](/docs/reference/engine/classes/IKControl.md) position
  to that of the [Target](/docs/reference/engine/classes/IKControl.md).
- Rotation: aligns the [EndEffector](/docs/reference/engine/classes/IKControl.md) rotation
  to that of the [Target](/docs/reference/engine/classes/IKControl.md).
- LookAt: moves and orients the whole chain to make an axis (by default
  the forward axis) on the [EndEffector](/docs/reference/engine/classes/IKControl.md) point
  at a position in the world specified by [Target](/docs/reference/engine/classes/IKControl.md).

### Property: IKControl.Weight

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
  "category": "Behavior",
  "capabilities": [
    "Animation"
  ],
  "simulationAccess": true
}
```

You can control how much a given control affects the character pose by
using this property. Values should be in the [0, 1] range. 0 means no
effect, and 1 means full effect of the IK control. Values outside this
range are truncated. Smoothly varying this value allows you to blend in or
out a specific control to avoid jarring motion. It is 1 by default.

The weight determines the interpolation factor between the End-Effector
and the IK target. Setting the weight to 0 doesn't disable the IK Control
because other factors, including the SmoothTime smoothing factor and Pole,
can still change the pose. To truly disable the IK Control, turn the
[Enabled](/docs/reference/engine/classes/IKControl.md) property to false.

## Methods

### Method: IKControl:GetChainCount

**Signature:** `IKControl:GetChainCount(): int`

Returns the number of segments in the IK chain, meaning the number of
parent-child links between the [ChainRoot](/docs/reference/engine/classes/IKControl.md) and
the [EndEffector](/docs/reference/engine/classes/IKControl.md). A chain of three parts has
a count of `2`.

The chain always has one more node than it has segments, so the valid
indices for [GetNodeWorldCFrame()](/docs/reference/engine/classes/IKControl.md)
and [GetNodeLocalCFrame()](/docs/reference/engine/classes/IKControl.md) range from
`1` to the returned count plus `1`. This returns `0` when the
[IKControl](/docs/reference/engine/classes/IKControl.md) doesn't resolve to a valid chain, such as when its
required properties aren't set.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `int` — The number of segments in the chain, or `0` if the chain isn't valid.

### Method: IKControl:GetChainLength

**Signature:** `IKControl:GetChainLength(): float`

Returns the total length of the IK chain in studs, computed as the sum of
the world-space distances between each consecutive part from the
[EndEffector](/docs/reference/engine/classes/IKControl.md) up to the
[ChainRoot](/docs/reference/engine/classes/IKControl.md). This is the maximum reach of the
chain: a [Target](/docs/reference/engine/classes/IKControl.md) placed farther than this distance
from the chain's base can't be reached, and the chain extends toward it as
far as it can.

This returns `0` when the [IKControl](/docs/reference/engine/classes/IKControl.md) doesn't resolve to a valid
chain, such as when its required properties aren't set.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `float` — The combined length of the chain in studs, or `0` if the chain isn't
valid.

### Method: IKControl:GetNodeLocalCFrame

**Signature:** `IKControl:GetNodeLocalCFrame(index: int): CFrame`

Returns the [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the node at the given `index` in the
solved IK chain, relative to its parent node. Nodes are ordered from the
[ChainRoot](/docs/reference/engine/classes/IKControl.md) at index `1` to the
[EndEffector](/docs/reference/engine/classes/IKControl.md) at
[GetChainCount()](/docs/reference/engine/classes/IKControl.md) plus `1`.

This reflects the pose most recently produced by the solver. Use
[GetNodeWorldCFrame()](/docs/reference/engine/classes/IKControl.md) for the same
node in world space. If the `index` is outside the valid range, or the
[IKControl](/docs/reference/engine/classes/IKControl.md) hasn't resolved a valid chain, this returns the identity
[CFrame](/docs/reference/engine/datatypes/CFrame.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The 1-based position of the node in the chain, from `1` (the [ChainRoot](/docs/reference/engine/classes/IKControl.md)) up to [GetChainCount()](/docs/reference/engine/classes/IKControl.md) plus `1` (the [EndEffector](/docs/reference/engine/classes/IKControl.md)). |

**Returns:** `CFrame` — The node's [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the local space of its parent node, or
the identity [CFrame](/docs/reference/engine/datatypes/CFrame.md) if the index is out of range or the
chain hasn't been solved.

### Method: IKControl:GetNodeWorldCFrame

**Signature:** `IKControl:GetNodeWorldCFrame(index: int): CFrame`

Returns the world-space [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the node at the given `index`
in the solved IK chain. Nodes are ordered from the
[ChainRoot](/docs/reference/engine/classes/IKControl.md) at index `1` to the
[EndEffector](/docs/reference/engine/classes/IKControl.md) at
[GetChainCount()](/docs/reference/engine/classes/IKControl.md) plus `1`.

This reflects the pose most recently produced by the solver. Use
[GetNodeLocalCFrame()](/docs/reference/engine/classes/IKControl.md) for the same
node relative to its parent. If the `index` is outside the valid range, or
the [IKControl](/docs/reference/engine/classes/IKControl.md) hasn't resolved a valid chain, this returns the
identity [CFrame](/docs/reference/engine/datatypes/CFrame.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The 1-based position of the node in the chain, from `1` (the [ChainRoot](/docs/reference/engine/classes/IKControl.md)) up to [GetChainCount()](/docs/reference/engine/classes/IKControl.md) plus `1` (the [EndEffector](/docs/reference/engine/classes/IKControl.md)). |

**Returns:** `CFrame` — The node's world-space [CFrame](/docs/reference/engine/datatypes/CFrame.md), or the identity
[CFrame](/docs/reference/engine/datatypes/CFrame.md) if the index is out of range or the chain hasn't
been solved.

### Method: IKControl:GetRawFinalTarget

**Signature:** `IKControl:GetRawFinalTarget(): CFrame`

Returns the [CFrame](/docs/reference/engine/datatypes/CFrame.md) that the solver aims the
[EndEffector](/docs/reference/engine/classes/IKControl.md) at on the current frame, before
[SmoothTime](/docs/reference/engine/classes/IKControl.md) smoothing is applied. This is the
[Target](/docs/reference/engine/classes/IKControl.md) after [Weight](/docs/reference/engine/classes/IKControl.md),
[Offset](/docs/reference/engine/classes/IKControl.md), and
[EndEffectorOffset](/docs/reference/engine/classes/IKControl.md) are factored in. For
a `LookAt` [Type](/docs/reference/engine/classes/IKControl.md), it's the world position the chain
is oriented toward.

Compare with
[GetSmoothedFinalTarget()](/docs/reference/engine/classes/IKControl.md), which
returns the same target after smoothing. The two are equal when
[SmoothTime](/docs/reference/engine/classes/IKControl.md) is `0`.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `CFrame` — The final target [CFrame](/docs/reference/engine/datatypes/CFrame.md), in world space, before smoothing.

### Method: IKControl:GetSmoothedFinalTarget

**Signature:** `IKControl:GetSmoothedFinalTarget(): CFrame`

Returns the [CFrame](/docs/reference/engine/datatypes/CFrame.md) that the solver aims the
[EndEffector](/docs/reference/engine/classes/IKControl.md) at on the current frame, after
[SmoothTime](/docs/reference/engine/classes/IKControl.md) smoothing has been applied to the
raw target from [GetRawFinalTarget()](/docs/reference/engine/classes/IKControl.md).
Smoothing uses a critically damped spring that eases toward the raw value
over roughly [SmoothTime](/docs/reference/engine/classes/IKControl.md) seconds.

Because [SmoothTime](/docs/reference/engine/classes/IKControl.md) defaults to `0.05`, this
value trails [GetRawFinalTarget()](/docs/reference/engine/classes/IKControl.md)
slightly while the target moves. When `SmoothTime` is `0`, this returns
the same [CFrame](/docs/reference/engine/datatypes/CFrame.md) as `GetRawFinalTarget`.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `CFrame` — The final target [CFrame](/docs/reference/engine/datatypes/CFrame.md), in world space, after smoothing.

## Inherited Members

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