from functools import reduce

numbers = [3, 9, 7, 8, 15, 5, 24, 47, 35, 69, 75]
print(numbers)
# take even numbers, square and add them

# [8, 24] -> [64, 576] -> 640
print(f"reduce(lambda x, y: x + y, map(lambda eno: eno * eno, filter(lambda no: no % 2 == 0, numbers))): "
      f"{reduce(lambda x, y: x + y, map(lambda eno: eno * eno, filter(lambda no: no % 2 == 0, numbers)))}")

print("----------------------------------------------------")
months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]
print(months)
tuple_ex = ('Dec', 31)
print(tuple_ex)
print(f"tuple_ex[0]: {tuple_ex[0]}")
print(f"tuple_ex[1]: {tuple_ex[1]}")
# Find the sum of all the no. of days in the months tuple array
print(f"sum(list(map(lambda tup: tup[1], months))): "
      f"{sum(list(map(lambda tup: tup[1], months)))}")
print(f"reduce(lambda x, y: x + y, list(map(lambda tup: tup[1], months))): "
      f"{reduce(lambda x, y: x + y, list(map(lambda tup: tup[1], months)))}")
# get the tuple with the least no. of days from months tuple array
print(f"reduce(lambda x, y: x if x[1] < y[1] else y, months): "
      f"{reduce(lambda x, y: x if x[1] < y[1] else y, months)}")
print(f"reduce(lambda x, y: x if x[1] < y[1] else y, months): "
      f"{reduce(lambda x, y: x if x[1] < y[1] else y, months)[0]}")
print(f"reduce(lambda x, y: x if x[1] < y[1] else y, months): "
      f"{reduce(lambda x, y: x if x[1] < y[1] else y, months)[1]}")

