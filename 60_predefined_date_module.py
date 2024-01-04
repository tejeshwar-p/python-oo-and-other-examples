import datetime

print(datetime.datetime.today())
today_date = datetime.datetime.today()
print(f"today_date: {today_date}")
print(f"today_date.year: {today_date.year}")
print(f"today_date.month: {today_date.month}")
print(f"today_date.hour: {today_date.hour}")
print(f"today_date.minute: {today_date.minute}")
print(f"today_date.second: {today_date.second}")
print(f"today_date.microsecond: {today_date.microsecond}")
print("-----------------------------------------------------")
some_date_1 = datetime.datetime(2019, 12, 30)
print(f"some_date: {some_date_1}")
some_date_2 = datetime.datetime(2019, 12, 30, 0, 0)
print(f"some_date_2: {some_date_2}")
some_date_3 = datetime.datetime(2019, 12, 30, 5, 30, 0)
print(f"some_date_3: {some_date_3}")
some_date_4 = datetime.datetime(2019, 12, 30, 5, 30, 5, 234567)
print(f"some_date_3: {some_date_4}")
print(f"some_date_4.date(): {some_date_4.date()}")
print(f"some_date_4.time(): {some_date_4.time()}")
copy_some_date_4 = some_date_4
print(some_date_4)
copy_some_date_4 + datetime.timedelta(days=90)
print(copy_some_date_4 + datetime.timedelta(days=90))
# original value of some_date_4 will not be modified



