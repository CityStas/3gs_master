---
title: "Dynamic clouds"
url: /docs/en-us/environment/clouds
last_updated: 2026-10-30T19:55:43Z
description: "Dynamic Clouds render realistic, customizable clouds that drift slowly across the sky."
---

# Dynamic clouds

Roblox's **dynamic clouds** are realistic clouds that drift slowly across the sky. You can adjust their appearance through the `Class.Clouds` object to create unique atmospheres such as stormy skies, stunning sunsets, and alien worlds. You can also customize their direction and speed through [global wind](/docs/en-us/environment/global-wind.md).

## Enable clouds

You can manage dynamic clouds in a game through the `Class.Clouds` object. While you can place this object anywhere for organization or replication purposes, clouds only render if you parent the object under the `Class.Terrain` class.

To enable dynamic clouds:

1. In the **Explorer** window, hover over **Terrain** and click the ⊕ button. A contextual menu displays.
2. From the menu, insert **Clouds**.![Clouds object shown in Explorer window of Studio](../assets/studio/explorer/Terrain-Clouds.png)
3. Adjust the appearance of clouds through the new object's properties.
4. Set the clouds in motion through [global wind](/docs/en-us/environment/global-wind.md).

## Cloud properties

From the `Class.Clouds` object under `Class.Terrain`, you can adjust the appearance of clouds through the **Properties** window.

### Cover

The `Class.Clouds.Cover|Cover` property controls how much the clouds span across the overall skyscape layer from a value of 0 (sparse cloud cover) to 1 (full cloud cover).

#### 0.65

![Clouds with Cover value of 0.65](../assets/lighting-and-effects/clouds/Cover-A.jpg)

#### 0.8

![Clouds with Cover value of 0.8](../assets/lighting-and-effects/clouds/Cover-B.jpg)

### Density

The `Class.Clouds.Density|Density` property controls the intensity of the particles that make up each cloud, mainly affecting their transparency. For example, lower values produce light, semi-translucent clouds, and higher values produce heavy, dark clouds with a stormy appearance.

#### 0.1

![Clouds with Density value of 0.05](../assets/lighting-and-effects/clouds/Density-A.jpg)

#### 0.3

![Clouds with Density value of 0.4](../assets/lighting-and-effects/clouds/Density-B.jpg)

### Color

The `Class.Clouds.Color|Color` property controls the material color of cloud particles. It's important to note that several `Class.Lighting` and `Class.Atmosphere` properties also influence cloud color, so if you want to simulate specific atmospheres, experiment with multiple properties until you have the effect you want.

#### [255, 255, 255]

![Clouds with Color value of [255, 255, 255]](../assets/lighting-and-effects/clouds/Color-A.jpg)

#### [75, 50, 255]

![Clouds with Color value of [75, 50, 255]](../assets/lighting-and-effects/clouds/Color-B.jpg)
