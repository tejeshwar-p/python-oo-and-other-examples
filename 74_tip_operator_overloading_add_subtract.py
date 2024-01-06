# Operator overloading is only present in Python and not in Java
i = 1  # this is an object
j = 2  # this is an object

print(i + j)  # adding two objects


class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))


amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
# without implementing __add__ it will print below error when we try to add
# TypeError: unsupported operand type(s) for +: 'Money' and 'Money'
print(amount1 + amount2)
print(amount2 - amount1)
