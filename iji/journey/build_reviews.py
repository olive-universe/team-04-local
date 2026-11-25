# -*- coding: utf-8 -*-
"""reviews/raw/*.txt (브라우저에서 옮긴 글)를 지문(SHA-256 앞 12자리)으로 원문과 맞춰 보고 reviews/yacht_reviews.csv를 만든다.

raw 파일 형식:
    THREAD 제목 | URL
    @@@ 글번호 | 작성일 | 지문
    본문 …
지문은 브라우저에서 원문(줄마다 공백을 한 칸으로, 빈 줄 없앰)으로 계산한 값이다.
옮긴 글의 지문이 다르면 한 글자라도 바뀐 것이므로 CSV에 넣지 않고 화면에 알린다.
"""
import csv
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "reviews" / "raw"
OUT = HERE / "reviews" / "yacht_reviews.csv"


def norm(t):
    t = re.sub("[​‌‍﻿]", "", t.replace(" ", " "))
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in t.split("\n")]
    return "\n".join(l for l in lines if l)


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]


rows, bad = [], []
for f in sorted(RAW.glob("*.txt")):
    text = f.read_text(encoding="utf-8")
    head, *blocks = re.split(r"^@@@ ", text, flags=re.M)
    title, url = [s.strip() for s in head.replace("THREAD ", "", 1).strip().rsplit(" | ", 1)]
    for b in blocks:
        first, _, body = b.partition("\n")
        pid, date, fp = [s.strip() for s in first.split(" | ")]
        body = norm(body)
        if sha(body) != fp:
            bad.append(f"{f.name} 글 {pid}")
            continue
        rows.append({"출처": f"{url.split('/')[2]} · {title}", "URL": f"{url}#post-{pid}", "작성일": date, "별점": "", "원문": body})

with open(OUT, "w", encoding="utf-8-sig", newline="") as fo:
    w = csv.DictWriter(fo, fieldnames=["연번", "출처", "URL", "작성일", "별점", "원문"])
    w.writeheader()
    for i, r in enumerate(rows, 1):
        w.writerow({"연번": i, **r})

print(f"CSV {len(rows)}건 저장 · 지문 불일치로 뺀 글 {len(bad)}건")
for x in bad:
    print("  불일치:", x)
