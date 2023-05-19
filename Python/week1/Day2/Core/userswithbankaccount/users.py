from Bank_account import BankAccount

class User(BankAccount):
    def__init__(self,name,email)
    super().__init__(self)
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0,02,balance=0)

    def make_deposit(self, amount):
        super().deposit(amount)
        return self


    def make_withdrawal(self, amount):
        super().withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'Your balance now is {self.balance}')
        return self

