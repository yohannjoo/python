class User:
    def __init__(self,name):
        self.name = name
        self.account_balance = 0
        
    
    def make_deposit(self, amount):
        self.account_balance+=amount
        return self


    def make_withdrawal(self, amount):
        self.account_balance -= amount 
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self


johann = User("johann")
johann.name = "Johann"
johann.make_withdrawal(100).make_deposit(200).make_deposit(200).make_deposit(200).display_user_balance()


Bob = User("Bob")
Bob.name = "Bob"
Bob.make_withdrawal(50).make_withdrawal(50).make_deposit(300).make_deposit(300).display_user_balance()

Larry = User("Larry")
Larry.name = "Larry"
Larry.make_withdrawal(400).make_withdrawal(400).make_withdrawal(400).make_deposit(100).display_user_balance()

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
