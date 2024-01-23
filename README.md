# car-service
Python application with a 4-layered architecture: data access layer ([Domain package]), persistence layer ([Repository package]), business layer ([Service package])) and presentation layer ([User_Interface package]). The data is saved in memory. Tests were done to validate the data ([Tests package]).

Application for managing a car service that supports the following functionalities:
1. CRUD car: id, model, year of purchase, no. km, under warranty. Km and year of manufacture must be strictly positive.
2. CRUD customer card: id, name, surname, CNP, date of birth (dd.mm.yyyy), date of registration (dd.mm.yyyy). The CNP must be unique.
3. CRUD transaction: id, machine_id, client_card_id (may be null), parts amount, labor amount, date and time. If there is a customer card, then apply a 10% discount on labor. If the car is under warranty, then the parts are free. The price paid and discounts given are printed.
4. Search cars and customers by model, year of manufacture, first name, CNP, etc. Full text search.
5. Display all transactions with the amount contained in a given range.
6. Display machines in descending order by the amount obtained per labor.
7. Display of customer cards in descending order according to the amount of discounts obtained.
8. Deleting all transactions in a certain range of days.
9. Warranty update for each car: a car is under warranty if and only if it has a maximum of 3 years and a maximum of 60,000 km.
