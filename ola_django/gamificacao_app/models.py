from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Selo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='selos/') 
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuarios = models.ManyToManyField(User, related_name='selos', blank=True)
    criterio = models.TextField(null=True, blank=True)
    

    
    def __str__(self):
        return self.nome
    
class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_atividade = models.DateField()

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.EmailField(max_length=60, unique=True)
    
    def __str__(self):
        return self.nome

class PessoaSelo(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    selo = models.ForeignKey(Selo, on_delete=models.CASCADE)
    data_ganho = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pessoa.nome} - {self.selo.nome}"

class PessoaAtividade(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    data_realizado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pessoa.nome} - {self.atividade.nome}"

class Calendario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return self.titulo
    
class Transacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.CharField(max_length=50)  
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.valor}"