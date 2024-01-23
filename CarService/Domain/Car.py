class Car:
    """
      Car business object.
    """

    def __init__(self, id_car, model, year_purchase, number_km, guarantee):
        """
            Creates a car
            :param id_car: int, the card id.
            :param model: str, the model
            :param year_of_purchase: int, the year of purchase
            :param number_km: int, the number km
            :param guarantee: int, garantia masinii
                                1, daca exista
                                0, altfel
        """
        self.id_car = id_car
        self.model = model
        self.year_purchase = year_purchase
        self.number_km = number_km
        self.guarantee = guarantee
    def __str__(self):
        return 'Car {}- {},  {}, {}, {}'.format(self.id_car,
                                                  self.model,
                                                  self.year_purchase,
                                                  self.number_km,
                                                  self.guarantee)
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_car == other.id_car and self.model == other.model and self.year_purchase == other.year_purchase and self.number_km == other.number_km and self.guarantee == other.guarantee
