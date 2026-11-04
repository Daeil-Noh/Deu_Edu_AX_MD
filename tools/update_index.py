"""강의 목록 페이지(ai-data-analysis/index.html)의 '주차별 강의' 부분을 실제 파일 기준으로 다시 만든다.
python3 tools/update_index.py
· weekNN/lessonMM.html 이 있으면 차시 제목에 링크
· weekNN/lessonMM.ipynb 가 있으면 'Colab 실습' 링크, assignment*.ipynb / 기타 노트북은 '과제·양식' 링크
"""
import os, re, glob, html

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
C = os.path.join(ROOT, 'ai-data-analysis')
COLAB = 'https://colab.research.google.com/github/Daeil-Noh/Deu_Edu_AX_MD/blob/main/ai-data-analysis/'

WEEKS = [
    (1, 'AX와 AI 데이터 분석', ['AI와 데이터 분석이란?', '제조·연구·로봇 현장의 AX 사례', '데이터 윤리와 개인정보 기초'], ''),
    (2, '데이터 분석 과정', ['분석 프로세스: 문제 정의부터 해석까지', '데이터의 종류: 공정·센서·실험 데이터', '공공데이터·AI허브에서 데이터 찾기'], ''),
    (3, '분석 환경 시작하기', ['Google Colab 시작하기', '파이썬 최소 문법 ①: 변수·자료형·리스트', '파이썬 최소 문법 ②: 조건문·반복문·라이브러리'], ''),
    (4, '생성형AI 코딩 도우미', ['생성형AI로 코드 만들고 실행하기', 'AI로 오류 메시지 읽고 해결하기', 'AI 코드 검증 기초: 환각과 편향'], ''),
    (5, '데이터 불러오기와 정리', ['표 데이터 불러오기와 살펴보기(pandas)', '조건으로 고르기와 정렬하기', '결측치 처리와 자료형 정리'], ''),
    (6, '통계로 데이터 읽기', ['평균·중앙값·분산', '분포와 이상치', '그룹별 집계로 비교하기'], ''),
    (7, '데이터 시각화', ['목적에 맞는 그래프 고르기', '그래프 그리기 실습', '상관관계와 인과관계: 공정 변수와 품질'], '과제1 데이터 시각화'),
    (8, '중간고사', [], '1~7주 · 오프라인 시험'),
    (9, '머신러닝 시작하기', ['머신러닝이란? (지도·비지도 학습)', '학습 데이터와 검증 데이터 나누기', '전공 문제를 데이터 문제로 바꾸기'], '보고서 주제 제출'),
    (10, '예측: 회귀', ['회귀의 개념', '공정 조건으로 품질 예측하기', '예측 오차로 성능 평가하기'], ''),
    (11, '판정: 분류', ['분류의 개념: 의사결정나무와 과적합', '불량품 판정 실습', '정확도·정밀도·재현율'], '과제2 불량품 분류'),
    (12, '군집과 이상탐지', ['비슷한 것끼리 묶기: 군집', '이상탐지와 설비 예지보전', '제공 코드로 이상탐지 실습'], ''),
    (13, '딥러닝과 생성형AI', ['신경망 원리 직관적으로 이해하기', '이미지 인식과 비전 검사', '생성형AI의 원리'], ''),
    (14, '전공 분석 보고서', ['예시 프로젝트: AI와 함께 분석 전 과정 따라 하기', '분석 보고서 작성법', '결과 해석과 AI 활용 검증 점검'], ''),
    (15, '기말고사', [], '9~14주 · 오프라인 시험 · 보고서 제출'),
]
EXTRA_NAMES = {'assignment1': '과제1 양식', 'assignment2': '과제2 양식', 'topic_form': '보고서 주제 양식', 'report_template': '보고서 양식'}


def week_html(w, title, lessons, note):
    d = f'week{w:02d}'
    items = ''
    for i, t in enumerate(lessons, 1):
        page = os.path.join(C, d, f'lesson{i:02d}.html')
        nb = os.path.join(C, d, f'lesson{i:02d}.ipynb')
        t_e = html.escape(t)
        if os.path.exists(page):
            li = f'{i}차시 · <a href="{d}/lesson{i:02d}.html">{t_e}</a>'
            if os.path.exists(nb):
                li += f' <a class="nb" href="{COLAB}{d}/lesson{i:02d}.ipynb" target="_blank" rel="noopener">Colab 실습</a>'
        else:
            li = f'{i}차시 · {t_e}<span class="soon">준비 중</span>'
        items += f'<li>{li}</li>'
    extras = ''
    for p in sorted(glob.glob(os.path.join(C, d, '*.ipynb'))):
        stem = os.path.splitext(os.path.basename(p))[0]
        if re.fullmatch(r'lesson\d\d', stem):
            continue
        name = EXTRA_NAMES.get(stem, stem)
        extras += f' <a class="nb" href="{COLAB}{d}/{stem}.ipynb" target="_blank" rel="noopener">{html.escape(name)}</a>'
    head = f'<div class="week-head"><span class="week-no">{w}주</span><span class="week-title">{html.escape(title)}</span>'
    if note:
        head += f'<span class="week-note">{html.escape(note)}</span>'
    head += extras + '</div>'
    body = f'\n      <ol>{items}</ol>' if items else ''
    return f'    <div class="week{" exam" if not lessons else ""}">\n      {head}{body}\n    </div>'


def main():
    p = os.path.join(C, 'index.html')
    s = open(p, encoding='utf-8').read()
    block = '\n'.join(week_html(*w) for w in WEEKS)
    s2 = re.sub(r'(<div class="weeks">\n)(.*?)(\n  </div>\n</main>)', lambda m: m.group(1) + block + m.group(3), s, flags=re.S)
    assert s2 != s or block in s, 'weeks block not found'
    if '.week .nb' not in s2:
        s2 = s2.replace('</head>', '<style>\n  .week a.nb { font-size: 12px; font-weight: 700; margin-left: 8px; padding: 2px 8px; border-radius: 6px; background: #e8710a; color: #fff; text-decoration: none; white-space: nowrap; }\n</style>\n</head>', 1)
    open(p, 'w', encoding='utf-8').write(s2)
    n = len(re.findall(r'lesson\d\d\.html', block))
    print(f'index updated: {n} lessons linked')


if __name__ == '__main__':
    main()
