---
name: SolverConvergenceVisualizationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether and at what granularity the physics solver's convergence quality is overlaid as a debug visualization in Studio."
---

# SolverConvergenceVisualizationMode

Controls whether and at what granularity the physics solver's convergence
quality is overlaid as a debug visualization in Studio.

**Type:** enum

## Description

Controls whether and at what granularity the physics solver's convergence
quality is overlaid as a 3D debug visualization in Roblox Studio. When active,
constraint edges connecting assembly root bodies are drawn as colored
cylinders; the worst-ranked edge within each simulation island is drawn in
red, while all remaining edges stay green. This visualization is only rendered
in Studio (not in published experiences). The metric used to rank convergence
is selected separately via
[PhysicsSettings.SolverConvergenceMetricType](/docs/reference/engine/classes/PhysicsSettings.md). Defaults to
[SolverConvergenceVisualizationMode.Disabled](/docs/reference/engine/enums/SolverConvergenceVisualizationMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Disabled` | 0 | No solver convergence visualization is rendered; the default state. |
| `PerIsland` | 1 | Renders a single convergence metric label at the center of each simulation island displaying the velocity-stage and position-stage maxima, which may come from different constraints. |
| `PerEdge` | 2 | Renders convergence metrics as text labels on each aggregated body-pair edge between assembly root bodies. |