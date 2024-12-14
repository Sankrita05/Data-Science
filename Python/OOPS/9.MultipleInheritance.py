class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Flyer:
    def fly(self):
        return f"{self.name} is flying!"

class Bird(Animal, Flyer):
    def speak(self):
        return f"{self.name} says Tweet!"

class Bat(Animal, Flyer):
    def speak(self):
        return f"{self.name} says Squeak!"

# Creating instances of derived classes
parrot = Bird("Parrot")
bat = Bat("Bat")

# Using methods from both base classes
print(parrot.speak())  # Output: Parrot says Tweet!
print(parrot.fly())    # Output: Parrot is flying!

print(bat.speak())     # Output: Bat says Squeak!
print(bat.fly())       # Output: Bat is flying!