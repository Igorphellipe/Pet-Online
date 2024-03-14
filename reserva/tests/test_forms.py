import pytest

from reserva.forms import ReservaForm

#Teste de formulario, verifica se todos os dados obedecendo as regras do formulário.
@pytest.mark.django_db
def test_validacao_de_formulario():
    data = {
        'nome': 'Joaquim',
        'email': 'joa@email.com',
        'nome_pet': 'Zeus',
        'data': '2024-03-15',
        'turno': 'tarde',
        'tamanho': 2,
        'observacoes': 'Zeus muito bravo'
    }

    form = ReservaForm(data=data)
    assert form.is_valid()

#Teste para verificar se o formulario e invalido se o campo nome estiver em branco.
@pytest.mark.django_db
def test_verfica_nome_no_formulario():
    data = {
        'nome': '',
        'email': 'joa@email.com',
        'nome_pet': 'Zeus',
        'data': '2024-01-17',
        'turno': 'tarde',
        'tamanho': 2,
        'observacoes': 'Zeus muito bravo'
    }

    form = ReservaForm(data=data)
    assert not form.is_valid()

    assert 'nome' in form.errors


#Teste para verificar se o formulario não e valido se o campo data estiver vazio
@pytest.mark.django_db
def test_verifica_data_formulario():
    data = {
        'nome': 'José',
        'email': 'joa@email.com',
        'nome_pet': 'Zeus',
        'data': '',
        'turno': 'tarde',
        'tamanho': 2,
        'observacoes': 'Zeus muito bravo'
    }

    form = ReservaForm(data=data)
    assert not form.is_valid()

    assert 'data' in form.errors