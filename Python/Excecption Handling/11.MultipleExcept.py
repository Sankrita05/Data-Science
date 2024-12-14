def divide_numbers(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid operand types")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("This block always executes")

# Example usage
divide_numbers(10, 2)     # Result: 5.0
divide_numbers(10, 0)     # Error: Division by zero
divide_numbers("10", 2)   # Error: Invalid operand types