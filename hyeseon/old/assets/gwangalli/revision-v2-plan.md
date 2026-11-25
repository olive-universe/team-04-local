# Gwangalli visitor experience revision

Approved scope: user requested readable signs, correctly assembled benches, human-scale distinctive enterable cafe/boutique/hotel/claw arcade, and stronger Gwangalli attractions. Previous instruction delegates routine decisions without confirmation.

Evidence: screenshot signs show vertically flattened text. Live SurfaceGui uses FixedSize CanvasSize 800x600 on a roughly 40x3.5 stud sign; aspect mismatch confirmed. Existing facade row has solid collidable walls and no doors. Benches use world-axis coordinates despite a curved promenade.

Design: preserve beach/water/bridge/show, archive old facades, replace central frontage with four fictional shops of varied height and silhouette. Add walkable interiors and actual Seats. Use session demo tokens only, no real-money purchases. Shape public spaces from verified official Gwangalli tourism context; Google Maps dynamic content was not readable, so no surveyed or exact-business-location claims.

Tasks:
- [x] Correct SurfaceGui sizing/font and rebuild aligned bench assemblies.
- [x] Replace repeated large facades with four enterable furnished shops, different heights and distinct silhouettes.
- [x] Add cafe orders, souvenirs, claw-game play and hotel lobby/rooftop interaction with distance/cooldown/balance validation.
- [x] Add busking, SUP, photo pavilion, light walk and waterfront seating, with a richer tourist route.
- [x] Playtest readable signs, actual entry/seating/order, arcade, hotel; save after QA. Roblox version 17 saved.

Independent tasks are delegated through dispatching-parallel-agents: official-source research, geometry source, and interaction source use separate files. Root owns live Studio, landscape and integration.

## Verified in Studio

- 22 SurfaceGuis all use PixelsPerStud. Cafe, boutique and hotel title TextFits=true; Korean cafe sign visually inspected close up.
- Eight promenade bench models have aligned seat/back axes and correct local back offsets. 48 actual Seats total.
- Character walked through cafe doorway; ordered citrus tea, balance100->92, actual Tool delivered; walked onto cafe Seat and Humanoid became Seated while holding drink.
- Boutique purchase delivered shell keychain, balance92->77.
- Claw play spent5 (77->72); prize result was a win and bear reward branch ran. Individual claws have three grouped moving parts. Rest pose restored after cycle.
- Hotel check-in spent20, roof teleport settled atY68, return to lobby settledY6. Fixed overlay remaining open after teleport; retest confirmed it closed.
- Out-of-range repeat request rejected with too_far; balance remained80 in fresh hotel test.
- Six-stop count uses explicit replicated attribute after a client replication race was observed and fixed.
- iPhone17Pro landscape750x381 and portrait401x778 shop menus fit; portrait buttons329x56 and TextFits=true. Simulator reset to default. Physical phone touch remains unverified.
- Console showed only show-clock and tour-client readiness messages. Independent review found no important remaining issue; decorative piano is not described as playable.

## Map supplied during final QA

User supplied https://maps.app.goo.gl/2T2k1cF1nHgmbDiY9. Web open and browser host could not read its images, but the user's open Chrome Google Maps place page and nearby-attractions list were accessible through native accessibility. Read public place names, not reviewer identities or ratings. See research note for observations and limits.

## Follow-up visual bug and full replay

The user correctly identified a sideways held cup. Fixed upright visual geometry and added a server-timed, client-evaluated two-bone drinking pose compatible with current R15 AnimationConstraints. Standing/seated sipping, interruption, empty cup, on-foot venue traversal, claw motion, and hotel round trip were replayed and measured. See playtest-retest-2026-11-16.md. The later Google Maps photo was downloaded and viewed; 23 varied background buildings and a low continuous Terrain ridge were added behind the interactive venues. Final saved Roblox version: 22.

Reference: research/2026-11-16-gwangalli-attractions-v2.md. Exact file contracts are build_shops_v2.luau, ShopInteractions.server.luau, ShopUI.client.luau and revise_public_space_v2.luau.
