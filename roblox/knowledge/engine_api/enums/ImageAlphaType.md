---
name: ImageAlphaType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum for determining if the alpha or color is locked while combining two images."
---

# ImageAlphaType

Enum for determining if the alpha or color is locked while combining two
images.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 1 | The default behavior in which neither color nor alpha values are locked. |
| `LockCanvasAlpha` | 2 | The alpha values of the image will not be modified. |
| `LockCanvasColor` | 3 | The color values of the image will not be modified. |