from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_selos, name='home'),  
    path('selos/', views.listar_selos, name='listar_selos'),
    path('selos/adicionar/', views.adicionar_selo, name='adicionar_selo'),
    path('transacoes/criar/', views.criar_transacao, name='criar_transacao'),
    path('transacoes/', views.listar_transacoes, name='listar_transacoes'),
]
