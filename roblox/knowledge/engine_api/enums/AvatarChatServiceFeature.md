---
name: AvatarChatServiceFeature
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A bitmask enum whose items represent individual avatar chat capabilities for voice and video communication within an experience."
---

# AvatarChatServiceFeature

A bitmask enum whose items represent individual avatar chat capabilities for
voice and video communication within an experience.

**Type:** enum

## Description

A bitmask enum whose items represent individual avatar chat capabilities for
voice and video communication within an experience. Each item is a single bit
flag; multiple flags are combined with bitwise-OR to form a feature mask that
`IsEnabled()` can test. Flags fall into three categories: universe/place
settings (set by the server based on creator configuration), user eligibility
and opt-in state (resolved per-player from backend permissions), and
moderation status.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No avatar chat features are enabled. This is the default value of the bitmask before any capabilities are resolved. |
| `UniverseAudio` | 1 | Voice chat audio is enabled at the universe level. This is a server-side setting configured by the experience creator; it must be combined with [AvatarChatServiceFeature.PlaceAudio](/docs/reference/engine/enums/AvatarChatServiceFeature.md) for audio to be active in a given place. |
| `UniverseVideo` | 2 | Avatar video (camera-based facial animation) is enabled at the universe level. This is a server-side setting configured by the experience creator; it must be combined with [AvatarChatServiceFeature.PlaceVideo](/docs/reference/engine/enums/AvatarChatServiceFeature.md) for video to be active in a given place. |
| `PlaceAudio` | 4 | Voice chat audio is enabled for the current place. Both this flag and [AvatarChatServiceFeature.UniverseAudio](/docs/reference/engine/enums/AvatarChatServiceFeature.md) must be set for audio to be active in the place. |
| `PlaceVideo` | 8 | Avatar video (camera-based facial animation) is enabled for the current place. Both this flag and [AvatarChatServiceFeature.UniverseVideo](/docs/reference/engine/enums/AvatarChatServiceFeature.md) must be set for video to be active in the place. |
| `UserAudioEligible` | 16 | The user meets the requirements to use voice chat audio (age-verified, not banned, etc.). Eligibility is resolved per-player from backend permissions; it does not imply the user has opted in (see [AvatarChatServiceFeature.UserAudio](/docs/reference/engine/enums/AvatarChatServiceFeature.md)). |
| `UserAudio` | 32 | The user has opted in to voice chat audio. This flag is only meaningful when [AvatarChatServiceFeature.UserAudioEligible](/docs/reference/engine/enums/AvatarChatServiceFeature.md) is also set; together they indicate the user both can and has chosen to use voice. |
| `UserVideoEligible` | 64 | The user meets the requirements to use avatar video (camera-based facial animation). Eligibility is resolved per-player from backend permissions; it does not imply the user has opted in (see [AvatarChatServiceFeature.UserVideo](/docs/reference/engine/enums/AvatarChatServiceFeature.md)). |
| `UserVideo` | 128 | The user has opted in to avatar video (camera-based facial animation). This flag is only meaningful when [AvatarChatServiceFeature.UserVideoEligible](/docs/reference/engine/enums/AvatarChatServiceFeature.md) is also set; together they indicate the user both can and has chosen to use video. |
| `UserBanned` | 256 | The user is currently banned from avatar chat features. When this flag is present in the client features mask, voice and video capabilities are unavailable to the player regardless of other eligibility flags. |
| `UserVerifiedForVoice` | 512 | The user has completed voice verification. |