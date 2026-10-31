---
name: FluidFidelity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the geometric representation used to compute aerodynamic forces."
---

# FluidFidelity

Determines the geometric representation used to compute aerodynamic forces.

**Type:** enum

## Description

Determines the geometric representation used to compute aerodynamic forces and
torques for [MeshPart](/docs/reference/engine/classes/MeshPart.md) and [PartOperation](/docs/reference/engine/classes/PartOperation.md) instances.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Let the physics engine select the geometric representation for aerodynamic force and torque calculations. |
| `UseCollisionGeometry` | 1 | Use the current collision geometry specified by [TriangleMeshPart.CollisionFidelity](/docs/reference/engine/classes/TriangleMeshPart.md) for aerodynamic force and torque calculations . |
| `UsePreciseGeometry` | 2 | Force the engine to compute aerodynamic forces and torques using a more precise geometry representation based on the original mesh. This option may increase join and replication time if used on a large scale. |