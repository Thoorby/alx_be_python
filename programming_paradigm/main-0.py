# programming_paradigm/main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Set an initial balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    if ':' in command_input:
        command, param = command_input.split(':', 1)
        try:
            amount = float(param)
        except ValueError:
            print("Invalid amount format. Use a number.")
            sys.exit(1)
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
