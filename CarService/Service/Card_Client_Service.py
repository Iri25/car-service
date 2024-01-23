from Domain.Card_Client import CardClient


class ClientService:
    """
        Manages clientd client logic.
    """
    def __init__(self, clientRepository, transactionRepository):
        """
                Creates a clientd client service.
        """
        self.clientRepository = clientRepository
        self.transactionRepository = transactionRepository

    def add_client(self, id_card_client, name, first_name, cnp, date_of_birth, date_of_registration):
        """
            Creates a card client:
            :param id_card_client: int, id ul clientului.
            :param name: str, numele clientului
            :param first_name: int, prenumele clientului
            :param cnp: int, CNP-UL client
            :param date_of_birth: int, data nasterii
            :param date_of_registration: int, data inregistrarii
       """

        errors = []
        if id_card_client in self.clientRepository.get_all():
            errors.append('Exista deja un client cu id-ul {}'.format(id_card_client))

        '''if cnp in self.get_cnp():
            errors.append('Exista deja un client cu cnp-ul {}'.format(cnp))'''


        client = CardClient(id_card_client, name, first_name, cnp, date_of_birth, date_of_registration)
        clients = self.get_all()
        cnps = map(lambda client: client.cnp, clients)
        if client.cnp in cnps:
            errors.append('Exista deja un client cu acest CNP')

        if errors != []:
            raise ValueError(errors)
        client = CardClient(id_card_client, name, first_name, cnp, date_of_birth, date_of_registration)
        self.clientRepository.add(client)

    def get_cnp(self):
        lista = []
        for client in self.clientRepository.get_all():
            lista.append(client.cnp)
        return lista

    def update(self, client):
        '''
           Updates client.
           :param client: the client to update
           :return: -
           :raises: KeyError if the id does not exist
       '''
        id_client = client.id_client
        if id_client not in self.clientRepository.get_all():
            raise KeyError('There is no client with that id!')
        self.clientRepository.update(client)

    def delete(self, id_card_client):
        """
            Deletes a clientd.
            :param id_clientd_client: id ul clientdului de sters
            :return: -
            :raises KeyError: if no client with id_clientd_client
        """
        if id_card_client not in self.clientRepository.storage.keys():
              raise KeyError('There is no client with that id!')
        del self.clientRepository.storage[id_card_client]

    def get_all(self):
        return list(self.clientRepository.get_all().values())

    def search_clients(self, search_information):
        """
            Cauta un obiect in clasa studenti.
            :param object_client:
            :return: lista cu obiectele cliente corespund cu obiect_client
        """

        lista = []
        for object_client in self.get_all():
            '''s = str(object_client.id_card_client)
            r = s.find(search_information)
            if r != -1:
                lista.append(object_client)'''

            s = object_client.name
            r = s.find(search_information)
            if r != -1:
                lista.append(object_client)

            s = object_client.first_name
            r = s.find(search_information)
            if r != -1:
                lista.append(object_client)

            s = str(object_client.cnp)
            r = s.find(search_information)
            if r != -1:
                lista.append(object_client)

            s = object_client.date_of_birth
            r = s.find(search_information)
            if r != -1:
                lista.append(object_client)

            s = object_client.date_of_registration
            r = s.find(search_information)
            if r != -1:
                lista.append(object_client)
        return lista
        '''
        list = []
        for object_client in self.clientRepository.get_all():
            if object_client in object_client.id_client:
                list.append(object_client)
            elif object_client in object_client.name:
                list.append(object_client)
            elif object_client in object_client.first_name:
                list.append(object_client)
            elif object_client in object_client.cnp:
                list.append(object_client)
            elif object_client in object_client.date_of_birth:
                list.append(object_client)
            elif object_client in object_client.date_of_registration:
                list.append(object_client)
        return list'''


    def handle_cliens_disc(self):
        return sorted(self.get_all(), key=lambda transaction: transaction.getTranzactieSumaManopera(), reverse=True)

    def date(self, date_of_registration, a, b):
        idclient = 0
        id = 0
        x = date_of_registration.split('.')
        day = x[0]
        if a < int(day) and int(day) < b:
            for client in self.get_all():
                if client.date_of_registration is date_of_registration:
                    idclient = client.id_client
                    for transaction in self.transactionRepository.get_all():
                        if idclient == transaction.id_client:
                           id = transaction.id_client
        return id

    def permutations_clients(self):
        clients = self.get_all()
        result = []
        n = len(clients)
        ids_of_clients = []
        for client in clients:
            ids_of_clients.append(client.id_client)

        def inner(current_permutation):
            if len(current_permutation) == n:
                result.append(current_permutation)
                return

            for i in range(0, n):
                if ids_of_clients[i] not in current_permutation:
                    inner(current_permutation + [ids_of_clients[i]])

        inner([])
        return result