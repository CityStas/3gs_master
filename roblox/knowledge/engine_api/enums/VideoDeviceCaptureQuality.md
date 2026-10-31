---
name: VideoDeviceCaptureQuality
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the capture resolution and frame rate used by a `VideoDeviceInput` when reading from a camera device."
---

# VideoDeviceCaptureQuality

Specifies the capture resolution and frame rate used by a `VideoDeviceInput`
when reading from a camera device.

**Type:** enum

## Description

Specifies the capture resolution and frame rate used by a `VideoDeviceInput`
when reading from a camera device. Set via the `CaptureQuality` property. The
actual resolution and frame rate for each value are optimized per platform.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The default capture quality. |
| `Low` | 1 | Captures at a reduced quality to lower resource usage on constrained or mobile platforms. |
| `Medium` | 2 | Captures at a balanced quality suitable for most use cases. |
| `High` | 3 | Captures at the highest available quality. |