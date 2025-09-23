#Create acc with 2 attribute balance and acocunt 
#create a method fo debit and cedit

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs.{amount} was debited")
        print("Total balance is:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} was credited")
        print("Total balance is:", self.get_balance())

    def get_balance(self):
        return self.balance


# creating object
acc1 = Account(10000, 12345)

# transactions
acc1.debit(1000)
acc1.credit(500)

# final details
# print("Final Balance:", acc1.balance)
# print("Account Number:", acc1.account_no)

