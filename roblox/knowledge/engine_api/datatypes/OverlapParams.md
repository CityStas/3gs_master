---
name: OverlapParams
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Stores parameters used in boundary-querying functions."
---

# OverlapParams

Stores parameters used in boundary-querying functions.

**Type:** datatype

## Description

The [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) data type stores parameters for use with
[WorldRoot](/docs/reference/engine/classes/WorldRoot.md) boundary-querying functions, in particular
[WorldRoot:GetPartBoundsInBox()](/docs/reference/engine/classes/WorldRoot.md),
[WorldRoot:GetPartBoundsInRadius()](/docs/reference/engine/classes/WorldRoot.md) and
[WorldRoot:GetPartsInPart()](/docs/reference/engine/classes/WorldRoot.md). The
[ExcludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) properties store a
set of objects and their descendants that will be excluded and included from
the query. The [OverlapParams.CollisionGroup](/docs/reference/engine/datatypes/OverlapParams.md) property can specify a
collision group for the boundary query operation.

Unlike most data types in Luau, you can change all of the members of
[OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) without creating a new object, allowing you to reuse
the same object repeatedly.

## Constructors

### OverlapParams.new

**Signature:** `OverlapParams.new()`

Returns a blank [OverlapParams](/docs/reference/engine/datatypes/OverlapParams.md) object. Unlike other data type
constructors, this constructor does not have any parameters, so you should
set its properties appropriately.

## Properties

### OverlapParams.ExcludeInstances

**Type:** `{Instance}?`

An optional array of instances whose descendants will be excluded from the
query. This property can be used simultaneously with
[IncludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) to allow for
mixed filtering, for example including a large folder but excluding
specific child instances. If an instance matches both an exclude and
include filter, exclusions take priority over inclusions.

### OverlapParams.IncludeInstances

**Type:** `{Instance}?`

An optional array of instances whose descendants will be included in the
query. This property can be used simultaneously with
[ExcludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) to allow for
mixed filtering. If an instance matches both an exclude and include
filter, exclusions take priority over inclusions.

Setting `IncludeInstances` to `nil` versus an empty array (`{}`) has
opposite effects. `IncludeInstances = nil` is the most permissive filter
(includes everything), whereas `IncludeInstances = {}` is the most
restrictive filter (includes nothing).

### OverlapParams.MaxParts

**Type:** `number`

The maximum amount of parts to be returned by the query. The default value
of zero (`0`) represents no limit.

### OverlapParams.CollisionGroup

**Type:** `string`

Specifies a collision group for the operation. Parts in collision groups
that are set to **not** collide with this group are ignored. If this
property is omitted, the operation assumes the **Default** collision
group.

### OverlapParams.Tolerance

**Type:** `number`

Slightly increases the volume of the boundary-querying operation, clamped
between `0` and `0.05` studs.

### OverlapParams.RespectCanCollide

**Type:** `bool`

This property, if `true`, makes the boundary-querying operation use an
intersected part's [BasePart.CanCollide](/docs/reference/engine/classes/BasePart.md) value in favor of its
[BasePart.CanQuery](/docs/reference/engine/classes/BasePart.md) value when determining whether that part is
included in the array of spatial query results.

### OverlapParams.BruteForceAllSlow

**Type:** `bool`

When enabled, the query will ignore all part collision properties and
perform a brute-force check on every part. This will negatively impact
performance and should not be used in live experiences.

### OverlapParams.FilterDescendantsInstances

**Type:** `Array`

An array of objects whose descendants are used in filtering candidates.
Note that this property has been superseded by
[ExcludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) which should be
used for new work.

### OverlapParams.FilterType

**Type:** `RaycastFilterType`

Determines whether the
[FilterDescendantsInstances](/docs/reference/engine/datatypes/OverlapParams.md)
array is used as an exclude or include list. Note that this property has
been superseded by
[ExcludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) which should be
used for new work.

## Methods

### OverlapParams:AddToFilter

**Signature:** `OverlapParams:AddToFilter(instances: Instance | Array): ()`

Adds the instances provided to
[FilterDescendantsInstances](/docs/reference/engine/datatypes/OverlapParams.md).
Note that this property has been superseded by
[ExcludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) and
[IncludeInstances](/docs/reference/engine/datatypes/OverlapParams.md) which should be
used for new work.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instances` | `Instance | Array` |  | An instance or an array containing instances to add. |

**Returns:** `()`