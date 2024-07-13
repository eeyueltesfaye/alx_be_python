class BankAccount:
    def __init__(self, initial_balance = 0.0) :
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount

        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("withdrawl amount must be positive")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

if __name__ == "__main__":

    account = BankAccount(200)
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()   
