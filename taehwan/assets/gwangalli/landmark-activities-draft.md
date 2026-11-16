# Landmark experiences — approval draft

Status: 2026-11-16 Claude가 Studio에 설치·플레이 검증 후 저장(Roblox 버전 26). 공개 게시는 하지 않음. 사용자 결정: 실제 브랜드 이름 그대로 사용(수업 발표용 비공개).

## Proposed free activities

- **인생네컷:** open a nearby booth menu, choose four shots, and take four timed poses. One player uses the booth at a time for at most 19 seconds. Return to the original standing position afterward. Retake, view this visit’s latest strip, or close it. Screenshots are transient in-game images; no upload, device download, gallery save, login, or permission request. If screenshot capture is unavailable, show four frozen avatar views in a booth backdrop, explicitly marked as previews.
- **올리브영:** choose a sunscreen tube or mask packet. Receive a visible, labeled game prop in the backpack.
- **삼진어묵:** receive a visible upright wooden skewer with folded fishcake pieces.
- **민락회센터:** choose a small fish souvenir or a seafood tray prop.
- All samples are free, have a 10-second per-player/item cooldown, and allow one of each prop at a time. No health/speed effects. No currency, Robux, persistence, or modifications to existing token shops. Menus state that these are game recreations with no official brand affiliation.

## Runtime contract

- `LandmarkActivities.server.luau` → ServerScriptService; `LandmarkUI.client.luau` → StarterPlayerScripts.
- Geometry container: `workspace.GwangalliLandmarks`. Prompt parents must be BaseParts under that container, with `LandmarkKind` set to `BeautySample`, `FishCakeOrder`, `FourCuts`, or `SeafoodSample`.
- Container Vector3 attributes: `PhotoStandPosition`, `PhotoCameraPosition`, and `PhotoLookAtPosition`. Stand is the desired character pivot/root height, not floor height. Geometry proposal uses `(-390, 6, 230)`, `(-390, 8, 218)` (2026-11-16 Claude: 212→218, 사진 속 캐릭터가 너무 작아서), and `(-390, 7, 230)`.
- Server creates `ReplicatedStorage.GwangalliLandmarkRemote`. Client requests: `Gift, item`, `Photo`, `PhotoDone`. Server sends tables with `type`: `Menu`, `Message`, `PhotoStart`, `PhotoEnd`.
- Server remembers the actual prompt and expires its menu authorization after 90 seconds; each gift/start requires an alive character within 14 studs. PhotoDone only returns an active participant to the original server-recorded pivot. Death, disconnect, cancellation, and the server timeout release the booth.
- Photo capture temporarily disables movement controls, locally poses shoulders, hides Gwangalli ScreenGuis during shots, unequips tools via server, then restores joints/HUD/controls and a Custom camera with Humanoid subject. It does not anchor, seat, or alter movement statistics.
- Language follows `PlayerGui.GwangalliTour.Language`: Korean for `ko`, English fallback for all other language choices.

## Validation still required after approval

No runtime playtest or Luau compiler was available during local draft preparation. Source was inspected against the contracts above. Before publishing, test two-player booth contention, reset/cancel during capture, touch layout, R6/R15 shoulder poses, held prop orientation, and transient CaptureService image display. Capture callback timeout is 1.1 seconds per frame; a slow/unavailable callback selects the four-avatar-preview fallback. Only the latest strip is kept for the current visit; reopening a distant booth does not authorize a remote retake.

Official API reference checked through the read-only Roblox docs tool: [CaptureService.CaptureScreenshot](https://create.roblox.com/docs/reference/engine/classes/CaptureService.md). The implementation never invokes save/share APIs.

## Studio 설치·검증 기록 (2026-11-16, Claude)

Codex가 예산 한도로 멈춘 뒤 이어서 진행했다. Studio는 `%LOCALAPPDATA%\Roblox\mcp.bat`(StudioMCP)로 연결했다.

### 바꾼 점
- **위치**: Codex 좌표(올리브영 x-950, 삼진어묵 x950, 민락회센터 x1450)는 기존 맵(x -615~615) 밖의 바다·허공이었다. 가게 거리 양 끝 빈 땅(앞면 z=195)으로 옮겼다: 올리브영 x-520, 인생네컷 x-390(그대로), 삼진어묵 x360, 민락회센터 x520. 겹치는 부품 0개 확인.
- **간판**: 고정 글자 크기라 거의 안 보였다. TextScaled + UIPadding, PixelsPerStud=min(35, 95/간판높이)로 바꿨다(TextScaled는 100px가 상한).
- **네컷 자세**: R15 AnimationConstraint 관절이라 Motor6D.C0 회전이 먹히지 않아 4장이 같은 자세였다. 캐릭터 Animate의 wave/point/cheer/laugh 애니메이션을 직접 재생하고, wave 0.6초·point 0.85초에서 멈춰 팔이 올라간 순간을 찍는다. 자세 이름: 안녕!/저기 봐!/만세!/하하!.
- **촬영 화면**: 카운트다운 창이 가운데를 가려 작게(300×180) 위쪽으로 옮겼다.
- **카메라**: PhotoCameraPosition z 212→218(사진 속 캐릭터가 너무 작았다).

### 설치된 것
- `Workspace.GwangalliLandmarks` (부품 469개, 건물 4곳)
- `ServerScriptService.GwangalliLandmarkActivities`, `StarterPlayerScripts.GwangalliLandmarkUI`, `StarterPlayerScripts.GwangalliWorldLabels`

### 플레이 검증 (Studio 플레이 모드, 데스크톱)
| 항목 | 결과 |
|---|---|
| 올리브영 | E → 메뉴 열림, 마스크팩 소품 지급 |
| 삼진어묵 | E → 메뉴, 어묵꼬치 소품 지급 |
| 민락회센터 | E → 메뉴, 해산물 한상 소품 지급. 계단으로 2층(Y≈28) 걸어 올라감 |
| 인생네컷 | 촬영 자리 이동 → 4장 촬영(실제 스크린샷) → 원래 자리·Custom 카메라 복귀, 4장 모두 다른 자세 |
| 언어 | KO→EN 버튼으로 랜드마크 간판·안내 문구·기존 카페 간판이 영어로 바뀜 |
| 콘솔 | 게임 코드 오류 없음 |

### 남은 확인
- 테스트 도구의 길찾기(instance 지정)가 캐릭터를 카운터 위에 올려놓는 경우가 있었다. 테스트 중 두 번 캐릭터를 길로 옮겼다(PivotTo, 테스트 픽스처). 실제 플레이어 이동 문제인지는 확인하지 않았다.
- 메뉴 언어는 한국어/영어만(일본어·중국어는 영어로 표시). 휴대폰 터치, 2인 동시 촬영, R6 캐릭터는 미검증.
- 로컬 `TourClient.luau`에는 Studio에 있는 불꽃 물 반사 코드가 빠져 있다. Studio 쪽이 기준이며 로컬로 덮어쓰지 말 것.
- 남은 순서: ② 산책 NPC(`build_city_life.luau`는 `ServerStorage.GwangalliNPCSource` 필요, 아직 없음) ③ 맵 넓히기·사격 게임·픽셀 거리 아이디어 검사받기.

## 올리브영 v4 (밀락더마켓점 스타일) 1차 · 2026-11-16 Claude

- 사용자 결정: 실제 이름 사용, 민락회센터 옆으로 이동, 참고 사진 추가 검색.
- 자리 맞바꿈: 올리브영 x360(민락회센터 옆), 삼진어묵 x-520. 옛 v3 올리브영은 `ServerStorage.GwangalliLandmarksArchive.OliveYoung_v3`에 보관.
- 빌드: `build_oliveyoung_v4.luau` (부품 136개). 창고형 외곽(높이 36), 서쪽 빨간 벽돌 벽, 통유리 앞면, 검은 철골 트러스 5개, 후면 메자닌(바닥 world Y=19) + 벽돌 난간벽 + 검은 난간 + '올영호' 현수막 2개, 동쪽 계단 16단, 뷰티 샘플 계산대 유지.
- 조명: PointLight 밝기 0.9·범위 45, 천장 9개 + 메자닌 아래 3개 + 메자닌 위 2개. 2.2는 하얗게 날아갔다.
- 검증(플레이): 계단으로 메자닌 도착(root Y=22), 메자닌 위 이동, 계산대 E → 메뉴 열림, 콘솔 오류 없음. Roblox 버전 29 저장.
- 다음: 2차 매장 안(그물·부표 천장, 파라솔 매대, 벌크 박스, 초록 상자, 냉동고, 구역 나누기, 계산대 자리 정리).

## 올리브영 v4 2차 (매장 안) · 2026-11-16 17:46 Claude — 스크립트만 씀, 아직 실행 안 함

- 이번 세션에는 Studio 연결(StudioMCP)이 없어서 Studio에 설치·플레이 검증을 하지 못했다. 파일만 써 둠: `build_oliveyoung_v4_round2.luau` (부품 약 93개, 상한 200).
- 넣은 것: 그물 천장 + 부표 8개, 파라솔 매대 3개(샘플 병 포함), 서쪽 벽 벌크 박스 3더미, 초록 상자 5개, 메자닌 아래 냉동고 4대, 구역 간판 4개(스킨케어·선케어·마스크팩·부산 한정).
- 피한 자리: 입구 통로 x -9..9, 계산대 x 16..36 z 8..16, 계단 x 38..50 z 19..38, 메자닌 기둥, 메자닌 아래 높이 15.
- 다시 돌리면 `OliveYoung.Round2Interior` 폴더만 지우고 새로 만든다(1차 건물은 그대로).
- 다음: Studio를 연결해 명령창에서 실행 → 플레이로 입구→계산대→계단→메자닌 길이 막히지 않는지 확인 → 구역 간판 영어 전환(WorldLabels) 되는지 확인 → Roblox 저장.
