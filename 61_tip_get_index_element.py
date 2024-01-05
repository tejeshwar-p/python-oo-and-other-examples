numbers = [1, 4, 6, 7, 9, 0, 3]
print(numbers)
print("----------------------- print values -----------------------")
for number in numbers:
    print(number)
print("----------------------- print indexes and values -----------------------")
for index, number in enumerate(numbers):
    print(f"{index} - {number}")
print("----------------------- print indexes and values -----------------------")
vowel_list = list("aeiou")
print(vowel_list)
for index, vowel in enumerate(vowel_list):
    print(f"{index} - {vowel}")


