class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} sings beautifully!"

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Calling the speak method on each object
print(dog.speak())   # Output: Buddy says Woof!
print(cat.speak())   # Output: Whiskers says Meow!
print(bird.speak())  # Output: Tweetie sings beautifully!