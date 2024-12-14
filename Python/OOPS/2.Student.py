class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

    def display(self):
        print(f"{self.name} {self.age}")

s = Student()
s.name, s.age = input().split()

s.display()