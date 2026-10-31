---
title: "Installation and setup"
url: /docs/en-us/resources/battle-royale/installation-and-setup
last_updated: 2026-10-30T19:55:54Z
description: "Explains the installation and setup details for the Battle Royale game kit."
---

# Installation and setup

To setup the Battle Royale game, you must download [Studio](/docs/en-us/studio/setup.md) and the project [reference files](#reference-files).

Additional configuration of the [place IDs](#copy-and-paste-place-ids), [server](#adjust-server-fill), and [publishing](#publish-additional-places) settings are also required before continuing on to [running the game](/docs/en-us/resources/battle-royale/run-the-game.md).

## Reference files

[RobloxBattleRoyale.zip](../../assets/resources/battle-royale/installation-and-setup/RobloxBattleRoyale.zip) consists of easily accessible `.rbxl` files which you can open in Roblox Studio and experiment with immediately.

| Name | Description |
| --- | --- |
| Lobby.rbxl | Entrance lobby where players choose the game mode. |
| Gameplay.rbxl | Where the battle match takes place. |
| Queue.rbxl | Queue place where players gather before being teleported to battle map. |

## Create a new game

Roblox Battle Royale must be structured as a game with six unique places. To begin:

1. Open `Lobby.rbxl` in Roblox Studio.![Lobby View.](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Lobby-View.jpeg)
2. Select **File** → **Publish As…** to open the publishing window.
3. Near the bottom of the window, click **Create new experience**.
4. Type in **Lobby** for the place name.![Set Lobby Name](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Lobby-Set-Name.png)
5. For the **Creator** field, select "Me" to publish the place to your personal account, or select a group.
6. When ready, click the **Create** button.

## Add additional places

Once the lobby place is published, you'll need to add **five additional places** to the game:

1. If it's not already visible, open the **Asset Manager** window.
2. Double-click the **Places** folder.![Select Places](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-AM-Select-Places-1.png)
3. Right-click in any empty region of the window (not over a place name/tile) and select **Add New Place**. Repeat this a total of five times so that you have six places.
4. Right-click each of the **new** places, select **Rename**, and name them as follows:![Battle royale Place Names](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Place-Names.png)
5. Publish the game again (**File** → **Publishx**).

## Copy and paste place IDs

Each place must be cross-associated so that players can teleport from the lobby to various play mode queues and vice-versa. To achieve this, you'll need to gather the place IDs of the places you created above.

1. In the **Asset Manager** window, right-click **Lobby** and select **Copy ID to Clipboard**.![Copy Lobby ID](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Lobby-Copy-ID.png)
2. If it's not already visible, open the **Explorer** window.
3. Open the **MainConfiguration** script within **ReplicatedFirst** → **Configurations**.![MainConfiguration Script](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Place-MainConfiguration.png)
4. Locate the `_places` table and paste the copied ID from step #1 as the value of the `lobby` key.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local Players = game:GetService("Players")


local isServer = RunService:IsServer()
local ConfigEvent = nil

local _placeOverrides = {}
local _overrides = {}

---

-- List of named places in the game
local _places = {
 lobby = 0123456789,
 gameplay_development = 0,
 queue_default = 0,
 queue_deathmatch = 0,
 queue_teamDeathmatch = 0,
 queue_freePlay = 0
}

---
```
5. Repeat the **Copy ID to Clipboard** process for the other five places and paste them into the associated `_places` table key value. | Place | Table key |
| --- | --- | | Lobby | lobby | | Gameplay | gameplay_development | | Queue (Default) | queue_default | | Queue (Deathmatch) | queue_deathmatch | | Queue (Team Deathmatch) | queue_teamDeathmatch | | Queue (Free Play) | queue_freePlay |```lua
-- List of named places in the game
local _places = {
 lobby = 0123456789,
 gameplay_development = 0987654321,
 queue_default = 0123459876,
 queue_deathmatch = 0987651234,
 queue_teamDeathmatch = 0132457689,
 queue_freePlay = 0678912345
}
```
6. Publish the game again (**File** → **Publish**).

## Adjust server fill

By default, Roblox balances players/servers for an optimal social gameplay experience, but a battle royale should allow for bigger and more intense battles. To achieve this:

1. Open Studio's **File** ⟩ **Experience Settings** window.
2. Select the **Places** tab.
3. For each of the six places, click the button and select **Edit**.![Edit Place Settings](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Edit-Place.png)
4. For **Server Fill**, select **Maximum**.![Set Server Fill to Maximum.](../../assets/resources/battle-royale/installation-and-setup/Place-Server-Fill-Maximum.png)
5. Click **Save** at the bottom of the window.

## Publish additional places

Now you'll need to open the remaining `.rbxl` files from the downloaded bundle, modify their `_places` tables, and publish them.

### Copy places table

1. Refer to the `_places` table in the lobby's **MainConfiguration** script:

```lua
--------------------------------------
-- List of named places in the game
local _places = {
	lobby = 0123456789,
	gameplay_development = 0987654321,
	queue_default = 0123459876,
	queue_deathmatch = 0987651234,
	queue_teamDeathmatch = 0132457689,
	queue_freePlay = 0678912345
}
--------------------------------------
```

1. Select the **entire table** and copy it to the clipboard with `Ctrl``C` (`⌘``C` on Mac).
2. Close the lobby place by clicking the X in its tab.![Close Lobby Tab.](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Lobby-Close.png)

### Replace tables

1. Open the `Gameplay.rbxl` file.
2. Open its **MainConfiguration** script within **ReplicatedFirst** → **Configurations**.![MainConfiguration Script](../../assets/resources/battle-royale/installation-and-setup//Battle-Royale-Place-MainConfiguration.png)
3. Paste the `_places` table you copied above over the existing `_places` table (`Ctrl``V`; `⌘``V`) so that each place's tables are identical.```lua
--------------------------------------
-- List of named places in the game
local _places = {
 lobby = 0123456789,
 gameplay_development = 0987654321,
 queue_default = 0123459876,
 queue_deathmatch = 0987651234,
 queue_teamDeathmatch = 0132457689,
 queue_freePlay = 0678912345
}
--------------------------------------
```
4. Select **File** → **Publish As…** to open the publishing window.
5. Near the bottom of the window, click **Update existing experience…**.
6. Locate and click the **Lobby** place that you published earlier.
7. On the next screen, you should see a list of the places you added earlier. From the list, select the **Gameplay** place and click the **Overwrite** button.![Overwrite Existing Place](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Place-Overwrite.png)
8. Once the place is published, close it by clicking the X in its tab.![Close the place tab.](../../assets/resources/battle-royale/installation-and-setup/Battle-Royale-Gameplay-Close.png)
9. Open the `Queue.rbxl` file and repeat this process, using **File** → **Publish As…** to publish it to all four queue places. Essentially, `Queue.rbxl` should be published to the **Queue (Default)**, **Queue (Deathmatch)**, **Queue (Team Deathmatch)**, and **Queue (Free Play)** slots. | File | Publish Slot |
| --- | --- | | Lobby.rbxl | Lobby | | Gameplay.rbxl | Gameplay | | Queue.rbxl | Queue (Default) | | Queue.rbxl | Queue (Deathmatch) | | Queue.rbxl | Queue (Team Deathmatch) | | Queue.rbxl | Queue (Free Play) |
