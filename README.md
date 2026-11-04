# Deu_Edu_AX_MD

동의대학교 AX 마이크로디그리 공통 AI 교과 온라인 교안 (GitHub Pages로 제공)

| 폴더 | 교과 | 대상 |
|---|---|---|
| [`ai-data-analysis/`](ai-data-analysis/) | AI와 데이터 분석 | 이공계열 2학년 1학기 |
| [`genai-practice/`](genai-practice/) | 생성형AI 활용 실무 | 인문·상경계열 |
| `assets/` | 두 교과가 함께 쓰는 스타일(CSS)·스크립트(JS) | — |

## 구조

```
index.html                    # 교과 선택 첫 화면
assets/css/course.css         # 공통 스타일 (교과별 색상: data-course="ai" | "genai")
assets/js/course.js           # 목록 페이지 공통 동작
assets/css/slides.css         # 슬라이드형 교안 스타일 (1280×720 화면을 창 크기에 맞춤)
assets/js/slides.js           # 슬라이드 넘김(← → 키·스와이프·버튼), 단계별 등장(.frag), 퀴즈
assets/js/icons.js            # 공통 선 아이콘 (<svg class="ic"><use href="#i-이름"/></svg>)
ai-data-analysis/
  index.html                  # 주차별 강의 목록
  weekNN/lessonMM.html        # N주 M차시 슬라이드 교안 (차시당 25분 영상 기준)
  weekNN/lessonMM.js          # 그 차시의 직접 해 보기(인터랙티브) 화면
genai-practice/
  index.html
```

## 배포

Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / `(root)`

## 슬라이드 조작

← → 키(내용이 한 단계씩 나타난 뒤 다음 장) / 스페이스 / 화면 스와이프 / 하단 ◀ ▶ 버튼으로 넘김, `F` 전체화면. 주소 끝 `#5`처럼 쪽 번호로 바로 이동 가능. 브라우저 인쇄(PDF 저장) 시 한 장씩 출력.
