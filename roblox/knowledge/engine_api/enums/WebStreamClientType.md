---
name: WebStreamClientType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies what type of streaming to use when creating a WebStreamClient."
---

# WebStreamClientType

Specifies what type of streaming to use when creating a
[WebStreamClient](/docs/reference/engine/classes/WebStreamClient.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `SSE` | 0 | Traditional Server-Sent Events (SSE) client. Requires `text/event-stream` to be returned in the `Content-Type` header. Messages in the stream will follow the [event stream format](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format). |
| `RawStream` | 1 | General purpose HTTP streaming client. It can connect to any server that provides streaming data transfer (e.g. [chunked encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Transfer-Encoding)). It provides no guarantees about the stream format. |
| `WebSocket` | 2 | [WebSocket](https://en.wikipedia.org/wiki/WebSocket) client that provides a bidirectional communication channel over a TCP connection. |