from Domain.Car import Car
from Domain.Card_Client import CardClient
from Domain.Transaction import Transaction
from Repository.Car_Repository import CarRepository
from Repository.Card_Client_Repository import ClientRepository
from Repository.Transaction_Repository import TransactionRepository
from Service.Car_Service import CarService
from Service.Card_Client_Service import ClientService
from Service.Transaction_Service import TransactionService
from User_Interface.Console import Console

def zip_for_carRepository(carRepository):
    list_id = [1, 2, 3, 4, 5]
    list_nume = ["lamburghini", "ferrari", "dacia", "lamburghini", "dacia"]
    list_an = [2015, 2018, 2019, 2019, 2018]
    list_km = [12349000, 1234, 12345, 1234225, 12345555]
    list_garantie = [0, 0, 0, 1, 0]
    list = zip(list_id, list_nume, list_an, list_km, list_garantie)
    for id, nume, an, km, garantie in list:
        carRepository.add(Car(id, nume, an, km, garantie))
        print(Car(id, nume, an, km, garantie))
    #print(carRepository.get_all())
    #for i in carRepository.get_all():
    #   print(i)


def populate(carRepository, clientRepository, transactionRepository):
    """carRepository.add(Car(1, 'lamborghini', 2015, 12349000, 0))
    carRepository.add(Car(2, 'ferrari', 2018, 1234, 0))
    carRepository.add(Car(3, 'dacia', 2019, 12345, 0))
    carRepository.add(Car(4, 'lamborghini', 2019, 1234225, 1))
    carRepository.add(Car(5, 'dacia', 2018, 12345555, 0))"""

    zip_for_carRepository(carRepository)
    print("---------------------------")

    clientRepository.add(CardClient(1, 'a', 'b', 1234223522, '9.12.2002', '1.09.2019'))
    clientRepository.add(CardClient(2, 'd', 'c', 1111117265, '12.12.2002', '11.09.2019'))
    clientRepository.add(CardClient(3, 'e', 'f', 1000032312, '6.12.2002', '4.04.2014'))
    clientRepository.add(CardClient(4, 'h', 'm', 1444433232, '6.12.2000', '4.04.20019'))
    clientRepository.add(CardClient(5, 'n', 'o', 1999233232, '6.12.20013', '4.04.2014'))

    transactionRepository.add(Transaction(1, 1, 1, 13, 14, '9.12.2012', '19:12'))
    transactionRepository.add(Transaction(3, 2, 2, 73, 56, '12.12.2012', '17:12'))
    transactionRepository.add(Transaction(5, 3, 3, 19, 88, '17.12.2012', '8:12'))
    transactionRepository.add(Transaction(6, 4, 4, 19, 50, '10.12.2012', '20:10'))
    transactionRepository.add(Transaction(7, 5, 5, 19, 50, '6.12.2012', '12:12'))




def main():
    
    carRepository = CarRepository()
    clientRepository = ClientRepository()
    transactionRepository = TransactionRepository()

    carService = CarService(carRepository)
    clientService = ClientService(clientRepository, transactionRepository)
    transactionService = TransactionService(transactionRepository, carRepository, clientRepository)
    populate(carRepository,clientRepository,transactionRepository)
    #zip_for_carRepository(carRepository)
    console = Console(carService, clientService, transactionService, carRepository, clientRepository, transactionRepository)

    console.run_console()
main()