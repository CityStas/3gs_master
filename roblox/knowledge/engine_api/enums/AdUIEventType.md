---
name: AdUIEventType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of user-interaction or system event that occurred on the immersive ad UI overlay of an AdGui."
---

# AdUIEventType

Describes the type of user-interaction or system event that occurred on the
immersive ad UI overlay of an [AdGui](/docs/reference/engine/classes/AdGui.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AdLabelClicked` | 0 | The player clicked the "Sponsored" label on the ad overlay, which opens the ad disclosure prompt showing advertiser and payer information. |
| `VolumeButtonClicked` | 1 | The player clicked the volume toggle button on the ad overlay, which mutes or unmutes the video ad audio. |
| `FullscreenButtonClicked` | 2 | The player clicked the fullscreen toggle button, which smoothly zooms the camera to a centered view of the ad surface and enables audio. |
| `PlayButtonClicked` | 3 | The player clicked the play button on the ad overlay. If the ad is already in fullscreen, playback resumes; otherwise it enters fullscreen mode which also starts (or resumes) the video. |
| `PauseButtonClicked` | 4 | The player clicked the pause button while a video ad is playing in fullscreen mode, which pauses video playback. |
| `CloseButtonClicked` | 5 | The player clicked the close button on the fullscreen video ad view, which exits fullscreen mode and returns to the normal camera position. |
| `WhyThisAdClicked` | 6 | The player clicked the "Why this ad?" link, which displays the EUDSA (European Digital Services Act) disclosure prompt showing the advertiser and payer names for the current ad creative. |
| `PlayEventTriggered` | 7 | A system-initiated play/resume event that clears the force-pause state and resumes video playback if the stream is open. |
| `PauseEventTriggered` | 8 | A system-initiated pause event, used when the engine needs to force-pause the video (for example, when a dropdown menu opens over the ad). Prevents viewability-based auto-play from resuming playback until a corresponding system event clears that pause. |