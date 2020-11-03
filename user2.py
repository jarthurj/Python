class User():
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0
	def make_deposit(self, amount):
		self.account_balance += amount
		self.display_user_balance()
		return self
	def make_withdrawal(self, amount):
		self.account_balance -= amount
		self.display_user_balance()
		return self
	def display_user_balance(self):
		print(self.name," balance:",self.account_balance)
	def transfer_money(self, other_user, amount):
		self.account_balance -= amount
		other_user.account_balance += amount
		self.display_user_balance()
		other_user.display_user_balance()

mike = User("mike123","mike@yahoo.com")
andy = User("andy123", "andy@yahoo.com")
dave = User("dave123", "dave@yahoo.com")

mike.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(400).display_user_balance()

andy.make_deposit(200).make_deposit(200).make_withdrawal(100).display_user_balance()


dave.make_deposit(900).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)

mike.transfer_money(andy, 200)


