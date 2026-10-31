---
name: HumanoidDisplayDistanceType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "HumanoidDisplayDistanceType determines how Humanoid.HealthDisplayDistance, and Humanoid.NameDisplayDistance are used in determining whether a players's name and health are visible to other players."
---

# HumanoidDisplayDistanceType

HumanoidDisplayDistanceType determines how
[Humanoid.HealthDisplayDistance](/docs/reference/engine/classes/Humanoid.md), and
[Humanoid.NameDisplayDistance](/docs/reference/engine/classes/Humanoid.md) are used in determining whether a
players's name and health are visible to other players.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Viewer` | 0 | A player selecting `Viewer` on their [Humanoid](/docs/reference/engine/classes/Humanoid.md) will see the Name and healthbar of other players if those other players are within the distance settings set in the [Humanoid](/docs/reference/engine/classes/Humanoid.md) selecting `Viewer` (this can be thought of as the lowest priority, and will not be taken into account if other players are selecting 'Subject' or 'None'). |
| `Subject` | 1 | A player selecting `Subject` on their [Humanoid](/docs/reference/engine/classes/Humanoid.md) will allow other players to see their Name and healthbar if those other players are within the distance settings set in the [Humanoid](/docs/reference/engine/classes/Humanoid.md) selecting `Subject` (this can be thought of as the second highest priority). |
| `None` | 2 | A player selecting `None` on their [Humanoid](/docs/reference/engine/classes/Humanoid.md) will not have their Name and healthbar displayed to other players under any circumstance (this can be thought of as the highest priority). |