---
name: EnviromentalPhysicsThrottle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to control the throttle rate of Roblox's physics engine."
---

# EnviromentalPhysicsThrottle

Used to control the throttle rate of Roblox's physics engine.

**Type:** enum

## Description

The `EnviromentalPhysicsThrottle` enum is used with
[PhysicsSettings.PhysicsEnvironmentalThrottle](/docs/reference/engine/classes/PhysicsSettings.md), controlling how
aggressively the engine skips physics simulation steps to reduce CPU load.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `DefaultAuto` | 0 | Automatically adjusts throttle level based on performance. |
| `Disabled` | 1 | No throttling; every physics step runs. |
| `Always` | 2 | Maximum throttling; physics is effectively frozen. |
| `Skip2` | 3 | Runs 1 out of every 2 steps (50% reduction). If [Workspace.PhysicsSteppingMethod](/docs/reference/engine/classes/Workspace.md) is set to [Adaptive](/docs/reference/engine/enums/PhysicsSteppingMethod.md), skipping is based on groups of 4 steps instead of individual steps. |
| `Skip4` | 4 | Runs 1 out of every 4 steps (75% reduction). If [Workspace.PhysicsSteppingMethod](/docs/reference/engine/classes/Workspace.md) is set to [Adaptive](/docs/reference/engine/enums/PhysicsSteppingMethod.md), skipping is based on groups of 4 steps instead of individual steps. |
| `Skip8` | 5 | Runs 1 out of every 8 steps (87.5% reduction). If [Workspace.PhysicsSteppingMethod](/docs/reference/engine/classes/Workspace.md) is set to [Adaptive](/docs/reference/engine/enums/PhysicsSteppingMethod.md), skipping is based on groups of 4 steps instead of individual steps. |
| `Skip16` | 6 | Runs 1 out of every 16 steps (93.75% reduction). If [Workspace.PhysicsSteppingMethod](/docs/reference/engine/classes/Workspace.md) is set to [Adaptive](/docs/reference/engine/enums/PhysicsSteppingMethod.md), skipping is based on groups of 4 steps instead of individual steps. |