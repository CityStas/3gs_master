---
name: CompletionItemKind
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the category of a script editor autocomplete suggestion, controlling its icon and display in the completion list."
---

# CompletionItemKind

Indicates the category of a script editor autocomplete suggestion, controlling
its icon and display in the completion list.

**Type:** enum

## Description

Describes the semantic category of an item returned by the Luau Language
Server Protocol (LSP) autocomplete provider. Roblox Studio's script editor
uses this value to select the icon shown next to each completion item and to
apply autocomplete scoring and filtering logic.

This enum mirrors the
[LSP CompletionItemKind specification](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#completionItemKind)
(values 1–25). Plugins that register an autocomplete callback via
[ScriptEditorService:RegisterAutocompleteCallback()](/docs/reference/engine/classes/ScriptEditorService.md) may set the `kind`
field on each `CompletionItem` to one of these values to hint how their
suggestion should be presented.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Text` | 1 | Indicates the completion item represents a plain text suggestion. |
| `Method` | 2 | Indicates the completion item represents a method on a class or object. |
| `Function` | 3 | Indicates the completion item represents a function. |
| `Constructor` | 4 | Indicates the completion item represents a constructor. |
| `Field` | 5 | Indicates the completion item represents a field within a record or struct. |
| `Variable` | 6 | Indicates the completion item represents a variable binding. |
| `Class` | 7 | Indicates the completion item represents a class or type definition. |
| `Interface` | 8 | Indicates the completion item represents an interface type. |
| `Module` | 9 | Indicates the completion item represents a module. |
| `Property` | 10 | Indicates the completion item represents a property on a class or object. |
| `Unit` | 11 | Indicates the completion item represents a unit of measurement or a module-level value. |
| `Value` | 12 | Indicates the completion item represents a value expression. |
| `Enum` | 13 | Indicates the completion item represents an enum type. |
| `Keyword` | 14 | Indicates the completion item represents a language keyword. |
| `Snippet` | 15 | Indicates the completion item represents an insertable code snippet with tab stops. |
| `Color` | 16 | Indicates the completion item represents a color value. |
| `File` | 17 | Indicates the completion item represents a file reference. |
| `Reference` | 18 | Indicates the completion item represents a reference to another symbol. |
| `Folder` | 19 | Indicates the completion item represents a folder or directory. |
| `EnumMember` | 20 | Indicates the completion item represents an individual enum member value. |
| `Constant` | 21 | Indicates the completion item represents a constant value. |
| `Struct` | 22 | Indicates the completion item represents a struct or table type. |
| `Event` | 23 | Indicates the completion item represents an event. |
| `Operator` | 24 | Indicates the completion item represents an operator. |
| `TypeParameter` | 25 | Indicates the completion item represents a generic type parameter. |