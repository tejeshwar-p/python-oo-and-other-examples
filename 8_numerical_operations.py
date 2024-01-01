# The result of division in python is always a floating point type
# In Java however, the result of division is integer type
# In python there are no pre increment (++) or (--) operators
# We have to do either num += 1 or num = num + 1
def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def division_only_integer(num1, num2):
    return num1 // num2


def power_of_number(num, power):
    return num ** power


def power_of_number_by_pow(num, power):
    return pow(num, power)


print(addition(2, 3))
print(subtraction(10, 3))
print(multiplication(9, 9))
print(division(10, 2))
print(division_only_integer(20, 6))
print(power_of_number(10, 2))
print(power_of_number_by_pow(10, 3))
print(max(34, 23, 5, 6, 67, 2, 90, 89, 91, 30))
print(min(34, 23, 5, 6, 67, 2, 90, 89, 91, 30))
print(round(5.6))
print(round(5.6817687684, 3))
print(float(7))
print(int(7.77))

