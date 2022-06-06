""" datetime Module Challenges

    Challenges

"""

from datetime import time, date, datetime, timedelta
from dateutil import tz

"""
1- Can you find the current time?

"""
res = datetime.now()
print(res)



"""
2- How old are you by days?
"""

from datetime import date
birthday = datetime(1991, 10, 26)
current_date = datetime.now()
delta = current_date - birthday
res = delta.days
print(res, 'days')


"""
3- What is the date before 90 days from now?
"""

ini_time_for_now = datetime.now()

print("initial_date", str(ini_time_for_now))
future_date_after_90days = ini_time_for_now - timedelta(days=90)
res = str(future_date_after_90days)
print('the date before 90 days is :', res)

"""
4- A website allows people to use its services only if they are above 30 years,
how to check if you are eligible to use that website?

"""
birth_day = str(input('Enter your birthday : '))
date_format = "%d-%m-%Y"
my_date = datetime.strptime(birth_day, date_format)
year1 = my_date.year
current_date = datetime.now()
year2 = current_date.year
res1 = year2 - year1
print(res1)
if int(res1) > 30:
    print('welcome to our website')
else:
    print('sorry, you are not allowed to access our website')

"""
5- Write a Python program which takes the following string
date_time = 'Jun 12 2013 5:30PM', converts the string into a datetime object,
and then print the result.


"""
import datetime

date_time = 'Jun 12 2013 5:30PM'
format = '%b %d %Y %I:%M%p'  # The format
datetime_str = datetime.datetime.strptime(date_time, format)
print(datetime_str)


"""
6- Write a Python program in which you define the following date
2015-07-15 19:39:04 as a datetime object,
and then convert the object into a string object

"""

from datetime import datetime


date_time = datetime(2015, 7, 15, 19, 39, 4)
datetime_formated = date_time.strftime('%d/%m/%Y %H-%M-%S')

print(datetime_formated)

"""
7- Compute the difference between two datetimes objects,
using relativedelta function
date1 (2009, 2, 3)
date2 (2012, 4, 6)

"""

from dateutil.relativedelta import relativedelta
import datetime
date1 = datetime.datetime(2009, 2, 3)
date2 = datetime.datetime(2012, 4, 6)
res = relativedelta(date1, date2)
print(res)

