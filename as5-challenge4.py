# Challenge 4: Implement a Banking Account


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def set_account_info(self):
        self.title = input("Enter account title: ")
        self.balance = float(input("Enter account balance: "))

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=None):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def set_savings_account_info(self):
        super().set_account_info()
        self.interestRate = float(input("Enter interest rate: "))



print("\nAccount Information")
account = Account()
account.set_account_info()

print(f"Title: {account.title}")
print(f"Balance: {account.balance}")


print("\nSavings Account Information")
savings_account = SavingsAccount()
savings_account.set_savings_account_info()

print(f"Title: {savings_account.title}")
print(f"Balance: {savings_account.balance}")
print(f"Interest Rate: {savings_account.interestRate}\n")
