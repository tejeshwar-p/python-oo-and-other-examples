from functools import reduce

numbers = [3, 15, 12, 10]
print(numbers)
print(f"sum(numbers): {sum(numbers)}")
print(f"max(numbers): {max(numbers)}")

print(f"reduce(lambda x, y: x+y, numbers): "
      f"{reduce(lambda x, y: x + y, numbers)}")
print(f"reduce(lambda x, y: x*y, numbers): "
      f"{reduce(lambda x, y: x * y, numbers)}")
print(f"reduce(lambda x, y: max(x, y), numbers): "
      f"{reduce(lambda x, y: max(x, y), numbers)}")
print(f"reduce(lambda x, y: min(x, y), numbers): "
      f"{reduce(lambda x, y: min(x, y), numbers)}")

print("----------------------------------------------------------")
words = ['Apple', 'Ant', 'Bat']
print(words)
print(f"reduce(lambda x, y: x if len(x) > len(y) else y, words): "
      f"{reduce(lambda x, y: x if len(x) > len(y) else y, words)}")
