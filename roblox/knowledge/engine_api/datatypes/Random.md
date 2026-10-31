---
name: Random
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Generates pseudorandom numbers and directions."
---

# Random

Generates pseudorandom numbers and directions.

**Type:** datatype

## Description

The [Random](/docs/reference/engine/datatypes/Random.md) data type generates pseudorandom numbers and directions.

## Constructors

### Random.new

**Signature:** `Random.new(seed: number)`

Returns a new [Random](/docs/reference/engine/datatypes/Random.md) object. If you don't provide the seed
parameter, [Random](/docs/reference/engine/datatypes/Random.md) uses a seed from an internal entropy source.

If you provide a seed, it should be within the range [-9007199254740991,
9007199254740991], and [Random](/docs/reference/engine/datatypes/Random.md) will round it down to the nearest
integer. So seeds of 0, 0.99, and [math.random()](/docs/reference/engine/globals/math.md) all produce
identical generators. If you need to generate a seed and store it for
later retrieval, use [math.random(max)](/docs/reference/engine/globals/math.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `seed` | `number` |  | An optional number that initializes the pseudorandom number generator's internal state, truncated toward zero to a whole number. Should be within the range [-9007199254740991, 9007199254740991]; values outside this range are clamped to 0. |

**Datatype.Random**

Generates a pseudorandom seed and uses it to create a new [Random](/docs/reference/engine/datatypes/Random.md)
generator.

```lua
local max = 2147483647 -- use a large integer
local seed = math.random(max)
local generator = Random.new(seed)
```

## Methods

### Random:NextInteger

**Signature:** `Random:NextInteger(min: number, max: number): number`

Returns a pseudorandom integer uniformly distributed over `[min, max]`,
inclusive of both endpoints. If `min` is greater than `max`, the two
values are swapped so the call still succeeds. Both arguments are
truncated toward zero to whole numbers before sampling.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `min` | `number` |  | The minimum integer value of the range (inclusive). Truncated toward zero to a whole number. |
| `max` | `number` |  | The maximum integer value of the range (inclusive). Truncated toward zero to a whole number. |

**Returns:** `number`

### Random:NextNumber

**Signature:** `Random:NextNumber(): number`

Returns a uniform pseudorandom real number in the range of 0 to 1,
inclusive.

**Returns:** `number` — A pseudorandom number uniformly distributed over [0, 1].

### Random:NextNumber

**Signature:** `Random:NextNumber(min: number, max: number): number`

Returns a uniform pseudorandom real number in the range of `min` to `max`,
inclusive.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `min` | `number` |  | The minimum value of the range (inclusive). |
| `max` | `number` |  | The maximum value of the range (inclusive). |

**Returns:** `number` — A pseudorandom number uniformly distributed over [min, max].

### Random:Shuffle

**Signature:** `Random:Shuffle(tb: table): ()`

Uniformly shuffles the array part of `tb` in-place using `NextInteger` to
pick indices. If there are any `nil` "holes" in the array part of the
table, `Shuffle` throws an error, since shuffling could change the length.

The hash part of `tb` is ignored. No metamethods of `tb` are invoked.

The shuffle is defined to be a Fisher-Yates shuffle so the number of
`NextInteger` calls is guaranteed to be consistent between engine versions
for a given size of table.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tb` | `table` |  | The table whose array part is shuffled in-place. |

**Returns:** `()`

### Random:NextUnitVector

**Signature:** `Random:NextUnitVector(): Vector3`

Returns a unit vector with a pseudorandom direction. Vectors returned from
this function are uniformly distributed over the unit sphere.

**Returns:** `Vector3` — A unit vector with a pseudorandom direction.

### Random:Clone

**Signature:** `Random:Clone(): Random`

Returns a new [Random](/docs/reference/engine/datatypes/Random.md) object whose internal state is copied from
the original. After cloning, both the original and the clone produce the
same sequence of pseudorandom values going forward, but they advance
independently — consuming a value from one does not affect the other.

**Returns:** `Random` — A new Random object with the same internal state as the original.