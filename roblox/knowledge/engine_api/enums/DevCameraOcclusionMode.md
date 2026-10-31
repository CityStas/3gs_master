---
name: DevCameraOcclusionMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how the default camera handles objects that are in-between the camera and the camera subject."
---

# DevCameraOcclusionMode

Determines how the default camera handles objects that are in-between the
camera and the camera subject.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Zoom` | 0 | The camera zooms in until there is nothing between it and its subject. |
| `Invisicam` | 1 | Any objects between the camera and its subject become translucent locally. |