def print_string_functions():
    print("-------------------- message1 -------------------")
    message1 = "Hello World"
    # message1 = 'Hello World'
    # is also considered as valid string in python.
    print(f"type of message1 is: {type(message1)}")
    print(f"upper(): {message1.upper()}")
    print(f"lower(): {message1.lower()}")

    print("-------------------- message2 -------------------")
    message2 = "hello"
    print(f"capitalize(): {message2.capitalize()}")
    print(f"capitalize() directly on strings: {'world'.capitalize()}")
    print(f"is_lower() for message2: {message2.islower()}")
    print(f"is_upper() for message2: {message2.isupper()}")

    print("-------------------- message3 -------------------")
    message3 = "this is a line"
    print(f"message3: {message3}")
    print(f"istitle() for message3: {message3.title()}")

    print("-------------------- message4 -------------------")
    message4 = "12345"
    print(f"message4: {message4}")
    print(f"isdigit: {message4.isdigit()}")
    print(f"isalpha: {message4.isalpha()}")
    message4 = "12345ABC"
    print(f"message4: {message4}")
    print(f"isalpha: {message4.isalpha()}")
    print(f"isalnum: {message4.isalnum()}")
    message4 = "12345 ABC"
    print(f"message4: {message4}")
    print(f"isalnum: {message4.isalnum()}")
    message4 = "ABC"
    print(f"message4: {message4}")
    print(f"isalpha: {message4.isalpha()}")

    print("-------------------- message5 -------------------")
    message5 = "Hello World Again"
    print(f"message5: {message5}")
    print(f"startswith(): {message5.startswith('H')}")
    print(f"find() for Again: {message5.find('Again')}")
    print(f"find() for World: {message5.find('World')}")
    print(f"find() for ABCD: {message5.find('ABCD')}")


print_string_functions()
