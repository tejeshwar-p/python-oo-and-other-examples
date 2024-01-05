import datetime

now_date_time = datetime.datetime.today()
print(f"now_date_time: {now_date_time}")
print(f"now_date_time.__str__(): {now_date_time.__str__()}")
print(now_date_time.__repr__())
print()
some_date_time = datetime.datetime(2018, 9, 27, 23, 10, 12, 234570)
print(f"some_date_time: {some_date_time}")
print(f"some_date_time.__str__(): {some_date_time.__str__()}")
print(f"some_date_time.__repr__(): {some_date_time.__repr__()}")

# repr tells us how to create new object with that value printed by __repr__() method

# It is good practice to provide __repr__ for custom classes
# to inform users how to create new object
# If implementation is provided for __repr__ and
# NO implementation is provided for __str__ then __str__ uses __repr__ internally




