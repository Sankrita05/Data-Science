# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the derived class
dog_instance = Dog("Buddy")

# Calling methods from the base and derived classes
dog_instance.speak()  # This will call the overridden method in Dog class