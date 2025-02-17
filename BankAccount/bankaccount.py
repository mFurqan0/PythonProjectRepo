class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc = acc 

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited from your account") 
        print("total balance =", self.get_bal())
    
    #credit method 
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited in your account") 
        print("total balance =", self.get_bal())

    def get_bal(self):
        return self.balance     

acc1 = Account(10000,2803)
acc1.debit(100)