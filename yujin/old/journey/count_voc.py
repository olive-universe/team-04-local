# count_voc.py · 리뷰를 윤 씨 여정 7단계로 나누어 센다 (11일차 3교시)
# 쓰는 법: python -I count_voc.py <리뷰 CSV 경로>
# 규칙은 아래 STAGES · STAGE3_EXCLUDE · COMPLAINT · PRAISE · AD 낱말 목록이 전부다.
# 고친 판 (2026-11-26): 2단계 'listing' 좁힘 · 4단계 'insurance'를 7단계로 옮김 · 3단계에서 점검 뒤 값 깎기 글 뺌. 규칙을 고치면 다시 돌린다.
# 낱말은 대소문자를 가리지 않고 찾는다. 한 리뷰가 여러 단계의 낱말을 가지면 여러 단계에 모두 센다.
import csv
import re
import sys

STAGES = [
    ("1 처음 배를 사기로 마음먹고 매물을 찾기 시작한다",
     r"first boat|new to boating|fairly new|take the plunge|looking for (?:a|our|my) (?:first )?boat|buy(?:ing)? (?:a|my|our) (?:first )?boat|purchase my"),
    ("2 중고 거래 앱에서 매물 글 두 개를 본다",
     r"\blistings\b|listed for sale|\badverts?\b|\bphotos?\b|\bpictures?\b|too good to be true|private seller|for sale"),
    ("3 두 매물 가운데 어느 쪽 값이 맞는지 견줘 보려 한다 (팀 병목)",
     r"\bprice[ds]?\b|\bpricing\b|overpriced|valuation|comparable|asking price|market value"),
    ("4 사기 전에 등록 기한과 배를 댈 곳을 알아본다",
     r"\bslips?\b|marina|moorage|mooring|\bberth|deadline"),
    ("5 판매자에게 물어볼 것을 들고 연락한다",
     r"\bseller|\bowner|\bcontact|\bcalled\b|\bphone|\bemail|negotiat|bargain|\boffer|deposit|contract"),
    ("6 배 상태를 점검받는다",
     r"\bsurvey|inspection|sea trial|hauled? out|\bmechanic"),
    ("7 돈을 보내고 배를 넘겨받아 내 이름으로 등록한다",
     r"escrow|\bpayment|\bwire|\bbank|\bmoney|documentation|\btitle\b|registration|\blien|coast guard|paperwork|closing|insurance"),
]
STAGE3_EXCLUDE = r"bargain|lower price|price (?:reduction|adjustment)|adjustment to the selling price|renegotiat"
COMPLAINT = (r"scam|ripped off|fraud|stolen|beware|problem|\bissues?\b|missed|\bfail|wrong|\blost\b|frustrat|painful|"
             r"nightmare|refund|disclaimer|could not|couldn.t|can.t|woes|trouble|lawsuit|\bsued\b|vague|expensive|worried|hidden")
PRAISE = r"\bgreat\b|\bhappy\b|\blove\b|\blucky\b|\bperfect\b|wonderful|\bthanks?\b|\bbest\b|excited"
AD = r"sponsored|advertisement|#ad\b|협찬|광고"


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


def main(path):
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    head, body = rows[0], rows[1:]
    total = len(body)
    seen, dup, ads, kept = set(), [], [], []
    for r in body:
        num, text = r[0], r[5]
        key = re.sub(r"\s+", " ", text).strip()
        if key in seen:
            dup.append(num)
            continue
        seen.add(key)
        if re.search(AD, text, re.I):
            ads.append(num)
            continue
        kept.append(r)
    star_col = [r[4] for r in kept if r[4].strip()]
    print("전체 리뷰 수:", total)
    print("뺀 리뷰: 중복", len(dup), dup, "· 광고/협찬", len(ads), ads)
    print("센 리뷰 수(분모):", len(kept))
    print("별점 칸(5번째 칸 '" + head[4] + "')에 값이 있는 리뷰:", len(star_col))
    none = []
    for name, pat in STAGES:
        hits = [r for r in kept if re.search(pat, r[5], re.I)]
        if name.startswith("3 "):
            # 고친 규칙 (2026-11-26, yujin 결정 가): 점검 뒤 값을 깎는 말이 함께 있으면 3단계(값 견주기)에서 뺀다
            hits = [r for r in hits if not re.search(STAGE3_EXCLUDE, r[5], re.I)]
        comp = [r for r in hits if re.search(COMPLAINT, r[5], re.I)]
        print("\n##", name)
        print("리뷰 건수:", len(hits), "· 불편 건수:", len(comp))
        shown = 0
        for r in comp:
            for s in sentences(r[5]):
                if re.search(pat, s, re.I) and re.search(COMPLAINT, s, re.I) and len(s) <= 260:
                    print("  인용 · 번호", r[0], "|", s)
                    shown += 1
                    break
            if shown == 3:
                break
    for r in kept:
        if not any(re.search(p, r[5], re.I) for _, p in STAGES):
            none.append(r[0])
    print("\n어느 단계에도 들어가지 않은 리뷰:", len(none))
    print("\n## 비꼬는 말일 수 있는 리뷰 (칭찬 낱말 + 불편 낱말이 한 문장에)")
    n = 0
    for r in kept:
        for s in sentences(r[5]):
            if re.search(PRAISE, s, re.I) and re.search(COMPLAINT, s, re.I) and len(s) <= 260:
                print("  번호", r[0], "|", s)
                n += 1
                break
        if n == 5:
            break


if __name__ == "__main__":
    main(sys.argv[1])
