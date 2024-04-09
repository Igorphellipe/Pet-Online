# Criando um django forms para validar dados e transformar em liguagem Python
# Através de dados enviados pelo usário no formulário

#Metodo form.is_valid() -> Verfica se os campos são validos
#Metodo form.as_p() -> gera um HTML desse formulário em forma de TAG p.

from django import forms
from base.models import Contato, Reserva
from datetime import date

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class ReservaPet(forms.ModelForm):

    def clean_dia_da_reserva(self):
        dia_da_reserva = self.cleaned_data['dia_da_reserva']
        hoje = date.today()
        dat = Reserva.objects.filter(dia_da_reserva=dia_da_reserva).count()
        if dat >= 4:
            raise forms.ValidationError('Não é possivel realizar reserva')
        elif dia_da_reserva < hoje:
            raise forms.ValidationError('Não é possivel realizar uma reserva para o passado')
        return dia_da_reserva
     
    class Meta:
        model = Reserva
        fields = ['nome_do_pet', 'telefone', 'dia_da_reserva', 'petshop', 'porte_animal', 'observacao']