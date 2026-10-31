---
name: PredictiveStreamingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with Workspace.PredictiveStreamingMode to control whether the engine streams instances predictively."
---

# PredictiveStreamingMode

Used with [Workspace.PredictiveStreamingMode](/docs/reference/engine/classes/Workspace.md) to control whether the
engine streams instances predictively.

**Type:** enum

## Description

Used by [Workspace.PredictiveStreamingMode](/docs/reference/engine/classes/Workspace.md) to control whether streaming
pre-fetches content in the predicted direction of player movement, reducing
visible pop-in. [PredictiveStreamingMode.Enabled](/docs/reference/engine/enums/PredictiveStreamingMode.md) uses player velocity
and heading to pre-fetch beyond the current position-based radius.
[PredictiveStreamingMode.Disabled](/docs/reference/engine/enums/PredictiveStreamingMode.md) uses only the position-based radius.
[PredictiveStreamingMode.Default](/docs/reference/engine/enums/PredictiveStreamingMode.md) uses the engine's current default
behavior for predictive streaming.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine's current default behavior for predictive streaming. |
| `Enabled` | 1 | Enables predictive streaming, pre-fetching content in the direction of player movement to reduce pop-in. |
| `Disabled` | 2 | Disables predictive streaming; content is streamed based on the player's current position radius only. |