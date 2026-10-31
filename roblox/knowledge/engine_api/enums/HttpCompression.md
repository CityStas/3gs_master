---
name: HttpCompression
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the compression algorithm applied to HTTP request body sent via HttpService."
---

# HttpCompression

Specifies the compression algorithm applied to HTTP request body sent via
[HttpService](/docs/reference/engine/classes/HttpService.md).

**Type:** enum

## Description

Specifies the compression algorithm applied to the body of an HTTP request
when calling [HttpService:RequestAsync()](/docs/reference/engine/classes/HttpService.md) or
[HttpService:PostAsync()](/docs/reference/engine/classes/HttpService.md). Pass this enum value in the `Compress` field
of the request options table to reduce bandwidth when sending large payloads.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No compression is applied to the request body. This is the default. |
| `Gzip` | 1 | The request body is compressed using the Gzip algorithm before being sent. |