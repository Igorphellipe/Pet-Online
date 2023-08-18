from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        reservas = Reserva.objects.filter(data=data).count()
        if data < hoje:
            raise forms.ValidationError('Não é possivel realizar uma reserva para o passado')
        elif reservas > 4:
            raise forms.ValidationError('Não foi possivel fazer reserva para essa data!')
        return reservas


    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho',
            'observacoes'
        ]