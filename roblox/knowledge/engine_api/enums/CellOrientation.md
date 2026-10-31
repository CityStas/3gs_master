---
name: CellOrientation
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the corner orientation of a legacy terrain cell, used with the deprecated Terrain:SetCell() method."
---

# CellOrientation

Specifies the corner orientation of a legacy terrain cell, used with the
deprecated [Terrain:SetCell()](/docs/reference/engine/classes/Terrain.md) method.

**Type:** enum

## Description

Deprecated. Specifies the corner from which a legacy terrain cell's block
begins, used with the deprecated [Terrain:SetCell()](/docs/reference/engine/classes/Terrain.md) and
[Terrain:SetCells()](/docs/reference/engine/classes/Terrain.md) methods. When viewed from directly above (downward
vertical perspective), the value identifies which corner of the cell the block
occupies, ordered clockwise starting from the upper-left.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NegZ` | 0 | Upper-left corner orientation when the cell is viewed from directly above. |
| `X` | 1 | Upper-right corner orientation when the cell is viewed from directly above. |
| `Z` | 2 | Lower-right corner orientation when the cell is viewed from directly above. |
| `NegX` | 3 | Lower-left corner orientation when the cell is viewed from directly above. |