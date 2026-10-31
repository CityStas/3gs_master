---
name: RotationCurveKey
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A time-value pair used with RotationCurve instances."
---

# RotationCurveKey

A time-value pair used with [RotationCurve](/docs/reference/engine/classes/RotationCurve.md) instances.

**Type:** datatype

## Description

A time-value pair used with [RotationCurve](/docs/reference/engine/classes/RotationCurve.md) instances.

The [Interpolation](/docs/reference/engine/datatypes/RotationCurveKey.md) property dictates
the interpolation mode for the segment started by this key and ended by the
next key on the curve. Each segment may use a different interpolation mode.

The [LeftTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) and
[RightTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) properties apply to the
cubic interpolation mode and define the desired tangent (slope) at the key.
Different left and right values can be used to encode discontinuities in slope
at the key. Attempting to set a
[RightTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) value on a key that
doesn't use the cubic interpolation mode will result in a runtime error. It is
possible to set the [LeftTangent](/docs/reference/engine/datatypes/RotationCurveKey.md)
property on any key, as it will be used should the preceding segment use cubic
interpolation.

## Constructors

### RotationCurveKey.new

**Signature:** `RotationCurveKey.new(time: number, cframe: CFrame, Interpolation: KeyInterpolationMode)`

Creates a new [RotationCurveKey](/docs/reference/engine/datatypes/RotationCurveKey.md) at a given time with a given
[CFrame](/docs/reference/engine/datatypes/CFrame.md). [LeftTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) and
[RightTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) are left
uninitialized and, if not initialized, tangent values of 0 will be used
when evaluating the curve.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` |  | Time at which to create the new [RotationCurveKey](/docs/reference/engine/datatypes/RotationCurveKey.md). |
| `cframe` | `CFrame` |  | [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the new [RotationCurveKey](/docs/reference/engine/datatypes/RotationCurveKey.md). |
| `Interpolation` | `KeyInterpolationMode` |  | The interpolation mode for the segment started by this key. Defaults to [KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md). |

## Properties

### RotationCurveKey.Interpolation

**Type:** `KeyInterpolationMode`

Defines the interpolation mode used for the curve segment that begins at
this key and ends at the next key. Possible values are
[KeyInterpolationMode.Constant](/docs/reference/engine/enums/KeyInterpolationMode.md) (holds the key's value until the next
key), [KeyInterpolationMode.Linear](/docs/reference/engine/enums/KeyInterpolationMode.md) (linearly interpolates between
this key and the next using spherical linear interpolation), and
[KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md) (uses a cubic hermite spline shaped by
[RightTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) and the next key's
[LeftTangent](/docs/reference/engine/datatypes/RotationCurveKey.md)). Defaults to
[KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md).

Setting this property to a non-cubic mode automatically clears
[RightTangent](/docs/reference/engine/datatypes/RotationCurveKey.md) (because tangent
slope is only meaningful in cubic segments).

### RotationCurveKey.Time

**Type:** `number`

The time position of this [RotationCurveKey](/docs/reference/engine/datatypes/RotationCurveKey.md) along the curve's
timeline, in seconds. Keys within a [RotationCurve](/docs/reference/engine/classes/RotationCurve.md) are kept sorted
by ascending time; inserting a key at the same time as an existing key
replaces the existing key. Defaults to `0`.

### RotationCurveKey.Value

**Type:** `CFrame`

The rotation stored at this key, represented as a [CFrame](/docs/reference/engine/datatypes/CFrame.md). Only
the rotational component of the CFrame is used; the positional component
is ignored. Defaults to [CFrame.identity](/docs/reference/engine/datatypes/CFrame.md).

### RotationCurveKey.RightTangent

**Type:** `number`

The outgoing tangent (slope) at this key, controlling the shape of the
cubic segment that extends toward the next key. Defaults to `0`. This
property can only be set when
[Interpolation](/docs/reference/engine/datatypes/RotationCurveKey.md) is
[KeyInterpolationMode.Cubic](/docs/reference/engine/enums/KeyInterpolationMode.md); attempting to set it on a key with a
different interpolation mode raises a runtime error. Returns `nil` if the
tangent has not been explicitly assigned.

### RotationCurveKey.LeftTangent

**Type:** `number`

The incoming tangent (slope) at this key, controlling the shape of the
cubic segment arriving from the previous key. Defaults to `0`. Unlike
[RightTangent](/docs/reference/engine/datatypes/RotationCurveKey.md), this property can
be set on a key regardless of its own interpolation mode, because the
preceding segment may use cubic interpolation and needs a defined slope at
its endpoint. Returns `nil` if the tangent has not been explicitly
assigned.