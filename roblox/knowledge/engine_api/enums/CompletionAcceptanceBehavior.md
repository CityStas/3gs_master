---
name: CompletionAcceptanceBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the Script Editor inserts or replaces text when an autocomplete suggestion is accepted with Enter or Tab."
---

# CompletionAcceptanceBehavior

Controls how the Script Editor inserts or replaces text when an autocomplete
suggestion is accepted with Enter or Tab.

**Type:** enum

## Description

Controls how the Script Editor treats existing text **after** the cursor when
you accept an autocomplete suggestion with Enter or Tab. Accepting a
completion always replaces the typed prefix **before** the cursor. The active
value is stored in [Studio.AutocompleteAcceptanceBehavior](/docs/reference/engine/classes/Studio.md), which
defaults to [CompletionAcceptanceBehavior.InsertOnEnterReplaceOnTab](/docs/reference/engine/enums/CompletionAcceptanceBehavior.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Insert` | 0 | Accepting a completion with either Enter or Tab inserts the suggestion without replacing existing text after the cursor. |
| `Replace` | 1 | Accepting a completion with either Enter or Tab replaces existing text after the cursor with the full suggestion text. |
| `ReplaceOnEnterInsertOnTab` | 2 | Pressing Enter replaces existing text after the cursor; pressing Tab inserts without replacing text after the cursor. |
| `InsertOnEnterReplaceOnTab` | 3 | Pressing Enter inserts without replacing text after the cursor; pressing Tab replaces text after the cursor. This is the default of [Studio.AutocompleteAcceptanceBehavior](/docs/reference/engine/classes/Studio.md). |