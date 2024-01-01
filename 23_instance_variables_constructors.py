# variables inside class is not instance variable. Its class variable
# If we want instance variables we have to define them inside constructor

# Two ways for toString() method similar to Java in python -> str, repr

class Book:
    # This is a class variable (like static in Java)
    default_name = "This is default name"

    def __init__(self, name):
        # This is an instance variable
        self.name = name

    def __repr__(self):
        return repr(self.name)


book1 = Book("Mastering Java")
book2 = Book("Mastering Python")

print(book1)
print(book2)
