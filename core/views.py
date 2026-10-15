from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento

def index_view(request):
    return render(request, 'core/index.html')

def consulta_ramais_view(request):
    return render(request, 'core/ramais.html')  

def autenticacao_ti(request):
    return render(request, 'core/ti.html')  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('painel_ti') 
    else:
        form = AuthenticationForm()
    
    return render(request, 'core/ti.html', {'form': form})

@login_required(login_url='login_ti')
def painel_ti_view(request):
    """Gerencia o cadastro, listagem e salvamento dos equipamentos no SQLite."""
    if request.method == 'POST':
        tombo = request.POST.get('tombo')
        nome_maquina = request.POST.get('nome_maquina')
        ip_alocado = request.POST.get('ip_alocado')
        setor = request.POST.get('setor')

        if tombo and nome_maquina and ip_alocado and setor:
            Equipamento.objects.create(
                tombo=tombo,
                nome_maquina=nome_maquina,
                ip_alocado=ip_alocado,
                setor=setor
            )
        return redirect('painel_ti')

    # Busca todos os equipamentos cadastrados no SQLite
    equipamentos = Equipamento.objects.all().order_by('-id')
    
    context = {
        'equipamentos': equipamentos,
    }
    
    return render(request, 'core/painel.html', context)

@login_required(login_url='login_ti')
def editar_patrimonio(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.tombo = request.POST.get('tombo')
        equipamento.nome_maquina = request.POST.get('nome_maquina')
        equipamento.ip_alocado = request.POST.get('ip_alocado')
        equipamento.setor = request.POST.get('setor')
        equipamento.save()
        return redirect('painel_ti')
    
    return render(request, 'core/editar_patrimonio.html', {'equipamento': equipamento})

@login_required(login_url='login_ti')
def excluir_patrimonio(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    equipamento.delete()
    return redirect('painel_ti')