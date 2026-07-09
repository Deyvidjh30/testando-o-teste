# testando-o-teste

Painel administrativo com a estrutura de páginas separada em `templates`, `static/css` e `static/js`.

## Login admin definido

Use estes dados para entrar como administrador:

- Matrícula: `202400`
- Senha: `admin123`
- Página após login: `templates/admin.html`

O login usa matrícula, não nome. O link **Feed** do menu administrativo aponta para `/feed`, para reaproveitar o mesmo feed usado pelo usuário comum.

## Estrutura

- `templates/login.html`
- `templates/admin.html`
- `static/css/login.css`
- `static/css/admin.css`
- `static/js/login.js`
- `static/js/admin.js`

## Como visualizar

```bash
python3 -m http.server 4173
```

Depois acesse `http://localhost:4173/templates/login.html`.
