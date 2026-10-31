---
name: TableMajorAxis
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by UITableLayout.MajorAxis to decide whether direct siblings are rows or columns."
---

# TableMajorAxis

Used by [UITableLayout.MajorAxis](/docs/reference/engine/classes/UITableLayout.md) to decide whether direct siblings are
rows or columns.

**Type:** enum

## Description

Used to indicate whether the direct siblings of a [UITableLayout](/docs/reference/engine/classes/UITableLayout.md) are
considered the rows or the columns. The children of the direct siblings are
the columns or rows, respectively.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `RowMajor` | 0 | The direct siblings are considered rows. |
| `ColumnMajor` | 1 | The direct siblings are considered columns. |