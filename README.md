# testando-o-teste

Painel administrativo estático para ser aberto quando o login existente identificar o usuário administrador.

## Admin definido no banco

Use estes dados no banco/seed do login já existente:

- Login: `admin`
- Senha: `admin123`
- Perfil: `admin`
- Redirecionamento após login: `admin.html`

O link **Feed** do menu aponta para `/feed`, para reaproveitar o mesmo feed usado pelo usuário comum.

## Como visualizar

```bash
python3 -m http.server 4173
```

Depois acesse `http://localhost:4173/admin.html`.
