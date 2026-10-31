---
name: DragDetectorDragStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with DragDetector as the paradigm to generate proposed motion, given a stream of cursor rays."
---

# DragDetectorDragStyle

Used with [DragDetector](/docs/reference/engine/classes/DragDetector.md) as the paradigm to generate proposed motion,
given a stream of cursor rays.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `TranslateLine` | 0 | 1D motion along the detector's [Axis](/docs/reference/engine/classes/DragDetector.md), by default the world **Y** axis. |
| `TranslatePlane` | 1 | 2D motion in the plane **perpendicular** to the detector's [Axis](/docs/reference/engine/classes/DragDetector.md), by default the world **XZ** plane. |
| `TranslatePlaneOrLine` | 2 | 2D motion in the plane **perpendicular** to the detector's [Axis](/docs/reference/engine/classes/DragDetector.md) and, when the modifier is active, 1D motion along the detector's [Axis](/docs/reference/engine/classes/DragDetector.md). |
| `TranslateLineOrPlane` | 3 | 1D motion along the detector's [Axis](/docs/reference/engine/classes/DragDetector.md) and, when the modifier is active, 2D motion in the plane **perpendicular** to the detector's [Axis](/docs/reference/engine/classes/DragDetector.md). |
| `TranslateViewPlane` | 4 | 2D motion in the plane perpendicular to the camera's view. In this mode, the plane is constantly updated, even while dragging, and will always face the camera's current view. |
| `RotateAxis` | 5 | Rotation about the detector's [Axis](/docs/reference/engine/classes/DragDetector.md), by default the world **Y** axis. |
| `RotateTrackball` | 6 | Trackball rotation, further customized through the [TrackballRadialPullFactor](/docs/reference/engine/classes/DragDetector.md) and [TrackballRollFactor](/docs/reference/engine/classes/DragDetector.md) properties. |
| `Scriptable` | 7 | Calculates desired motion via a custom function provided through [SetDragStyleFunction()](/docs/reference/engine/classes/DragDetector.md). |
| `BestForDevice` | 8 | **TranslatePlaneOrLine** for mouse and gamepad; **TranslatePlane** for touch; **6DOF** for VR. |