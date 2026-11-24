# 리팩토링 기록 · 2026-11-16

파일 내용은 고치지 않고 자리와 이름만 바꿨다. 지운 파일은 없다.

- CLAUDE.old.md → archive/CLAUDE.old.md
- research/2026-11-12-주제1.md → archive/2026-11-12-주제1.md
- research/2026-11-12-주제2.md → archive/2026-11-12-주제2.md
- my-assets.md → assets/my-assets.md
- team-assets.md → assets/team-assets.md
- story-assets.md → assets/story-assets.md
- data-spec.md → specs/data-spec.md
- research/2026-11-13-항만-명세.md → specs/2026-11-13-항만-명세.md
- source-map.md → research/source-map.md
- examples/before-after-pattern-a (1).md → examples/before-after-pattern-a.md

- 옮기기 전 파일 수: 55 / 옮긴 뒤 파일 수(이 기록 파일 빼고): 55
- prompts/08-fieldwork-plan.md → prompts/09-fieldwork-plan.md (2026-11-16, 08-project-analysis.md와 번호가 겹쳐서)
- fieldwork-plan.md (허심청 버전) → archive/2026-11-16-fieldwork-plan-허심청.md (2026-11-16, 맨 위 fieldwork-plan.md를 광안리 버전으로 새로 쓰면서)
- inputs/kakao-raw.txt (유용한 순·최신순이 섞인 첫 복사본) → archive/2026-11-16-kakao-raw-섞인정렬.txt (2026-11-16, 최신순으로 다시 복사한 글로 바꾸면서)

## 2026-11-17 · 지금 주제(광안리 불꽃축제)와 상관없는 옛 파일을 archive/로

파일 내용은 고치지 않고 자리만 옮겼다. 지운 파일은 없다.

- research/_check.md → archive/2026-11-16-_check.md (부전2동 노트 확인 메모)
- research/2026-11-12-bujeon-2-dong.md → archive/2026-11-12-bujeon-2-dong.md (다른 동네 주제)
- research/2026-11-12-gwangalli-eobang-festival.md → archive/2026-11-12-gwangalli-eobang-festival.md (어방축제, 불꽃축제 아님)
- research/2026-11-13-gwangalli-eobang.md → archive/2026-11-13-gwangalli-eobang.md (어방축제, 불꽃축제 아님)
- metrics.md → archive/2026-11-16-metrics-허심청.md (허심청 주제)
- emotion-keywords.md → archive/2026-11-16-emotion-keywords-허심청.md (허심청 주제)
- 옮기기 전 파일 수: 143 / 옮긴 뒤 파일 수: 143 (.git 폴더 빼고)

## 2026-11-17 · raw/ 원본을 갈래별 폴더로 (이름 규칙: collection-rules.md 맨 아래)

파일 내용은 고치지 않았다(옮기기 전후 해시 같음). raw/는 git에 올리지 않는 폴더라 커밋 기록에는 남지 않는다.

- raw/google-raw-1-번역본.txt → raw/text/2026-11-16_구글맵_광안리_외국어리뷰-번역본.txt
- raw/google-raw-2-원문.txt → raw/text/2026-11-16_구글맵_광안리_외국어리뷰-원문.txt
- 경로가 적힌 inputs/google_reviews_source.md 2줄을 새 경로로 고쳤다. 00-먼저-읽기.md는 폴더 지도를 새로 쓸 때 고친다.

## 2026-11-17 · archive/의 옛 파일을 old/로 (archive/는 정리본 자리로 바뀜)

팀 규칙(team-04-local 커밋 2e53738)에 맞춰 CLAUDE.md 폴더 규칙을 "옛 파일은 old/"로 바꿨다. 파일 내용은 고치지 않았다. 위 기록들의 `archive/…` 경로는 이제 `old/…`에서 찾는다.

- archive/ → old/ : 2026-11-12-bujeon-2-dong.md, 2026-11-12-gwangalli-eobang-festival.md, 2026-11-12-주제1.md, 2026-11-12-주제2.md, 2026-11-13-gwangalli-eobang.md, 2026-11-16-_check.md, 2026-11-16-emotion-keywords-허심청.md, 2026-11-16-fieldwork-plan-허심청.md, 2026-11-16-metrics-허심청.md, CLAUDE.old.md
- archive/ → old/ (git에 올리지 않는 파일): 2026-11-16-kakao-raw-섞인정렬.txt — .gitignore 줄도 `archive/*kakao-raw*.txt` → `old/*kakao-raw*.txt`로 바꿈
- archive/에 남은 것: files/(정리본 10개, 올리지 않음), metadata.csv

## 2026-11-17 · 주제와 상관없는 파일을 old/로 (사용자 요청 "필요없는 파일 폐기" → 규칙대로 지우지 않고 옮김)

지금 주제(광안리 불꽃축제)와 상관없는 파일을 옮겼다. 내용은 고치지 않았다. 이 파일 이름이 적힌 옛 문서(00-먼저-읽기.md, 01-깃-정리.md, 2026-11-16-회고.md, examples/demo-project-analysis.md, prompts/06-csv-spec.md, specs/2026-11-13-항만-명세.md, specs/data-spec.md)는 고치지 않았으니, 그 경로는 old/에서 찾는다.

- inputs/yeongdo_commercial_raw.csv → old/yeongdo_commercial_raw.csv (영도, 다른 동네)
- inputs/yeongdo_commercial_raw_clean.csv → old/yeongdo_commercial_raw_clean.csv (영도)
- inputs/busan_port_container_2025.csv → old/busan_port_container_2025.csv (항만, 주제와 무관)
- day4-afternoon-plan.md → old/day4-afternoon-plan.md (4일차 계획, 지난 일)
- inputs/huhshimchung_reviews_100.csv → old/huhshimchung_reviews_100.csv (옛 주제 허심청)
- research/ 오늘 노트 6개 → old/ (수업 주제와 별개: 2026-11-17-character-abilities-vfx-skills.md, -game-dev-skills.md, -roblox-skills-install.md, -roblox-skills-selection.md, -token-saving-opensource.md, -tp-studio-gaps.md). git에 올라간 적 없는 파일이라 커밋 기록에는 없음.

## 2026-11-17 · 로블록스 작업을 별도 비공개 폴더로 분리 (개인 저작물)

- assets/gwangalli/ 전체(68개) → `~/OneDrive/Documents/gwangalli-roblox/` (맨 위)
- specs/gwangan-drive-design.md, specs/gwangan-drive-plan.md → gwangalli-roblox/docs/specs/
- prompts/10-roblox-gwangalli-map.md → gwangalli-roblox/docs/prompts/
- research/2026-11-16-gwangalli-map-reference.md, -gwangalli-reference-images.md, -올리브영-모델링-참고이미지.md, research/roblox-skills-manifest.json, old/의 로블록스·스킬 노트 4개 → gwangalli-roblox/docs/research/
- .gitignore에 assets/gwangalli/ 추가. 이 폴더의 예전 커밋 기록에는 남아 있음(원격 없음, 내 PC에만).

## 2026-11-19 · 세계관을 바이블 폴더로 다시 쓰면서 옛 다섯 칸을 old/로

- brand/worldview.md → old/worldview-v1-2026-11-19.md (내용은 고치지 않음. 새 세계관은 brand/bible/, 프롬프트 prompts/12-worldview-deep.md)
- 이 파일을 가리키던 곳: .claude/skills/cheoeum-bulkkot-taehwan/SKILL.md, brand/persona.md, 00-먼저-읽기.md 9-3 → 바이블 E단계에서 고친다
- brand/one-page.md (켄지 한 사람 대상, 자리 비교표) → old/one-page-v1-2026-11-19.md. 같은 자리에 segments.md S2 대상 팀 기획서를 새로 씀 (수업 오후 과제)

## 2026-11-19 · 로블록스 자료를 다시 모두 gwangalli-roblox/로 (태환 요청)

11-17에 로블록스 작업을 뺀 뒤 llm-academy에 새로 생긴 로블록스 자료를 모두 `~/OneDrive/Documents/gwangalli-roblox/`로 옮겼다. 모두 git에 올라간 적 없는 파일이다. 복사한 뒤 원본과 같은지(diff·cmp) 확인하고 llm-academy 쪽을 지웠다.

- assets/gwangalli/vehicles/ (18개: 사이버트럭·로드스터 모델·운전 스크립트·미리보기) → gwangalli-roblox/vehicles/
- AGENTS.md (로블록스 맵 안내) → gwangalli-roblox/docs/AGENTS-from-llm-academy.md (로블록스 폴더의 AGENTS.md와 내용이 달라 이름을 바꿈)
- .mcp.json (Roblox Studio 연결 설정) → 지움. gwangalli-roblox/.mcp.json에 똑같은 파일이 있음
- 로블록스 판 brand/worldview.md·brand/one-page.md (커밋 안 된 초안) → gwangalli-roblox/docs/brand/worldview-roblox-2026-11-19.md, one-page-roblox-2026-11-19.md. llm-academy의 두 파일은 마지막 커밋 상태로 돌려 놓음
- 그대로 둔 것: "로블록스를 옮겼다"는 기록(회고·이 파일·01-깃-정리.md), inventory/scoring.md의 한 줄 언급, .claude/settings.local.json

## 2026-11-19 · 폴더 정리: 지난 주제 파일 넷을 old/로 (태환 요청)

파일 내용은 고치지 않고 자리와 이름만 바꿨다 (git mv).

- specs/2026-11-13-항만-명세.md → old/2026-11-13-항만-명세.md (항만 컨테이너 CSV 명세. CSV는 이미 old/)
- specs/data-spec.md → old/data-spec-영도.md (영도 상권 CSV 명세. 광안리 언급 0)
- transcripts/heosimcheong-maxjacqui.txt → old/heosimcheong-maxjacqui.txt (허심청 찜질방 영상 자막, `SOURCE.md` 6번이 가리킴)
- source-map.md (맨 위) → old/source-map-맨위판-2026-11-16.md (`research/source-map.md`와 이름이 같고 내용이 다름. 부전동·어방축제 줄이 있는 쪽. `fieldwork-plan.md`가 읽은 파일)
- specs/·transcripts/ 폴더는 비어서 없어짐
- 같은 날 지운 것 (git에 없던 것): 글자가 깨진 빈 폴더 `걄/`(파일 0개), main에 합쳐진 작업 공간 3개와 브랜치(final-notes-a1-b1, worldview-bible, roblox-move-log). worldview-bible·roblox-move-log 폴더는 권한 문제로 다 지워지지 않아 `.claude/worktrees/`에 남음

## 2026-11-23 · 보도자료 교체 (wellness/industry/files/)

파일 내용은 고치지 않고 자리와 이름만 바꿨다 (mv, git에 없던 파일).

- wellness/industry/files/press-1.md → old/industry-press-2026-11-23/press-1-올리브베러-성수점.md (…/press/335, `wellness/industry/summary.md`가 읽은 파일)
- wellness/industry/files/press-2.md → old/industry-press-2026-11-23/press-2-테크-콘퍼런스.md (…/press/366, `wellness/industry/summary.md`가 읽은 파일)
- 새 press-1.md = 美 5개점 추가 출점 (…/press/349), 새 press-2.md = 컬러 그라운드 홍대 (…/press/359)

## 2026-11-24 · 주제 전환: 모모스커피 단계 표를 old/로

파일 내용은 고치지 않고 자리와 이름만 바꿨다.

- valuechain/steps.md (모모스커피 단계 표) → old/valuechain-steps-momos-2026-11-24.md
- 새 valuechain/steps.md = 부산 식당 다국어 메뉴판 AI 단계 표

## 2026-11-24 · 주제 전환: 6~8일차 옛 산출물을 old/로 (태환 요청 "다 다시")

파일 내용은 고치지 않고 자리만 바꿨다 (git mv).

- inventory/ (inventory.csv·scoring.md·scoring.csv·top3.md, 불꽃축제 판) → old/fireworks-local-2026-11-24/inventory/
- brand/ (persona.md·one-page.md·segments.md·bible/ 등, 불꽃축제 판) → old/fireworks-local-2026-11-24/brand/
- CLAUDE.md 4절의 "`brand/persona.md` 맨 위 '뺀 것'"은 이제 old/fireworks-local-2026-11-24/brand/persona.md에 있다 (옛 불꽃 글에만 적용)
- 새 inventory/·brand/·story/ = 부산 식당 다국어 메뉴판 AI 판
