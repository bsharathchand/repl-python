class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0

class User(object):
  def __init__(self,username):
    self.username = username

my_account = BankAccount(15)
my_account.withdraw(50)
print (my_account.balance, my_account.overdrawn())

user = User('sbhaskara')
print (user.username)