---
name: TextDirection
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the base text rendering direction for TextLabel, TextButton, and TextBox instances."
---

# TextDirection

Controls the base text rendering direction for [TextLabel](/docs/reference/engine/classes/TextLabel.md),
[TextButton](/docs/reference/engine/classes/TextButton.md), and [TextBox](/docs/reference/engine/classes/TextBox.md) instances.

**Type:** enum

## Description

Controls the base paragraph direction used when laying out text. Used by
[TextLabel.TextDirection](/docs/reference/engine/classes/TextLabel.md), [TextButton.TextDirection](/docs/reference/engine/classes/TextButton.md), and
[TextBox.TextDirection](/docs/reference/engine/classes/TextBox.md), which default to [TextDirection.Auto](/docs/reference/engine/enums/TextDirection.md).

[TextDirection.Auto](/docs/reference/engine/enums/TextDirection.md) lets the Unicode Bidirectional Algorithm determine
the paragraph's base direction from the first strong directional character.
[TextDirection.LeftToRight](/docs/reference/engine/enums/TextDirection.md) or [TextDirection.RightToLeft](/docs/reference/engine/enums/TextDirection.md) pins the
base direction regardless of content, which is useful for mixed-script strings
where automatic detection would choose the wrong base.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Auto` | 0 | Automatically determines text direction from the first strong directional character using the Unicode Bidirectional Algorithm. |
| `LeftToRight` | 1 | Forces the paragraph base direction to left-to-right regardless of the text content. |
| `RightToLeft` | 2 | Forces the paragraph base direction to right-to-left regardless of the text content. |