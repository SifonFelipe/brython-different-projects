const toggle = document.querySelector('.theme-toggle');

if (toggle) {
  const updateButton = () => {
    const theme = document.documentElement.dataset.theme || 'light';
    toggle.setAttribute('aria-pressed', String(theme === 'dark'));
    toggle.querySelector('.theme-label').textContent = theme === 'dark' ? 'Light' : 'Dark';
  };

  updateButton();
  toggle.addEventListener('click', () => {
    const next = (document.documentElement.dataset.theme || 'light') === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    localStorage.setItem('theme', next);
    updateButton();
  });
}
