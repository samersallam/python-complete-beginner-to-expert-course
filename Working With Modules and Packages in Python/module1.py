""" Lecture: Working With Modules and Packages in Python

    Outlines:
    1- How to Import a Module


"""
# 1- How to Import a Module

# built-in module
import math

math.sin(5)

from math import *

sin(5)
cos(10)

from math import sin, cos

sin(5)
cos(10)
tan(10)

import math as m

m.sin(5)

from math import sin as math_sin

math_sin(5)

# your module
from module2 import clac_area
res1 = clac_area(5, 6)

print(res1)

import module2
res2 = clac_area(5, 6)
print(res2)
