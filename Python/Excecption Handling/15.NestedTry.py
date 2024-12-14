try:
    # Outer try block
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    try:
        # Nested try block
        result = num1 / num2
        print(f"Result: {result}")

    except ZeroDivisionError:
        # Handle division by zero exception
        print("Error: Division by zero is not allowed.")

except ValueError:
    # Handle invalid input (non-integer) exception
    print("Error: Please enter valid integers.")
except Exception as e:
    # Handle other unexpected exceptions
    print(f"An unexpected error occurred: {e}")