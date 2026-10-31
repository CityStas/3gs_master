---
name: AvatarSettingsBuildMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether players can freely scale their avatar body or whether the experience enforces custom scale ranges."
---

# AvatarSettingsBuildMode

Determines whether players can freely scale their avatar body or whether the
experience enforces custom scale ranges.

**Type:** enum

## Description

Determines whether avatar body scaling in an experience uses full
platform-wide limits (player's choice) or creator-defined custom ranges. This
enum is used by the `BuildMode` property to control how avatar height, width,
head, body type, and proportions scales are constrained when a player joins
the experience.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerChoice` | 0 | Players can scale their avatar body freely within the full platform-wide limits. This is the default value. |
| `CustomBuild` | 1 | The experience enforces creator-defined min/max ranges for avatar body scales (height, width, head, body type, and proportions), overriding the platform defaults. |