---
name: NumberSequenceKeypoint
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Represents keypoint within a NumberSequence with a particular time, value, and envelope size."
---

# NumberSequenceKeypoint

Represents keypoint within a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) with a particular time,
value, and envelope size.

**Type:** datatype

## Description

The [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) data type represents keypoints within a
NumberSequence with a particular time, value, and envelope size.

## Constructors

### NumberSequenceKeypoint.new

**Signature:** `NumberSequenceKeypoint.new(time: number, value: number)`

Returns a [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) with the given `time` and
`value`, with [Envelope](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md)
defaulting to 0 (no random variance). The `time` parameter should be a
number between 0 and 1, and `value` can be any number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` |  | The relative time position of the keypoint within the sequence, expressed as a number from 0 to 1. |
| `value` | `number` |  | The base numeric value at this keypoint's time position. |

### NumberSequenceKeypoint.new

**Signature:** `NumberSequenceKeypoint.new(time: number, value: number, envelope: number)`

Returns a [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) with the given `time`,
`value`, and `envelope`. The `envelope` parameter must be a non-negative
number that defines the amount of random variance applied to `value` at
runtime; the actual output for this keypoint is chosen randomly within
[value&nbsp;&minus;&nbsp;envelope,&nbsp;value&nbsp;+&nbsp;envelope].

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `time` | `number` |  | The relative time position of the keypoint within the sequence, expressed as a number from 0 to 1. |
| `value` | `number` |  | The base numeric value at this keypoint's time position. |
| `envelope` | `number` |  | The amount of random variance that can be applied to the value at runtime; must be non-negative. |

## Properties

### NumberSequenceKeypoint.Envelope

**Type:** `number`

The amount of variance allowed from the value. For example, a value of 0.5
with an envelope of 0.1 could compute to between 0.4 and 0.6 at runtime.
The most common use case for this property is to randomize the size of
particles (within the envelope) from a
[ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md).

### NumberSequenceKeypoint.Time

**Type:** `number`

The relative time at which this keypoint is positioned within the parent
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md), expressed as a number from 0 to 1 where 0 is
the beginning of the sequence and 1 is the end. Within a
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md), the first keypoint must have a time of 0 and
the last keypoint must have a time of 1; any intermediate keypoints must
be in ascending time order. The engine linearly interpolates values and
envelopes between consecutive keypoints based on their time positions.
Defaults to 0.

### NumberSequenceKeypoint.Value

**Type:** `number`

The base numeric value at this keypoint's position in the sequence. When
the engine evaluates a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md), it linearly interpolates
between adjacent keypoints' values based on time. If
[Envelope](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) is greater than 0, the
actual output at runtime may vary randomly within the range
[Value&nbsp;&minus;&nbsp;Envelope,&nbsp;Value&nbsp;+&nbsp;Envelope].
Defaults to 0.