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

## 2026-11-17 · archive/의 옛 파일을 old/로 (팀 규칙 바뀜: archive/는 정리본 자리)

팀 CLAUDE.md 규칙이 "안 쓰는 것은 내 이름 폴더의 old/로"로 바뀌어(커밋 2e53738) 옛 파일 10개를 옮겼다. 내용은 고치지 않았다(git mv). 위 기록들의 `archive/…` 경로는 이제 `old/…`에서 찾는다.

- archive/ → old/ : 2026-11-12-bujeon-2-dong.md, 2026-11-12-gwangalli-eobang-festival.md, 2026-11-12-주제1.md, 2026-11-12-주제2.md, 2026-11-13-gwangalli-eobang.md, 2026-11-16-_check.md, 2026-11-16-emotion-keywords-허심청.md, 2026-11-16-fieldwork-plan-허심청.md, 2026-11-16-metrics-허심청.md, CLAUDE.old.md
- archive/에 남은 것: metadata.csv (정리본 표)

## 2026-11-17 · 주제와 상관없는 파일을 old/로 (사용자 요청 "필요없는 파일 폐기" → 규칙대로 지우지 않고 옮김)

지금 주제(광안리 불꽃축제)와 상관없는 파일을 옮겼다. 내용은 고치지 않았다. 이 파일 이름이 적힌 옛 문서(00-먼저-읽기.md, 01-깃-정리.md, 2026-11-16-회고.md, examples/demo-project-analysis.md, prompts/06-csv-spec.md, specs/2026-11-13-항만-명세.md, specs/data-spec.md)는 고치지 않았으니, 그 경로는 old/에서 찾는다.

- inputs/yeongdo_commercial_raw.csv → old/yeongdo_commercial_raw.csv (영도, 다른 동네)
- inputs/yeongdo_commercial_raw_clean.csv → old/yeongdo_commercial_raw_clean.csv (영도)
- inputs/busan_port_container_2025.csv → old/busan_port_container_2025.csv (항만, 주제와 무관)
- day4-afternoon-plan.md → old/day4-afternoon-plan.md (4일차 계획, 지난 일)
- GitHub에서만 뺌(git rm --cached, .gitignore에 추가, 내 PC에는 그대로): inputs/google_reviews.csv, inputs/team_reviews.csv, inputs/huhshimchung_reviews_100.csv — 리뷰 글 원문이라 공개 저장소에 두지 않음. 예전 커밋 기록에는 남아 있음.
