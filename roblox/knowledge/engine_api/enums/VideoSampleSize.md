---
name: VideoSampleSize
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The size of textures produced by VideoSampler."
---

# VideoSampleSize

The size of textures produced by [VideoSampler](/docs/reference/engine/classes/VideoSampler.md).

**Type:** enum

## Description

Controls the resolution of textures produced by [VideoSampler](/docs/reference/engine/classes/VideoSampler.md). Use the
smallest resolution that meets your needs to minimize memory usage and improve
sampling performance.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Small` | 0 | Use when the video sample is displayed on roughly a quarter of the screen. |
| `Medium` | 1 | Use when the video sample is displayed on roughly half the screen. |
| `Large` | 2 | Use when the video sample is displayed on roughly three quarters of the screen. |
| `Full` | 3 | Use when the video sample is displayed full screen. |