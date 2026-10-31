---
name: TextTruncate
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the truncation of text when using the `TextTruncate` property."
---

# TextTruncate

Controls the truncation of text when using the `TextTruncate` property.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Text is not truncated. |
| `AtEnd` | 1 | Text is truncated at the end of the text; extra graphemes that cannot fit into the space are replaced with `...`. Word boundaries are respected if possible.  For example, if the control is between -> and <- like so:  `->Long text is truncated at the en<-d of the last complete word`  The text will be:  `Long text is truncated at the...` |
| `SplitWord` | 2 | If the end of the line occurs in the middle of a word, the text is truncated inside of that word. Extra graphemes that cannot fit into the space are replaced with `...`.  For example, if the control is between -> and <- like so:  `->Long text is truncated at the en<-d of the last complete word`  The text will be:  `Long text is truncated at the en...` |