from django.shortcuts import redirect, render

ADMIN_MATRICULA = '202400'
ADMIN_SENHA = 'admin123'

USUARIOS = [
    {'matricula': '202410', 'nome': 'Vitor', 'area': 'Dança', 'sub_lider': True},
    {'matricula': '202411', 'nome': 'M. Eduarda', 'area': 'Roteiro - Figurino', 'sub_lider': False},
    {'matricula': '202412', 'nome': 'Ana Clara', 'area': 'Staff', 'sub_lider': False},
    {'matricula': '202413', 'nome': 'João Pedro', 'area': 'Comunicação', 'sub_lider': False},
]


def login_view(request):
    erro = ''
    if request.method == 'POST':
        matricula = request.POST.get('matricula', '').strip()
        senha = request.POST.get('senha', '').strip()

        if matricula == ADMIN_MATRICULA and senha == ADMIN_SENHA:
            request.session['usuario_logado'] = {'matricula': matricula, 'admin': True}
            return redirect('admin_panel')

        request.session['usuario_logado'] = {'matricula': matricula, 'admin': False}
        return redirect('feed')

    return render(request, 'login.html', {'erro': erro})


def cadastro_view(request):
    return render(request, 'cadastro.html')


def feed_view(request):
    return render(request, 'feed.html')


def admin_panel_view(request):
    usuario = request.session.get('usuario_logado')
    if not usuario or not usuario.get('admin'):
        return redirect('login')

    return render(request, 'admin.html', {'usuarios': USUARIOS, 'total_usuarios': len(USUARIOS)})
