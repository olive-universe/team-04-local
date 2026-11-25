# count_voc.py · 리뷰를 journey/stages.md 여정 단계로 나누어 센다
# 쓰는 법 (저장소 맨 위 폴더에서): python hyeseon/journey/count_voc.py
# 규칙은 voc.md 맨 위 '단계를 고르는 규칙'과 같다. 규칙을 고치면 둘 다 고친다.
import csv
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
REVIEW_FILE = ROOT / "yujin" / "team_reviews.csv"

# 단계: 아래 말이 리뷰에 하나라도 있으면 그 단계에 넣는다. 한 리뷰가 여러 단계에 들어갈 수 있다.
STAGES = [
    ("1. 요트를 갖고 싶어져요", ["요트", "노을", "야경", "뷰", "낭만", "마천루", "선셋", "Yachting"]),
    ("2. 중고 매물을 찾아봐요", ["예약", "인터넷", "패키지", "신청", "몰랐"]),
    ("3. 매물이 진짜인지 확인해요 (병목)", ["평점", "조작", "공지", "신뢰", "믿", "사기", "전화", "문자"]),
    ("4. 배를 직접 보러 가요", ["주차", "화장실", "안내", "어디로", "기다리", "본관", "건물", "시설", "샤워", "탈의",
                           "직원", "강사", "스텝", "친절", "운영", "지하철", "교통", "접근성", "노후", "오래된"]),
    ("5. 값을 정하고 계약해요", ["원에", "원 상당", "000원", "가격", "비용", "요금", "price", "cost", "pay"]),
    ("6. 돈을 보내고 명의를 바꿔요", ["결제", "환불", "송금", "명의", "등록"]),
    ("7. 배를 댈 곳을 찾아요", ["정박", "계류", "구청", "임대", "공공"]),
]

# 불편: 아래 말이 하나라도 있으면 '불편을 말한 리뷰'로 센다. 별점은 따로 센다.
COMPLAINT_WORDS = ["최악", "더럽", "악취", "불친절", "극혐", "비추", "아쉬", "부족", "안받", "씹", "못탐", "못봤",
                   "못탔", "무서웠", "노후", "조작", "강제", "공지는 없", "깡패", "반말", "비아냥", "poor",
                   "줄어", "제대로 안", "이딴", "타지마", "안좋", "지연"]

# 뺄 리뷰: 광고·협찬이라고 밝힌 말
AD_WORDS = ["협찬", "광고", "제공받", "원고료", "체험단"]

# 비꼼 후보: 칭찬 말이 있으면서, 별점 3점 이하이거나 말끝을 흐리는 표시가 있는 리뷰. 강한 불만 말이 있으면 뺀다 (판단은 사람이 한다)
PRAISE_WORDS = ["좋", "재밌", "재미", "훌륭", "멋", "빼어난", "행복", "최고", "감성"]
HEDGE_MARKS = ["..", "?", "하지만", "지만", "ㅋㅋ"]


# 다른 낱말 안에 들어 있어 잘못 걸리는 경우: 이 낱말을 지운 뒤 찾는다 (예: "리뷰" 안의 "뷰")
EXCEPT = {"뷰": "리뷰"}

# 비꼼 후보에서 빼는 강한 불만 말 (대놓고 불만이면 비꼼이 아니다)
STRONG_WORDS = ["최악", "극혐", "더럽", "악취", "불친절", "비추", "깡패"]


def has(text, words):
    return any(w in (text.replace(EXCEPT[w], "") if w in EXCEPT else text) for w in words)


def one_line(text):
    return " / ".join(p.strip() for p in text.splitlines() if p.strip())


def quote(text, words):
    """불편 말이 든 줄을 원문 그대로 고른다 (줄을 자르거나 고치지 않는다)."""
    lines = [p.strip() for p in text.splitlines() if p.strip()]
    hit = [p for p in lines if any(w in p for w in words)]
    return " / ".join(hit) if hit else one_line(text)


def main():
    rows = list(csv.DictReader(open(REVIEW_FILE, encoding="utf-8-sig")))
    total = len(rows)

    seen, kept, dropped = set(), [], []
    for r in rows:
        key = " ".join(r["리뷰"].split())
        if key in seen:
            dropped.append((r["연번"], "같은 글이 앞에 이미 있음"))
            continue
        seen.add(key)
        if has(r["리뷰"], AD_WORDS):
            dropped.append((r["연번"], "광고·협찬이라고 밝힘"))
            continue
        kept.append(r)

    out = []
    out.append("| 여정 단계 | 리뷰 건수 | 그 가운데 불편을 말한 건수 | 그 가운데 별점 1 · 2점 건수 | 불편 인용 셋(연번과 원문 그대로) |")
    out.append("|---|---|---|---|---|")
    no_stage = []
    stage_of = {r["연번"]: [] for r in kept}
    for name, words in STAGES:
        in_stage = [r for r in kept if has(r["리뷰"], words)]
        for r in in_stage:
            stage_of[r["연번"]].append(name)
        complaints = [r for r in in_stage if has(r["리뷰"], COMPLAINT_WORDS)]
        low = [r for r in complaints if r["별점"].strip() in ("1", "2")]
        no_star = [r for r in complaints if not r["별점"].strip()]
        low_cell = str(len(low)) + (f" (별점 없음 {len(no_star)}건 [확인 필요])" if no_star else "")
        quotes = "<br>".join(f'({r["연번"]}) "{quote(r["리뷰"], COMPLAINT_WORDS)}"'
                             for r in sorted(complaints, key=lambda r: (r["별점"], int(r["연번"])))[:3]) or "없음"
        out.append(f"| {name} | {len(in_stage)} | {len(complaints)} | {low_cell} | {quotes} |")

    no_stage = [r["연번"] for r in kept if not stage_of[r["연번"]]]
    out.append("")
    out.append(f"- 전체 리뷰 수(분모): 이 파일 안에서 {total}건")
    out.append(f"- 뺀 리뷰: {len(dropped)}건" + ("" if not dropped else " — " + ", ".join(f"{n}번({why})" for n, why in dropped)))
    out.append(f"- 센 리뷰: {len(kept)}건")
    out.append(f"- 어느 단계에도 들어가지 않은 리뷰: {len(no_stage)}건 (연번 {', '.join(no_stage) or '없음'})")
    multi = [n for n, s in stage_of.items() if len(s) >= 2]
    out.append(f"- 두 단계 이상에 들어간 리뷰: {len(multi)}건 (그래서 단계별 건수를 더하면 센 리뷰 수보다 크다)")
    all_complaints = [r for r in kept if has(r["리뷰"], COMPLAINT_WORDS)]
    out.append(f"- 불편을 말한 리뷰(단계와 상관없이): {len(all_complaints)}건")

    out.append("")
    out.append("## 비꼼 후보 (칭찬 말 + 별점 3점 이하 또는 말끝 흐림, 강한 불만 말은 뺌 · 최대 다섯 · 판단은 사람이)")
    cands = [r for r in kept
             if has(r["리뷰"], PRAISE_WORDS) and not has(r["리뷰"], STRONG_WORDS)
             and (r["별점"].strip() in ("1", "2", "3") or any(m in r["리뷰"].replace("... 더보기", "") for m in HEDGE_MARKS))]
    cands.sort(key=lambda r: (r["별점"], int(r["연번"])))
    out.append(f"- 규칙에 걸린 후보: {len(cands)}건 (별점 낮은 순으로 다섯까지 적음)")
    for r in cands[:5]:
        out.append(f'- ({r["연번"]}, 별점 {r["별점"]}) "{one_line(r["리뷰"])}"')

    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
