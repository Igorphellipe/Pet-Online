import pytest
from datetime import date, timedelta
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


#Teste para recuperar um agendamento especifico na API
@pytest.mark.django_db
def test_buscar_agendamento_id(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agenda/1')
    assert resposta.status_code == 200 



#Fixture para armazenar dados para atualizar o agendamento
@pytest.fixture
def dados_agendamento_atualizado():
    hoje = date.today() + timedelta(days=1)
    petshop = baker.make(Petshop)
    return {
        'nome_do_pet': 'Teste API', 'telefone': '6192076868', 
        'dia_da_reserva': hoje, 'observacao': 'Bom Dia', 'petshop': petshop.pk,
    } 

#Teste para atualizar um Agendamento com ID especifica 
@pytest.mark.django_db
def test_atualizar_agendamento_id(agendamento, usuario, dados_agendamento_atualizado):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.put('/api/agenda/1', dados_agendamento_atualizado)
    assert resposta.status_code == 200


#Teste para deletar um agendamento com ID definido
@pytest.mark.django_db
def test_deletar_agendamento_id(agendamento, usuario):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.delete('/api/agenda/1')
    assert resposta.status_code == 204