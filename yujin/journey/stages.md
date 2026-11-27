# stages · 윤 씨 한 사람의 여정 (11일차 2교시)

> **2026-11-27 메모:** 2026-11-26 팀 방향 전환(요트 정보·매매 가이드 + 업체 광고 수익, 경매·안전결제·수수료 없음) **전에 만든 기록**입니다. 본문은 그날 그대로 두었고, 경매 · 안전결제 · 수수료 · 매입자 · 시세 추정을 기능으로 적은 부분은 지금 방향과 다릅니다. 지금 방향은 `yujin/CLAUDE.md` 6주 목표를 봅니다.

- 작성: 2026-11-26 · Claude 초안, yujin 확인 전
- 읽은 파일: 맨 위 `valuechain/map.md` (팀 병목 3단계), 맨 위 `LOCAL.md`, 맨 위 `story/storyboard.md`, 리뷰 파일 `iji/journey/reviews/yacht_reviews.csv` (김이지 님 파일, 읽기만 함)
- 세 가지 항목
  - 기획 목적: 밸류체인 맵에서 팀이 고른 병목 '3단계 · 견줄 공개 시세가 없음' 앞뒤 구간을, 고객 한 사람이 겪는 순서로 펼친다
  - 우선순위: 생각 · 감정 칸은 리뷰 글(`iji/journey/reviews/yacht_reviews.csv`)의 말로만 채우기. 없으면 [확인 필요]
  - 대상 / 제외: 요트투어를 타 보고 처음 배를 사려는 윤 씨 (`story/storyboard.md:11`) / 리뷰에 없는 감정을 지어내기, 회사 쪽 일(고객이 보지 못하는 일)
- 리뷰 건수는 세지 않았습니다. 세는 것은 3교시에 Python으로 합니다.

## 리뷰를 읽을 때 꼭 알 것

- **이 리뷰는 윤 씨의 말이 아닙니다.** 해외(주로 미국 · 영국) 보트 포럼에 보트를 사거나 판 사람들이 쓴 영어 글 131건입니다 (trawlerforum.com · forums.ybw.com · forums.sailboatowners.com · forums.iboats.com, 2016~ 글). 같은 일을 먼저 겪은 다른 나라 사람의 말을 빌려 놓은 것입니다.
- 근거 칸의 '번호'는 CSV 첫 칸 `번호`입니다 (글 안에 줄바꿈이 있어 파일 줄 번호와 다릅니다).
- 따옴표 안은 원문 그대로이고, 옆 괄호는 Claude가 옮긴 뜻입니다.
- 이 포럼 글에는 **계류장 · 마리나 이야기**(slip · marina · moorage로 찾아 0건)와 **매물 값을 견줘 보는 이야기**가 없었습니다. 그 단계는 [확인 필요]로 두었습니다.

## 여정 표

| 번호 | 여정 단계 (고객이 하는 일) (밸류체인 맵 단계) | 행동 | 생각 | 감정 | 접점 (고객이 만나는 화면 · 사람 · 장소) | 근거 |
|---:|---|---|---|---|---|---|
| 1 | 처음 배를 사기로 마음먹고 매물을 찾기 시작한다 (1 · 3) | "중고 요트 사는 법"을 검색한다 | "Does anyone have any tips to help avoid being scammed or ripped off." (사기당하거나 바가지 쓰지 않을 팁이 있을까요) | "take the plunge a purchase my first boat!" (드디어 첫 배를 사려고 해요!) | 검색 화면 · 마린딜러 웹페이지 첫 화면 | `yacht_reviews.csv` 번호 94 · `story/storyboard.md:28` "휴대폰으로 "중고 요트 사는 법"을 검색해 이 페이지를 엶" |
| 2 | 중고 거래 앱에서 마음에 드는 매물 글 두 개를 본다 (3) | 매물 글의 가격 · 사용시간 칸을 읽는다 | "looks too good to be true!" (믿기 어려울 만큼 좋아 보여요) | [확인 필요] | 중고 거래 앱 매물 글 | `yacht_reviews.csv` 번호 104 · `story/storyboard.md:29` "사용시간을 숫자로 적은 글은 0건이었어요." |
| 3 | **두 매물 가운데 어느 쪽 값이 맞는지 견줘 보려 한다 (3 · 팀 병목)** | 견줄 시세를 찾는다 | [확인 필요] | [확인 필요] | 마린딜러 웹페이지 1 · 2컷 ("이 두 배, 어느 쪽 값이 맞는지 견줘 보실 수 있으세요?") | 리뷰에 근거 없음 · `story/storyboard.md:28` "두 매물 가운데 어느 쪽 값이 맞는지 알고 싶음" (스토리보드의 설계 문장, 고객 글 아님) |
| 4 | 사기 전에 등록 기한과 배를 댈 곳을 알아본다 (4) | 기한 두 줄과 수영만 소식을 읽고 원문 링크를 연다 | [확인 필요] | [확인 필요] | 마린딜러 웹페이지 3 · 4컷 · 국가법령정보센터 · KNN 기사 | 리뷰에 근거 없음 · `story/storyboard.md:30` · `:31` |
| 5 | 판매자에게 물어볼 것 넷을 들고 연락한다 (5) | 물어볼 것 넷을 옮겨 적어 판매자에게 묻는다 | "needs the right seller, the right paperwork, and some trust from both sides" (맞는 판매자, 맞는 서류, 서로의 믿음이 필요해요) | [확인 필요] | 마린딜러 웹페이지 5컷 · 판매자 (연락 수단 [확인 필요]) | `yacht_reviews.csv` 번호 118 · `story/storyboard.md:32` "판매자에게 물어볼 것 넷" |
| 6 | 배 상태를 점검받는다 (2) | 배를 물 밖으로 꺼내 점검하고 시운전한다 | "a survey, even by the best, is not worth as much as going over the boat myself with a fine toothed comb." (최고의 검사라도 내가 꼼꼼히 훑어보는 것만 못해요) | [확인 필요] | 점검하는 사람 (서베이어 [지금 없음]) | `yacht_reviews.csv` 번호 41 · `yujin/busan_used_yacht_platform_plan.md:49` "상가 후 선체·엔진·전장 점검 + 시운전" |
| 7 | 돈을 보내고 배를 넘겨받아 내 이름으로 등록한다 (6 · 7) | 돈을 맡기거나 보내고, 변경등록을 한다 | "But they could not confirm that the checking account was an escrow account or not." (그 계좌가 에스크로 계좌인지 확인해 주지 못했어요) | "I was excited thinking it was my documentation transfer coming in BUT, it was a letter saying that there was a problem with transferring the documentation." (명의 이전 서류가 온 줄 알고 들떴는데, 이전에 문제가 있다는 편지였어요) · "which got painful getting them to actually return the money." (돈을 실제로 돌려받기까지 고생스러웠어요) | 돈을 맡는 곳 [지금 없음] · 등록 관청 [확인 필요] | `yacht_reviews.csv` 번호 29 · 번호 9 · 번호 118 |

## 표를 읽고 보이는 것

- **팀 병목(3단계)의 생각 · 감정 칸이 비었습니다.** 포럼 글에 '값을 견줘 보는' 이야기가 없었기 때문입니다. 병목인데 고객의 말이 없다는 것 자체가 확인할 거리입니다.
- 고객의 말이 몰린 곳은 **1단계(사기 걱정)와 7단계(돈 · 명의 이전)**입니다. 김태환 님 단계표가 '핵심'으로 적은 자리(사기 전 확인 · 명의이전)와 겹칩니다 (`valuechain/compare.md` 2절).

## 근거가 가장 비어 있는 단계

- 근거가 가장 비어 있는 단계: **3단계 (두 매물 가운데 어느 쪽 값이 맞는지 견줘 보기 · 팀 병목)** — 리뷰 파일이 해외 보트 포럼 글이라 매물 값을 견줘 보는 이야기가 없음 (Claude가 적음, yujin이 맡김 · 2026-11-26)
- 확인 · 원문 대조: 생각 · 감정 칸 인용 8개 모두 리뷰 파일의 해당 번호 본문에 글자 그대로 있음 (Claude가 프로그램으로 대조, 2026-11-26). 사람이 Ctrl+F로 직접 찾은 인용: 1단계 감정 칸 "take the plunge a purchase my first boat!" — yujin이 `iji/journey/reviews/yacht_reviews.csv`에서 찾음 (2026-11-26)
