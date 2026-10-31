---
name: RaycastParams
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A container for parameters used in raycasting operations."
---

# RaycastParams

A container for parameters used in raycasting operations.

**Type:** datatype

## Description

The [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) data type stores parameters for
[WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) operations. The
[ExcludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) properties store a
set of objects and their descendants that will be excluded and included from
the query. The [RaycastParams.IgnoreWater](/docs/reference/engine/datatypes/RaycastParams.md) property can be used to
ignore [Terrain](/docs/reference/engine/classes/Terrain.md) water, and the [RaycastParams.CollisionGroup](/docs/reference/engine/datatypes/RaycastParams.md)
property can specify a collision group for the raycasting operation.

This object is different from the similarly named [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md)
which provides the results of a raycast.

Unlike most data types in Luau, you can change all of the members of
[RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) without creating a new object, allowing you to reuse
the same object repeatedly.

## Constructors

### RaycastParams.new

**Signature:** `RaycastParams.new()`

Returns a blank [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) object. Unlike other data type
constructors, this constructor does not have any parameters, so you should
set its properties appropriately.

## Properties

### RaycastParams.ExcludeInstances

**Type:** `{Instance}?`

An optional array of instances whose descendants will be excluded from the
query. This property can be used simultaneously with
[IncludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) to allow for
mixed filtering, for example including a large folder but excluding
specific child instances. If an instance matches both an exclude and
include filter, exclusions take priority over inclusions.

### RaycastParams.IncludeInstances

**Type:** `{Instance}?`

An optional array of instances whose descendants will be included in the
query. This property can be used simultaneously with
[ExcludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) to allow for
mixed filtering. If an instance matches both an exclude and include
filter, exclusions take priority over inclusions.

Setting `IncludeInstances` to `nil` versus an empty array (`{}`) has
opposite effects. `IncludeInstances = nil` is the most permissive filter
(includes everything), whereas `IncludeInstances = {}` is the most
restrictive filter (includes nothing).

### RaycastParams.IgnoreWater

**Type:** `bool`

Determines whether the water material is considered when raycasting
against [Terrain](/docs/reference/engine/classes/Terrain.md).

### RaycastParams.CollisionGroup

**Type:** `string`

Specifies a collision group for the raycasting operation. Parts in
collision groups that are set to **not** collide with this group are
ignored. If this property is omitted, the raycast assumes the **Default**
collision group.

### RaycastParams.RespectCanCollide

**Type:** `bool`

This property, if `true`, makes the raycast operation use an intersected
part's [CanCollide](/docs/reference/engine/classes/BasePart.md) value in favor of its
[CanQuery](/docs/reference/engine/classes/BasePart.md) value when determining whether that
part is included in the [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md).

### RaycastParams.BruteForceAllSlow

**Type:** `bool`

When enabled, the query will ignore all part collision properties and
perform a brute-force check on every part. This will negatively impact
performance and should not be used in live experiences.

### RaycastParams.Margin

**Type:** `number`

Expands the cast shape uniformly in every direction. Must be finite and
greater than or equal to `0`. Defaults to `0`.

`Margin` applies to [WorldRoot:Shapecast()](/docs/reference/engine/classes/WorldRoot.md),
[WorldRoot:Blockcast()](/docs/reference/engine/classes/WorldRoot.md), [WorldRoot:Spherecast()](/docs/reference/engine/classes/WorldRoot.md) and
[WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md). The expanded shape is what the maximum-size
limit is checked against, so a large `Margin` can make an otherwise valid
cast throw.

Setting a non-zero `Margin` on a [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md) makes the
operation behave as a sphere cast of that radius.

### RaycastParams.SizeGradient

**Type:** `number`

Scales the cast shape over the length of the cast. Must be finite and
greater than or equal to `-1`. Defaults to `0`, which casts the shape at a
constant size.

The shape starts at its original size and is scaled by `1 + SizeGradient`
by the end of the cast, interpolating in between. A `SizeGradient` of
`0.5` finishes the cast 50% larger, `-0.5` finishes it at half size, and
`-1` shrinks it away entirely.

`SizeGradient` scales the shape's own size, not
[Margin](/docs/reference/engine/datatypes/RaycastParams.md), so a cast with both keeps its
margin at a constant width along the way. [WorldRoot:Spherecast()](/docs/reference/engine/classes/WorldRoot.md)
is the exception: radius and margin are one and the same for a sphere, so
both scale together.

### RaycastParams.FilterDescendantsInstances

**Type:** `Array`

An array of objects whose descendants are used to filter raycasting
candidates. Note that this property has been superseded by
[ExcludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) which should be
used for new work.

### RaycastParams.FilterType

**Type:** `RaycastFilterType`

Determines whether the
[FilterDescendantsInstances](/docs/reference/engine/datatypes/RaycastParams.md)
array is used as an exclude or include list. Note that this property has
been superseded by
[ExcludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) which should be
used for new work.

## Methods

### RaycastParams:AddToFilter

**Signature:** `RaycastParams:AddToFilter(instances: Instance | Array): ()`

Adds the instances provided to
[FilterDescendantsInstances](/docs/reference/engine/datatypes/RaycastParams.md).
Note that this property has been superseded by
[ExcludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/RaycastParams.md) which should be
used for new work.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instances` | `Instance | Array` |  | An instance or an array containing instances to add. |

**Returns:** `()`