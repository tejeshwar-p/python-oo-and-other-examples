class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, that):
        if self.currency == that.currency:
            self.amount += that.amount
        else:
            # raise Exception('Currency does not match')
            raise CurrencyDoesNotMatchException(self.currency+" "+that.currency)

    def __repr__(self):
        return repr((self.currency, self.amount))


class CurrencyDoesNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)


print("-----------------------------------------------------")
amount1 = Amount('EUR', 35)
amount2 = Amount('EUR', 91)

amount2.add(amount1)
print(amount2)
print("-----------------------------------------------------")
amount1 = Amount('EUR', 35)
amount2 = Amount('USD', 91)

amount2.add(amount1)
print(amount2)
print("-----------------------------------------------------")