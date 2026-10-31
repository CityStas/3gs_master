---
name: Genre
last_updated: 2026-10-30T19:55:54Z
type: enum
tags:
  - Deprecated
summary: "Used to represent the type of game."
---

# Genre

Used to represent the type of game.

**Type:** enum

## Description

`Genre` categorizes an experience by its play-style theme. Its only consumer
is the [DataModel.Genre](/docs/reference/engine/classes/DataModel.md) property, which is deprecated and no longer
functional — reading [DataModel.Genre](/docs/reference/engine/classes/DataModel.md) may throw an error. The enum
values are listed here for reference only; new experiences should not depend
on this enum.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 0 | The game's genre is set to All. The game will be listed as all possible genres. |
| `TownAndCity` | 1 | The game's genre is set to Town and City. |
| `Fantasy` | 2 | The game's genre is set to Fantasy. |
| `SciFi` | 3 | The game's genre is set to SciFi (Science Fiction). |
| `Ninja` | 4 | The game's genre is set to Ninja. |
| `Scary` | 5 | The game's genre is set to Scary. |
| `Pirate` | 6 | The game's genre is set to Pirate. |
| `Adventure` | 7 | The game's genre is set to Adventure. |
| `Sports` | 8 | The game's genre is set to Sports. |
| `Funny` | 9 | The game's genre is set to Funny. |
| `WildWest` | 10 | The game's genre is set to Wild West. |
| `War` | 11 | The game's genre is set to War. |
| `SkatePark` | 12 | The game's genre is set to Skate Park. |
| `Tutorial` | 13 | The game's genre is set to Tutorial. |