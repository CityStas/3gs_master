---
name: NumberSequence
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A series of floats across a period of time."
---

# NumberSequence

A series of floats across a period of time.

**Type:** datatype

## Description

The [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) data type represents a series of number values
from `0` to `1`. The number values are expressed using the
[NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) type. This type is used in properties such
as [ParticleEmitter.Size](/docs/reference/engine/classes/ParticleEmitter.md) and [Beam.Transparency](/docs/reference/engine/classes/Beam.md) to define a
numerical change over time.

#### Equality

Two [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) objects are equivalent only if the values of
their [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) are equivalent, even if both would
result in similar graphs.

#### Evaluation

The [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) type does not have a built-in method for getting
the value at a certain time/point because keypoints can have random envelopes.
However, assuming the envelope values of your keypoints are all `0`, you can
use the following function to evaluate at a specific time.

```lua
local function evalNumberSequence(sequence: NumberSequence, time: number)
    -- If time is 0 or 1, return the first or last value respectively
    if time == 0 then
        return sequence.Keypoints[1].Value
    elseif time == 1 then
        return sequence.Keypoints[#sequence.Keypoints].Value
    end

    -- Otherwise, step through each sequential pair of keypoints
    for i = 1, #sequence.Keypoints - 1 do
        local currKeypoint = sequence.Keypoints[i]
        local nextKeypoint = sequence.Keypoints[i + 1]
        if time >= currKeypoint.Time and time < nextKeypoint.Time then
            -- Calculate how far alpha lies between the points
            local alpha = (time - currKeypoint.Time) / (nextKeypoint.Time - currKeypoint.Time)
            -- Return the value between the points using alpha
            return currKeypoint.Value + (nextKeypoint.Value - currKeypoint.Value) * alpha
        end
    end
end

local numberSequence = NumberSequence.new{
    NumberSequenceKeypoint.new(0, 0),
    NumberSequenceKeypoint.new(0.5, 1),
    NumberSequenceKeypoint.new(1, 0),
}

print(evalNumberSequence(numberSequence, 0.65))  --> 0.7
```

## Constructors

### NumberSequence.new

**Signature:** `NumberSequence.new(n: number)`

Returns a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) with the start and end values set to
the provided `n`.

```lua
local numberSequence = NumberSequence.new(n)
-- Equivalent to
local numberSequence = NumberSequence.new{
    NumberSequenceKeypoint.new(0, n),
    NumberSequenceKeypoint.new(1, n)
}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `n` | `number` |  | The constant value used for both the start and end keypoints of the sequence. |

### NumberSequence.new

**Signature:** `NumberSequence.new(n0: number, n1: number)`

Returns a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) of two keypoints with `n0` as the
start value and `n1` as the end value.

```lua
local numberSequence = NumberSequence.new(n0, n1)
-- Equivalent to
local numberSequence = NumberSequence.new{
    NumberSequenceKeypoint.new(0, n0),
    NumberSequenceKeypoint.new(1, n1)
}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `n0` | `number` |  | The value at the start of the sequence (time 0). |
| `n1` | `number` |  | The value at the end of the sequence (time 1). |

### NumberSequence.new

**Signature:** `NumberSequence.new(Keypoints: Array)`

Returns a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) from an array of
[NumberSequenceKeypoints](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md). The keypoints
must be provided in a non-descending time value order. At least two
keypoints must be provided, and they must have a time value of `0` (first)
and `1` (last).

```lua
local numberSequence = NumberSequence.new{
    NumberSequenceKeypoint.new(0, 0),
    NumberSequenceKeypoint.new(0.5, 0.5, 0.25),
    NumberSequenceKeypoint.new(1, 1)
}
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `Keypoints` | `Array` |  | An array of [NumberSequenceKeypoints](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) ordered by non-descending time, starting at time 0 and ending at time 1, with a maximum of 20 keypoints. |

## Properties

### NumberSequence.Keypoints

**Type:** `Array`

An array containing [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) values for the
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md).