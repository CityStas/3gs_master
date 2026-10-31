---
name: FileSystemWalkMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether FileSystemService:Walk() descends into subdirectories."
---

# FileSystemWalkMode

Controls whether [FileSystemService:Walk()](/docs/reference/engine/classes/FileSystemService.md) descends into
subdirectories.

**Type:** enum

## Description

Controls whether [FileSystemService:Walk()](/docs/reference/engine/classes/FileSystemService.md) traverses only the immediate
entries of the target directory or also descends recursively into
subdirectories. Pass one of these values as the `mode` argument to `Walk`;
when `mode` is omitted the method defaults to
[FileSystemWalkMode.NonRecursive](/docs/reference/engine/enums/FileSystemWalkMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `NonRecursive` | 0 | Visits only the immediate entries of the specified directory, without descending into subdirectories. |
| `Recursive` | 1 | Visits all entries in the specified directory and all of its subdirectories, incrementing the iterator's `Depth` field for each level descended. |