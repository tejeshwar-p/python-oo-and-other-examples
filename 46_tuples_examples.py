
def create_someone():
    return 'Someone', 1990, 'India'


someone_obj = create_someone()
print(type(someone_obj))
print("---------------------------------------")
name, year, country = someone_obj
print(someone_obj)
print(name)
print(year)
print(country)
print("---------------------------------------")
print(len(someone_obj))
print(someone_obj[0])
print(someone_obj[1])
print(someone_obj[2])
print("---------------------------------------")
# tuple does not support item assignment. It is read only once created.
# tuple is immutable

# TypeError: 'tuple' object does not support item assignment
# someone_obj[1] = 1991
# print(someone_obj[1])
print("---------------------------------------")
# accessing values from tuple is efficient than accessing values from list
person = ('John Doe', 20, 'India')
print(type(person))
name, age, country = person
print(name, age, country)
print("---------------------------------------")
# below line will throw error - ValueError: too many values to unpack (expected 2)
# because no. of values to be assigned is less than the values which the tuple has.
# name, age = person
# print(name, age)
print("---------------------------------------")
x = 0
y = 1
x, y = 0, 1
x, y = y, x
print(x, y)
print("---------------------------------------")
# how to create tuple with only one element?
x = (0)  # this will not work because it will be considered as int
print(type(x))
x = (0,)  # this will be considered as tuple
print(type(x))

