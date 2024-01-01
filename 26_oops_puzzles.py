# For all the constructors and instance methods 'self' is mandatory
class Country:

    # here name of argument representing the object's instance can be 'self'
    # or any other name but convention is using 'self'
    def __init__(self):
        print("constructor")

    def some_instance_method(self):
        print("some instance method")


india = Country()
india.some_instance_method()

# There is NO constructor overloading in python!
# However, we can do like this below for kind of constructor overloading
# by passing default values for optional parameters


class State:
    def __init__(self, name="Nowhere State"):
        self.name = name
        print(name)


state1 = State()
state2 = State("AP")


