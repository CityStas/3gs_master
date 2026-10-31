---
name: DefaultScriptSyncFileType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the file extension used when Studio's script sync feature saves script instances to the filesystem."
---

# DefaultScriptSyncFileType

Controls the file extension used when Studio's script sync feature saves
script instances to the filesystem.

**Type:** enum

## Description

Specifies whether Studio writes synced script files with a `.lua` or `.luau`
extension when using the file sync (external editor) workflow. The active
value is read from [Studio.DefaultScriptSyncFileType](/docs/reference/engine/classes/Studio.md). Defaults to
[DefaultScriptSyncFileType.Luau](/docs/reference/engine/enums/DefaultScriptSyncFileType.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Lua` | 0 | Script files are synced to the filesystem with a `.lua` extension. |
| `Luau` | 1 | Script files are synced to the filesystem with a `.luau` extension. |