import pytest
import datetime
from model_bakery import baker
from base.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

#Teste de Serializer para verificar as validações postas nos serializers
@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop = baker.make(Petshop)
    return {
        'nome_do_pet': 'nome teste', 'telefone': '61982074534',
        'dia_da_reserva': ontem, 'observacao': 'Helo', 'petshop': petshop.pk
    }

@pytest.mark.django_db
def test_data_agendamento_invalido(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
    assert not serializer.is_valid()