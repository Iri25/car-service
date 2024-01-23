class ClientRepository():
    def __init__(self):
        """
            Creates a car service.
        """
        self.storage = {}

    def add(self, client):
        self.storage[client.id_client] = client

    def update(self, client):
        self.storage[client.id_client] = client

    def get_all(self):
        return self.storage

    def get_ID(self, id_card_client):
        if id_card_client in self.storage:
            return self.storage[id_card_client]
        return None

    def get_id(self, id_card_client):
        """
            if self.storage[id_card_client] == None:
                return None
            else:
                return self.storage[id_card_client]
        """

        if id_card_client in self.storage.keys():
            return self.storage[id_card_client]
        else:
            return None