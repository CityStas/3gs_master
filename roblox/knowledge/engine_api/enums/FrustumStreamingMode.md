---
name: FrustumStreamingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with Player.FrustumStreaming to control the engine's instance streaming behavior for their camera view"
---

# FrustumStreamingMode

Used with [Player.FrustumStreaming](/docs/reference/engine/classes/Player.md) to control the engine's instance
streaming behavior for their camera view

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior, currently equivalent to `Disabled`. |
| `Enabled` | 1 | Always stream camera view. |
| `Disabled` | 2 | Disable camera view streaming. |
| `Automatic` | 3 | Allow the engine to decide when to stream the camera view based client ability and gameplay factors. |