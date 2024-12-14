class Person: # Class Definition
    # Constructor (__init__ method)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def greet(self): # self refers to the instance of the class.
        # Instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes and calling methods
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")

person1.greet()
person2.greet()
