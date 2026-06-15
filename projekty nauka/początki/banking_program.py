
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount to deposit: $"))

    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))

    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount

def main():
    global balance
    balance = 0
    is_running = True

    while is_running:
        print("Welcome to the banking program!")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Thank you for using the banking program. Goodbye!")
            is_running = False
        else:
            print("Invalid choice. Please try again.")

    print("Program has ended.")

if __name__ == "__main__":
    main()