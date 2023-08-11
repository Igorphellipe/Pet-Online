from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class Reserva(models.Model):
    nome_do_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    dia_da_reserva = models.DateField(auto_now_add=True)
    observacao = models.TextField()
    