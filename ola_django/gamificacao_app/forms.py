from django import forms
from .models import Selo,Transacao

class SeloForm(forms.ModelForm):
    class Meta:
        model = Selo
        fields = ["nome","descricao","imagem"]
        
class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['tipo', 'valor']
        