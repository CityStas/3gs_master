---
name: ScrollBarInset
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used with ScrollingFrame.HorizontalScrollBarInset and ScrollingFrame.VerticalScrollBarInset to indicate whether the canvas should be inset by ScrollBarThickness for the respective scroll bar."
---

# ScrollBarInset

This enum is used with [ScrollingFrame.HorizontalScrollBarInset](/docs/reference/engine/classes/ScrollingFrame.md) and
[ScrollingFrame.VerticalScrollBarInset](/docs/reference/engine/classes/ScrollingFrame.md) to indicate whether the canvas
should be inset by
[ScrollBarThickness](/docs/reference/engine/classes/ScrollingFrame.md) for the
respective scroll bar.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The canvas will never be inset for the respective scroll bar. |
| `ScrollBar` | 1 | The canvas will only be inset if the respective scroll bar is showing. |
| `Always` | 2 | The canvas will always be inset for the respective scroll bar, regardless of whether that scroll bar is showing. |