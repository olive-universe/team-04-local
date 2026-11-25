# CSV 정리 + 명세 쓰기 (AX 데이터·서비스 트랙)

`data-spec.md`를 `llm-academy` 폴더에 놓은 뒤, 파일 이름 두 곳만 바꿉니다.
고를 수 있는 파일: `inputs/yeongdo_commercial_raw.csv`(영도구 상가 원본 행), `inputs/busan_port_container_2025.csv`(항만), 어제 받은 `inputs/` 파일.

```text
inputs/yeongdo_commercial_raw.csv 를 정리하고 명세를 써 줘.
1. 원본은 고치지 말고, 정리한 표는 inputs/yeongdo_commercial_raw_clean.csv 로 새로 저장해(UTF-8 BOM, 엑셀에서 한글이 깨지지 않게).
2. 정리는 세 가지만: 모든 행이 빈 칸인 열은 빼고, 완전히 같은 행은 하나만 남기고, 무엇을 몇 개 뺐는지 기록해. 숫자는 바꾸지 마.
3. data-spec.md 의 명세 7칸을 채워: 제공기관 · 갱신주기 · 기준 시점 · 행 수(원본/정리 후) · 컬럼 뜻 · 단위 · 결측·주의.
4. 제공기관·갱신주기는 SOURCE-day03.md(어제 파일이면 SOURCE.md)에서 가져오고, 단위를 파일과 설명에서 못 찾으면 '못 찾음'이라고 적어.
```
