def convert_type_str_bool():
    print(f"str(True): {str(True)}")
    print(f"bool('True'): {bool('True')}")
    print(f"bool('true'): {bool('true')}")
    print(f"bool('tru'): {bool('tru')}")
    print(f"bool('false'): {bool('false')}")
    print(f"bool('False'): {bool('False')}")
    print(f"bool(''): {bool('')}")
    print("------------------------------------")


# any string content represents true for bool function
# only empty string is false for bool function


convert_type_str_bool()


def convert_type_str_int():
    print(f"str(123): {str(123)}")
    print(f"str(12345): {str(12345)}")
    print(f"str('456'): {str('456')}")
    print(f"str(456.789): {str(456.789)}")
    print(f"str('456.789'): {str('456.789')}")
    print(f"int('55'): {int('55')}")
    # Below conversion will not work - ValueError: invalid literal for int() with base 10: '55.67'
    # print(f"int('55.67'): {int('55.67')}")
    # print(f"int('5567asdf'): {int('5567asdf')}")
    # Convert to hexadecimal
    print(f"int('57abc'): {int('57abc', 16)}")
    print("------------------------------------")


convert_type_str_int()


def convert_type_str_float():
    print(f"float('34.56'): {float('34.56')}")
    # ValueError: could not convert string to float: '34.56ab'
    # print(f"float('34.56ab'): {float('34.56ab')}")


convert_type_str_float()
