from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index_view(request):
    return render(request, 'core/index.html')

def consulta_ramais_view(request):
    return render(request, 'core/ramais.html')   """Renderiza a página pública de consulta de ramais."""

def autenticacao_ti(request):
    return render(request, 'core/ti.html')  """Renderiza a página de autenticação/login da TI."""

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Pega o usuário autenticado pelo formulário
            user = form.get_user()
            login(request, user)
            # Redireciona usando o nome da rota (name) configurado no urls.py
            return redirect('painel_ti') 
    else:
        form = AuthenticationForm()
    
    return render(request, 'core/ti.html', {'form': form})

@login_required(login_url='login_ti')  # Se não estiver logado, redireciona para a tela de login
def painel_ti_view(request):
    """Renderiza a página protegida do painel de TI."""
    return render(request, 'core/painel.html')