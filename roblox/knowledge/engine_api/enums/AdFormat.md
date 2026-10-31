---
name: AdFormat
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the format of an ad used with AdService methods."
---

# AdFormat

Specifies the format of an ad used with [AdService](/docs/reference/engine/classes/AdService.md) methods.

**Type:** enum

## Description

Specifies the format of an ad passed to [AdService](/docs/reference/engine/classes/AdService.md) methods such as
[AdService:GetAdAvailabilityNowAsync()](/docs/reference/engine/classes/AdService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `RewardedVideo` | 0 | A full-screen video ad that plays to completion and rewards the viewer, used as the `adFormat` argument for [AdService](/docs/reference/engine/classes/AdService.md) methods. |