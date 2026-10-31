---
name: UITheme
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Deprecated Studio UI color theme (`Light` or `Dark`)."
---

# UITheme

Deprecated Studio UI color theme (`Light` or `Dark`).

**Type:** enum

## Description

A deprecated enum that previously represented the Studio UI color theme. It
was exposed through the `UI_Theme` property (also deprecated) and contained
[UITheme.Light](/docs/reference/engine/enums/UITheme.md) and [UITheme.Dark](/docs/reference/engine/enums/UITheme.md). The enum is retained only for
backward compatibility with existing plugins that reference it; it has no
effect. Use [Studio.Theme](/docs/reference/engine/classes/Studio.md) to read or set the current
[StudioTheme](/docs/reference/engine/classes/StudioTheme.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Light` | 0 | The light Studio UI color theme. Deprecated; has no effect. |
| `Dark` | 1 | The dark Studio UI color theme. Deprecated; has no effect. |