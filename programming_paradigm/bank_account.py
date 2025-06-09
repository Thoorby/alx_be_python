# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__account_balance:
            return False
        elif amount <= 0:
            print("Withdraw amount must be positive.")
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
