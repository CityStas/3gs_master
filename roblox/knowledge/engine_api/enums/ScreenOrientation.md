---
name: ScreenOrientation
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The preference of in-game screen orientation on hand-held devices."
---

# ScreenOrientation

The preference of in-game screen orientation on hand-held devices.

**Type:** enum

## Description

Indicates what orientation the game prefers to be played on mobile devices.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `LandscapeLeft` | 0 | A preference where the game is displayed landscape (horizontally) with the bottom of the device on the left side of the screen. |
| `LandscapeRight` | 1 | A preference where the game is displayed landscape (horizontally) with the bottom of the device on the right side of the screen. |
| `LandscapeSensor` | 2 | A preference where the game is displayed landscape (horizontally) with the bottom of the device on the left of right side of the screen depending on the device's orientation (the sensor determines which side allows for the game to be displayed right-side-up). |
| `Portrait` | 3 | A preference where the game is displayed portrait (vertically) with the bottom of the device on the bottom of the screen. |
| `Sensor` | 4 | A preference where the game is displayed depending on the best match to the device's current orientation - either landscape (left/right) or portrait. |