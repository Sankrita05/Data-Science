celsius = -300.0  # Pre-defined temperature

try:
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not valid.")
        
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Celsius:", celsius)
    print("Temperature in Fahrenheit:", fahrenheit)
    
except ValueError as e:
    print("Invalid Argument:", e)
    
except Exception as e:
    print("An unknown error occurred.")

