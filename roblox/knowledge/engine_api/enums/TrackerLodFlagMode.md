---
name: TrackerLodFlagMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether a real-time face-tracker feature (audio or video) is forced on, forced off, or left to the automatic LOD system."
---

# TrackerLodFlagMode

Controls whether a real-time face-tracker feature (audio or video) is forced
on, forced off, or left to the automatic LOD system.

**Type:** enum

## Description

Type of the `AudioMode` and `VideoMode` properties on `TrackerLodController`.
Each defaults to [TrackerLodFlagMode.Auto](/docs/reference/engine/enums/TrackerLodFlagMode.md). Lets a script force a tracker
pipeline (audio-based or video-based facial animation) on or off, or leave the
decision to the automatic LOD system.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ForceFalse` | 0 | Forces the associated tracker feature disabled, regardless of the current LOD state. |
| `ForceTrue` | 1 | Forces the associated tracker feature enabled, regardless of the current LOD state. |
| `Auto` | 2 | Defers the enabled/disabled decision to the automatic LOD system. |