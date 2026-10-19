def check_balance(balance):
    print("Current Balance:", balance)


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance = balance + amount
        print("Money deposited successfully!")
        print("Updated Balance:", balance)
    else:
        print("Please enter a valid amount.")

    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Updated Balance:", balance)

    return balance


def login():
    correct_pin = "1234"
    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("Login successful!")
        return True
    else:
        print("Incorrect PIN!")
        return False


def atm():
    balance = 1000

    if login():
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                check_balance(balance)

            elif choice == "2":
                balance = deposit(balance)

            elif choice == "3":
                balance = withdraw(balance)

            elif choice == "4":
                print("Thank you for using our ATM!")
                break

            else:
                print("Invalid choice! Please try again.")


atm()