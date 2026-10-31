---
name: AudioSampleFormat
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the numeric format used to represent individual audio samples."
---

# AudioSampleFormat

Describes the numeric format used to represent individual audio samples.

**Type:** enum

## Description

The `AudioSampleFormat` enum describes the numeric format used to represent
individual audio samples in an audio stream buffer.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Int16` | 0 | Samples are represented as 16-bit signed integers, ranging from `-32768` to `32767`. |
| `Float32` | 1 | Samples are represented as 32-bit floating-point numbers, typically ranging from `-1.0` to `1.0`. |