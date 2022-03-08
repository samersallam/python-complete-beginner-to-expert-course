""" Python Number Challenges

    Challenges

"""

"""
1- Write a Python program to define the following numbers
and print the type of each one:
5.8, false, 4, 3 +j 10

"""
a = 5.8
resa = type(a)
b = False
resb = type(b)
c = 4
resc = type(c)
d = complex (3, 10)
resd = type(d)

print(a, ' is ', resa)
print(b, ' is ', resb)
print(c, ' is ', resc)
print(d, ' is ', resd)

"""
2- Write a Python program to find
the maximum and minimum number of the following numbers (11, 23, -9, -11, -25)
"""
maximum = max(11, 23, -9, -11, -25)
minimum = min (11, 23, -9, -11, -25)
print('Maximum number is ', maximum)
print('Minimum number is ', minimum)

"""
3- Write a Python program to find the rounded value of 9.3
"""
a = 9.3
r = round(9.3)
print(r)