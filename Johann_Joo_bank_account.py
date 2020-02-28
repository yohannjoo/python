class bank_account:
	
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
		return self
	def withdrawal(self, amount):
		self.balance -= amount
		if self.balance < amount:
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		return self

	def display_account_info(self):
		print("Balance:", self.balance)
		return self.balance

	def yield_interest(self):
		if self.balance > 0:
			self.int_rate = self.balance * self.int_rate
			return self.int_rate
		print(self.int_rate)	

abc = bank_account(10, 100)
abc.deposit(100).deposit(300).deposit(200).withdrawal(1000).display_account_info()

Larry = bank_account(100, 1000)
Larry.deposit(3000).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).display_account_info()
