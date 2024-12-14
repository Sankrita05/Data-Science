try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except ArithmeticError:
    print("Arithmetic error occurred")