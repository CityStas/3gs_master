---
name: AssetTypeVerification
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the asset type verification mode."
---

# AssetTypeVerification

Determines the asset type verification mode.

**Type:** enum

## Description

Determines the asset type verification mode used when calling
[Humanoid:ApplyDescriptionAsync()](/docs/reference/engine/classes/Humanoid.md) or
[Players:CreateHumanoidModelFromDescriptionAsync()](/docs/reference/engine/classes/Players.md). This verification
mode determines if the method will load models or not. Loading models can be
insecure if it's possible for malicious users to trick your game into loading
unexpected models that you own which may include malicious scripts. You should
set this to `Always` unless you want to load non-catalog assets.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 1 | Use the default behavior for asset type verification. |
| `ClientOnly` | 2 | Only verify asset types on the client. Asset type verification can not be turned off on the client. |
| `Always` | 3 | Always verify the asset types to be loaded and disallow loading models. |