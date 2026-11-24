# data-spec · 부산 선박사고 위치 699건 (3일차 데이터·서비스 트랙)

- 작성: yujin · 2026-11-24
- 원본: `data/ship_accident_points_kcg.zip` 안 `TL_SHPACC_HS_P.dbf` (전국 38,625개) — 원본은 고치지 않음
- 꺼낸 표: `data/busan_ship_accidents_raw.csv` — `acdnt_pstn`(사고위치) 글에 '부산'이 든 레코드만. UTF-8 BOM (엑셀에서 한글이 깨지지 않게). 맨 앞에 원본 레코드 번호 `record_no` 칸을 더함.

## 정리한 것

강의 기준 세 가지로 정리를 시도했습니다.

| 정리 | 결과 |
|---|---|
| 모든 행이 빈 칸인 열 빼기 | 0개 — 27개 열 모두 값이 하나 이상 있음 |
| 완전히 같은 행 하나만 남기기 | 0개 — `record_no`를 빼고 비교해도 같은 행 없음 |
| 숫자 바꾸기 | 하지 않음 |

뺄 것이 없어 정리한 표가 원본과 똑같았습니다. 그래서 `_clean.csv`는 따로 두지 않고 `busan_ship_accidents_raw.csv` 하나만 둡니다.

## 명세 7칸

| 칸 | 내용 |
|---|---|
| 제공기관 | 해양수산부 국립해양조사원 해도수로과 (해양경찰청 공유 데이터 기반) — `SOURCE.md` 3절, https://www.data.go.kr/data/15130156/fileData.do |
| 갱신주기 | 수시 (1회성 데이터) — 공공데이터포털 페이지, `SOURCE.md` 3절 |
| 기준 시점 | 파일 이름 20250811. 제작일자 `fbctn_ymd`는 2018-12-06 ~ 2023-12-08 (부산 699건 중 20181206이 460건). 사고 발생일은 알 수 없음 (아래 결측·주의) |
| 행 수 | 원본 전국 38,625개 → 부산 699행 (머리줄 빼고). 정리 후 699행 그대로 |
| 컬럼 뜻 | 27개. 컬럼 정의서(zip 안 `…컬럼맵핑정보.xlsx`) 기준: `record_no` 원본 레코드 번호(더함) · `gid` 공간정보아이디 · `obj_sn` 객체일련번호 · `inst_cd` 기관코드 · `biz_zone_c` 사업구역코드 · `fbctn_ymd` 제작일자 · `clsf_cd` 분류코드 · `ocrn_ymd` 발생일자 · `ocrn_hm` 발생시분 · `acdnt_pstn` 사고위치 · `ycdnt`·`xcdnt` Y·X좌표 · `orgnl_lat`·`orgnl_lot` 원본위도·경도 · `cmptnc_kcg` 관할해양경찰서코드 · `ocrn_sear_` 발생해역코드 · `acdnt_type` 사고유형코드 · `ocrn_caus_` 발생원인코드 · `wthr_bknw_` 날씨특보코드 · `acdnt_ship` 사고선박수 · `ship_knd_c` 선박종류코드 · `rscu_prsn`·`dth_prsn`·`misg_prsn` 구조·사망·실종인원 · `orgnl_xcdn`·`orgnl_ycdn` 원본X·Y좌표 · `err_cd` 오류코드 |
| 단위 | `ycdnt`·`xcdnt`: 미터 — 데이터에서 찾음 (zip 안 `.prj`에 `UNIT["Meter",1.0]`, Korea 2000 통합좌표계). `orgnl_lat`·`orgnl_lot`: 도\|분\|초 — 데이터에서 찾음 (예 `35\|07\|10` = 북위 35도 7분 10초, 부산 위도와 맞음). `acdnt_ship`: 척 · `rscu_prsn`·`dth_prsn`·`misg_prsn`: 명 — 컬럼 이름('사고선박수', '구조인원')에서 짐작, 정의서에 단위 칸은 없음. 나머지 코드 칸: 단위 없음 |
| 결측·주의 | ① `ocrn_ymd`(발생일자)·`ocrn_hm`(발생시분)에 날짜·시각이 아니라 35·34·0 같은 값만 있음 (699행 중 35가 683행). `orgnl_xcdn`·`orgnl_ycdn`도 같은 값(35가 683행). 가설: 칸이 서로 밀려 위도 '도' 값이 들어간 것일 수 있음 → 사고 날짜는 이 표로 알 수 없음. ② 코드 칸(`ship_knd_c`, `acdnt_type`, `ocrn_caus_`, `wthr_bknw_`, `ocrn_sear_`, `cmptnc_kcg`)의 뜻은 zip 안에 없음 [확인 필요: 코드표]. ③ `cmptnc_kcg`가 '0'인 행 80개, 빈 행 0개. ④ `ycdnt`·`xcdnt`가 0인 행 3개 (좌표 없음). ⑤ `err_cd`가 채워진 행 94개 (ERR004 84개 등, 뜻 모름). ⑥ '부산' 글자로 골랐기 때문에, 부산 앞바다라도 사고위치 글이 비었거나 '부산'이 없는 사고는 빠짐 (전국 사고위치 빈 행 11,415개). ⑦ 사고위치 글에 신고 주소가 먼저 적힌 행이 있음 (예 `record_no` 14274) |

## 다시 확인할 것 (사람이)

- 엑셀로 `busan_ship_accidents_raw.csv`를 열어 맨 아래 행 번호가 700(머리줄 + 699)인지 봅니다. 보기만 하고 저장하지 않고 닫습니다.
- 단위 칸에서 '짐작'이라고 적은 줄(척·명)은 정의서에 없는 단위입니다.
