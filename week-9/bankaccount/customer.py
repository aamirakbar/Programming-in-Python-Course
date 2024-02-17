from bankaccount import BankAccount

class Customer:
    
    __id = 0
    
    def __init__(self, name, balance ,int_rate):
        self.__name = name
        self.__account_number = Customer.__create_account_number()
        self.__account = BankAccount(balance, int_rate)
        
    def __create_account_number():
        Customer.__id += 1
        return f"customer-{Customer.__id}"
    
    def __str__(self):
        return f"Customer name: {self.__name}\n" +\
               f"Account number: {self.__account_number} \n" +\
               f"{self.__account}"
               

customer1 = Customer("Babar", 1000.0, 0.005)
print(customer1)
customer2 = Customer("Virat", 20000.0, 0.005)
print(customer2)
