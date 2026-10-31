---
name: MoveState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Represents the state of a SkateboardPlatform."
---

# MoveState

Represents the state of a [SkateboardPlatform](/docs/reference/engine/classes/SkateboardPlatform.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Stopped` | 0 | Skateboard is stopped (not moving). |
| `Coasting` | 1 | Skateboard is coasting (not actively speeding up / being pushed). |
| `Pushing` | 2 | Skateboard is being pushed (speeding up). |
| `Stopping` | 3 | Skateboard is stopping, but still moving. |
| `AirFree` | 4 | Skateboard is in the air. |