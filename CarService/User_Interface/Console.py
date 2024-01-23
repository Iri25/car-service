from Domain.Card_Client import CardClient
from Domain.Car import Car
from Domain.Transaction import Transaction
from Service.Card_Client_Service import ClientService
from Service.Car_Service import CarService


class Console:

    def __init__(self, carService, clientService, transactionService, carRepository, clientRepository, transactionRepository):
        self.car_service = carService
        self.client_service = clientService
        self.transaction_service = transactionService
        self.car_repository = carRepository
        self.client_repository = clientRepository
        self.transaction_repository = transactionRepository

    def show_menu(self):
        print('1. Cars')
        print('2. Clients')
        print('3. Transactions')
        print('x. Exit')

    def run_console(self):

        while True:
            self.show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.show_cars()
            if op == '2':
                self.show_clients()
            if op == '3':
                self.show_transactions()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    # CARS

    def show_cars(self):

        while True:
            self.show_menu_cars()
            op = input('Optiune: ')
            if op == '1':
                self.handle_cars_add()
            elif op == '2':
                self.handle_cars_remove()
            elif op == '3':
                self.handle_cars_update()
            elif op == '4':
                self.handle_search_cars()
            elif op == '5':
                self.handle_cars_update_guarantee()
            elif op == '6':
                id = int(input("Dati id-ul de cautat: "))
                self.handle_binary_search(id)
            elif op == '7':
                self.handle_permutations_cars()
            elif op == 'a':
                self.handle_cars_show()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def show_menu_cars(self):
        print('     --- Cars ---')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare full text')
        print('5. Actualizare garantie')
        print('6. Binary search')
        print('7. Permutare masini')
        print('a. Afisare')
        print('x. Iesire')

    def handle_cars_add(self):
        try:
            id_car = int(input('ID-ul: '))
            model = input('Modelul: ')
            year_purchase = int(input('Anul achizitiei: '))
            number_km = int(input('Numarul km: '))
            guarantee = int(input('Garantie: '))
            self.car_service.add_car(id_car, model, year_purchase, number_km, guarantee)
            print('Masina a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_cars_remove(self):
        try:
            id_car = int(input('Dati id-ul de sters: '))
            self.car_service.delete(id_car)
            print("Masina a fost stearsa")

        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_cars_update(self):
        try:
            id_car = int(input('Dati id-ul de actualizat: '))
            model = input('Modelul: ')
            year_purchase = int(input('Anul achizitiei: '))
            number_km = int(input('Numarul km: '))
            guarantee = int(input('Garantie: '))
            car = Car(id_car, model, year_purchase, number_km, guarantee)
            self.car_service.update(car)
            print("Masina a fost actualizata!")
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_search_cars(self):
        information = input("Cuvantul de cautat: ")
        l = self.car_service.search_cars(information)
        for m in l:
            print(m)

    def handle_cars_update_guarantee(self):
        try:
            for car in self.car_service.get_all():
                id = self.car_service.update_guarantee(car)
                if id != 0:
                    id_car = car.id_car
                    model = car.model
                    year_purchase = car.year_purchase
                    number_km = car.number_km
                    guarantee = 1
                    car = Car(id_car, model, year_purchase, number_km, guarantee)
                    self.car_service.update(car)
                    print('Garantia a fost actualizata')
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_binary_search(self, id):
        try:
            results = self.car_service.binary_search(id)
            print(results)
        except Exception as ve:
            print('Error: ', ve)

    def handle_permutations_cars(self):
        try:
            a = self.car_service.permutations_cars()
            print(a)
        except Exception as ve:
            print('Error: ', ve)


    def handle_cars_show(self):
        for car in self.car_service.get_all():
            print(car)



    # CLIENTS

    def show_clients(self):

        while True:
            self.show_menu_clients()
            op = input('Optiune: ')
            if op == '1':
                self.handle_clients_add()
            elif op == '2':
                self.handle_clients_remove()
            elif op == '3':
                self.handle_clients_update()
            elif op == '4':
                self.handle_search_clients()
            elif op == '5':
                self.handle_permutations_clients()
            elif op == 'a':
                self.handle_clients_show()
            elif op == 'x':
                break
            else:
                print('Comanda imposibila!')

    def show_menu_clients(self):
        print('     --- Clients ---')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare full text')
        print('5. Permutare clienti')
        print('a. Afisare')
        print('x. Iesire')

    def handle_clients_add(self):
        try:
            id_card_client = int(input('ID-ul: '))
            name = input('Nume: ')
            first_name = input('Prenume: ')
            cnp = int(input('CNP: '))
            date_of_birth = input('Data nasterii: ')
            date_of_registration = input('Data inregistrarii: ')
            self.client_service.add_client(id_card_client, name, first_name, cnp, date_of_birth, date_of_registration)
            print('Clientul a fost adaugat!')
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_clients_remove(self):
        try:
            id_card_client = int(input('Dati id-ul de sters: '))
            self.client_service.delete(id_card_client)
            print("Clientul a fost sters")

        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def handle_clients_update(self):
        try:
            id_card_client = int(input('Dati id-ul de actualizat: '))
            name = input('Nume: ')
            first_name = input('Prenume: ')
            cnp = int(input('CNP: '))
            date_of_birth = input('Data nasterii: ')
            date_of_registration = input('Data inregistrarii: ')
            client = CardClient(id_card_client, name, first_name, cnp, date_of_birth, date_of_registration)
            self.client_service.update(client)
            print("Clientul a fost actualizat!")
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def handle_search_clients(self):
        information = input("Cuvantul de cautat: ")
        la = self.client_service.search_clients(information)
        for m in la:
            print(m)

    def handle_permutations_clients(self):
        try:
            a = self.client_service.permutations_clients()
            print(a)
        except Exception as ve:
            print('Error: ', ve)

    def handle_clients_show(self):
        for client in self.client_service.get_all():
            print(client)

    # TRANSACTIONS

    def show_transactions(self):

        while True:
            self.show_menu_transactions()
            op = input('Optiune: ')
            if op == '1':
                self.handle_transactions_add()
            elif op == '2':
                self.handle_transactions_remove()
            elif op == '3':
                self.handle_transactions_update()
            elif op == '4':
                self.handle_transactions_sum_of_piece_interval()
            #elif op == '5':
            #   self.handle_transactions_sum_of_piece_filter()
            elif op == '6':
                self.handle_transactions_sum_of_work_interval()
            #elif op == '7':
            #   self.handle_transactions_sum_of_work_interval_zip()
            elif op == '8':
                self.handle_ordoner_desc_cars_by_sum_of_work()
            elif op == '9':
                self.handle_ordoner_desc_cars_by_sum_of_work()
            elif op == '10':
                self.handle_ordoner_desc_clients_by_discounts()
            elif op == '11':
                self.handle_ordoner_desc_clients_by_discounts()
            elif op == '12':
                self.handle_ordoner_desc_clients_by_discounts_sort_propre()
            elif op == '13':
                self.handle_remove_transactions()
            elif op == '14':
                self.handle_permutations_transactions()
            elif op == 'a':
                self.handle_transactions_show()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def show_menu_transactions(self):
        print('     --- Transactions ---')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Afisarea tranzactiilor cu suma pieselor cuprinsa intr-un interval')
        # print('5 Afisarea tranzactiilor cu suma pieselor cuprinsa intr-un interval(filter)')
        print('6. Afisarea tranzactiilor cu suma manoperei cuprinsa intr-un interval ')
        #print('7. Afisarea tranzactiilor cu suma manoperei cuprinsa intr-un interval(zip)')
        print('8. Afisarea masinilor descrescator dupa suma manopera')
        print('9.  Afisarea masinilor descrescator dupa suma manopera(lambda)')
        print('10. Afisarea clientiilor descrescator dupa valoarea reducerilor')
        print('11. Afisarea clientiilor descrescator dupa valoarea reducerilor(lambda)')
        print('12. Afisarea clientiilor descrescator dupa valoarea reducerilor(sort propre)')
        print('13. Stergerea tranzactiilor dintr-un interval')
        print('14. Permutare tranzactii')
        print('a. Afisare')
        print('b. Back')

    def handle_transactions_add(self):
        try:
            id = int(input('ID-ul: '))
            id_car = int(input('Id-ul masinii: '))
            id_card_client = int(input('Id-ul clientului: '))
            sum_of_piese = int(input('Suma piese: '))
            sum_of_work = int(input('Suma manopera: '))
            date = input("Data: ")
            hour = input("Ora: ")
            self.transaction_service.add_transaction(id, id_car, id_card_client, sum_of_piese, sum_of_work, date, hour)
            print('Tranzactia a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            print(ve)


    def handle_transactions_remove(self):
        try:
            id = int(input('Dati id-ul de sters: '))
            self.transaction_service.delete(id)
            print("Tranzactia a fost stearsa!")

        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def handle_transactions_update(self):
        try:
            id = int(input('Dati id-ul de actualizat: '))
            id_car = int(input('Id-ul masinei: '))
            id_card_client = int(input('Id-ul clientului: '))
            sum_of_piese = int(input('Suma piese: '))
            sum_of_work = int(input('Suma manopera: '))
            date = input("Data: ")
            hour = input("Ora: ")
            client = Transaction(id, id_car, id_card_client, sum_of_piese, sum_of_work, date, hour)
            self.transaction_service.update(client)
            print("Tranzactia a fost actualizata!")
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_transactions_sum_of_piece_interval(self):
        try:
            a = int(input("Dati capatul inferior: "))
            b = int(input("Dati capatul superioi: "))
            raport = "Tranzactiile care au suma pieselor in intervalul: "
            for transaction in self.transaction_service.get_all():
                if self.transaction_service.sum_of_piece_interval(a, b, transaction.getTranzactieSumaPiese()):
                    raport += str(transaction.getTranzactieId())
                    raport += str(',')
                else:
                    print("Nu apartine intervalui!")
            print(raport)
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_transactions_sum_of_piece_filter(self):
        list = []
        try:
            a = int(input("Dati capatul inferior: "))
            b = int( input("Dati capatul superioi: "))
            transactions = self.transaction_service.get_all
            list  = self.transaction_service.transactions_filter(transactions, a, b)
            print(list)
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_transactions_sum_of_work_interval(self):
        try:
            a = int(input("Dati capatul inferior: "))
            b = int(input("Dati capatul superioi: "))
            raport = "Tranzactiile care au suma manoperei in intervalul: "
            for transaction in self.transaction_service.get_all():
                if self.transaction_service.sum_of_work_interval(a, b, transaction.getTranzactieSumaManopera()):
                    raport += str(transaction.getTranzactieId())
                    raport += str(',')
                else:
                    print('Nu apartine intervalului!')
            print(raport)
        except ValueError as ve:
            print('Erori:')
            print(ve)

    '''
    def handle_transactions_sum_of_work_interval_zip(self):
        try:
            self.transaction_service.sum_of_work_interval_zip()
        except ValueError as ve:
            print('Erori:')
            print(ve)
    '''


    def handle_ordoner_desc_cars_by_sum_of_work(self):
        self.transaction_service.desc_cars_by_sum_of_work()

    def handle_ordoner_desc_clients_by_discounts(self):
        self.transaction_service.desc_clients_by_discounts()

    def handle_ordoner_desc_clients_by_discounts_sort_propre(self):
        self.transaction_service.desc_clients_by_discounts()

    def handle_remove_transactions(self):
        try:
            id = 0
            a = int(input('The first day: '))
            b = int(input('The final day: '))
            for client in self.client_service.get_all():
                id = self.client_service.date(client.date_of_registration, a, b)
                if id != 0:
                    print(id)
                    self.transaction_service.delete(id)
                else:
                    print("Nu exista inregistrare in acest interval!")
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_permutations_transactions(self):
        try:
            a = self.transaction_service.permutations_transactions()
            print(a)
        except ValueError as ve:
            print('Erori:')
            print(ve)

    def handle_transactions_show(self):
        for transaction in self.transaction_service.get_all():
            print(transaction)