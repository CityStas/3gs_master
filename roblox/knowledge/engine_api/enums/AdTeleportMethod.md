---
name: AdTeleportMethod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the method by which a player teleports during an immersive ad portal flow."
---

# AdTeleportMethod

Describes the method by which a player teleports during an immersive ad portal
flow.

**Type:** enum

## Description

Describes the user-initiated method by which a player teleports during an
immersive ad portal flow, distinguishing forward travel to the advertiser's
experience from a return to the publisher's experience.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Undefined` | 0 | Default uninitialized sentinel value indicating that no teleport method has been determined yet. |
| `PortalForward` | 1 | The player teleported forward to the advertiser's destination experience by walking into an [AdPortal](/docs/reference/engine/classes/AdPortal.md). |
| `InGameMenuBackButton` | 2 | The player initiated a return teleport to the publisher's experience by pressing the back button in the in-game menu. |
| `UIBackButton` | 3 | The player initiated a return teleport to the publisher's experience by pressing a back button rendered in the ad destination's UI overlay. |