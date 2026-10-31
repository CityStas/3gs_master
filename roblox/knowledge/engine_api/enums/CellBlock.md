---
name: CellBlock
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Deprecated enum specifying the geometric block shape of a legacy voxel terrain cell, used with the removed Terrain:SetCell() method."
---

# CellBlock

Deprecated enum specifying the geometric block shape of a legacy voxel terrain
cell, used with the removed [Terrain:SetCell()](/docs/reference/engine/classes/Terrain.md) method.

**Type:** enum

## Description

Specifies the geometric shape of a legacy voxel terrain cell, used with the
deprecated [Terrain:SetCell()](/docs/reference/engine/classes/Terrain.md) and [Terrain:SetCells()](/docs/reference/engine/classes/Terrain.md) methods.
Each value corresponds to one of the five reflected block shapes in the old
voxel terrain system. This enum and the methods that consume it are
deprecated; use smooth terrain APIs instead.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Solid` | 0 | A legacy voxel cell that is completely filled, occupying the full cell volume. |
| `VerticalWedge` | 1 | A legacy voxel cell shaped as a vertical wedge, occupying half of a full cell's volume. |
| `CornerWedge` | 2 | A legacy voxel cell shaped as a corner wedge, occupying approximately one-third of a full cell's volume. |
| `InverseCornerWedge` | 3 | A legacy voxel cell shaped as an inverse corner wedge, occupying approximately two-thirds of a full cell's volume. |
| `HorizontalWedge` | 4 | A legacy voxel cell shaped as a horizontal wedge, occupying half of a full cell's volume. |