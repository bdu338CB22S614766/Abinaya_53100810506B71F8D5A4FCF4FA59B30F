class Bank_Account:

  def __init__(self):
    self.balance = 0
    print("Hello!!! the Deposit  & Withdrawl Machine")

  def deposit(self):
    amount = float(input("Enter the amount to be Deposited:"))
    self.balance += amount
    print(" \n Amount            Deposited:", amount)

  def Withdraw(self):
    amount = float(input("Enter the amount to be Withdrew:"))
    if self.balance >= amount:
      self.balance -= amount
      print("\n You Withdraw:", amount)
    else:
      print("\n Insufficient balance")

  def display(self):
    print(" \n Account Balance=", self.balance)


s = Bank_Account()

s.deposit()
s.Withdraw()
s.display()
