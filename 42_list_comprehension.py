print("------------------------------- traditional way -------------------------------")
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(f"numbers: {numbers}")

numbers_length_four = []

for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)

print(f"numbers_length_four: {numbers_length_four}")
print("------------------------------- using list comprehension -------------------------------")
numbers_length_four = [number for number in numbers]
print(f"using 'number for number in numbers' - \n\tnumbers_length_four: {numbers_length_four}")
numbers_length_four = [len(number) for number in numbers]
print(f"using 'len(number) for number in numbers' - \n\tnumbers_length_four: {numbers_length_four}")
numbers_length_four = [number.upper() for number in numbers]
print(f"using 'number.upper() for number in numbers' - \n\tnumbers_length_four: {numbers_length_four}")
numbers_length_four = [number for number in numbers if len(number) == 4]
print(f"using 'number for number in numbers if len(number) == 4' - \n\tnumbers_length_four: {numbers_length_four}")
values = [3, 6, 9, 1, 4, 1, 6, 3]
print(values)
values_even = [value for value in values if value % 2 == 0]
print(values_even)
