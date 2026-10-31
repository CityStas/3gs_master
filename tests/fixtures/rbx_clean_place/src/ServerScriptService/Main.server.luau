--!strict
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Shop = require(ReplicatedStorage:WaitForChild("Shop"))

local function onPlayerAdded(player: Player)
	task.wait(0.1)
	local cart = { { name = "Sword", price = 10 }, { name = "Shield", price = 25 } }
	local total = Shop:total(cart)
	Shop:notify(player, total > 0)
end

Players.PlayerAdded:Connect(onPlayerAdded)
