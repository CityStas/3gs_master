---
name: ExternalEditorMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether Roblox Studio opens scripts in the operating system's default editor or in a user-selected external editor."
---

# ExternalEditorMode

Controls whether Roblox Studio opens scripts in the operating system's default
editor or in a user-selected external editor.

**Type:** enum

## Description

Controls whether Roblox Studio opens scripts in the operating system's default
editor or in a specific editor chosen by the user. Used by the
`ExternalEditorMode` property of [Studio](/docs/reference/engine/classes/Studio.md). The default value is
[ExternalEditorMode.SystemDefault](/docs/reference/engine/enums/ExternalEditorMode.md).

When set to [ExternalEditorMode.UserSelectedEditor](/docs/reference/engine/enums/ExternalEditorMode.md), the
[Studio.ExternalEditorSelection](/docs/reference/engine/classes/Studio.md) property becomes active and determines
which editor executable Studio launches.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `SystemDefault` | 0 | Studio opens scripts using the operating system's default application for the file type. |
| `UserSelectedEditor` | 1 | Studio opens scripts using the external editor executable specified in [Studio.ExternalEditorSelection](/docs/reference/engine/classes/Studio.md). |