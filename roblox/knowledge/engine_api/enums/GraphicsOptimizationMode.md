---
name: GraphicsOptimizationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the player's preferred trade-off between rendering quality and frame rate when using manual graphics quality."
---

# GraphicsOptimizationMode

Specifies the player's preferred trade-off between rendering quality and frame
rate when using manual graphics quality.

**Type:** enum

## Description

Preferred trade-off between visual quality and performance for
[UserGameSettings.GraphicsOptimizationMode](/docs/reference/engine/classes/UserGameSettings.md) when the player uses
**manual** graphics quality. This setting has no effect when graphics quality
is automatic. Defaults to [GraphicsOptimizationMode.Balanced](/docs/reference/engine/enums/GraphicsOptimizationMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Performance` | 0 | Prefers frame rate over visual fidelity, corresponding to manual render quality levels 1–3. |
| `Balanced` | 1 | Middle-ground preference, corresponding to manual render quality levels 4–7. This is the default of [UserGameSettings.GraphicsOptimizationMode](/docs/reference/engine/classes/UserGameSettings.md). |
| `Quality` | 2 | Prefers visual fidelity over frame rate, corresponding to manual render quality levels 8–10. |