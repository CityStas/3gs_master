---
name: FinishRecordingOperation
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how ChangeHistoryService:FinishRecording() completes or discards a recording session."
---

# FinishRecordingOperation

Controls how [ChangeHistoryService:FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) completes or
discards a recording session.

**Type:** enum

## Description

Controls what [ChangeHistoryService:FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) does when a
plugin ends a recording. Pass [FinishRecordingOperation.Commit](/docs/reference/engine/enums/FinishRecordingOperation.md) to push
recorded changes onto the undo/redo stack,
[FinishRecordingOperation.Append](/docs/reference/engine/enums/FinishRecordingOperation.md) to merge them with the previous entry
when possible, or [FinishRecordingOperation.Cancel](/docs/reference/engine/enums/FinishRecordingOperation.md) to discard them.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Cancel` | 0 | Cancels the recording, automatically undoing any work in progress. |
| `Commit` | 1 | Commits the recorded work. |
| `Append` | 2 | Commits the recorded work and merges with the previous recording if possible. |