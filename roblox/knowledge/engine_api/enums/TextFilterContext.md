---
name: TextFilterContext
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether text submitted to TextService:FilterStringAsync() or TextService:FilterAndTranslateStringAsync() is intended for a public or private audience, controlling the strictness of the text filtering backend."
---

# TextFilterContext

Indicates whether text submitted to [TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md) or
[TextService:FilterAndTranslateStringAsync()](/docs/reference/engine/classes/TextService.md) is intended for a public
or private audience, controlling the strictness of the text filtering backend.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PublicChat` | 1 | Indicates the string will be visible to all players or a broad public audience, applying the strictest level of text filtering. |
| `PrivateChat` | 2 | Indicates the string is part of a private conversation between specific users, applying filtering appropriate for one-to-one or small-group exchanges. |