class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")


class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        available_balance = self.balance + self.overdraft_limit
        if available_balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Transaction declined: Insufficient funds")


if __name__ == "__main__":
    # Create a savings account
    savings_acc = SavingsAccount("SAV-001", 5000)
    savings_acc.display_balance()
    savings_acc.deposit(1000)
    savings_acc.calculate_interest()
    savings_acc.display_balance()

    # Create a current account
    current_acc = CurrentAccount("CUR-001", 2000)
    current_acc.display_balance()
    current_acc.withdraw(1500)
    current_acc.display_balance()
    current_acc.withdraw(3000)
