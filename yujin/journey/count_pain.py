# count_pain.py · 불편 후보마다 빈도(몇 건 / 분모)와 강도(그 가운데 별점 1·2점)를 센다 (11일차 4교시)
# 쓰는 법 (저장소 맨 위 폴더에서): python -I yujin/journey/count_pain.py yujin/team_reviews.csv
# 리뷰 파일과 단계는 yujin/journey/voc.md (혜선 님 voc.md 복사본)와 같다: 투어 후기 69건, hyeseon/journey/stages.md 1~7단계.
# 고친 판 (2026-11-26): 첫 판에서 44번(친절한 '전화응대'), 20번(센터가 있는지 '몰랐어요')이 잘못 들어가고 12번(주차 극혐), 46번(pay separately)을 놓쳐 규칙을 고침.
# 후보 규칙: ALL의 말이 모두(그룹마다 하나 이상) 리뷰에 있으면 그 후보에 센다. 같은 글·광고 글은 voc.md처럼 뺀다.
import csv
import sys

CANDIDATES = [
    ("A", "화장실이 더럽고 냄새가 나요", "4. 배를 직접 보러 가요",
     [["화장실"], ["더럽", "냄새", "악취", "청소", "최악"]]),
    ("B", "주차할 자리가 없어요", "4. 배를 직접 보러 가요",
     [["주차"], ["불편", "부족", "극혐", "자리"]]),
    ("C", "직원이 반말하고 불친절해요", "4. 배를 직접 보러 가요",
     [["반말", "불친절", "비아냥", "깡패"]]),
    ("D", "연락하라더니 전화·문자에 답이 없어요", "3. 매물이 진짜인지 확인해요 (병목)",
     [["전화", "문자", "연락"], ["안받", "씹", "답이 없", "답장", "안 받", "없어"]]),
    ("E", "타기 직전에야 조건을 알려 줘요", "3. 매물이 진짜인지 확인해요 (병목)",
     [["사전 공지", "공지는 없", "미리 알려", "탈 때 알려"]]),
    ("F", "평점이 조작된 것 같아 못 믿겠어요", "3. 매물이 진짜인지 확인해요 (병목)",
     [["조작", "평점"], ["조작", "믿", "의심", "이상"]]),
    ("G", "값이 따로 붙어서 올라가요", "5. 값을 정하고 계약해요",
     [["따로", "별도", "separately", "extra"], ["비용", "가격", "요금", "cost", "pay", "price"]]),
]
AD_WORDS = ["협찬", "광고", "제공받", "원고료", "체험단"]


def match(text, groups):
    return all(any(w in text for w in g) for g in groups)


def main(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    seen, kept, dropped = set(), [], []
    for r in rows:
        key = " ".join(r["리뷰"].split())
        if key in seen or any(w in r["리뷰"] for w in AD_WORDS):
            dropped.append(r["연번"])
            continue
        seen.add(key)
        kept.append(r)
    n = len(kept)
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"전체 {len(rows)}건 · 뺀 리뷰 {len(dropped)}건 {dropped} · 분모 {n}건")
    print("| 후보 | 손님 말투 | 여정 단계 | 빈도 | 강도(별점 1·2점) | 연번 |")
    print("|---|---|---|---|---|---|")
    for cid, line, stage, groups in CANDIDATES:
        hit = [r for r in kept if match(r["리뷰"], groups)]
        low = [r for r in hit if r["별점"].strip() in ("1", "2")]
        nostar = [r for r in hit if not r["별점"].strip()]
        strength = f"{len(low)} / {len(hit)}" + (f" ({round(100 * len(low) / len(hit))}%)" if hit else "") \
            + (f" · 별점 없음 {len(nostar)}건" if nostar else "")
        ids = ", ".join(r["연번"] for r in hit)
        print(f"| {cid} | {line} | {stage} | {len(hit)} / {n} | {strength} | {ids} |")


if __name__ == "__main__":
    main(sys.argv[1])
