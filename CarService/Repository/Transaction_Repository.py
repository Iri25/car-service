from Domain.Transaction import Transaction

class TransactionRepository():
    def __init__(self):
        self.storage = {}

    def add(self, tranzactie):
        self.storage[tranzactie.getTranzactieId()] = tranzactie

    def get_all(self):
        return self.storage

    def get_sum_of_work(self, sum_of_work):
        if sum_of_work in self.storage:
            return self.storage[sum_of_work]
        return None

    def get_sum_of_piece(self, sum_of_piece):
        if sum_of_piece in self.storage:
            return self.storage[sum_of_piece]
        return None
    def id_client(self):
        return self.id_client


