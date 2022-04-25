""" Lecture: random Module

    Outlines
    1- Some Useful random Module Functions
"""
import random

# 1- Some Useful random Module Functions

"""
randint(a:int, b:int) -> int 
Generates a random integer between a and b.
"""

r1 = random.randint(3, 60)
print(r1)

"""
random() -> float
Generates a random float number in the range (0 - 1).
"""

r2 = random.random()
print(r2)

"""
uniform(a:float, b:float) -> float
Generates a random float number in the range(a - b).
"""
r3 = random.uniform(1, 3)
print(r3)

"""
seed(a:int) -> None
Initializes the random number generator (to reproduce the same random numbers).
"""
random.seed(10)
r4 = random.random()
r5 = random.randint(1, 5)
print(r4)
print(r5)
