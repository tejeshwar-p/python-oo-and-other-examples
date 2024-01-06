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

    def __gt__(self, other):
        return (self.currency, self.amount) > (other.currency, other.amount)

    # we can also compare like this -
    # def __gt__(self, other):
    #     return self.amount > other.amount

    def __ge__(self, other):
        return (self.currency, self.amount) >= (other.currency, other.amount)

    def __lt__(self, other):
        return (self.currency, self.amount) < (other.currency, other.amount)

    # we can also compare like this -
    # def __lt__(self, other):
    #     return self.amount < other.amount

    def __le__(self, other):
        return (self.currency, self.amount) <= (other.currency, other.amount)


amount1 = Money('AUD', 10)
amount2 = Money('EUR', 10)
amount3 = Money('AUD', 10)
amount4 = Money('AUD', 20)
# A is considered smaller than E
print(f"amount1 > amount2: {amount1 > amount2}")
print(f"amount2 > amount3: {amount2 > amount3}")
print(f"amount3 > amount1: {amount3 > amount1}")
print("----------------------------------------------")
print(f"amount1 > amount2: {amount1 < amount2}")
print(f"amount2 > amount3: {amount2 < amount3}")
print(f"amount3 > amount1: {amount3 < amount1}")
print("----------------------------------------------")
print(f"amount1 >= amount3: {amount1 >= amount3}")
print(f"amount4 >= amount1: {amount4 >= amount1}")
print("----------------------------------------------")
print(f"amount1 <= amount3: {amount1 <= amount3}")
print(f"amount4 <= amount1: {amount4 <= amount1}")
