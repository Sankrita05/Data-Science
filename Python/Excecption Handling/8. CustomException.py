# Custom exception class
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    age = -5
    if age < 0:
        raise CustomException("Age cannot be negative")
        
    print("Age is:", age)
except CustomException as e:
    print("Custom Exception caught:", e)

