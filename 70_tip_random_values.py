import random

print(random.random())
print(random.randint(1, 10))  # both are inclusive
print(random.randrange(1, 25, 2))
print(random.randrange(15, 35, 3))
print(random.randrange(0, 100, 5))

num_list = [2, 3, 7, 9, 56, 34, 23]
print(num_list)
print(random.choice(num_list))
print(random.choice('abcdefghijklmnopqrstuvwxyz'))
print(random.sample(num_list, 2))
print(random.sample(num_list, 3))
print(random.sample(num_list, 5))



