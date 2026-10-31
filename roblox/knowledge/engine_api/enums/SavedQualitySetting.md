---
name: SavedQualitySetting
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Represents the user's saved graphics quality preference, stored in UserGameSettings.SavedQualityLevel."
---

# SavedQualitySetting

Represents the user's saved graphics quality preference, stored in
[UserGameSettings.SavedQualityLevel](/docs/reference/engine/classes/UserGameSettings.md).

**Type:** enum

## Description

Represents the user's saved graphics quality preference, stored in
[UserGameSettings.SavedQualityLevel](/docs/reference/engine/classes/UserGameSettings.md). When set to
[SavedQualitySetting.Automatic](/docs/reference/engine/enums/SavedQualitySetting.md), the engine selects quality automatically
based on device performance; otherwise the chosen level (1–10) is persisted
across sessions and applied as the initial quality setting on next launch.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Graphics quality is determined automatically based on device performance. |
| `QualityLevel1` | 1 | Saved graphics quality level 1 — the lowest explicit quality setting. |
| `QualityLevel2` | 2 | Saved graphics quality level 2. |
| `QualityLevel3` | 3 | Saved graphics quality level 3. |
| `QualityLevel4` | 4 | Saved graphics quality level 4. |
| `QualityLevel5` | 5 | Saved graphics quality level 5. |
| `QualityLevel6` | 6 | Saved graphics quality level 6. |
| `QualityLevel7` | 7 | Saved graphics quality level 7. |
| `QualityLevel8` | 8 | Saved graphics quality level 8. |
| `QualityLevel9` | 9 | Saved graphics quality level 9. |
| `QualityLevel10` | 10 | Saved graphics quality level 10 — the highest explicit quality setting. |