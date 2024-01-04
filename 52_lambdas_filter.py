numbers = [1, 89, 54, 34]
print(numbers)
print(f"filter(lambda x: x % 2 == 1, numbers): {list(filter(lambda x: x % 2 == 1, numbers))}")
print(f"filter(lambda x: x % 2 == 0, numbers): {list(filter(lambda x: x % 2 == 0, numbers))}")
print(f"filter(lambda x: x % 2, numbers): {list(filter(lambda x: x % 2, numbers))}")
print("--------------------------------------------------------------")
words = ["Apple", "Ant", "Bat"]
print(f"filter(lambda word: word.endswith('at'), words): {list(filter(lambda word: word.endswith('at'), words))}")
print(f"filter(lambda word: len(word) == 3, words): {list(filter(lambda word: len(word) == 3, words))}")
print(f"filter(lambda word: word.startswith('A'), words): {list(filter(lambda word: word.startswith('A'), words))}")
