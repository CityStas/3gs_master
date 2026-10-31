---
name: GradientTileMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used alongside UIGradient.TileMode to set how the gradient repeats."
---

# GradientTileMode

Used alongside [UIGradient.TileMode](/docs/reference/engine/classes/UIGradient.md) to set how the gradient repeats.

**Type:** enum

## Description

Used alongside [UIGradient.TileMode](/docs/reference/engine/classes/UIGradient.md) to set how the gradient repeats
when the full sequence does not fully cover the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Clamp` | 0 | Default mode where the color/transparency values at the start and end of the sequence extend infinitely, so the start values fill any area before the gradient and the end values fill any area after it. |
| `Repeat` | 1 | The gradient repeats by wrapping the color/transparency sequence tiles seamlessly from end back to start. This can produce a visible seam if the first and last color/transparency values in the sequence differ. |
| `Mirror` | 2 | The gradient reflects at each boundary so the color/transparency sequence ping-pongs. This produces a smooth repetition with no seam, since the direction reverses at each tile edge. |