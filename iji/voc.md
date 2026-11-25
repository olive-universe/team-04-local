# 고객의 목소리(VOC) · 마린딜러 (중고 요트 거래)

- 작성: 김이지 · 2026-11-25
- 목적: 고객의 불편을 고객이 남긴 글로 근거를 세운다
- 여정 단계: `journey/stages.md` (태환 님 여정 6단계 사본, 고치지 않음)
- 세는 방법: `journey/count_voc.py`로만 센다. 눈으로 세지 않는다. 인용은 원문 그대로 옮긴다.
- 건수는 모두 "이 파일 안에서 몇 건"이다. 요트 고객 전체의 비율이 아니다.
- **리뷰 파일: `journey/reviews/yacht_reviews.csv`** (해외 보트 포럼 글 131건). 팀 저장소와 내 폴더에 중고 요트 고객 리뷰가 없어서 새로 모았다. 아래 '리뷰 파일 정보'의 한계를 먼저 읽는다.

## 단계를 고르는 규칙 (이 말이 있으면 이 단계)

- 한 리뷰에 여러 단계의 말이 있으면 그 단계마다 한 번씩 센다.
- 대소문자는 가리지 않는다.
- 한글 말은 글 안에 그 글자가 있으면 맞는다.
- 영어 말은 **낱말 전체**가 맞아야 한다(예: `broke`는 broker에서 잡히지 않음). 뒤에 s · es · ed · ing가 붙은 꼴도 같이 센다(survey → surveys, surveyed).
- 영어 말 끝에 `*`가 있으면 앞부분만 맞아도 센다(예: `inspect*` → inspection, inspector).
- 이 목록은 `count_voc.py`의 `STAGES` · `PAIN` · `AD` · `PRAISE`와 같다. 바꿀 때는 두 곳을 함께 바꾼다.

| 여정 단계 (`stages.md` 번호) | 이 말이 있으면 |
| --- | --- |
| 1 살 만한 요트 매물을 찾는다 | 매물 · 사이트 · 광고글 · 사진 · 가격문의 · 전화 문의 · 전화문의 / listing · listed · advert* · ad · photo* · picture* · broker |
| 2 매물과 판매자가 진짜인지 확인한다 | 사기 · 가짜 · 허위 · 명의 · 소유자 · 압류 · 서류 · 신분 / scam* · fake · fraud* · title · lien · owner · stolen · paperwork |
| 3 배를 직접 보고 상태를 확인한다 | 검수 · 시운전 · 점검 · 엔진 · 선체 · 누수 · 서베이 · 검사 / survey · surveyor · sea trial · seatrial · inspect* · engine · hull · leak · moisture |
| 4 가격과 조건을 확인하고 계약한다 | 계약 · 계약서 · 협상 · 네고 · 가격 조정 · 깎 / contract · offer · negotiat* · purchase agreement · bargain* |
| 5 대금 지급 방법을 확인하고 지급한다 | 송금 · 입금 · 계약금 · 잔금 · 에스크로 · 환불 · 안전결제 / deposit · escrow · funds · payment · paid · refund* · checking account |
| 6 명의를 바꾸고 배를 넘겨받는다 | 명의이전 · 명의 이전 · 변경등록 · 등록 · 인도 · 넘겨받 · 운송 · 탁송 / registration · title transfer · documentation · delivery · delivered · closing · handover |

| 판단 | 이 말이 있으면 |
| --- | --- |
| 불편을 말함 | 불편 · 문제 · 고장 · 사기 · 후회 · 손해 · 비싸 · 늦 · 안 됨 · 안됨 · 못 · 걱정 · 속았 · 환불 · 분쟁 · 다툼 / problem · issue · missed · regret* · scam* · broke · broken · leak · fail* · disappoint* · lost · nightmare · worried · concerned · frustrat* · painful · ripped off · expensive · mess · dangerous |
| 뺌: 광고·협찬이라고 밝힘 | 광고 · 협찬 · 제공받아 · 제공 받아 · 원고료 / sponsored · #ad · paid partnership · affiliate |
| 뺌: 같은 글 | 띄어쓰기·대소문자를 무시하고 글이 같으면 두 번째부터 뺌 |
| 비꼬는 말 후보 | 칭찬 말(좋 · 최고 · 감사 · 친절 · 만족 · 대단 · 훌륭 / great · thanks · awesome · love · perfect · nice · fun · good · happy)과 불편 말이 **같은 문장**에 같이 있음. 기계는 후보만 고르고, 판단은 사람이 한다 |
| 불편 인용 셋 | 그 단계에서 불편을 말한 리뷰 가운데 **연번이 앞선 셋**. 리뷰마다 불편 말이 처음 나온 문장을 원문 그대로 자름(사람이 고르지 않음) |

알아 둘 한계
- 말 맞추기 방식이라 뜻은 보지 않는다. 예: "issue"는 불편이 아니어도 잡히고, "paid off"(대출을 다 갚음)도 5단계에 들어간다.
- "광고글"은 1단계 말이면서, '광고' 때문에 그 리뷰가 광고로 빠질 수 있다. 뺀 리뷰 연번은 사람이 한 번 훑어본다.
- 규칙 첫판(2026-11-25)은 영어를 글자 조각으로 맞춰서 broke가 broker에서, ad가 had에서 잡혔다. 그래서 낱말 단위로 고쳤다 (문서 끝 '정정 기록').

## 리뷰 파일 정보

- 파일: `journey/reviews/yacht_reviews.csv` (만든 프로그램: `journey/build_reviews.py`, 옮긴 원문: `journey/reviews/raw/`)
- 칸: `연번,출처,URL,작성일,별점,원문` (UTF-8, 머리줄 = 1행). URL은 글마다 `#post-글번호`까지 붙어 있다.
- 모은 날짜: 2026-11-25 · 모은 사람: 김이지 (Claude가 Chrome 브라우저로 열어 읽음)
- 모은 곳 (스레드 7개, 모두 영어 포럼):

| raw 파일 | 스레드 | URL |
| --- | --- | --- |
| `tf-73768-p1.txt`, `tf-73768-p2.txt` | Boat issues found after the survey and deal closed (Trawler Forum) | https://www.trawlerforum.com/threads/boat-issues-found-after-the-survey-and-deal-closed.73768/ |
| `ybw-626718-p1.txt`, `ybw-626718-p2.txt` | Tips to Spot a Boat Scammer (YBW Forum) | https://forums.ybw.com/threads/tips-to-spot-a-boat-scammer.626718/ |
| `sbo-1249923039-p1.txt` | Coast Guard Red Tape Woes (Sailboat Owners Forums, 1쪽만) | https://forums.sailboatowners.com/threads/coast-guard-red-tape-woes.1249923039/ |
| `ybw-612244-p1.txt` | Escrow (YBW Forum) | https://forums.ybw.com/threads/escrow.612244/ |
| `iboats-685516-p1.txt` | Came across a BUYER BEWARE situation… (iboats) | https://forums.iboats.com/threads/came-across-a-buyer-beware-situation-wanted-to-spread-the-word.685516/ |
| `tf-73321-p1.txt` | Escrow (Trawler Forum) | https://www.trawlerforum.com/threads/escrow.73321/ |

- 모은 방법: 브라우저에서 스레드를 열고, 글마다 다른 글 인용(blockquote)을 뺀 본문만 뽑았다. 줄마다 공백을 한 칸으로 줄이고 빈 줄을 없앴다(글자는 바꾸지 않음). 브라우저에서 원문 지문(SHA-256 앞 12자리)을 계산했고, 옮긴 글을 `build_reviews.py`가 같은 방법으로 다시 계산해 맞춰 봤다. 지문이 다른 글은 CSV에 넣지 않았다.
- CSV에 넣기 전에 뺀 글 (Python이 세는 '뺀 리뷰'와 따로):
  - 1건: YBW 8757324 — 지문 불일치. 사전 뜻풀이를 붙여 넣은 글로, 눈에 안 보이는 글자가 섞여 옮길 때 달라짐
  - 1건: iboats 5135935 — 다른 사람 이름과 이메일 주소가 들어 있어 통째로 뺌(원문을 고칠 수 없어서)
- **한계 (반드시 함께 적기)**
  - 모두 영어권(미국·영국 등) 포럼 글이다. 부산·국내 요트 고객의 목소리가 아니다. 국내 글은 네이버가 브라우저에서 막혀 모으지 못했다.
  - 리뷰 사이트가 아니라 포럼이라 **별점이 없다** → 별점 칸은 모두 `[확인 필요]`.
  - 구매자 경험담 말고도 조언, 잡담, 브로커·변호사·판매자가 쓴 글이 섞여 있다. 누가 고객인지는 가려내지 않았다(사람이 판단).
  - Escrow 두 스레드의 첫 글(YBW 8494250, Trawler Forum 1246331)은 같은 사람이 두 곳에 올린 것으로 보이지만 글자가 조금 달라 '같은 글'로 빠지지 않는다. 또 이 글은 **판매자** 쪽 불편이다.
  - 스레드 7개에서 고른 글이라, 어느 단계 글이 많은지는 **스레드를 어떻게 골랐는지**를 따라간다(검수·사기·에스크로·명의 주제로 골랐음).

## 결과 (`count_voc.py`가 채움, 손으로 고치지 않음)

<!-- 결과 시작 -->
| 여정 단계 | 리뷰 건수 | 그 가운데 불편을 말한 건수 | 그 가운데 별점 1 · 2점 건수 | 불편 인용 셋 (연번 · 원문 그대로) |
| --- | --- | --- | --- | --- |
| 1 살 만한 요트 매물을 찾는다 | 28건 | 14건 | [확인 필요] (별점 없음) | 3: "I've just been reading a bit more on the several threads posted around the web about this scam."<br>6: "the scam has re-emerged as M a n t i s A u t o C o n s i g n m e n t S a l e s."<br>34: "I’m concerned that the broker has my money in his checking account and I have to wait for him to finalize all of the paperwork before he wires me the money." |
| 2 매물과 판매자가 진짜인지 확인한다 | 40건 | 23건 | [확인 필요] (별점 없음) | 1: "Looks like people, who have fallen for the scam, have been scammed out of many $10's of thousands of $$$$'s."<br>3: "I've just been reading a bit more on the several threads posted around the web about this scam."<br>4: "it seems that some/many who have been taken by this scam have found very favorable reviews by Google searching." |
| 3 배를 직접 보고 상태를 확인한다 | 52건 | 31건 | [확인 필요] (별점 없음) | 38: "Seeing a number of threads with folks talking about problems they are trying to solve that were not found during a survey, some asking about recourse on the surveyor."<br>39: "He missed a big one."<br>40: "If the issues that were missed are egregious (expensive and should be obvious to a trained surveyor), possibly contacting the accrediting body that this surveyor belongs to would be at least worth a phone call or email, and if "bad enough" contacting a marine lawyer for advice would be in order?" |
| 4 가격과 조건을 확인하고 계약한다 | 14건 | 8건 | [확인 필요] (별점 없음) | 40: "If the issues that were missed are egregious (expensive and should be obvious to a trained surveyor), possibly contacting the accrediting body that this surveyor belongs to would be at least worth a phone call or email, and if "bad enough" contacting a marine lawyer for advice would be in order?"<br>68: "I also advise Buyers not to have any expectation of a survey adjustment to the Selling Price unless really big issues are found like the generator needs a rebuild or in the case of a composite boat, the bottom is so badly blistered it needs to be peeled."<br>71: "My DeFever 44 had some issues that were not found on survey but were present at purchase." |
| 5 대금 지급 방법을 확인하고 지급한다 | 16건 | 7건 | [확인 필요] (별점 없음) | 9: "So a few weeks ago I got a letter from the Coast Guard; I was excited thinking it was my documentation transfer coming in BUT, it was a letter saying that there was a problem with transferring the documentation."<br>28: "The PO is a close family friend i've known since I was born so im not worried about if it was paid off."<br>34: "I’m concerned that the broker has my money in his checking account and I have to wait for him to finalize all of the paperwork before he wires me the money." |
| 6 명의를 바꾸고 배를 넘겨받는다 | 21건 | 4건 | [확인 필요] (별점 없음) | 9: "So a few weeks ago I got a letter from the Coast Guard; I was excited thinking it was my documentation transfer coming in BUT, it was a letter saying that there was a problem with transferring the documentation."<br>23: "Documentation companies check on these things and straighten out problems for you, so you can get your documentation (= title)."<br>70: "Most surveyors I know have this coverage and understand its importance, and in most cases the coverage is available through their professional organization, so shame on the surveyor who lost his home, there's no reason for that." |

- 전체 리뷰 수(분모): 이 파일 안에서 131건
- 뺀 리뷰: 0건 — 같은 글 두 번째 이상 0건 (연번 없음), 광고·협찬이라고 밝힘 0건 (연번 없음)
- 어느 단계에도 들어가지 않은 리뷰: 이 파일 안에서 37건 (연번 2, 13, 17, 19, 33, 52, 56, 57, 61, 62, 67, 77, 84, 85, 86, 87, 88, 89, 90, 91, 98, 99, 100, 105, 106, 107, 108, 109, 111, 112, 113, 116, 117, 119, 121, 123, 124)
- 한 리뷰가 여러 단계의 말을 담으면 그 단계마다 한 번씩 셌다. 그래서 단계별 건수를 더하면 분모보다 클 수 있다.

### 칭찬처럼 보이지만 비꼬는 말일 수 있는 리뷰 (기계가 고른 후보, 판단은 사람이)

- 58: "Survey missed bad shaft bearings - 5 out of 6 were bad. He spotted an issue with one cutlass bearing. All of this was a major repair, as we had to remove the generator to get at it. Electrical was a mess. Plumbing had a broken line behind one muffler and the other muffler was cracked and needed replacing. If there was a way to half ass a fix the PO did it.
I would hire a separate electrical and mechanical surveyor, besides a more general survey. Then have a good independent mechanic available at the haul out to give you some idea of the costs of repairing or updating issues.
Jack"
- 65: "I once considered becoming a marine surveyor and went to see my lawyer to ask his advice before taking the plunge. “ Don’t touch it with a barge pole” he advised me. “ See that pile of documents on that shelf … they’re all lawsuits directed at surveyors!” Needless to say, I followed his advice. Some time later a good friend, a marine surveyor, lost his home in a lawsuit over a survey he had done, not for the man who sued him but for a previous owner who had passed the old survey on. So yes, surveyors can be sued, despite the disclaimers, but their sins of omission need to be pretty egregious. That said, a trawler I purchased a year ago was surveyed by a pretty competent fellow who, nonetheless, missed several areas of delamination in the foc’sle lining and the house sides (glass over marine ply recently rebuilt). Fortunately I was able to replace all the foregoing myself but shudder at what it would cost if local ‘chippies’ were employed at $90 per hour plus!"
- 70: "Where to begin. First, I learned long ago, if everyone who considered starting a business made decisions based on what their attorney told them, no one would start a business. I have had the same business attorney for 17 years (he was the third one) and I don't know how I would manage without him, however, he's a rare breed (former enlisted Marine embassy guard), he understands the goal if business is to actually do business and be profitable. Most attorneys will give you the worst case scenario, and if you only listen to that, you will be paralyzed with fear and never do anything but work for someone else.
If you are a surveyor and you aren't incorporated, and insured, to protect your assets, you are truly a fool. Most surveyors I know have this coverage and understand its importance, and in most cases the coverage is available through their professional organization, so shame on the surveyor who lost his home, there's no reason for that.
In my nearly forty years in the business I can think of only a few cases where I've heard of surveyors being sued, must are judgement proof, the business has few assets, so those doing the suing move on to more lucrative targets.
Having said all that, I have encountered my share of inept, incompetent and negligent surveyors; and that behavior was what partially inspired me to start my consulting business. I managed a boat yard (after working as a marine mechanic and electrician for 7 years) and saw too may examples of folks buying brokerage vessels without being made aware of the many and often obvious flaws. I would go aboard the vessel to look it over in preparation for the work they wanted to do, fun stuff like water makers, inverters, paint and varnish, only to come away with a 25, 50 or 100k dollar estimate to fix seacocks, raw water plumbing, electrical, exhaust, and running gear issues. That news was difficult to deliver, as it was never in the budget for the new owners. When I delivered the news, the response invariably was, "But we had it surveyed and none of that was noted".
I have my bones to pick with many, but not all, hull and engine surveyors, of that there is no doubt, however, there are exceptions, smart, savvy, competent individuals who often come from the marine trades, as former mechanics, shipwrights, and engineers, who have the necessary first hand experience, and thus confidence, to thoroughly review and critique a vessel in the manner it should be reviewed for a pre-purchase survey, the one opportunity a buyer has to catch faults, flaws and defects and avoid big, expensive post sale surprises. I have nothing against those who retire from other non-marine professions, but the ones that become surveyors because they 'just want to be around boats' usually don't have, in my experience, what it takes to identify shortcomings, many of which are subtle and easily missed. Equally, surveyors, even competent ones, who are not physically fit, those who can't crawl through bilges and behind engines, are not well suited to the task."
<!-- 결과 끝 -->


## 사람이 본 한계 (Python 결과를 고치지 않고 적어 둠, 2026-11-25)

- 연번 28 "not worried": 걱정하지 **않는다**는 말인데 `worried` 때문에 5단계 불편으로 잡혔다. 말 맞추기는 '않는다'를 못 본다.
- 연번 70 "lost his home": 조사원이 소송으로 집을 잃은 이야기인데 `lost`와 `documentation`이 겹쳐 6단계 불편 인용에 들어갔다. 구매자의 명의 불편이 아니다.
- 연번 9 (Coast Guard 서류 이전 문제)는 6단계 글인데 `paid` 때문에 5단계에도 들어갔다.
- 연번 29·34 (Escrow 스레드)는 **판매자**가 돈을 못 받은 불편이다. 매수인 여정이 아니다.
- 비꼬는 말 후보는 3건만 나왔다. 셋 다 비꼼이라기보다 칭찬 말(good · fun)과 불편 말이 한 문장에 같이 있는 경우로 보이며, 판단은 사람이 한다.

## 정정 기록

| 언제 | 고치기 전 | 고친 뒤 | 까닭 |
| --- | --- | --- | --- |
| 2026-11-25 | 영어 말을 글자 조각으로 맞춤(예: `broke`, `ad `, `wire`). 결과: 1단계 50건 · 불편 41건 | 영어 말은 낱말 전체로 맞춤(뒤에 s·es·ed·ing 허용, `*`만 앞부분 맞춤). `wire` 빼고 `funds`·`paid`·`checking account` 넣음. 불편 말·단계 말 몇 개 더함. 결과: 1단계 28건 · 불편 14건 | `broke`가 broker에서, `ad`가 had·read에서 잡혀 "Our boat broker received $320,000…"가 불편 인용으로 올라옴. `wire`는 전기 배선(wiring) 글을 대금 단계로 넣을 수 있음 |
| 2026-11-25 | 비꼬는 말 후보: 칭찬 말과 불편 말이 **한 글**에 같이 있음 | **같은 문장**에 같이 있음 | 긴 글은 거의 다 두 말을 함께 담아 후보가 무의미해짐 |
