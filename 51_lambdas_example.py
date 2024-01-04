def multiply_by_2(data):
    return data*2


print(multiply_by_2)


def do_this_and_print(func, data):
    print(func(data))


do_this_and_print(multiply_by_2, 12)

func_example_reference = multiply_by_2
print(func_example_reference(23))

print("------------------------- traditional way for passing functions -------------------------")


def multiply_by_3(data):
    return data * 3


do_this_and_print(multiply_by_3, 125)

print("------------------------- using lambdas for passing functions -------------------------")
do_this_and_print(lambda data: data*3, 125)
do_this_and_print(lambda data: data*5, 125)
do_this_and_print(lambda data: data*data, 125)
do_this_and_print(lambda data: data**3, 125)
do_this_and_print(lambda data: len(data), 'Something')
