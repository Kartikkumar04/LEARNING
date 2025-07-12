def credit(balance):
    amount = float(input("Enter amount to credit: "))
    if amount > 50000:
        print("Credit Limit Crossed (Limit: 50000)")
    else:
        balance += amount
        print(f"{amount} credited successfully. New Balance: {balance}")
    return balance


def debit(balance):
    amount = float(input("Enter amount to debit: "))
    if amount > balance:
        print("Low Balance - Transaction Failed")
    else:
        balance -= amount
        print(f"{amount} debited successfully. Remaining Balance: {balance}")
    return balance


def show_menu():
    print("BANKING SYSTEM")
    print("1. Credit")
    print("2. Debit")
    print("3. Exit")


def banking_system():
    balance = float(input("Enter your starting balance: "))
    
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            balance = credit(balance)
        elif choice == "2":
            balance = debit(balance)
        elif choice == "3":
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

banking_system()