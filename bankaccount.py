class BankAccount:
	def __init__(self, int_rate=.01, balance=0):
		self.balance = balance
		self.int_rate = int_rate
	def deposit(self, amount):
		self.balance += amount
		return self
	def withdraw(self, amount):
		self.balance -= amount
		return self
	def display_account_info(self):
		print("Balance:",self.balance,"Interest Rate:",self.int_rate)
		return self
	def yield_interest(self):
		if self.balance > 0:
			interest = self.balance * self.int_rate
			self.balance += interest
		return self

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()