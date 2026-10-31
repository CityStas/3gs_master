---
name: PlayerDeviceTrustLevel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The trust level of a player's device."
---

# PlayerDeviceTrustLevel

The trust level of a player's device.

**Type:** enum

## Description

The trust level of a player's device as reported by
[Player.DeviceTrustLevel](/docs/reference/engine/classes/Player.md). The trust level describes the device, not the
player or their account.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Pending` | 0 | Roblox is still checking the device. Every player starts at this level, and some players might stay at it for the whole session. |
| `Unknown` | 1 | Roblox can't tell whether the device is trusted, because the player is on an unsupported platform or an error occurred on the Roblox side. The device might or might not be trustworthy. |
| `None` | 2 | The device failed the check, or the player is on a platform that can't be verified. |
| `Standard` | 3 | The device passed some of the checks, but not all of them. |
| `Full` | 4 | The device passed every check. |