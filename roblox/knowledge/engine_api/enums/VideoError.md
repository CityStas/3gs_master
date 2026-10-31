---
name: VideoError
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the result of a video operation in the engine's video subsystem."
---

# VideoError

Indicates the result of a video operation in the engine's video subsystem.

**Type:** enum

## Description

`VideoError` represents the outcome of video operations performed by the
engine. Values are surfaced through video-related callbacks and APIs to
describe why an operation succeeded or failed.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Ok` | 0 | The video operation completed successfully without error. |
| `Eof` | 1 | The end of the video stream or file has been reached. |
| `EAgain` | 2 | No data is available at this moment; the caller should retry the operation. |
| `BadParameter` | 3 | An invalid or out-of-range parameter was supplied to the video operation. |
| `AllocFailed` | 4 | A memory allocation required for the video operation failed. |
| `CodecInitFailed` | 5 | The video codec failed to initialize. |
| `CodecCloseFailed` | 6 | The video codec failed to shut down cleanly. |
| `DecodeFailed` | 7 | The video decoder failed to decode a frame from the stream. |
| `ParsingFailed` | 8 | Parsing the video stream or container format failed. |
| `Unsupported` | 9 | The requested video operation or format is not supported on this platform. |
| `Generic` | 10 | A generic or unclassified error occurred in the video subsystem. |
| `DownloadFailed` | 11 | The video asset could not be downloaded. |
| `StreamNotFound` | 12 | The requested video stream could not be found. |
| `EncodeFailed` | 13 | The video encoder failed to encode a frame. |
| `CreateFailed` | 14 | Creating a required video resource or object failed. |
| `NoPermission` | 15 | The video operation was denied because the required permission, such as camera access, has not been granted. |
| `NoService` | 16 | The required video service is unavailable on this device or platform. |
| `ReleaseFailed` | 17 | Releasing a video resource failed. |
| `Unknown` | 18 | An unknown or unrecognized error occurred; this value covers errors that have no specific classification in this enum. |