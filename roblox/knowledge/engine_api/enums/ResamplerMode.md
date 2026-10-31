---
name: ResamplerMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the image filtering used."
---

# ResamplerMode

Determines the image filtering used.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Bilinear filtering of the four near pixels in the image. |
| `Pixelated` | 1 | Nearest neighbor filtering of the closest pixel in the image. |