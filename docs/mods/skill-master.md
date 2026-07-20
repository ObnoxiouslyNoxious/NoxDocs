# **Skill Master**

<div class="mod-hero" markdown>

![Skill Master](../assets/img/mods/skill-master.png){ .mod-icon }

<span class="pz-tag">B42</span><span class="pz-tag">SP/MP</span>

*Reach Level 10 in a skill and stop rolling the dice on which magazine drops.*

**Build:** 42.0+ | **SP/MP:** Singleplayer & Multiplayer

[:fontawesome-brands-steam-symbol: Steam Workshop](#) · [Skill Master Unlocks spreadsheet](https://docs.google.com/spreadsheets/d/1x7gENzsmInoTABxbqRh_CR-d0xdaM6pnuaYCjVcqeM4/edit?usp=sharing)

</div>

## Overview

In vanilla Project Zomboid, many crafting recipes stay locked behind magazines or research items even after you've maxed the relevant skill. Skill Master fixes that: the moment you hit **Level 10** in any skill, every recipe tied to that skill unlocks automatically — no magazine required — and where applicable, the matching mastery trait (e.g. Herbalist, Axeman, Tailor) is granted too.

It works across **all skills**, picks up **modded recipes** automatically by scanning every loaded recipe at runtime, and applies retroactively if you load a save where you're already Level 10 in something.

## Gallery

<!--
<div class="gallery-grid" markdown>
![Caption 1](../assets/img/mods/gallery/skill-master/1.png) ![Caption 2](../assets/img/mods/gallery/skill-master/2.png)
</div>
-->

## Features

- Auto-unlocks all magazine/research-gated recipes tied to a skill at Level 10 — 86 recipes confirmed across testing
- Grants the matching mastery trait at Level 10 for 15 traits across 17 skills (e.g. Herbalist, Axeman, Tailor, Mason, Whittler, Artisan)
- Retroactive on save load — no need to re-level if you're already at 10
- Automatically includes modded recipes tied to a skill, no configuration needed
- Fully multiplayer-safe — unlocks are handled per character, server-side
- Recipe unlocks and trait grants can be toggled independently in Sandbox Settings

## Installation

Subscribe to the mod on Steam Workshop and add it to your mod list:

```ini
Mods=SkillMasterB42
```

No server-side files are required.

## Configuration

Found under the **Skill Master** tab in Custom Sandbox options.

| Option | Default | Effect |
|---|---|---|
| Enable Recipe Unlocks | On | Reaching Level 10 in a skill unlocks all magazine/research-gated recipes for that skill |
| Enable Trait Grants | On | Reaching Level 10 in a skill grants the associated character trait |

Both options are independent — recipes only, traits only, both, or neither.

## Compatibility

| Build |  SP | Hosted MP | Dedicated MP
|:---:|:---:|:---:|:---:|
| 42.0+ | ✅ | ✅ | ✅ |
| 41 or earlier | ❌ | ❌ | ❌ |

Compatible with modded recipes — Skill Master scans all loaded recipes at runtime, so anything tied to a skill by another mod is automatically included. Safe to add to an existing save. Safe to remove (already-unlocked recipes and granted traits remain on your character).

## FAQ / Troubleshooting

!!! question "Does this bypass the skill requirement for actually crafting the item?"

    No — you still need the minimum skill level to use a recipe. This only removes the "must read a magazine first" gate.

!!! question "Will other players' progress be affected when I hit Level 10?"

    No — unlocks are handled per character. Only the player who reached Level 10 is affected.

!!! question "Does it work with the 'See Not Known Recipes' sandbox setting?"

    Yes, it's compatible.

!!! question "I disabled trait grants — will already-granted traits be removed?"

    No, disabling the option only stops future grants; it doesn't revoke traits you already have.

## Credits

- [Skill Master Unlocks spreadsheet](https://docs.google.com/spreadsheets/d/1x7gENzsmInoTABxbqRh_CR-d0xdaM6pnuaYCjVcqeM4/edit?usp=sharing) — full list of every recipe and trait unlock by skill

## Changelog

See the mod's Steam Workshop page for the full version history.
