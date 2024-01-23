from Domain.Car import Car


class CarService:
    """
       Manages car logic.
    """
    def __init__(self, carRepository):
        """
            Creates a car service.
        """
        self.carRepository = carRepository

    def add_car(self, id_car, model, year_purchase, number_km, guarantee):
        """
             Creates a car.
            :param id_car: int, the card id.
            :param model: str, the model.
            :param year_purchase: int, anul fabricatiei
            :param number_km: int, numarul de kilometri
            :param guarantee: int, garantia masinii
                            1, daca exista
                            0, altfel
        """
        errors = []
        if id_car in self.carRepository.get_all():
            errors.append('Exista deja o masina cu id-ul {}'.format(id_car))
        if year_purchase < 0:
            errors.append('Anul achizitiei este < 0 '.format(year_purchase))

        if errors != []:
            raise ValueError(errors)
        car = Car(id_car, model, year_purchase, number_km, guarantee)
        self.carRepository.add(car)

    def update(self, car):
        '''
            Updates car.
            :param car: the car to update
            :return: -
            :raises: KeyError if the id does not exist
        '''
        id_car = car.id_car
        if id_car not in self.carRepository.get_all():
            raise KeyError('There is no car with that id!')
        self.carRepository.update(car)

    def delete(self, id_car):
        """
            Deletes a car.
            :param car_id: the car id to delete.
            :return: -
            :raises KeyError: if no car with car_id
        """
        if id_car not in self.carRepository.storage.keys():
            raise KeyError('There is no car with that id!')
        del self.carRepository.storage[id_car]


    def search_cars(self, search_information):
        """
            Cauta un obiect in clasa car.
            :param search_information:
            :return:
        """

        list = []
        for object_car in self.get_all():
            s = str(object_car.id_car)
            r = s.find(search_information)
            if r != -1:
                list.append(object_car)

            s = object_car.model
            r = s.find(search_information)
            if r != -1:
                list.append(object_car)

            s = str(object_car.year_purchase)
            r = s.find(search_information)
            if r != -1:
                list.append(object_car)

            s = str(object_car.number_km)
            r = s.find(search_information)
            if r != -1:
                list.append(object_car)

            s = str(object_car.guarantee)
            r = s.find(search_information)
            if r != -1:
                list.append(object_car)
        return list

        """
        if search_information in object_car.id_car:
            list.append(object_car)
        elif search_information in object_car.model:
            list.append(object_car)
        elif search_information in object_car.year_purchase:
            list.append(object_car)
        elif search_information in object_car.number_km:
            list.append(object_car)
        elif search_information in object_car.guarantee:
            list.append(object_car)
        return list
        """


    def find_by_id(self, id_car):
        '''
        Finds a car object by id
        :param id_car: the car id
        :return: the car if found, or None if not found
        '''

        for car in self.get_all():
            if car.id_car == id_car:
                return self.carRepository.storage[id_car]
        return None

    def update_guarantee(self, car):
        id = 0
        if car.number_km <= 60000 and (2019 - car.year_purchase) <= 3:
            id = car.id_car
        return id

    def get_all(self):
        return list(self.carRepository.get_all().values())

        #l = list(self.carRepository.get_all().values())
        #for m in l:
        #    print(m)
        #return l

    def binary_search(self, needle):
        '''
        Searches for needle in haystack
        :param needle:
        :return:
        '''

        cars = self.get_all()
        list = []
        for car in cars:
            list.append(car.id_car)
        haystack = sorted(list, key=lambda car: car)
        st = 0
        n = len(list)
        dr = n-1
        while st <= dr:
            m = (st+dr) // 2
            if haystack[m] == needle:
                return self.find_by_id(haystack[m])
            if haystack[m] < needle:
                st = m+1
            else:
                dr = m-1
        return False

    def permutations_cars(self):
        cars = self.get_all()
        result = []
        n = len(cars)
        ids_of_cars = []
        for car in cars:
            ids_of_cars.append(car.id_car)

        def inner(current_permutation):
            if len(current_permutation) == n:
                result.append(current_permutation)
                return

            for i in range(0, n):
                if ids_of_cars[i] not in current_permutation:
                    inner(current_permutation + [ids_of_cars[i]])
        inner([])
        return result