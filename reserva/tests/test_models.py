from datetime import date   

import pytest
from model_bakery import baker

from reserva.models import Reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada():
    data = date(2024, 1, 11)
    reserva = baker.make(
        Reserva,
        nome ='Jerry',
        data = data,
        turno = 'tarde'
    )

    assert str(reserva) == 'Jerry: 2024-01-11 - tarde'




'''from base.models import Petshop, Reserva
@pytest.mark.django_db
def test_qtd_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 3
    baker.make(
        Reserva,
        quantidade,
        petshop=petshop
    )

    assert petshop.qtd_reservas() == 3
'''

@pytest.fixture
def reserva():
    data = date(2024, 1, 11)
    reserva = baker.make(
        Reserva,
        nome = 'Jerry',
        data = data,
        turno = 'manhã' 
    )
    return reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Jerry: 2024-01-11 - manhã'
    