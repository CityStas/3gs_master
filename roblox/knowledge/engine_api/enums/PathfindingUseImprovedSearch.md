---
name: PathfindingUseImprovedSearch
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether PathfindingService uses an improved search algorithm."
---

# PathfindingUseImprovedSearch

Controls whether [PathfindingService](/docs/reference/engine/classes/PathfindingService.md) uses an improved search algorithm.

**Type:** enum

## Description

Determines whether [PathfindingService](/docs/reference/engine/classes/PathfindingService.md) uses an improved pathfinding
search algorithm. This enum is used by
[Workspace.PathfindingUseImprovedSearch](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default pathfinding behavior. |
| `Disabled` | 1 | Uses the legacy pathfinding search algorithm. |
| `Enabled` | 2 | Uses the improved pathfinding search algorithm. |