#Model a bank account with support for deposit and withdraw operations. In that one can simulate a bank transaction



class Account:
    def __init__(self):
        self.balance = 10

      
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
        
customer1= Account()

#print(customer1.deposit(int(input("Amount Deposited :"))))
print(customer1.withdraw(int(input("Amount to Withdraw :"))))