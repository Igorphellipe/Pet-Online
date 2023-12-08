# Criando um django forms para validar dados e transformar em liguagem Python
# Através de dados enviados pelo usário no formulário

#Metodo form.is_valid() -> Verfica se os campos são validos
#Metodo form.as_p() -> gera um HTML desse formulário em forma de TAG p.

from django import forms
from base.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class ReservaPet(forms.Form):
    Nome_do_Pet = forms.CharField()
    Telefone = forms.CharField()
    Dia_Reserva = forms.DateField(help_text='aaaa-mm-dd')
    Observacao = forms.CharField(widget=forms.Textarea)
    