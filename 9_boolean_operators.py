is_done = True


def print_is_done():
    if is_done:
        print(is_done)
    print("----------------------------")


print_is_done()


def print_boolean_combinations():
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"False and True: {False and True}")
    print(f"False and False: {False and False}")
    print(f"not True: {not True}")
    print(f"not False: {not False}")
    print(f"True ^ True: {True ^ True}")
    print(f"True ^ False: {True ^ False}")
    print(f"False ^ True: {False ^ True}")
    print(f"False ^ False: {False ^ False}")
    i = 5
    print(f"i == 5: {i == 5}")
    print(f"i >= 5: {i >= 5}")
    print(f"i <= 5: {i <= 5}")
    print(f"i > 5: {i > 5}")
    print(f"i < 5: {i < 5}")


print_boolean_combinations()
