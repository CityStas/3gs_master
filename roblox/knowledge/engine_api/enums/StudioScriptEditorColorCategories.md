---
name: StudioScriptEditorColorCategories
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Color categories used to theme the Script Editor in Roblox Studio."
---

# StudioScriptEditorColorCategories

Color categories used to theme the Script Editor in Roblox Studio.

**Type:** enum

## Description

Identifies visual element categories whose colors can be customized in the
Roblox Studio Script Editor theme system. Each value is a distinct syntactic
or UI region in the editor.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Fallback foreground color used for script text that does not match any more specific syntax category. |
| `Operator` | 1 | Color applied to operator tokens such as `+`, `-`, `*`, `/`, `==`, and `..` in scripts. |
| `Number` | 2 | Color applied to numeric literal tokens in scripts. |
| `String` | 3 | Color applied to string literal tokens, including quoted strings and long-string literals. |
| `Comment` | 4 | Color applied to comment tokens (single-line `--` and block `--[[ ]]` comments) in scripts. |
| `Keyword` | 5 | Color applied to Luau reserved keywords such as `if`, `then`, `else`, `do`, `end`, `return`, and `while`. |
| `Builtin` | 6 | Color applied to Luau built-in functions and standard library identifiers in scripts. |
| `Method` | 7 | Color applied to method call identifiers in scripts. |
| `Property` | 8 | Color applied to property access identifiers (tokens following a `.` operator) in scripts. |
| `Nil` | 9 | Color applied to the `nil` literal token in scripts. |
| `Bool` | 10 | Foreground color used to highlight boolean literals (`true` and `false`) in scripts. |
| `Function` | 11 | Color applied to the `function` keyword token in function declarations. |
| `Local` | 12 | Color applied to the `local` keyword token in local variable and function declarations. |
| `Self` | 13 | Color applied to the `self` identifier token in method bodies. |
| `LuauKeyword` | 14 | Color applied to Luau-specific type annotation keywords such as `type` and `typeof`. |
| `FunctionName` | 15 | Color applied to the identifier that names a function in its declaration. |
| `TODO` | 16 | Color applied to `TODO` markers found inside comments in scripts. |
| `Background` | 17 | Main background color of the Script Editor canvas. |
| `SelectionText` | 18 | Foreground color for text within the currently selected range in the Script Editor. |
| `SelectionBackground` | 19 | Background highlight color for the currently selected text range in the Script Editor. |
| `FindSelectionBackground` | 20 | Background highlight color applied to text ranges matched by a Find or Replace operation. |
| `MatchingWordBackground` | 21 | Background highlight color applied to all occurrences of the word under the cursor when word-highlight is active. |
| `Warning` | 22 | Color used for warning-severity diagnostic markers and underlines in scripts. |
| `Error` | 23 | Color used for error-severity diagnostic markers and underlines in scripts. |
| `Info` | 24 | Color used for information-severity diagnostic markers in scripts. |
| `Hint` | 25 | Color used for hint-severity diagnostic markers in scripts. |
| `Whitespace` | 26 | Color used to render visible whitespace characters (spaces and tabs) when that display option is enabled. |
| `ActiveLine` | 27 | Background highlight color applied to the line that currently contains the text cursor. |
| `DebuggerCurrentLine` | 28 | Background highlight color for the line the debugger is currently paused on. |
| `DebuggerErrorLine` | 29 | Background highlight color for a line that caused a runtime error during a debugging session. |
| `Ruler` | 30 | Color of the vertical column ruler line drawn at the configured character-width limit in the Script Editor. |
| `Bracket` | 31 | Color applied to bracket characters such as `(`, `)`, `[`, `]`, `{`, and `}` in scripts. |
| `Type` | 32 | Color applied to Luau type name tokens in type annotations and declarations. |
| `MenuPrimaryText` | 33 | Primary text color for items listed in autocomplete and context-menu popups. |
| `MenuSecondaryText` | 34 | Secondary text color (for example, type annotations or documentation hints) in autocomplete popups. |
| `MenuSelectedText` | 35 | Text color of the currently highlighted item in autocomplete and context-menu popups. |
| `MenuBackground` | 36 | Background color for autocomplete and context-menu popups in the Script Editor. |
| `MenuSelectedBackground` | 37 | Background color of the currently highlighted item in autocomplete and context-menu popups. |
| `MenuScrollbarBackground` | 38 | Background color of the scrollbar track inside autocomplete and context-menu popups. |
| `MenuScrollbarHandle` | 39 | Color of the scrollbar thumb (handle) inside autocomplete and context-menu popups. |
| `MenuBorder` | 40 | Border color for autocomplete and context-menu popups in the Script Editor. |
| `DocViewCodeBackground` | 41 | Background color for inline code blocks rendered in the documentation viewer panel within Studio. |
| `AICOOverlayText` | 42 | Text color for labels displayed in the AI Code Overlay panel. |
| `AICOOverlayButtonBackground` | 43 | Background color for AI Code Overlay action buttons in their default (idle) state. |
| `AICOOverlayButtonBackgroundHover` | 44 | Background color for AI Code Overlay action buttons when the pointer hovers over them. |
| `AICOOverlayButtonBackgroundPressed` | 45 | Background color for AI Code Overlay action buttons while they are being pressed. |
| `IndentationRuler` | 46 | Color of the vertical guide lines drawn at each indentation level in the script editor gutter. |