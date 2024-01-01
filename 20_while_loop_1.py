def first_example():
    i = 0
    while i < 11:
        print(i)
        i += 1
    return i  # final loop count


final_loop_count = first_example()
print(f"final_loop_count: {final_loop_count}")


# print all the squares of numbers < 100
# 1, 4, 9, 16, 25
def squares_of_numbers_up_to(number):
    i = 1
    while i < number:
        print(i * i)
        i += 1


squares_of_numbers_up_to(100)
