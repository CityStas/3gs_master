---
name: ElasticBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used by ScrollingFrame.ElasticBehavior to control when elastic scrolling is active on touch‑enabled devices."
---

# ElasticBehavior

This enum is used by [ScrollingFrame.ElasticBehavior](/docs/reference/engine/classes/ScrollingFrame.md) to control when
elastic scrolling is active on touch‑enabled devices.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `WhenScrollable` | 0 | Scrolling is elastic when there is content to be scrolled to. |
| `Always` | 1 | Scrolling is always elastic, even when there isn't content available to scroll to. |
| `Never` | 2 | Scrolling is never elastic and the canvas will never scroll beyond its bounds. |