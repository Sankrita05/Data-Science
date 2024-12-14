class Shape:
    def __init__(self):
        self.area = 0

    def print_area(self):
        print("Area:", self.area)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def print_area(self):
        print("Rectangle Area:", self.area)


s = None
r = Rectangle(4, 6)

s = r
s.print_area()
