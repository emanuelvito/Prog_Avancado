from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from .models import Equipamento


def index_view(request):
    return render(request, 'core/index.html')


def consulta_ramais_view(request):
    return render(request, 'core/ramais.html')


def autenticacao_ti(request):
    return render(request, 'core/ti.html')

# Simplifica a validação do form usando 'data=request.POST or None'
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('painel_ti')
    
    return render(request, 'core/ti.html', {'form': form})


@login_required(login_url='login_ti')
def painel_ti_view(request):
    erro = None
    if request.method == 'POST':
        # Cria direto no banco; se faltar campo obrigatório ou der duplicidade, cai nas exceções
        try:
            
            Equipamento.objects.create(
                tombo=request.POST.get('tombo'),
                nome_maquina=request.POST.get('nome_maquina'),
                ip_alocado=request.POST.get('ip_alocado'),
                setor=request.POST.get('setor')
            )
            return redirect('painel_ti')
        except IntegrityError:
            erro = 'Este número de tombo já está em uso.'

    context = {
        'equipamentos': Equipamento.objects.all().order_by('-id'),
        'erro': erro
    }
    return render(request, 'core/painel.html', context)


@login_required(login_url='login_ti')
def editar_patrimonio(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    erro = None

    if request.method == 'POST':
        equipamento.tombo = request.POST.get('tombo')
        equipamento.nome_maquina = request.POST.get('nome_maquina')

        # Atualiza IP e setor apenas se vierem preenchidos no formulário
        if ip := request.POST.get('ip_alocado'):
            equipamento.ip_alocado = ip
        if setor := request.POST.get('setor'):
            equipamento.setor = setor

        try:
            equipamento.save()
            return redirect('painel_ti')
        except IntegrityError:
            erro = 'Este número de tombo já está em uso.'

    return render(request, 'core/editar_patrimonio.html', {
        'equipamento': equipamento, 
        'erro': erro
    })


@login_required(login_url='login_ti')
def excluir_patrimonio(request, pk):
    get_object_or_404(Equipamento, pk=pk).delete()
    return redirect('painel_ti')