# testando-o-teste

Projeto Django unificado com login, cadastro, feed e painel administrativo usando a estrutura correta do repositório.

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd Scripta-testes/scripta
python manage.py runserver
```

Abra `http://127.0.0.1:8000/login/`.

## Login admin

- Matrícula: `202400`
- Senha: `admin123`

Quando entrar com esses dados, o sistema vai direto para o painel administrativo. O admin também consegue acessar o mesmo feed do usuário comum pelo menu **Feed**.

## Estrutura

- `Scripta-testes/templates/` páginas HTML (`login`, `cadastro`, `feed`, `admin`).
- `Scripta-testes/static/css/` estilos.
- `Scripta-testes/static/js/` scripts.
- `Scripta-testes/scripta/usuarios/views.py` lógica de login, cadastro, feed e admin.
