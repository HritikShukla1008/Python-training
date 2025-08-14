#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current balance: ₹{self.balance}")



class SavingAccount(BankAccount):
    interest_rate = 0.04  # 4%

    def apply_interest(self):
        interest = self.balance * SavingAccount.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied at rate {SavingAccount.interest_rate * 100}%.")


# Current Account subclass
class CurrentAccount(BankAccount):
    overdraft_limit = 50000  # ₹50,000

    def withdraw(self, amount):
        if amount <= self.balance + CurrentAccount.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully (Overdraft allowed).")
        else:
            print("Withdrawal exceeds overdraft limit.")

# --- Main Program Flow ---
def main():
    account_type = input("Enter account type (saving/current): ").strip().lower()
    account_holder = input("Enter account holder name: ").strip()
    
    while True:
        try:
            balance = float(input("Enter initial balance: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if account_type == 'saving':
        account = SavingAccount(account_holder, balance)
        print("\nYour account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Interest Rate (Bank Fixed): {SavingAccount.interest_rate * 100}%")
    elif account_type == 'current':
        account = CurrentAccount(account_holder, balance)
        print("\nYour account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Overdraft Limit (Bank Fixed): ₹{CurrentAccount.overdraft_limit}")
    else:
        print("Invalid account type.")
        return

    # Operations menu
    while True:
        print("\nChoose operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        if account_type == 'saving':
            print("4. Apply Interest (Bank-decided rate)")
            print("5. Exit")
        else:
            print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4' and account_type == 'saving':
            account.apply_interest()
        elif (choice == '4' and account_type == 'current') or (choice == '5' and account_type == 'saving'):
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice.")

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:




