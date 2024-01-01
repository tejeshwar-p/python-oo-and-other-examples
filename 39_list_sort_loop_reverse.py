numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers)
print("---------------------------------------------------------------")
# numbers.revers() is an inplace reverse.
# It means it will change the original list
numbers.reverse()
print(numbers)
print("---------------------------------------------------------------")
# If we do not want inplace reversed list, we can use reversed method
# for ex -
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
another_numbers = reversed(numbers)
print(another_numbers)
for number in another_numbers:
    print(number)
print("---------------------------------------------------------------")
# numbers.sort() does an inplace sort.
numbers.sort()
print(numbers)
print("---------------------------------------------------------------")
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# If we do not want inplace sorted list, we can use sorted() method
for number in sorted(numbers):
    print(number)
print("---------------------------------------------------------------")
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# Here sorting will be performed based on the length of the element
for number in sorted(numbers, key=len):
    print(number)
print("---------------------------------------------------------------")
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# Here sorting will be performed based on the length of the element + reverse
for number in sorted(numbers, key=len, reverse=True):
    print(number)
print("---------------------------------------------------------------")
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.sort(key=len, reverse=True)
print(numbers)


