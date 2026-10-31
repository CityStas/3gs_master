---
name: DigitsRigDescription
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
summary: "Maps the 15 phalanx joints of one hand (5 fingers, 3 joints each) and exposes forward- and inverse-kinematics helpers for controlling finger poses at runtime."
---

# Class: DigitsRigDescription

> Maps the 15 phalanx joints of one hand (5 fingers, 3 joints each) and exposes
> forward- and inverse-kinematics helpers for controlling finger poses at
> runtime.

## Description

Enables interoperability of animations across hand rigs and drives the hand
finger solver. Each `DigitsRigDescription` maps the 15 phalanx joints of one
hand (5 fingers with 3 joints each) to engine instances, stores their T-pose
adjustments, and exposes forward- and inverse-kinematics helpers for
controlling finger poses at runtime.

## Properties

### Property: DigitsRigDescription.Index1

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

The [Motor6D](/docs/reference/engine/classes/Motor6D.md), [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md), or [Bone](/docs/reference/engine/classes/Bone.md) instance
mapped to the proximal (first) phalanx of the index finger.

### Property: DigitsRigDescription.Index1TposeAdjustment

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

`CoordinateFrame` applied to `Index1` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Index2

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

The `Instance` mapped to the medial (second) phalanx of the index finger.

### Property: DigitsRigDescription.Index2TposeAdjustment

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

`CoordinateFrame` applied to `Index2` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Index3

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

The `Instance` mapped to the distal (third) phalanx of the index finger.

### Property: DigitsRigDescription.Index3TposeAdjustment

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

`CoordinateFrame` applied to `Index3` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.IndexRange

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

A `Vector3` describing the motion range of the index finger, used by the
finger solver.

### Property: DigitsRigDescription.IndexSize

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

Size of the index finger, used by the finger solver to preserve contacts.

### Property: DigitsRigDescription.Middle1

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

The `Instance` mapped to the proximal (first) phalanx of the middle
finger.

### Property: DigitsRigDescription.Middle1TposeAdjustment

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

`CoordinateFrame` applied to `Middle1` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Middle2

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

The `Instance` mapped to the medial (second) phalanx of the middle finger.

### Property: DigitsRigDescription.Middle2TposeAdjustment

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

`CoordinateFrame` applied to `Middle2` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Middle3

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

The `Instance` mapped to the distal (third) phalanx of the middle finger.

### Property: DigitsRigDescription.Middle3TposeAdjustment

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

`CoordinateFrame` applied to `Middle3` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.MiddleRange

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

A `Vector3` describing the motion range of the middle finger, used by the
finger solver and scalable-property system.

### Property: DigitsRigDescription.MiddleSize

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

Scale factor for the middle finger, used when the rig is scaled through
the scalable-property system.

### Property: DigitsRigDescription.Pinky1

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

The `Instance` mapped to the proximal (first) phalanx of the pinky finger.

### Property: DigitsRigDescription.Pinky1TposeAdjustment

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

`CoordinateFrame` applied to `Pinky1` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Pinky2

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

The `Instance` mapped to the medial (second) phalanx of the pinky finger.

### Property: DigitsRigDescription.Pinky2TposeAdjustment

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

`CoordinateFrame` applied to `Pinky2` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Pinky3

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

The `Instance` mapped to the distal (third) phalanx of the pinky finger.

### Property: DigitsRigDescription.Pinky3TposeAdjustment

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

`CoordinateFrame` applied to `Pinky3` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.PinkyRange

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

A `Vector3` describing the motion range of the pinky finger, used by the
finger solver and scalable-property system.

### Property: DigitsRigDescription.PinkySize

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

Scale factor for the pinky finger, used when the rig is scaled through the
scalable-property system.

### Property: DigitsRigDescription.Ring1

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

The `Instance` mapped to the proximal (first) phalanx of the ring finger.

### Property: DigitsRigDescription.Ring1TposeAdjustment

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

`CoordinateFrame` applied to `Ring1` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Ring2

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

The `Instance` mapped to the medial (second) phalanx of the ring finger.

### Property: DigitsRigDescription.Ring2TposeAdjustment

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

`CoordinateFrame` applied to `Ring2` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Ring3

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

The `Instance` mapped to the distal (third) phalanx of the ring finger.

### Property: DigitsRigDescription.Ring3TposeAdjustment

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

`CoordinateFrame` applied to `Ring3` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.RingRange

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

A `Vector3` describing the motion range of the ring finger, used by the
finger solver and scalable-property system.

### Property: DigitsRigDescription.RingSize

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

Scale factor for the ring finger, used when the rig is scaled through the
scalable-property system.

### Property: DigitsRigDescription.Side

```json
{
  "type": "DigitsRigDescriptionSide",
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
    "Animation"
  ]
}
```

Which hand this description belongs to: `None`, `Left`, or `Right`. Used
when mapping `HandRigLabel` joints to the corresponding `HumanoidRigLabel`
entries on the parent `HumanoidRigDescription`.

### Property: DigitsRigDescription.Thumb1

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

The `Instance` mapped to the proximal (first) phalanx of the thumb.

### Property: DigitsRigDescription.Thumb1TposeAdjustment

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

`CoordinateFrame` applied to `Thumb1` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Thumb2

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

The `Instance` mapped to the medial (second) phalanx of the thumb.

### Property: DigitsRigDescription.Thumb2TposeAdjustment

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

`CoordinateFrame` applied to `Thumb2` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.Thumb3

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

The `Instance` mapped to the distal (third) phalanx of the thumb.

### Property: DigitsRigDescription.Thumb3TposeAdjustment

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

`CoordinateFrame` applied to `Thumb3` to normalize the joint into its
canonical T-pose orientation before retargeting or solving.

### Property: DigitsRigDescription.ThumbRange

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

A `Vector3` describing the motion range of the thumb, used by the finger
solver and scalable-property system.

### Property: DigitsRigDescription.ThumbSize

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

Scale factor for the thumb, used when the rig is scaled through the
scalable-property system.

## Methods

### Method: DigitsRigDescription:GetFingerControl

**Signature:** `DigitsRigDescription:GetFingerControl(fingerIndex: int): Vector3`

Returns the current control `Vector3` for the finger at the given 1-based
index (1 = Thumb … 5 = Pinky). The components are:

- **X** — extension in `[0, 1]`: `0` is fully curled, `1` is fully
  extended.
- **Y** — lateral (side) rotation in `[-1, 1]`.
- **Z** — axial (twist) rotation in `[-1, 1]`.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fingerIndex` | `int` |  | 1-based index of the finger to query (1 = Thumb, 2 = Index, 3 = Middle, 4 = Ring, 5 = Pinky). |

**Returns:** `Vector3` — The control [Vector3](/docs/reference/engine/datatypes/Vector3.md) whose X is extension [0, 1], Y is
lateral rotation [-1, 1], and Z is axial rotation [-1, 1].

### Method: DigitsRigDescription:GetFingerTip

**Signature:** `DigitsRigDescription:GetFingerTip(fingerIndex: int): Vector3`

Returns the world-space position of the fingertip for the finger at the
given 1-based index (1 = Thumb … 5 = Pinky). Currently always returns
`Vector3.zero`.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fingerIndex` | `int` |  | 1-based index of the finger to query (1 = Thumb, 2 = Index, 3 = Middle, 4 = Ring, 5 = Pinky). |

**Returns:** `Vector3` — The world-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) position of the fingertip.
Currently always returns [Vector3.zero](/docs/reference/engine/datatypes/Vector3.md).

### Method: DigitsRigDescription:SetFingerControl

**Signature:** `DigitsRigDescription:SetFingerControl(fingerIndex: int, control: Vector3): ()`

Drives the three-joint chain of the finger at the given 1-based index (1 =
Thumb … 5 = Pinky) using forward kinematics. The `control` components are
clamped before application:

- **X** — extension, clamped to `[0, 1]`.
- **Y** — lateral rotation, clamped to `[-1, 1]` (maps to ±50°).
- **Z** — axial rotation, clamped to `[-1, 1]` (maps to ±50°).

Joint angles for the three phalanges are computed via Ptolemy's theorem
applied to the chain lengths.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fingerIndex` | `int` |  | 1-based index of the finger to drive (1 = Thumb, 2 = Index, 3 = Middle, 4 = Ring, 5 = Pinky). |
| `control` | `Vector3` |  | A [Vector3](/docs/reference/engine/datatypes/Vector3.md) whose X sets extension [0, 1], Y sets lateral rotation [-1, 1], and Z sets axial rotation [-1, 1]; each component is clamped before application. |

**Returns:** `()` — void

### Method: DigitsRigDescription:SetFingerTip

**Signature:** `DigitsRigDescription:SetFingerTip(fingerIndex: int, point: Vector3): ()`

Moves the fingertip of the finger at the given 1-based index (1 = Thumb …
5 = Pinky) toward the world-space target `point` using inverse kinematics.
The solver computes the required extension, lateral, and axial control
values and then calls `SetFingerControl` internally.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fingerIndex` | `int` |  | 1-based index of the finger to solve (1 = Thumb, 2 = Index, 3 = Middle, 4 = Ring, 5 = Pinky). |
| `point` | `Vector3` |  | World-space [Vector3](/docs/reference/engine/datatypes/Vector3.md) target position for the fingertip. |

**Returns:** `()` — void

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