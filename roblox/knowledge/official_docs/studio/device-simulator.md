---
title: "Device Simulator"
url: /docs/en-us/studio/device-simulator
last_updated: 2026-10-30T19:55:57Z
description: "Use Device Simulator to preview how your experience looks and behaves on devices you don't have in front of you, directly in Roblox Studio."
---

# Device Simulator

**Device Simulator** is a toolbar in Roblox Studio that previews how your experience looks and behaves on a device you don't have in front of you. It simulates a device's screen dimensions, pixel density, on-screen keyboard, and platform. The controls sit in a toolbar above the 3D viewport rather than in a separate panel, so you can reach them while you're playtesting.

> **Warning:** Device Simulator is in [beta](https://devforum.roblox.com/t/studio-beta-new-device-simulator-toolbar-and-network-simulator/4861695), and its functionality might change. To enable it, open **File** and select **Beta Features**, then enable **New Device Simulator** and restart Studio.
## Open Device Simulator

The toolbar appears above the 3D viewport whenever a place is open. It stays available in both edit and play modes, so you can change the simulated device in the middle of a playtest without stopping, switching, and restarting.

## Simulate a device

The left side of the toolbar holds one button per device category, followed by a chip naming the active device.

![Device Simulator toolbar showing an iPhone selected above the Studio viewport.](../assets/studio/device-simulator/device-simulator-toolbar.png)

| Category | What it simulates |
| --- | --- |
| **Phone** | Phones and tablets, including touch input and the on-screen keyboard. |
| **Desktop** | Desktop and laptop resolutions. |
| **Console** | Console output resolutions and gamepad-first input. |
| **Headset** | VR headsets. |

Clicking a category switches to that category's default device. A category is disabled when no device in it is available to simulate. Clicking the device chip opens the device menu, where devices are grouped to make the trade-off you're testing explicit:

- **Phone**: **Flagship**, **Mid-range**, and **Entry level**, so you can walk a layout down the performance ladder.
- **Desktop**, **Console**, and **Headset**: one group of built-in devices per category.
- **Custom**: devices you created yourself, in every category.
- **Current device**: no simulation. Your own monitor and input, listed under **Desktop**.

The last row of the menu, **Manage devices**, opens the Device Manager.

### Device controls

The right side of the toolbar holds actions that apply to the simulated device. Which ones appear depends on what you're simulating.

| Control | Available for | Description |
| --- | --- | --- |
| **Rotate** | Phones and tablets | Rotates the simulated device to the next orientation. |
| **Mock Android back button** | Android devices | Sends a back button press. Enabled while the client view is active. |
| **Touch controls** | Phones and tablets | Lists the keyboard and mouse shortcuts that stand in for multi-touch gestures while playtesting. |
| **Virtual controller** | All devices | Toggles [Controller Emulator](/docs/en-us/studio/controller-emulator.md), which emulates gamepads, VR controllers, and TV remotes. |
| **Display scaling** | While simulating a device | Chooses how the simulated screen is mapped onto your monitor. |

### Simulate touch input

A mouse has one contact point, so gestures that need two are mapped onto modifier keys. Open **Touch controls** to see the shortcuts for your platform:

- **Pinch + rotate**: Alt + drag
- **Two-finger pan**: Alt + Shift + drag

## Display scaling

A simulated 1080-pixel-tall phone screen and your 1080-pixel-tall monitor have the same pixel count but very different physical sizes, so a UI element that's comfortable on one can be unreadable on the other. The **Display scaling** menu chooses which of those properties the viewport preserves:

![Display scaling menu with physical size, actual resolution, fit to window, calibration, and auto-detection options.](../assets/studio/device-simulator/device-simulator-display-scaling.png)

| Mode | Description |
| --- | --- |
| **Physical size** | Matches the simulated screen's real-world size, so on-screen elements are as large as they would be in a player's hand. |
| **Actual resolution** | Maps one simulated pixel to one of your monitor's pixels. |
| **Fit to window** | Scales the simulated screen to fill the available viewport. |

**Physical size** only holds if Studio knows how large your own monitor is, which it can't read directly. Two menu items supply that number:

- **Auto-detect scaling** matches the pixel density and scaling factor your operating system reports for your display. Turning it off falls back to your saved manual calibration. This item only appears in **Physical size** mode, because it has no effect in the other two.
- **Calibrate physical scaling** measures your display by hand. Drag the slider until the image on screen matches the width of a student ID or library card. Calibrating turns auto-detect off and switches to **Physical size**.

Both values persist across sessions, so calibrating once is enough.

## Manage devices

**Manage devices** in the device menu opens the Device Manager, with one tab per category: **Mobile**, **Desktop**, **Console**, and **Headset**. It opens on the tab matching the device you're simulating.

![Device Manager showing device categories, standard and custom devices, and custom device configuration fields.](../assets/studio/device-simulator/device-manager.png) ### Show and hide standard devices

The **Standard** list holds Roblox's built-in devices. Use **Add devices** to choose which of them appear in the toolbar's device menu, and hide the rest to keep the menu down to the devices you actually test against. Hiding a device doesn't delete it, so you can re-add it at any time. Custom devices always stay visible, as does the device you're currently simulating.

![Add devices dialog with checkboxes that control which devices appear in the Standard list.](../assets/studio/device-simulator/device-manager-add-devices.png) ### Create custom devices

Add a custom device to model hardware Roblox doesn't ship a profile for, or to isolate a single property, such as the same phone with half the memory. **Duplicate** copies a standard device as a starting point.

| Field | Description | Accepted values |
| --- | --- | --- |
| **Name** | The name shown in the device menu. | Required, unique, 200 characters or fewer. |
| **Platform** | The platform the experience reports at runtime. | Platform of the simulated device. |
| **Dimensions** | Screen width and height in pixels. | Width 1 to 7680, height 1 to 4320. |
| **Pixel density** | Pixels per inch, which drives physical-size scaling. | 72 to 10,000. |
| **Keyboard height** | How much of the screen the on-screen keyboard covers, per orientation. | Portrait and landscape, 0 to 4320. |

## Simulate controller input

Simulating a device tells you how your experience looks on that hardware. It doesn't put a matching controller in your hands. [Controller Emulator](/docs/en-us/studio/controller-emulator.md) pairs with Device Simulator to emulate the gamepads, VR controllers, handhelds, and TV remotes that hardware ships with, so you can test input without owning any of it. Selecting a console, headset, handheld, or Android TV device here switches Controller Emulator to that device's matching controller automatically.

## Simulate network conditions

Simulating a device tells you how your experience looks on that hardware. It doesn't tell you how it feels on that hardware's connection. [Network Simulator](/docs/en-us/studio/network-simulator.md) is in the same toolbar and shapes traffic during a playtest, so you can test against high latency, jitter, and packet loss without a second device or a throttled router.

## Example workflows

- **Check a layout across form factors.** Click phone, then tablet, then console, and watch the viewport rescale to each. Safe area, overflow, and anchoring problems surface immediately.
- **Test the bottom of the performance range.** Simulate an **Entry level** phone rather than a **Flagship**, and confirm your UI still reads at that pixel density and your experience still fits in that memory budget.
- **Validate touch UX.** Simulate a touch device and use the touch shortcuts to confirm your inputs land where you expect.
- **Check the on-screen keyboard.** Simulate a phone, focus a text field, and confirm the keyboard doesn't cover the controls the player needs while typing.
- **Verify physical sizing.** Calibrate physical scaling once, then compare a phone against a tablet in **Physical size** mode to see whether your tap targets and text are large enough on the smaller screen.
