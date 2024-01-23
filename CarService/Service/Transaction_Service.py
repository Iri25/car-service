from Domain.Transaction import Transaction
from Repository.Car_Repository import CarRepository
from Repository.Card_Client_Repository import ClientRepository

class TransactionService:
    """
        Manages transaction logic.
    """
    def __init__(self, transactionRepository, carRepository, clientRepository):
        """
            Creates a location service.
        """
        self.transactionRepository = transactionRepository
        self.carRepository = carRepository
        self.clientRepository = clientRepository

    def get_all(self):
        return list(self.transactionRepository.get_all().values())

    def add_transaction(self, id, id_car, id_card_client, sum_of_piece, sum_of_work, date, hour):
        """
            Creates a transaction
            :param id_transaction: int, the transaction id.
            :param id_car: int, the car id
            :param id_card_client: int, the client id
            :param sum_of_piece: int, the amount of piece
            :param sum_of_work: int, the amount of work
            :param date: str, the date
            :param hour: str, the hour
        """

        errors = []
        if id in self.transactionRepository.get_all():
            errors.append('Exista deja o tranzactie cu id-ul {}'.format(id))

        if errors != []:
            raise ValueError(errors)


        c = self.clientRepository.get_id(id_card_client)
        if c != None:
            c.sum_of_work = 0.9 * sum_of_work
        elif c == None:
            errors.append("Nu exista clientul!")
        else:
            c = 0

        m = self.carRepository.get_ID(id_car)
        if m == None:
            errors.append("Nu exista masina!")
        else:
            if m.guarantee == 1:
                self.sum_of_piece = 0
        if errors != []:
            raise ValueError(errors)


        transaction = Transaction(id, id_car, id_card_client, sum_of_piece, sum_of_work, date, hour)
        self.transactionRepository.add(transaction)

    def update(self, transaction):
        '''
            Updates transaction.
            :param transaction_id: the car to update
            :return: -
        '''
        id = transaction.id
        if id not in self.transactionRepository.storage.keys():
            raise KeyError('There is no car with that id!')
        self.transactionRepository.add(transaction)

    def delete(self, id_car):
        '''
            :param car_id: the car id to delete.
            :return: -
            :raises KeyError: if no car with car_id
        '''
        if id_car not in self.transactionRepository.storage.keys():
            raise KeyError('There is no car with that id!')
        del self.transactionRepository.storage[id_car]

    def sum_of_piece_interval(self, a, b, sum):
        """
            Check if sum of piece is between a and b
            :param a: the initial member
            :param b: the final member
            :return: -
        """
        if a < sum and sum < b:
            return True
        return False

    def sum_of_work_interval(self, a, b, sum):
        """
            Check if sum of work is between a and b
            :param a: the initial member
            :param b: the final member
            :return: -
        """
        if a < sum and sum < b:
            return True
        return False

    def desc_cars_by_sum_of_work(self):
        transaction_list = self.get_all()
        #for l in transaction_list:
        #print(l)
        transaction_list = sorted(self.get_all(), key=lambda t: t.sum_of_work, reverse=True)
        # tlist = tlist.sort( key t.suma_manopera, reverse = True)
        l = []
        for t in transaction_list:
            l.append(self.carRepository.get_ID(t.id_car))
        for m in l:
            print(m)
        return l

    def desc_clients_by_discounts(self):
        transaction_list = self.get_all()
        #for m in transaction_list:
        #print(m)
        lista = []
        for t in transaction_list:
            #if t.id_client != 0:
            lista.append(t)
        lista = sorted(transaction_list, key=lambda t: t.sum_of_work, reverse=True)
        l = []
        for t in lista:
            l.append(self.clientRepository.get_id(t.id_client))
        for m in l:
            print(m)
        return l

    def remove_transactions(self, a, b, date):
        if a < date and date < b:
            del self.transactionRepository.storage[id]

    def verification_transaction_interval(self, transaction, a, b):
        if a < transaction.sum_of_piece < b:
            return True
        else:
            return False


    def transactions_filter(self, transactions, a, b):
        list = []
        f = []
        for transaction in transactions:
            list = list + self.verification_transaction_interval()
            f = filter(list, transactions)
            return f



        
    def permutations_transactions(self):
        transactions = self.get_all()
        result = []
        n = len(transactions)
        ids_of_transactions = []
        for transaction in transactions:
            ids_of_transactions.append(transaction.id)

        def inner(current_permutation):
            if len(current_permutation) == n:
                result.append(current_permutation)
                return

            for i in range(0, n):
                if ids_of_transactions[i] not in current_permutation:
                    inner(current_permutation + [ids_of_transactions[i]])

        inner([])
        return result
    
    def sort_propre(self):
        '''
        Sorts the customer cards by the number of points from highest to smallest
        :return: a list with the sorted cards
        '''

        clients = self. get_all()
        a = []
        result = []
        for client in clients:
            a.append(client)
        for i in range(1, len(a)):
            for j in range(i):
                if int(a[i].sum_of_work) > int(a[j].sum_of_work):
                    a.insert(j, a[i])
                    del a[i+1]
        for dic in a:
            result.append(dic.__str__())
        return result