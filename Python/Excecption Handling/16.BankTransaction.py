class BankAccount:
    def __init__(self, acc_num, initial_balance):
        self.account_number = acc_num
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Invalid input. Please enter a valid withdrawal amount.")

        if amount > self.balance:
            raise RuntimeError("Insufficient balance.")

        self.balance -= amount
        print("Withdrawal successful. New balance: ${:.2f}".format(self.balance))


# Create a BankAccount object with predefined values
account = BankAccount(12345, 1000.0)

try:
    # Nested try-except blocks
    try:
        # Attempt to withdraw money from the account
        account.withdraw(1500.0)
        
    except RuntimeError as e:
        # Handle specific exception (Insufficient balance)
        print(e)
        
except ValueError as e:
    # Handle general exception (Invalid input)
    print(e)
    
except Exception as e:
    # Handle any other unknown exceptions
    print("An unknown error occurred.")


