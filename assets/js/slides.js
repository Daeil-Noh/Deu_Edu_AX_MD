// DEU AX Micro-Degree 슬라이드 넘김 (← → 키, 스페이스, 스와이프, 하단 버튼, F 전체화면)
(function () {
  const deck = document.querySelector('.deck');
  const slides = Array.from(document.querySelectorAll('.slide'));
  const prev = document.querySelector('[data-prev]');
  const next = document.querySelector('[data-next]');
  const count = document.querySelector('.count');
  const bar = document.querySelector('.bar');
  const total = slides.length;
  let cur = 0;

  slides.forEach((s, i) => {
    const no = s.querySelector('.s-foot .no');
    if (no) no.textContent = (i + 1) + ' / ' + total;
  });

  function fit() {
    const vp = document.querySelector('.viewport');
    const pad = window.innerWidth < 640 ? 8 : 32;
    const k = Math.min((vp.clientWidth - pad) / 1280, (vp.clientHeight - pad) / 720);
    deck.style.transform = 'translate(-50%, -50%) scale(' + k + ')';
  }

  function go(i, push) {
    cur = Math.max(0, Math.min(total - 1, i));
    slides.forEach((s, j) => {
      s.classList.toggle('active', j === cur);
      s.setAttribute('aria-hidden', j === cur ? 'false' : 'true');
    });
    count.textContent = (cur + 1) + ' / ' + total;
    bar.style.width = ((cur + 1) / total) * 100 + '%';
    prev.disabled = cur === 0;
    next.disabled = cur === total - 1;
    if (push !== false) history.replaceState(null, '', '#' + (cur + 1));
  }

  prev.addEventListener('click', () => go(cur - 1));
  next.addEventListener('click', () => go(cur + 1));

  document.addEventListener('keydown', (e) => {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const k = e.key;
    if (['ArrowRight', 'PageDown', ' ', 'Enter'].includes(k) && !(k === 'Enter' && e.target.tagName === 'BUTTON')) {
      if (k === ' ' && e.target.tagName === 'BUTTON') return;
      e.preventDefault(); go(cur + 1);
    } else if (['ArrowLeft', 'PageUp', 'Backspace'].includes(k)) { e.preventDefault(); go(cur - 1); }
    else if (k === 'Home') go(0);
    else if (k === 'End') go(total - 1);
    else if (k === 'f' || k === 'F') toggleFs();
  });

  // 스와이프
  let sx = null, sy = null;
  document.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
  document.addEventListener('touchend', (e) => {
    if (sx === null) return;
    const dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) go(cur + (dx < 0 ? 1 : -1));
    sx = sy = null;
  });

  function toggleFs() {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen && document.documentElement.requestFullscreen();
    else document.exitFullscreen && document.exitFullscreen();
  }
  const fs = document.querySelector('[data-fs]');
  if (fs) fs.addEventListener('click', toggleFs);

  window.addEventListener('resize', fit);
  window.addEventListener('hashchange', () => go(parseInt(location.hash.slice(1), 10) - 1 || 0, false));
  fit();
  go((parseInt(location.hash.slice(1), 10) || 1) - 1, false);
})();

// 퀴즈: <div class="q" data-answer="b" data-explain="..."> 안의 .opts button[data-v]
document.querySelectorAll('.q').forEach((q) => {
  const answer = q.dataset.answer;
  const fb = q.querySelector('.feedback');
  const buttons = q.querySelectorAll('.opts button');
  buttons.forEach((btn) => btn.addEventListener('click', () => {
    const ok = btn.dataset.v === answer;
    buttons.forEach((b) => { b.disabled = true; if (b.dataset.v === answer) b.classList.add('correct'); });
    if (!ok) btn.classList.add('wrong');
    fb.innerHTML = (ok ? '<b class="ok">정답입니다.</b> ' : '<b class="no">다시 생각해 볼까요?</b> ') + q.dataset.explain;
    fb.classList.add('show');
  }));
});

// 토글 비교
document.querySelectorAll('[data-switch]').forEach((wrap) => {
  const buttons = wrap.querySelectorAll('.switch button');
  const panels = wrap.querySelectorAll('[data-panel]');
  const show = (id) => {
    buttons.forEach((b) => b.setAttribute('aria-pressed', b.dataset.target === id));
    panels.forEach((p) => (p.hidden = p.dataset.panel !== id));
  };
  buttons.forEach((b) => b.addEventListener('click', () => show(b.dataset.target)));
  if (buttons[0]) show(buttons[0].dataset.target);
});
