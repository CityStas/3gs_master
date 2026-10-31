---
name: UserAcquisitionSource
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how a player first found the current experience."
---

# UserAcquisitionSource

Describes how a player first found the current experience.

**Type:** enum

## Description

The `UserAcquisitionSource` enum describes how a player first found the
current experience.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `PendingAttribution` | 1 | The player started playing recently, and their acquisition source is not available yet. |
| `HomeRecommendation` | 2 | The player first joined from a recommendation on the Home page. |
| `ContinueToPlay` | 3 | The player first joined from the Continue section. |
| `Curation` | 4 | The player first joined from content curated by Roblox, such as featured experiences or events. |
| `Friends` | 5 | The player first joined through a friend. |
| `Search` | 6 | The player first joined from search results. |
| `Teleport` | 7 | The player first joined by teleporting from another experience. |
| `Ads` | 8 | The player first joined from an ad, such as a sponsored ad, search ad, or portal ad. |
| `HomeOther` | 9 | The player first joined from a part of the Roblox app other than Home recommendations, such as Charts or Favorites. |
| `Other` | 10 | The player first joined from another source, such as a share link, chat, or a notification. |