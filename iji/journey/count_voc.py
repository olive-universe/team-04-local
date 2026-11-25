# -*- coding: utf-8 -*-
"""마린딜러 VOC 세기: 리뷰 CSV를 journey/stages.md 여정 6단계로 나누고 voc.md 결과 칸을 채운다.

쓰는 법 (iji 폴더 안 journey 폴더에서):
    python -I count_voc.py reviews/yacht_reviews.csv

입력 CSV 칸 (UTF-8, 머리줄 = 1행): 연번,출처,URL,작성일,별점,원문
- 별점은 비워도 된다 (비면 [확인 필요]).
- 규칙(단어 목록)은 voc.md 맨 위 '단계를 고르는 규칙'과 같아야 한다. 바꾸면 두 곳을 같이 바꾼다.
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VOC = HERE / "voc.md"
START, END = "<!-- 결과 시작 -->", "<!-- 결과 끝 -->"

# 맞추는 법
# - 한글 말: 글 안에 그 글자가 있으면 맞음
# - 영어 말: 낱말 전체가 맞아야 함 (broke는 broker에서 안 잡힘). 뒤에 s · es · ed · ing가 붙은 꼴도 같이 셈
# - 영어 말 끝에 * : 앞부분만 맞아도 셈 (inspect* → inspection, inspector)
# 여정 단계 (journey/stages.md 번호 1~6) → 이 말이 들어 있으면 그 단계 (여러 단계에 동시에 들어갈 수 있음)
STAGES = [
    ("1 살 만한 요트 매물을 찾는다", ["매물", "사이트", "광고글", "사진", "가격문의", "전화 문의", "전화문의",
                                  "listing", "listed", "advert*", "ad", "photo*", "picture*", "broker"]),
    ("2 매물과 판매자가 진짜인지 확인한다", ["사기", "가짜", "허위", "명의", "소유자", "압류", "서류", "신분",
                                     "scam*", "fake", "fraud*", "title", "lien", "owner", "stolen", "paperwork"]),
    ("3 배를 직접 보고 상태를 확인한다", ["검수", "시운전", "점검", "엔진", "선체", "누수", "서베이", "검사",
                                  "survey", "surveyor", "sea trial", "seatrial", "inspect*", "engine", "hull", "leak", "moisture"]),
    ("4 가격과 조건을 확인하고 계약한다", ["계약", "계약서", "협상", "네고", "가격 조정", "깎",
                                   "contract", "offer", "negotiat*", "purchase agreement", "bargain*"]),
    ("5 대금 지급 방법을 확인하고 지급한다", ["송금", "입금", "계약금", "잔금", "에스크로", "환불", "안전결제",
                                      "deposit", "escrow", "funds", "payment", "paid", "refund*", "checking account"]),
    ("6 명의를 바꾸고 배를 넘겨받는다", ["명의이전", "명의 이전", "변경등록", "등록", "인도", "넘겨받", "운송", "탁송",
                                 "registration", "title transfer", "documentation", "delivery", "delivered", "closing", "handover"]),
]
# 불편을 말했다고 보는 말
PAIN = ["불편", "문제", "고장", "사기", "후회", "손해", "비싸", "늦", "안 됨", "안됨", "못 ", "걱정", "속았", "환불", "분쟁", "다툼",
        "problem", "issue", "missed", "regret*", "scam*", "broke", "broken", "leak", "fail*", "disappoint*",
        "lost", "nightmare", "worried", "concerned", "frustrat*", "painful", "ripped off", "expensive", "mess", "dangerous"]
# 광고·협찬이라고 밝힌 말 (이 말이 있으면 뺌)
AD = ["광고", "협찬", "제공받아", "제공 받아", "원고료", "sponsored", "#ad", "paid partnership", "affiliate"]
# 칭찬 말과 불편 말이 '같은 문장'에 같이 있으면 '비꼬는 말일 수 있음' 후보 (판단은 사람이)
PRAISE = ["좋", "최고", "감사", "친절", "만족", "대단", "훌륭", "great", "thanks", "awesome", "love", "perfect", "nice", "fun", "good", "happy"]


def _pat(w):
    w = w.lower()
    if not w.isascii():
        return None
    if w.endswith("*"):
        return re.compile(r"(?<!\w)" + re.escape(w[:-1]))
    return re.compile(r"(?<!\w)" + re.escape(w) + r"(?:s|es|ed|ing)?(?!\w)")


_CACHE = {}


def has(text, words):
    low = text.lower()
    hit = []
    for w in words:
        if w not in _CACHE:
            _CACHE[w] = _pat(w)
        p = _CACHE[w]
        if (p.search(low) if p else w.lower() in low):
            hit.append(w)
    return hit


def sentence_with(text, words):
    """키워드가 처음 나오는 문장을 원문 그대로 잘라 준다 (글자는 바꾸지 않음)."""
    parts = re.split(r"(?<=[.!?。\n])", text)
    for p in parts:
        if has(p, words):
            return p.strip()
    return text.strip()


def norm(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def main(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig", newline="")))
    total = len(rows)
    seen, kept, dup, ad = set(), [], [], []
    for r in rows:
        t = r["원문"]
        if norm(t) in seen:
            dup.append(r["연번"]); continue
        seen.add(norm(t))
        if has(t, AD):
            ad.append(r["연번"]); continue
        kept.append(r)

    lines = ["| 여정 단계 | 리뷰 건수 | 그 가운데 불편을 말한 건수 | 그 가운데 별점 1 · 2점 건수 | 불편 인용 셋 (연번 · 원문 그대로) |",
             "| --- | --- | --- | --- | --- |"]
    unplaced = [r for r in kept if not any(has(r["원문"], w) for _, w in STAGES)]
    for name, words in STAGES:
        inn = [r for r in kept if has(r["원문"], words)]
        pain = [r for r in inn if has(r["원문"], PAIN)]
        stars = [r["별점"].strip() for r in pain]
        if pain and all(s == "" for s in stars):
            low = "[확인 필요] (별점 없음)"
        else:
            low = f"{sum(1 for s in stars if s in ('1', '2', '1.0', '2.0'))}건" + (" (별점 빈 칸 있음)" if "" in stars else "")
        quotes = "<br>".join(
            f"{r['연번']}: \"{sentence_with(r['원문'], PAIN).replace('|', '｜')}\"" for r in pain[:3]) or "-"
        lines.append(f"| {name} | {len(inn)}건 | {len(pain)}건 | {low} | {quotes} |")

    lines += ["",
              f"- 전체 리뷰 수(분모): 이 파일 안에서 {total}건",
              f"- 뺀 리뷰: {len(dup) + len(ad)}건 — 같은 글 두 번째 이상 {len(dup)}건 (연번 {', '.join(dup) or '없음'}), "
              f"광고·협찬이라고 밝힘 {len(ad)}건 (연번 {', '.join(ad) or '없음'})",
              f"- 어느 단계에도 들어가지 않은 리뷰: 이 파일 안에서 {len(unplaced)}건 (연번 {', '.join(r['연번'] for r in unplaced) or '없음'})",
              "- 한 리뷰가 여러 단계의 말을 담으면 그 단계마다 한 번씩 셌다. 그래서 단계별 건수를 더하면 분모보다 클 수 있다.",
              "", "### 칭찬처럼 보이지만 비꼬는 말일 수 있는 리뷰 (기계가 고른 후보, 판단은 사람이)", ""]
    def same_sentence(t):
        return any(has(s, PRAISE) and has(s, PAIN) for s in re.split(r"(?<=[.!?。\n])", t))
    cands = [r for r in kept if same_sentence(r["원문"])][:5]
    lines += [f"- {r['연번']}: \"{r['원문'].strip()}\"" for r in cands] or ["- 후보 없음"]

    block = "\n".join(lines)
    text = VOC.read_text(encoding="utf-8")
    a, b = text.index(START) + len(START), text.index(END)
    VOC.write_text(text[:a] + "\n" + block + "\n" + text[b:], encoding="utf-8")
    print(block)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2 or not Path(sys.argv[1]).exists():
        print("리뷰 CSV 경로를 주세요. 예: python -I count_voc.py reviews/yacht_reviews.csv")
        sys.exit(1)
    main(sys.argv[1])
