import pytest
from datetime import date
from rest_framework.test import APIClient
from model_bakery import baker
from base.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer

#Teste para verificar se a API retorna os petshops
@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len (resposta.data['results']) == 0

#Teste para verifcar se a API retorna os agendamentos 
@pytest.fixture
def agendamento():
    return baker.make(Reserva)

@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agenda')
    assert len(resposta.data['results']) == 1 

#Teste para verificar criação de agendamento, colocado o metodo de force.Authenticate
#para força a autenticação na API e criar um agendamento.

@pytest.fixture
def dados_agendamento():
    hoje = date.today()
    petshop = baker.make(Petshop)
    return {
        'nome_do_pet': 'Teste View', 'telefone': '61920584484', 
        'dia_da_reserva': hoje, 'observacao': 'Hello World', 'petshop': petshop.pk,
    }

#fixture criada para simular autenticação de usuário na API para criar uma reserva.
@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agenda', dados_agendamento)
    assert resposta.status_code == 201

