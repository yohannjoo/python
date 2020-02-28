# class User:
#     def __init__(self, username, email_address):# now our method has 2 parameters!
#         self.name = username			# and we use the values passed in to set the name attribute
#         self.email = email_address		# and the email attribute
#         self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
        
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#     	self.account_balance += amount

# guido = User("guido", "guido.com")
# monty = User("monty", "monty.com")
# guido.name = "Guido"
# monty.name = "Monty"
# guido.email = "guido.com"
# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50




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
