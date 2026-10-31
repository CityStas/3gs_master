---
name: PathWaypoint
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A description of the steps required to reach the next waypoint in a path."
---

# PathWaypoint

A description of the steps required to reach the next waypoint in a path.

**Type:** datatype

## Description

The `PathWaypoint` data type is constructed by a [PathWaypointAction](/docs/reference/engine/enums/PathWaypointAction.md)
action, [Vector3](/docs/reference/engine/datatypes/Vector3.md) position, and [string](/docs/reference/engine/globals/string.md) label which is used
by the [PathfindingService](/docs/reference/engine/classes/PathfindingService.md) to create points along a generated path.

## Constructors

### PathWaypoint.new

**Signature:** `PathWaypoint.new(position: Vector3, action: PathWaypointAction, label: string)`

Returns a [PathWaypoint](/docs/reference/engine/datatypes/PathWaypoint.md) object from the given [Vector3](/docs/reference/engine/datatypes/Vector3.md)
position, [PathWaypointAction](/docs/reference/engine/enums/PathWaypointAction.md) action, and optional string label.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | The 3D position of the waypoint. |
| `action` | `PathWaypointAction` |  | The action to perform at the waypoint. |
| `label` | `string` |  | The name of the navigation area that generates the waypoint. |

## Properties

### PathWaypoint.Action

**Type:** `PathWaypointAction`

The action to perform at this waypoint as an [PathWaypointAction](/docs/reference/engine/enums/PathWaypointAction.md).

### PathWaypoint.Position

**Type:** `Vector3`

The 3D position of this waypoint.

### PathWaypoint.Label

**Type:** `string`

The name of the navigation area that generates this waypoint. Automatic
jump links have `Jump` as their label.