---
name: FramerateManagerMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the Frame Rate Manager (FRM) adjusts rendering quality to maintain target frame rates."
---

# FramerateManagerMode

Controls how the Frame Rate Manager (FRM) adjusts rendering quality to
maintain target frame rates.

**Type:** enum

## Description

Controls how the Frame Rate Manager (FRM) dynamically scales rendering quality
— including view distance, block count, and quality level — to meet frame rate
targets. The FRM is enabled separately via [RenderSettings.EnableFRM](/docs/reference/engine/classes/RenderSettings.md);
this enum selects its operating mode when active.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | The engine selects whether to run FRM based on hardware and platform context. This is the default. |
| `On` | 1 | FRM is explicitly enabled and dynamically adjusts rendering quality to meet frame rate targets. |
| `Off` | 2 | FRM quality throttling is disabled; block count is fixed at the baseline level regardless of frame rate. |