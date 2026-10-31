---
name: RenderFidelity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the level of detail that solid modeled and mesh parts will be shown in."
---

# RenderFidelity

Determines the level of detail that solid modeled and mesh parts will be shown
in.

**Type:** enum

## Description

This enum determines the level of detail that
[meshes](/docs/en-us/parts/meshes.md) and
[solid modeled](/docs/en-us/parts/solid-modeling.md) parts will be shown in. The
default is **Automatic**, meaning the object's detail is based on its distance
from the camera as outlined in the following table.

| Distance From Camera | Render Fidelity |
| --- | --- |
| Less than 250 studs | Highest |
| 250 to 500 studs | Medium |
| 500 or more studs | Lowest |

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Object's level of detail is dynamically controlled by its distance from the camera (see table above). |
| `Precise` | 1 | Object is rendered in the highest fidelity regardless of its distance from the camera. |
| `Performance` | 2 | Push performance as much as possible, trying to maintain quality if possible, and discarding appearance if that's necessary to reach performance. This means that the performance will always be excellent, but mesh visuals may be affected negatively. |