class Book:
    # This is a class variable (like static in Java)
    default_name = "This is default name"

    def __init__(self, name, copies):
        # This is an instance variable
        self.name = name
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))


book1 = Book("Mastering Java", "200")
book2 = Book("Mastering Python", "100")

print(book1)
print(book2)
