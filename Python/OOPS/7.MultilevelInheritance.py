class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.")

class Labrador(Dog):
    def swim(self):
        print(f"{self.name} can swim.")

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")
labrador = Labrador("Max")

# Calling methods
animal.speak()      # Output: Generic Animal makes a sound.
dog.speak()         # Output: Buddy makes a sound.
dog.bark()          # Output: Buddy barks.
labrador.speak()    # Output: Max makes a sound.
labrador.bark()     # Output: Max barks.
labrador.swim()     # Output: Max can swim.