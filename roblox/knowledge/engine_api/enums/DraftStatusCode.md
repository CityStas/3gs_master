---
name: DraftStatusCode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the state of a script draft tracked by DraftsService."
---

# DraftStatusCode

Describes the state of a script draft tracked by [DraftsService](/docs/reference/engine/classes/DraftsService.md).

**Type:** enum

## Description

State of a script draft from `GetDraftStatus` and from `CommitStatusChanged` /
`UpdateStatusChanged`. See individual items for in-sync, outdated, committed,
and removed-script outcomes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OK` | 0 | The draft is in sync with the server's base version and has no blocking conflicts. |
| `DraftOutdated` | 1 | The server version of the script has advanced beyond the base version used when the draft was created, so the draft must be updated before it can be committed. |
| `ScriptRemoved` | 2 | The script referenced by the draft no longer exists in the data model. |
| `DraftCommitted` | 3 | The draft was successfully committed to the server and removed from the local sandbox. |