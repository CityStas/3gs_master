---
name: CollisionFidelity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines behavior of the collision hitbox for MeshPart and PartOperation instances."
---

# CollisionFidelity

Determines behavior of the collision hitbox for [MeshPart](/docs/reference/engine/classes/MeshPart.md) and
[PartOperation](/docs/reference/engine/classes/PartOperation.md) instances.

**Type:** enum

## Description

Determines behavior of the collision hitbox for [MeshPart](/docs/reference/engine/classes/MeshPart.md) and
[PartOperation](/docs/reference/engine/classes/PartOperation.md) instances. See
[here](/docs/en-us/workspace/collisions.md#collision-fidelity) for a visual
representation of the various options.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Collision model uses a voxel-based convex-hull decomposition that is relatively fast but may not be highly accurate, especially for holes, doorways, and cavities in general. |
| `Hull` | 1 | Collision model uses the convex hull of the visual mesh. |
| `Box` | 2 | Collision model uses a bounding box that encompasses the visual mesh. |
| `PreciseConvexDecomposition` | 3 | Collison model uses a convex-hull decomposition of the visual mesh which is computed by a variation of an algorithm called HACD. This option is the most accurate representation of collision geometry for complex objects with built-in tolerances to reduce the total number of convex-hulls by compromising on accuracy when justified. |
| `Tunable` | 4 | Collision model that supports precision tuning of convex decomposition fidelity. |