def traditional_if(number):
    if number % 2 == 0:
        is_even = True
    else:
        is_even = False
    print(f"Is {number} even?: {is_even}")


traditional_if(11)


def enhanced_if(number):
    is_even = True if number % 2 == 0 else False
    print(f"Is {number} even?: {is_even}")


enhanced_if(11)
