# In python functions are first class citizens
# check below examples to understand more.
# on high level it means functions are like objects and can be passes around

def multiply_by_2(data):
    return data*2


# here we can see that it is like an object stored at a specific memory location
# so this function can be passed to another function!
print(multiply_by_2)


def do_this_and_print(func, data):
    print(func(data))


do_this_and_print(multiply_by_2, 12)

func_example_reference = multiply_by_2
print(func_example_reference(23))
