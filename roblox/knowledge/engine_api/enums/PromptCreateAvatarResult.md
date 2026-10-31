---
name: PromptCreateAvatarResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Result codes returned by AvatarCreationService:PromptCreateAvatarAsync() indicating whether avatar creation succeeded or why it failed."
---

# PromptCreateAvatarResult

Result codes returned by
[AvatarCreationService:PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md) indicating whether
avatar creation succeeded or why it failed.

**Type:** enum

## Description

Result codes returned by
[AvatarCreationService:PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md) to indicate the
outcome of an in-experience avatar creation flow. A value of
[PromptCreateAvatarResult.Success](/docs/reference/engine/enums/PromptCreateAvatarResult.md) means the avatar was created and
published; all other values identify the failure reason so the experience can
surface an appropriate message to the player.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | The avatar was successfully created and published to the player's account. |
| `PermissionDenied` | 2 | The player explicitly declined the avatar creation consent prompt. |
| `Timeout` | 3 | The avatar creation consent prompt timed out before the player responded. |
| `UploadFailed` | 4 | The avatar assets passed validation but the server-side upload or bundle creation step failed. |
| `NoUserInput` | 5 | The player did not interact with the avatar creation consent prompt before it closed. |
| `InvalidHumanoidDescription` | 6 | The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) supplied to [AvatarCreationService:PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md) was invalid and could not be used to create an avatar. |
| `UGCValidationFailed` | 7 | The avatar's geometry or content failed Roblox's UGC (User-Generated Content) validation checks. |
| `ModeratedName` | 8 | The proposed avatar name or description was rejected by Roblox moderation. |
| `MaxOutfits` | 9 | The player has reached the maximum number of outfits allowed on their Roblox account. |
| `PurchaseFailure` | 10 | The avatar creation attempt failed because the player did not have sufficient Robux to cover the required purchase. |
| `UnknownFailure` | 11 | An unexpected or unclassified failure occurred during avatar creation. |
| `TokenInvalid` | 12 | The creation token provided to [AvatarCreationService:PromptCreateAvatarAsync()](/docs/reference/engine/classes/AvatarCreationService.md) was not valid or did not match the current experience. |