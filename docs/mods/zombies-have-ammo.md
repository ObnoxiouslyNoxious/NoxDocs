# **Zombies Have Ammo**

<div class="mod-hero" markdown>

![Zombies Have Ammo](../assets/img/mods/ammo.png){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

*"Is that 1–5 9mm rounds in your pocket, or are you just happy to see me?"*

**Build:** 42 | **SP/MP:** Singleplayer & Multiplayer

[:fontawesome-brands-steam-symbol: Steam Workshop](#)

</div>

## Overview

Gives zombies a configurable chance to drop loose ammunition or ammo boxes when killed, on top of vanilla drop behavior. Ammo type is chosen by a weighted rarity system with per-calibre tuning, and there's optional support for **Vanilla Firearms Expansion (VFE)** and **Guns of Marz** ammo pools. All spawning is server-side only, preventing duplication and desync in multiplayer.

## Gallery

<div class="gallery-grid" markdown>
![Zombies Have Ammo screenshot 1](../assets/img/mods/gallery/zombies-have-ammo/ZHA1.png) ![Zombies Have Ammo screenshot 2](../assets/img/mods/gallery/zombies-have-ammo/ZHA2.png) ![Zombies Have Ammo screenshot 3](../assets/img/mods/gallery/zombies-have-ammo/ZHA3.png) ![Zombies Have Ammo screenshot 4](../assets/img/mods/gallery/zombies-have-ammo/ZHA4.png) ![Zombies Have Ammo screenshot 5](../assets/img/mods/gallery/zombies-have-ammo/ZHA5.png) ![Zombies Have Ammo screenshot 6](../assets/img/mods/gallery/zombies-have-ammo/ZHA6.png) ![Zombies Have Ammo screenshot 7](../assets/img/mods/gallery/zombies-have-ammo/ZHA7.png) ![Zombies Have Ammo screenshot 8](../assets/img/mods/gallery/zombies-have-ammo/ZHA8.png) ![Zombies Have Ammo screenshot 9](../assets/img/mods/gallery/zombies-have-ammo/ZHASS1.png) ![Zombies Have Ammo screenshot 10](../assets/img/mods/gallery/zombies-have-ammo/ZHASS2.png)
</div>

## Features

- Configurable chance for zombies to drop loose ammo or ammo boxes
- Weighted rarity system — common calibres (9mm, .38, .45) appear more often than rare ones (.44 Magnum)
- Independent Enable + Weight setting for every vanilla calibre
- Optional ammo pools for Vanilla Firearms Expansion (3 calibres) and Guns of Marz (26 calibres), each independently toggleable
- Fully server-side spawning — no duplication or desync risk

## How It Works

Every zombie death triggers a single **Ammo Roll**:

1. If the roll fails, nothing drops.
2. If it succeeds, a second roll (only if Ammo Packs are enabled) decides loose rounds vs. an ammo Box — never both.
3. Ammo type is picked from a weighted rarity table across whichever pools are enabled (Vanilla, VFE, Guns of Marz).

## Installation

Subscribe to the mod on Steam Workshop and add it to your mod list — no server-side files are required:

```ini
Mods=ZombiesHaveAmmo
```

For VFE or Guns of Marz calibre support, subscribe to and load those mods as well, then enable their pools in Sandbox Settings.

## Configuration

Settings live under the **Zombies Have Ammo** tab, split into three sub-tabs.

**Zombies Have Ammo (Main)**

| Setting | Default | Range | Description |
|---|---|---|---|
| Ammo Drop Chance | 25% | 0–100% | Chance a zombie drops ammo on death |
| Minimum / Maximum Ammo | 1 / 5 | 1–100 | Range of rounds/Boxes dropped |
| Enable Ammo Packs | Off | On/Off | Allows a Box drop instead of loose rounds |
| Ammo Pack Drop Chance | 10% | 0–100% | Of the times ammo drops, chance it's a Box (not an independent roll) |
| Minimum / Maximum Ammo Packs | 1 / 1 | 1–20 | Range of Boxes dropped when a Pack drop occurs |

Each vanilla calibre (9mm, .38, .45, 12 Gauge, .30-30, 5.56, .308, .357, .44) has its own Enable toggle and Weight setting on this tab.

**VFE Ammo** — requires Vanilla Firearms Expansion Redux (`VFExpansionReduxb42`) active. Master "Enable VFE Ammo" toggle (default Off), plus per-calibre Enable/Weight for .22 LR, .223 Rem, and 7.62x39mm.

**Guns of Marz Ammo** — requires Guns of Marz active. Master "Enable Guns of Marz Ammo" toggle (default Off), plus per-calibre Enable/Weight across all 26 Guns of Marz calibres.

### Drop chances at default settings

| Step | Outcome | Chance |
|---|---|---|
| 1 | Ammo drop triggers | 25% |
| 2 (Ammo Packs off) | Loose rounds | 100% of the 25% |
| 2 (Ammo Packs on, 10%) | Box drops | 10% of the 25% → 2.5% true chance |

**Vanilla ammo pool weights** (higher = more common): 9mm 20, .38 Special 16, .45 ACP 14, 12 Gauge 14, .30-30 12, 5.56x45mm 10, .308 6, .357 Magnum 4, .44 Magnum 2.

## Compatibility

| Build |  SP | Hosted MP | Dedicated MP
|:---:|:---:|:---:|:---:|
| 42 | ✅ | ✅ | ✅ |
| 41 or earlier | ❌ | ❌ | ❌ |

Compatible with all loot mods — does not modify vanilla loot tables. Optional support for VFE and Guns of Marz. Safe to add or remove from an existing save.

## FAQ / Troubleshooting

!!! question "I enabled VFE/Guns of Marz ammo but I'm not seeing those calibres drop."

    Make sure the source mod (VFE or Guns of Marz) is actually active in your mod list, and that both the pool's master toggle and the individual calibre's Enable toggle are on.

!!! question "Will this duplicate ammo in multiplayer?"

    No — all spawning runs server-side only.

## Credits

- [Steam Workshop](#)

## Changelog

**v2.0.0**

- Added per-calibre Enable/Weight tuning for every ammo type
- Added Ammo Packs (box drops) as a configurable option
- Added Guns of Marz ammo pool support (26 calibres)
- Split Sandbox settings into three tabs (Main, VFE Ammo, Guns of Marz Ammo)
- Migrated random rolls to `newrandom()` for improved performance

See the mod's Steam Workshop page for the full version history.
