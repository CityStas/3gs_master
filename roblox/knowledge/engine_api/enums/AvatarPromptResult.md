---
name: AvatarPromptResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The result of prompt operations of AvatarEditorService."
---

# AvatarPromptResult

The result of prompt operations of [AvatarEditorService](/docs/reference/engine/classes/AvatarEditorService.md).

**Type:** enum

## Description

Indicates the outcome of a prompt operation initiated by
[AvatarEditorService](/docs/reference/engine/classes/AvatarEditorService.md). Each `Prompt` method on the service (such as
[AvatarEditorService:PromptSaveAvatar()](/docs/reference/engine/classes/AvatarEditorService.md),
[AvatarEditorService:PromptSetFavorite()](/docs/reference/engine/classes/AvatarEditorService.md), and
[AvatarEditorService:PromptCreateOutfit()](/docs/reference/engine/classes/AvatarEditorService.md)) displays a native dialog to
the user and fires a corresponding `Completed` event that passes this enum as
its `result` parameter.

- **Success** — the user confirmed the prompt and the back-end request
  completed without error.
- **PermissionDenied** — the user dismissed the prompt or otherwise declined
  to grant the requested permission.
- **Failed** — an error occurred while processing the request (for example, a
  network failure or an invalid response from the server).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | The prompted action was completed. |
| `PermissionDenied` | 2 | Denied permission to take the prompted action. |
| `Failed` | 3 | Failure while trying to take the prompted action. |