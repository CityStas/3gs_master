# Cookbook: валидированный RemoteEvent (сервер — источник истины)

Задача: клиент просит купить предмет. Клиент может врать про цену, количество, цель и
частоту запросов. Всё, что приходит из `RemoteEvent`, — недоверенный ввод.

## 1. Один модуль создаёт все remote-объекты

`ReplicatedStorage/Shared/Remotes.luau`

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Remotes = ReplicatedStorage:FindFirstChild("Remotes")
if not Remotes then
    Remotes = Instance.new("Folder")
    Remotes.Name = "Remotes"
    Remotes.Parent = ReplicatedStorage
end

local function get(name: string, className: string): Instance
    local existing = Remotes:FindFirstChild(name)
    if existing then return existing end
    local remote = Instance.new(className)
    remote.Name = name
    remote.Parent = Remotes
    return remote
end

return {
    Purchase = get("Purchase", "RemoteEvent"),
    GetInventory = get("GetInventory", "RemoteFunction"),
}
```

Почему так: если каждый скрипт создаёт свой remote, появляются дубликаты с одинаковым
именем, и `WaitForChild` на клиенте может вернуть не тот объект. Один модуль — одно имя.

## 2. Обработчик на сервере: шесть проверок

`ServerScriptService/Bootstrap.server.luau`

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Remotes = require(ReplicatedStorage.Shared.Remotes)
local ShopConfig = require(game:GetService("ServerStorage").Server.ShopConfig)

local RATE_LIMIT = 4                    -- запросов в секунду на игрока
local buckets: { [Player]: { count: number, reset: number } } = {}

local function allow(player: Player): boolean
    local now = os.clock()
    local b = buckets[player]
    if not b or now >= b.reset then
        b = { count = 0, reset = now + 1 }
        buckets[player] = b
    end
    b.count += 1
    return b.count <= RATE_LIMIT
end

Remotes.Purchase.OnServerEvent:Connect(function(player: Player, itemId: unknown)
    -- 1. тип
    if type(itemId) ~= "string" or #itemId > 64 then return end
    -- 2. частота
    if not allow(player) then return end
    -- 3. состояние персонажа
    local character = player.Character
    if not character or not character:FindFirstChild("HumanoidRootPart") then return end
    -- 4. существование предмета (цена берётся с сервера, не с клиента)
    local item = ShopConfig[itemId]
    if not item then return end
    -- 5. право владения / баланс
    if not Inventory.canPay(player, item.price) then return end
    -- 6. изменение состояния одним атомарным шагом
    Inventory.charge(player, item.price)
    Inventory.grant(player, itemId)
    Remotes.Purchase:FireClient(player, itemId, true)
end)

Players.PlayerRemoving:Connect(function(player)
    buckets[player] = nil               -- иначе таблица течёт на каждом вошедшем
end)
```

## 3. Клиент: только интерфейс, никакой логики цены

```lua
local button = script.Parent.BuyButton
button.Activated:Connect(function()
    if not button:GetAttribute("Enabled") then return end
    Remotes.Purchase:FireServer("speed_boost")
end)

Remotes.Purchase.OnClientEvent:Connect(function(itemId: string, ok: boolean)
    if not ok then
        warn(`покупка отклонена: {itemId}`)
    end
end)
```

Клиент не решает, хватает ли денег, и не отправляет цену. Он показывает то, что прислал
сервер.

## 4. Чего не делать

| Ошибка | Последствие |
|---|---|
| `FireServer(itemId, price)` | клиент назначает цену |
| проверка баланса только в UI | эксплойт покупает бесплатно |
| `RemoteFunction:InvokeClient` с сервера | серверный поток висит, если клиент не ответил |
| без лимита частоты | спам в обработчик, лаги у всех |
| `player.UserId` из payload | подмена: берите `player` из аргумента события |
