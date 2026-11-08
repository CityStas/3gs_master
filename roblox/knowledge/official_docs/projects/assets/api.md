---
title: "Creator Store queries"
url: /docs/en-us/projects/assets/api
last_updated: 2026-10-30T19:55:51Z
description: "Creator Store Queries let you externally query the Creator Store and Marketplace Catalog."
---

# Creator Store queries

You can search Roblox's assets outside Studio by accessing the Creator Store API. Use the [Creator Store API](#creator-store-api) to query Studio assets, such as meshes, models, and audio, and the [Marketplace API](#marketplace-api) to query avatar assets on the Marketplace.

Each API requires a URL and custom search parameters for that specific catalog. If both URL and parameters are valid, the API returns a JSON format with the results of your search.

## Creator Store API

For information on making calls to the Creator Store API for search, see Toolbox Service in the [Open Cloud reference](/docs/en-us/cloud/reference/features/creator-store.md#Toolbox_SearchCreatorStoreAssets).

## Marketplace API

You can query avatar items from the Marketplace using the following URL: `https://catalog.roblox.com/v1/search/items/details?[params]`

You can replace `[params]` with the appropriate [query parameters](#query-parameters) to customize your search.

### Query parameters

You can specify search parameters by appending a series of parameters and values to the URL, each separated by a `&`.

Use the following parameters to query the Marketplace:

| Parameter | Type | Options and Values |
| --- | --- | --- |
| Category | byte | `0` = Featured<br>`1` = All<br>`2` = Collectibles<br>`3` = Clothing<br>`4` = BodyParts<br>`5` = Gear<br>`11` = Accessories<br>`12` = AvatarAnimations<br>`13` = CommunityCreations |
| CreatorType | byte | `1` = User<br>`2` = Group<br><br>Queries using `CreatorType` also require the `CreatorTargetId` parameter. |
| CreatorTargetId | long | The user or group ID depending on the CreatorType provided.<br><br>Queries using `CreatorTargetId` also require the `CreatorType` parameter. |
| CreatorName | string | Search by creator name. If `Enum.CreatorType` is not provided, search is for users only. |
| Cursor | string | Each search response contains a `nextPageCursor` if there is a next page and `previousPageCursor` if there is a previous page. Pass either of these values in the Cursor parameter of your next query to get the next or previous page of results. The cursor is valid if the other query parameters remain the same. |
| Genres | byte | Specifies the genre for the search. The recommended approach to filtering on genres is to match the URL of a catalog page.<br><br>`1` = TownAndCity<br>`2` = Medieval<br>`3` = SciFi<br>`4` = Fighting<br>`5` = Horror<br>`6` = Naval<br>`7` = Adventure<br>`8` = Sports<br>`9` = Comedy<br>`10` = Western<br>`11` = Military<br>`13` = Building<br>`14` = FPS<br>`15` = RPG |
| Keyword | string | Standard keyword search. |
| Limit | int | Number of results to return. Values are currently limited to 10, 28, and 30. |
| MaxPrice | int | The maximum price in Robux of items in the query. |
| MinPrice | int | The minimum price in Robux of items in the query. |
| SortAggregation | byte | `1` = PastDay<br>`3` = PastWeek<br>`4` = PastMonth<br>`5` = AllTime |
| SortType | byte | `0` = Relevance (Default)<br>`1` = Favorited<br>`2` = Sales<br>`3` = Updated<br>`4` = PriceAsc <br>`5` = PriceDesc |
| Subcategory | byte | `0` = Featured<br>`1` = All<br>`2` = Collectibles<br>`3` = Clothing<br>`4` = BodyParts<br>`5` = Gear<br>`9` = Hats<br>`10` = Faces<br>`12` = Shirts<br>`13` = TShirts<br>`14` = Pants<br>`15` = Heads<br>`19` = Accessories<br>`20` = HairAccessories<br>`21` = FaceAccessories<br>`22` = NeckAccessories<br>`23` = ShoulderAccessories<br>`24` = FrontAccessories<br>`25` = BackAccessories<br>`26` = WaistAccessories<br>`27` = AvatarAnimations<br>`37` = Bundles<br>`38` = AnimationBundles <br>`39` = EmoteAnimations<br>`40` = CommunityCreations<br>`41` = Melee<br>`42` = Ranged<br>`43` = Explosive<br>`44` = PowerUp<br>`45` = Navigation<br>`46` = Musical<br>`47` = Social<br>`48` = Building<br>`49` = Transport<br>`54` = HeadAccessories<br>`55` = ClassicTShirts<br>`56` = ClassicShirts<br>`57` = ClassicPants<br>`58` = TShirtAccessories<br>`59` = ShirtAccessories<br>`60` = PantsAccessories<br>`61` = JacketAccessories<br>`62` = SweaterAccessories<br>`63` = ShortsAccessories<br>`64` = ShoesBundles<br>`65` = DressSkirtAccessories<br>`66` = DynamicHeads |

The following URL will search for the first 10 "Gear" items in "Accessories" sorted by all-time ("SortAggregation") and relevance ("SortType") created by Roblox ("CreatorTargetId" and "CreatorType"):

`https://catalog.roblox.com/v1/search/items/details?Category=11&Subcategory=5&CreatorTargetId=1&CreatorType=User&SortType=0&SortAggregation=5&Limit=10`

### Response fields

API responses return in a JSON format. The response provides asset details in the `data` key using the following fields:

| Field | Description |
| --- | --- |
| assetType | One of the following asset type values (only returned if the item is an asset).<br><br>`2` = T-Shirt<br>`8` = Hat<br>`11` = Shirt<br>`12` = Pants<br>`17` = Head<br>`18` = Face<br>`19` = Gear<br>`25` = Arms<br>`26` = Legs<br>`27` = Torso<br>`28` = RightArm<br>`29` = LeftArm<br>`30` = LeftLeg<br>`31` = RightLeg<br>`41` = HairAccessory<br>`42` = FaceAccessory<br>`43` = NeckAccessory<br>`44` = ShoulderAccessory<br>`45` = FrontAccessory<br>`46` = BackAccessory<br>`47` = WaistAccessory<br>`48` = ClimbAnimation<br>`49` = DeathAnimation<br>`50` = FallAnimation<br>`51` = IdleAnimation<br>`52` = JumpAnimation<br>`53` = RunAnimation<br>`54` = SwimAnimation<br>`55` = WalkAnimation<br>`56` = PoseAnimation<br>`61` = EmoteAnimation |
| bundleType | The bundle type ID (only returned if the item is a bundle). Possible values are `BodyParts` and `AvatarAnimations`. |
| creatorName | The creator's name. |
| creatorTargetId | The creator's ID. |
| creatorType | The item's creator type. |
| description | The item description. |
| favoriteCount | The favorite count of an item. |
| genres | List of the item's genres. Possible values include `All`, `Tutorial`, `Scary`, `TownAndCity`, `War`, `Funny`, `Fantasy`, `Adventure`, `SciFi`, `Pirate`, `FPS`, `RPG`, `Sports`, `Ninja`, and `WildWest`. |
| id | The ID of the item. |
| itemRestrictions | List of the item's restrictions. Possible values include `ThirteenPlus`, `LimitedUnique`, `Limited`, and `Rthro`. |
| itemStatus | List of the item's status flags. Possible values include `New`, `Sale`, `XboxExclusive`, `AmazonExclusive`, `GooglePlayExclusive`, `IosExclusive`, and `SaleTimer`. |
| itemType | The item type. Possible values are `Asset` or `Bundle`. |
| lowestPrice | The lowest reseller price of the item (only returned if the item is resellable). |
| name | The item name. |
| price | The listing price of the item (current price may differ if the item is resellable). |
| priceStatus | The price status of an item that is not on sale. Possible values are `Free`, `OffSale`, or `NoResellers`. |
| purchaseCount | The purchase count of an item. |
| unitsAvailableForConsumption | The unit available for consumption of a limited unique item. |

The following is an example of expected return output for a single item:

```json
{
	"keyword": null,
	"previousPageCursor": null,
	"nextPageCursor": "2_1_c541d05046b5c1c78a5d386b5e302243",
	"data": [
    {
        "id":527373900,
        "itemType":
        "Asset",
        "assetType":42,
        "name":"Restless Souls Bandana",
        "description":"This bandana won't help you blend in with ghosts, but at least you'll be stylish.",
        "productId":41270974,
        "genres":[
          "Scary",
          "Adventure"
          ],
        "itemStatus":[],
        "itemRestrictions":[],
        "creatorType":"User",
        "creatorTargetId":1,
        "creatorName":"Roblox",
        "price":300,
        "favoriteCount":15943,
        "offSaleDeadline":null
        }
	]
}
```
