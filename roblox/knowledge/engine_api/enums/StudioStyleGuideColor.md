---
name: StudioStyleGuideColor
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "An enum that lists color roles used by Studio themes, passed to StudioTheme:GetColor() to retrieve the correct theme color for a given UI element in a plugin."
---

# StudioStyleGuideColor

An enum that lists color roles used by Studio themes, passed to
[StudioTheme:GetColor()](/docs/reference/engine/classes/StudioTheme.md) to retrieve the correct theme color for a given
UI element in a plugin.

**Type:** enum

## Description

Named color roles in Roblox Studio's theming system. Each item is a UI color
slot, not a literal color. Pass with [StudioStyleGuideModifier](/docs/reference/engine/enums/StudioStyleGuideModifier.md) to
[StudioTheme:GetColor()](/docs/reference/engine/classes/StudioTheme.md) to get the active theme's [Color3](/docs/reference/engine/datatypes/Color3.md) so
plugin widgets adapt when the user switches Light/Dark themes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `MainBackground` | 0 | The primary background color used by the toolbar and windows. |
| `Titlebar` | 1 | The color of windows' title bars. |
| `Dropdown` | 2 | The color of dropdown menus, like those found in the Properties window. |
| `Tooltip` | 3 | The background color of tooltips, like those seen when hovering over buttons on the toolbar or properties in the Properties window. |
| `Notification` | 4 | The background color of message box and dialog notification panels. |
| `ScrollBar` | 5 | The color of scrollbar handles, like those seen in the Explorer window. |
| `ScrollBarBackground` | 6 | The background color of scrollbars, like those seen in the Explorer window. |
| `TabBar` | 7 | The background color of the tab bar, like the one where the script editor is opened. |
| `Tab` | 8 | The color of tabs on the tab bar, like the ones opened when the script editor is opened. |
| `FilterButtonDefault` | 9 | The default background color of filter buttons in the Script Analysis widget. |
| `FilterButtonHover` | 10 | The background color of filter buttons in the Script Analysis widget when hovered. |
| `FilterButtonChecked` | 11 | The background color of filter buttons in the Script Analysis widget when they are in a checked (active) state. |
| `FilterButtonAccent` | 12 | The accent color drawn on the top and left edges of filter buttons in the Script Analysis widget. |
| `FilterButtonBorder` | 13 | The border color of filter buttons in the Script Analysis widget. |
| `FilterButtonBorderAlt` | 14 | The border color of filter buttons in the Script Analysis widget when they are hovered or checked. |
| `RibbonTab` | 15 | The color of a tab on the toolbar menu. |
| `RibbonTabTopBar` | 16 | The background color of the toolbar. |
| `Button` | 17 | The background color of clickable buttons. |
| `MainButton` | 18 | The background color of clickable buttons that are the primary action. |
| `RibbonButton` | 19 | The background color of buttons on the toolbar. |
| `ViewPortBackground` | 20 | The background color of the game viewport. |
| `InputFieldBackground` | 21 | The background color of input fields, like those found in the Explorer window. |
| `Item` | 22 | The background color of items listed in the Explorer and Properties windows. |
| `TableItem` | 23 | The background color of row items in table views such as the Game Settings window. |
| `CategoryItem` | 24 | The background color of category header items in the Properties widget. |
| `GameSettingsTableItem` | 25 | The color of items within tables in the settings window. |
| `GameSettingsTooltip` | 26 | The color of tooltips in the settings window. |
| `EmulatorBar` | 27 | The color of the bar shown when the mobile emulator is active. |
| `EmulatorDropDown` | 28 | The color of the device and physical size dropdowns in the emulator bar. |
| `ColorPickerFrame` | 29 | The background color of the color picker. |
| `CurrentMarker` | 30 | The color of the current-item marker, such as the blue selection indicator in the logout menu in the Light theme. |
| `Border` | 31 | The color of borders, like those found in the Properties window. |
| `DropShadow` | 32 | The color used for drop-shadow decorations on floating panels and menus. |
| `Shadow` | 33 | The color of shadows rendered under floating items like dropdowns. |
| `Light` | 34 | The light role color from the Qt widget palette, used for the lightest shading of 3D widget effects. |
| `Dark` | 35 | The dark role color from the Qt widget palette, used for the darkest shading of 3D widget effects. |
| `Mid` | 36 | The mid role color from the Qt widget palette, used between the button and dark shading for 3D widget effects. |
| `MainText` | 37 | The primary text color used throughout Studio's UI. |
| `SubText` | 38 | The color of secondary text such as status labels shown in the Team Create widget for offline users and place owners. |
| `TitlebarText` | 39 | The text color displayed in dock widget title bars and Ribbon tabs. |
| `BrightText` | 40 | The color of text displayed inside input fields and other high-contrast contexts. |
| `DimmedText` | 41 | The color of placeholder or dimmed text shown in empty input fields. |
| `LinkText` | 42 | The color of hyperlink text in Studio panels and documentation views. |
| `WarningText` | 43 | The color of warning messages, such as those displayed in the Output window. |
| `ErrorText` | 44 | The color of error messages, such as those displayed in the Output window. |
| `InfoText` | 45 | The color of informational messages, such as those displayed in the Output window. |
| `SensitiveText` | 46 | The color used to display sensitive information text, such as certain messages in the Output window. |
| `ScriptSideWidget` | 47 | The background color of the Script Editor's side gutter, which displays fold icons and breakpoint markers. |
| `ScriptBackground` | 48 | The background color of the Script Editor canvas. |
| `ScriptText` | 49 | The default text color for unclassified tokens in the Script Editor. |
| `ScriptSelectionText` | 50 | The foreground text color of the active text selection in the Script Editor. |
| `ScriptSelectionBackground` | 51 | The background color of the active text selection in the Script Editor. |
| `ScriptFindSelectionBackground` | 52 | The background color of text matched by the current find query in the Script Editor. |
| `ScriptMatchingWordSelectionBackground` | 53 | The background color of all occurrences of the word under the cursor highlighted as matching selections in the Script Editor. |
| `ScriptOperator` | 54 | The color of operator symbols in the Script Editor. |
| `ScriptNumber` | 55 | The color of numeric literals in the Script Editor. |
| `ScriptString` | 56 | The color of string literals in the Script Editor. |
| `ScriptComment` | 57 | The color of comment text in the Script Editor. |
| `ScriptKeyword` | 58 | The color of Lua reserved keywords that don't have a more specific color role in the Script Editor. |
| `ScriptBuiltInFunction` | 59 | The color of recognized built-in global identifiers in the Script Editor, including non-function globals. |
| `ScriptWarning` | 60 | The color of warning markers and underlines in the Script Editor. |
| `ScriptError` | 61 | The color of error markers and underlines in the Script Editor. |
| `ScriptInformation` | 62 | The color of informational diagnostic markers in the Script Editor. |
| `ScriptHint` | 63 | The color of hint diagnostic underlines and scrollbar markers in the Script Editor. |
| `ScriptWhitespace` | 64 | The color of rendered whitespace characters (spaces and tabs) when whitespace display is enabled in the Script Editor. |
| `ScriptRuler` | 65 | The color of the column ruler line displayed in the Script Editor when the ruler is enabled. |
| `DocViewCodeBackground` | 66 | The background color of inline code blocks in the Script Editor's documentation view. |
| `DebuggerCurrentLine` | 67 | The highlight color applied to the line currently paused on in the script debugger. |
| `DebuggerErrorLine` | 68 | The highlight color applied to a line that caused a debugger error or runtime exception. |
| `DiffFilePathText` | 69 | The text color of the file path displayed in the header row of a diff view. |
| `DiffTextHunkInfo` | 70 | The text color of hunk-info lines (the `@@` header rows) in the diff view. |
| `DiffTextNoChange` | 71 | The text color of unchanged context lines in the diff view. |
| `DiffTextAddition` | 72 | The text color of added lines in the diff view. |
| `DiffTextDeletion` | 73 | The text color of deleted lines in the diff view. |
| `DiffTextSeparatorBackground` | 74 | The background color of hunk-separator rows in the diff view text area. |
| `DiffTextNoChangeBackground` | 75 | The background color of unchanged context lines in the diff view. |
| `DiffTextAdditionBackground` | 76 | The background color of added lines in the diff view. |
| `DiffTextDeletionBackground` | 77 | The background color of deleted lines in the diff view. |
| `DiffLineNum` | 78 | The text color of line numbers in the diff view gutter. |
| `DiffLineNumSeparatorBackground` | 79 | The background color of line-number cells in the diff gutter for hunk-separator rows. |
| `DiffLineNumNoChangeBackground` | 80 | The background color of line-number cells in the diff gutter for unchanged lines. |
| `DiffLineNumAdditionBackground` | 81 | The background color of line-number cells in the diff gutter for added lines. |
| `DiffLineNumDeletionBackground` | 82 | The background color of line-number cells in the diff gutter for deleted lines. |
| `DiffFilePathBackground` | 83 | The background color of the file-path header row in a diff view. |
| `DiffFilePathBorder` | 84 | The border color of the file-path header row in a diff view. |
| `ChatIncomingBgColor` | 85 | The background color of incoming messages in the Studio chat widget. |
| `ChatIncomingTextColor` | 86 | The text color of incoming messages in the Studio chat widget. |
| `ChatOutgoingBgColor` | 87 | The background color of outgoing messages in the Studio chat widget. |
| `ChatOutgoingTextColor` | 88 | The text color of outgoing messages in the Studio chat widget. |
| `ChatModeratedMessageColor` | 89 | The color used to display moderated or filtered messages in the Studio chat widget. |
| `Separator` | 90 | The color of separator lines that divide sections within Studio panels. |
| `ButtonBorder` | 91 | The border color of standard clickable buttons. |
| `ButtonText` | 92 | The label text color of standard clickable buttons. |
| `InputFieldBorder` | 93 | The border color of text input fields throughout Studio. |
| `CheckedFieldBackground` | 94 | The background color of checkbox and checked-state input fields. |
| `CheckedFieldBorder` | 95 | The border color of checkbox and checked-state input fields. |
| `CheckedFieldIndicator` | 96 | The color of the check mark or indicator drawn inside a checked input field. |
| `HeaderSection` | 97 | The background color of section header rows in Studio widgets such as the Properties window. |
| `Midlight` | 98 | The midlight role color from the Qt widget palette, used between the button and light shading for 3D widget effects. |
| `StatusBar` | 99 | The color of the status bar shown at the bottom of Studio, if it is visible. |
| `DialogButton` | 100 | The background color of standard buttons in modal dialog boxes. |
| `DialogButtonText` | 101 | The label text color of standard buttons in modal dialog boxes. |
| `DialogButtonBorder` | 102 | The border color of standard buttons in modal dialog boxes. |
| `DialogMainButton` | 103 | The background color of the primary action button (such as OK or Save) in modal dialog boxes. |
| `DialogMainButtonText` | 104 | The label text color of the primary action button in modal dialog boxes. |
| `InfoBarWarningBackground` | 105 | The background color of the warning bar that appears at the top of a widget to surface important notices. |
| `InfoBarWarningText` | 106 | The text color of warning messages inside the info bar warning strip. |
| `ScriptEditorCurrentLine` | 107 | The background highlight color applied to the line containing the cursor in the Script Editor. |
| `ScriptMethod` | 108 | The color of function-call target identifiers in the Script Editor, including bare functions and indexed methods. |
| `ScriptProperty` | 109 | The color of property name identifiers in the Script Editor. |
| `ScriptNil` | 110 | The color of the `nil` literal in the Script Editor. |
| `ScriptBool` | 111 | The color of boolean literals (`true` and `false`) in the Script Editor. |
| `ScriptFunction` | 112 | The color of the `function` keyword token in the Script Editor. |
| `ScriptLocal` | 113 | The color of the `local` keyword in the Script Editor. |
| `ScriptSelf` | 114 | The color of the `self` identifier in the Script Editor. |
| `ScriptLuauKeyword` | 115 | The color of Luau-specific keywords (such as type annotation keywords) in the Script Editor. |
| `ScriptFunctionName` | 116 | The color of function name identifiers in the Script Editor. |
| `ScriptTodo` | 117 | The highlight color applied to TODO annotations in script comments. |
| `ScriptBracket` | 118 | The color of parentheses, braces, and square brackets in the Script Editor. |
| `AttributeCog` | 119 | The color of the attribute cog icon shown in the Properties widget. |
| `AICOOverlayText` | 128 | The text color used inside the AI companion (AICO) overlay panel. |
| `AICOOverlayButtonBackground` | 129 | The background color of buttons in the AI companion (AICO) overlay panel. |
| `AICOOverlayButtonBackgroundHover` | 130 | The background color of buttons in the AI companion (AICO) overlay panel when hovered. |
| `AICOOverlayButtonBackgroundPressed` | 131 | The background color of buttons in the AI companion (AICO) overlay panel when pressed. |
| `OnboardingCover` | 132 | The overlay color used to dim non-focused areas during onboarding flows. |
| `OnboardingHighlight` | 133 | The highlight color used to draw attention to a UI element during onboarding flows. |
| `OnboardingShadow` | 134 | The shadow color used beneath highlighted elements during onboarding flows. |
| `BreakpointMarker` | 136 | The color of the breakpoint marker shown in the script editor gutter. |
| `DiffLineNumHover` | 137 | The text color of line numbers in the diff gutter when hovered. |
| `DiffLineNumSeparatorBackgroundHover` | 138 | The background color of line-number cells in the diff gutter for hunk-separator rows when hovered. |