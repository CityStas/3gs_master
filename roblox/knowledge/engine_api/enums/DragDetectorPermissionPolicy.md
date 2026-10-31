---
name: DragDetectorPermissionPolicy
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to control the permission level for which players can interact with a DragDetector."
---

# DragDetectorPermissionPolicy

Used to control the permission level for which players can interact with a
[DragDetector](/docs/reference/engine/classes/DragDetector.md).

**Type:** enum

## Description

Used to control the permission level for which players can interact with a
[DragDetector](/docs/reference/engine/classes/DragDetector.md) through its
[PermissionPolicy](/docs/reference/engine/classes/DragDetector.md) property.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Nobody` | 0 | No players can interact with the [DragDetector](/docs/reference/engine/classes/DragDetector.md). |
| `Everybody` | 1 | All players can interact with the [DragDetector](/docs/reference/engine/classes/DragDetector.md). |
| `Scriptable` | 2 | Invokes the function registered via [DragDetector:SetPermissionPolicyFunction()](/docs/reference/engine/classes/DragDetector.md), enabling/disabling the detector based on whether the function returns `true` or `false`. |