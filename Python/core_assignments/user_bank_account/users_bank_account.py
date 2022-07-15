class BankAccount:
    bank_name="Wells Fargo"
    int_rate = 0.1
    balance = 0

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self, int_rate):
        if self.balance > 0:
            self.balance = self.balance * (int_rate)
        else:
            self.balance = self.balance
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit = self.account.balance + amount
        print(self.account.balance)

print(self.account.balance)


user1 = BankAccount(0.3, 500)
user1.deposit(50).deposit(100).withdraw(100).yield_interest(0.5).display_account_info()

user2 = BankAccount(0.1, 20)
user2.deposit(10).deposit(122).withdraw(3).withdraw(5).withdraw(10).withdraw(50).yield_interest(0.4).display_account_info()





