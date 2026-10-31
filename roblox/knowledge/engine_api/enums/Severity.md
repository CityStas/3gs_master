---
name: Severity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Classifies the severity level of a Luau LSP diagnostic reported by a Script Analysis callback."
---

# Severity

Classifies the severity level of a Luau LSP diagnostic reported by a Script
Analysis callback.

**Type:** enum

## Description

`Severity` is used in the diagnostics table returned by Script Analysis
callbacks registered with
[ScriptEditorService:RegisterScriptAnalysisCallback()](/docs/reference/engine/classes/ScriptEditorService.md). Each diagnostic
entry can include a `severity` field set to one of these values to control how
the diagnostic is categorized in the **Script Analysis** tool and how the
corresponding source range is highlighted in the Script Editor.

The enum maps directly to the
[Language Server Protocol `DiagnosticSeverity` specification](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#diagnosticSeverity).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Error` | 1 | Reports a critical error that indicates a definite problem in the script. |
| `Warning` | 2 | Reports a potential problem that can cause incorrect behavior but does not prevent the script from running. |
| `Information` | 3 | Conveys informational context about the script without indicating a problem. |
| `Hint` | 4 | Provides a subtle suggestion, such as a style improvement or an unused-variable notice. |