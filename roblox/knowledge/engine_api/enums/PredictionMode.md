---
name: PredictionMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used with RunService:SetPredictionMode() to define the prediction mode for the instance."
---

# PredictionMode

Enum used with [RunService:SetPredictionMode()](/docs/reference/engine/classes/RunService.md) to define the prediction
mode for the instance.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | The engine will automatically decide if this instance should be predicted or not. Currently, only [BaseParts](/docs/reference/engine/classes/BasePart.md) near the local player character's [Humanoid](/docs/reference/engine/classes/Humanoid.md) will be predicted within a dynamic radius that grows and shrinks based on the device's capability to handle the simulation load. |
| `On` | 1 | The instance will be predicted. Mismatches in the attributes of this instance between the client and server will cause a rollback and resimulation. If the instance is a [BasePart](/docs/reference/engine/classes/BasePart.md), its physics properties will be predicted ahead of the replicated authoritative server state. |
| `Off` | 2 | The instance will **not** be predicted. Regular network ownership semantics apply. |