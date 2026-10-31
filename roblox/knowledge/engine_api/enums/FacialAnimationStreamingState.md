---
name: FacialAnimationStreamingState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A bitmask enum describing which facial animation streaming capabilities are active for a user or service."
---

# FacialAnimationStreamingState

A bitmask enum describing which facial animation streaming capabilities are
active for a user or service.

**Type:** enum

## Description

`FacialAnimationStreamingState` is a bitmask enum that represents which facial
animation streaming modalities are currently enabled. Values can be combined
via bitwise OR to represent multiple active states simultaneously. It covers
both per-user opt-in state and place- or server-level enablement.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Indicates that no facial animation streaming is active. |
| `Audio` | 1 | Indicates that audio-based facial animation streaming is enabled for the user. |
| `Video` | 2 | Indicates that video-based facial animation streaming is enabled for the user. |
| `Place` | 4 | Indicates that facial animation streaming is enabled at the place level. |
| `Server` | 8 | Indicates that facial animation streaming is enabled at the server level. |