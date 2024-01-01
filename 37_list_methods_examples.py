animals = ['cat', 'dog', 'elephant', 'deer']
print(len(animals))
# Below sum, min, max will give errors
# because sum, min and max are not defined for string data type
# print(sum(animals))

# max will give the element having maximum alphabet order
print(max(animals))
# min will give the element having minimum alphabet order
print(min(animals))

animals.append('fish')
print(animals)

# To remove element by value
animals.remove('dog')
print(animals)

print(animals[2])
print(animals[0])

# incorrect index will give error - IndexError: list index out of range
# print(animals[10])

# To remove element by index
del animals[1]
print(animals)

animals.extend('giraffe')
print(animals)
animals.append('giraffe')
print(animals)
animals.extend(['horse', 'peacock'])
print(animals)
animals = animals + ['rabbit', 'eagle']
print(animals)
animals = animals + ['lion', 'monkey']
print(animals)

# In python there are no data type restrictions for list
animals.append(20)
print(animals)

