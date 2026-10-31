---
name: TrackerMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the combination of input sources an `RTAnimationTracker` is currently using to drive animation."
---

# TrackerMode

Describes the combination of input sources an `RTAnimationTracker` is
currently using to drive animation.

**Type:** enum

## Description

Describes what combination of input inference modes an `RTAnimationTracker` is
currently using. The value is read-only and reflects whether audio-to-curve
(a2c) inference, video-to-curve (v2c) inference, both, or neither is active at
a given moment.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No tracking inference is active; the tracker is idle or has not successfully started. |
| `Audio` | 1 | Only audio-to-curve (lipsync) inference is active; no camera-based facial tracking is running. |
| `Video` | 2 | Only video-to-curve facial tracking is active; audio-based lipsync inference is not running. |
| `AudioVideo` | 3 | Both audio-to-curve lipsync inference and video-to-curve facial tracking are active simultaneously. |