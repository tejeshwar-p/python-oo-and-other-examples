# import decimal
from decimal import Decimal
import math

# The below value is not accurate when the built - in float is used
print(4.5 - 3.2)  # prints 1.2999999999999998 which is not correct
# value1 = decimal.Decimal('4.5')
value1 = Decimal('4.5')
value2 = Decimal('3.2')
print(value1 - value2)
print("Always use Decimal class for accurate decimal values, especially in financial calculations")
print("----------------------------------------")
print(math.pi)
print(math.e)


