# refactor-log · 파일 자리 옮긴 기록

- 규칙: 파일 내용은 고치지 않고 자리와 이름만 바꾼다. 지우지 않는다. (`CLAUDE.md` 5. 폴더 규칙)

| 날짜 | 원래 자리 → 새 자리 | 이유 |
|---|---|---|
| 2026-11-24 | `CLAUDE.template.md` → `old/CLAUDE.template.md` | 이미 `CLAUDE.md`로 채워서 다 쓴 틀 |
| 2026-11-24 | `.gitkeep` → `old/.gitkeep` | 폴더를 깃허브에 보이게 하려던 빈 파일. 이제 필요 없음 |
| 2026-11-25 | `inputs/team_reviews_source.md` → `data/team_reviews_source.md` | 강의가 `inputs/`라고 한 파일은 `data/`에 둔다는 규칙. 원문·닉네임이 없는 기록 파일이라 옮김. 후기 원문 파일(`kakao-raw.txt`, `kakao-raw-2.txt`, `team_reviews.csv`)은 `inputs/`에 그대로 둠 |
| 2026-11-25 | `inputs/kaka0-raw.txt` → `inputs/kakao-raw.txt` | 파일 이름 오타(o 대신 숫자 0) 고침. 내용은 그대로 |
| 2026-11-26 | `story/ImagePrint.jpg` → `inputs/ImagePrint.jpg` | 국제신문 제공 사진. 실린 페이지에 무단 배포 금지 문구가 있어 공개 저장소에 올리지 않음 (8일차 1교시 그림 연습용) |

- 파일 개수 (`examples/` 뺌, 이 기록 파일 빼고 셈): 옮기기 전 30개 → 옮긴 뒤 30개
