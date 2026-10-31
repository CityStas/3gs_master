---
title: "Pickup system"
url: /docs/en-us/resources/battle-royale/pickup-system
last_updated: 2026-10-30T19:55:54Z
description: "Explains the pickup system for the Battle Royale game kit."
---

# Pickup system

The Roblox Battle Royale **pickup system** lets players pick up different kinds of objects, although it's currently only used for weapon pickups. In game, weapons are spawned around the game map and — when players get close enough — an on-screen key/action/button prompt appears along with the weapon name and description.

![Battle Royale Weapon Example](../../assets/resources/battle-royale/pickup-system/Battle-Royale-Weapon-Pickup.jpg)
> **Info:** Roblox Battle Royale uses the [Weapons Kit](/docs/en-us/resources/weapons-kit.md), so please consult its documentation for details and customization options.
## Structure

There are several important folders related to the pickup system. Make sure that these folders are set up correctly in your project:

- `Workspace/PickupSpawners` — Contains pickup spawner `Class.Part|Parts` which tell the system where to place visual pickup `Class.Model|Models` (see the next point). Note that these spawners are **not required** to be in this folder since the system looks for parts tagged with the **PickupSpawner** tag instead of the folder path.![Pickup Spawners](../../assets/resources/battle-royale/pickup-system/Battle-Royale-PickupSpawners.png)
  > **Info:** Pickup spawners can be placed at any physical location in the game, but they will choose a weapon **randomly** from `ReplicatedStorage/Assets/Weapons` and use the name-matched pickup model as a visual representation.
- `ReplicatedStorage/Assets/Weapons` — Contains the weapons (functional `Class.Tool|Tools`) that the pickup system grants when a weapon pickup is activated.![Battle Royale Items](../../assets/resources/battle-royale/pickup-system/Battle-Royale-Weapons.png)
- `ReplicatedStorage/Assets/Pickups` — Contains the pickup `Class.Model|Models` that the system will place at pickup spawners in the game world. **These should be visual models only**, not functional weapon Tools.![Battle Royale Pickups](../../assets/resources/battle-royale/pickup-system/Battle-Royale-Pickups.png)

## Add new pickups

As noted above, pickups require both a functional `Class.Tool` and a visual `Class.Model` that will be spawned in the game world.

### Tool

1. Create a `Class.Tool` and give it a unique name. You can create new weapons based upon those in the [Weapons Kit](/docs/en-us/resources/weapons-kit.md) or take tools from the [Toolbox](/docs/en-us/projects/assets/toolbox.md).
2. Place the `Class.Tool` in `ReplicatedStorage/Assets/Weapons`.![Battle Royale New Weapon](../../assets/resources/battle-royale/pickup-system/Battle-Royale-New-Weapon.png)

### Model

1. Create a `Class.Model` for the visual pickup and give it the **same name** as you gave the `Class.Tool`.
2. Through the [Tags](/docs/en-us/studio/properties.md#instance-tags) section of its properties, apply the following tags to the model:
  - **Action**
  - **Pickup**
  - **WeaponPickup**
  - **WeaponSystemIgnore**
  - One of the rarity tags as outlined in [Rarity](#rarity).
3. Place the model in `ReplicatedStorage/Assets/Pickups`.![Battle Royale New Pickup](../../assets/resources/battle-royale/pickup-system/Battle-Royale-New-Pickup.png)

### Rarity

Pickup rarity is not defined by any mathematical formula, but you can associate an on-screen GUI like those pictured below to suggest an item's rarity.

1. Open the `ReplicatedFirst/Configurations/RarityConfiguration` script. This script contains tables for each rarity category, each of which includes a color value (`Color`) for the pickup's particle effect and an asset ID (`Image`) for the on-screen GUI background. For each GUI:
  - The item name will appear as the model/weapon name.
  - The description will appear as the rarity name (such as **Epic**) plus **Item**. The default rarities are as follows, but feel free to define your own. | Rarity | GUI |
| --- | --- | | Common |  | | Uncommon |  | | Rare |  | | Epic |  | | Legendary |  | | Special |  |
2. For the pickup `Class.Model` you created previously (located in `ReplicatedStorage/Assets/Pickups`), assign one of the tags you've defined in the `RarityConfiguration` script.
