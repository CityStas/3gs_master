---
name: SlimTranscoderStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the backend transcoding state of a SLIM model, from upload through transcoding to success or failure."
---

# SlimTranscoderStatus

Describes the backend transcoding state of a SLIM model, from upload through
transcoding to success or failure.

**Type:** enum

## Description

Describes the backend transcoding state of a SLIM model. The status progresses
as the model is uploaded to the content-delivery network and transcoded into
SLIM assets. The **DebugVisualizations** panel in the Developer Console can
color-code models by this status to surface which models have successfully
transcoded and which have failed.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | The transcoding status has not yet been determined. This is the initial state before the model has been queried. Shown as yellow in the debug tint overlay. |
| `Transcoding` | 1 | SLIM transcoding is currently in progress on the backend. The model is expected to transition to Succeeded or Failed once transcoding completes. Shown as blue in the debug tint overlay. |
| `Succeeded` | 2 | Transcoding completed successfully and the SLIM assets are available for streaming. Shown as green in the debug tint overlay. |
| `Failed` | 3 | Transcoding did not complete successfully. Shown as red in the debug tint overlay. |