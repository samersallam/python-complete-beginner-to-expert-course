""" Exceptions Handling in Python Challenges

    Challenges

"""

"""
1- Write a Python program that creates a new list containing the square root
of the following list items l1 = [36, -25, -49].
Make sure to catches error if  any exists

"""
import math as m
l1 = [36, -25, -49]

try:
    a = [m.sqrt(x) for x in l1]
    print(a)
except Exception:
    print("no sqrt for negative numbers")

else:
    print('every thing is ok')


"""
2- Assume we have the following generator:
 lst = [1, 2, 3,4,5], gen = (x*x for x in lst)
Print the generators items using 'while' loop and 'next()' function
without letting the code throw an exception

"""
lst = [1, 2, 3, 4, 5]
gen = (x*x for x in lst)
try:
    i = 0
    while(i < len(lst)):
        print(next(gen))
        i += 1

except StopIteration:
    print('no more items')

"""
3- Write a Python program that tries to print values of some dictionary keys
which are not available and catch that error.
Where our dictionary is:
student_dict = {"name": "Huda", "age": 24, " course": "Python Beginner to Advanced"}
Try to print student_dict['year']


"""
student_dict = {"name": "Huda", "age": 24, " course": "Python Beginner to Advanced"}

try:

    print(student_dict['name'])
    print(student_dict['age'])
    print(student_dict['year'])

except IndexError as e:
    print('Sending the error to the system logger')
    print(f'The following exception ({e}) has been raised')
else:
    print("Everything went ok")