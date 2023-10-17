class BankAccount:
# Provide your code for this class here
  def __init__(self,acc_id:int,acc_name:str):
    self.acc_id = acc_id
    self.acc_name = acc_name
    self.balance = 0.0

  def get_balance(self) -> float:
    return round(self.balance,2)
  def deposit(self, x: float):
    if x <= 0:
      print("Invalid amount")
    else:
      self.balance += x

  def withdraw(self, x: float):
    if x <= 0:
      print("Invalid amount")
    elif self.balance < x:
      print("Insufficient fund")
    else:
      self.balance -= x

  def transfer(self, q: "BankAccount", x: float):
    if q == self:
      print("Same account")
    elif x <= 0:
      print("Invalid amount")
    elif self.balance < x:
      print("Insufficient fund")
    else:
      self.balance -= x
      q.balance += x
  


# Do NOT change the code below this line
############################
class AccountDatabase:
  def __init__(self):
    self.db = []

  def add(self,account):
    self.db.append(account)

  def find_account(self, acc_id):
    for acc in self.db:
      if acc.acc_id==acc_id:
        return acc
    print("Account not found")
    return None

account_database = AccountDatabase()

acc1 = BankAccount(int(input()), input())
account_database.add(acc1)
acc2 = BankAccount(int(input()), input())
account_database.add(acc2)

while True:
    c = input()
    if c=='q':
      print("Done")
      break
    elif c=='d':
      acc = account_database.find_account(int(input()))
      if acc is not None:
        acc.deposit(float(input()))
    elif c=='w':
      acc = account_database.find_account(int(input()))
      if acc is not None:
        acc.withdraw(float(input()))
    elif c=='t':
      acc1 = account_database.find_account(int(input()))
      if acc1 is not None:
        acc2 = account_database.find_account(int(input()))
        if acc2 is not None:
          acc1.transfer(acc2, float(input()))
    elif c=='b':
      acc = account_database.find_account(int(input()))
      if acc is not None:
        print("Balance =", acc.get_balance())
    else:
      print("Invalid command")