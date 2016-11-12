# cashdesl.py
class Bill:
    
    def __init__(self, amount):
        self.amount = amount
        if self.amount < 0:
            raise ValueError()
        if type(self.amount) != int:
            raise TypeError()


    def __str__(self):
        return "A %d$ bill" % (self.amount)

    def __repr__(self):
        return "%d$ bills" % (self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == int(other)

    def __hash__(self):
        return hash(repr(self.amount))

class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def total(self):
        return sum(int(i) for i in self.bills)

    def __len__(self):
        return len(self.bills)
    

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:

    def __init__(self):
        self.money_holder = {}

    def take_money(self, money):
        self.money = money
        if isinstance(self.money, Bill):
            if self.money not in self.money_holder:
                self.money_holder[self.money] = 1
            else:
                self.money_holder[self.money] += 1
        else:
            for i in self.money:
                if i not in self.money_holder:
                    self.money_holder[i] = 1
                else:
                    self.money_holder[i] += 1

    def total(self):
        return sum(int(k)*v for k,v in self.money_holder.items())

    def inspect(self):
        result = ''
        result += "We have a total of %d$ in the desk\n"% self.total()
        result += "We have the following count of bills, sorted in ascending order:\n"
        smth = sorted([key for key in self.money_holder.keys()], key=lambda x: int(x))
        count = len(smth)
        for i in smth:
            result += repr(i) + ' - ' + str(self.money_holder[i])
            count -= 1
            if count > 0:
                result += '\n'
        return result


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total()) # 390
print(desk.inspect())



