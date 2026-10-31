---
name: ColorSequenceKeypoint
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A color and time value that represents a keypoint in a ColorSequence."
---

# ColorSequenceKeypoint

A color and time value that represents a keypoint in a
[ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md).

**Type:** datatype

## Description

The [ColorSequenceKeypoint](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) data type represents a single keypoint in
a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md). Each keypoint has a time position between `0` and
`1` and a [Color3](/docs/reference/engine/datatypes/Color3.md) value that defines the color at that point in the
sequence. Properties that use a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), such as
[ParticleEmitter.Color](/docs/reference/engine/classes/ParticleEmitter.md), [Beam.Color](/docs/reference/engine/classes/Beam.md), and [Trail.Color](/docs/reference/engine/classes/Trail.md),
interpolate linearly between consecutive keypoints in RGB color space.

```lua
local keypoints = {
    ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 0, 0)),
    ColorSequenceKeypoint.new(0.5, Color3.fromRGB(0, 255, 0)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(0, 0, 255)),
}
local colorSequence = ColorSequence.new(keypoints)
```

## Constructors

### ColorSequenceKeypoint.new

**Signature:** `ColorSequenceKeypoint.new(time: number, color: Color3)`

Returns a [ColorSequenceKeypoint](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) with the given `time` and
`color`. The `time` parameter should be a number between 0 and 1, where 0
represents the beginning of the sequence and 1 represents the end. The
`color` parameter is a [Color3](/docs/reference/engine/datatypes/Color3.md) whose components must each be
between 0 and 1.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` |  | The position of the keypoint along the sequence, a number between 0 and 1. |
| `color` | `Color3` |  | The color value at this keypoint. |

## Properties

### ColorSequenceKeypoint.Time

**Type:** `number`

The relative time at which this keypoint is positioned within the parent
[ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), expressed as a number from 0 to 1 where 0 is the
beginning of the sequence and 1 is the end. Within a
[ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), the first keypoint must have a time of 0 and the
last keypoint must have a time of 1; any intermediate keypoints must be in
ascending time order. The engine linearly interpolates colors between
consecutive keypoints in RGB color space based on their time positions.
Defaults to 0.

### ColorSequenceKeypoint.Value

**Type:** `Color3`

The [Color3](/docs/reference/engine/datatypes/Color3.md) color value at this keypoint's position in the
sequence. When the engine evaluates a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), it
linearly interpolates between adjacent keypoints' color values in RGB
color space based on time. Each component of the color (red, green, blue)
must be between 0 and 1. Defaults to (0, 0, 0) (black).