class BankAccount:
    def __init__(self, bal, int_rate):
        self.__balance = bal
        self.__interest_rate = int_rate
        
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    def calculate_interest(self):
        return self.__balance * self.__interest_rate