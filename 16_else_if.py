def get_the_inputs():
    print("inside get_the_inputs()")
    input_value = input("Enter a number: ")
    input_value = int(input_value)
    traditional_if(input_value)


def traditional_if(number):
    if number == 1:
        print(f"number is {number}")
    elif number == 2:
        print(f"number is {number}")
    elif number == 3:
        print(f"number is {number}")
    elif number == 4:
        print(f"number is {number}")
    elif number == 5:
        print(f"number is {number}")
    else:
        print(f"number is greater than 5")


get_the_inputs()


# traditional_if(2)
# traditional_if(5)
# traditional_if(11)
