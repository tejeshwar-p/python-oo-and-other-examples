import string


def print_string_module_methods():
    print(string.__all__)
    print(string.ascii_letters)
    print(string.ascii_uppercase)
    print(string.ascii_lowercase)
    print(string.capwords("this is some text"))
    print(string.capwords("this is   some text   with extra spaces"))
    print(string.capwords("this is other text", sep='t'))
    print(string.capwords("this is other text", sep='o'))
    print(string.digits)
    print(string.hexdigits)
    print(string.octdigits)
    print(string.printable)
    print(string.punctuation)
    print(string.whitespace)
    print("----------------------------")
    print('a' in string.ascii_letters)
    print('1' in string.ascii_letters)
    print('asdf' in string.ascii_letters)
    print('abcd' in string.ascii_letters)


print_string_module_methods()
