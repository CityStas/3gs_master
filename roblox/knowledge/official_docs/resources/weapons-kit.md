---
title: "Weapons kit"
url: /docs/en-us/resources/weapons-kit
last_updated: 2026-10-30T19:55:56Z
description: "The Weapons Kit assists in creating competitive combat-based games."
---

# Weapons kit

Roblox offers the following prefab weapons to assist in creating competitive combat-based games. The core system features projectile-based weapons with an over-the-shoulder camera, and setting the projectile speed high enough can simulate raycasting weapons like laser guns.

> **Info:** The content of this project and documentation can be used under Roblox's [Limited Use License](/docs/en-us/resources/limited-use-license.md).

To use a prefab weapon in your game:

1. Select a weapon from below, navigating to the asset library link. _Pistol__Shotgun__Auto Rifle__Submachine Gun__Sniper Rifle__Crossbow__Grenade Launcher__Rocket Launcher__Railgun_
2. On the weapon's item page, click the **Get Model** button and confirm the transaction.
3. In Studio, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select your **Inventory** section.
4. Locate the weapon and click it to add it into the place. When prompted whether to put the tool into the starter pack, click **Yes** if you want players to start with the weapon in their backpack, or click **No** to simply place the weapon in the 3D world as a pickup.
5. If this is the **first time** bringing in a prefab weapon, move its `WeaponsSystem` folder into `Class.ServerScriptService` to serve as the unified [system folder](#system-folder-structure) for all prefab weapons in the game.

## System folder structure

The `WeaponsSystem` folder is a unified folder that contains assets, configurations, and scripts that power all prefab weapons in the game. If located in `Class.ServerScriptService`, it overrides any equivalent `WeaponsSystem` folders that may reside within individual weapons.

Within the `WeaponsSystem` folder, different aspects are controlled by the following `Class.ModuleScript|ModuleScripts`:

| Aspect | Handled primarily within... |
| --- | --- |
| Weapons functionality | <ul><li>`WeaponsSystem`</li><li>`Libraries/BaseWeapon`</li><li>`WeaponTypes/BulletWeapon`</li><li>`WeaponTypes/BowWeapon`</li></ul> |
| [Shoulder camera](#shoulder-camera) | <ul><li>`Libraries/ShoulderCamera`</li></ul> |
| [Weapons GUI](#weapons-gui) | <ul><li>`Libraries/WeaponsGui`</li><li>`Libraries/DirectionalIndicatorGuiManager`</li><li>`Libraries/DamageBillboardHandler`</li></ul> |

## Weapon structure

Prefab weapons are [tools](/docs/en-us/players/tools.md) and are named as they will appear in the player's backpack. Each weapon is structured with a similar hierarchy.

### Weapon type

The `WeaponType` `Class.StringValue` corresponds with the `Class.ModuleScript` for the weapon in the `WeaponsSystem/WeaponTypes` folder. The two base values are `BulletWeapon` and `BowWeapon`.

### Weapon model

Each weapon contains a `Class.Model` made up of one or more `Class.BasePart|BaseParts` to form the physical weapon. One of these should be set as the model's `Class.Model.PrimaryPart|PrimaryPart`.

The model also includes the following important descendants which may be parented to one of the model's `Class.BasePart|BaseParts`:

- `TipAttachment` — `Class.Attachment` whose position on the parent `Class.BasePart` determines where bullets/projectiles come out.
- `HandleAttachment` — `Class.Attachment` whose position on the parent `Class.BasePart` determines where the tool's [handle](/docs/en-us/players/tools.md#set-the-handle) is welded.
- `Fired` **optional** — `Class.Sound` that plays when the weapon is fired.
- `Reload` **optional** — `Class.Sound` that plays when the weapon is reloaded.
- Additional descendants for any [specialized options](#specialized-options).

### Configuration

The `Configuration` folder contains specific "value" types for weapon behavior. Beyond the defaults, you can add additional configuration items for [specialized options](#specialized-options) when applicable.

As follows are the base configurations and their default values:

| Item | Description | Default |
| --- | --- | --- |
| `AimTrack` | Name of the aim animation track in `Assets/Animations` of the [system folder](#system-folder-structure). | `RifleAim` |
| `AimZoomTrack` | Name of the aim zooming animation track in `Assets/Animations` of the [system folder](#system-folder-structure). | `RifleAimDownSights` |
| `AmmoCapacity` | Number of shots in each "ammo clip" before player must reload. Note that ammo is unlimited and this does not specify how much ammo a player is carrying. | `30` |
| `BulletSpeed` | Speed that bullets/projectiles travel when shot. Setting this to a very high value like `20000` simulates raycasting weapons like laser guns. | `1000` |
| `BurstShotCooldown` | Time between each shot in a burst; only matters if you set `FireMode` to `Burst`. | Value of `ShotCooldown` |
| `FiredPlaybackSpeedRange` | Amount that the pitch can vary for the `Fired` sound of the weapon. Set this to `0` to always play it at the same pitch. | `0.1` |
| `FireMode` | Choose from either `Semiautomatic` (one shot per click/tap), `Automatic` (continuous fire), or `Burst` (burst of shots equal to `NumBurstShots` on each click/tap). | `Semiautomatic` |
| `FullDamageDistance` | Maximum distance that shots will do full damage. Anything hit beyond this distance will receive less and less damage as the distance nears `ZeroDamageDistance`. | `1000` |
| `GravityFactor` | Amount that gravity should influence each bullet/projectile. For example, this value for the [Crossbow](https://create.roblox.com/store/asset/95459776337362/Crossbow) is `1` because arrows arc during flight, but this value for the [Rocket Launcher](https://create.roblox.com/store/asset/123935881517645/Rocket-Launcher) is `0` because propelled rockets travel straight. | `0` |
| `HasScope` | Set to `true` if you want to use the scope that's specified in [Weapons GUI](#weapons-gui). | `false` |
| `HitDamage` | Amount of damage each direct hit does. | `10` |
| `MaxDistance` | Maximum distance bullets/projectiles travel before disappearing. | `2000` |
| `MaxSpread` | Maximum amount of spread for the weapon. | Value of `MinSpread` |
| `MinSpread` | Minimum amount of spread for the weapon. | `0` |
| `NumBurstShots` | Number of shots per click/burst; only matters if you set `FireMode` to `Burst`. | `3` |
| `NumProjectiles` | Number of bullets/projectiles that will fire at the same time when you click/tap once. This is useful for weapons like the [Shotgun](https://create.roblox.com/store/asset/104068096273092/Shotgun) that fires multiple bullets at same time. Note that one shot will always use exactly one ammo regardless of this value. | `1` |
| `RecoilDecay` | Decay multiplier for recoil; essentially the rate at which recoil diminishes after shooting. | `0.825` |
| `RecoilDelayTime` | Waiting time after shooting/clicking before recoil is added to camera. | `0.07` |
| `RecoilMax` | Maximum recoil added for each shot. | `0.5` |
| `RecoilMin` | Minimum recoil added for each shot. | `0.05` |
| `ReloadAnimation` | Name of the reload animation track in `Assets/Animations` of the [system folder](#system-folder-structure). | `RifleReload` |
| `ShotCooldown` | Minimum waiting time between clicks. For weapons with `FireMode` of `Automatic`, this is also the time between shots while pressing the fire button or holding click. | `0.1` |
| `StartupTime` | Length of time after equipping the weapon before the player can shoot. This prevents players from firing a single shot from multiple different weapons in quick succession. | `0.2` |
| `TotalRecoilMax` | Total maximum accumulated recoil. Weapon's current recoil will never exceed this value. | `2` |
| `ZeroDamageDistance` | Anything hit at or beyond this distance will receive no damage. | `10000` |

## Specialized options

You can add/modify the following options for any weapon. These customizations require modifying either the weapon's `Class.Model`, the weapon's `Class.Configuration`, or both. Some configurations are dependent on others, such as [muzzle particles](#muzzle-particles) which require the necessary children for [projectile/hit effects and sounds](#projectilehit-effects-and-sounds).

### Bolt animations and sounds

A weapon's **bolt** is the part that moves back and forth each time it's fired.

- Descendants of the weapon's [weapon model](#weapon-model):
  - `Bolt` — `Class.BasePart` that moves when the weapon is fired.
  - `BoltMotor` — `Class.Motor6D` used to animate the bolt. Make sure to set the motor's `Class.Motor6D.Part0|Part0` to the weapon model's `Class.Model.PrimaryPart|PrimaryPart` and `Class.Motor6D.Part1|Part1` to the `Bolt` part.
  - `BoltMotorStart` — `Class.Attachment` whose position on the parent `Class.BasePart` determines where the bolt is when it's at rest.
  - `BoltMotorTarget` — `Class.Attachment` whose position on the parent `Class.BasePart` determines where the bolt animates to when shooting.
  - `BoltOpenSound` **optional** — `Class.Sound` that plays when the bolt opens.
  - `BoltCloseSound` **optional** — `Class.Sound` that plays when the bolt closes.
- Descendants of the weapon's [configuration](#configuration) folder:
  - `ActionOpenTime` **optional** — Time it takes for the bolt to animate to open position. Default is `0.025`.
  - `ActionCloseTime` **optional** — Time it takes for the bolt to animate to closed position. Default is `0.075`.

### Ejected bullet casings

Weapons can include physical bullet casings that eject upon firing and fall to the ground.

- Descendants of the weapon's [weapon model](#weapon-model):
  - `CasingEjectPoint` — `Class.Attachment` whose position on the parent `Class.BasePart` determines where you want bullet casings to pop out. Note that its orientation determines the direction that casings pop out.
- Descendants of the weapon's [configuration](#configuration) folder:
  - `CasingEffect` — Name of casing `Class.BasePart` in `Assets/Effects/Casings` of the [system folder](#system-folder-structure).
  - `CasingEjectSpeedMin` **optional** — Minimum eject speed of casings. Default is `15`.
  - `CasingEjectSpeedMax` **optional** — Maximum eject speed of casings. Default is `18`.
- Child of the casing `Class.BasePart` in `Assets/Effects/Casings` of the [system folder](#system-folder-structure):
  - `CasingHitSound` **optional** — `Class.Sound` that plays when casings hit the ground.

### Projectile/hit effects and sounds

You can configure physical projectiles for any weapon, along with `Class.Sound|Sounds`, `Class.Beam|Beams`, and `Class.ParticleEmitter|ParticleEmitters` for hit effects and other special effects.

- Descendants of the weapon's [configuration](#configuration) folder:
  - `ShotEffect` — Name of a shot effect stored within `Assets/Effects/Shots` of the [system folder](#system-folder-structure).
  - `ShouldMovePart` **optional** — Set to `true` if the weapon's `ShotEffect` should move with the projectile or `false` if not. You should only set this to `true` if there's a visible object that moves with each shot, such as an arrow or rocket. Default is `false`.
  - `BeamFadeTime` **optional** — Time it takes for `Beam0` or `Beam1` (see below) to fade after the bullet/projectile hits something. By default, no manual fade will be applied by code. Default is `0`.
  - `BeamWidth0` **optional** — Thickness of `Beam0` or `Beam1` at `Attachment0` (see below). Default is `1.5`.
  - `BeamWidth1` **optional** — Thickness of `Beam0` or `Beam1` at `Attachment1` (see below). Default is `1.8`.
  - `NumHitParticles` **optional** — Number of particles the `HitParticles` (see below) emitter will emit. Default is `3`.
  - `HitParticlesUsePartColor` **optional** — Set to `true` if you want the hit particles to be the color of the hit surface; `false` if you want hit particles to not change color. Default is `true`.
- Descendants of the specified `ShotEffect` noted in the above section:
  - `Flying` **optional** — `Class.Sound` that plays while the bullet/projectile is traveling.
  - `Beam0` **optional** — First slot for a trailing `Class.Beam` behind the bullet/projectile. Don't forget to set `Attachment0` and `Attachment1`.
  - `Beam1` **optional** — Second slot for a trailing `Class.Beam` behind the bullet/projectile. Don't forget to set `Attachment0` and `Attachment1`.
  - `Attachment0` **optional** — `Class.Attachment` whose position on the parent `Class.BasePart` determines the back of trailing beams; make sure to set `Class.Beam.Attachment0` on both `Beam0` and `Beam1` to this.
  - `Attachment1` **optional** — `Class.Attachment` whose position on the parent `Class.BasePart` determines the front of trailing beams; make sure to set `Class.Beam.Attachment1` on both `Beam0` and `Beam1` to this.
  - `TrailParticles` **optional** — `Class.ParticleEmitter` parented as a direct child of `Attachment0`; this will emit while the bullet/projectile is traveling.
  - `LeadingParticles` **optional** — `Class.ParticleEmitter` parented as a direct child of `Attachment1`; this will emit while the bullet/projectile is traveling.
  - `HitEffect` **optional** — `Class.Attachment` whose position will be set to `Class.Beam.Attachment1` of `Beam0` when the bullet/projectile hits. You must specify `Beam0` and its attachments for this to work properly.
  - `HitSound` **optional** — `Class.Sound` parented as a direct child of `HitEffect`; plays when the bullet/projectile hits.
  - `HitParticles` **optional** — `Class.Sound` parented as a direct child of `HitEffect`; emits when the bullet/projectile hits.
  - `Mesh` **optional** — `Class.SpecialMesh` that you want to appear as a physical projectile. Make sure you set `ShouldMovePart` in the weapon's configuration to `true` if you have a visible object here.

### Muzzle particles

This option emits particles from the specified `Class.ParticleEmitter` at the weapon's `TipAttachment` `Class.Attachment` when it's fired. Descendants of the weapon's [configuration](#configuration) folder include:

- `ShotEffect` — Name of a shot effect stored within `WeaponsSystem/Assets/Effects/Shots`. As a child of this shot effect, include a `Class.ParticleEmitter` asset named `MuzzleParticles`.
- `NumMuzzleParticles` **optional** — Number of muzzle particles that will be emitted. Default is `50`.

### Muzzle flashes

This option creates a `Class.Beam` flash effect when the weapon is fired.

- Descendants of the weapon's [weapon model](#weapon-model):
  - `MuzzleFlash0` — `Class.Attachment` used to specify one side of muzzle flash. Position doesn't matter.
  - `MuzzleFlash1` — `Class.Attachment` used to specify opposite side of muzzle flash. Position doesn't matter.
  - `MuzzleFlash` — `Class.Beam` for the muzzle flash effect. Make sure to set the beam's `Class.Beam.Attachment0|Attachment0` to `MuzzleFlash0` and `Class.Beam.Attachment1|Attachment1` to `MuzzleFlash1`.
- Descendants of the weapon's [configuration](#configuration) folder:
  - `MuzzleFlashTime` **optional** — Length of time muzzle flash will show for. Default is `0.03`.
  - `MuzzleFlashRotation0` **optional** — Minimum rotation of muzzle flash. Default is `Library.math.pi|-math.pi`.
  - `MuzzleFlashRotation1` **optional** — Maximum rotation of muzzle flash. Default is `Library.math.pi|math.pi`.
  - `MuzzleFlashSize0` **optional** — Minimum size of muzzle flash. Default is `1`.
  - `MuzzleFlashSize1` **optional** — Maximum size of muzzle flash. Default is `1`.

### Particle trails

This option creates a trail of varying length from the weapon to the projectile impact point. Descendants of the weapon's [configuration](#configuration) folder include:

- `TrailLength` **optional** — Length of trail behind bullet/projectile; default is `nil` which means the trail length will instead be calculated using `TrailLengthFactor`.
- `TrailLengthFactor` **optional** — If specified, the trail length will be set to this value multiplied by the distance the bullet/projectile traveled in the last frame; default is `1`. Note that this will be overridden if you include `TrailLength`.
- `ShowEntireTrailUntilHit` **optional** — Set to `true` to render the trail from the weapon tip all the way to wherever the projectile is; this will override both `TrailLength` and `TrailLengthFactor` and the trail will only disappear once the projectile hits something. Set to `false` to use one of the above two options to calculate trail length. Default is `false`.

### Hit marks

This visual addition appears on the surface where projectiles hit and is useful for arrows, bullet holes, scorch marks, etc. Descendants of the weapon's [configuration](#configuration) folder include:

- `HitMarkEffect` **optional** — Name of a `Class.Part`/`Class.MeshPart`/`Class.SpecialMesh` hit mark effect stored within `WeaponsSystem/Assets/Effects/HitMarks`. Default is `BulletHole`.
- `AlignHitMarkToNormal` **optional** — Set to `true` if the hit mark should always align flat against the surface like a bullet hole, or `false` if the hit mark should appear stuck in the surface from the direction the projectile came from (like an arrow). Default is `true`.

As noted by `HitMarkEffect` above, you can add a part/mesh within `WeaponsSystem/Assets/Effects/HitMarks` to appear as a physical projectile. For example, including an arrow `Class.MeshPart` and setting `AlignHitMarkToNormal` to `false` will make the arrow stick out of the surface from the direction you shot it. This `Class.Part`/`Class.MeshPart`/`Class.SpecialMesh` may contain the following descendants:

- `Glow` **optional** — `Class.Decal` which appears on the hit surface fully opaque, then rapidly gets more transparent, like a glowing effect on the surface that fades quickly. Useful for things like showing a glowing red mark where explosives hit.
- `BulletHole` **optional** — `Class.Decal` which appears on the hit surface fully opaque and, after 4 seconds, fades to transparent over 1 second.
- `ImpactBillboard` **optional** — `Class.BillboardGui` which displays at the hit surface, always facing towards the camera.
- `Impact` **optional** — `Class.ImageLabel` as a direct child of `ImpactBillboard`; this begins fully opaque, grows to the full size of the `ImpactBillboard` over `0.1` seconds, then shrinks to half its size and fades to full transparency over `0.1` seconds.

### Exploding projectiles

Projectiles can include an `Class.Explosion` object to damage player characters in an area around the impact point. Descendants of the weapon's [configuration](#configuration) folder include:

- `ExplodeOnImpact` **optional** — Set to `true` if you want bullets/projectiles for the weapon to explode on impact, `false` otherwise. Default is `false`.
- `BlastRadius` **optional** — `Class.Explosion.BlastRadius|BlastRadius` of explosion; default is `8`.
- `BlastPressure` **optional** — `Class.Explosion.BlastPressure|BlastPressure` of explosion; default is `10000`.
- `BlastDamage` **optional** — Damage dealt to things in the center of the explosion. Note that the explosion does less damage the farther away hit objects are from the center of the explosion. Default is `100`.

### Charging weapon

A charging weapon like the [Railgun](https://create.roblox.com/store/asset/124545474340043/Railgun) must be charged up between shots before it can fire again.

- Descendants of the weapon's [weapon model](#weapon-model):
  - `Charging` **optional** — `Class.Sound` which plays while the weapon is charging.
  - `Discharging` **optional** — `Class.Sound` which plays while the weapon is discharging, for example if you charge the weapon just partially and release the shoot button.
  - `ChargeComplete` **optional** — `Class.Sound` which plays when the weapon has reached full charge.
  - `DischargeComplete` **optional** — `Class.Sound` which plays when the weapon has completely discharged.
  - `ChargeGlow` **optional** — `Class.BasePart` which will get less transparent as the weapon charges up, such that it will be fully opaque at 100% charge.
  - `ChargeCompleteParticles` **optional** — `Class.ParticleEmitter` which emits when the weapon has finished charging. This emitter can be a child of any model `Class.BasePart` or a child of an `Class.Attachment` within the `Class.BasePart`.
  - `DischargeCompleteParticles` **optional** — `Class.ParticleEmitter` which emits when the weapon has completely discharged. This emitter can be a child of any model `Class.BasePart` or a child of an `Class.Attachment` within the `Class.BasePart`.
  - `ChargingParticles` **optional** — `Class.ParticleEmitter` which emits while the weapon is charging. You can include multiple emitters of this name and each will emit while charging. This emitter can be a child of any model `Class.BasePart` or a child of an `Class.Attachment` within the `Class.BasePart`.
- Descendants of the weapon's [configuration](#configuration) folder:
  - `ChargeRate` — Rate at which the weapon will charge. This value must be specified to indicate that the weapon uses charging.
  - `DischargeRate` **optional** — Rate at which the weapon will discharge. Default is `0` which means the weapon will not discharge at all.
  - `ChargePassively` **optional** — Set to `true` if you want the weapon to passively charge so it will shoot instantly when you click, or `false` if you want to click/touch to charge the weapon and have it fire once full charge is reached. Default is `false`.
  - `ChargingParticlesRatePerCharge` **optional** — Number of particles that will emit out of all `ChargingParticles` emitters multiplied by the current charge of the weapon. Default is `20`, meaning that if the weapon charge is at 10%, each `ChargingParticles` emitter will emit 2 particles (`20*0.1`), and if the weapon charge is at 90%, each emitter will emit 18 particles (`20*0.9`).
  - `FireDischarge` **optional** — Amount of charge the weapon will lose after firing a fully charged shot. Default is `1`.
  - `NumChargeCompleteParticles` **optional** — Number of particles the `ChargeCompleteParticles` emitter will emit once the weapon is fully charged. Default is `25`.
  - `NumDischargeCompleteParticles` **optional** — Number of particles the `DischargeCompleteParticles` emitter will emit when the weapon is completely discharged. Default is `25`.

### Bow weapon

A bow weapon like the [Crossbow](https://create.roblox.com/store/asset/95459776337362/Crossbow) can include a realistic string and arms construction, as well as a visual arrow nocked to the string.

In addition to adding model descendants, you need to apply the following:

- Make the weapon into a [charging weapon](#charging-weapon). For example, add the required `ChargeRate` within the weapon's `Class.Configuration` that specifies how fast the string is drawn. Additionally, consider adding optional descendants to the weapon's `Class.Model` such as a `Charging` sound for the string/arms being pulled back.
- Set the `WeaponType` to `BowWeapon` as indicated in [weapon structure](#weapon-structure).

Descendants of the weapon's [weapon model](#weapon-model) include:

- `LeftString` **optional** — `Class.Beam` for the visual left half of the string.
- `RightString` **optional** — `Class.Beam` for the visual right half of the string.
- `Arrow` **optional** — `Class.BasePart` for the arrow that appears when the bow is fully drawn. Note that this is only for visual appearance on the bow (the actual fired arrow will be a `ShotEffect` as outlined in [projectile/hit effects and sounds](#projectilehit-effects-and-sounds)).
- `String1` — `Class.Attachment` for the center point of the string.
- `StringLoose` — `Class.Attachment` point where `String1` should be when the bow is at rest.
- `StringTight` — `Class.Attachment` point where `String1` should be when the bow is fully drawn.
- `Arms` **optional** — `Class.Part` that just serves as an internal indicator that the bow arms will be animated. This may contain the following direct children:
  - `LeftString0` — `Class.Attachment` point where the left side of the string is attached to the bow.
  - `RightString0` — `Class.Attachment` point where the right side of the string is attached to the bow.
  - `LeftLoose` — `Class.Attachment` point where `LeftString0` should be when the bow is at rest.
  - `RightLoose` — `Class.Attachment` point where `RightString0` should be when the bow is at rest.
  - `LeftTight` — `Class.Attachment` point where `LeftString0` should be when the bow is fully drawn.
  - `RightTight` — `Class.Attachment` point where `RightString0` should be when the bow is fully drawn.
  - `Mesh` — `Class.SpecialMesh` part of the bow that will actually bend when the bow is drawn. Note that you must specify the following four `Class.Vector3Value` objects to make this animate.
    - `LooseOffset` — `Class.Vector3Value` offset of the `Class.SpecialMesh` when the bow is at rest.
    - `TightOffset` — `Class.Vector3Value` offset of the `Class.SpecialMesh` when the bow is fully drawn.
    - `LooseScale` — `Class.Vector3Value` scale of the `Class.SpecialMesh` when the bow is at rest.
    - `TightScale` — `Class.Vector3Value` scale of the `Class.SpecialMesh` when the bow is fully drawn.

## Weapons GUI

The core weapons system interfaces with this system to update the GUI based on things like spread of the gun, indicators for when you get hit or hit others, etc.

The `WeaponsSystemGui` is a `Class.ScreenGui` object in `WeaponsSystem/Assets` that is parented to `Class.PlayerGui` when the game starts. `WeaponSystemGui` has four descendants as follows:

- `ScalingElements` is a `Class.Folder` with the following descendants:
  - `DirectionalIndicators` — `Class.Folder` where all [directional indicators](#directional-indicators) are stored.
  - `Crosshair` — A `Class.Frame` containing a `Class.UIAspectRatioConstraint` and image labels for the bottom, left, right, and top elements of the crosshair.
  - `HitMarker` — A `Class.Frame` containing a `Class.UIAspectRatioConstraint` and a `HitMarkerImage` image label that appears and fades when the player successfully hits another player character.
- `LargeTouchscreen` is a `Class.Frame` containing `AimButton` and `FireButton` buttons that display on large touchscreens.
- `Scope` is a `Class.Frame` that contains the `ScopeImage` image label which shows up when zooming on a weapon with `HasScope` enabled (see [weapon structure](#weapon-structure)).
- `SmallTouchscreen` is a `Class.Frame` containing `AimButton` and `FireButton` buttons that display on small touchscreens.

### Directional indicators

Directional indicators are used to show the direction of something around the player's crosshair. For example, if someone shoots you, a red semi-circle can show up around your crosshair in the direction the shot came from. Other examples include indicators to show the direction of footsteps, indirect gunfire, or even environmental objects such as chests.

To create a new indicator, add a new `Class.Frame` in `WeaponsSystemGui/ScalingElements/DirectionalIndicators` with the following structure:

- Indicator (`Class.Frame`)
  - `Class.UIAspectRatioConstraint`
  - `Class.ImageLabel` for the directional indicator. Tweaking the rotation of the image in Studio may be required unless you upload the image so that it's facing down and there's little or no blank space around it. This image label must also contain its own `Class.UIAspectRatioConstraint`.
  - `Class.Configuration` containing optional properties to adjust:
    - `DistanceLevelFromCenter` **optional** — Number of distance levels from the center of the screen (each distance level is about `0.03` screen scale). Default is `6`.
    - `FadeTime` **optional** — Indicator fade time following its activation and the `TimeBeforeFade` time. Default is `1`.
    - `Name` **optional** — Name of the directional indicator as you want to reference it in code. Default is the name of the indicator's top-level `Class.Frame`.
    - `TimeBeforeFade` **optional** — Number of seconds that the indicator will appear for before fading. Default is `1`.
    - `TransparencyBeforeFade` **optional** — Transparency of the indicator before it starts to fade. Default is `0`.
    - `WidthLevel` **optional** — Number of width levels from center (each width level is about `0.03` screen scale). Default is the value of `DistanceLevelFromCenter`.

Once created, you can activate an indicator via the following command inside `WeaponsSystem/Libraries/WeaponsGui` where `indicatorName` is the string name of the indicator to activate and `worldPos` is the world position where the directional indicator should point:

```lua
self.DirectionalIndicatorGuiManager:ActivateDirectionalIndicator(indicatorName, worldPos)
```

> **Info:** If an indicator is activated an additional time before it has had time to fade completely, a new indicator of that type will be instantiated. This allows an unlimited number of any type of indicator to be activated at the same time.
>
> You can also activate directional indicators from outside of `WeaponsGui` by replacing `self` in the above code with the instance of `WeaponsGui` in your code. However, it's recommended that you activate it from inside `WeaponsGui` and trigger it via a `Class.RemoteEvent` or a `Class.BindableEvent`. For reference, see how `DamageIndicator` is activated within `WeaponsGui`.
### Damage billboard

The damage billboard is used to show numbers above a character's head when they are damaged. These will only show up for the player that damaged another player's character, not for spectating players.

Damage billboards are handled in `WeaponsSystem/Libraries/DamageBillboardHandler` and can be activated from any client-side code as follows, where `damage` is the amount of damage done and `adornmentPart` is the part on which to adorn the billboard, such as the victim's head:

```lua
DamageBillboardHandler:ShowDamageBillboard(damage, adornmentPart)
```

## Shoulder camera

The shoulder camera is a third-person camera that looks over the player character's right shoulder. To customize the shoulder camera, modify the variables under the `-- Configuration parameters (constants)` comment in the `ShoulderCamera.new()` function of `WeaponsSystem/Libraries/ShoulderCamera`. You can modify things such as field of view, offset from the character, walk speed while [sprinting or zooming](#sprint-and-zoom), etc.

## Sprint and zoom

By default, the weapons system adds "sprint" capability so players can sprint by holding the `Shift` key, pushing fully up on the dynamic thumbstick (mobile), or pushing fully up on the left joystick (gamepad). If you want to disable sprinting, set the value of `SprintEnabled` within `WeaponsSystem/Configuration` to `false`.

The system also reduces player speed while they're aiming/zooming, but you can disable this behavior by setting the value of `SlowZoomWalkEnabled` within `WeaponsSystem/Configuration` to `false`.
