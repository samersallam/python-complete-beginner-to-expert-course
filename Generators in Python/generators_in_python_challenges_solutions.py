""" Generators in Python Challenges

    Challenges

"""

"""
1- Write a Python program that creates a generator which returns the following list
items l1 = [12, 34, 76, 89] divided by 100,
and then extract the generator values using:
a.	next function
b.	for loop

"""
l1 = [12, 34, 76, 89]

print('Extract generator values using next function')
gen = (x / 100 for x in l1)
f = next(gen)
s = next(gen)
th = next(gen)
fth = next(gen)
print(f)
print(s)
print(th)
print(fth)

print('Extract generators values using for loop')
gen = (x / 100 for x in l1)
for item in gen:
    print(item)

"""
2- Write a Python program that creates a generator which returns even elements
from the given tuple tu1 = (17, 40, 36, 7, 5, -20),
and then extract the generator values using for loop

"""
tu1 = (17, 40, 36, 7, 5, -20)
gen1 = (x for x in tu1 if x % 2 == 0)
print('Extract generators values using for loop')
for item in gen1:
    print(item)

"""
3- Write a Python program that creates a generator which returns even elements
from the given tuple tu1 = (17, 40, 36, 7, 5, -20) and 0 otherwise,
and then extract generator values using next function

"""
tu1 = (17, 40, 36, 7, 5, -20)
gen2 = (x if x % 2 == 0 else 0 for x in tu1 )
print('Extract generator values using next function')
f = next(gen2)
s = next(gen2)
th = next(gen2)
fth = next(gen2)
fith = next(gen2)
sth = next(gen2)
print(f)
print(s)
print(th)
print(fth)
print(fith)
print(sth)

"""
4- Write a Python program that defines a generator function which generates
multiples of 5 until the given numbers ‘num’. Use your generator for num=25
"""


def multiple_five(num):
    for i in range(num):
        if i % 5 == 0:
            yield i


for i in multiple_five(25):
    print(i)