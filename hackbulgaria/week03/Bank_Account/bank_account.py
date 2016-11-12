# bank_account.py
class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        if balance < 0:
            raise ValueError()
        self._balance = balance
        self.currency = currency
        self.acc_history = ["Account was created"]

    def deposit(self, amount):
        if amount < 0:
            raise ValueError()
        self._balance += amount
        self.acc_history.append('Deposited {0}{1}'.format(amount, self.currency))
    
    def balance(self):
        self.acc_history.append('Balance check -> {0}{1}'.format(self._balance, self.currency))
        return self._balance

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
            self.acc_history.append('{0}{1} was withdrawed'.format(amount, self.currency))
            return True
        else:
            self.acc_history.append('Withdraw for {0}{1} failed.'.format(amount, self.currency))
            return False

    def __str__(self):
        return "Bank account for {0} with balance of {1}{2}".format(self.name, self._balance, self.currency)

    def __int__(self):
        self.acc_history.append('__int__ check -> {0}{1}'.format(self._balance, self.currency))
        return self._balance
    
    def transfer_to(self, account, amount):
        if self.currency == account.currency and self._balance - amount >= 0:
            # 1st step
            self._balance -= amount
            self.acc_history.append('Transfer to {0} for {1}{2}'.format(account.name, amount, self.currency))
            # 2cd step
            account._balance += amount
            account.acc_history.append('Transfer from {0} for {1}{2}'.format(self.name, amount, self.currency))
            return True

    def history(self):
        
        return self.acc_history

account = BankAccount("Rado", 0, "$")
print(account)
account.deposit(1000)
print(account.balance())
str(account)
int(account)
print(account.history())
print(account.withdraw(500))
print(account.balance())
print(account.history())
print(account.withdraw(1000))
print(account.balance())
print(account.history())
print(['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$', '500$ was withdrawed', 'Balance check -> 500$', 'Withdraw for 1000$ failed.', 'Balance check -> 500$'] == account.history())

rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))
print(rado.balance())
print(ivo.balance())
print(rado.history())
print(ivo.history())


print(rado.history() == ['Account was created', 'Transfer to Ivo for 500BGN', 'Balance check -> 500BGN'])
print(ivo.history() == ['Account was created', 'Transfer from Rado for 500BGN', 'Balance check -> 500BGN'])

['Account was created', 'Transfer to Ivo for 500BGN', 'Balance check -> 500$']






