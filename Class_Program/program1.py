class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance: Rs.", self.balance)

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Invalid transfer amount.")
        elif amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful.")
        else:
            print("Error: Insufficient balance for transfer.")


# Create two bank account objects
account1 = BankAccount("Amit")
account2 = BankAccount("Priya")

# Deposit money
account1.deposit(5000)
account2.deposit(3000)

# Withdraw money
account1.withdraw(1000)

# Transfer money from Amit to Priya
account1.transfer(1500, account2)

# Display account details
print("\n--- Account 1 Details ---")
account1.display_balance()

print("\n--- Account 2 Details ---")
account2.display_balance()