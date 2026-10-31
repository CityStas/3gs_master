---
title: "Free camera mode"
url: /docs/en-us/workspace/camera/free-camera
last_updated: 2026-10-30T19:56:02Z
description: "Free camera mode allows free roam of the local camera around the scene."
---

# Free camera mode

Roblox provides a custom debug **free camera mode** (freecam) to experience owners and editors, which detaches the camera from your character so you can fly it freely through your experience for capturing scenes the default camera can't reach. It's especially useful for capturing cinematic screenshots and videos, as well as spectating players in live games and debugging issues.

## Availability

You can use free camera mode in two places:

- **Roblox Studio** - freecam is available during [playtesting](/docs/en-us/studio/testing-modes.md#playtesting) sessions.
- **The live client** - you must be the experience owner, or be granted edit permissions in the experience.

> **Info:** Currently, freecam can only be toggled on with a keyboard (`Left Shift` + `P`). Once active, it can be controlled with either keyboard and mouse or a gamepad.
## How to toggle

Press `Left Shift` + `P` to toggle free camera mode on or off. When enabled, the camera detaches from your character and your on-screen UI is automatically hidden so you get an unobstructed view of the scene.

## Input Action System

The enhanced free camera capabilities described on this page — including the [configuration menu](#configuration-menu) and [cinematic post-processing](#custom-post-processing) — run on the [Input Action System](/docs/en-us/input/input-action-system.md) (IAS) and are available only when your experience is opted into the upgraded IAS player scripts.

To opt in, set `Class.Workspace.PlayerScriptsUseInputActionSystem` to `Enum.RolloutState|Enabled` to allow free camera controls to run on IAS so inputs sink cleanly alongside your default gameplay actions.

## Camera controls

In freecam mode, the camera can move and rotate to your desired positioning independent of the character and scene. The following controls are available to control the camera:

| Action | Keyboard & Mouse | Gamepad |
| --- | --- | --- |
| Move forward / left / back / right | `W` `A` `S` `D` | Left thumbstick |
| Change elevation (up / down) | `E` / `Q` | `R2` / `L2` |
| Rotate / pan the view | Hold the right mouse button and drag, or pan on a trackpad | Right thumbstick |
| Zoom (field of view) | Mouse scroll wheel, or trackpad pinch | `X` / `Y` |
| Roll (tilt left / right) | `Z` / `C` — double-tap either key to reset roll | `L1` / `R1` — double-tap to reset roll |
| Move slower for precise framing | Hold `Shift` while moving | — |
| Open the configuration menu | `↑` (up arrow) | D-pad Up |

### Movement

Use `W` `A` `S` `D` (or the left thumbstick) to fly the camera through your scene.

### Elevation

Use `E` and `Q` (or `R2` / `L2`) to raise and lower the camera vertically.

### Rotation

Hold the right mouse button and drag (or use the right thumbstick) to rotate and pan the view toward your subject.

### Field of view

Scroll the mouse wheel (or press `X` / `Y` on a gamepad) to zoom the field of view. Narrowing the field of view produces a tighter, more telephoto framing on distant subjects.

### Roll

Use `Z` and `C` (or `L1` / `R1`) to roll the camera for a Dutch-angle effect. Double-tap either roll control to snap the camera back to the default level.

## Configuration menu

Press `↑` (or D-pad Up) to open the on-screen **config menu**, which exposes deeper adjustments for fine-tuning your shot.

Navigate the menu with the following controls:

- `↑` `↓` move the selection through the list.
- `→` enters a group or selects an item to edit.
- `←` goes back to the previous level, or closes the menu from the top level.
- When editing an item, `←` `→` adjust the value and `↑` `↓` exit editing.

On a gamepad, use the D-pad in the corresponding directions.

### Movement, rotation, roll, and field of view

Each of these motion controls exposes two independent settings in the config menu:

- **Speed** controls how fast the value changes. Increase it to cover ground, zoom, tilt, or pan more quickly; decrease it for fine, precise adjustments.
- **Stiffness** controls how the camera settles into an input change. Higher stiffness is snappy and follows your input tightly with little smoothing; lower stiffness adds damping so the camera eases in and out gradually for smoother, more cinematic motion.

**High speed** — the camera rotates quickly:

**Low speed** — the camera rotates slowly for precise framing:

**High stiffness** — the camera follows input tightly and stops sharply:

**Low stiffness** — the camera eases in and out for smoother, more cinematic motion:

### UI visibility

Control which on-screen interface stays visible so you can capture a clean shot or keep key information on screen.

- **Screen GUIs** — toggle the experience's on-screen UI overlays. Set to **On** to keep them visible, or **Off** to hide them for an unobstructed view.
- **Leaderboard** — toggle the player leaderboard. Set to **On** to keep it on screen, or **Off** to hide it.

### Player Lock

Player Lock keeps the camera trained on a specific player's character as they move, so you can follow the action without manually tracking.

- **Enable** — turn Player Lock on or off. When on, the camera follows the chosen target; when off, the camera moves freely.
- **Target** — cycle through the players in the server to choose who the camera locks onto.

### Custom post-processing

Layer cinematic [post-processing effects](/docs/en-us/environment/post-processing-effects.md) onto your shot. **Enable** disables all existing post-processing effects in favor of custom freecam ones, and each effect below can then be toggled and fine-tuned on its own:

- [**Depth of Field**](/docs/en-us/environment/post-processing-effects.md#depth-of-field) blurs parts of the scene that aren't in focus — great for drawing the eye to a subject or softening a distant background.
- [**Bloom**](/docs/en-us/environment/post-processing-effects.md#bloom) exaggerates bright lights so light-colored areas glow, simulating a camera pointed at a strong light source.
- [**Blur**](/docs/en-us/environment/post-processing-effects.md#blur) applies a Gaussian blur across the entire view for soft, dreamy, or fully out-of-focus looks.
- [**Color Correction**](/docs/en-us/environment/post-processing-effects.md#color-correction) adjusts brightness, contrast, saturation, and tint to set the mood or grade the overall color of your shot.
- [**Sun Rays**](/docs/en-us/environment/post-processing-effects.md#sun-rays) casts a halo of light with rays around the sun, shaped by objects between the camera and the sun for realistic light and shadow.
- [**Color Grading**](/docs/en-us/environment/post-processing-effects.md#color-grading) changes how rendered colors map to the screen — switch between the vivid modern look and a less-saturated retro tone.

## GUI visibility shortcuts

Separate from the config menu's [UI visibility](#ui-visibility) toggles, Roblox provides engine-level keyboard shortcuts that hide categories of on-screen UI, useful for capturing a clean shot without any interface. They work in the **live client** and in a Studio **playtest**, and are available to the same audience as free camera — the experience owner or a user with edit permission (and always in Studio). Press the same shortcut again to restore.

These controls are currently available for keyboard only. Hold `Ctrl` (or `⌘` on macOS) and `Left Shift`, then press:

| Shortcut | Hides / shows |
| --- | --- |
| `Ctrl``Left Shift``G` | The Roblox-provided **Core UI**, such as the top bar and menus. |
| `Ctrl``Left Shift``C` | Developer-created `Class.ScreenGui\|ScreenGuis` (on-screen 2D UIs). |
| `Ctrl``Left Shift``B` | Developer-created `Class.BillboardGui\|BillboardGuis` (world-space 3D billboards). |
| `Ctrl``Left Shift``N` | Player nameplates (names and health bars). |

**`Ctrl``Left Shift``G`** — toggle the Roblox Core UI:

**`Ctrl``Left Shift``C`** — toggle the experience's on-screen GUIs:

**`Ctrl``Left Shift``B`** — toggle developer-created BillboardGuis:

**`Ctrl``Left Shift``N`** — toggle player nameplates:
