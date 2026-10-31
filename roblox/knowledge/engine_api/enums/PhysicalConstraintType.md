---
name: PhysicalConstraintType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the type of physical joint created when importing a rigged asset."
---

# PhysicalConstraintType

Specifies the type of physical joint created when importing a rigged asset.

**Type:** enum

## Description

Controls which joint class connects bones in an imported rig skeleton.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AnimationConstraint` | 0 | Import creates [AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md) instances to connect the rig's bone joints. |
| `Motor6D` | 1 | Import creates [Motor6D](/docs/reference/engine/classes/Motor6D.md) instances to connect the rig's bone joints. |