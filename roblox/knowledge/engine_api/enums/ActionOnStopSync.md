---
name: ActionOnStopSync
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies how Roblox Studio handles local files when file sync stops."
---

# ActionOnStopSync

Specifies how Roblox Studio handles local files when file sync stops.

**Type:** enum

## Description

Controls the behavior selected by the
[ActionOnStopSync](/docs/reference/engine/classes/Studio.md) setting.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AlwaysAsk` | 0 | Prompts before deleting local files when file sync stops. |
| `KeepLocalFiles` | 1 | Keeps local files when file sync stops. |
| `DeleteLocalFiles` | 2 | Deletes local files when file sync stops. |