from Domain.Card_Client import CardClient
from Domain.Car import Car
from Domain.Transaction import Transaction


def test_car():
    c1 = Car(1, 'lamborghini', 2000, 1234, 1)
    assert c1.id_car == 1
    assert c1.model == 'lamborghini'
    assert c1.year_purchase == 2000
    assert c1.number_km == 1234
    assert c1.guarantee == 1


test_car()


def test_client():
    cl1 = CardClient(1, 'Bulai', 'Roxana', 12345, '12.12.1982', '12.12.2008')
    assert cl1.id_client == 1
    assert cl1.name == 'Bulai'
    assert cl1.first_name == 'Roxana'
    assert cl1.cnp == 12345
    assert cl1.date_of_birth == '12.12.1982'
    assert cl1.date_of_registration == '12.12.2008'


test_client()


def test_transaction():
    transaction1 = Transaction(1, 1, 1, 122, 125, '12.12.2009', '12:12')
    assert transaction1.id == 1
    assert transaction1.id_car == 1
    assert transaction1.id_client == 1
    assert transaction1.sum_of_piece == 122
    assert transaction1.sum_of_work == 125
    assert transaction1.date == '12.12.2009'
    assert transaction1.hour == '12:12'

test_transaction()