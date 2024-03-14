from pytest_django.asserts import assertTemplateUsed
import pytest
from datetime import date, timedelta
from reserva.models import Reserva
#Teste para verificar se a View retornar o template esperado quando feito GET
def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')

#Teste para verificar se o envio de dados retorna SUCESSO
@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client):
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'nome_pet': 'Jerry',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'O Jerry está muito sujo'
    }
    response = client.post('criar_reserva', dados)

    assert response.status_code == 200
    #assert 'Reserva realizada com sucesso' in str(response.content)


#Teste para verificar se os dados enviados para o BD foram realmente salvos 
@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client):
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'Fred',
        'email': 'fred@email.com',
        'nome_pet': 'Filó',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 1,
        'observacoes': 'A filó está muito suja!'
    }
    client.post ('/reserva/', dados)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados['nome']
    assert reserva.nome_pet == dados['nome_pet']

#Fixture criada para armazenar dados do dicionario criado para enviar informçoes ao BD
@pytest.fixture
def dados_validos():
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'fred',
        'email': 'fred@email.com',
        'nome_pet': 'Filó',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'Filó está muito suja!'
    }
    return dados

#Teste para verificar resposta da URL e se os dados estão sendo enviados corretamente para BD
@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, dados_validos):
    response = client.post('/reserva/', dados_validos)

    assert response.status_code == 200
    assert 'Reserva realizada com sucesso' in str (response.content)


@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
    client.post('/reserva/', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']
    assert reserva.nome_pet == dados_validos['nome_pet']



#teste para verificar se a validação de Reserva está funcioando
#O sistema não pode aceitar reservas para datas anteriores
@pytest.mark.django_db
def test_reserva_datas_anteriores(client):
    dia = date.today() - timedelta(days=1) #data atual -1 dia.
    dados = {
        'nome': 'Simba',
        'email': 'simba@email.com',
        'nome_pet': 'Jorginho',
        'data': dia, #data com dia anterior ao oficial para verificar se o sistema faz a reserva
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'Jorginho está muito sujo'
    }
    response = client.post('/reserva/', dados)

    assert response.status_code == 200
    assert Reserva.objects.all().count() == 0