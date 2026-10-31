---
name: CoreGuiType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Represents all available CoreGui \"types\" such as the Backpack and text chat window."
---

# CoreGuiType

Represents all available [CoreGui](/docs/reference/engine/classes/CoreGui.md) "types" such as the [Backpack](/docs/reference/engine/classes/Backpack.md)
and text chat window.

**Type:** enum

## Description

This enum represents all available [CoreGui](/docs/reference/engine/classes/CoreGui.md) "types" such as the
[Backpack](/docs/reference/engine/classes/Backpack.md) and text chat window.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PlayerList` | 0 | Dynamically updated [Players](/docs/reference/engine/classes/Players.md) list, commonly used as a [leaderboard](/docs/en-us/players/leaderboards.md). |
| `Health` | 1 | The character's [Health](/docs/reference/engine/classes/Humanoid.md) bar. |
| `Backpack` | 2 | The character's [Backpack](/docs/reference/engine/classes/Backpack.md) which contains [in‑experience tools](/docs/en-us/players/tools.md). |
| `Chat` | 3 | The [text chat](/docs/en-us/chat/in-experience-text-chat.md) window. |
| `All` | 4 | Refers to all available core UI. |
| `EmotesMenu` | 5 | Popup menu of character [emotes](/docs/en-us/characters/emotes.md). |
| `SelfView` | 6 | A player's perspective or view of their own character. |
| `Captures` | 7 | A "capture" button along the right side of the screen. |
| `AvatarSwitcher` | 8 | The **Avatar Switcher** allows users to change their platform avatar. |
| `ExperienceShop` | 9 | The in-experience shop overlay that lets players browse and purchase items without leaving the experience. |