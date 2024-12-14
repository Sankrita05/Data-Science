class Vehicle:
    def __init__(self):
        print("Vehicle constructor")

    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car constructor")

    def start(self):
        print("Car started")


class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print("ElectricCar constructor")

    def start(self):
        print("ElectricCar started")

# What is the order of constructor calls when you create an ElectricCar object?
# Vehicle constructor -> Car constructor -> ElectricCar constructor