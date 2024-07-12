class BankAccount():
    def __init__(self, initial_balance):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        self.initial_balance += amount

    def winthdraw(self, amount):
     if amount <= self.account_balance:
        self.account_balance -= amount
        return True
     else:
        return False
    def diplay_balance(self):
       print(f"Current balance: ${self.account_balance}")
        
    




