---
name: PhysicalProperties
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Describes properties that affect the physical behavior of a BasePart."
---

# PhysicalProperties

Describes properties that affect the physical behavior of a [BasePart](/docs/reference/engine/classes/BasePart.md).

**Type:** datatype

## Description

The [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) data type describes several physical
properties of a [BasePart](/docs/reference/engine/classes/BasePart.md):
[Density](/docs/reference/engine/datatypes/PhysicalProperties.md),
[Elasticity](/docs/reference/engine/datatypes/PhysicalProperties.md), and
[Friction](/docs/reference/engine/datatypes/PhysicalProperties.md). It is used in the
similarly-named [BasePart.CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md) property.

#### Weighting Behavior

[PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) also provides weightings properties,
[ElasticityWeight](/docs/reference/engine/datatypes/PhysicalProperties.md) and
[FrictionWeight](/docs/reference/engine/datatypes/PhysicalProperties.md). When two parts
interact, the friction and elasticity between them are determined in the same
way by the following pairwise weighted average function:

```lua
local function getActualFriction(partA, partB)
	return (partA.Friction * partA.FrictionWeight + partB.Friction * partB.FrictionWeight) / (partA.FrictionWeight + partB.FrictionWeight)
end
```

Although the formula above refers to the
[Friction](/docs/reference/engine/datatypes/PhysicalProperties.md) and
[FrictionWeight](/docs/reference/engine/datatypes/PhysicalProperties.md) of two parts,
**A** and **B**, the formula is used in the same manner when determining
[Elasticity](/docs/reference/engine/datatypes/PhysicalProperties.md). Generally, when the
weight of **A** is much greater than that of **B**, the actual value will be
closer to **A**. If the weights are similar, the actual value will be close to
the midpoint between their individual values.

## Constructors

### PhysicalProperties.new

**Signature:** `PhysicalProperties.new(material: Material)`

Returns a [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) container, with the density,
friction, and elasticity specified for this material.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `material` | `Material` |  | The [Material](/docs/reference/engine/enums/Material.md) for which to retrieve default physical properties. |

### PhysicalProperties.new

**Signature:** `PhysicalProperties.new(density: number, friction: number, elasticity: number)`

Returns a [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) container, with the specified
density, friction, and elasticity.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `density` | `number` |  | The mass per unit volume of the part, clamped to the range [0.0001, 100]. |
| `friction` | `number` |  | The coefficient of friction opposing sliding motion, clamped to [0, 2]. |
| `elasticity` | `number` |  | The coefficient of restitution (bounciness) applied on collision, clamped to [0, 1]. |

### PhysicalProperties.new

**Signature:** `PhysicalProperties.new(density: number, friction: number, elasticity: number, frictionWeight: number, elasticityWeight: number)`

Creates a [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) container with the specified
density, friction, elasticity, weight of friction, and weight of
elasticity.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `density` | `number` |  | The mass per unit volume of the part, clamped to the range [0.0001, 100]. |
| `friction` | `number` |  | The coefficient of friction opposing sliding motion, clamped to [0, 2]. |
| `elasticity` | `number` |  | The coefficient of restitution (bounciness) applied on collision, clamped to [0, 1]. |
| `frictionWeight` | `number` |  | The weight of this part's friction in the pairwise weighted average, clamped to [0, 100]. |
| `elasticityWeight` | `number` |  | The weight of this part's elasticity in the pairwise weighted average, clamped to [0, 100]. |

### PhysicalProperties.new

**Signature:** `PhysicalProperties.new(density: number, friction: number, elasticity: number, frictionWeight: number, elasticityWeight: number, acousticAbsorption: number)`

Creates a [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) container with the specified
density, friction, elasticity, weight of friction, weight of elasticity,
and acoustic absorption.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `density` | `number` |  | The mass per unit volume of the part, clamped to the range [0.0001, 100]. |
| `friction` | `number` |  | The coefficient of friction opposing sliding motion, clamped to [0, 2]. |
| `elasticity` | `number` |  | The coefficient of restitution (bounciness) applied on collision, clamped to [0, 1]. |
| `frictionWeight` | `number` |  | The weight of this part's friction in the pairwise weighted average, clamped to [0, 100]. |
| `elasticityWeight` | `number` |  | The weight of this part's elasticity in the pairwise weighted average, clamped to [0, 100]. |
| `acousticAbsorption` | `number` |  | How much sound energy the surface absorbs during acoustic simulation, clamped to [0, 1]. |

## Properties

### PhysicalProperties.AcousticAbsorption

**Type:** `number`

A value between `0` and `1` denoting how absorbent the material is to
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md). When using acoustic simulation,
surfaces with higher absorption will result in less reverb than surfaces
with lower absorption.

Note that this does not affect the degree to which audio transmits
**through** surfaces; for that, see
[Density](/docs/reference/engine/datatypes/PhysicalProperties.md).

### PhysicalProperties.Density

**Type:** `number`

Density is defined as the amount of mass per unit volume. The more dense a
part is, the more force it takes to accelerate it. Acceptable range is
`0.0001` to `100.0` and values outside this range will be clamped.

When using acoustic simulation, parts with higher density will muffle
occluded [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) more.

### PhysicalProperties.Friction

**Type:** `number`

Friction is defined as the force that opposes the relative lateral motion
of two solid surfaces in contact. The greater the friction on a part, the
quicker it will decelerate when it rubs against another part with
friction. Acceptable range is `0.0` to `2.0` and values outside this range
will be clamped.

### PhysicalProperties.Elasticity

**Type:** `number`

Elasticity refers to a part's tendency to retain energy when colliding
with another part. An [Elasticity](/docs/reference/engine/datatypes/PhysicalProperties.md)
of 1 indicates that the part bounces with the same energy it had before a
collision. Acceptable range is `0.0` to `1.0` and values outside this
range will be clamped.

### PhysicalProperties.FrictionWeight

**Type:** `number`

The friction weight of two parts rubbing together creates a ratio used to
calculate the actual friction between the two parts. The higher a part's
[FrictionWeight](/docs/reference/engine/datatypes/PhysicalProperties.md), the more its
[Friction](/docs/reference/engine/datatypes/PhysicalProperties.md) is used. Acceptable range
is `0.0` to `100.0` and values outside this range will be clamped.

### PhysicalProperties.ElasticityWeight

**Type:** `number`

The elasticity weight of two parts colliding creates a ratio used to
calculate the actual elasticity between the two parts. The higher a part's
[ElasticityWeight](/docs/reference/engine/datatypes/PhysicalProperties.md), the more
its [Elasticity](/docs/reference/engine/datatypes/PhysicalProperties.md) is used.
Acceptable range is `0.0` to `100.0` and values outside this range will be
clamped.