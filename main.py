class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than 0."
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Account balance for {self._account_holder_name}: ${self._account_balance}"

# Create an instance of the BankAccount class
account1 = BankAccount("12345", "John Doe", 1000)

# Test deposit and withdrawal functionality
print(account1.display_balance())  # Display initial balance
print(account1.deposit(500))        # Deposit $500
print(account1.withdraw(200))       # Withdraw $200
print(account1.display_balance())  # Display updated balance
print(account1.withdraw(2000))      # Attempt to withdraw more than the balance
      