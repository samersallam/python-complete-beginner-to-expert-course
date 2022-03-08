""" Lecture: Python Number

    Outlines
    1- How to Create a Number
    2- Some Useful Number Functions
"""


# 1- How to Create a Number
boolean_number = True
print('Boolean number : ', boolean_number)
type_b = type(boolean_number)
print('Boolean number type : ', type_b)

int_number = 10
print('Integer number : ', int_number)
type_i = type(int_number)
print('Integer number type : ', type_i)

float_number = 6.2
print('Float number : ', float_number)
type_f = type(float_number)
print('Float number type : ', type_f)

complex_number = complex(int_number, float_number)
print('Complex number : ', complex_number)
type_c = type(complex_number)
print('Complex number type : ', type_c)

# 2- Some Useful Number Functions

"""
min(arg1: int or float, arg2: int or float, *args: collection of int or float) -> int or float
Returns the minimum of all the arguments.
"""
minimum = min(1, 2, 3, 4)
print(minimum)

minimum = min(1, 2, 3, 4, 0, 1.5, -4)
print(minimum)

"""
max(arg1: int or float, arg2: int or float, *args: collection of int or float) -> int or float
Returns the maximum of all the arguments.
"""

maximum = max(1, 2, 3, 4)
print(maximum)

maximum = max(1, 2, 3, 4, 0, 1.5, -4)
print(maximum)

"""
round(number: float, ndigits=None) -> int
Rounds a number to a given precision in decimal digits.
"""
r1 = round(10.7)
print(r1)
