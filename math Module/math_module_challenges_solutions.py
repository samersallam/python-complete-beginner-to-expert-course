""" math Module Challenges

    Challenges

"""
import math as m

"""
 1- Assume you have an angle = 60, write a Python program to find:
a.	sin(angle)
b.	cos(angle)
c.	tan(angle)
d.	degrees(angle)
e.	radians(angle)

"""
angle = 60
sin = m.sin(angle)
cos = m.cos(angle)
tan = m.tan(angle)
deg = m.degrees(angle)
rad = m.radians(angle)

print('sin angle is : ', sin)
print('cos angle is : ', cos)
print('tan angle is : ', tan)
print('degrees(angle) is : ', deg)
print('radians(angle) is : ', rad)

"""
2- Assume you have the calculation result y = 98.34521,
write a Python program to round this result:
a.	upwards to the nearest integer
b.	downwards to the nearest integer

"""
y = 98.34521
upwards = m.ceil(y)
downwards= m.floor(y)
print('round y upwards is : ', upwards)
print('round y downwards is : ', downwards)

"""
3- Assume you have x = 7, write a Python program to find:
a.	log(x) 
b.	e^x.
c.	x^3
d.	The absolute value of x
e.	The square root of x
"""
x = 7
log = m.log(x)
e = m.exp(x)
p = m.pow(x, 3)
absolute = m.fabs(x)
sq = m.sqrt(x)

print('log(x) is : ', log)
print('e^x is : ', e)
print(' x ^ 3 is : ', p)
print('absolute value of x is : ', absolute)
print('square root of x is : ', sq)
