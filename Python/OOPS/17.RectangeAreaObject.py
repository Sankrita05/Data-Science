class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width


# Method to calculate the area of a Rectangle object
def calculate_area(rect):
    # Write your code here
    return rect.get_width()*rect.get_length()

    
    
# Create a Rectangle object
rectangle = Rectangle(5, 3)

# Calculate and print the area of the rectangle
area = calculate_area(rectangle)
print("Area of the rectangle:", area)

