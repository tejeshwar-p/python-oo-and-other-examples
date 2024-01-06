from functools import total_ordering


# In python, instead of implementing every >, <, etc comparisons
# most of them can be derived from implementations of other methods
# To do this we can use @total_ordering decorator.
# @total_ordering will automatically implement other
# there is performance implication if comparisons are done
# many times when @total_ordering is used.

@total_ordering
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

    def __gt__(self, other):
        return (self.currency, self.amount) > (other.currency, other.amount)

    # we can also compare like this -
    # def __gt__(self, other):
    #     return self.amount > other.amount


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

