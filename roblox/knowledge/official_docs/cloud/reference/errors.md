---
title: "Errors"
url: /docs/en-us/cloud/reference/errors
last_updated: 2026-10-30T19:55:39Z
description: "Defines the errors that are returned by Open Cloud APIs"
---

# Errors

The following sections describe the error handling for Open Cloud APIs. Due to implementation differences across endpoints and validation layers, error responses can vary significantly in format.

## Gateway errors

For authentication or routing issues, both Open Cloud v1 and v2 APIs may return errors in this format:

```json
{
  "errors": [
    {
      "code": 0,
      "message": "Invalid API Key"
    }
  ]
}
```

## Open Cloud v2

Open Cloud v2 APIs generally follow a consistent error format when the error occurs within the API endpoint itself.

### Standard v2 error format

Open Cloud v2 APIs return errors in this format:

- `code` - A string representing the error type (e.g. `INVALID_ARGUMENT`, `NOT_FOUND`).
- `message` - A human-readable message explaining the error.
- `details` - An optional array containing additional error-specific information.

```json
{
  "code": "INVALID_ARGUMENT",
  "message": "Invalid User ID in the request."
}
```

```json
{
  "code": "INVALID_ARGUMENT",
  "message": "The provided filter is invalid.",
  "details": [
    {
      ...
    }
  ]
}
```

### v2 error codes

The following table describes possible values for `code` in v2 API responses.

| Code | HTTP Status | Description |
| --- | --- | --- |
| `INVALID_ARGUMENT` | 400 | You passed an invalid argument, such as an invalid `universeId`. You might also have missing or invalid headers, such as `Content-Length` and `Content-Type`. |
| `PERMISSION_DENIED` | 403 | Your request doesn't have sufficient permissions or scopes to perform the operation. |
| `NOT_FOUND` | 404 | The system can't find your specified resources, such as a data store entry. |
| `ABORTED` | 409 | The operation was aborted. |
| `RESOURCE_EXHAUSTED` | 429 | You don't have enough quota to perform the operation, typically due to sending too many requests. |
| `CANCELLED` | 499 | The system terminates the request, typically due to a client side timeout. |
| `INTERNAL` | 500 | Internal server error, typically due to a server bug. |
| `NOT_IMPLEMENTED` | 501 | The server doesn't implement the API method. |
| `UNAVAILABLE` | 503 | Service is unavailable, typically returned when the server is down. |

## Open Cloud v1

Open Cloud v1 APIs have inconsistent error response formats. The format depends on the specific endpoint, the type of error, and where the error occurs in the request processing pipeline.

Most v1 endpoints return errors in one of these three formats:

```json
{
  "error": "INVALID_ARGUMENT",
  "message": "Invalid cursor.",
  "errorDetails": [
    {
      "errorDetailType": "DatastoreErrorInfo",
      "datastoreErrorCode": "InvalidCursor"
    }
  ]
}
```

```json
{
  "code": "INVALID_ARGUMENT",
  "message": "Invalid cursor."
}
```

```json
{
  "errors": {
    "assetId": ["The value 'a' is not valid."]
  },
  "type": "https://tools.ietf.org/html/rfc9110#section-15.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "extensions": {
    "traceId": "00-427917f0fc3b8375ee33e4603a7f0693-f3f6ad560ff1a122-00"
  }
}
```

### v1 error codes

The following table describes possible values for `error` or `code` in v1 API responses:

| HTTP Status Code | Error | Descriptions |
| --- | --- | --- |
| 400 | INVALID_ARGUMENT | You passed an invalid argument, such as an invalid `universeId`. You might also have missing or invalid headers, such as `Content-Length` and `Content-Type`. |
| 403 | INSUFFICIENT_SCOPE | The request requires higher privileges than provided by the access token. |
| 403 | PERMISSION_DENIED | Your request doesn't have sufficient scope to perform the operation. |
| 404 | NOT_FOUND | The system can't find your specified resources, such as a data store. |
| 409 | ABORTED | The operation was aborted due to a conflict, such as publishing a place that is not part of the universe. |
| 429 | RESOURCE_EXHAUSTED | You don't have enough quota to perform the operation, typically due to sending too many requests. |
| 499 | CANCELLED | The system terminates the request, typically due to a client side timeout. |
| 500 | INTERNAL | Internal server error. Typically a server bug. |
| 501 | NOT_IMPLEMENTED | The server doesn't implement the API method. |
| 503 | UNAVAILABLE | Service unavailable. Typically the server is down. |
