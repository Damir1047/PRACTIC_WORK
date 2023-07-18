

class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)

account1 = BankAccount('Bob', 10000, 586542145)
account1.print_data()
