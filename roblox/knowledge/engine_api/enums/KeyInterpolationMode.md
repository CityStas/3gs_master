---
name: KeyInterpolationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the interpolation method between two keys."
---

# KeyInterpolationMode

Describes the interpolation method between two keys.

**Type:** enum

## Description

Describes the interpolation method for a [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) or
[RotationCurve](/docs/reference/engine/classes/RotationCurve.md) segment between the key for which this mode is set and
the next key in the curve.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Constant` | 0 | The segment starting at this key will constantly evaluate to the value set at this key. |
| `Linear` | 1 | The segment starting at this key will evaluate using a linear interpolation at this key and the value at the next key. |
| `Cubic` | 2 | The segment starting at this key will evaluate using cubic interpolation of this key value using its right tangent and the next key value and its left tangent. |