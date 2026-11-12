# Video

## Video

From Build 42.22 onwards, a Mod can ship its own Videos in `media/videos/`. MTF plays them as a layer in the Theme, usually full screen. This feature is somewhat experimental, relying on a game feature only recently opened up to Mods.

---

## Requirements

| Requirement | Value |
|:---|:---|
| Game Build | **42.22 or later** to play a Video a Mod ships. On older builds the fallback Image is shown instead |
| Format | A **Bink** Video (`.bik`, not `.bk2`) |
| Location | The Mod's own `media/videos/` folder, the file name **with its `.bik` extension**, no sub-folders |
| Fallback | `media/videos/<filename>.png`. Example: for `emt_loop.bik` the Image is `emt_loop.bik.png`. A still Image shown whenever the Video cannot play |
| Player Setting | **Video Effects** on. With it off, the fallback Image is drawn |

The Video Effects requirement means the Player's own setting. MTF switches Video Effects off for the vanilla Main Menu Video (see [Zomboid's Menu Video](#zomboids-menu-video)), but that does not count, as the Theme's Video still plays. MTF only does this to avoid decoding two Videos at once.

Name the file after the Theme (for example `emt_intro.bik`). The game searches every active Mod's `media/videos/` in load order and the **last Mod with that name wins**. A generic name raises the chance of a collision with a file from another Mod.

---

## Render Draw: `ctx.video.draw`

```lua
local playing = ctx.video.draw(filename, srcW, srcH, alpha, offsetX, offsetY, fit, anchor, freeze, still)
```

| Argument | Usage |
|:---|:---|
| `filename` | File name in `media/videos/` **including `.bik`** (see above). Without the extension the game finds nothing and MTF prints a warning |
| `srcW`, `srcH` | The Video's **true pixel size**. They must be correct |
| `alpha` | Opacity, `1` by default |
| `offsetX`, `offsetY` | Pixel offset of the cover-scaled Video (a drift, a pan) |
| `fit` | `"cover"` (default) fills the screen. `"cropped"` scales to the screen **width** and shows the whole Video, for a wide cropped Video (see below). A rect table `{ x, y, w, h }` draws it exactly there (see [Video with Overlay](#video-with-overlay)) |
| `anchor` | With `"cropped"`: `"center"` (default), `"top"` or `"bottom"` |
| `freeze` | `true` draws the current frame without advancing it. `ctx.video.play` uses this once the Main Menu is leaving for a game |
| `still` | The path of the fallback Graphic to draw when the Video cannot play, for example `"media/ui/emt_still.png"`. Without it, MTF uses `media/videos/<filename>.png`. A `ctx.video.play` clip sets the same thing with its own `still` field |

`ctx.video.draw` cover-scales the Video over the whole screen (unless `fit` is set) and advances it one frame per call. Call it once per frame from `render.background` or `render.foreground`. It returns `true` only while the Video itself is playing and `false` while the fallback Image is shown.

```lua
local function renderBackground(ctx)
    ctx.screen:drawRect(0, 0, ctx.width, ctx.height, 1, 0, 0, 0)
    ctx.video.draw("emt_loop.bik", 1920, 1080, 1)
end

MenuThemeFramework.registerTheme({
    id = "ExampleMenuTheme",
    name = "Example Menu Theme",
    render = { background = renderBackground },
})
```

### Cropped/Wide Videos

By default, a wide Video that is not 16:9 (such as 1920x440) is scaled up to fill the screen height and most of it is cut off at the sides. `fit = "cropped"` scales it to the screen width instead. The whole Video then shows as a band, with the rest of the screen left for the Theme to fill. Draw a Background behind it, or a foreground or overlay in front of it.

```lua
ctx.screen:drawRect(0, 0, ctx.width, ctx.height, 1, 0, 0, 0)
ctx.video.draw("emt_band.bik", 1920, 440, 1, 0, 0, "cropped", "bottom")
```

The fallback `.png` is placed the same way. In a `ctx.video.play` clip, use `fit = "cropped", anchor = "center"` as clip fields (or put them on the `opts` table for every clip).

### Video with Overlay

An overlay is a full-screen PNG with a transparent window the Video shows through. Drawn with plain cover scaling, the window and the Video drift apart as the screen shape changes. `ctx.coverFrame` keeps them locked:

```lua
-- the overlay is 1920x1080 and its window is centred on row 662 of it
local x, y, scale = ctx.coverFrame(662, 662 / 1080)   -- row 662 sits 61% of the way down the screen
local w, h = 1920 * scale, 440 * scale                -- the video at the same scale
local rect = { x = x, y = y + 662 * scale - h / 2, w = w, h = h }
ctx.video.draw("emt_band.bik", 1920, 440, 1, 0, 0, rect)
ctx.screen:drawTextureScaled(overlayTex, x, y, 1920 * scale, 1080 * scale, 1, 1, 1, 1)
```

`ctx.coverFrame(focusY, screenFocus, refW, refH)` cover-scales a reference canvas (default 1920x1080) and positions it so row `focusY` lands at `screenFocus` (a fraction of the screen height). It returns the canvas's top-left `x, y` and its `scale`. The canvas always covers the whole screen, on 16:9, ultrawide and square windows alike. With `fit` as a rect table `{ x, y, w, h }` in screen pixels, the Video (or its fallback Graphic) is drawn exactly there. A Video taller than the window has its top and bottom hidden behind the overlay.

Layer further elements on top of the Video by drawing in order, with the Video first, then the Theme's own Images, blends and text.

---

## Paired Video & Audio: `ctx.video.play`

Bink Videos cannot play their own Audio in Project Zomboid. The game's Java code never configures a `.bik`'s audio track (verified in 42.21 and 42.22). The only Audio is a normal Sound from the Theme's Sound Script. MTF lets a Theme declare a Video and Audio **pair**, the Video and a Sound from the Sound Script playing together. List the pairs in `registerTheme` and call `ctx.video.play()` once per frame.

```lua
MenuThemeFramework.registerTheme({
    id = "ExampleMenuTheme",
    name = "Example Menu Theme",
    video = {
        mode = "shuffle",
        clips = {
            { video = "emt_a.bik", sound = "EMT_VideoAudio_A", lengthMs = 20000, width = 1920, height = 1080 },
            { video = "emt_b.bik", sound = "EMT_VideoAudio_B", lengthMs = 31500, width = 1920, height = 1080 },
        },
    },
    render = {
        background = function(ctx)
            ctx.screen:drawRect(0, 0, ctx.width, ctx.height, 1, 0, 0, 0)
            ctx.video.play()
        end,
    },
})
```

| Field | Usage |
|:---|:---|
| `video` | File name in `media/videos/` including `.bik`, as for `ctx.video.draw` |
| `sound` | The Sound (from the Theme's Sound Script) that is this Video's Audio. Optional |
| `lengthMs` | How long the clip runs, in ms, before MTF ends it and starts the next clip (or this same clip again). **Needed on every clip in an `order` or `shuffle` list**, as a clip without it never ends and the list stays on it. At that moment MTF restarts the Video and its Sound together, unless `restartVideo` / `restartSound` are `false`. **Without it, the Video and Sound loop by themselves**, which can drift |
| `still` | The fallback Graphic, shown when the Video cannot play. Default: `media/videos/<video>.png` |
| `width`, `height` | The Video's true pixel size (default 1920 x 1080). MTF scales the clip, keeping its shape, until it fills the window. Anything that overflows is cropped |
| `soundVolume` | 0 to 100: this clip's own Sound level, as a percentage of the Video Sound Volume slider the Player sets (default 100) |
| `ambient` | A second Sound layered over the first, using any Sound Script name, one the Theme ships or a vanilla one (for example `"ambientOutsideDayWoods"`) |
| `ambientVolume` | 0 to 100: the ambient Sound's level, as a percentage of the Video Sound Volume slider (default 100) |
| `ambientDelay` | ms between the ambient Sound ending and playing again (0 means it loops with no gap). Not used by a Sound whose script has `loop = true` |
| `restartSound` | `false` leaves the **Sound** running when the next clip uses the same Sound. Its Sound Script entry must have `loop = true`, letting the game loop it with no stop and start (a restart leaves a split-second gap). With both `restartVideo` and `restartSound` false, nothing happens at the boundary, with the two looping by themselves until they are realigned at the next Main Menu visit |
| `restartVideo` | `false` on a clip that repeats itself. When the next clip is the same Video file, it is left running (it loops by itself) instead of being closed and reopened at the boundary. This avoids reopening the file on that frame, which can show as a one-frame glitch. The Video's own loop and the Sound's timer can then drift apart slowly until they are realigned at the next Main Menu visit. By default (`true`) the Video is closed and reopened at frame 0 |
| `fit`, `anchor` | `"cropped"` plus `"top"`, `"center"` or `"bottom"`, as for `ctx.video.draw` |

`ctx.video.play()` with no argument plays the Theme's `video` table. Passing a table (`ctx.video.play(opts)`) plays that one instead. Besides `mode`, `clips` and `fadeMs`, the table accepts `alpha`, `offsetX`, `offsetY`, `fit`, `anchor` and `cover` for every clip. `ctx.video.stop()` stops the playlist and its Sound and closes the Video. The next `ctx.video.play()` call starts it again.

### Modes

| `mode` | Playback |
|:---|:---|
| `"random"` (default) | One clip picked at random each time the Main Menu is visited, looped |
| `"order"` | The clips one after another in the order listed, then round again |
| `"shuffle"` | The clips one after another in a random order, a new order each lap, never starting a lap on the clip that just played |

`mode` can also be a function that returns one of the mode names above. This lets a Player Setting in Menu Theme Settings choose the mode:

```lua
    mode = function(ctx) return ctx.settings.get("VideoMode") end
```

Changing the Setting restarts the playlist. The `"order"` and `"shuffle"` modes need a `lengthMs` on every clip.

### Applying Fade Between Videos: `fadeMs`

With `mode = "order"` or `"shuffle"` and two or more clips that have a `lengthMs`, add `fadeMs` to the `video` table. MTF then fades through black between them:

```lua
video = { mode = "order", fadeMs = 600, clips = { ... } },
```

The Video (and the clip's Sound) fade out over the last `fadeMs` of a clip. The clip is swapped while the screen is black. MTF holds the black for `Config.VIDEO_BOUNDARY_HOLD_MS` (150 ms) and then fades the next clip in over `fadeMs`. It is not used by `random` or by a single looping clip, which have no clip change.

### Menu Cover

Each Main Menu visit, `ctx.video.play` keeps a black cover over the clip until the Video has actually started, then fades the cover away (`Config.VIDEO_COVER_FADE_MS`). This ensures the first frame of the Video is never a half-decoded one. Pass `cover = false` in the `ctx.video.play` options to turn this off.

### When Audio Is Longer than the Video

The Sound can be longer than the Video. Set the clip's `lengthMs` to the **Sound's** length. This works best when the Audio's length is an exact multiple of the Video's length. The Video loops by itself inside that time and MTF restarts the Video and the Sound together at the end. They can never drift apart by more than the one lap.

| Sound | Video | Laps |
|:---|:---|:---|
| 108 s | 27 s (810 frames at 30 fps) | 4 |
| 108 s | 36 s (1080 frames at 30 fps) | 3 |

!!! note "Work in Frames"
    The Sound's length in seconds times the frame rate must divide evenly by the Video's frame count. Measure the Sound to the millisecond, not to the second.

### MTF Boundary Behaviour

At the end of `lengthMs` (and at the start of every Main Menu visit), in one frame, MTF:

1. Closes the Video with `closeAndDestroy()`
2. Stops the pair's Sound
3. Opens the next Video (or the same one) with `getVideo`, which always starts at frame 0
4. Starts the next Sound

This keeps a looping pair from drifting and chains the clips. `ctx.video.play` returns `true` only while a Video itself is playing. With the fallback Image it returns `false`, but the Sound and the timer still run.

### Sound Script Rules for Paired Sounds

- Define them like any other Sound ([Audio](audio.md)). A clip with a `lengthMs` uses `loop = false`, as MTF restarts the Sound itself. A clip without `lengthMs`, or with `restartSound = false`, needs `loop = true`.
- The Sound fades in over `Config.VIDEO_FADE_IN_MS` (3000 ms) when the Main Menu opens. It fades in again when it resumes after a stop, but not at every clip restart.
- The Sound's volume follows its own **Video Sound Volume** slider in the Menu Theme Settings window (Audio tab), shown whenever the Theme has a clip with a Sound. `Config.VIDEO_VOLUME` sets its starting value.
- A Theme whose clips have Sounds replaces vanilla's Main Menu Music in the same way as a Theme with Music Tracks.
- MTF stops the paired Sound at the same moments it stops the Main Menu Music, when the Player starts or loads a game, joins or hosts a server, or accepts the Mods screen. The Video freezes on its current frame at the same moment (it is drawn but no longer advanced). Both start again if the Main Menu is handed back to the Player (a hosted abort, a rejected connect). MTF also cleans up a Sound left playing by a Lua reload. It keeps the handle in `Zomboid/Lua/MenuThemeFramework/<settingsFolder>/VideoSound.txt`.

!!! note "Video Requires Build 42.22+"
    The clips, timer and Sound all run on older builds, but only 42.22 can open a Video from a Mod folder. On 42.21 each clip shows its fallback `media/videos/<name>.bik.png` while its Sound plays.

---

## Video Behaviour

- The Video is opened on first use and kept open. It is closed when a world starts loading and when the Main Menu's own Background closes on the way into a game. A Lua reload, a screen change, the Menu Theme Settings window and accepting changes on the Mods screen do **not** close it.
- If the Video cannot be opened (an older build, or the file is missing or invalid), MTF remembers the failure and uses the fallback Image from then on, without retrying every frame.

---

## Zomboid's Menu Video

The Main Menu has its own background Video that the game plays under every Theme. **By default MTF stops it.** On the Title Menu it switches the game's **Video Effects** option off (this exposes the base game's Image Background) and draws a black layer where the vanilla Background was. Nothing of it shows under the Theme. MTF puts the Player's own value back before the Options screen, before any game starts and whenever the Main Menu is handed back to the Player. The Player's value is saved to a file, which stops a crash leaving the option switched off.

A Theme's own Video is not affected, as `ctx.video.draw` and `ctx.video.play` follow the Player's own Video Effects setting. The clip plays whenever the Player has it on.

A Theme that wants the vanilla Video or its Image layers to stay visible (for example a transparent overlay drawn over the vanilla Main Menu) opts out with:

```lua
menu = { disableVideoEffects = false },
```

!!! warning "Between Theme Frames"
    When a Player switches from one Menu Theme to another in the Mods screen, the vanilla Background can show for a moment before the new Theme draws its black layer. This is unfortunately a limitation of how the Lua reloading process works.

---

## Pairing Sound by Hand

This section is for Themes that need their own control over Video and Sound. A Video played through `ctx.video.draw` is **Video only**. Any Sound to go with it is started by the Theme, as below. `ctx.video.play` does all of this already.

```lua
local emitter = getSoundManager():getUIEmitter()
local handle = emitter:playSound("EMT_VideoAudio_A")   -- returns 0 on failure
```

### Starting the Sound and the Video Together

Each frame the game runs Lua `OnFETick` first, then updates the sound system, then draws the screen (including the Video frame). A Sound started from a front-end tick is therefore already mixed before that frame's Video is drawn. Started from a render callback it lands one frame late. Calling `emitter:tick()` right after `playSound` starts it inside the Theme's own call.

### Base Game Limitations

- No sync system. The base game gives Lua no Video playback position, no Video length or frame rate, no end-of-Video signal and no restart call. There is also no way to read a Sound handle's playback position.
- The game loops a Video by itself, silently. The vanilla Main Menu Video relies on this. A looping Sound and a looping Video of the same length slowly drift apart.
- Hold-and-release is not confirmed. Not calling `RenderFrame` holds the Video frame still, but the Video's internal clock may keep running. It could jump ahead on resume.

### A Timer and a Fresh Start

This is the sequence `ctx.video.play` uses.

Know how long each pair is (`lengthMs`, as Music does). With no loop signal, the reliable method is to restart **both** at the boundary:

1. When the pair's time has expired, call `tex:closeAndDestroy()`.
2. Call `getVideo` for the same file again. This is a guaranteed fresh Video from frame 0 (the cache entry is removed, the native Video is closed and the file is re-read).
3. Start the Sound again at the same moment.

### Playing One Video After Another

The same close-and-reopen sequence chains Videos. Open the next one at the boundary (opening it early may let it run ahead while it is hidden):

```lua
oldTex:closeAndDestroy()
local nextTex = getVideo("emt_b.bik", 1920, 1080)   -- nil if the name is bad
if nextTex then
    emitter:playSound("EMT_VideoAudio_B")
end
-- then call nextTex:RenderFrame() once per frame
```

!!! warning "Video Rules"
    - Always use `closeAndDestroy()`. Calling `destroy()` directly makes the next `getVideo` return the dead texture once.
    - Check `getVideo` for `nil`. A file name that fails to load is **blocked for the rest of the session** (no Lua call clears it). Check the names when the Theme loads.
    - Two Videos can be open at once, but only close the old one at the boundary.

---

## Tips

!!! note "Tips"
    - Always ship the fallback `.png` (a good first frame). It is what Players on older builds, or with Video Effects off, will see.
    - Keep the Video short and loopable. Large Videos cost memory and disk.
    - Test with Video Effects both on and off. Test on a build older than 42.22 too if the Theme supports it.

---
