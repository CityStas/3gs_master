---
name: ScopeCheckResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the outcome of an `ExperienceAuthService` scope-authorization request."
---

# ScopeCheckResult

Indicates the outcome of an `ExperienceAuthService` scope-authorization
request.

**Type:** enum

## Description

Returned by an `ExperienceAuthService` scope-authorization callback to
indicate whether the player granted, denied, or failed to complete a
permission-consent flow. Callers such as [AssetService](/docs/reference/engine/classes/AssetService.md) and
[AvatarCreationService](/docs/reference/engine/classes/AvatarCreationService.md) inspect this value to decide whether to proceed
with the authorized action or surface an appropriate error to the developer.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ConsentAccepted` | 0 | The player accepted the authorization prompt and a valid token was issued for the requested scopes. |
| `InvalidScopes` | 1 | The requested scopes are not recognized or are not permitted for the calling context. |
| `Timeout` | 2 | The scope-check request exceeded the configured timeout period before the player responded. |
| `NoUserInput` | 3 | The authorization prompt was dismissed without any explicit player action, such as when the player disconnects or the UI is closed without a response. |
| `BackendError` | 4 | The Roblox backend returned an error or unexpected HTTP status when exchanging the consent grant for an authorization token. |
| `UnexpectedError` | 5 | An unexpected error occurred that is not covered by a more specific result code. |
| `InvalidArgument` | 6 | One or more arguments passed to the scope-check call were invalid, such as an empty scope list, a null player instance, or a player who is no longer in the experience. |
| `ConsentDenied` | 7 | The player explicitly declined the authorization prompt. |