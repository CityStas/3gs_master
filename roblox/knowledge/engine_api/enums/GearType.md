---
name: GearType
last_updated: 2026-10-30T19:55:54Z
type: enum
tags:
  - Deprecated
summary: "Categorizes gear items by type for use with deprecated gear-allowlist properties."
---

# GearType

Categorizes gear items by type for use with deprecated gear-allowlist
properties.

**Type:** enum

## Description

The GearType Enum is used as an argument in
[DataModel:IsGearTypeAllowed()](/docs/reference/engine/classes/DataModel.md). Gear may have more than one
type/attribute.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `MeleeWeapons` | 0 | Gear with the 'Melee' attribute. |
| `RangedWeapons` | 1 | Gear with the 'Ranged' attribute. |
| `Explosives` | 2 | Gear with the 'Explosive' attribute. |
| `PowerUps` | 3 | Gear with the 'Power Up' attribute. |
| `NavigationEnhancers` | 4 | Gear with the 'Navigation' attribute. |
| `MusicalInstruments` | 5 | Gear with the 'Musical' attribute. |
| `SocialItems` | 6 | Gear with the 'Social' attribute. |
| `BuildingTools` | 7 | Gear with the 'Building' attribute. |
| `Transport` | 8 | Gear with the 'Transport' attribute. |