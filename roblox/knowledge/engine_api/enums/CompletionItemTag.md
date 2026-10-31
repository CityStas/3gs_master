---
name: CompletionItemTag
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the tags for completion items in ScriptEditorService:RegisterAutocompleteCallback()."
---

# CompletionItemTag

Determines the tags for completion items in
[ScriptEditorService:RegisterAutocompleteCallback()](/docs/reference/engine/classes/ScriptEditorService.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Deprecated` | 1 | Indicates that the completion is deprecated, applying a penalty towards its score and crossing it out in the completion list. |
| `IncorrectIndexType` | 2 | Indicates that the completion is a member and being accessed with the wrong index type (e.g. using `:` to access a property), hiding it from the completion list. |
| `PluginPermissions` | 3 | Indicates that the completion requires Plugin security level to access, hiding it if the client lacks this level. |
| `CommandLinePermissions` | 4 | Indicates that the completion requires Command line security level to access, hiding it if the client lacks this level. |
| `RobloxPermissions` | 5 | Indicates that the completion requires core script security level to access, hiding it if the client lacks this level. |
| `AddParens` | 6 | Instructs the editor to add parentheses before the cursor after inserting the given completion, if accepted. |
| `PutCursorInParens` | 7 | Instructs the editor to add parentheses before the cursor and move the cursor into the parentheses after inserting the given completion, if accepted. |
| `TypeCorrect` | 8 | Indicates that the completion is type correct in the current context, granting a bonus to its score. |
| `ClientServerBoundaryViolation` | 9 | Indicates that the completion is being accessed from the wrong side of the client/server boundary (e.g. Players.LocalPlayer in a server script), hiding it from the completion list. |
| `Invalidated` | 10 | Indicates that the completion is stale because the cursor has moved outside the item's valid replacement range, hiding it from the completion list. |
| `PutCursorBeforeEnd` | 11 | Instructs the editor to move the cursor to just before the nearest preceding `end` keyword after inserting the given completion, if accepted. |