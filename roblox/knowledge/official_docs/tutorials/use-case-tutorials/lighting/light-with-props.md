---
title: "Light with props"
url: /docs/en-us/tutorials/use-case-tutorials/lighting/light-with-props
last_updated: 2026-10-30T19:56:00Z
description: "The process for creating light sources out of props."
---

# Light with props

While overall world lighting is globally controlled through the `Class.Lighting` service, games can also include in-game **light sources** like lamps, torches, spotlights, TV screens, etc.

![alt](../../../assets/tutorials/lighting-with-props/Misty-Harbor-Banner.jpg)

## Starter project

The remainder of this tutorial uses the [Misty Harbor](https://www.roblox.com/games/6445909934/Misty-Harbor) project as a showcase. To follow along, open it in Studio before proceeding.

![Edit in Studio option from the game's main page](../../../assets/tutorials/lighting-with-props/Misty-Harbor-Edit-Place.png) ## Point lights

A `Class.PointLight` emits light **spherically** from a single point. This object is ideal for non-directional light sources like bulbs, torches, and fireballs.

Light sources like point lights need to be inserted directly into parts, meshes, or attachments. Here, a point light will be inserted into an existing model within the darkened city.

1. Find and select a **LightPole** model like the one shown below, near the central fountain.![alt](../../../assets/tutorials/lighting-with-props/LightPole-Select-Model.jpg)
2. In the **Explorer** window, expand the model's tree and select the **LightCasing** part.
3. Change its **Material** property to **Neon** — this will make the part appear to glow brightly, although it will not actually emit any light.
4. With **LightCasing** still selected, insert a new **PointLight** object.
5. With **PointLight** selected, customize its **Brightness** and **Color** values._Brightness = 4__Color = 255, 175, 100_
6. Further customize the light by adjusting its **Range** property. This value defines the radial distance of illumination from the light's position, measured in studs._Range = 8__Range = 12_

## Spot lights

A `Class.SpotLight` emits light in the shape of a **cone**. This object is ideal for light sources like street lamps, flashlights, and headlights.

1. Select the taller arched **StreetLight** model next to the construction across the street. Currently the light is pointed out instead of down at the street.![alt](../../../assets/tutorials/lighting-with-props/StreetLight-Select-Model.jpg)
2. Expand the model's tree to reveal the **SpotLight** object.
3. With **SpotLight** selected, test out different values for its **Face** property to change which face/axis light is emitted from._Face = Left__Face = Bottom_
4. Adjust the **Angle** property to increase or decrease the spread of light emission. The maximum value is 180 which illuminates a full half sphere from the cone's apex._Angle = 30__Angle = 75_
5. Experiment with different **Brightness** and **Color** values, as with the point light.

## Surface lights

A `Class.SurfaceLight` emits light from the entire surface/face of a part, rather than just from a single point. This object is useful for light sources like TV or computer screens, lighted billboards, and fluorescent panels.

1. Find and select the lighted **RobloxBillboard** sign on top of the café.![alt](../../../assets/tutorials/lighting-with-props/Billboard-Select-Model.jpg)
2. Expand the model's tree to reveal the SurfaceLight object.
3. With **SurfaceLight** selected, test out different **Face** values to change which face/surface light is emitted from. Notice that light is emitted from the **entire surface**, not a point upon it._Face = Bottom__Face = Right_
4. Adjust the **Angle** property to increase or decrease the spread of light emission from the part's surface. An angle of 0 means that light travels directly outward from the surface while an angle of 180 means light travels outward perpendicular to the surface._Angle = 60__Angle = 0_

By using lighting props instead of just general world lighting, you open up the possibility of creating new genres and environments like cyberpunk cities, traditional light festivals, or moody detective scenes.
