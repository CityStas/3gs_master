---
name: DraggerCoordinateSpace
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the coordinate space used when dragging objects in Studio."
---

# DraggerCoordinateSpace

Determines the coordinate space used when dragging objects in Studio.

**Type:** enum

## Description

Determines the coordinate space in which the Studio dragger moves and orients
selected objects. Used as the type of the
[DraggerService.DraggerCoordinateSpace](/docs/reference/engine/classes/DraggerService.md) property, which defaults to
[DraggerCoordinateSpace.Object](/docs/reference/engine/enums/DraggerCoordinateSpace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Object` | 0 | Dragging is performed relative to the object's local coordinate space. |
| `World` | 1 | Dragging is performed relative to the world coordinate space. |