---
name: FileMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether FileSystemService normalizes line endings when reading or writing files."
---

# FileMode

Controls whether [FileSystemService](/docs/reference/engine/classes/FileSystemService.md) normalizes line endings when
reading or writing files.

**Type:** enum

## Description

The `FileMode` enum is passed to [FileSystemService:ReadFile()](/docs/reference/engine/classes/FileSystemService.md) and
[FileSystemService:WriteFile()](/docs/reference/engine/classes/FileSystemService.md) to control line-ending handling.
[FileMode.Text](/docs/reference/engine/enums/FileMode.md) normalizes `\r\n` sequences to `\n` on both read and
write, ensuring consistent cross-platform behavior when working with text
content. [FileMode.Binary](/docs/reference/engine/enums/FileMode.md) performs no transformation, preserving every
byte exactly as stored on disk.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Binary` | 0 | Reads or writes raw bytes with no line-ending transformation, preserving all characters exactly as stored on disk. |
| `Text` | 1 | Reads or writes file content with `\r\n` sequences normalized to `\n`, ensuring consistent line endings across platforms. |