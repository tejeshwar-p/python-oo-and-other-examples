from collections import deque

queue = deque(['Zero', 'One', 'Two', 'Three'])
print(queue)
print(f"queue.pop(): {queue.pop()}")
queue.append('Four')
queue.append('Five')
queue.append('Six')
print(queue)
queue.appendleft('Minus One')
print(queue)
print(f"queue.popleft(): {queue.popleft()}")
print(queue)


