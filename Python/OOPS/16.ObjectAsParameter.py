class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

# The printPersonInfo method takes a Person object as a parameter, and it can access the name and age properties of the Person object to print their values.
def print_person_info(p):
    print("Name:", p.get_name())
    print("Age:", p.get_age())


# Create a Person object
person = Person("Alice", 30)

# Call a method and pass the object as a parameter
print_person_info(person)
