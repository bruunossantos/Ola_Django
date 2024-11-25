from django.shortcuts import render, redirect
from django.db.models import Sum  # Importação correta do Sum
from .models import Receita, Despesa  # Importando os modelos corretamente

def home(request):
    total_receitas = Receita.objects.aggregate(Sum('valor'))['valor__sum'] or 0  # Corrigido para Sum
    total_despesas = Despesa.objects.aggregate(Sum('valor'))['valor__sum'] or 0  # Corrigido para Sum
    saldo = total_receitas - total_despesas

    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo
    }

    return render(request, 'orcamento_app/home.html', context)  # Caminho ajustado para orcamento_app/

def adicionar_receita(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        data = request.POST['data']
        Receita.objects.create(descricao=descricao, valor=valor, data=data)
        return redirect('home')
    return render(request, 'orcamento_app/adicionar_receita.html')  # Caminho ajustado para orcamento_app/

def adicionar_despesa(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        data = request.POST['data']
        Despesa.objects.create(descricao=descricao, valor=valor, data=data)
        return redirect('home')
    return render(request, 'orcamento_app/adicionar_despesa.html')  # Caminho ajustado para orcamento_app/

from django.shortcuts import render
from .models import Receita, Despesa  # Certifique-se de ter modelos para receitas e despesas

def extratos(request):
    receitas = Receita.objects.all()
    despesas = Despesa.objects.all()
    return render(request, 'orcamento_app/extratos.html', {'receitas': receitas, 'despesas': despesas})

