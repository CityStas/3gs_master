---
name: HumanoidRigDescription
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "Stores the joint mapping, T-pose, and per-joint properties for a 22-joint bipedal character rig. Joints may be AnimationConstraint, Motor6D, or Bone instances."
---

# Class: HumanoidRigDescription

> Stores the joint mapping, T-pose, and per-joint properties for a 22-joint
> bipedal character rig. Joints may be [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md),
> [Motor6D](/docs/reference/engine/classes/Motor6D.md), or [Bone](/docs/reference/engine/classes/Bone.md) instances.

## Description

Stores the joint mapping, reference T-pose and per-joint properties for a
bipedal `Humanoid` character rig. Each of the 22 joints in the rig hierarchy
can reference an `Instance` (typically a `Motor6D`, `AnimationConstraint` or
`Bone`), define a T-pose adjustment transform, rotation range limits, and
carry a size for volumetric visualization and retargeting. For an example
Blender and Maya rig hierarchy with all optional joints, see
[Character specifications - Advanced R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs).

Use `AutoRig` to automatically populate joint references from a character
model, or assign joints individually. Supports both R6 (6-joint) and R15
(15-joint) rig subsets in addition to the full 22-joint standard set, as well
as rigs with more than 22 joints by mapping the key subset of joints.

## Properties

### Property: HumanoidRigDescription.Chest

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the chest joint. This joint is the branch point for the neck
chain and both clavicle chains.

### Property: HumanoidRigDescription.ChestRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the chest joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.ChestRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the chest joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.ChestSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Size of the chest joint's volume sphere, used for rig visualization and
collision.

### Property: HumanoidRigDescription.ChestTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the chest joint to align it with
the T-pose reference orientation.

### Property: HumanoidRigDescription.HeadBase

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the head base joint. This is the terminal joint of the head
chain.

### Property: HumanoidRigDescription.HeadBaseRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the head base joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.HeadBaseRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the head base joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.HeadBaseSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the head base joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.HeadBaseTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the head base joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftAnkle

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left ankle joint.

### Property: HumanoidRigDescription.LeftAnkleRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left ankle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftAnkleRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left ankle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftAnkleSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left ankle joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftAnkleTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left ankle joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftClavicle

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left clavicle (collarbone) joint.

### Property: HumanoidRigDescription.LeftClavicleRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left clavicle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftClavicleRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left clavicle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftClavicleSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left clavicle joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftClavicleTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left clavicle joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftElbow

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left elbow joint.

### Property: HumanoidRigDescription.LeftElbowRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left elbow joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftElbowRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left elbow joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftElbowSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left elbow joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftElbowTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left elbow joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftHip

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left hip joint. This is the root of the left leg chain.

### Property: HumanoidRigDescription.LeftHipRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left hip joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftHipRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left hip joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftHipSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left hip joint's volume sphere, used for rig visualization
and collision.

### Property: HumanoidRigDescription.LeftHipTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left hip joint to align it with
the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftKnee

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left knee joint.

### Property: HumanoidRigDescription.LeftKneeRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left knee joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftKneeRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left knee joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftKneeSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left knee joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftKneeTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left knee joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftShoulder

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left shoulder joint.

### Property: HumanoidRigDescription.LeftShoulderRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left shoulder joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftShoulderRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left shoulder joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftShoulderSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left shoulder joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftShoulderTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left shoulder joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftToeBase

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left toe base joint. This is the terminal joint of the
left leg chain.

### Property: HumanoidRigDescription.LeftToeBaseRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left toe base joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftToeBaseRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left toe base joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftToeBaseSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left toe base joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftToeBaseTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left toe base joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.LeftWrist

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the left wrist joint. This is the terminal joint of the left
arm chain.

### Property: HumanoidRigDescription.LeftWristRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the left wrist joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftWristRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the left wrist joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.LeftWristSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the left wrist joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.LeftWristTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the left wrist joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.Neck

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the neck joint.

### Property: HumanoidRigDescription.NeckRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the neck joint along each local axis
(X, Y, Z).

### Property: HumanoidRigDescription.NeckRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the neck joint along each local axis
(X, Y, Z).

### Property: HumanoidRigDescription.NeckSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the neck joint's volume sphere, used for rig visualization and
collision.

### Property: HumanoidRigDescription.NeckTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the neck joint to align it with the
T-pose reference orientation.

### Property: HumanoidRigDescription.OriginOffset

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
    "Animation",
    "PluginOrOpenCloud"
  ]
}
```

Coordinate frame offset of the rig origin relative to the character
model's primary part. Adjusts where the rig hierarchy is anchored within
the character.

### Property: HumanoidRigDescription.RightAnkle

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right ankle joint.

### Property: HumanoidRigDescription.RightAnkleRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right ankle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightAnkleRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right ankle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightAnkleSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right ankle joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightAnkleTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right ankle joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightClavicle

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right clavicle (collarbone) joint.

### Property: HumanoidRigDescription.RightClavicleRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right clavicle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightClavicleRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right clavicle joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightClavicleSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right clavicle joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightClavicleTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right clavicle joint to align
it with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightElbow

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right elbow joint.

### Property: HumanoidRigDescription.RightElbowRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right elbow joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightElbowRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right elbow joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightElbowSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right elbow joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightElbowTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right elbow joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightHip

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right hip joint. This is the root of the right leg chain.

### Property: HumanoidRigDescription.RightHipRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right hip joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.RightHipRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right hip joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.RightHipSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right hip joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightHipTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right hip joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightKnee

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right knee joint.

### Property: HumanoidRigDescription.RightKneeRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right knee joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightKneeRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right knee joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightKneeSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right knee joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightKneeTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right knee joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightShoulder

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right shoulder joint.

### Property: HumanoidRigDescription.RightShoulderRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right shoulder joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightShoulderRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right shoulder joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightShoulderSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right shoulder joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightShoulderTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right shoulder joint to align
it with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightToeBase

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right toe base joint. This is the terminal joint of the
right leg chain.

### Property: HumanoidRigDescription.RightToeBaseRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right toe base joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightToeBaseRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right toe base joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightToeBaseSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right toe base joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightToeBaseTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right toe base joint to align
it with the T-pose reference orientation.

### Property: HumanoidRigDescription.RightWrist

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the right wrist joint. This is the terminal joint of the
right arm chain.

### Property: HumanoidRigDescription.RightWristRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the right wrist joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightWristRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the right wrist joint along each
local axis (X, Y, Z).

### Property: HumanoidRigDescription.RightWristSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the right wrist joint's volume sphere, used for rig
visualization and collision.

### Property: HumanoidRigDescription.RightWristTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the right wrist joint to align it
with the T-pose reference orientation.

### Property: HumanoidRigDescription.Root

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the root joint, which is the base of the entire rig
hierarchy. The waist, left hip, and right hip chains all originate from
this joint.

### Property: HumanoidRigDescription.RootRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the root joint along each local axis
(X, Y, Z).

### Property: HumanoidRigDescription.RootRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the root joint along each local axis
(X, Y, Z).

### Property: HumanoidRigDescription.RootSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the root joint's volume sphere, used for rig visualization and
collision.

### Property: HumanoidRigDescription.RootTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the root joint to align it with the
T-pose reference orientation.

### Property: HumanoidRigDescription.Spine

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the spine joint.

### Property: HumanoidRigDescription.SpineRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the spine joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.SpineRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the spine joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.SpineSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the spine joint's volume sphere, used for rig visualization
and collision.

### Property: HumanoidRigDescription.SpineTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the spine joint to align it with
the T-pose reference orientation.

### Property: HumanoidRigDescription.Waist

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
  "category": "Mapping",
  "capabilities": [
    "Animation"
  ]
}
```

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) joint
instance for the waist joint.

### Property: HumanoidRigDescription.WaistRangeMax

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Maximum rotation range in degrees for the waist joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.WaistRangeMin

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
  "category": "Range",
  "capabilities": [
    "Animation"
  ]
}
```

Minimum rotation range in degrees for the waist joint along each local
axis (X, Y, Z).

### Property: HumanoidRigDescription.WaistSize

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
  "category": "Size",
  "capabilities": [
    "Animation"
  ]
}
```

Diameter of the waist joint's volume sphere, used for rig visualization
and collision.

### Property: HumanoidRigDescription.WaistTposeAdjustment

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
  "category": "Tpose",
  "capabilities": [
    "Animation"
  ]
}
```

Coordinate frame adjustment applied to the waist joint to align it with
the T-pose reference orientation.

## Methods

### Method: HumanoidRigDescription:GetJointFromName

**Signature:** `HumanoidRigDescription:GetJointFromName(name: string): Instance`

Returns the joint instance associated with the given joint name. Accepts
both standard joint names (e.g., `"LeftShoulder"`) and R15 body part names
(e.g., `"LeftLowerLeg"`). Name matching is case-insensitive. Returns `nil`
if no joint with the given name is mapped.

*Security: None · Thread Safety: Safe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | string |

**Returns:** `Instance` — Instance

### Method: HumanoidRigDescription:GetJointNames

**Signature:** `HumanoidRigDescription:GetJointNames(): Array`

Returns an array of all 22 standard joint name strings for this rig
description, in hierarchy order: Root, Waist, Spine, Chest, Neck,
HeadBase, LeftClavicle, LeftShoulder, LeftElbow, LeftWrist, RightClavicle,
RightShoulder, RightElbow, RightWrist, LeftHip, LeftKnee, LeftAnkle,
LeftToeBase, RightHip, RightKnee, RightAnkle, RightToeBase.

*Security: None · Thread Safety: Safe · Capabilities: Animation*

**Returns:** `Array` — Array

### Method: HumanoidRigDescription:GetR15JointNames

**Signature:** `HumanoidRigDescription:GetR15JointNames(): Array`

Returns an array of the 15 joint name strings used by R15 rigs: Root,
Waist, Neck, LeftShoulder, LeftElbow, LeftWrist, RightShoulder,
RightElbow, RightWrist, LeftHip, LeftKnee, LeftAnkle, RightHip, RightKnee,
RightAnkle.

*Security: None · Thread Safety: Safe · Capabilities: Animation*

**Returns:** `Array` — Array

### Method: HumanoidRigDescription:GetR6JointNames

**Signature:** `HumanoidRigDescription:GetR6JointNames(): Array`

Returns an array of the 6 joint name strings used by R6 rigs: Root, Neck,
LeftShoulder, RightShoulder, LeftHip, RightHip.

*Security: None · Thread Safety: Safe · Capabilities: Animation*

**Returns:** `Array` — Array

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