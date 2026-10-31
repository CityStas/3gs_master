---
name: RaycastResult
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Stores results from a raycast operation."
---

# RaycastResult

Stores results from a raycast operation.

**Type:** datatype

## Description

The [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md) data type stores the result of a successful
raycasting operation performed by [WorldRoot:Raycast()](/docs/reference/engine/classes/WorldRoot.md). It contains the
properties listed below.

This object should not be confused with the similarly-named
[RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) which is used to perform a raycast.

## Properties

### RaycastResult.Distance

**Type:** `number`

The distance between the ray origin and the intersection point.

### RaycastResult.Instance

**Type:** `BasePart`

The [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell that the ray intersected.

### RaycastResult.Material

**Type:** `Material`

The [Material](/docs/reference/engine/enums/Material.md) at the intersection point. For normal parts this is
the [BasePart.Material](/docs/reference/engine/classes/BasePart.md); for [Terrain](/docs/reference/engine/classes/Terrain.md) this can vary depending
on terrain data.

### RaycastResult.Position

**Type:** `Vector3`

The world space point at which the intersection occurred, usually a point
directly on the surface of the [BasePart](/docs/reference/engine/classes/BasePart.md) or [Terrain](/docs/reference/engine/classes/Terrain.md) cell.

### RaycastResult.Normal

**Type:** `Vector3`

The normal vector of the intersected face.