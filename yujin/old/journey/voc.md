# voc · 윤 씨 여정 단계별 고객 목소리 (11일차 3교시)

- 작성: 2026-11-26 · Claude 초안, yujin 확인 전
- 리뷰 파일: `iji/journey/reviews/yacht_reviews.csv` (김이지 님 파일, 읽기만 함) — 해외 보트 포럼 글 131건, 영어. **윤 씨의 말이 아니라 다른 나라에서 같은 일을 먼저 겪은 사람들의 글**입니다 (`stages.md` '리뷰를 읽을 때 꼭 알 것').
- 여정 단계: `yujin/journey/stages.md` 7단계
- 세는 프로그램: `yujin/journey/count_voc.py` — 돌리는 법: `journey` 폴더에서 `python -I count_voc.py ../../iji/journey/reviews/yacht_reviews.csv`
- 세 가지 항목
  - 기획 목적: 고객의 불편을 고객이 남긴 글로 근거를 세운다
  - 우선순위: 세는 것은 Python으로. 눈으로 세지 않기. 인용은 원문 그대로
  - 대상 / 제외: 이 파일의 리뷰 전부 / 같은 글이 두 번 이상 있는 리뷰(한 번만 셈), 광고 · 협찬이라고 밝힌 리뷰
- 건수는 모두 **이 파일 131건 가운데 몇 건**입니다. 고객 전체의 비율이 아닙니다.

## 1. 단계를 고르는 규칙

리뷰 본문에 아래 낱말이 하나라도 있으면 그 단계에 셉니다 (대소문자 무시). 한 리뷰가 여러 단계에 들어갈 수 있습니다. 낱말 목록은 `count_voc.py`의 `STAGES`와 같습니다.

| 단계 | 이런 말이 있으면 |
|---|---|
| 1 처음 배를 사기로 마음먹고 매물을 찾기 시작한다 | first boat · new to boating · fairly new · take the plunge · looking for a/our/my (first) boat · buy(ing) a/my/our (first) boat · purchase my |
| 2 중고 거래 앱에서 매물 글 두 개를 본다 | listings · listed for sale · advert(s) · photo(s) · picture(s) · too good to be true · private seller · for sale |
| 3 두 매물 가운데 어느 쪽 값이 맞는지 견줘 보려 한다 (팀 병목) | price(d/s) · pricing · overpriced · valuation · comparable · asking price · market value — **단, 같은 글에 bargain · lower price · price reduction/adjustment · adjustment to the selling price · renegotiat 가 있으면 뺌** (점검 뒤 값 깎기 이야기) |
| 4 사기 전에 등록 기한과 배를 댈 곳을 알아본다 | slip(s) · marina · moorage · mooring · berth · deadline |
| 5 판매자에게 물어볼 것을 들고 연락한다 | seller · owner · contact · called · phone · email · negotiat · bargain · offer · deposit · contract |
| 6 배 상태를 점검받는다 | survey · inspection · sea trial · haul(ed) out · mechanic |
| 7 돈을 보내고 배를 넘겨받아 내 이름으로 등록한다 | escrow · payment · wire · bank · money · documentation · title · registration · lien · coast guard · paperwork · closing · insurance |

- **불편**: 본문에 scam · ripped off · fraud · stolen · beware · problem · issue(s) · missed · fail · wrong · lost · frustrat · painful · nightmare · refund · disclaimer · could not · couldn't · can't · woes · trouble · lawsuit · sued · vague · expensive · worried · hidden 가운데 하나가 있으면 '불편을 말한 리뷰'로 셉니다.
- **고친 판 (2026-11-26, yujin 결정 '가')**: 첫 번째로 센 결과에서 잘못 들어간 글이 보여 규칙을 고쳤습니다 — 2단계 'listing'을 'listings'·'listed for sale'로 좁힘 (첫 판에서 "not listing what was not found"가 잡힘), 'insurance'를 4단계에서 7단계로 옮김, 3단계에서 점검 뒤 값을 깎는 글을 뺌. 첫 판 숫자: 1 · 5/4, 2 · 7/5, 3 · 8/6, 4 · 12/8, 5 · 46/31, 6 · 46/34, 7 · 46/20.

## 2. 표 (고친 규칙으로 Python이 센 값)

| 여정 단계 | 리뷰 건수 | 그 가운데 불편을 말한 건수 | 그 가운데 별점 1 · 2점 건수 | 불편 인용 (번호와 원문 그대로) |
|---|---:|---:|---|---|
| 1 처음 배를 사기로 마음먹고 매물을 찾기 시작한다 | 5 | 4 | [확인 필요] | 번호 122 "if its your first boat I would recommend having someone with you on the test drive who knows these engines and can identify any problems." |
| 2 중고 거래 앱에서 매물 글 두 개를 본다 | 6 | 4 | [확인 필요] | 번호 3 "They basically re-brand the web site and use the same pictures, etc." · 번호 6 "Exact same web site and fake ad listings, using CL as their bait system." · 번호 118 "In the meantime saw an advert but, a private seller." |
| **3 두 매물 가운데 어느 쪽 값이 맞는지 견줘 보려 한다 (팀 병목)** | **6** | **4** | [확인 필요] | **값을 견줘 보는 이야기의 인용 없음** — 아래 '사람이 읽어 본 것' 참고 |
| 4 사기 전에 등록 기한과 배를 댈 곳을 알아본다 | 5 | 2 | [확인 필요] | 번호 24 "Not so strict back then (pre 9/11) at the marinas for all official documents b/f moving in." |
| 5 판매자에게 물어볼 것을 들고 연락한다 | 46 | 31 | [확인 필요] | 번호 36 "The Florida Department of Business and Professional Regulation issues those licenses and would be the agency to contact if you think your broker is doing something shady." · 번호 40 "Most surveyors have disclaimers in their contracts/paperwork that could make it difficult to "hold them accountable", if they are not willing to admit their error(s)." · 번호 48 "In one case the owner sold the problematic boat and bought a new Nordhavn." |
| 6 배 상태를 점검받는다 | 46 | 34 | [확인 필요] | 번호 38 "Seeing a number of threads with folks talking about problems they are trying to solve that were not found during a survey, some asking about recourse on the surveyor." · 번호 40 (위와 같은 문장) · 번호 41 "A combination of expensive findings that should have been found by the hull and condition or the mechanical surveyor." |
| 7 돈을 보내고 배를 넘겨받아 내 이름으로 등록한다 | 50 | 24 | [확인 필요] | 번호 3 "There is a parade of people on these forums who have been scammed out of their money ." · 번호 9 "So a few weeks ago I got a letter from the Coast Guard; I was excited thinking it was my documentation transfer coming in BUT, it was a letter saying that there was a problem with transferring the documentation." · 번호 23 "Documentation companies check on these things and straighten out problems for you, so you can get your documentation (= title)." |

## 3. 표 아래

- **전체 리뷰 수 (분모): 131건**
- **뺀 리뷰: 0건** — 같은 글 0건, 광고 · 협찬이라고 밝힌 글 0건
- **어느 단계에도 들어가지 않은 리뷰: 44건** (131건 가운데)
- 별점: 이 파일의 5번째 칸 '별점'은 131건 모두 비어 있어 [확인 필요]입니다.
- 한 리뷰가 여러 단계에 들어가므로 단계 건수의 합은 131보다 큽니다.
- 5 · 6단계 인용에 번호 40이 둘 다 나옵니다. 'contracts'(5단계)와 'surveyors'(6단계)가 한 문장에 있어서입니다. 5단계는 낱말이 넓어(owner · contract 등) 점검 이야기까지 들어왔을 수 있습니다.

## 4. 사람이 읽어 본 것 (Claude가 매칭된 문장을 읽음, 판단은 yujin 확인 전)

- **3단계(팀 병목) 6건은 모두 '두 매물 값을 견줘 보는' 이야기가 아닙니다.** 판매자가 값을 내림(번호 60 "but I lowered price lot from 320000…"), 점검 보고서로 값 협상(66 · 72), 보관 값(108 "pending prices"), 판매자와 값 합의(118), 엔진 차이로 생기는 값 차이(131). → Python은 6건을 셌지만, **이 파일에는 윤 씨처럼 매물 값을 견줘 보려는 고객 목소리가 사실상 없습니다.** 2교시 `stages.md`에서 3단계 감정 칸이 [확인 필요]였던 것과 같습니다.
- 4단계 5건 가운데 번호 78 "underneath gear stored under "V" berths or sofas."는 'berth'가 배 안의 침대를 뜻해 잘못 들어왔습니다.

## 5. 칭찬처럼 보이지만 비꼬는 말일 수 있는 리뷰 (판단은 사람이 함)

칭찬 낱말(great · happy · love · lucky · perfect · wonderful · thanks · best · excited)과 불편 낱말이 한 문장에 함께 있는 글입니다. 3건만 나왔습니다.

| 번호 | 원문 | 뜻 (Claude가 옮김) | 불편인가 (yujin) |
|---|---|---|---|
| 8 | "The best I can tell is that they run the scam for a month or so, probably rake in a half million $ , then fold up the tent for a while." | 제가 보기엔 한 달쯤 사기를 치고 50만 달러쯤 챙긴 뒤 잠시 접는 것 같아요 | |
| 9 | "So a few weeks ago I got a letter from the Coast Guard; I was excited thinking it was my documentation transfer coming in BUT, it was a letter saying that there was a problem with transferring the documentation." | 서류가 온 줄 알고 들떴는데, 이전에 문제가 있다는 편지였어요 | |
| 63 | "You are performing your due diligence within a very compressed time period so things can get missed, but you have to try to minimize errors - that's accomplished by working with the best people you can find." | 짧은 시간에 확인하다 보니 놓치는 게 생길 수 있으니, 찾을 수 있는 최고의 사람들과 일해야 해요 | |

## 6. 원문 대조

- 이 파일의 인용은 모두 리뷰 파일의 해당 번호 본문에 글자 그대로 있음 (Claude가 프로그램으로 대조, 2026-11-26)
- 사람이 Ctrl+F로 직접 찾은 인용: [yujin이 적음]
