---
name: PromptCreateAssetResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the result of a AvatarCreationService:PromptCreateAvatarAssetAsync() call."
---

# PromptCreateAssetResult

Describes the result of a
[AvatarCreationService:PromptCreateAvatarAssetAsync()](/docs/reference/engine/classes/AvatarCreationService.md) call.

**Type:** enum

## Description

Outcome of [AvatarCreationService:PromptCreateAvatarAssetAsync()](/docs/reference/engine/classes/AvatarCreationService.md) after
a player responds to the in-game asset creation prompt. Distinguishes a
successful publish from failure modes such as moderation rejection, declined
consent, insufficient Robux, validation failure, or upload errors.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | The asset was successfully created and published. |
| `PermissionDenied` | 2 | The player explicitly declined the asset-creation consent prompt. |
| `Timeout` | 3 | The creation attempt timed out because the player disconnected or left the experience. |
| `UploadFailed` | 4 | The asset upload to the Roblox backend failed after validation. |
| `NoUserInput` | 5 | The player did not interact with the creation prompt before it expired. |
| `UnknownFailure` | 6 | The asset creation failed for an unspecified or unexpected reason. |
| `UGCValidationFailed` | 7 | The asset failed user-generated content validation checks before upload. |
| `ModeratedName` | 8 | The asset name or description was rejected by Roblox moderation. |
| `PurchaseFailure` | 9 | The asset could not be created because the player had insufficient Robux. |
| `TokenInvalid` | 10 | The creation token provided to the prompt was invalid or could not be verified. |