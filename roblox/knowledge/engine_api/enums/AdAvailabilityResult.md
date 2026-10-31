---
name: AdAvailabilityResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether an ad is available or the reason it cannot be shown."
---

# AdAvailabilityResult

Indicates whether an ad is available or the reason it cannot be shown.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `IsAvailable` | 1 | An ad is available to show the user. |
| `DeviceIneligible` | 2 | The device is ineligible to receive ads. |
| `ExperienceIneligible` | 3 | The experience is ineligible to receive ads. Check if its eligibility has been revoked. |
| `InternalError` | 4 | An unspecified internal error occurred. Try fetching the ad again. |
| `NoFill` | 5 | There are no ads available to fill your ad request. You might have hit the ad frequency limit. |
| `PlayerIneligible` | 6 | The user is ineligible to receive ads during this session. The user might be under 13 or located in a blocked region. |
| `PublisherIneligible` | 7 | The publisher is ineligible to receive ads because they have not met the publisher eligibility requirements. |