# set does not allow duplicates (similar to Java set)
numbers = [1, 3, 4, 2, 5, 3, 2]
print(f"numbers: {numbers}")
numbers_set = set(numbers)
print(f"numbers_set: {numbers_set}")
numbers_set.add(2)
print(f"adding 2 - numbers_set: {numbers_set}")
numbers_set.add(0)
print(f"adding 0 - numbers_set: {numbers_set}")
numbers_set.remove(0)
print(f"removing 0 - numbers_set: {numbers_set}")
# set does not support access by index like list
# below code will throw error - TypeError: 'set' object does not support indexing
# print(numbers_set[0])
print(f"2 in numbers_set: {2 in numbers_set}")
print(f"6 in numbers_set: {6 in numbers_set}")
print(f"max(numbers_set): {max(numbers_set)}")
print(f"min(numbers_set): {min(numbers_set)}")
print(f"sum(numbers_set): {sum(numbers_set)}")
print(f"len(numbers_set): {len(numbers_set)}")
numbers_1_to_5_set = set(range(1, 6))
print(f"set(range(1, 6)) - numbers_1_to_5_set: {numbers_1_to_5_set}")
numbers_4_to_10_set = set(range(4, 11))
print(f"set(range(4, 11)) - numbers_4_to_10_set: {numbers_4_to_10_set}")
# we CANNOT combine two sets using '+' operator
# we have to use pipe symbol '|'
# pipe symbol '|' does union of both the sets (also removes duplicates)
print("----------------------- set union -----------------------")
print(f"numbers_1_to_5_set | numbers_4_to_10_set: {numbers_1_to_5_set | numbers_4_to_10_set}")
print("----------------------- set intersection -----------------------")
# to do intersection we have to use ampersand '&' symbol
print(f"numbers_1_to_5_set & numbers_4_to_10_set: {numbers_1_to_5_set & numbers_4_to_10_set}")
print("----------------------- set subtraction -----------------------")
# subtraction removes the common elements from 1st set and all elements from 2nd set
print(f"numbers_1_to_5_set - numbers_4_to_10_set: {numbers_1_to_5_set - numbers_4_to_10_set}")
print(f"numbers_4_to_10_set - numbers_1_to_5_set: {numbers_4_to_10_set - numbers_1_to_5_set}")
