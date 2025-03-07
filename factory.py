import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(message)s")


# Абстрактний клас Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


# Клас Car, що успадковується від Vehicle
class Car(Vehicle):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")


# Клас Motorcycle, що успадковується від Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")


# Абстрактний клас VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


# Фабрика для транспортних засобів США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


# Фабрика для транспортних засобів Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


# Використання фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Ducati", "Panigale V4")
vehicle2.start_engine()
