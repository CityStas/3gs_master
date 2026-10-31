--!strict
local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")

local store = DataStoreService:GetDataStore("Test_v1")

local function onPlayerAdded(player: Player)
	local data = store:GetAsync("player_" .. player.UserId)
	print("loaded", data)
	local me = Players.LocalPlayer
	print(me)
end

Players.PlayerAdded:Connect(onPlayerAdded)

while true do
	wait(1)
end
