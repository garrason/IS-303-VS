from bank_account import BankAccount


def main():
    print("Welcome to the Bank of Elijah!")
    customer_name = input("Please enter your name: ").strip()
    account = BankAccount(customer_name)

    # Keep showing the menu until the customer chooses to quit.
    while True:
        print("\nPlease choose an option:")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. View account information")
        print("4. Quit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            account.make_deposit()
        elif choice == "2":
            account.make_withdrawal()
        elif choice == "3":
            account.view_account_information()
        elif choice == "4":
            print("Thank you for your business!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
