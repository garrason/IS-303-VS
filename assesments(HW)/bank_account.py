import random
import math


class BankAccount:
    def __init__(self, customer_name):
        # Each new account starts with its own name, number, and balance.
        self.customer_name = customer_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def make_deposit(self):
        try:
            amount = float(input("How much would you like to deposit? "))
        except ValueError:
            print("Please enter a valid dollar amount.")
            return

        if not math.isfinite(amount) or amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            amount = round(amount, 2)
            if amount == 0:
                print("Please enter at least $0.01.")
                return
            self.balance = round(self.balance + amount, 2)
            print(f"Deposited: ${amount:.2f}")

    def make_withdrawal(self):
        try:
            amount = float(input("How much would you like to withdraw? "))
        except ValueError:
            print("Please enter a valid dollar amount.")
            return

        if not math.isfinite(amount) or amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            amount = round(amount, 2)
            if amount == 0:
                print("Please enter at least $0.01.")
            elif amount > self.balance:
                print("You do not have enough money in your account.")
            else:
                self.balance = round(self.balance - amount, 2)
                print(f"Withdrawn: ${amount:.2f}")

    def view_account_information(self):
        print(f"Name: {self.customer_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
