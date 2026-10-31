---
name: ThreadPoolConfig
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Thread pooling scheme for the task scheduler."
---

# ThreadPoolConfig

Thread pooling scheme for the task scheduler.

**Type:** enum

## Description

Controls the thread pooling scheme used by [TaskScheduler](/docs/reference/engine/classes/TaskScheduler.md). The selected
value determines how many worker threads the task scheduler allocates for
background work. [TaskScheduler.ThreadPoolConfig](/docs/reference/engine/classes/TaskScheduler.md) defaults to `Auto`.

The `PerCore` variants scale the thread count with the number of physical CPU
cores reported by the operating system. The `Threads` variants use an absolute
count regardless of hardware. `Auto` lets the scheduler choose internally.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Auto` | 0 | Let task scheduler make a decision internally. |
| `Threads1` | 1 | Utilize 1 worker thread, ignore the physical CPU core count. |
| `Threads2` | 2 | Utilize 2 worker threads, ignore the physical CPU core count. |
| `Threads3` | 3 | Utilize 3 worker threads, ignore the physical CPU core count. |
| `Threads4` | 4 | Utilize 4 worker threads, ignore the physical CPU core count. |
| `Threads8` | 8 | Utilize 8 worker threads, ignore the physical CPU core count. |
| `Threads16` | 16 | Utilize 16 worker threads, ignore the physical CPU core count. |
| `PerCore1` | 101 | Utilize 1 worker thread per available physical CPU core. |
| `PerCore2` | 102 | Utilize 2 worker threads per available physical CPU core. |
| `PerCore3` | 103 | Utilize 3 worker threads per available physical CPU core. |
| `PerCore4` | 104 | Utilize 4 worker threads per available physical CPU core. |