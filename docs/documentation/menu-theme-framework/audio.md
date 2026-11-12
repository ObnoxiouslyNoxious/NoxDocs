# Audio

## Audio

MTF handles the playback of all Audio. The Theme supplies the Audio Files, a Sound Script and a list of Tracks. MTF defines three types of Sound:

| Type | Played by | Defined in |
|:---|:---|:---|
| **Menu Music** | MTF | `music` in `registerTheme` and the Theme's Sound Script |
| **UI Sounds** (Click, Hover, Launch) | MTF | MTF's own Sound Scripts. There is nothing to register |
| **Intro and One-Shot Sounds** | Theme | The Theme's Sound Script, with `loop = false`, or a Sound the game already has |

!!! info "Notes"
    - Audio is **Ogg Vorbis** (`.ogg`) in `media/sounds/`.
    - The Sound Script lives in `media/scripts/`, one `module Base { ... }` block with a `sound` per file.

### The Sound Script

A Music Track from GTA Menu Theme:

From `GMT_Sounds.txt`:

```text
    sound GMT_Song_IV_LoadingTheme
    {
        category = Ambient,
        master = Primary,
        loop = true,
        volume = 1.0,
        is3D = false,
        clip
        {
            file = media/sounds/GMT_Song_IV_LoadingTheme.ogg,
        }
    }
```


A one-shot intro Sound is the same shape with `loop = false`:

From `GMT_Sounds.txt`:

```text
    sound GMT_ZomboidIntroAudio
    {
        category = Ambient,
        master = Primary,
        loop = false,
        volume = 1.0,
        is3D = false,
        clip
        {
            file = media/sounds/GMT_ZomboidIntroAudio.ogg,
        }
    }
```


!!! warning "Reminder: Avoid Putting Comments in a Sound Script"
    A comment can silently stop Sounds registering. Keep Sound Scripts bare, exactly as above.

---

## Music

The `music` list in `registerTheme` holds one entry per Track. An entry is either the Sound name on its own or a table with the parts below:

```lua
music = {
    "EMT_MenuTrack_1",
    { "EMT_MenuTrack_2", "Example Music", 162000 },
},
```

The table form is `{ soundName, displayName, lengthMs, kind }`. A plain Sound name is shown as itself and has no length, making that Track loop forever.

| Field | Usage |
|:---|:---|
| `soundName` | The Sound defined in the Theme's Sound Script |
| `displayName` | Shown in the Audio tab. Plain text or a translation key. Defaults to the Sound name |
| `lengthMs` | The Track length in milliseconds. In Random mode MTF plays every Track once in a shuffled order (never the same one twice in a row) and moves on when the Track has played this long. **Without it, that Track loops forever** |
| `kind` | Optional. A free word such as `"ambient"` or `"song"`, used by `musicKindSetting` (below) |

GTA Menu Theme builds its Track list from a central Config table, keeping all Track names and lengths in one place:

From `GMT_Theme.lua`:

```lua
local tracks = {}
for n = 1, GMT_Config.MAIN_MENU_MUSIC_AVAILABLE_TRACKS do
	tracks[n] = {
		GMT_Config.MAIN_MENU_MUSIC_TRACK_SOUNDS[n],
		GMT_Config.MAIN_MENU_MUSIC_TRACK_NAMES[n] or ("Track " .. n),
		GMT_Config.MAIN_MENU_MUSIC_TRACK_LENGTHS_MS[n],
	}
end
```

From `GMT_Config.lua` (the comments between the tables are left out):

```lua
GMT_Config.MAIN_MENU_MUSIC_AVAILABLE_TRACKS = 11 -- how many GMT_Song_*.ogg files actually exist
GMT_Config.MAIN_MENU_MUSIC_TRACK_SOUNDS = {
    [1] = "GMT_Song_IV_LoadingTheme",
    [2] = "GMT_Song_IV_PauseTheme",
    [3] = "GMT_Song_SA_MainTheme",
    [4] = "GMT_Song_V_MainTheme",
    [5] = "GMT_Song_V_LoadingTheme",
    [6] = "GMT_Song_III_MainTheme",
    [7] = "GMT_Song_LCS_MainTheme",
    [8] = "GMT_Song_Vice_MainTheme",
    [9] = "GMT_Song_SA_CrashTheme",
    [10] = "GMT_Song_CW_XinShansTheme",
    [11] = "GMT_Song_V_NoHappyEndings",
}
GMT_Config.MAIN_MENU_MUSIC_TRACK_NAMES = {
    [1] = "IV - Loading Theme",
    [2] = "IV - Pause Theme",
    [3] = "SA - Main Theme",
    [4] = "V - Main Theme",
    [5] = "V - Loading Theme",
    [6] = "III - Main Theme",
    [7] = "LCS - Main Theme",
    [8] = "Vice - Main Theme",
    [9] = "SA - C.R.A.S.H Theme",
    [10] = "CW - Xin Shan's Theme",
    [11] = "V - No Happy Endings",
}
GMT_Config.MAIN_MENU_MUSIC_TRACK_LENGTHS_MS = {
    [1] = 336271, [2] = 544311, [3] = 481268, [4] = 316309, [5] = 416624,
    [6] = 331000, [7] = 245914, [8] = 316334, [9] = 240654, [10] = 239294,
    [11] = 319878,
}
```


RDR Menu Theme writes its 16 Tracks out directly in the same table form, each with the kind `"ambient"`. It also sets `musicRepeatOne` (see [Track Kinds and Repeat One](#track-kinds-and-repeat-one)):

From `RMT_Theme.lua`:

```lua
	musicRepeatOne = true,
	music = {
		{ "RMT_Ambient_Brandywine", "Brandywine", 240064, "ambient" },
		{ "RMT_Ambient_CalumetRavine", "Calumet Ravine", 170731, "ambient" },
		{ "RMT_Ambient_ChollaSprings", "Cholla Springs", 256064, "ambient" },
		{ "RMT_Ambient_Colter", "Colter", 276987, "ambient" },
		{ "RMT_Ambient_GreatPlains", "Great Plains", 241954, "ambient" },
		{ "RMT_Ambient_Grizzlies", "Grizzlies", 275968, "ambient" },
		{ "RMT_Ambient_Guarma", "Guarma", 229850, "ambient" },
		{ "RMT_Ambient_Heartlands", "Heartlands", 177295, "ambient" },
		{ "RMT_Ambient_LarnedSod", "Larned Sod", 177295, "ambient" },
		{ "RMT_Ambient_Lemoyne", "Lemoyne", 246921, "ambient" },
		{ "RMT_Ambient_Mexico", "Mexico", 284544, "ambient" },
		{ "RMT_Ambient_RattlesnakeHollow", "Rattlesnake Hollow", 228987, "ambient" },
		{ "RMT_Ambient_Roanoke", "Roanoke", 199744, "ambient" },
		{ "RMT_Ambient_ScarlettMeadows", "Scarlett Meadows", 182064, "ambient" },
		{ "RMT_Ambient_TallTrees", "Tall Trees", 234731, "ambient" },
		{ "RMT_Ambient_Wapiti", "Wapiti", 242249, "ambient" },
	},
```

### Track Kinds and Repeat One

Two optional `registerTheme` fields change how the playlist runs:

| Field | Usage |
|:---|:---|
| `musicKindSetting` | The `key` of one of the Theme's own `choice` Settings. When the Player's choice equals a Track's `kind`, Random mode plays only Tracks of that kind. Any other value (such as `"both"`) plays them all. Changing the Setting starts a fresh shuffle |
| `musicRepeatOne` | `true` stops the playlist advancing. One Track is picked each time the Main Menu is entered (at launch, or back from a game) and repeats until the Main Menu is left |

Menu Theme Template's `MTT_Theme.lua` shows `musicKindSetting` in use.

---

## MTF Audio Behaviour

- Music starts when the Main Menu first appears, fading in over `MUSIC_FADE_IN_MS`, at the Player's Music volume set in Menu Theme Settings.
- The Player can pick **Random** or force one Track in the Audio tab. A forced Track loops.
- Music stops immediately when the Player starts or loads a game, joins or hosts a server, or accepts the Mods screen.
- Accepting changes in the Mods screen reloads Lua. MTF keeps the same Track playing through the reload. It stops the Track if the Player removed the Theme. A fresh game launch always starts a new Track.
- If the Theme has at least one Track, or a Video clip with a Sound, MTF mutes Zomboid's Music and Sound Effects channels. With neither, Zomboid's Music plays untouched.

---

## Volume

| Setting | Default | Notes |
|:---|:---|:---|
| `Config.MUSIC_VOLUME` | `0.3` | Starting default only. The Player's slider takes over once the Player sets a level |
| `Config.MUSIC_FADE_IN_MS` | `3000` | Fade-in time of each Track as it starts |
| `Config.UI_SOUND_VOLUME` | `1.5` | Starting default for the click, hover and launch Sounds |
| `Config.UI_SOUND_MAX_GAIN` | `3.0` | The loudest the UI Sound slider can go. At 100%, the click, hover and launch Sounds play at this multiple of the volume recorded in the file. `3.0` is three times as loud. `UI_SOUND_VOLUME` above is on the same scale |

Put these values in a table and pass it to `registerTheme` as `config`:

From `GMT_Theme.lua`:

```lua
local mtfConfig = {
	MUSIC_VOLUME = 0.3,
	MUSIC_FADE_IN_MS = GMT_Config.MAIN_MENU_MUSIC_FADE_IN_MS,
	UI_SOUND_VOLUME = 0.5 * (MenuThemeFramework.Config.UI_SOUND_MAX_GAIN or 3.0), -- 50 percent on the Options slider (its 100% is UI_SOUND_MAX_GAIN)
	LOGO_FADE_IN_MS = GMT_Config.MENU_LOGO_FADE_IN_MS,
	LOGO_DISPLAY_HEIGHT = GMT_Config.MENU_LOGO_DISPLAY_HEIGHT,
	LAYOUT_DESIGN_ASPECT = GMT_Config.LAYOUT_DESIGN_ASPECT,
	LAYOUT_REFERENCE_WIDTH = GMT_Config.LAYOUT_REFERENCE_WIDTH,
}
```


---

## Setting a Music Delay (`holdMusic`)

With `menu = { holdMusic = true }` the first Track waits until the Theme calls `ctx.music.start()`. Use it when an intro has its own Sound and the playlist should begin after it. Calling `start()` again is harmless.

From `GMT_MainMenuSlideshow.lua`:

```lua
local function startMenuMusic(reason)
    if currentCtx then
        GMT_dprint("starting main menu music (%s)", reason)
        currentCtx.music.start()
    else
        GMT_warnOnce("no MTF ctx yet, cannot start main menu music (%s)", reason)
    end
end
```


Other Music calls:

```lua
ctx.music.start()          -- begin playback (needed only with holdMusic = true)
ctx.music.skip()           -- move to the next track
ctx.music.currentTrack()   -- the playing track's sound name, or nil
```

---

## Intro and One-Shot Sounds

The Theme's own Sounds are separate from the playlist. Play them through the UI emitter:

```lua
local emitter = getSoundManager():getUIEmitter()
local handle = emitter:playSound("EMT_LogoSound")   -- returns 0 on failure
if handle ~= 0 then emitter:setVolume(handle, 1.0) end
```

Stop one early with `emitter:stopSound(handle)`.

GTA Menu Theme does exactly this when its Logo scene ends, then starts the playlist:

From `GMT_MainMenuSlideshow.lua`:

```lua
local function finishLogoAudio(reason)
    if not state or state.logoAudioFinished then
        return
    end

    if logoAudioHandle then
        local emitter = getSoundManager():getUIEmitter()
        if emitter then
            emitter:stopSound(logoAudioHandle)
        end
    end

    logoAudioHandle = nil
    logoAudioFading = false
    state.logoAudioFinished = true
    GMT_dprint("stopped logo audio (%s)", reason)

    startMenuMusic("logo audio unloaded")
end
```

### Zomboid Sounds

A Theme does not have to ship its own Sound file. `emitter:playSound` takes the name of any Sound the game knows. A Sound Script entry from Zomboid's own files works the same way as the Theme's own, with no Sound Script or `.ogg` needed. If the game does not know the name, `playSound` returns `0`.

```lua
local emitter = getSoundManager():getUIEmitter()
local handle = emitter:playSound("ambientOutsideDayWoods")   -- a vanilla sound, returns 0 on failure
if handle ~= 0 then emitter:setVolume(handle, 0.5) end
```

The Sound's own script decides whether it ends by itself or keeps going. A Sound whose script loops runs until the Theme calls `emitter:stopSound(handle)`.

RDR Menu Theme layers vanilla ambient Sounds (birds, wind, rain and so on) under each of its Video clips. MTF plays them when a clip carries `ambient`. A Theme that uses Video does not need the emitter code itself (see [Video](video.md)). The same Sound, listed in a clip:

From `RMT_Config.lua`:

```lua
{
	video = "RMT_Menu_Brandenburg.bik", still = "media/videos/RMT_Menu_Brandenburg.bik.png", sound = "RMT_Menu_Brandenburg",
	lengthMs = 30000, soundVolume = 100, restartVideo = false, restartSound = false, width = RMT_Config.VIDEO_WIDTH, height = RMT_Config.VIDEO_HEIGHT,
	ambient = "ambientOutsideDayWoods", ambientVolume = 100, ambientDelay = 0,
},
```

---

## UI Sounds

MTF replaces the vanilla click, hover and launch Sounds on the Main Menu (`MTF_UI_HighlightMainMenuItem`, `MTF_UI_ActivateMainMenuItem`, `MTF_UI_ActivatePlayButton`). The vanilla UI Sounds play on Zomboid's Sound Effects channel, which MTF mutes. Zomboid's default Main Menu Video ambient Sound (the TV static and thunder) also plays on the Sound Effects channel. Without that channel muted, the TV static would play over the Theme's Music.

The replacement UI Sounds play automatically, including for d-pad movement.

For the Theme's own widgets:

```lua
MenuThemeFramework.playClickSound()
MenuThemeFramework.playHoverSound()
MenuThemeFramework.playLaunchSound()
```

---
