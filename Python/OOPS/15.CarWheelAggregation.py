class Wheel:
    def __init__(self, wheel_type):
        self.type = wheel_type

    def print_type(self):
        print("Wheel Type:", self.type)

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.front_left_wheel = Wheel("Front Left")
        self.front_right_wheel = Wheel("Front Right")
        self.rear_left_wheel = Wheel("Rear Left")
        self.rear_right_wheel = Wheel("Rear Right")

    def print_info(self):
        print(f"Make: {self.make}, Model: {self.model}")
        self.front_left_wheel.print_type()
        self.front_right_wheel.print_type()
        self.rear_left_wheel.print_type()
        self.rear_right_wheel.print_type()


my_car = Car("Toyota", "Camry")
my_car.print_info()

