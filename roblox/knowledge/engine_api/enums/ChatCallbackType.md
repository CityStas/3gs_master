---
name: ChatCallbackType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies a hook point in the legacy Luau chat pipeline for use with Chat:RegisterChatCallback() and Chat:InvokeChatCallback()."
---

# ChatCallbackType

Identifies a hook point in the legacy Luau chat pipeline for use with
[Chat:RegisterChatCallback()](/docs/reference/engine/classes/Chat.md) and [Chat:InvokeChatCallback()](/docs/reference/engine/classes/Chat.md).

**Type:** enum

## Description

Enumerates the callback hook points available in the legacy Luau chat system.
Pass a value to [Chat:RegisterChatCallback()](/docs/reference/engine/classes/Chat.md) to bind a function to the
corresponding event, and to [Chat:InvokeChatCallback()](/docs/reference/engine/classes/Chat.md) to invoke the
registered function for that event. Each value targets either the client or
the server; attempting to register a server-only callback on the client (or
vice versa) raises an error.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OnCreatingChatWindow` | 1 | Client-only callback invoked before the chat window is constructed, allowing custom settings to be supplied. |
| `OnClientSendingMessage` | 2 | Client-only callback reserved for when the client sends a message; not currently invoked. |
| `OnClientFormattingMessage` | 3 | Client-only callback invoked before a message is displayed, allowing its display data to be modified. |
| `OnServerReceivingMessage` | 17 | Server-only callback invoked when the server receives a message from a speaker, allowing the message to be modified or suppressed. |