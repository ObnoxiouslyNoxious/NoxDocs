# Settings and Translations

## Settings and Translations

MTF draws and stores the Theme's own Player Settings, shows its Credits and reads every Player-facing string as a possible translation key.

---

## Player Settings

The Theme declares its options and MTF draws them on the DISPLAY tab of the Menu Theme Settings window. MTF stores them, keeping the Player's choices between sessions. There are three types.

```lua
settings = {
    -- tick box. default 1 = on, 0 = off
    { key = "SkipIntro", type = "bool", default = 0, label = "IGUI_EMT_SkipIntro" },

    -- dropdown. default is one of values; labels (optional) are shown instead of the raw values
    { key = "Style", type = "choice", default = "soft", values = { "soft", "hard" },
        labels = { "IGUI_EMT_Soft", "IGUI_EMT_Hard" }, label = "IGUI_EMT_Style" },

    -- slider
    { key = "Speed", type = "slider", default = 20, min = 10, max = 60, step = 2, label = "IGUI_EMT_Speed" },
},
```

| Field | Applies to | Meaning |
|:---|:---|:---|
| `key` | all | The Theme's name for the option. Unique within the Theme |
| `type` | all | `"bool"`, `"choice"` or `"slider"` |
| `default` | all | `1` or `0` for bool; one of `values` for choice; a number for slider |
| `label` | all | Row text, plain or a translation key |
| `values` | choice | The list of stored values |
| `labels` | choice | Optional display names, in the same order as `values` |
| `min`, `max`, `step` | slider | Range and increment |
| `first` | all | `true` shows this Setting at the very top of the Display tab, above MTF's own rows. Without it, the Theme's Settings come after them |

GTA Menu Theme has three Settings, a choice (the Slideshow animation), another choice (the Main Menu font) and a tick box (Skip Intro). Skip Intro is marked `first = true` to sit at the top of the tab.

From `GMT_Theme.lua`:

```lua
	settings = {
		{ key = "Transition", type = "choice", default = GMT_Config.MAIN_MENU_TRANSITION_STYLE or "slide",
			values = { "slide", "slidedown", "fade" }, labels = { "IGUI_GMT_AnimSlide", "IGUI_GMT_AnimSlideDown", "IGUI_GMT_AnimFade" },
			label = "IGUI_GMT_SlideshowAnimation" },
		{ key = "MenuFont", type = "choice", default = "barlow",
			values = { "vanilla", "inter", "barlow" },
			labels = { "IGUI_GMT_FontVanilla", "IGUI_GMT_FontInter", "IGUI_GMT_FontBarlow" },
			label = "IGUI_GMT_MenuFont" },
		{ key = "SkipIntro", type = "bool", default = 0, first = true, label = "IGUI_GMT_SkipIntro" },
	},
```


### Reading Them

Read a Setting by its declared `key`, from any callback:

```lua
if ctx.settings.getBoolean("SkipIntro") then ... end
local style = ctx.settings.get("Style")            -- "soft" or "hard"
local seconds = ctx.settings.getNumber("Speed")    -- 10..60
```

Settings are saved per Theme in `Zomboid/Lua/MenuThemeFramework/<settingsFolder>/MTF_Settings.txt` (the folder defaults to the Theme's `id`) under `<id>.<key>`. Reading is cheap. There is no need to cache a value.

Outside a callback (where there is no `ctx`), read through the store directly with the full key, as the GMT font function does:

```lua
local choice = MTF_Settings.get("GMT.MenuFont")
```

---

## The Menu Theme Settings Window

The Settings Button at the bottom left of the Main Menu opens the window. It has four tabs:

| Tab | Contents |
|:---|:---|
| **DISPLAY** | The Theme's Settings and MTF's own display rows (below) |
| **AUDIO** | Music Volume, Music Track (Random or one forced Track), UI Sound Volume and, when the Theme has a Video clip with a Sound, Video Sound Volume |
| **UI** | Show/Hide Menu Buttons, letting the Player hide any title-menu Button except Exit in every Layout |
| **CREDITS** | The Theme's `credits`, MTF's own entry, then the Theme's `creditsFooter` |

The DISPLAY tab lists, in this order:

1. The Theme's Settings marked `first = true`
2. **Slideshow Animation**, only for Themes using the built-in `backgrounds` Slideshow (not with `render.background`)
3. **Replace Main Menu Logo**, only if the Mod ships `<assetPrefix>_Menu_Logo.png`
4. **Hide Game Version**, always shown
5. The Theme's other Settings, with **Button Layout** last when the Theme offers two or more Layouts

---

## Credits

A list of headed sections for the CREDITS tab. Headers and rows are plain text or translation keys.

From `GMT_Theme.lua`:

```lua
	credits = {
		{ header = "IGUI_GMT_CreditsCreatedBy", rows = { "ObnoxiouslyNoxious" } },
		{ header = "IGUI_GMT_CreditsMusic", rows = { "IGUI_GMT_CreditsMusicRemixes" } },
		{ header = "IGUI_GMT_CreditsSpecialThanks", rows = { "RedChili - PZSurvivorStudio" } },
	},
```


`creditsFooter` takes the same shape. Its entries are shown at the very bottom of the CREDITS tab, after MTF's own entry (for a disclaimer, for example):

```lua
creditsFooter = {
    { header = "IGUI_EMT_Disclaimer", rows = { "IGUI_EMT_DisclaimerText" } },
},
```

---

## Translations

Anything shown to Players (`name`, `credits`, `creditsFooter`, `label`, `labels`, Music `displayName`, Layout `name`) can be a translation key. Put the keys in `common/media/lua/shared/Translate/EN/IG_UI.json`:

```json
{
    "IGUI_EMT_Title": "Example Menu Theme",
    "IGUI_EMT_SkipIntro": "Skip Intro Sequence"
}
```

- Prefix every key with the Theme's own Abbreviation. Keys then cannot clash with another Mod's.
- Plain text also works but cannot be translated.
- For common words such as Close, Save or Cancel, prefer the game's own translation keys. The same goes for vanilla place names. Only fall back to the Theme's own keys.

---
