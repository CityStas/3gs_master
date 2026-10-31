---
name: PathWaypointAction
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the action to take when a PathWaypoint is reached."
---

# PathWaypointAction

Describes the action to take when a [PathWaypoint](/docs/reference/engine/datatypes/PathWaypoint.md) is reached.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Walk` | 0 | Walk action needed to reach the next waypoint. |
| `Jump` | 1 | Jump action needed to reach the next waypoint. |
| `Custom` | 2 | A developer-defined custom action is needed to traverse a [PathfindingLink](/docs/reference/engine/classes/PathfindingLink.md) to reach the next waypoint. |