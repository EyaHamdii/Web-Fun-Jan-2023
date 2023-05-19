class BankAccount:
     def __init__(self,int_rate,balance):
          self.int_rate = int_rate
          self.balance=balance

     def deposit (self ,amount):
         self.balance +=amount
         return self

     def withdraw(self,amount):
          if self.balance>amount:
               self.balance-=amount
          else:  
               print("Insufficient finds: charging a $5 fee")
               self.balance-=5
          return self
    
     def display_account_info(self):
          print(f"balance:${self.balance}")
          return self
    
     def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)           
            return self
account1=BankAccount(0.02,200)
account1.deposit(300).deposit(100).deposit(100).display_account_info()
account1.withdraw(150).display_account_info()
account1.yield_interest().display_account_info()
account2=BankAccount(0.02,200)
account2.deposit(150).deposit(150).display_account_info()
account2.withdraw(50).withdraw(20).withdraw(10).withdraw(5).display_account_info()
account2.yield_interest().display_account_info()

