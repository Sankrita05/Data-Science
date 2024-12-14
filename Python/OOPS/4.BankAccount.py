class BankAccount : # This class represents a bank account.
    __accountNumber = None
    __accountHolder = None
    __balance = None
    
    # A constructor to initialize the attributes when creating a new account.
    def __init__(self, accountNumber, accountHolder): 
        BankAccount.__accountNumber = accountNumber
        BankAccount.__accountHolder = accountHolder
        BankAccount.__balance = 0
    
    # This method allows you to deposit a specified amount into the account.
    def deposit(self , value): 
        BankAccount.__balance += value
        print(f"Deposited: ${value}")

    # This method allows you to withdraw a specified amount from the account.  
    def withdraw(self , value): 
        BankAccount.__balance -= value
        print(f"Withdrawn: ${value}")

    # This method displays the account information, including the account number, account holder's name, and the current balance.
    def getAccountInfo(self):
        print(f"Account Number: {BankAccount.__accountNumber}");
        print(f"Account Holder: {BankAccount.__accountHolder}");
        print(f"Balance: ${BankAccount.__balance}"); 


# Write your code here
# Create a BankAccount object
account = BankAccount(12345, "John Doe")

# Perform deposits and withdrawals and display account info
account.deposit(1000)
account.withdraw(500)
account.deposit(200)

# Display the final account information
account.getAccountInfo()