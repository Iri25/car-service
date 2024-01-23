class CardClient:
    """
        Client business object.
    """

    def __init__(self, id_card_client, name, first_name, cnp, date_of_birth, date_of_registration):
        """
            Creates a card client
            :param id_card_client: int, the card id.
            :param name: str, the name
            :param first_name: str, the first name
            :param cnp: int, the cnp
            :param date_of_birth: str, the date of birtth
            :param date_of_registration: str, the date of registration
        """
        self.id_client = id_card_client
        self.name = name
        self.first_name = first_name
        self.cnp = cnp
        self.date_of_birth = date_of_birth
        self.date_of_registration = date_of_registration

    def __str__(self):
        return 'CardClient {}- {},  {}, {}, {}, {}'.format(self.id_client, self.name, self.first_name, self.cnp, self.date_of_birth, self.date_of_registration)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_client == other.id_client and self.name == other.name and self.first_name == other.first_name and self.cnp == other.cnp and self.date_of_birth == other.date_of_birth and self.date_of_registration == other.date_of_registration