---
name: RuntimeUndoBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how ChangeHistoryService records and handles undo history during a Studio playtest session."
---

# RuntimeUndoBehavior

Controls how [ChangeHistoryService](/docs/reference/engine/classes/ChangeHistoryService.md) records and handles undo history
during a Studio playtest session.

**Type:** enum

## Description

`RuntimeUndoBehavior` is the type of the
`ChangeHistoryService.RuntimeUndoBehavior` property and determines what Studio
does when a waypoint is requested (via
[ChangeHistoryService:SetWaypoint()](/docs/reference/engine/classes/ChangeHistoryService.md) or the recording API) while the
game is in the run state (i.e., during a playtest). The three values offer
different trade-offs between undo granularity and physics-change handling.

The default behavior is [RuntimeUndoBehavior.Aggregate](/docs/reference/engine/enums/RuntimeUndoBehavior.md): waypoints are
suppressed during the run, all runtime edits accumulate into a single
waypoint, and they are all reverted at once when the playtest stops or resets.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Aggregate` | 0 | Rejects waypoint requests during a run session; all runtime changes accumulate into a single waypoint that is reverted together when the session stops or resets. |
| `Snapshot` | 1 | Accepts waypoint requests during a run session and captures a snapshot of each instance's position and velocity at every waypoint boundary so that physics state can be fully restored on undo. |
| `Hybrid` | 2 | Accepts waypoint requests during a run session but excludes unsolicited physics changes (position and velocity drift from simulation) from the recorded history. |