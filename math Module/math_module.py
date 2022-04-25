""" Lecture: math Module

    Outlines
    1- General Functions
    2- Rounding Functions
    3- Trigonometric Functions
    4- Mathematical Constants
    
"""
import math

# 1- General Functions

x = 4
"""
exp(x: int or float) -> float
Returns the value of E^x, where e is Euler's number,
and x is the number passed to it.
"""

exp_x = math.exp(x)
print('exp(x) is : ', exp_x)

"""
fabs(x: float) -> float
Returns the absolute value of the float x.

"""

fabs_x = math.fabs(x)
print('fabs(x) is : ', fabs_x)

"""
sqrt(x: int or float) -> int or float
Returns the square root of x.

"""

sqrt_x = math.sqrt(x)
print('sqrt(x) is : ', sqrt_x)

"""
pow(x: int or float, y: int) -> int or float
Returns the value of x to the power of y.

"""
pow_x = math.pow(x, 3)
print('pow(x,3) is : ', pow_x)

"""
log(x: int or float, base: int or float=math.e) -> int or float
Returns the logarithm of x to the given base.

"""

# Example 1
log_x = math.log(x)
print('log(x) is : ', log_x)

# Example 2
log_x = math.log(x, 5)
print('log(x, 5) is : ', log_x)

# 2- Rounding Functions
x = 3.5893

"""

ceil(x:float) -> int
Rounds a number upwards to the nearest integer, and returns the result.

"""

ceil_x = math.ceil(x)
print('ceil(x) is : ', ceil_x)

"""
floor(x:float) -> int
Rounds a number downwards to the nearest integer, and returns the result.

"""

floor_x = math.floor(x)
print('floor(x) is : ', floor_x)

# 3- Trigonometric Functions

x = 3.14

"""
sin(x:int or float) -> int or float
Returns the sine of x.

"""
sin_x = math.sin(x)
print('sin(x) is : ', sin_x)

"""
cos(x:int or float)-> int or float
Returns the cosine of x.

"""
cos_x = math.cos(x)
print('cos(x) is : ', cos_x)

"""
tan(x:float or int) -> int or float
Returns the tangent of x.

"""
tan_x = math.tan(x)
print('tan(x) is : ', tan_x)

"""
degrees(x: float or int) -> int or float
Converts the value of x from radians to degrees.

"""

degrees_x = math.degrees(x)
print('degrees(x) is : ', degrees_x)

"""
radians(x: float or int) -> int or float
Converts the value of x from degrees to radians.

"""

x = 180
radians_x = math.radians(x)
print('radians(x) is : ', radians_x)

# 4- Mathematical Constants
pi = math.pi  # returns PI (3.1415...)
print('Mathematical pi : ', pi)

e = math.e   # returns Euler's number (2.7182...)
print('Euler Number "e" : ', e)
