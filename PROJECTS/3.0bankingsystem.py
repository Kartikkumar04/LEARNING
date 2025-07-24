balance = 10000 
print("Welcome to the Banking System")
print("Press 1 for Credit")
print("Press 2 for Debit")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    print("Welcome to Credit")
    amount = int(input("Enter amount to credit: "))
    balance = balance + amount
    print("Amount Credited Successfully")
    print("New Balance:", balance)
elif choice == 2:
    print("Welcome to Debit")
    amount = int(input("Enter amount to debit: "))
    if amount > balance:
        print("Transaction Failed: Low Balance")
    else:
        balance = balance - amount
        print("Amount Debited Successfully")
        print("New Balance:", balance)