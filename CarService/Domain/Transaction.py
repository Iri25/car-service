class Transaction:
    """
        Transaction business object.
    """
    def __init__(self, id, id_car, id_card_client, sum_of_piece, sum_of_work, date, hour):
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
        self.id = id
        self.id_car = id_car
        self.id_client = id_card_client
        self.sum_of_piece = sum_of_piece
        self.sum_of_work = sum_of_work
        self.date = date
        self.hour = hour

    def __str__(self):
        return 'Transaction {}- {}, {}, {}, {}, {}, {}'.format(self.id, self.id_car, self.id_client, self.sum_of_piece, self.sum_of_work, self.date, self.hour)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id == other.id and self.id_car == other.id_car and self.id_client == other.id_client and self.sum_of_piece == other.sum_of_piece and self.sum_of_work == other.sum_of_work and self.date == other.date and self.hour == other.hour

    def getTranzactieId(self):
        return self.id

    def getTranzactieSumaPiese(self):
        return self.sum_of_piece

    def getTranzactieSumaManopera(self):
        return self.sum_of_work
