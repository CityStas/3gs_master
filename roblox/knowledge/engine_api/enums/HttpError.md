---
name: HttpError
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum representing errors that can occur when making HTTP requests, unrelated to HTTP status codes returned by the server."
---

# HttpError

Enum representing errors that can occur when making HTTP requests, unrelated
to HTTP status codes returned by the server.

**Type:** enum

## Description

Transport-level errors that can occur when making HTTP requests via
[HttpService](/docs/reference/engine/classes/HttpService.md). These values are distinct from HTTP status codes (such as
404 or 500) that a remote server might return in a successful response;
[HttpError](/docs/reference/engine/enums/HttpError.md) values indicate that the request did not complete normally at
the network or client level.

When a request callback receives an error code other than [HttpError.OK](/docs/reference/engine/enums/HttpError.md),
the associated `HttpResponse` should not be considered valid.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OK` | 0 | No error occurred; the request completed successfully. This value is unrelated to the HTTP 200 OK status code. |
| `InvalidUrl` | 1 | The request URL is malformed or otherwise invalid; depending on the platform, a bad URL might instead surface as [HttpError.DnsResolve](/docs/reference/engine/enums/HttpError.md) or [HttpError.ConnectFail](/docs/reference/engine/enums/HttpError.md). |
| `DnsResolve` | 2 | The hostname in the request URL could not be resolved via DNS. |
| `ConnectFail` | 3 | The client failed to establish a TCP connection to the remote host. |
| `OutOfMemory` | 4 | The client ran out of memory while processing the HTTP request or response. |
| `TimedOut` | 5 | The request did not receive a response within the allowed time limit. |
| `TooManyRedirects` | 6 | The server returned more redirects than the client is configured to follow. |
| `InvalidRedirect` | 7 | The server returned a redirect response with an invalid or malformed Location header. |
| `NetFail` | 8 | A general network-level failure occurred that does not fall into a more specific error category. |
| `Aborted` | 9 | The HTTP request was aborted before it could complete. |
| `SslConnectFail` | 10 | The TLS/SSL handshake with the remote server failed during connection establishment. |
| `SslVerificationFail` | 11 | The server's TLS certificate could not be verified. |
| `Unknown` | 12 | An error occurred that does not map to any other [HttpError](/docs/reference/engine/enums/HttpError.md) value. |
| `ConnectionClosed` | 13 | The connection was closed by the remote end before the full response was received, typically indicating a server or network problem. |
| `ServerProtocolError` | 14 | An HTTP/2 protocol-level error was returned by the server. |
| `CreatorEnvironmentsNotSupportedByService` | 15 | The request was sent from a non-live environment (such as Studio) and the target service does not support creator environments. |
| `InactivityTimeout` | 16 | A streaming request timed out because no data was transferred during the inactivity window. |
| `TooManyOutstandingRequests` | 17 | The request was rejected because the client has exceeded its limit for concurrent or pending requests. |
| `InvalidRangeResponse` | 18 | The server returned an invalid response to a ranged HTTP request, such as responding with a full 200 status instead of the expected 206 Partial Content. |