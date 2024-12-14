class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")


generic_animal = Animal()
dog = Dog()
cat = Cat()

generic_animal.make_sound()
dog.make_sound()
cat.make_sound()
