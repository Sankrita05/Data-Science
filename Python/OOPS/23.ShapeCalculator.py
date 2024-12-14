class ShapeCalculator:
    # Calculate the area of shapes
    @staticmethod
    def calculate_area(length, width=-1):
        # Write your code here
        if width==-1:
            return length*length
        else:
            return length*width


# Taking input from the user
square_side = int(input())
length, width  = map(int, input().split())

# Calculate the area of a square
square_area = ShapeCalculator.calculate_area(square_side)
# Calculate the area of a rectangle
rectangle_area = ShapeCalculator.calculate_area(length, width)

# Print the results
print(square_area)
print(rectangle_area)

