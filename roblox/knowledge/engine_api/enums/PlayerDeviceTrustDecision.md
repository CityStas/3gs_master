---
name: PlayerDeviceTrustDecision
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The decision that IntegrityService.EvaluatePlayerDeviceTrust returns for a player."
---

# PlayerDeviceTrustDecision

The decision that [IntegrityService.EvaluatePlayerDeviceTrust](/docs/reference/engine/classes/IntegrityService.md) returns
for a player.

**Type:** enum

## Description

The decision that [IntegrityService.EvaluatePlayerDeviceTrust](/docs/reference/engine/classes/IntegrityService.md) returns
in the `Action` field of its result, which tells Roblox whether a player can
stay in the server based on their device trust level.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Accept` | 0 | The player stays in the server. |
| `Reject` | 1 | The player is disconnected from the server and sees a rejection message. |