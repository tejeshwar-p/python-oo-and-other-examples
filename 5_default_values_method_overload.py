def print_multiplication_table(table, start, end):
    for i in range(start, end + 1):
        print(f"{table} x {i} = {table * i}")
    print("--------------------------------------------")


print_multiplication_table(7, 1, 10)


def print_multiplication_table_def_value(table, start=10, end=20):
    for i in range(start, end + 1):
        print(f"{table} x {i} = {table * i}")
    print("--------------------------------------------")


print_multiplication_table_def_value(9)

print_multiplication_table_def_value(5, 1, 10)
