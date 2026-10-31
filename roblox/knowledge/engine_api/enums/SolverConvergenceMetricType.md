---
name: SolverConvergenceMetricType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the metric used to identify the least-converged constraint when visualizing physics solver convergence."
---

# SolverConvergenceMetricType

Specifies the metric used to identify the least-converged constraint when
visualizing physics solver convergence.

**Type:** enum

## Description

Specifies the metric used to determine which constraint is least converged
within a solver island when
[PhysicsSettings.SolverConvergenceVisualizationMode](/docs/reference/engine/classes/PhysicsSettings.md) is active. The
selected metric controls what data is gathered per constraint and displayed in
the per-edge and per-island overlay. The default value, stored on
[PhysicsSettings.SolverConvergenceMetricType](/docs/reference/engine/classes/PhysicsSettings.md), is
[SolverConvergenceMetricType.AlgorithmAgnostic](/docs/reference/engine/enums/SolverConvergenceMetricType.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `IterationBased` | 0 | Identifies the least-converged constraint using the estimated force change from an additional, non-applied solver iteration. |
| `AlgorithmAgnostic` | 1 | Identifies the least-converged constraint using a residual-based convergence metric supported across solver algorithms. |