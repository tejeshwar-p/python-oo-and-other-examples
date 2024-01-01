def string_immutability_1():
    message = "Hello"
    print(f"message: {message}")
    print(f"message.upper(): {message.upper()}")
    print(f"message: {message}")


string_immutability_1()
# int, float, str and bool are immutable in python


def print_characters(string_value):
    for character in string_value:
        print(character)


# There is no character data type in python
print_characters("This is some string")

