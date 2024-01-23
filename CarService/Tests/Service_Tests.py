from Domain.Card_Client import CardClient
from Domain.Car import Car
from Domain.Transaction import Transaction


def test_add_car():
    car1 = Car(1, 'lamborghini', 2008, 1234, 1)
    assert car1.id_car == 1
    assert car1.year_purchase == 2008
    assert car1.model == "lamborghini"
    assert car1.number_km == 1234
    assert car1.guarantee == 1

test_add_car()


def test_add_client():
    client1 = CardClient(1, 'a', 'b', 123456, '12.12.2012', '13.09.2009')
    assert client1.id_client == 1
    assert client1.name == 'a'
    assert client1.first_name == 'b'
    assert client1.cnp == 123456
    assert client1.date_of_birth == '12.12.2012'
    assert client1.date_of_registration == '13.09.2009'

test_add_client()


def test_add_transaction():
    transaction1 = Transaction(1, 1, 1, 13, 14, '12.12.2012', '12:12')
    assert transaction1.id == 1
    assert transaction1.sum_of_piece == 13
    assert transaction1.sum_of_work == 14
    assert transaction1.id_client == 1
    assert transaction1.id_car == 1
    
test_add_transaction()