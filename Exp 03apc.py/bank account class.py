class BankAccount:
    count = 1000

    def __init__(self, account_holder):
        BankAccount.count += 1
        self.account_number = BankAccount.count
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
        else:
            print("Insufficient balance")


a1 = BankAccount("Amit")
a2 = BankAccount("Priya")

a1.deposit(5000)
a1.withdraw(500)
a1.transfer(1000, a2)

a1.display_balance()
a2.display_balance()