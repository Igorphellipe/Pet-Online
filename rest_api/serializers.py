from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from base.models import Reserva, Contato, Petshop, PorteAnimal
import datetime as dt



class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )
    class Meta:
        model = Petshop
        fields = '__all__'

class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'


class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data


class PorteAnimalModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )
    class Meta:
        model = PorteAnimal
        fields = '__all__'
    

class PorteAnimalNestedModelSerializer(ModelSerializer):
    class Meta:
        model = PorteAnimal
        fields = '__all__'    

class PorteAnimalRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PorteAnimalNestedModelSerializer
        super().__init__(**kwargs)
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    


class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )
    porte = PorteAnimalRelatedFieldCustomSerializer(
        queryset=PorteAnimal.objects.all(),
        read_only=False)

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

