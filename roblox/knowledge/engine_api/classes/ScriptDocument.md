---
name: ScriptDocument
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Represents the ephemeral state of an open document in the Studio Script Editor, providing APIs for reading and editing code."
---

# Class: ScriptDocument

> Represents the ephemeral state of an open document in the Studio Script
> Editor, providing APIs for reading and editing code.

## Description

A [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) instance is a proxy of the document of a Studio
Script Editor. It's different from the [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) open in the
editor in that it represents the ephemeral state of an open document, and its
representation is in a format that's more suited for reading and editing code
than executing it. In particular, [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) reflects any changes
that have been made to the open script in Drafts Mode, which the source
property doesn't.

The Script Editor itself exists and changes on a different thread than any
[DataModel](/docs/reference/engine/classes/DataModel.md), so the [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) replicates the open Script
Editor, but it isn't the open editor. Because of the replication, there's
sometimes a slight delay between changing the text in the editor and updating
the [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md). The delay usually occurs because the
[DataModel](/docs/reference/engine/classes/DataModel.md) is busy, and it's almost always extremely small, but it
still exists.

The existence of a [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) indicates that a document is open in
the Script Editor. All [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) instances have
[ScriptEditorService](/docs/reference/engine/classes/ScriptEditorService.md) as its parent. Each instance adheres to the
following encoding conventions:

- All text in [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) is UTF-8 encoded.
- All line indices are 1-indexed.
- All character indices are 1-indexed and count UTF-8 bytes, not graphemes, so
  the same warning from [TextBox.CursorPosition](/docs/reference/engine/classes/TextBox.md) applies: many Unicode
  characters take more than one byte.
- All ranges are inclusive of their start position and exclusive of their end
  position, so start == end implies an empty range.

All APIs for [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) are at **Plugin** level security.

## Methods

### Method: ScriptDocument:AddReadOnlyReasonsAsync

**Signature:** `ScriptDocument:AddReadOnlyReasonsAsync(reasons: Array): ()`

Adds reasons for the Script Editor UI to be read-only, which makes the
editor read-only. Yields the current thread until the editor acknowledges
the change. Adding a reason that is already active does nothing.

Read-only state is tracked as a set of named reasons so that multiple
plugins can make an editor read-only without interfering with each other.
The editor stays read-only until every reason is removed with
[ScriptDocument:RemoveReadOnlyReasonsAsync()](/docs/reference/engine/classes/ScriptDocument.md).

Read-only mode only prevents changes from the editor UI and
[ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) edit functions. It doesn't prevent changes made by
other means, such as setting [Script.Source](/docs/reference/engine/classes/Script.md) or calling
[ScriptEditorService:UpdateSourceAsync()](/docs/reference/engine/classes/ScriptEditorService.md).

Reasons starting with `RBX` are reserved for Roblox; this function throws
an error if `reasons` contains one. This function also throws an error for
the Command bar.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `reasons` | `Array` |  | An array of non-empty strings naming the reasons to add. |

**Returns:** `()`

**ScriptDocument:AddReadOnlyReasonsAsync()**

ScriptDocument:AddReadOnlyReasonsAsync()

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")
local Workspace = game:GetService("Workspace")

local newScript = Instance.new("Script")
newScript.Parent = Workspace

local success, err = ScriptEditorService:OpenScriptDocumentAsync(newScript)
if not success then
	warn(`Failed to open script document: {err}`)
	return
end

local scriptDocument = ScriptEditorService:FindScriptDocument(newScript)
-- Use a reason name unique to your plugin so it doesn't collide with other plugins' reasons
scriptDocument:AddReadOnlyReasonsAsync({ "MyPluginReview" })
print(`{scriptDocument.Name} is read-only: {scriptDocument:IsReadOnly()}`)
```

### Method: ScriptDocument:CloseAsync

**Signature:** `ScriptDocument:CloseAsync(): Tuple`

Requests that the editor associated with this document close. Yields the
current thread until the editor responds to the request. If the function
succeeds, it returns (true, nil). If the function fails, it returns
(false, string) as a description of the problem.

This function can't close the command bar.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — A tuple where the first element is `true` if the editor closed
successfully, or `false` followed by a string describing the failure
reason.

**ScriptDocument:CloseAsync**

ScriptDocument:CloseAsync

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

local documents = ScriptEditorService:GetScriptDocuments()
local scriptDocument
-- Find the first open script document
for _, document in documents do
	-- The Command Bar can't be closed, so don't select it
	if not document:IsCommandBar() then
		scriptDocument = document
		break
	end
end

if scriptDocument then
	local success, err = scriptDocument:CloseAsync()
	if success then
		print(`Closed {scriptDocument.Name}`)
	else
		warn(`Failed to close {scriptDocument.Name} because: {err}`)
	end
else
	print("No open scripts")
end
```

### Method: ScriptDocument:EditTextAsync

**Signature:** `ScriptDocument:EditTextAsync(newText: string, startLine: int, startCharacter: int, endLine: int, endCharacter: int): Tuple`

Replaces the text in the specified range from (`startLine`, `startColumn`)
to (`endLine`, `endColumn`) with `newText`. If the range is empty, then
the function inserts the text at (`startLine`, `startColumn`). If the text
cursor is within the specified range, the cursor moves to the end position
of the edit. Otherwise, the text cursor doesn't move. This function yields
the current thread until it receives a reply from the editor about the
edit.

If the function succeeds, it returns (`true`, `nil`).

The function throws an error if:

- The range is invalid.
- The range would slice one Unicode character, for example replace only
  some of the bytes of the unicode character.
- The `newText` itself contains invalid UTF-8.

If the function fails, it returns (false, string). The string is a
description of the problem. The most common failure type is a version
mismatch. This occurs when you try to call `EditTextAsync` during the time
when the [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) is out of sync with the contents of the
editor. If this happens, you can retry the edit.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `newText` | `string` |  | The replacement string to insert into the specified range. |
| `startLine` | `int` |  | The 1-indexed line number where the replacement range begins. |
| `startCharacter` | `int` |  | The 1-indexed UTF-8 byte offset within `startLine` where the replacement range begins. |
| `endLine` | `int` |  | The 1-indexed line number where the replacement range ends (exclusive). |
| `endCharacter` | `int` |  | The 1-indexed UTF-8 byte offset within `endLine` where the replacement range ends (exclusive). |

**Returns:** `Tuple` — A tuple where the first element is `true` if the edit was applied
successfully, or `false` followed by a string describing the failure
reason.

### Method: ScriptDocument:ForceSetSelectionAsync

**Signature:** `ScriptDocument:ForceSetSelectionAsync(cursorLine: int, cursorCharacter: int, anchorLine?: int?, anchorCharacter?: int?): Tuple`

Asks the editor to set its cursor selection to the argument values. Both
anchor arguments must be passed, or neither. If neither is passed, then
they each default to being the same as the corresponding cursor argument.
The editor might decline to update its cursor if the text content of the
document has changed. Unlike
[ScriptDocument:RequestSetSelectionAsync()](/docs/reference/engine/classes/ScriptDocument.md), the editor will not
decline to move its cursor if the cursor has moved since the request was
made. Returns (true, nil) if the cursor was updated, and (false, string)
with an explanation string if it was not. Yields the current thread until
the editor replies.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cursorLine` | `int` |  | The 1-indexed line number for the cursor position. |
| `cursorCharacter` | `int` |  | The 1-indexed UTF-8 byte offset within the line for the cursor position. |
| `anchorLine` | `int?` | `nil` | The 1-indexed line number for the anchor position. Defaults to `cursorLine` if not provided. |
| `anchorCharacter` | `int?` | `nil` | The 1-indexed UTF-8 byte offset within the line for the anchor position. Defaults to `cursorCharacter` if not provided. |

**Returns:** `Tuple` — A tuple where the first element is `true` if the cursor was updated,
or `false` followed by a string explaining why the update was
declined.

**ScriptDocument:ForceSetSelectionAsync()**

ScriptDocument:ForceSetSelectionAsync()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	-- Get the text on the cursor's current line
	local cursorLine = scriptDocument:GetSelection()
	local lineText = scriptDocument:GetLine(cursorLine)
	-- Force select the entire line of text
	local success, err = scriptDocument:ForceSetSelectionAsync(cursorLine, 1, cursorLine, #lineText + 1)
	if success then
		print("Set selection!")
	else
		print(`Failed to set selection because: {err}`)
	end
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetLine

**Signature:** `ScriptDocument:GetLine(lineIndex?: int?): string`

Returns the text of the specified line. When no argument is provided,
returns the line of the current cursor position.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `lineIndex` | `int?` | `nil` | The 1-indexed line number to retrieve. Defaults to the current cursor line if not provided. |

**Returns:** `string` — The text content of the specified line as a string.

**ScriptDocument.SelectionChanged and ScriptDocument:GetLine()**

ScriptDocument.SelectionChanged and ScriptDocument:GetLine()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	scriptDocument.SelectionChanged:Connect(function(positionLine, positionCharacter, anchorLine, anchorCharacter)
		print(`Selected: Line {positionLine}, Char {positionCharacter}`)
		print(`Anchor: Line {anchorLine}, Char {anchorCharacter}`)
		local lineText = scriptDocument:GetLine(positionLine)
		print(`Selected line text: {lineText}`)
	end)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetLineCount

**Signature:** `ScriptDocument:GetLineCount(): int`

Returns the number of lines in the active document.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `int` — The total number of lines in the document.

**ScriptDocument:GetLineCount()**

ScriptDocument:GetLineCount()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	local lineCount = scriptDocument:GetLineCount()
	print(`The script has {lineCount} lines!`)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetReadOnlyReasons

**Signature:** `ScriptDocument:GetReadOnlyReasons(): List<string>`

Returns the reasons the Script Editor UI is currently read-only, sorted
alphabetically. The array includes reasons added by any plugin as well as
reasons that start with `RBX`, which Roblox reserves for its own features.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `List<string>` — A sorted array of strings. The array is empty if the editor isn't
read-only.

**ScriptDocument:GetReadOnlyReasons()**

ScriptDocument:GetReadOnlyReasons()

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")

for _, document in ScriptEditorService:GetScriptDocuments() do
	local reasons = document:GetReadOnlyReasons()
	if #reasons > 0 then
		print(`{document.Name} is read-only because of: {table.concat(reasons, ", ")}`)
	end
end
```

### Method: ScriptDocument:GetScript

**Signature:** `ScriptDocument:GetScript(): LuaSourceContainer`

Returns the underlying [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) instance, if one exists,
otherwise `nil`.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `LuaSourceContainer` — The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) that the document is editing, or `nil`
if the document does not represent a script instance in the place
(e.g. the Command Bar is not a real script instance).

**ScriptDocument:GetScript()**

ScriptDocument:GetScript()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	local openScript = scriptDocument:GetScript()
	print(`Currently open script: {openScript:GetFullName()}`)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetSelectedText

**Signature:** `ScriptDocument:GetSelectedText(): string`

Gets the text selected in the editor, or an empty string if there is no
selection.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `string` — The currently selected text as a string, or an empty string if nothing
is selected.

**ScriptDocument:HasSelectedText() and :GetSelectedText()**

ScriptDocument:HasSelectedText() and :GetSelectedText()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	scriptDocument.SelectionChanged:Connect(function()
		if scriptDocument:HasSelectedText() then
			local selectedText = scriptDocument:GetSelectedText()
			print(`Currently selected text: {selectedText}`)
		else
			print("No text currently selected")
		end
	end)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetSelection

**Signature:** `ScriptDocument:GetSelection(): Tuple`

Returns the last known selection of the Script Editor in the format:
`CursorLine, CursorChar, AnchorLine, AnchorChar`. If the Script Editor has
no selection, `CursorLine == AnchorLine` and `CursorChar == AnchorChar`.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — CursorLine, CursorChar, AnchorLine, AnchorChar.

### Method: ScriptDocument:GetSelectionEnd

**Signature:** `ScriptDocument:GetSelectionEnd(): Tuple`

Gets the larger of the cursor position and anchor. If the editor has no
selection, they are the same value.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — A tuple of (line, character) representing the larger of the cursor and
anchor positions, both 1-indexed.

**ScriptDocument:GetSelectionStart() and :GetSelectionEnd()**

ScriptDocument:GetSelectionStart() and :GetSelectionEnd()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	local startLine, startCharacter = scriptDocument:GetSelectionStart()
	local endLine, endCharacter = scriptDocument:GetSelectionEnd()
	print(`Selection start: Line {startLine}, Char {startCharacter}`)
	print(`Selection end: Line {endLine}, Char {endCharacter}`)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetSelectionStart

**Signature:** `ScriptDocument:GetSelectionStart(): Tuple`

Gets the smaller of the cursor position and anchor. If the editor has no
selection, they are the same value.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — A tuple of (line, character) representing the smaller of the cursor
and anchor positions, both 1-indexed.

**ScriptDocument:GetSelectionStart() and :GetSelectionEnd()**

ScriptDocument:GetSelectionStart() and :GetSelectionEnd()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	local startLine, startCharacter = scriptDocument:GetSelectionStart()
	local endLine, endCharacter = scriptDocument:GetSelectionEnd()
	print(`Selection start: Line {startLine}, Char {startCharacter}`)
	print(`Selection end: Line {endLine}, Char {endCharacter}`)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetText

**Signature:** `ScriptDocument:GetText(startLine?: int?, startCharacter?: int?, endLine?: int?, endCharacter?: int?): string`

Returns text from the open editor. Must be called with 0, 2 or 4
arguments:

- If called with 0 arguments, gets the entire contents of the open editor.
- If called with 2 arguments, gets the text of the document starting at
  (`startLine`, `startColumn`).
- If called with 4 arguments, gets the text of the document starting at
  (`startLine`, `startColumn`) and ending at (`endLine`, `endColumn`).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `startLine` | `int?` | `nil` | The 1-indexed line number where the text range begins. Optional; omit all arguments to get the entire document. |
| `startCharacter` | `int?` | `nil` | The 1-indexed UTF-8 byte offset within `startLine` where the text range begins. |
| `endLine` | `int?` | `nil` | The 1-indexed line number where the text range ends (exclusive). Optional; omit to read from `startLine`/`startCharacter` to the end of the document. |
| `endCharacter` | `int?` | `nil` | The 1-indexed UTF-8 byte offset within `endLine` where the text range ends (exclusive). |

**Returns:** `string` — The text content within the specified range as a string.

**ScriptDocument:GetText()**

ScriptDocument:GetText()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	local text = scriptDocument:GetText()
	print(`Script contents: {text}`)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:GetViewport

**Signature:** `ScriptDocument:GetViewport(): Tuple`

Returns the currently displayed line numbers in the editor change. The
editor displays the lines between startLine and endLine, inclusive. The
first and last line might only display partially. For example, only the
topmost pixel of the last line might be on screen. Furthermore, code
folding might hide lines between startLine and endLine.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — A tuple of (startLine, endLine) representing the 1-indexed range of
lines currently visible in the editor.

**ScriptDocument:GetViewport**

ScriptDocument:GetViewport

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	local firstLine, lastLine = scriptDocument:GetViewport()
	print(`Currently viewing lines {firstLine} to {lastLine}`)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:HasSelectedText

**Signature:** `ScriptDocument:HasSelectedText(): boolean`

Returns whether or not the editor has any text selected.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — `true` if the editor has a non-empty text selection, `false`
otherwise.

**ScriptDocument:HasSelectedText() and :GetSelectedText()**

ScriptDocument:HasSelectedText() and :GetSelectedText()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	scriptDocument.SelectionChanged:Connect(function()
		if scriptDocument:HasSelectedText() then
			local selectedText = scriptDocument:GetSelectedText()
			print(`Currently selected text: {selectedText}`)
		else
			print("No text currently selected")
		end
	end)
else
	print("No scripts open")
end
```

### Method: ScriptDocument:IsCommandBar

**Signature:** `ScriptDocument:IsCommandBar(): boolean`

Returns true if the [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) represents the Command bar. The
command bar has special rules and limitations in this API:

- Studio creates the Command bar before running plugins, so it doesn't
  always fire the opened event, although it does close and reopen as
  Studio transitions between DataModels.
- You can't edit the Command bar with `EditTextAsync` for security
  reasons.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — `true` if this document represents the Command bar, `false` otherwise.

**ScriptDocument:IsCommandBar()**

ScriptDocument:IsCommandBar()

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

local documents = ScriptEditorService:GetScriptDocuments()

for _, document in documents do
	if document:IsCommandBar() then
		print("Command bar document:", document)
	end
end
```

### Method: ScriptDocument:IsReadOnly

**Signature:** `ScriptDocument:IsReadOnly(): boolean`

Returns true if the Script Editor UI is currently read-only. This is
equivalent to checking whether [ScriptDocument:GetReadOnlyReasons()](/docs/reference/engine/classes/ScriptDocument.md)
returns a non-empty array.

A read-only editor prevents the user from changing the script through the
editor UI, and [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) edit functions such as
[ScriptDocument:EditTextAsync()](/docs/reference/engine/classes/ScriptDocument.md) fail. It doesn't prevent changes
made by other means, such as setting [Script.Source](/docs/reference/engine/classes/Script.md) or calling
[ScriptEditorService:UpdateSourceAsync()](/docs/reference/engine/classes/ScriptEditorService.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — `true` if the editor is read-only, `false` otherwise.

**ScriptDocument:IsReadOnly()**

ScriptDocument:IsReadOnly()

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")

for _, document in ScriptEditorService:GetScriptDocuments() do
	if document:IsReadOnly() then
		print(`{document.Name} is read-only`)
	else
		print(`{document.Name} is editable`)
	end
end
```

### Method: ScriptDocument:MultiEditTextAsync

**Signature:** `ScriptDocument:MultiEditTextAsync(edits: Array): Tuple`

Applies a batch of text edits to the document as a single atomic
operation, then yields the current thread until it receives a reply from
the editor. Each entry in the `edits` array is a table describing one
replacement, with the same meaning as the arguments to
[ScriptDocument:EditTextAsync()](/docs/reference/engine/classes/ScriptDocument.md), and the following fields:

- `NewText`: The replacement text.
- `StartLine`: The line of the start of the range to replace.
- `StartCharacter`: The character of the start of the range to replace.
- `EndLine`: The line of the end of the range to replace.
- `EndCharacter`: The character of the end of the range to replace.

The edits are applied together, so either all of them succeed or none of
them are applied. Before applying any edit, the function validates every
edit and throws an error if:

- Any range is invalid.
- Any range would slice one Unicode character, for example replace only
  some of the bytes of the unicode character.
- Any `NewText` itself contains invalid UTF-8.
- The ranges of two edits overlap.

If the function succeeds, it returns (`true`, `nil`). If the function
fails, it returns (`false`, `string`), where the string describes the
problem. As with [ScriptDocument:EditTextAsync()](/docs/reference/engine/classes/ScriptDocument.md), the most common
failure is a version mismatch, which occurs when the
[ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) is momentarily out of sync with the contents of the
editor; if this happens, you can retry the edits.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `edits` | `Array` |  | An array of tables, each describing a text replacement with fields `NewText`, `StartLine`, `StartCharacter`, `EndLine`, and `EndCharacter`. |

**Returns:** `Tuple` — A tuple where the first element is `true` if all edits were applied
successfully, or `false` followed by a string describing the failure
reason.

### Method: ScriptDocument:RemoveReadOnlyReasonsAsync

**Signature:** `ScriptDocument:RemoveReadOnlyReasonsAsync(reasons: Array): ()`

Removes reasons for the Script Editor UI to be read-only, previously added
with [ScriptDocument:AddReadOnlyReasonsAsync()](/docs/reference/engine/classes/ScriptDocument.md) or the
`InitialReadOnlyReasons` option of
[ScriptEditorService:OpenScriptDocumentAsync()](/docs/reference/engine/classes/ScriptEditorService.md). Yields the current
thread until the editor acknowledges the change. Removing a reason that
isn't active does nothing.

The editor stays read-only while any other reason remains active. Reasons
starting with `RBX` are reserved for Roblox; plugins can't remove them,
and this function throws an error if `reasons` contains one.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `reasons` | `Array` |  | An array of non-empty strings naming the reasons to remove. |

**Returns:** `()`

**ScriptDocument:RemoveReadOnlyReasonsAsync()**

ScriptDocument:RemoveReadOnlyReasonsAsync()

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")
local Workspace = game:GetService("Workspace")

local newScript = Instance.new("Script")
newScript.Parent = Workspace

local success, err = ScriptEditorService:OpenScriptDocumentAsync(newScript)
if not success then
	warn(`Failed to open script document: {err}`)
	return
end

local scriptDocument = ScriptEditorService:FindScriptDocument(newScript)
scriptDocument:AddReadOnlyReasonsAsync({ "MyPluginReview", "MyPluginLocked" })

-- The editor stays read-only while any other reason remains active
scriptDocument:RemoveReadOnlyReasonsAsync({ "MyPluginReview" })
print(`Read-only after removing one reason: {scriptDocument:IsReadOnly()}`)

scriptDocument:RemoveReadOnlyReasonsAsync({ "MyPluginLocked" })
print(`Read-only after removing all reasons: {scriptDocument:IsReadOnly()}`)
```

### Method: ScriptDocument:RequestSetSelectionAsync

**Signature:** `ScriptDocument:RequestSetSelectionAsync(cursorLine: int, cursorCharacter: int, anchorLine?: int?, anchorCharacter?: int?): Tuple`

Asks the editor to set its cursor selection to the argument values. Both
anchor arguments must be passed, or neither. If neither is passed, then
they each default to being the same as the corresponding cursor argument.
The editor might decline to update its cursor if the text content of the
document has changed, or the cursor has moved since the request was made.
Returns (true, nil) if the cursor was updated, and (false, string) with an
explanation string if it was not. Yields the current thread until the
editor replies.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cursorLine` | `int` |  | The 1-indexed line number for the cursor position. |
| `cursorCharacter` | `int` |  | The 1-indexed UTF-8 byte offset within the line for the cursor position. |
| `anchorLine` | `int?` | `nil` | The 1-indexed line number for the anchor position. Defaults to `cursorLine` if not provided. |
| `anchorCharacter` | `int?` | `nil` | The 1-indexed UTF-8 byte offset within the line for the anchor position. Defaults to `cursorCharacter` if not provided. |

**Returns:** `Tuple` — A tuple where the first element is `true` if the cursor was updated,
or `false` followed by a string explaining why the update was
declined.

**ScriptDocument:RequestSetSelectionAsync()**

ScriptDocument:RequestSetSelectionAsync()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	-- Get the text on the cursor's current line
	local cursorLine = scriptDocument:GetSelection()
	local lineText = scriptDocument:GetLine(cursorLine)
	-- Force select the entire line of text
	local success, err = scriptDocument:RequestSetSelectionAsync(cursorLine, 1, cursorLine, #lineText + 1)
	if success then
		print("Set selection!")
	else
		print(`Failed to set selection because: {err}`)
	end
else
	print("No scripts open")
end
```

### Method: ScriptDocument:ReviewableTextEditsAsync

**Signature:** `ScriptDocument:ReviewableTextEditsAsync(changes: Array): Tuple`

Applies a batch of line-based text edits to the document that are
presented to the user as reviewable inline diffs in the Script Editor
gutter. Each entry in the `changes` array is a table with the following
fields:

- `Text`: The replacement text to insert. Must be a non-empty string
  unless `EndLine` is provided.
- `StartLine`: The 1-indexed line number where the edit begins. If
  `EndLine` is omitted, the text is inserted before this line. If
  `EndLine` is provided, lines from `StartLine` through `EndLine` are
  replaced.
- `EndLine`: Optional. The 1-indexed last line of the range to replace
  (inclusive). Must be greater than or equal to `StartLine`.

The edits must not overlap or border each other; there must be at least
one unchanged line between any two edits. Edits are applied atomically.
The function throws an error if any entry has invalid fields. If the
function fails due to a version mismatch or other editor-side issue, it
returns (`false`, `string`).

This method cannot be used on the Command bar.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `changes` | `Array` |  | An array of tables, each with a `Text` field (the replacement string), a `StartLine` field (1-indexed line to insert or begin replacing at), and an optional `EndLine` field (1-indexed last line to replace, inclusive). |

**Returns:** `Tuple` — A tuple where the first element is `true` if the edits were applied
successfully, or `false` followed by a string describing the failure
reason.

## Events

### Event: ScriptDocument.SelectionChanged

**Signature:** `ScriptDocument.SelectionChanged(positionLine: int64, positionCharacter: int64, anchorLine: int64, anchorCharacter: int64)`

Fires when the ScriptDocument changes, including immediately after a text
change.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `positionLine` | `int64` | The 1-indexed line number of the cursor position after the change. |
| `positionCharacter` | `int64` | The 1-indexed UTF-8 byte offset of the cursor position after the change. |
| `anchorLine` | `int64` | The 1-indexed line number of the selection anchor after the change. |
| `anchorCharacter` | `int64` | The 1-indexed UTF-8 byte offset of the selection anchor after the change. |

**ScriptDocument.SelectionChanged and ScriptDocument:GetLine()**

ScriptDocument.SelectionChanged and ScriptDocument:GetLine()

```lua
--!nocheck

-- Run the following code in the Command Bar while a script is open

local ScriptEditorService = game:GetService("ScriptEditorService")

local function getFirstOpenDocument()
	local documents = ScriptEditorService:GetScriptDocuments()
	for _, document in documents do
		if not document:IsCommandBar() then
			return document
		end
	end
	return nil
end

local scriptDocument = getFirstOpenDocument()

if scriptDocument then
	scriptDocument.SelectionChanged:Connect(function(positionLine, positionCharacter, anchorLine, anchorCharacter)
		print(`Selected: Line {positionLine}, Char {positionCharacter}`)
		print(`Anchor: Line {anchorLine}, Char {anchorCharacter}`)
		local lineText = scriptDocument:GetLine(positionLine)
		print(`Selected line text: {lineText}`)
	end)
else
	print("No scripts open")
end
```

### Event: ScriptDocument.ViewportChanged

**Signature:** `ScriptDocument.ViewportChanged(startLine: int64, endLine: int64)`

Fires when the displayed line numbers in the editor change. See
[ScriptDocument.GetViewport](/docs/reference/engine/classes/ScriptDocument.md) for details.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `startLine` | `int64` | The 1-indexed first line currently visible in the editor viewport. |
| `endLine` | `int64` | The 1-indexed last line currently visible in the editor viewport. |

**Connecting to ScriptDocument.ViewportChanged**

Demonstrates using [ScriptDocument.ViewportChanged](/docs/reference/engine/classes/ScriptDocument.md) to print the start
and end line of the script's viewport when it changes.

To run:

1. Ensure Output view is open
2. Run the below code in the Command Bar
3. Scroll up and down in the opened Script window

```lua
--!nocheck

--[[
	To run:
		1. Ensure Output view is open
		2. Run the below code in the Command Bar
		3. Scroll up and down in the opened Script window

	Print statements from the ViewportChanged event will appear in the Output
]]

local Workspace = game:GetService("Workspace")
local ScriptEditorService = game:GetService("ScriptEditorService")

-- Create text that spans many lines
local dummyText = string.rep("-- Dummy Text\n", 60)

-- Create a script containing the dummy text and open it
local otherScript = Instance.new("Script")
otherScript.Source = dummyText
otherScript.Parent = Workspace
local success, err = ScriptEditorService:OpenScriptDocumentAsync(otherScript)
if not success then
	warn(`Failed to open script because: {err}`)
	return
end

-- Get a reference to the opened script
local scriptDocument = ScriptEditorService:FindScriptDocument(otherScript)

local function onViewportChanged(startLine: number, endLine: number)
	print(`Script Viewport Changed - startLine: {startLine}, endLine: {endLine}`)
end
-- Connect the ViewportChanged event to the function above that prints the start and end line of the updated viewport
scriptDocument.ViewportChanged:Connect(onViewportChanged)
```

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some