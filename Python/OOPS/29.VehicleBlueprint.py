from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.name = n

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start_engine(self):
        print("Car engine started for " + self.name + ".")


car_name = "Nano"

my_car = Car(car_name)
my_car.start_engine()