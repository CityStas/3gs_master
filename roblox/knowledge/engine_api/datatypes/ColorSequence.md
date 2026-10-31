---
name: ColorSequence
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A gradient of color values comprised of ColorSequenceKeypoints."
---

# ColorSequence

A gradient of color values comprised of
[ColorSequenceKeypoints](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md).

**Type:** datatype

## Description

The [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) data type represents a gradient of color values
from `0` to `1`. The color values are expressed using the
[ColorSequenceKeypoint](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) type. This type is used in various properties
of [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md), [Trail](/docs/reference/engine/classes/Trail.md), [Beam](/docs/reference/engine/classes/Beam.md), and other objects
that use color gradients.

#### Equality

Two [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) objects are equivalent only if the values of
their [ColorSequenceKeypoint](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) are equivalent, even if both would
result in similar gradients.

#### Evaluation

The [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) type does not have a built-in method for getting
the value at a certain time/point. However, you can use the following function
to evaluate at a specific time.

```lua
local function evalColorSequence(sequence: ColorSequence, time: number)
    -- If time is 0 or 1, return the first or last value respectively
    if time == 0 then
        return sequence.Keypoints[1].Value
    elseif time == 1 then
        return sequence.Keypoints[#sequence.Keypoints].Value
    end

    -- Otherwise, step through each sequential pair of keypoints
    for i = 1, #sequence.Keypoints - 1 do
        local thisKeypoint = sequence.Keypoints[i]
        local nextKeypoint = sequence.Keypoints[i + 1]
        if time >= thisKeypoint.Time and time < nextKeypoint.Time then
            -- Calculate how far alpha lies between the points
            local alpha = (time - thisKeypoint.Time) / (nextKeypoint.Time - thisKeypoint.Time)
            -- Evaluate the real value between the points using alpha
            return Color3.new(
                (nextKeypoint.Value.R - thisKeypoint.Value.R) * alpha + thisKeypoint.Value.R,
                (nextKeypoint.Value.G - thisKeypoint.Value.G) * alpha + thisKeypoint.Value.G,
                (nextKeypoint.Value.B - thisKeypoint.Value.B) * alpha + thisKeypoint.Value.B
            )
        end
    end
end

local colorSequence = ColorSequence.new{
    ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 0, 0)),
    ColorSequenceKeypoint.new(0.5, Color3.fromRGB(0, 190, 200)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(190, 0, 255))
}

print(evalColorSequence(colorSequence, 0.75))  --> 0.372549, 0.372549, 0.892157
```

## Constructors

### ColorSequence.new

**Signature:** `ColorSequence.new(c: Color3)`

Returns a sequence of two keypoints with `c` for both the start and end
values.

```lua
local colorSequence = ColorSequence.new(c)
-- Equivalent to
local colorSequence = ColorSequence.new{
    ColorSequenceKeypoint.new(0, c),
    ColorSequenceKeypoint.new(1, c)
}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `c` | `Color3` |  | The [Color3](/docs/reference/engine/datatypes/Color3.md) value used for both the start and end of the sequence. |

### ColorSequence.new

**Signature:** `ColorSequence.new(c0: Color3, c1: Color3)`

Returns a new [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) with `c0` as the start value and
`c1` as the end value.

```lua
local colorSequence = ColorSequence.new(c0, c1)
-- Equivalent to
local colorSequence = ColorSequence.new{
    ColorSequenceKeypoint.new(0, c0),
    ColorSequenceKeypoint.new(1, c1)
}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `c0` | `Color3` |  | The [Color3](/docs/reference/engine/datatypes/Color3.md) value at the start of the sequence (time 0). |
| `c1` | `Color3` |  | The [Color3](/docs/reference/engine/datatypes/Color3.md) value at the end of the sequence (time 1). |

### ColorSequence.new

**Signature:** `ColorSequence.new(keypoints: Array)`

Returns a new [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) from an array of
[ColorSequenceKeypoints](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md). The keypoints
must be in a non-descending time value order. At least two keypoints must
be provided, and they must have a time value of `0` (first) and `1`
(last).

```lua
local red = Color3.fromRGB(255, 0, 0)
local cyan = Color3.fromRGB(0, 190, 200)
local purple = Color3.fromRGB(190, 0, 255)

local colorSequence = ColorSequence.new{
    ColorSequenceKeypoint.new(0, red),
    ColorSequenceKeypoint.new(0.5, cyan),
    ColorSequenceKeypoint.new(1, purple)
}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keypoints` | `Array` |  | An array of [ColorSequenceKeypoint](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) values ordered by non-descending time, starting at time 0 and ending at time 1. Must contain at least 2 and no more than 20 keypoints. |

## Properties

### ColorSequence.Keypoints

**Type:** `Array`

An array containing [ColorSequenceKeypoint](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) values for the
[ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md).