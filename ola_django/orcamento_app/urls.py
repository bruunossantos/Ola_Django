from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar-receita/', views.adicionar_receita, name='adicionar_receita'),
    path('adicionar-despesa/', views.adicionar_despesa, name='adicionar_despesa'),
    path('extratos/', views.extratos, name='extratos'),
]
