---
name: LocalizationTable
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A LocalizationTable is a database of translations. It contains source strings and translations for various languages."
---

# Class: LocalizationTable

> A LocalizationTable is a database of translations. It contains source strings
> and translations for various languages.

## Description

A LocalizationTable is a database of translations. It contains source strings
and translations for various languages. It is used with the [Translator](/docs/reference/engine/classes/Translator.md)
and [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) auto-translator system to control text
translations in the game. LocalizationTables are designed to be treated as
resources, like a texture or a script. They are not optimized to be modified
at runtime. Changing the contents of a table will cause the entire contents of
the table to be replicated to all players.

## LocalizationTable Entries

Each LocalizationTable contains a set of entries. Each entry contains the
translations of the text, along with some special fields:

- **Key** is an optional unique key for fast hash lookups in code. If it is
  non-empty it must be unique in the table.
- **Source** is the original text in the source language that will be used by
  the [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) automatic text replacement system to match
  GUI text and render a translation instead. The Source field can be filled by
  the text capture tools, or can be set manually. For key-based lookups the
  Source value can be used as a translation for
  [LocalizationTable.SourceLocaleId](/docs/reference/engine/classes/LocalizationTable.md) if the entry doesn't have a
  translation for that locale. If Source is empty then the entry will not be
  used by the automatic replacement system.
- **Context** is the full Instance name for the object that the text appeared
  on. Context is used for disambiguation by the automatic text replacement
  system. When multiple matches for the Source are found, the system will pick
  the best match by matching backwards from the end of the Context string.
  There are other more robust ways to handle disambiguation available as well,
  like using multiple tables with [GuiBase2d.RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md).
- **Example** is whatever you want it to be. If the text capture tool guessed
  some parameters for a string the Example field will contain an example of
  them used in context.

All of these fields are optional, but at least either Key or Source must be
non-empty. No two entries can have the same Key, Source, and Context.

See
[Translating Dynamic Content](/docs/en-us/production/localization/translate-dynamic-content.md)
for more information.

## Code Samples

**LocalizationTable**

```lua
local LocalizationService = game:GetService("LocalizationService")

local function createLocalizationTable(entries): LocalizationTable
	local localTable = Instance.new("LocalizationTable")
	localTable.SourceLocaleId = LocalizationService.SystemLocaleId
	localTable:SetEntries(entries)
	return localTable
end

local entries = {
	{
		Key = "Hello_World", -- The 'expressionKey' to be used with GetString
		Values = { -- A dictionary of keys corresponding to IETF language tags, and their translations.
			["ru"] = " !", -- Russian
			["fr"] = "Bonjour le monde!", -- French
			["de"] = "Hallo Welt!", -- German
			["en-US"] = "Hello world!", -- English
			["it"] = "Ciao mondo!", -- Italian
			["pt-BR"] = "Ol Mundo!", -- Portuguese
			["ja"] = "", -- Japanese
			["es"] = "Hola Mundo!", -- Spanish
		},
	},
}

local helloWorldTable = createLocalizationTable(entries)
local translatorEnglish = helloWorldTable:GetTranslator("en-US")

print(translatorEnglish:FormatByKey("Hello_World"))
```

## Properties

### Property: LocalizationTable.SourceLocaleId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Localization",
  "capabilities": [
    "Basic"
  ]
}
```

The Roblox locale of the input key strings for this table, for example
"en-us" or "es-es." This is typically the "development language" of the
game. For a Translator that merges multiple LocalizationTable objects,
it's the LocaleId of the Default LocalizationTable. Defaults to "en-us".

### Property: LocalizationTable.DevelopmentLanguage *(hidden)*

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Localization",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This item has been superseded by [LocalizationTable.SourceLocaleId](/docs/reference/engine/classes/LocalizationTable.md) which should be used in all new work.

The default IETF tag to use if the ''languageKey'' parameter is excluded
from the [LocalizationTable:GetString()](/docs/reference/engine/classes/LocalizationTable.md) method.

### Property: LocalizationTable.Root *(hidden)*

```json
{
  "type": "Instance",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This item is deprecated. Do not use it for new work.

The object that is being targeted for localization by this table.
Localization is applied to it and all of it's descendants.

## Methods

### Method: LocalizationTable:GetEntries

**Signature:** `LocalizationTable:GetEntries(): Array`

The GetEntries function returns an array of dictionaries contained in a
given [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md), where each dictionary represents an entry
of localization data.

To set the entries of a LocalizationTable, you can use
[LocalizationTable:SetEntries()](/docs/reference/engine/classes/LocalizationTable.md).

Each dictionary in the array contains the following fields:

| Index | Type | Description |
| --- | --- | --- |
| **Key** | [string](/docs/reference/engine/globals/string.md) | A lookup key for this specific entry in the LocalizationTable. |
| **Source** | [string](/docs/reference/engine/globals/string.md) | The string used to format the localized string. Used as a lookup if a key is not provided. |
| **Context** | [string](/docs/reference/engine/globals/string.md) | An [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path to the object that was used to generate the LocalizationTable. Used as a lookup if a key is not provided. |
| **Example** | [string](/docs/reference/engine/globals/string.md) | The string used to format the localization. Optional. |
| **Values** | `Dictionary` | A dictionary of language translations for this localization entry. The keys of this dictionary are locale ids, and the values are strings that are used to apply localization for the language corresponding to the locale id. |

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Array` — An array of dictionaries, where each dictionary represents an entry of
localization data.

**Using a LocalizationTable**

The following code sample creates a `LocalizationTable`, sets its entries,
then gets and displays its entries. In order for this example to work, a
LocalizationTable instance must be located inside the `LocalizationService`
service.

The _entries_ variable is a table of dictionaries, each with the format
required to create a LocalizationTable with
[LocalizationTable:SetEntries()](/docs/reference/engine/classes/LocalizationTable.md).

The _get_results_ variable is a table of dictionaries - the same table that we
created with the _entries_ variable. We then loop through each of the tables
in this dictionary to display its _Values_/strings.

```lua
local LocalizationService = game:GetService("LocalizationService")

local localizationTable = LocalizationService:FindFirstChild("LocalizationTable")

local entries = {
	{
		["Key"] = "0001",
		["Source"] = "en-us",
		["Values"] = {
			["0001"] = "Hello Muddah, hello Fadduh.",
			["0002"] = "Here I am at Camp Granada.",
			["0003"] = "Camp is very entertaining.",
			["0004"] = "And they say we'll have some fun if it stops raining.",
		},
	},
}

localizationTable:SetEntries(entries)
local get_results = localizationTable:GetEntries()

for _index, dict in pairs(get_results) do
	for _key, value in pairs(dict["Values"]) do -- Loop through every key, value pair in the dictionary to print our strings
		print(value)
	end
end
```

**Expected output:** ```
And they say we'll have some fun if it stops raining.
Hello Muddah, hello Fadduh.
Here I am at Camp Granada.
Camp is very entertaining.
```

### Method: LocalizationTable:GetTranslator

**Signature:** `LocalizationTable:GetTranslator(localeId: string): Instance`

Returns a [Translator](/docs/reference/engine/classes/Translator.md) for entries in this LocalizationTable, in the
specified language. The translator will first search in this table and
then look in ancestor tables.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `localeId` | `string` |  | A Roblox locale identifier (for example, "en-us" or "es-es") specifying the language the returned Translator should target. |

**Returns:** `Instance` — The [Translator](/docs/reference/engine/classes/Translator.md) instance for the specified locale.

### Method: LocalizationTable:RemoveEntry

**Signature:** `LocalizationTable:RemoveEntry(key: string, source: string, context: string): ()`

Removes an entry from the LocalizationTable, using the specified `key`,
`source`, and `context` to narrow down the specific entry to be removed.

The entry is identified by the (`key`, `source`, `context`) triple. If
`key` is non-empty it alone identifies the entry because keys are unique
within the table. If `key` is empty the entry is matched by the (`source`,
`context`) pair. When no matching entry exists the call is a silent no-op.

Removing an entry deletes all of its translations and metadata. To remove
only a single locale's translation from an entry while keeping the entry
itself, use [LocalizationTable:RemoveEntryValue()](/docs/reference/engine/classes/LocalizationTable.md) instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry to remove. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path used for disambiguation. Used with source to identify the entry when key is empty. |

**Returns:** `()`

### Method: LocalizationTable:RemoveEntryValue

**Signature:** `LocalizationTable:RemoveEntryValue(key: string, source: string, context: string, localeId: string): ()`

Removes a single language translation from the LocalizationTable, using
the provided `key`, `source`, `context`, and `localeId` to narrow down the
specific entry to be modified.

The entry is identified by the (`key`, `source`, `context`) triple (see
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) for lookup rules). Once the entry
is found, only the translation for `localeId` is erased; the entry itself
and all other locale translations remain intact. The `localeId` is
case-insensitive (it is canonicalized internally). If no matching entry
exists, or the entry has no translation for `localeId`, the call is a
silent no-op.

To remove the entire entry including all translations, use
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md). To remove every translation of a
given locale across all entries, use
[LocalizationTable:RemoveTargetLocale()](/docs/reference/engine/classes/LocalizationTable.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path used for disambiguation. Used with source to identify the entry when key is empty. |
| `localeId` | `string` |  | The locale identifier (for example, "fr-fr") whose translation should be removed from the entry. |

**Returns:** `()`

### Method: LocalizationTable:RemoveTargetLocale

**Signature:** `LocalizationTable:RemoveTargetLocale(localeId: string): ()`

Removes all translations from the LocalizationTable with the specified
`localeId`.

This is a bulk operation that iterates every entry in the table and erases
the translation for `localeId` from each one. Entries themselves are not
removed even if they have no remaining translations after this call. To
remove a single translation from one specific entry, use
[LocalizationTable:RemoveEntryValue()](/docs/reference/engine/classes/LocalizationTable.md) instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `localeId` | `string` |  | A Roblox locale identifier (for example, "fr-fr") specifying which language's translations to remove from all entries. |

**Returns:** `()`

### Method: LocalizationTable:SetEntries

**Signature:** `LocalizationTable:SetEntries(entries: Variant): ()`

Sets the contents of the LocalizationTable.

The entries parameter should be an array of dictionaries in the same
format as the one returned from the [LocalizationTable:GetEntries()](/docs/reference/engine/classes/LocalizationTable.md)
function.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `entries` | `Variant` |  | An array of dictionaries in the same format returned by [LocalizationTable:GetEntries()](/docs/reference/engine/classes/LocalizationTable.md), each containing Key, Source, Context, Example, and Values fields. |

**Returns:** `()`

### Method: LocalizationTable:SetEntryContext

**Signature:** `LocalizationTable:SetEntryContext(key: string, source: string, context: string, newContext: string): ()`

Sets the **Context** field of a LocalizationTable entry to `newContext`,
using the specified `key`, `source`, and `context` to narrow down the
entry that will have this change applied.

The entry is identified by the (`key`, `source`, `context`) triple (see
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) for lookup rules). If no matching
entry exists, a new entry is created with the provided `key`, `source`,
and `newContext`. The method throws an error if setting the new context
would cause the entry to conflict with another existing entry that shares
the same key, source, and context combination.

The **Context** field stores an [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path that
the automatic text replacement system uses for disambiguation when
multiple entries share the same **Source** string.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The current [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path of the entry. Used with source to identify the entry when key is empty. |
| `newContext` | `string` |  | The new context string to assign to the entry. |

**Returns:** `()`

### Method: LocalizationTable:SetEntryExample

**Signature:** `LocalizationTable:SetEntryExample(key: string, source: string, context: string, example: string): ()`

Sets the **Example** field of a LocalizationTable entry to `example`,
using the specified `key`, `source`, and `context` to narrow down the
entry that will have this change applied.

The entry is identified by the (`key`, `source`, `context`) triple (see
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) for lookup rules). If no matching
entry exists, a new entry is created with the provided `key`, `source`,
and `context`. The new `example` value always overwrites any existing
example text on the entry.

The **Example** field is an arbitrary metadata string. The text-capture
tools use it to store a sample of parameterized content in context, but
developers may store any helpful annotation.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path of the entry. Used with source to identify the entry when key is empty. |
| `example` | `string` |  | The new example text to assign to the entry, typically a sample of parameterized content in context. |

**Returns:** `()`

### Method: LocalizationTable:SetEntryKey

**Signature:** `LocalizationTable:SetEntryKey(key: string, source: string, context: string, newKey: string): ()`

Sets the **Key** field of a LocalizationTable entry to `newKey`, using the
specified `key`, `source`, and `context` to narrow down the entry that
will have this change applied.

The entry is identified by the (`key`, `source`, `context`) triple (see
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) for lookup rules). If no matching
entry exists, a new entry is created with `newKey`, the provided `source`,
and `context`. The method throws an error if `newKey` would conflict with
an existing entry's key, because keys must be unique within the table. If
`newKey` equals the entry's current key the call is a no-op.

The **Key** field is an optional unique identifier for fast hash lookups
via [Translator:FormatByKey()](/docs/reference/engine/classes/Translator.md). When non-empty it must be unique
across the entire table.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The current unique key of the entry. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path of the entry. Used with source to identify the entry when key is empty. |
| `newKey` | `string` |  | The new key string to assign to the entry. Must be unique within the table if non-empty. |

**Returns:** `()`

### Method: LocalizationTable:SetEntrySource

**Signature:** `LocalizationTable:SetEntrySource(key: string, source: string, context: string, newSource: string): ()`

Sets the **Source** field of a LocalizationTable entry to `newSource`,
using the specified `key`, `source`, and `context` to narrow down the
entry that will have this change applied.

The entry is identified by the (`key`, `source`, `context`) triple (see
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) for lookup rules). If no matching
entry exists, a new entry is created with the provided `key`, `newSource`,
and `context`. The method throws an error if the resulting (`key`,
`newSource`, `context`) combination would conflict with an existing entry.
If `newSource` equals the entry's current source the call is a no-op.

The **Source** field is the original text in the source language used by
the [LocalizationService](/docs/reference/engine/classes/LocalizationService.md) automatic text replacement system to match
GUI text at runtime. Changing the source also recomputes the internal
expression matcher, so parameterized format strings (e.g. `{1:translate}`)
are re-parsed immediately.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The current source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path of the entry. Used with source to identify the entry when key is empty. |
| `newSource` | `string` |  | The new source text to assign to the entry. Used by the automatic text replacement system for matching GUI text at runtime. |

**Returns:** `()`

### Method: LocalizationTable:SetEntryValue

**Signature:** `LocalizationTable:SetEntryValue(key: string, source: string, context: string, localeId: string, text: string): ()`

Sets the text of the specified `localeId` in a LocalizationTable entry,
using the specified `key`, `source`, and `context` to narrow down the
entry that will have this change applied.

The entry is identified by the (`key`, `source`, `context`) triple (see
[LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) for lookup rules). If no matching
entry exists, a new entry is created with the provided `key`, `source`,
and `context` — this throws an error if both `key` and `source` are empty.
The `localeId` is case-insensitive (it is canonicalized internally).

If `text` is non-empty the translation is stored (or replaced) for
`localeId` on that entry. The text must be a valid format string
(parameters like `{1:translate}` must be well-formed or the call throws).
If `text` is an empty string the translation for `localeId` is removed
from the entry, equivalent to calling
[LocalizationTable:RemoveEntryValue()](/docs/reference/engine/classes/LocalizationTable.md).

To set multiple entries at once, use
[LocalizationTable:SetEntries()](/docs/reference/engine/classes/LocalizationTable.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry. If non-empty, identifies the entry by itself. |
| `source` | `string` |  | The source text of the entry. Used with context to identify the entry when key is empty. |
| `context` | `string` |  | The [Instance:GetFullName()](/docs/reference/engine/classes/Instance.md) path of the entry. Used with source to identify the entry when key is empty. |
| `localeId` | `string` |  | The Roblox locale identifier (for example, "fr-fr") for the translation to set or remove. |
| `text` | `string` |  | The translation text to store. If empty, the translation for the specified locale is removed from the entry. |

**Returns:** `()`

### Method: LocalizationTable:GetContents

**Signature:** `LocalizationTable:GetContents(): string`

> **Deprecated:** This item has been superseded by [LocalizationTable:GetEntries()](/docs/reference/engine/classes/LocalizationTable.md) which should be used in all new work.

Deprecated. Prefer [LocalizationTable:GetEntries()](/docs/reference/engine/classes/LocalizationTable.md), which returns
the same data as a structured array of dictionaries. Returns all entries
in the [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) encoded as a JSON-formatted string, the
legacy serialized representation of the table's contents. Each entry is an
object containing its `key`, `context`, `examples`, and `source` fields
(each omitted when empty) along with a `values` map of locale IDs to
translated strings.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `string` — The table's entries encoded as a JSON-formatted string.

### Method: LocalizationTable:GetString

**Signature:** `LocalizationTable:GetString(targetLocaleId: string, key: string): string`

> **Deprecated:** This item has been superseded by [LocalizationTable:GetTranslator()](/docs/reference/engine/classes/LocalizationTable.md) which should be used in all new work.

The GetString function returns a translation based on the specified
language and key.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `targetLocaleId` | `string` |  | Specified language. |
| `key` | `string` |  | An optional unique key for fast hash lookups in code. If it is non-empty it must be unique in the table. |

**Returns:** `string` — Translated string.

### Method: LocalizationTable:RemoveKey

**Signature:** `LocalizationTable:RemoveKey(key: string): ()`

> **Deprecated:** This item has been superseded by [LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md) which should be used in all new work

Deprecated in favor of [LocalizationTable:RemoveEntry()](/docs/reference/engine/classes/LocalizationTable.md). Calling
RemoveKey is the same as making the following call to RemoveEntry:

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key of the entry to remove. |

**Returns:** `()`

**Remove Key**

Demonstrates [LocalizationTable:RemoveKey()](/docs/reference/engine/classes/LocalizationTable.md).

```lua
local localizationTable = Instance.new("LocalizationTable")
local key = "Hello"
localizationTable:SetEntryValue(key, "", "", "en", "Hello")

localizationTable:RemoveEntry(key, "", "")
```

### Method: LocalizationTable:SetContents

**Signature:** `LocalizationTable:SetContents(contents: string): ()`

> **Deprecated:** This item has been superseded by [LocalizationTable:SetEntries()](/docs/reference/engine/classes/LocalizationTable.md) which should be used in all new work

The SetContents function sets the contents of the LocalizationTable, via
the legacy JSON format.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contents` | `string` |  | A JSON-formatted string encoding the table's entries, in the same format returned by [LocalizationTable:GetContents()](/docs/reference/engine/classes/LocalizationTable.md). |

**Returns:** `()`

### Method: LocalizationTable:SetEntry

**Signature:** `LocalizationTable:SetEntry(key: string, targetLocaleId: string, text: string): ()`

> **Deprecated:** This item has been superseded by [LocalizationTable:SetEntries()](/docs/reference/engine/classes/LocalizationTable.md) which should be used in all new work.

Deprecated. Prefer [LocalizationTable:SetEntryValue()](/docs/reference/engine/classes/LocalizationTable.md) for matching
an entry by key, source, and context, or
[LocalizationTable:SetEntries()](/docs/reference/engine/classes/LocalizationTable.md) to set many entries at once. Sets
the translation `text` for the locale `targetLocaleId` on the
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) entry identified by `key`, creating a new entry
with an empty source and context if no entry with that key exists. When
`targetLocaleId` matches the table's
[LocalizationTable.SourceLocaleId](/docs/reference/engine/classes/LocalizationTable.md), the entry's **Source** field is
also set to `text`.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The unique key identifying the entry. If no entry with this key exists, a new entry is created. |
| `targetLocaleId` | `string` |  | The Roblox locale identifier (for example, "en-us" or "fr-fr") for the translation to set. |
| `text` | `string` |  | The translation text to store for the specified locale. |

**Returns:** `()`

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