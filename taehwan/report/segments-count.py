# 세그먼트 건수 세기 · brand/segments.md 근거
# 실행: python -I report/segments-count.py   (llm-academy 폴더에서)
# 입력: inputs/team_reviews.csv (80건). 분모: 뜻을 읽을 수 없는 연번 14, 34를 뺀 78건 (report/review-report.md 와 같음)
# 2026-11-19 전태환 (Claude 도움)
import csv, io, re, sys

EXCLUDE = {"14", "34"}  # review-report.md 3칸: 뜻을 읽을 수 없는 글

# 세그먼트 = 리뷰에 적힌 '행동' 낱말. 정규식은 brand/segments.md 표의 '행동 기준'과 같아야 한다.
SEGMENTS = [
    ("S1 밤 풍경 보러 온 손님", "무엇을 하러·언제", r"밤|야경|해가 지|해질|해 질|석양|일몰|night|lighting|반짝"),
    ("S2 불꽃·행사 날 온 손님", "무엇을 하러·언제", r"불꽃|축제|드론|fireworks|drone|[Dd]rone"),
    ("S3 차를 몰고 온 손님", "어떻게 왔나", r"주차|차타고|차 타고|운전"),
    ("S4 해변에서 놀다 간 손님", "무엇을 하러·무엇을 골랐나", r"모래 ?냥|삽|요트|산책|들어가 놀|수영|레포츠|파라솔|튜브|세족|샤워|물멍|놀다|놀아|[Ss]wim"),
    ("S5 다시 온 손님", "다시 왔나", r"또 가|또 오|다시|오랜만|추억|고향|항상|늘 |언제와도|언제 방문해도|살았|lived|그립"),
]

rows = list(csv.DictReader(open("inputs/team_reviews.csv", encoding="utf-8-sig")))
rows = [r for r in rows if r["연번"] not in EXCLUDE]
N = len(rows)

out = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
out.write(f"분모 {N}\n")
hits = {}
for name, axis, pat in SEGMENTS:
    ids = [r["연번"] for r in rows if re.search(pat, r["리뷰"])]
    hits[name] = ids
    out.write(f"{name} | {axis} | {len(ids)}/{N} | {','.join(ids)}\n")

per = {}
for name, ids in hits.items():
    for i in ids:
        per.setdefault(i, []).append(name.split()[0])
multi = {i: s for i, s in per.items() if len(s) > 1}
none = [r["연번"] for r in rows if r["연번"] not in per]
out.write(f"두 세그먼트 이상 {len(multi)}/{N} | " + "; ".join(f"{i}:{'+'.join(s)}" for i, s in sorted(multi.items(), key=lambda x: int(x[0]))) + "\n")
out.write(f"어느 세그먼트에도 없음 {len(none)}/{N} | {','.join(none)}\n")
out.write(f"한 세그먼트 이상 {len(per)}/{N}\n")
