---
name: BulkMoveMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the set of property changed events that fire when parts are moved by WorldRoot:BulkMoveTo()."
---

# BulkMoveMode

Determines the set of property changed events that fire when parts are moved
by [WorldRoot:BulkMoveTo()](/docs/reference/engine/classes/WorldRoot.md).

**Type:** enum

## Description

Determines which property [Changed](/docs/reference/engine/classes/Object.md) events fire when
[WorldRoot:BulkMoveTo()](/docs/reference/engine/classes/WorldRoot.md) repositions parts. Passing
[BulkMoveMode.FireCFrameChanged](/docs/reference/engine/enums/BulkMoveMode.md) instead of
[BulkMoveMode.FireAllEvents](/docs/reference/engine/enums/BulkMoveMode.md) reduces per-part event overhead by
suppressing [Position](/docs/reference/engine/classes/BasePart.md),
[Orientation](/docs/reference/engine/classes/BasePart.md), and
[Rotation](/docs/reference/engine/classes/BasePart.md) changed signals while still firing the
[CFrame](/docs/reference/engine/classes/BasePart.md) changed signal. The default value of the
`eventMode` parameter in [WorldRoot:BulkMoveTo()](/docs/reference/engine/classes/WorldRoot.md) is
[BulkMoveMode.FireAllEvents](/docs/reference/engine/enums/BulkMoveMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `FireAllEvents` | 0 | Every property changed event fires for each moved part, including [CFrame](/docs/reference/engine/classes/BasePart.md), [Position](/docs/reference/engine/classes/BasePart.md), [Orientation](/docs/reference/engine/classes/BasePart.md), and [Rotation](/docs/reference/engine/classes/BasePart.md). |
| `FireCFrameChanged` | 1 | Only the [CFrame](/docs/reference/engine/classes/BasePart.md) property changed event fires for each moved part; [Position](/docs/reference/engine/classes/BasePart.md), [Orientation](/docs/reference/engine/classes/BasePart.md), and [Rotation](/docs/reference/engine/classes/BasePart.md) changed events are suppressed. |