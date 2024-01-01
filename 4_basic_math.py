def print_squares_of_numbers_up_to(number):
    print("---------- squares ------------")
    for i in range(0, number):
        print(i * i)


def print_squares_of_even_numbers_up_to(number):
    print("---------- squares of even ------------")
    for i in range(0, number):
        if i % 2 == 0:
            print(i * i)


def print_numbers_in_reverse(number):
    print("---------- reverse ------------")
    for i in range(number, 0, -1):
        print(i)


def main():
    print("inside main")
    print_squares_of_numbers_up_to(10)
    print_squares_of_even_numbers_up_to(10)
    print_numbers_in_reverse(10)


if __name__ == "__main__":
    main()

# main()
