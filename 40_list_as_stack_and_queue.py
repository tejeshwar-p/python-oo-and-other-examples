# Stack is last in first out - LIFO
# Queue is first in first out - FIFO

# use append() to insert into stack and pop() to pop out of stack
print("----------------- list as stack -----------------")
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers)
print(numbers.pop())
print(numbers)
print(numbers.pop())
print(numbers)
numbers.append(10)
print(numbers.pop())
print(numbers)

print("----------------- list as queue -----------------")
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers)
print(numbers.pop(0))
print(numbers)
numbers.append(10)
print(numbers)
print(numbers.pop(0))
print(numbers)
print(numbers.pop(0))
print(numbers)


