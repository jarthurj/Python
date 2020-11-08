class BankAccount:
	def __init__(self, balance=0, int_rate=.01):
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

class User():
	def __init__(self, name):
		self.name = name
		self.account = {}
	def make_deposit(self, accountname, amount):
		self.account[accountname].deposit(amount)
	def make_withdrawl(self, accountname, amount):
		self.account[accountname].withdraw(amount)
	def displayaccount(self):
		for accountname in self.account:
			self.account[accountname].display_account_info()
	def addaccount(self, accountname, initialdesposit, int_rate = .01):
		self.account[accountname] = BankAccount(initialdesposit, int_rate)
	def interest(self):
		for accountname in self.account:
			self.account[accountname].yield_interest()

user1 = User("John")
user1.addaccount("checking", 200)
user1.displayaccount()
user1.make_deposit("checking", 200)
user1.displayaccount()
user1.make_withdrawl("checking", 200)
user1.displayaccount()
user1.addaccount("savings", 200, .05)
user1.displayaccount()
user1.interest()
user1.displayaccount()