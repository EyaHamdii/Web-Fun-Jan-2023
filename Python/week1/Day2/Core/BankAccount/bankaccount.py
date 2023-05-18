class BankAccount:
    def __init__(self,int_rate,balance=0):
          self.int_rate = int_rate
          self.balance=balance

    def deposit (self ,amount):
         self.balance +=amount

    def withdraw(self,amount):
         if self.balance>amount:
              self.balance-=amount
         else:  
            print("Insufficient finds: charging a $5 fee")
            self.balance-=5
    
    def display_account_info(self):
     print=(f"balance:${self.balance}")
    
    def yield_interest(self):
        if self.balance>0:
            interest=self.balance*self.int_rate
            self.balance+= interest

