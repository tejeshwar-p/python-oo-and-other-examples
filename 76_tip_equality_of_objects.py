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

    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency, other.amount)

    # Not mandatory to implement this method
    def __ne__(self, other):
        return (self.currency, self.amount) != (other.currency, other.amount)


print(f"(1, 1) == (1, 1): {(1, 1) == (1, 1)}")
print(f"('1', 1) == ('1', 1): {('1', 1) == ('1', 1)}")
print(f"('1', 1) == ('1', 2): {('1', 1) == ('1', 2)}")
print(f"('1', 1) == ('2', 1): {('1', 1) == ('2', 1)}")
print(f"(1, 1) > (1, 1): {(1, 1) > (1, 1)}")
print(f"(1, 1) > (0, 1): {(1, 1) > (0, 1)}")
print(f"(1, 2) > (1, 1): {(1, 2) > (1, 1)}")
print(f"(1, 2) > (1, 3): {(1, 2) > (1, 3)}")
print(f"(1, 2) > (1, 3): {(1, 2) < (1, 3)}")

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)
print(f"amount1 == amount2: {amount1 == amount2}")
print(f"amount1 != amount2: {amount1 != amount2}")
print(f"amount1 == amount3: {amount1 == amount3}")
print(f"amount1 != amount3: {amount1 != amount3}")
# print(amount1 > amount2)
# print(amount1 < amount2)


