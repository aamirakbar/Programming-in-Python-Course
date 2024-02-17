from bankaccount import BankAccount

account1 = BankAccount(1000.0, 0.005)

print(account1.get_balance())
print(account1.calculate_interest())

account1.withdraw(500)

print(account1.get_balance())
print(account1.calculate_interest())