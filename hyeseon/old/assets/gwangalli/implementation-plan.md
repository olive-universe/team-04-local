# Gwangalli playable prototype implementation plan

Goal: turn the existing bridge into a walkable coastal scene with night lighting, a short repeating fireworks show and a tourist interface.

Architecture: keep the imported bridge; add separately named scenery and Terrain water; run visual effects locally from synchronized time. Store editable Luau sources alongside local assets. No data persistence or publishing in this phase.

Design approval: user approved proceeding with beach/promenade first on 2026-11-16. Continue inline in the existing Studio session. All dimensions are game design choices, not surveyed measurements. Reference source and limits are in research/2026-11-16-gwangalli-map-reference.md.

Constraints: preserve the bridge asset, do not overwrite existing user work, anchor scenery, keep spawn dry and unobstructed, bounded particle counts, cleanup transient effects, responsive multilingual UI, restore camera after photo mode.

Tasks:
- [x] 1. Build beach/promenade/cafe background as a separate model; place bridge offshore and set safe spawn. Verified by actual character navigation and screenshots.
- [x] 2. Add Terrain water and evening lighting, bridge accents and photo spots. Verified bridge visibility and dry start in play mode.
- [x] 3. Add repeating client fireworks, quality and audio toggles, show countdown, guide/language/photo UI and session stamp tour. Verified startup, mobile fit, camera recovery, bounded effects and language changes.
- [x] 4. Inspect client/server output, capture gameplay, record completed checks and remaining limitations. Saved to Roblox version 14, not published.

Review focus: character spawns dry; photo camera always exits; UI respects safe areas; late joins share show time; effects clean up and stop when quality is disabled.

Ruling: use Studio and reversible asset files directly rather than git worktrees because the deliverable is the live Studio scene and this folder is the user's artifact workspace.

Ruling: the procedural generator returned a small kiosk rather than a full environment. Preserve its source in ServerStorage.GwangalliSourceAssets; reuse the kiosk geometry and assemble the rest with build_scene.luau. The scene geometry is directly editable; it is not a surveyed reconstruction.

## Verification record

- 927 scenery BaseParts; all anchored. Existing bridge retained, center moved offshore to (0,70,-350).
- Play startup logged only `Gwangalli show clock ready` and `Gwangalli tour client ready`.
- Character started in Running state on dry pavement; navigated through all three spots; StampCount reached 3.
- Guide opened, five languages cycled with correct title and guide labels; photo restored Custom camera; timed tour restored walk mode automatically.
- OFF quality produced zero local effects during an active finale. High quality resumed effects; observed three shells and eight bursts within configured caps.
- iPhone 17 Pro: landscape viewport 750x381 and portrait 401x778; menu remained on screen. Emulator mouse clicks did not activate mobile buttons, so real touch interaction remains unverified. Desktop button interaction passed. Device simulation reset to default.
- Surf and burst assets both loaded and played in-engine. Surf TimeLength 40.224s; burst 5.0068s. Mute button set surf volume to zero. No claim of having listened to the audio.
- Fresh code review found no important bugs. Minor: rapidly toggling OFF and ON may permit a previously delayed boom after re-enabling; all nodes remain capped and expire.

## Audio sources

- Surf: ProSoundEffects, https://create.roblox.com/store/asset/9119677305
- Firework boom: adangames337, https://create.roblox.com/store/asset/130548883007767
- Both were free Creator Store audio insertions, not newly uploaded assets.

## Limits

Playable prototype only: building exteriors and shoreline proportions are approximations; no actual festival schedule, real business logos, permanent stamp storage or expansion districts. Fireworks currently include spherical, willow and ring variants with light, smoke and approximate water highlights. No public publication was performed. Real-device touch and performance still need testing.
