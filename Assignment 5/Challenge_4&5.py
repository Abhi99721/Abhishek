class Account: 
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    # withdrawal method
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    # deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    # this method just returns the value of balance
    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        
    # computes interest amount using the interest rate
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


demo1 = SavingsAccount("Ashish", 2000, 5)
print("Initial Balance:", demo1.getBalance())
demo1.withdrawal(1000)
print("Balance after withdrawal:", demo1.getBalance())
demo1.deposit(500)
print("Balance after deposit:", demo1.getBalance())
print("Interest on current balance:", demo1.interestAmount())