words = ['Apple', 'And', 'Bat']
print('Apple'.upper())

# map to uppercase (transformation)
# map will not change the number of values.
# map might change the data type of the values.
print(f"list(map(lambda word: word.upper(), words)): "
      f"{list(map(lambda word: word.upper(), words))}")

print(f"list(map(lambda word: len(word), words)): "
      f"{list(map(lambda word: len(word), words))}")

numbers = [1, 5, 2, 9]
print(numbers)
print(f"list(map(lambda number: number*number, numbers)): "
      f"{list(map(lambda number: number * number, numbers))}")

# numbers = [number for number in range(1, 11)]
print(f"list(map(lambda no: no*no, range(1, 11))): "
      f"{list(map(lambda no: no * no, range(1, 11)))}")
print(f"list(map(lambda no: no*no, [number for number in range(1, 11)])): "
      f"{list(map(lambda no: no * no, [number for number in range(1, 11)]))}")
