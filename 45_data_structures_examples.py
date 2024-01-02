str = "This is an awesome occasion. This has never happened before."
print("----------------------- list comprehension -----------------------")
squares_first_ten_numbers = [i*i for i in range(1, 11)]
print(squares_first_ten_numbers)
print(type(squares_first_ten_numbers))
print("----------------------- normal set -----------------------")
squares_first_ten_numbers_set = set(squares_first_ten_numbers)
print(squares_first_ten_numbers_set)
print(type(squares_first_ten_numbers_set))
print("----------------------- set comprehension -----------------------")
# below is set comprehension
# curly braces denote set comprehension (square braces denote list comprehension)
squares_first_ten_numbers_set_2 = {i*i for i in range(1, 11)}
print(squares_first_ten_numbers_set_2)
print(type(squares_first_ten_numbers_set_2))
print("----------------------- dict comprehension -----------------------")
squares_first_ten_numbers_dict = {i: i*i for i in range(1, 11)}
print(squares_first_ten_numbers_dict)
print(type(squares_first_ten_numbers_dict))
print("----------------------- empty types -----------------------")
print(f"type([]): {type([])}")
print(f"type({{}}): {type({})}")
print(f"type(set()): {type(set())}")
print(f"type({{1}}): {type({1})}")
print(f"type({{'A': 5}}): {type({'A': 5})}")
print(f"type(()): {type(())}")
