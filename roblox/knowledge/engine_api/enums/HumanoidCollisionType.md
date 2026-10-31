---
name: HumanoidCollisionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The collision Humanoid uses."
---

# HumanoidCollisionType

The collision [Humanoid](/docs/reference/engine/classes/Humanoid.md) uses.

**Type:** enum

## Description

Enum to select the [Humanoid.CollisionType](/docs/reference/engine/classes/Humanoid.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OuterBox` | 0 | Dynamically sized collision boxes based on mesh sizes. |
| `InnerBox` | 1 | Fixed size collision boxes, similar to the classic avatar collision. |