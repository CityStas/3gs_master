---
name: ScriptEditorService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "This service is used for interacting with ScriptDocument instances."
---

# Class: ScriptEditorService

> This service is used for interacting with [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) instances.

## Description

This service is used for interacting with [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) instances. It
provides methods to open, find, and list script documents that represent
scripts currently open in the Studio
[Script Editor](/docs/en-us/studio/script-editor.md). It also enables plugins to
register custom callbacks for autocomplete and script analysis, and fires
events when script documents are opened, closed, or changed.

This service is only available in Studio plugins and the command bar (Plugin
security level).

## Methods

### Method: ScriptEditorService:DeregisterAutocompleteCallback

**Signature:** `ScriptEditorService:DeregisterAutocompleteCallback(name: string): ()`

Removes a previously registered autocomplete callback with the name
`name`. The callback must have been registered with
[ScriptEditorService:RegisterAutocompleteCallback()](/docs/reference/engine/classes/ScriptEditorService.md). Throws an
error if no callback with the given name is currently registered.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The identifier that was used when registering the callback with [ScriptEditorService:RegisterAutocompleteCallback()](/docs/reference/engine/classes/ScriptEditorService.md). |

**Returns:** `()`

**DeregisterAutocompleteCallback()**

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService:DeregisterAutocompleteCallback("foo")
```

### Method: ScriptEditorService:DeregisterScriptAnalysisCallback

**Signature:** `ScriptEditorService:DeregisterScriptAnalysisCallback(name: string): ()`

Removes a previously registered Script Analysis callback with the name
`name`. The callback must have been registered with
[ScriptEditorService:RegisterScriptAnalysisCallback()](/docs/reference/engine/classes/ScriptEditorService.md). Throws an
error if no callback with the given name is currently registered.

After the callback is removed, Script Analysis automatically reruns on all
open scripts to update diagnostics.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The identifier that was used when registering the callback with [ScriptEditorService:RegisterScriptAnalysisCallback()](/docs/reference/engine/classes/ScriptEditorService.md). |

**Returns:** `()`

**DeregisterScriptAnalysisCallback()**

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService:DeregisterScriptAnalysisCallback("foo")
```

### Method: ScriptEditorService:FindScriptDocument

**Signature:** `ScriptEditorService:FindScriptDocument(script: LuaSourceContainer): ScriptDocument`

Returns the open [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) corresponding to the given
[LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md), or `nil` if the given script is not open.

A [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) only exists while the script has an open tab in
the Script Editor. If the script's editor tab is closed, this method
returns `nil` even if the script instance still exists in the DataModel.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `script` | `LuaSourceContainer` |  | The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) (such as a [Script](/docs/reference/engine/classes/Script.md), [LocalScript](/docs/reference/engine/classes/LocalScript.md), or [ModuleScript](/docs/reference/engine/classes/ModuleScript.md)) to find the open document for. |

**Returns:** `ScriptDocument` — The open [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) corresponding to the given script, or
nil if the script is not currently open in the Script Editor.

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

### Method: ScriptEditorService:GetEditorSource

**Signature:** `ScriptEditorService:GetEditorSource(script: LuaSourceContainer): string`

Returns the edit-time source for the given script.

If the script is open in the
[Script Editor](/docs/en-us/studio/script-editor.md), this method returns the
text currently being displayed in the editor. If the script is not open in
the editor, the method returns the text that the editor would display if
it's opened. The edit-time source is not always be consistent with the
[Script.Source](/docs/reference/engine/classes/Script.md) property.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `script` | `LuaSourceContainer` |  | The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) to retrieve the edit-time source text for. |

**Returns:** `string` — The edit-time source text of the script as a string.

### Method: ScriptEditorService:GetScriptDocuments

**Signature:** `ScriptEditorService:GetScriptDocuments(): List<ScriptDocument>`

Returns an array of the currently open script documents, including the
command bar. Each entry is a [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) representing one open
editor tab. The command bar's document can be identified with
[ScriptDocument:IsCommandBar()](/docs/reference/engine/classes/ScriptDocument.md) if you need to exclude it.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `List<ScriptDocument>` — An array of [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) objects representing all currently
open editor tabs, including the command bar.

**Print the name of every script**

Gets all script documents in the place with
[ScriptEditorService:GetScriptDocuments()](/docs/reference/engine/classes/ScriptEditorService.md) and prints their names.

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

local scriptDocuments = ScriptEditorService:GetScriptDocuments()
for _, scriptDocument in scriptDocuments do
	-- Prints the name of each script
	if not scriptDocument:IsCommandBar() then
		print(scriptDocument.Name)
	end
end
```

### Method: ScriptEditorService:OpenScriptDocumentAsync

**Signature:** `ScriptEditorService:OpenScriptDocumentAsync(script: LuaSourceContainer, options?: Dictionary): Tuple`

Requests that a Script Editor open the specified script. Returns (true,
nil) if the request succeeds. Returns (false, string) if the request
fails, with a string that describes the problem.

If the script is already open, this function succeeds and switches tabs to
the associated editor.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `script` | `LuaSourceContainer` |  | The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) to open in the Script Editor. |
| `options` | `Dictionary` | `nil` | A dictionary that supports the following options:  - `Temporary` &mdash; Boolean. Whether to open the script in a preview   tab. Default is false. - `HighlightRange` &mdash; A nested dictionary containing a line and   character range to highlight in the editor. Example:   `HighlightRange = { Start = { Line = 10, Character = 1 }, End = { Line = 15, Character = 20 }}`.   Lines and characters are 1-based. Out-of-range positions are clamped   to the nearest valid position: a `Line` or `Character` below 1   becomes 1, a `Character` past the end of its line becomes the end of   that line, and a `Line` past the last line becomes the end of the   script. `Start` and `End` are clamped independently; if `End` is   before `Start` after clamping, they are swapped, so the same text is   highlighted with the cursor at the later position. - `InitialReadOnlyReasons` &mdash; An array of strings. Reasons to add   with [ScriptDocument:AddReadOnlyReasonsAsync()](/docs/reference/engine/classes/ScriptDocument.md) once the   editor opens, so the script is read-only as soon as the call   returns. Example:   `InitialReadOnlyReasons = { "MyPluginTemplateScript" }`. |

**Returns:** `Tuple` — A tuple where the first value is a boolean indicating success and the
second is nil on success or a string describing the problem on
failure.

**OpenScriptDocumentAsync()**

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")
local Workspace = game:GetService("Workspace")

local newScript = Instance.new("Script")
newScript.Parent = Workspace

local success, err = ScriptEditorService:OpenScriptDocumentAsync(newScript)
if success then
	print("Opened script document")
else
	print(`Failed to open script document: {err}`)
end
```

**OpenScriptDocumentAsync() with InitialReadOnlyReasons**

Opens a script that is read-only as soon as the call returns.

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")
local Workspace = game:GetService("Workspace")

local templateScript = Instance.new("Script")
templateScript.Source = "-- Template provided by MyPlugin"
templateScript.Parent = Workspace

local success, err = ScriptEditorService:OpenScriptDocumentAsync(templateScript, {
	InitialReadOnlyReasons = { "MyPluginTemplateScript" },
})
if success then
	local scriptDocument = ScriptEditorService:FindScriptDocument(templateScript)
	print(`Opened read-only template: {scriptDocument:IsReadOnly()}`)
else
	warn(`Failed to open script document: {err}`)
end
```

### Method: ScriptEditorService:RegisterAutocompleteCallback

**Signature:** `ScriptEditorService:RegisterAutocompleteCallback(name: string, priority: int, callbackFunction: Function): ()`

Registers an autocomplete callback `callbackFunction` named `name` with
priority `priority`.

When the Script Editor invokes autocomplete, all registered autocomplete
callbacks call in order of ascending priority with the autocomplete
request and response. Multiple callbacks may share a priority, but then
their calling order is unpredictable. Each callback is intended to return
a response table with the same format as the response input table.
Callbacks shouldn't yield. The first callback invoked receives the
internal autocomplete's response as its response table, and subsequent
callbacks receive the previous callback's output as their response table.
Callbacks may either modify the passed table or return a new table of the
same format.

The `callbackFunction` must have the following type:
`(Request: table, Response: table) -> table`

The Request table has the following format:

```lua
type Request = {
  position: {
    line: number,
    character: number
  },
  textDocument: {
    document: ScriptDocument?,
    script: LuaSourceContainer?
  }
}
```

- `position` is the one-indexed cursor position where you are
  autocompleting.
- `textDocument.document` is the open [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) you are
  completing in, if it exists.
- `textDocument.script` is the [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) you are
  completing in, if it exists.

If both `textDocument.document` and `textDocument.script` are present,
then they correspond to each other:
`req.textDocument.document:GetScript() == req.textDocument.script`

The Response table has the following format:

```
type Response = {
  items: {
    {
      label: string, -- The label
      kind: Enum.CompletionItemKind?,
      tags: {Enum.CompletionItemTag}?,
      detail: string?,
      documentation: {
        value: string,
      }?,
      overloads: number?,
      learnMoreLink: string?,
      codeSample: string?,
      preselect: boolean?,
      textEdit: {
        newText: string,
        insert: { start: { line: number, character: number }, ["end"]: { line: number, character: number } },
        replace: { start: { line: number, character: number }, ["end"]: { line: number, character: number } },
      }?
    }
  }
}
```

- `Response.items` is an array of the completion items. The order of this
  array is insignificant, and it resorts in the editor as the user types.
- `Response.items[n].label` is the label of the item which display in the
  autocomplete menu.
- `Response.items[n].kind` specifies what type of autocomplete item this
  is. Primarily this controls the icon given to the item in the editor.
  Not all kinds have a unique icon. If not specified, the editor uses the
  "Text" icon. Unsupported kinds default to displaying the "Property"
  icon.
- `Response.items[n].tags` specifies an array of tags describing this
  completion item. See the [CompletionItemTag](/docs/reference/engine/enums/CompletionItemTag.md) for details on their
  function.
- `Response.items[n].details` specifies a string describing details about
  the completion item. For default items, this is a string representation
  of their type. Note that, in order for the documentation widget to
  display, `documentation` must be present, but `documentation.value` may
  be empty.
- `Response.items[n].documentation` specifies the main body of the
  documentation in its `value` field. `documentation` is present, even if
  value is empty, so the documentation window displays if either details
  or overloads are specified.
- `Response.items[n].overloads` specifies the number of overloads of a
  function autocompletion.
- `Response.items[n].learnMoreLink` links to a relevant page on the
  creator docs. This URL must be a `https` request to create.roblox.com;
  no other URLs display in the editor.
- `Response.items[n].codeSample` specifies a sample use of the completion
  item. `documentation` must be non-empty to display this field.
- `Response.items[n].preselect` If true, the editor sorts this completion
  item ahead of all others and selects it for the user by default. No
  effect if false or missing.
- `Response.items[n].textEdit` If present, accepting the completion
  applies this text edit - inserting or replacing the span between the
  positions start and end with newText.

If a callback returns a malformed result or encounters an error, the
editor discards the modified Response table and uses the built-in
autocomplete result list.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | A unique identifier for this callback, used to deregister it later with [ScriptEditorService:DeregisterAutocompleteCallback()](/docs/reference/engine/classes/ScriptEditorService.md). |
| `priority` | `int` |  | The invocation order among registered callbacks; lower values run first. |
| `callbackFunction` | `Function` |  | The function invoked during autocomplete with the signature `(Request: table, Response: table) -> table`. |

**Returns:** `()`

**RegisterAutocompleteCallback() and DeregisterAutocompleteCallback()**

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

type Request = {
	position: {
		line: number,
		character: number,
	},
	textDocument: {
		document: ScriptDocument?,
		script: LuaSourceContainer?,
	},
}

type Response = {
	items: {
		{
			label: string,
			kind: Enum.CompletionItemKind?,
			tags: { Enum.CompletionItemTag }?,
			detail: string?,
			documentation: {
				value: string,
			}?,
			overloads: number?,
			learnMoreLink: string?,
			codeSample: string?,
			preselect: boolean?,
			textEdit: {
				newText: string,
				replace: {
					start: { line: number, character: number },
					["end"]: { line: number, character: number },
				},
			}?,
		}
	},
}

local autocompleteCallback = function(request: Request, response: Response): Response
	local item = {
		label = "foo",
		preselect = true,
	}
	table.insert(response.items, item)
	return response
end

ScriptEditorService:RegisterAutocompleteCallback("foo", 1, autocompleteCallback)

-- To deregister the callback, run the following code in the Command Bar

ScriptEditorService:DeregisterAutocompleteCallback("foo")
```

### Method: ScriptEditorService:RegisterScriptAnalysisCallback

**Signature:** `ScriptEditorService:RegisterScriptAnalysisCallback(name: string, priority: int, callbackFunction: Function): ()`

Registers a Script Analysis callback `callbackFunction` named `name` with
`priority`. When Script Analysis in Studio runs, all registered callbacks
call in order of ascending priority. Each callback is intended to return a
response table matching the format specified below. Callbacks should not
yield.

The request table has the following format, where `script` is the
`LuaSourceContainer` that is going to be analyzed.

```
type Request = {
  script: LuaSourceContainer?
}
```

The response table has the following format, where `diagnostics` is an
array of diagnostic tables. Each diagnostic table has the entries listed
below.

```
type Response = {
  diagnostics: {
    {
      range: {
        start: {
          line: number,
          character: number,
        },
        ["end"]: {
          line: number,
          character: number,
        }
      },
      code: string?,
      message: string,
      severity: Enum.Severity?,
      codeDescription: { href: string }?
    }
  }
}
```

- `range` represents a text range that should be highlighted by the
  linter, providing what line/character to start highlighting and what
  line/character to stop highlighting.
- `code` is a label for the message.
- `message` is a warning message to be displayed for the line. This will
  also appear on a tooltip when the user hovers their cursor over the line
  in the Script Editor.
- `severity` is a [Severity](/docs/reference/engine/enums/Severity.md) value for the diagnostics. This
  determines how the diagnostic is categorized in the Script Analysis tool
  in Studio, as well as how text is highlighted in the Script Editor.
- `codeDescription` links to a relevant page on the creator docs. This URL
  must be an `https` request to `create.roblox.com`; no other URLs display
  in the editor.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | A unique identifier for this callback, used to deregister it later with [ScriptEditorService:DeregisterScriptAnalysisCallback()](/docs/reference/engine/classes/ScriptEditorService.md). |
| `priority` | `int` |  | The invocation order among registered callbacks; lower values run first. |
| `callbackFunction` | `Function` |  | The function invoked during Script Analysis with the signature `(Request: table) -> table`, returning a response containing diagnostics. |

**Returns:** `()`

**RegisterScriptAnalysisCallback()**

```lua
type Request = {
	["script"]: LuaSourceContainer,
}

type Response = {
	diagnostics: {
		{
			range: {
				start: {
					line: number,
					character: number,
				},
				["end"]: {
					line: number,
					character: number,
				},
			},
			code: string?,
			message: string,
			severity: Enum.Severity?,
			codeDescription: { href: string }?,
		}
	},
}

local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService:RegisterScriptAnalysisCallback("foo", 1, function(Req: Request): Response
	local response = {
		diagnostics = {},
	}
	local lineNo = 1

	-- Iterate line by line
	for text, newline in Req.script.Source:gmatch("([^\r\n]*)([\r\n]*)") do
		local startIndex, endIndex = string.find(text, "Foo")
		if startIndex and endIndex then
			table.insert(response.diagnostics, {
				range = {
					["start"] = {
						line = lineNo,
						character = startIndex,
					},
					["end"] = {
						line = lineNo,
						character = endIndex,
					},
				},
				code = "FooFinder",
				message = "Foo found here!",
				severity = Enum.Severity.Warning,
			})
		end
		lineNo = lineNo + #newline:gsub("\n+", "\0%0\0"):gsub(".%z.", "."):gsub("%z", "")
	end
	return response
end)
```

### Method: ScriptEditorService:UpdateSourceAsync

**Signature:** `ScriptEditorService:UpdateSourceAsync(script: LuaSourceContainer, callback: Function): ()`

Returns the edit-time [Script.Source](/docs/reference/engine/classes/Script.md) for the given script.

This function calls the passed callback using the old contents of the
script to calculate the new contents of the script.

If the script is open in the
[Script Editor](/docs/en-us/studio/script-editor.md), then it issues a
request to the editor to update its source. The editor may reject this
update if the [Script.Source](/docs/reference/engine/classes/Script.md) property was out of date with the
user's version of the script when this function was called, in which case
the callback will be re-invoked and the attempt will be repeated.

The callback may not yield. If the callback returns `nil`, the operation
is cancelled. This function yields until the operation is cancelled or
succeeds.

If the script is not open in the editor, the new content updates to the
script source, which is the text the editor would display if it is opened.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `script` | `LuaSourceContainer` |  | Script instance to be updated. |
| `callback` | `Function` |  | The function to return new script content. |

**Returns:** `()`

**Update Source Async**

Demonstrates [ScriptEditorService:UpdateSourceAsync()](/docs/reference/engine/classes/ScriptEditorService.md).

```lua
local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService:UpdateSourceAsync(workspace.Script, function(oldContent)
	return oldContent .. " World!"
end)
```

## Events

### Event: ScriptEditorService.TextDocumentDidChange

**Signature:** `ScriptEditorService.TextDocumentDidChange(document: ScriptDocument, changesArray: Variant)`

Fires just after a [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) changes. The `textChanged` is an
array of change structures of the format:

`{ range : { start : { line : number, character : number }, end : { line : number, character : number } }, text: string }`

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `document` | `ScriptDocument` | The [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) that changed. |
| `changesArray` | `Variant` | An array of change structures, each describing a range that was replaced and the new text. |

**ScriptEditorService.TextDocumentDidChange**

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService.TextDocumentDidChange:Connect(function(scriptDocument, changes)
	print("Changed", scriptDocument, changes)
end)
```

### Event: ScriptEditorService.TextDocumentDidClose

**Signature:** `ScriptEditorService.TextDocumentDidClose(oldDocument: ScriptDocument)`

Fires just before a [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) object is destroyed, which
happens right after the script editor closes. After this event fires, the
[ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) enters a "Closed" state, and trying to call its
methods throws an error. [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) objects aren't reusable,
even if the script editor reopens the same script.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `oldDocument` | `ScriptDocument` | The [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) that is about to be destroyed. |

**ScriptEditorService.TextDocumentDidClose**

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService.TextDocumentDidClose:Connect(function(scriptDocument)
	print("Closed", scriptDocument)
end)
```

### Event: ScriptEditorService.TextDocumentDidOpen

**Signature:** `ScriptEditorService.TextDocumentDidOpen(newDocument: ScriptDocument)`

Fires just after a [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) object is created and parented
to the service, which happens right after the script editor opens. The
[ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) passed to the handler is fully initialized and
ready to read or modify. This event also fires for the command bar
document.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `newDocument` | `ScriptDocument` | The newly created [ScriptDocument](/docs/reference/engine/classes/ScriptDocument.md) representing the opened editor tab. |

**ScriptEditorService.TextDocumentDidOpen**

```lua
--!nocheck

-- Run the following code in the Command Bar

local ScriptEditorService = game:GetService("ScriptEditorService")

ScriptEditorService.TextDocumentDidOpen:Connect(function(scriptDocument)
	print("Opened", scriptDocument)
end)
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