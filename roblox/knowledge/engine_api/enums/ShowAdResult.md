---
name: ShowAdResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Result codes returned by AdService:ShowRewardedVideoAdAsync() indicating whether a rewarded video ad completed successfully or why it did not."
---

# ShowAdResult

Result codes returned by [AdService:ShowRewardedVideoAdAsync()](/docs/reference/engine/classes/AdService.md)
indicating whether a rewarded video ad completed successfully or why it did
not.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ShowCompleted` | 1 | The ad was successfully shown to completion. |
| `AdNotReady` | 2 | You are trying to show a full-screen ad before the ad has fully loaded. You might have failed to properly fetch the ad, or the ad might have expired. |
| `AdAlreadyShowing` | 3 | You are trying to show a full-screen ad while another full-screen ad is already playing. |
| `InternalError` | 4 | An unspecified internal error occurred. Try showing the ad again. |
| `ShowInterrupted` | 5 | The ad view of the user has been interrupted. The user might have closed the ad view or left the experience, and should not receive a reward. |
| `InsufficientMemory` | 6 | The device does not have sufficient video memory available to display the ad. |