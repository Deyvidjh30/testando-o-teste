const ADMIN_ACCOUNT = {
  matricula: '202400',
  password: 'admin123',
  redirectTo: 'admin.html'
};

const loginForm = document.querySelector('#login-form');
const loginError = document.querySelector('#login-error');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const matricula = document.querySelector('#matricula').value.trim();
  const password = document.querySelector('#password').value.trim();

  if (matricula === ADMIN_ACCOUNT.matricula && password === ADMIN_ACCOUNT.password) {
    window.location.href = ADMIN_ACCOUNT.redirectTo;
    return;
  }

  loginError.textContent = 'Matrícula ou senha inválida.';
});
