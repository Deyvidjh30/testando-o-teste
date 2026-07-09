from django.db import connection
from django.shortcuts import redirect, render

ADMIN_MATRICULA = '202400'
ADMIN_SENHA = 'admin123'

USUARIOS_INICIAIS = [
    ('202410', 'Vitor', 'Dança', True),
    ('202411', 'M. Eduarda', 'Roteiro - Figurino', False),
    ('202412', 'Ana Clara', 'Staff', False),
    ('202413', 'João Pedro', 'Comunicação', False),
]


def preparar_banco():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS usuarios_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT UNIQUE NOT NULL,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL DEFAULT '',
                area TEXT NOT NULL DEFAULT 'Staff',
                sub_lider INTEGER NOT NULL DEFAULT 0
            )
            '''
        )
        for matricula, nome, area, sub_lider in USUARIOS_INICIAIS:
            cursor.execute(
                '''
                INSERT OR IGNORE INTO usuarios_usuario (matricula, nome, senha, area, sub_lider)
                VALUES (%s, %s, %s, %s, %s)
                ''',
                [matricula, nome, '123456', area, int(sub_lider)],
            )


def listar_usuarios():
    preparar_banco()
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT id, matricula, nome, area, sub_lider
            FROM usuarios_usuario
            ORDER BY nome
            '''
        )
        return [
            {
                'id': row[0],
                'matricula': row[1],
                'nome': row[2],
                'area': row[3],
                'sub_lider': bool(row[4]),
            }
            for row in cursor.fetchall()
        ]


def login_view(request):
    preparar_banco()
    erro = ''

    if request.method == 'POST':
        matricula = request.POST.get('matricula', '').strip()
        senha = request.POST.get('senha', '').strip()

        if matricula == ADMIN_MATRICULA and senha == ADMIN_SENHA:
            request.session['usuario_logado'] = {'matricula': matricula, 'admin': True}
            return redirect('admin_panel')

        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT id FROM usuarios_usuario WHERE matricula = %s AND senha = %s',
                [matricula, senha],
            )
            usuario = cursor.fetchone()

        if usuario:
            request.session['usuario_logado'] = {'matricula': matricula, 'admin': False}
            return redirect('feed')

        erro = 'Matrícula ou senha inválida.'

    return render(request, 'login.html', {'erro': erro})


def cadastro_view(request):
    preparar_banco()
    erro = ''

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        matricula = request.POST.get('matricula', '').strip()
        senha = request.POST.get('senha', '').strip()

        if nome and matricula.isdigit() and senha:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        '''
                        INSERT INTO usuarios_usuario (matricula, nome, senha, area, sub_lider)
                        VALUES (%s, %s, %s, %s, 0)
                        ''',
                        [matricula, nome, senha, 'Staff'],
                    )
                return redirect('login')
            except Exception:
                erro = 'Essa matrícula já está cadastrada.'
        else:
            erro = 'Preencha nome, matrícula numérica e senha.'

    return render(request, 'cadastro.html', {'erro': erro})


def feed_view(request):
    usuario = request.session.get('usuario_logado')
    if not usuario:
        return redirect('login')

    return render(request, 'feed.html', {'usuario': usuario})


def admin_panel_view(request):
    usuario = request.session.get('usuario_logado')
    if not usuario or not usuario.get('admin'):
        return redirect('login')

    preparar_banco()

    if request.method == 'POST':
        acao = request.POST.get('acao')
        matricula = request.POST.get('matricula', '').strip()

        if acao == 'promover':
            area = request.POST.get('area', 'Staff')
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE usuarios_usuario SET area = %s, sub_lider = 1 WHERE matricula = %s',
                    [area, matricula],
                )
        elif acao == 'remover':
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM usuarios_usuario WHERE matricula = %s', [matricula])

        return redirect('admin_panel')

    usuarios = listar_usuarios()
    return render(request, 'admin.html', {'usuarios': usuarios, 'total_usuarios': len(usuarios)})
