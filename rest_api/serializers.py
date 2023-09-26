from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import Reserva, Contato
import datetime as dt



class AgendamentoModelSerializer(ModelSerializer):

    def validate_dia_da_reserva(self, value):
        if value < dt.date.today():
            raise serializers.ValidationError('A data deve ser no futuro')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'

class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
        