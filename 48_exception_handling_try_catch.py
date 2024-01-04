try:
    i = 0
    number = 10/i
except ZeroDivisionError:
    number = 0
except ValueError:
    number = 1

print(number)
print("----------------------------------------")
try:
    i = 0
    number = 10/i
except (ZeroDivisionError, ValueError):
    number = 0

print(number)
print("----------------------------------------")
try:
    # i = 1  # will not throw
    i = 0
    number = 10/i
except ZeroDivisionError as zdError:
    print(zdError)
    number = 0
else:
    print('else')  # else will be executed when exception does not happen
finally:
    print('finally')

print(number)
