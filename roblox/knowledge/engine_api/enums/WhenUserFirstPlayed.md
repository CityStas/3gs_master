---
name: WhenUserFirstPlayed
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes when a player first played the current experience, represented as a bucket."
---

# WhenUserFirstPlayed

Describes when a player first played the current experience, represented as a
bucket.

**Type:** enum

## Description

The `WhenUserFirstPlayed` enum describes when a player first played the
current experience, represented as a bucket.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Segment data is unavailable. |
| `Days0To30` | 1 | The player first played the experience within the last 30 days. |
| `Days31To90` | 2 | The player first played the experience between 31 and 90 days ago. |
| `Days91To180` | 3 | The player first played the experience between 91 and 180 days ago. |
| `Days181To365` | 4 | The player first played the experience between 181 and 365 days ago. |
| `Days366Plus` | 5 | The player first played the experience more than 365 days ago. |