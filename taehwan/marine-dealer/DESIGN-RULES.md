# 마린딜러 디자인 규칙 (Yacht Marketplace UI/UX)

저장한 날: 2026-11-24 · 사용자가 붙여 준 규칙 원문을 그대로 옮김.

## 원문

# Project: 중고 요트 거래 플랫폼 (Yacht Marketplace)

## UI/UX & Design Rules (Strict - No AI Slop)
- **No Emojis:** UI 텍스트, 버튼, 배지, 제목, 더미 데이터 어디에도 이모지(예: 요트·반짝이 그림 글자)를 절대 사용하지 마라. 모든 아이콘은 `lucide-react` 또는 `@phosphor-icons/react` (strokeWidth 1.5)만 사용한다.
- **Color Palette:**
  - 배경: `#F8F9FA` (Off-white) / 카드 배경: `#FFFFFF`
  - 메인 텍스트 & 주요 버튼: `#0B192C` (Deep Marine Navy)
  - 보더(테두리): `#E2E8F0` (1px solid)
  - 촌스러운 블루/퍼플 그라데이션(`bg-gradient-*`) 및 네온 컬러 사용 금지.
- **Shapes & Elevation:**
  - `shadow-lg`, `shadow-xl` 등 과한 그림자 금지. 대신 `border border-slate-200`와 미세한 호버 상태(`hover:border-slate-400`)로 계층을 구분한다.
  - 과도한 둥글기(`rounded-2xl`, `rounded-3xl`) 대신 `rounded-md` 또는 `rounded-lg`로 절제된 각을 유지한다.
- **Typography & Hierarchy:**
  - 가격(KRW/USD), 전장(LOA ft), 건조연도(Year), 엔진 사용시간(Hours) 등 핵심 스펙 숫자는 `tabular-nums`를 적용해 정렬감을 맞춘다.
- **Domain-Specific Layout:**
  - 일반 당근마켓식 중고거래 UI(제목/가격/동네만 있는 리스트)를 피하고, 글로벌 요트 브로커리지(YachtWorld 등)처럼 **[좌측 다중 조건 필터 사이드바 + 우측 4:3 비율 실사 위주 매물 그리드]** 구조를 따른다.
  - 더미 데이터 작성 시 '홍길동', '멋진 요트' 같은 텍스트 금지. 실제 브랜드와 모델명(Beneteau Oceanis 46.1, Lagoon 42, Azimut 55 등) 및 실제 국내 계류장(수영만 요트경기장, 왕산마리나, 전곡항 등) 데이터를 사용한다.

(원문 첫 줄의 이모지 예시 두 개는 이 파일도 규칙을 지키도록 말로 바꿔 적음.)

## 이 프로젝트에 옮긴 방법

`index.html`은 React·Tailwind 없이 HTML 한 장이라 아래처럼 옮긴다.

| 규칙에 나온 것 | 이 파일에서 |
|---|---|
| `lucide-react` 아이콘 | Lucide 아이콘 SVG를 스크립트 안 `ICON` 객체에 넣고 `stroke-width="1.5"`로 그림 |
| `rounded-md` / `rounded-lg` | `border-radius:6px` / `8px` (`--r-sm` / `--r`) |
| `border-slate-200` | `1px solid #E2E8F0` (`--g-4`) |
| `hover:border-slate-400` | 호버 때 `border-color:#94A3B8` |
| `tabular-nums` | `font-variant-numeric:tabular-nums` |

- 남겨 두는 것: 문장 속 화살표 `→`·`←`, 수학 기호 `≠`, 신고 패킷 텍스트 안의 `■`(복사해 쓰는 글이라서), 리스크 원그래프의 `conic-gradient`(장식이 아니라 그래프라서).
- 상태색(초록 확인·노랑 주의·빨강 위험)은 뜻을 전하는 색이라 남긴다.
- 스크립트를 고친 뒤에는 꼭 `node tools/update-csp.js`를 돌린다 (안 하면 화면이 멈춤).

## 진행

- [x] 1단계: 규칙 저장 + 겉모양 정리 (색·그림자·둥글기·그라데이션·숫자·아이콘)
- [x] 2단계: 왼쪽 필터 사이드바 + 오른쪽 4:3 사진 격자 (선종·길이·연식·가격·계류지·검수 완료만, 정렬 4가지, 휴대폰에서는 접기)
- [x] 3단계: 실제 모델명·운영 중인 계류장(더베이101·왕산마리나·전곡항)으로 가상 매물 다시 쓰기 + 엔진 사용시간(Hours) 값과 필터 (근거: `../research/2026-11-24-요트-모델-제원-국내-계류장.md`)
