class DivisionByZeroExample:
    @staticmethod
    def divide(numerator, denominator):
        if denominator == 0:
            raise ArithmeticError("Division by zero is not allowed.")
        return numerator // denominator


numerator = 10
denominator = 0

try:
    result = DivisionByZeroExample.divide(numerator, denominator)
    print("Result:", result)
except ArithmeticError as e:
    print("Error: Division by zero is not allowed.")