# -*- coding: utf-8 -*-
"""마린딜러 불편 후보 세기: 리뷰 CSV에서 불편 후보마다 맞는 리뷰를 세고 pain-top3.md 결과 칸을 채운다.

쓰는 법 (iji 폴더 안 journey 폴더에서):
    python -I count_pain.py reviews/yacht_reviews.csv

- 후보마다 '말 묶음'이 여럿 있다. 리뷰가 **모든 묶음**에서 말을 하나 이상 담으면 그 후보로 센다.
- 맞추는 법은 count_voc.py와 같다 (영어는 낱말 전체 · 뒤에 s/es/ed/ing 허용 · 끝에 *면 앞부분만).
- 별점이 모두 비면 강도는 [확인 필요].
- 규칙을 바꾸면 pain-top3.md '후보를 고르는 규칙' 표도 같이 바꾼다.
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "pain-top3.md"
START, END = "<!-- 결과 시작 -->", "<!-- 결과 끝 -->"

# (한 줄 이름(손님 말투), 여정 단계(stages.md 번호), [말 묶음, ...])
CANDIDATES = [
    ("광고 보고 연락한 판매 회사가 사기였어요", "1 · 2",
     [["scam*", "fraud*", "fake", "ripoff", "ripped off", "too good to be true"]]),
    ("브로커 광고 말과 실제 배 상태가 달라요", "1",
     [["broker*"], ["neglect*", "poor quality", "adondoned", "abandon*", "get outs", "lovingly", "told me"]]),
    ("검수(서베이)에서 못 잡은 고장을 산 뒤에 알았어요", "3",
     [["survey", "surveyor", "inspect*"],
      ["missed", "miss", "not found", "after the sale", "after purchase", "since purchase", "unexpected"]]),
    ("검수원 실력을 미리 알 수 없고, 놓쳐도 책임을 묻기 어려워요", "3",
     [["survey", "surveyor"], ["accountable", "recourse", "disclaimer*", "sued", "lawsuit*", "honesty"]]),
    ("돈이 브로커 계좌에 묶여 언제 넘어갈지 몰라요", "5",
     [["escrow", "checking account", "funds", "wired"], ["broker*", "account"]]),
    ("예전 주인 대출(압류)이 안 지워져 명의 이전이 막혔어요", "6 (· 2)",
     [["lien*", "lein"], ["documentation", "title", "coast guard", "uscg", "cg"]]),
]

# '우리가 못 고치는 것인가'는 기계가 세지 않는다. 사람이 매긴 값을 여기 적고, 까닭은 pain-top3.md에 적는다.
HUMAN_CANNOT_FIX = {
    "광고 보고 연락한 판매 회사가 사기였어요": "아니요 (가설)",
    "브로커 광고 말과 실제 배 상태가 달라요": "모름",
    "검수(서베이)에서 못 잡은 고장을 산 뒤에 알았어요": "모름",
    "검수원 실력을 미리 알 수 없고, 놓쳐도 책임을 묻기 어려워요": "모름",
    "돈이 브로커 계좌에 묶여 언제 넘어갈지 몰라요": "모름",
    "예전 주인 대출(압류)이 안 지워져 명의 이전이 막혔어요": "모름",
}


def _pat(w):
    w = w.lower()
    if not w.isascii():
        return None
    if w.endswith("*"):
        return re.compile(r"(?<!\w)" + re.escape(w[:-1]))
    return re.compile(r"(?<!\w)" + re.escape(w) + r"(?:s|es|ed|ing)?(?!\w)")


def has(text, words):
    low = text.lower()
    out = []
    for w in words:
        p = _pat(w)
        if (p.search(low) if p else w.lower() in low):
            out.append(w)
    return out


def main(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig", newline="")))
    total = len(rows)
    lines = ["| 후보 | 여정 단계 | 빈도(이 파일에서 몇 건 / 분모) | 강도(그 리뷰 가운데 별점 1 · 2점 비율) | 해결 가능성(1~5) | 우리가 못 고치는 것인가 |",
             "| --- | --- | --- | --- | --- | --- |"]
    detail = []
    for name, stage, groups in CANDIDATES:
        hit = [r for r in rows if all(has(r["원문"], g) for g in groups)]
        stars = [r["별점"].strip() for r in hit]
        if not hit:
            strength = "- (0건)"
        elif all(s == "" for s in stars):
            strength = "[확인 필요] (별점 없음)"
        else:
            rated = [s for s in stars if s]
            low = sum(1 for s in rated if s in ("1", "2", "1.0", "2.0"))
            strength = f"{low}건 / {len(rated)}건" + (" (별점 빈 칸 있음)" if len(rated) < len(stars) else "")
        lines.append(f"| {name} | {stage} | {len(hit)}건 / {total}건 | {strength} |  | {HUMAN_CANNOT_FIX.get(name, '모름')} |")
        detail.append(f"- {name}: 연번 {', '.join(r['연번'] for r in hit) or '없음'}")
    lines += ["", f"- 분모: 이 파일(`reviews/yacht_reviews.csv`) 전체 리뷰 {total}건",
              "- 한 리뷰가 여러 후보에 맞으면 후보마다 한 번씩 셌다. 그래서 건수를 더하면 분모보다 클 수 있다.",
              "", "### 후보마다 맞은 리뷰 연번 (사람이 원문을 열어 확인할 것)", ""] + detail
    block = "\n".join(lines)
    print(block)
    if OUT.exists():
        text = OUT.read_text(encoding="utf-8")
        if START in text and END in text:
            a, b = text.index(START) + len(START), text.index(END)
            OUT.write_text(text[:a] + "\n" + block + "\n" + text[b:], encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2 or not Path(sys.argv[1]).exists():
        print("리뷰 CSV 경로를 주세요. 예: python -I count_pain.py reviews/yacht_reviews.csv")
        sys.exit(1)
    main(sys.argv[1])
