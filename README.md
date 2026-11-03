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
assets/js/course.js           # 퀴즈·토글 등 공통 동작
ai-data-analysis/
  index.html                  # 주차별 강의 목록
  weekNN/lessonMM.html        # N주 M차시 교안 (차시당 25분 영상 기준)
genai-practice/
  index.html
```

## 배포

Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / `(root)`
