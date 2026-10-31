---
name: PhysicsSteppingMethod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the physics engine advances simulation time for assemblies in a Workspace."
---

# PhysicsSteppingMethod

Controls how the physics engine advances simulation time for assemblies in a
[Workspace](/docs/reference/engine/classes/Workspace.md).

**Type:** enum

## Description

The `PhysicsSteppingMethod` enum determines the timestep arbiter strategy used
by the physics engine for all simulated assemblies in a place. It is set via
the [Workspace.PhysicsSteppingMethod](/docs/reference/engine/classes/Workspace.md) property. The default value is
[PhysicsSteppingMethod.Default](/docs/reference/engine/enums/PhysicsSteppingMethod.md), which currently resolves to the same
behavior as [PhysicsSteppingMethod.Adaptive](/docs/reference/engine/enums/PhysicsSteppingMethod.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The current default is `Adaptive`. |
| `Fixed` | 1 | All simulated assemblies inside the workspace will advance forward at 240 Hz. This option is best for optimal stability and simulation accuracy. |
| `Adaptive` | 2 | The engine attempts to assign optimal simulation rates for individual assemblies of either 240 Hz, 120 Hz, or 60 Hz. This setting is optimized for performance. |