--!strict
-- Shop: a module with one remote and one pure helper.
local ReplicatedStorage = game:GetService("ReplicatedStorage")

export type Item = {
	name: string,
	price: number,
}

local Shop = {}
Shop.__index = Shop

local purchase = Instance.new("RemoteEvent")
purchase.Name = "Purchase"
purchase.Parent = ReplicatedStorage

function Shop.new(): typeof(Shop)
	local self = setmetatable({}, Shop)
	return self
end

-- Total price of a cart, ignoring free items.
function Shop:total(items: { Item }): number
	local sum = 0
	for _, item in ipairs(items) do
		if item.price > 0 then
			sum += item.price
		end
	end
	return sum
end

function Shop:notify(player: Player, ok: boolean)
	purchase:FireClient(player, ok)
end

return Shop
