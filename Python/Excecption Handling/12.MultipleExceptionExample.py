try:
    numerator = 1
    denominator = 0
    
    if denominator == 0:
        raise ArithmeticError("Division by zero")
        
    print("Result:", numerator / denominator)
    
except ArithmeticError as ae:
    print("Error: Division by zero is not allowed.")
except ValueError as ime:
    print("Error: Please enter valid integer values.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
finally:
    # finally block
    pass
