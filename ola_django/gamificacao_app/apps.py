from django.apps import AppConfig

class GamificacaoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gamificacao_app'

    def ready(self):
       
        from .models import Selo
        criar_selos_iniciais()

def criar_selos_iniciais():

    from .models import Selo  
    selos_iniciais = [
       
        {"nome": "Esforçado Financeiro", "descricao": "Realize 10 transações financeiras para pagar contas ou transferir dinheiro."},
        {"nome": "Especialista Financeiro", "descricao": "Complete todos os módulos educacionais."},
        {"nome": "Poupador Iniciante", "descricao": "Aplique 5% da renda mensal na poupança."},
       
    ]

    for selo_data in selos_iniciais:
        Selo.objects.get_or_create(
            nome=selo_data["nome"],
            descricao=selo_data["descricao"],
        )