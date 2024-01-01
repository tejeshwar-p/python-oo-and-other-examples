class Book:

    def __init__(self, name, copies, copies_count=0):
        # This is an instance variable
        self.name = name
        self.copies = copies
        self.copies_count = copies_count

    def __repr__(self):
        return repr((self.name, self.copies))

    def increase_no_of_copies(self, copies_count):
        self.copies = self.copies + copies_count

    def decrease_no_of_copies(self, copies_count):
        self.copies = self.copies - copies_count


book1 = Book("Mastering Java", 200)
book1.increase_no_of_copies(50)
book2 = Book("Mastering Python", 100)
book2.decrease_no_of_copies(10)

print(book1)
print(book2)
