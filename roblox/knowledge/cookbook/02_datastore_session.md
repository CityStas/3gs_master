# Cookbook: сохранение данных игрока без потерь

Задача: прогресс игрока не теряется и не откатывается, когда он переходит между
серверами, а сервер падает.

## 1. Пять правил

1. `DataStoreService` работает только на сервере.
2. Любой вызов может упасть — `pcall` обязателен.
3. `UpdateAsync`, а не `SetAsync`, когда новое значение зависит от старого.
4. `GetAsync` вернул `nil` — это новый игрок. `GetAsync` **упал** — это не новый игрок:
   сохранять нельзя, иначе реальный прогресс будет перезаписан дефолтом.
5. Бюджет запросов ограничен (~60 + 10×игроков в минуту на чтение и на запись). Сохранять
   раз в 60–120 секунд и на выходе, а не каждый кадр.

## 2. Загрузка и сохранение

```lua
local DataStoreService = game:GetService("DataStoreService")
local store = DataStoreService:GetDataStore("PlayerData_v2")

local DEFAULT = { version = 2, coins = 0, inventory = {} }

local function retry<T>(fn: () -> T, attempts: number): (boolean, T?)
    for i = 1, attempts do
        local ok, result = pcall(fn)
        if ok then return true, result end
        if i < attempts then task.wait(2 ^ i) end
    end
    return false, nil
end

local function load(player: Player)
    local key = `player_{player.UserId}`
    local ok, data = retry(function()
        return store:GetAsync(key)
    end, 3)
    if not ok then
        warn(`не удалось загрузить {player.Name}: сессия на дефолтах, сохранение запрещено`)
        return nil                          -- nil = «не сохранять»
    end
    return data or table.clone(DEFAULT)     -- успешный nil = новый игрок
end

local function save(player: Player, data)
    local key = `player_{player.UserId}`
    local ok = retry(function()
        return store:UpdateAsync(key, function(_old)
            return data
        end)
    end, 3)
    if not ok then
        warn(`СОХРАНЕНИЕ НЕ УДАЛОСЬ {player.Name} ({key}) — повторить на следующем автосейве`)
    end
    return ok
end
```

## 3. Блокировка сессии (два сервера, один игрок)

Без блокировки: игрок вышел с сервера A, зашёл на B, B загрузил старые данные, A дописал
свои — прогресс B потерян.

```lua
local function acquire(key: string, jobId: string): boolean
    local ok, acquired = pcall(function()
        return store:UpdateAsync(key, function(old)
            old = old or table.clone(DEFAULT)
            local lock = old.lock
            local stale = not lock or (os.time() - (lock.at or 0)) > 60
            if lock and lock.job ~= jobId and not stale then
                return nil                  -- nil прерывает запись: блокировка чужая
            end
            old.lock = { job = jobId, at = os.time() }
            return old
        end)
    end)
    return ok and acquired ~= nil
end
```

`game.JobId` — идентификатор сервера. Блокировку снимать в `PlayerRemoving` и в
`BindToClose`.

## 4. BindToClose

```lua
game:BindToClose(function()
    local pending = 0
    for _, player in Players:GetPlayers() do
        local data = sessions[player]
        if data then
            pending += 1
            task.spawn(function()
                save(player, data)
                pending -= 1
            end)
        end
    end
    local deadline = os.clock() + 25
    while pending > 0 and os.clock() < deadline do
        task.wait(0.1)
    end
end)
```

Roblox даёт около 30 секунд. Сохранение, которое не уложилось, теряется — поэтому
автосейв раз в минуту важнее, чем идеальный финальный сейв.

## 5. Миграции схемы

Версия хранится в записи и применяется при загрузке, а не при сохранении:

```lua
local MIGRATIONS = {
    [1] = function(data)
        data.coins = data.money or 0
        data.money = nil
        data.version = 2
        return data
    end,
}
```

## 6. Симптомы

| Симптом | Причина |
|---|---|
| «DataStore request was added to queue» | превышен бюджет; при переполнении очереди вызов **отбрасывается** |
| «Cannot store dictionary in data store» | несериализуемое значение (Instance, смешанная таблица) |
| у части игроков прогресс сброшен | упавший `GetAsync` приняли за нового игрока |
| прогресс откатывается назад | два сервера без блокировки сессии |
| в Studio ничего не сохраняется | нужен доступ к API и опубликованное место |
