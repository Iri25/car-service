class CarRepository():
    def __init__(self):
        """
            Creates a car service.
        """
        self.storage = {}

    def add(self, car):
        self.storage[car.id_car] = car

    def update(self, car):
        self.storage[car.id_car] = car

    def get_all(self):
        """
            :return: a list of all the cars.
        """
        return self.storage
    def get_ID(self, id_car):
        if id_car in self.storage:
            return self.storage[id_car]
        return None