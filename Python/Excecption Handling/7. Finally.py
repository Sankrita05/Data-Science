def divide(a, b):
    if b == 0:
        raise ArithmeticError("Division by zero is not allowed.")
    return a // b


try:
    result = divide(10, 2)
    print("Result:", result)
except ArithmeticError as e:
    print("An arithmetic exception occurred.")
finally:
    print("Finally block always executed.")