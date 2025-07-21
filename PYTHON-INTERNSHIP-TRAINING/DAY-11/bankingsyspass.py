username = "kartik"
password = "1234"

print("Welcome to Bank ")
input_user = input("Enter username: ")
input_pass = input("Enter password: ")

if input_user == username and input_pass == password:
    print("\n Login Successful!")
    balance = 5000 

while True:
        print("\nBanking Menu")
        print("1. Check Balance")
        print("2. Credit (Deposit)")
        print("3. Debit (Withdraw)")
        print("4. Log Out")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f" Current Balance: {balance}")
        
        elif choice == '2':
            amount = float(input("Enter amount to credit: "))
            if amount > 0:
                balance += amount
                print(f"Credited {amount}. New Balance: {balance}")
            else:
                print("Invalid amount!")

        elif choice == '3':
            amount = float(input("Enter amount to debit: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Debited {amount}. New Balance: {balance}")
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == '4':
            print("Logout Successful4" \
            "")
            break
        else:
                print("Login failed. Invalid username or password.")

else:
        print("Invalid choice. Please select 1 to 4.")

