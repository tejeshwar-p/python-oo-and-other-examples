# In Java, If we allow direct access to instance variables,
# we would need to change client code (code using BookEnhanced class)
# if we need to add validations later
# For ex - if we want to make sure that the copies of book should not
# be changed to -100 we have to make copies private
# and add getter and setter methods. This is the only way to make sure
# the client code (code using BookEnhanced class) is not changed.
# This is the reason that by default almost all the Java data classes have
# getters and setters.
# But in Python, we can add logic at later point in time without modifying
# the client code (code using BookEnhanced class)
# We can add checks on copies without touching how the
# setting of copies is done in client code using property decorators

class BookEnhanced:
    def __init__(self, name, copies):
        self.name = name
        self._copies = copies  # underscore says it is a protected value
        # and should not be accessed directly. It is convention.

    @property
    def copies(self):
        print('getter called')
        return self._copies

    @copies.setter
    def copies(self, copies):
        print('setter called')
        if copies >= 0:
            self._copies = copies


microservices = BookEnhanced('Microservices', 5)
print(microservices.copies)
microservices.copies = 10
print(microservices.copies)
