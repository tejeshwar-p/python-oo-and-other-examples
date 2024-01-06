# Since python does not switch statement like in Java alternatives
# are to use either if elsif ladder or use a dictionary like below

week_days = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

print(week_days.get(7, 'Invalid_day'))

