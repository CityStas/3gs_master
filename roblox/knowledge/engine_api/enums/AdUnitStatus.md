---
name: AdUnitStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Exposes the status of an immersive ad."
---

# AdUnitStatus

Exposes the status of an immersive ad.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Inactive` | 0 | The ad unit isn't currently serving an ad and it may be configured incorrectly. An [AdGui](/docs/reference/engine/classes/AdGui.md) with this status will display its fallback image. |
| `Active` | 1 | The ad unit is currently serving an ad. Players will observe sponsored content in an [AdGui](/docs/reference/engine/classes/AdGui.md) and an [AdPortal](/docs/reference/engine/classes/AdPortal.md) will teleport users that walk through. |