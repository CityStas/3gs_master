---
name: FunctionalTestResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Status of a single functional test run."
---

# FunctionalTestResult

Status of a single functional test run.

**Type:** enum

## Description

Represents the outcome of a single functional test run.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Passed` | 0 | The test run was successful. |
| `Warning` | 1 | The test run is potentially unstable. |
| `Error` | 2 | The test run failed. |