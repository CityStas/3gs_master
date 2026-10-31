local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")

local player = Players.LocalPlayer
local gui = script.Parent:findFirstChild("ShopGui")
local part = Instance.new("Part", workspace)

print(player, gui, part)
