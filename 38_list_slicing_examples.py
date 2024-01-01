numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers)
print(len(numbers))
print(f"numbers[2]: {numbers[2]}")
print(f"numbers[2:6]: {numbers[2:6]}")
print(f"numbers[:6]: {numbers[:6]}")
print(f"numbers[3:]: {numbers[3:]}")
print(f"numbers[1:8:2]: {numbers[1:8:2]}")
print(f"numbers[1:8:3]: {numbers[1:8:3]}")
print(f"numbers[::3]: {numbers[::3]}")
# start from reverse
print(f"numbers[::-1]: {numbers[::-1]}")
print(f"numbers[::-3]: {numbers[::-3]}")
del numbers[3:]
print(numbers)
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
del numbers[5:7]
print(numbers)
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers[3:7] = [3, 4, 5, 6]
print(numbers)


