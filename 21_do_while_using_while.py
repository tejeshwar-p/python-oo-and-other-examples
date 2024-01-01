def print_cube_for_positive_numbers():
    number = 0
    while number >= 0:
        number = input("Enter a number: ")
        number = int(number)
        if number >= 0:
            print(f"Cube is: {number*number*number}")
    print("Exiting for negative numbers. Thank you!!")


print_cube_for_positive_numbers()
