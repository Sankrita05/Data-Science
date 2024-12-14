from abc import ABC, abstractmethod

# Abstract base class Shape
class Shape:
    # Abstract method for calculating area
    @abstractmethod
    def calculate_area(self):
        pass

# Derived class Square
class Square(Shape):
    def __init__(self, side_length):
        self.side = side_length

    # Implementation of calculate_area for Square
    def calculate_area(self):
        return self.side * self.side

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementation of calculate_area for Rectangle
    def calculate_area(self):
        return self.length * self.width


square_side = int(input())
rectangle_length, rectangle_width = list(map(int,input().split()))

# Create a Square with a side length
square = Square(square_side)

# Create a Rectangle with length and width
rectangle = Rectangle(rectangle_length, rectangle_width)

# Calculate and display the areas
print(square.calculate_area())
print(rectangle.calculate_area())

