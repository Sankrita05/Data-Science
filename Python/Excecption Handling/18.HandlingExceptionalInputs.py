try: 
    try:
        num1 = input()
        num2 = input()
        
        if not (num1.replace("-", "").isdigit() and num2.replace("-", "").isdigit()):
            raise ValueError("Invalid input.")
            
        num1 = int(num1)
        num2 = int(num2)
        
        result = num1 / num2
        print("Result of division:", result)
    
    except ValueError as ve:
        # Handle if the input is not an integer
        print("Invalid input.")
        
       
except Exception as e:
    # Handle any other unknown exceptions
    print("An unknown error occurred.")
    

