---
name: TrackerPromptEvent
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the type of prompt fired by the face tracker when a runtime condition requires user attention."
---

# TrackerPromptEvent

Indicates the type of prompt fired by the face tracker when a runtime
condition requires user attention.

**Type:** enum

## Description

Enumerates the categories of prompt events raised by `RTAnimationTracker` and
`FaceAnimatorService` via their `TrackerPrompt` events. Each value describes a
distinct condition that the face-tracking system wants to surface to
experience code so that the experience can react — for example, by displaying
UI guidance to the user.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `LODCameraRecommendDisable` | 0 | The LOD controller has determined that device performance is insufficient to sustain camera-based face tracking and recommends disabling camera input. |