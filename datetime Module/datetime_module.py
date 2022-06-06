""" Lecture: datetime Module

    Outlines:
    How to Define Date, Time and Date and Time
    How to Parse a String into Date and Time
    How to Convert Date and Time Into a String
    Date and Time Arithmetic

"""

from datetime import time, date, datetime, timedelta

from dateutil import tz


def show_date_and_time(date_time):
    print()
    ty1 = type(date_time)
    print('The type is : ', ty1)
    print('The value is : ', date_time)

    if type(date_time) is date or type(date_time) is datetime:
        year1 = date_time.year
        month1 = date_time.month
        day1 = date_time.day
        print('The year is : ', year1)
        print('The month is : ', month1)
        print('The day is : ', day1)

    if type(date_time) is time or type(date_time) is datetime:
        hour1 = date_time.hour
        minute1 = date_time.minute
        second1 = date_time.second
        print('The hour is : ', hour1)
        print('The minutes are : ', minute1)
        print('The seconds are : ', second1)

    print()


# 1- How to Define Date, Time and Date and Time
# Date
# - Using date class

my_date1 = date(1996, 12, 11)
ty = type(my_date1)
print('The type is : ', ty)
print('The value is : ', my_date1)
year = my_date1.year
month = my_date1.month
day = my_date1.day

print('The year is : ', year)
print('The month is : ', month)
print('The day is : ', day)

# - Get today date

"""
date.today() -> date object
Returns the current date or datetime.
"""
my_date2 = date.today()
show_date_and_time(my_date2)

# Time
# - Using time class
my_time = time(13, 24, 56)
ty2 = type(my_time)
print('The type is : ', ty2)
print('The value is : ', my_time)

hour = my_time.hour
minute = my_time.minute
second = my_time.second

print('The hour is : ', hour)
print('The minutes are : ', minute)
print('The seconds are : ', second)

# Date and Time
# - Using datetime class
my_date_time1 = datetime(1996, 12, 11, 13, 24, 56)
show_date_and_time(my_date_time1)

# - using combine

"""
datetime.combine(date, time) -> datetime object
Returns datetime object created from data and time objects.

"""
my_date = date(1996, 12, 11)
my_time = time(13, 24, 56)
my_date_time2 = datetime.combine(my_date, my_time)
show_date_and_time(my_date_time2)

# - Get the current date and time (in your area)

"""
datetime.now(tz=None) -> datetime object
Returns datetime object representing the current date and time.

"""
now = datetime.now()
show_date_and_time(now)

# - Get the current date and time (in your area)
now = datetime.now(tz=tz.tzlocal())
now_res = now.tzname()
print(now_res)

# - Get the current date and time (in a different area)
now = datetime.now(tz=tz.gettz("Europe/Paris"))
show_date_and_time(now)

# - Get the current date and time in UTC

"""
datetime.utcnow() -> datetime object
Returns a new datetime representing UTC date and time.
"""

utc_now = datetime.utcnow()
show_date_and_time(utc_now)

# 2- How to Parse a String into Date and Time

"""
datetime.strptime(string, format) -> datetime object
Returns a new datetime object parsed from a string.

"""

# Example 1
date_time_str = "30-5-1992 14:45:37"
date_time_format = "%d-%m-%Y %H:%M:%S"  # It is pre-defined symbols (https://strftime.org/)

my_date_time = datetime.strptime(date_time_str, date_time_format)
show_date_and_time(my_date_time)

# Example 2
date_str = "30-5-1992"
date_format = "%d-%m-%Y"  # It is pre-defined symbols (https://strftime.org/)

my_date = datetime.strptime(date_str, date_format)
ty4 = type(my_date)
print(ty4)  # It is datetime
print(my_date)

my_date = my_date.date()  # It is date
ty5 = type(my_date)
print(ty5)
print(my_date)
print()

# Example 3
time_str = "14:45:37"
time_format = "%H:%M:%S"  # It is pre-defined symbols (https://strftime.org/)

my_time = datetime.strptime(time_str, time_format)
ty3 = type(my_time)
print(ty3)  # It is datetime
print(my_time)

my_time = my_time.time()  # It is date
ty4 = type(my_time)
print(ty4)
print(my_time)
print()

# 3- How to Convert Date and Time Into a String

"""
datetime.strftime(format) -> string
Returns a string representing the date, controlled by an explicit format string.
"""

# Example 1 (date ant time)
my_date_time = datetime(1996, 12, 11, 13, 24, 56)
print('The default format : ', my_date_time)

formatted_date_time1 = my_date_time.strftime('%d/%m/%Y %H-%M-%S')
print(formatted_date_time1)

formatted_date_time2 = my_date_time.strftime('Time: %H-%M-%S Date: %d/%m/%Y')
print(formatted_date_time2)

# Example 2 (date only)
my_date = date(1996, 12, 11)
formatted_date = my_date.strftime('Date: %d - %m - %Y')
print(formatted_date)

# Example 3 (time only)
my_time = time(13, 24, 56)
formatted_time = my_time.strftime('Time: %H :: %M :: %S')
print(formatted_time)

# 4- Date and Time Arithmetic
# Example 1
my_date_time1 = datetime(1996, 12, 11, 13, 24, 56)
my_date_time2 = datetime(1996, 12, 15, 14, 24, 56)

time_diff = my_date_time2 - my_date_time1
ty = type(time_diff)
print(ty)
print(time_diff)

# Example 2
my_date1 = date(1996, 12, 11)
my_date2 = date(1996, 12, 18)

time_diff = my_date2 - my_date1  # Returns the difference by days and seconds
ty2 = type(time_diff)
print(ty2)
print(time_diff)

# Example 3
my_time1 = time(13, 24, 56)
my_time2 = time(13, 30, 58)

# time_diff = my_time2 - my_time1  # unsupported for the class time


# Example 4 (What is the date after 90 days from now?)

"""
timedelta(self, /, *args, **kwargs) -> date object
Returns difference between two datetime values.
"""

td = timedelta(days=90)
now = datetime.now()

date_after_90_days = now + td
show_date_and_time(date_after_90_days)

# Example 5

"""
relativedelta('dt1=None', 'dt2=None', 'years=0', 'months=0', 'days=0',
'leapdays=0','weeks=0', 'hours=0', 'minutes=0', 'seconds=0', 'microseconds=0',
'year=None','month=None', 'day=None', 'weekday=None', 'yearday=None',
'nlyearday=None','hour=None', 'minute=None', 'second=None', 'microsecond=None')

The relativedelta type is designed to be applied on an existing datetime and
represent an interval of time.
"""

# Introduce relativedelta and compare between relativedelta and timedelta


