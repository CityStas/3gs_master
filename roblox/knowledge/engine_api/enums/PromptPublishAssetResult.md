---
name: PromptPublishAssetResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Deprecated result enum for the `OpenPublishResultModal` event."
---

# PromptPublishAssetResult

Deprecated result enum for the `OpenPublishResultModal` event.

**Type:** enum

## Description

Deprecated result enum for the `OpenPublishResultModal` event. Use
[PromptCreatePlatformContentResult](/docs/reference/engine/enums/PromptCreatePlatformContentResult.md) instead.

[PromptCreateAssetResult](/docs/reference/engine/enums/PromptCreateAssetResult.md) is a separate result enum returned by the
`OpenCreateResultModal` event.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 1 | The asset was published successfully. |
| `PermissionDenied` | 2 | The user explicitly denied the consent prompt required to publish the asset. |
| `Timeout` | 3 | The publish flow timed out, typically because the user disconnected or left the experience during the consent prompt. |
| `UploadFailed` | 4 | The asset upload to the Roblox backend failed after consent was granted. |
| `NoUserInput` | 5 | The user did not grant or deny the consent prompt before the window expired. |
| `UnknownFailure` | 6 | The publish failed for an unspecified or unexpected reason. |