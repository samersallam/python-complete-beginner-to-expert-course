""" random Module Challenges

    Challenges

"""
import math as m
import random

# 1- Write a Python program to generate a random integer number in the range [5-10]
res1 = random.randint(5, 10)
print(res1)

# 2- Write a Python program to generate a random float number in the range [5-10]
res2 = random.uniform(5, 10)
print(res2)

# 3- Write a Python program to initialize the random number generator by the seed 5
random.seed(5)
res3 = random.uniform(5, 10)
res4 = random.randint(5, 10)
print(res3)
print(res4)
