---
name: RotationOrder
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The order of rotation axes used for Euler angles encoding of rotations."
---

# RotationOrder

The order of rotation axes used for Euler angles encoding of rotations.

**Type:** enum

## Description

Euler angles encode a rotation in 3D space via a sequence of three rotations
along the X, Y, and Z axes. The `RotationOrder` enum specifies the order in
which the engine performs these rotations.

To help visualize the many rotation orders, you can test them manually in
Studio with the [Rotate](/docs/en-us/parts.md#rotate) tool or by inserting
[task.wait()](/docs/reference/engine/globals/task.md) statements between individual rotations of a cube with a
unique face:

```lua
local cube = Instance.new("Part")
cube.Shape = Enum.PartType.Block
local rx, ry, rz = math.rad(90), math.rad(90), math.rad(90)

task.wait(5)
cube.CFrame *= CFrame.fromEulerAngles(rx, 0, 0)  -- X
task.wait(5)
cube.CFrame *= CFrame.fromEulerAngles(0, ry, 0)  -- Y
task.wait(5)
cube.CFrame *= CFrame.fromEulerAngles(0, 0, rz)  -- Z
```

An equivalent operation is:

```lua
local cube = Instance.new("Part")
cube.Shape = Enum.PartType.Block
local rx, ry, rz = math.rad(90), math.rad(90), math.rad(90)

cube.CFrame = CFrame.fromEulerAngles(rx, ry, rz, Enum.RotationOrder.XYZ)
```

## Items

| Name | Value | Description |
|------|-------|-------------|
| `XYZ` | 0 | X, Y, Z order. |
| `XZY` | 1 | X, Z, Y order. |
| `YZX` | 2 | Y, Z, X order. |
| `YXZ` | 3 | Y, X, Z order. |
| `ZXY` | 4 | Z, X, Y order. |
| `ZYX` | 5 | Z, Y, X order. |