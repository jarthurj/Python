class User():
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0
	def make_deposit(self, amount):
		self.account_balance += amount
		self.display_user_balance()
	def make_withdrawal(self, amount):
		self.account_balance -= amount
		self.display_user_balance()
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

mike.make_deposit(100)
mike.make_deposit(200)
mike.make_deposit(300)
mike.make_withdrawal(400)
mike.display_user_balance()

andy.make_deposit(200)
andy.make_deposit(200)
andy.make_withdrawal(100)
andy.display_user_balance()

dave.make_deposit(900)
dave.make_withdrawal(100)
dave.make_withdrawal(100)
dave.make_withdrawal(100)

mike.transfer_money(andy, 200)


