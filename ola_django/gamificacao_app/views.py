from django.shortcuts import render, redirect
from .models import Selo,Transacao
from .forms import SeloForm,TransacaoForm

def listar_selos(request):
    selos = Selo.objects.filter(usuarios=request.user)  
    return render(request, 'listar_selos.html', {'selos': selos})

def adicionar_selo(request):
    if request.method == 'POST':
        form = SeloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_selos')
    else:
        form = SeloForm()
    return render(request, 'adicionar_selo.html', {'form': form})

def verifica_concede_selo(usuario, criterio):

    if criterio == "transacoes_10":
        transacoes_contagem = Transacao.objects.filter(usuario=usuario).count()
        if transacoes_contagem >= 10:
            selo = Selo.objects.get(nome="Esforçado Financeiro")
            if not selo.usuarios.filter(id=usuario.id).exists():
                selo.usuarios.add(usuario)
                return f"Selo '{selo.nome}' conquistado!"
   
    return "Critérios não atendidos"


def criar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.usuario = request.user  
            transacao.save()
            
       
            mensagem = verifica_concede_selo(request.user)
            
            
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm()
    return render(request, 'criar_transacao.html', {'form': form})

def listar_transacoes(request):
   
    transacoes = Transacao.objects.filter(usuario=request.user) 
    return render(request, 'listar_transacoes.html', {'transacoes': transacoes})