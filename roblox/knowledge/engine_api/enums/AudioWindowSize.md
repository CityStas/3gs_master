---
name: AudioWindowSize
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "For audio effects that use some internal buffering, determines the window-size used."
---

# AudioWindowSize

For audio effects that use some internal buffering, determines the window-size
used.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Small` | 0 | The smallest buffer size, providing the lowest latency at the cost of frequency resolution. |
| `Medium` | 1 | A mid-sized buffer that balances frequency resolution and latency. |
| `Large` | 2 | The largest buffer size, providing higher frequency resolution at the cost of more latency. |