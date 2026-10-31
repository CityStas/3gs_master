---
name: ModerationStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the moderation review state of an avatar outfit or asset."
---

# ModerationStatus

Indicates the moderation review state of an avatar outfit or asset.

**Type:** enum

## Description

The `ModerationStatus` enum represents the current moderation review state of
avatar content such as outfits and assets. It is returned by
[AvatarCreationService](/docs/reference/engine/classes/AvatarCreationService.md) moderation events —
[AvatarCreationService.AvatarModerationCompleted](/docs/reference/engine/classes/AvatarCreationService.md),
[AvatarCreationService.AvatarAssetModerationCompleted](/docs/reference/engine/classes/AvatarCreationService.md), and
[AvatarCreationService.AvatarOutfitModerationCompleted](/docs/reference/engine/classes/AvatarCreationService.md) — to communicate
the outcome of a moderation check.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ReviewedApproved` | 1 | The content completed moderation review and was approved for use. |
| `ReviewedRejected` | 2 | The content completed moderation review and was rejected. |
| `NotReviewed` | 3 | The content has been submitted but moderation review is still pending. |
| `NotApplicable` | 4 | Moderation review is not applicable to this content. |
| `Invalid` | 5 | An unrecognized or error moderation status returned when the server response cannot be mapped to a known value. |