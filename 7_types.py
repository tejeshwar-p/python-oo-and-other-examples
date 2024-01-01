# Everything in python is an object
# Even different primitive looking values are objects
# Python is strongly typed and dynamic language
a = 123456
print("a = ")
print(type(a))

b = 123.456
print("b = ")
print(type(b))

c = "123.456"
print("c = ")
print(type(c))

d = True
print("d = ")
print(type(d))

e = False
print("e = ")
print(type(e))

a = "123456"
print("a = ")
print(type(a))

# From the above example we can see that a, b, c, d, e don't have any
# declared types. Also type of 'a' has changed dynamically during runtime
# from int to string. Hence, it is dynamically typed language.
# But every object in python has a type. Hence, it is strongly typed.
# Once an object has a type all the rules of that type apply to that object
# It means we will not be able to call any other methods of other type
# on that object.
