---
name: MembershipType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The membership type of a Player."
---

# MembershipType

The membership type of a Player.

**Type:** enum

## Description

Describes the paid-membership tier associated with a [Player](/docs/reference/engine/classes/Player.md). The value
is exposed via the [Player.MembershipType](/docs/reference/engine/classes/Player.md) property, which defaults to
[MembershipType.None](/docs/reference/engine/enums/MembershipType.md) and is set automatically by the server when the
player joins. Prefer [Player.HasRobloxSubscription](/docs/reference/engine/classes/Player.md) to check for an
active paid subscription.

The legacy Builders Club tiers ([MembershipType.BuildersClub](/docs/reference/engine/enums/MembershipType.md),
[MembershipType.TurboBuildersClub](/docs/reference/engine/enums/MembershipType.md),
[MembershipType.OutrageousBuildersClub](/docs/reference/engine/enums/MembershipType.md)) are no longer available for
purchase and are retained only for backward compatibility. All active paid
memberships are represented by [MembershipType.Premium](/docs/reference/engine/enums/MembershipType.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The player does not have an active paid membership. |
| `BuildersClub` | 1 | Legacy Builders Club membership. No longer available for purchase; retained for compatibility. Active paid memberships use [MembershipType.Premium](/docs/reference/engine/enums/MembershipType.md). |
| `TurboBuildersClub` | 2 | Legacy Turbo Builders Club membership. No longer available for purchase; retained for compatibility. Active paid memberships use [MembershipType.Premium](/docs/reference/engine/enums/MembershipType.md). |
| `OutrageousBuildersClub` | 3 | Legacy Outrageous Builders Club membership. No longer available for purchase; retained for compatibility. Active paid memberships use [MembershipType.Premium](/docs/reference/engine/enums/MembershipType.md). |
| `Premium` | 4 | The player has an active Premium membership. |