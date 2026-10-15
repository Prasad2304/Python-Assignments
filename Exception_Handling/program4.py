print("===== ATM System =====")

balance = 10000

try:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        balance = balance + amount

        print("Amount deposited successfully")
        print("New balance:", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > balance:
            raise ValueError("Insufficient balance")

        balance = balance - amount

        print("Please collect your cash")
        print("Remaining balance:", balance)

    else:
        print("Invalid choice")

except ValueError as e:
    print("Transaction Error:", e)

finally:
    print("Thank you for using ATM.")