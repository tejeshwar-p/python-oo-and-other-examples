def first_example():
    for i in range(1, 10):
        print(i)


def is_prime_number(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % 2 == 0:
            return False
    return True


def sum_up_to_n_number(number):
    final_sum = 0
    if number > 0:
        for i in range(0, number+1):
            final_sum += i
    else:
        return "Please enter numbers greater than 0"
    return final_sum


def sum_of_divisors(number):
    final_sum = 0
    if number > 0:
        for i in range(1, number + 1):
            if number % i == 0:
                final_sum += i
    else:
        return "Please enter number greater than 0"
    return final_sum


first_example()
print(is_prime_number(19))
print(sum_up_to_n_number(100))
print(sum_of_divisors(10))
