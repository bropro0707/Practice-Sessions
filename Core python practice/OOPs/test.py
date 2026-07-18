class Bankaccount:
    def __init__(self):
        self.__balance = 0
    def deposite(self,amount):
        self.__balance += amount
        print(f"{amount} has been added to the account")
    def withdrawl(self,amount):
        if amount > self.__balance:
            print("Not sufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawl: {amount}")
    def get_balance(self):
        return self.__balance
a = Bankaccount()
a.deposite(1000)
a.withdrawl(200)
print(a.get_balance())

 