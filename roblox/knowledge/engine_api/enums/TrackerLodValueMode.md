---
name: TrackerLodValueMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the video LOD level is selected for the face-tracking pipeline in `TrackerLodController`."
---

# TrackerLodValueMode

Controls how the video LOD level is selected for the face-tracking pipeline in
`TrackerLodController`.

**Type:** enum

## Description

Specifies whether the face-tracking video LOD level is chosen automatically by
the performance-adaptive LOD controller or forced to a fixed level. Used by
`VideoLodMode`, which defaults to [TrackerLodValueMode.Auto](/docs/reference/engine/enums/TrackerLodValueMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Force0` | 0 | Forces the face-tracking video pipeline to LOD level 0, the faster but less accurate processing mode. |
| `Force1` | 1 | Forces the face-tracking video pipeline to LOD level 1, the more accurate but more resource-intensive processing mode. |
| `Auto` | 2 | The LOD controller selects the video LOD level automatically based on real-time performance metrics. |