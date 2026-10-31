---
name: PromptCreateOutfitResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Result codes returned by AvatarCreationService:PromptCreateMakeupAsync() that describe the overall makeup look creation outcome."
---

# PromptCreateOutfitResult

Result codes returned by
[AvatarCreationService:PromptCreateMakeupAsync()](/docs/reference/engine/classes/AvatarCreationService.md) that describe the
overall makeup look creation outcome.

**Type:** enum

## Description

Result codes returned by
[PromptCreateMakeupAsync()](/docs/reference/engine/classes/AvatarCreationService.md).
Use this enum for the overall creation outcome. For a
[PartialSuccess](/docs/reference/engine/enums/PromptCreateOutfitResult.md) result, inspect
the method's per-asset results to determine which submitted assets were
created. Partial success does not guarantee that the makeup look itself was
created.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | All submitted makeup assets and the makeup look were created successfully. |
| `PartialSuccess` | 2 | At least one makeup asset was created, but one or more assets or the final makeup look composition did not succeed. |
| `CreationFailure` | 3 | No makeup assets could be created, so the makeup look was not created. |
| `PermissionDenied` | 4 | The player declined the makeup creation prompt. |
| `Timeout` | 5 | The makeup creation prompt timed out before the player responded. |
| `NoUserInput` | 6 | The player did not respond to the makeup creation prompt. |
| `UnknownFailure` | 7 | An unexpected or unclassified error prevented makeup look creation. |
| `UGCValidationFailed` | 8 | The makeup assets or creation tokens failed validation before upload. |