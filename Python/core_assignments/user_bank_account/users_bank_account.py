class BankAccount:
    bank_name="Wells Fargo"
    all_accounts=[]

    def __init__(self, int_rate = 0.1, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

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
            self.balance += self.balance * (int_rate)
        return self

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) #assigns bank account to user

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

# checkings = BankAccount(0.3, 500)
# checkings.deposit(50).deposit(100).withdraw(100).yield_interest(0.5).display_account_info()

# savings = BankAccount(0.1, 20)
# savings.deposit(10).deposit(122).withdraw(3).withdraw(5).withdraw(10).withdraw(50).yield_interest(0.4).display_account_info()

Maria= User("Maria", "maria@gmail.com")

# print(BankAccount.all_accounts)
# print(Maria.account.balance)
Maria.make_deposit(200)
Maria.make_withdraw(100)
Maria.display_user_balance()




