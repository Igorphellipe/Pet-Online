from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    mensagem = models.TextField(verbose_name='Mensagem')
    data = models.DateTimeField(verbose_name='Data Envio', auto_now_add=True)
    lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)

    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Fomulário de Contato'
        verbose_name_plural = 'Fomulários de Contatos'
        ordering = ['-data']


class Reserva(models.Model):
    nome_do_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    dia_da_reserva = models.DateField(auto_now_add=True)
    observacao = models.TextField()
