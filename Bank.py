# ATM Simulator in Python

balance = 10000.0  # Initial balance
pin = "1234"       # Default PIN

def check_pin():
    entered_pin = input("Enter your PIN: ")
    return entered_pin == pin

def check_balance():
    if check_pin():
        print(f"Your current balance is: Rs. {balance:.2f}")
    else:
        print("Incorrect PIN.")

def deposit():
    global balance
    if check_pin():
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Rs. {amount:.2f} deposited successfully.")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount.")
    else:
        print("Incorrect PIN.")

def withdraw():
    global balance
    if check_pin():
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print(f"Rs. {amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")
        except ValueError:
            print("Invalid amount.")
    else:
        print("Incorrect PIN.")

def change_pin():
    global pin
    old_pin = input("Enter current PIN: ")
    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully.")
        else:
            print("PINs do not match.")
    else:
        print("Incorrect current PIN.")

def main():
    while True:
        print("\n===== ATM Simulator Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            change_pin()
        elif choice == '0':
            print("Thank you for using ATM Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
