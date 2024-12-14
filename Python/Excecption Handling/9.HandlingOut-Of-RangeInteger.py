MIN_VALUE = -1000
MAX_VALUE = 1000

try:
    value = 2000
    if value < MIN_VALUE or value > MAX_VALUE:
        raise ValueError("Entered integer is out of the specified range.")
    print("You entered:", value)
    
except ValueError as ex:
    print("Error:", ex)
    