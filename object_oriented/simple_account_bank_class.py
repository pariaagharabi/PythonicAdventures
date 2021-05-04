from abc import ABC, abstractmethod
# Create a Class Phonebook that should keep A list of contacts. Derive the class Contact from two base classes Person and Address


class Bank_Account(ABC):
    def __init__(self, balance=0):
        self.balance = balance
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self, amount):
        # amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self, amount):
        # amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
            return True
        else:
            print("\nInsufficient balance  ")
            return False

    def display(self):
        print("\nNet Available Balance=", self.balance)


class Saving_Account(Bank_Account):
    def __init__(self, balance=0, intrest_rate=0.1):
        self.intrest_rate = intrest_rate
        super().__init__(balance)

    def calc_interset(self, years):
        return (self.balance * years * self.intrest_rate)/100


class Chequing_Account(Bank_Account):
    def __init__(self, balance=0):
        self.number_of_transactions = 0
        super().__init__(balance)

    def deposit(self, amount):
        super().deposit(amount)
        self.number_of_transactions += 1

    def withdraw(self, amount):
        if super().withdraw(amount):
            self.number_of_transactions += 1
            return True
        return False

    def display(self):
        super().display()
        print(f"Number of transactions: {self.number_of_transactions}")
