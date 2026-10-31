---
name: LexemeType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the category of a token produced when the Studio Explorer filter bar lexes a filter expression."
---

# LexemeType

Identifies the category of a token produced when the Studio Explorer filter
bar lexes a filter expression.

**Type:** enum

## Description

Studio-only Explorer filter lexer token kinds — not used by experience
scripts. Classifies each token produced while tokenizing text in the Studio
Explorer filter search bar. The lexer assigns one of these categories to every
token; the parser builds an expression tree that the filter evaluates against
the Explorer hierarchy.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Eof` | 0 | End-of-input token emitted when the lexer reaches the end of the filter string. |
| `Name` | 1 | An unquoted identifier token, such as an instance name or property key in a filter expression. |
| `QuotedString` | 2 | A string literal token delimited by single (`'`) or double (`"`) quotes, with backslash escape support. |
| `Number` | 3 | A numeric literal token representing an integer or decimal value used in a comparison. |
| `And` | 4 | The case-insensitive keyword `and`, used to combine filter conditions with logical AND. |
| `Or` | 5 | The case-insensitive keyword `or`, used to combine filter conditions with logical OR. |
| `Equal` | 6 | The equality comparison operator, matched as `=` or `==` in a filter expression. |
| `TildeEqual` | 7 | The not-equal comparison operator (`~=`). |
| `GreaterThan` | 8 | The greater-than comparison operator (`>`). |
| `GreaterThanEqual` | 9 | The greater-than-or-equal comparison operator (`>=`). |
| `LessThan` | 10 | The less-than comparison operator (`<`). |
| `LessThanEqual` | 11 | The less-than-or-equal comparison operator (`<=`). |
| `Colon` | 12 | The colon character (`:`), used as a separator in filter expressions such as `ClassName:PropertyName`. |
| `Dot` | 13 | The dot character (`.`), used to navigate nested property paths in a filter expression. |
| `LeftParenthesis` | 14 | The opening parenthesis character (`(`), used to begin a grouped subexpression in a filter. |
| `RightParenthesis` | 15 | The closing parenthesis character (`)`), used to end a grouped subexpression in a filter. |
| `Star` | 16 | The single wildcard character (`*`), used to match any single name segment in a filter path. |
| `DoubleStar` | 17 | The double wildcard token (`**`), which matches any number of path segments recursively across the instance hierarchy. |
| `ReservedSpecial` | 18 | A character that is syntactically recognized but has no defined meaning in the current filter grammar. |