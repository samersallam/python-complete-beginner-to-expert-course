""" Python Tuples Challenges

   Challenges

"""

"""
1- Write a Python program to create and print the following
tuple (' a', ' v', ' d').
"""

tuple_x = (' a', ' v', ' d')
print(tuple_x)

"""
2- Write a Python program to get the 4th element from the beginning
and 4th element from the end of the following tuple : 
tuple_y = ('h','e','l','l','o','p','y','t','h','o','n')
"""

tuple_y = ('h','e','l','l','o','p','y','t','h','o','n')
print(tuple_y)
item = tuple_y[3]
print(item)
item1 = tuple_y[-4]
print(item1)

"""
3- Write a Python program to find the length of the following tuple.
tuple_x = (5, 10, 7, 4, 15, 3)

"""

tuple_x = (5, 10, 7, 4, 15, 3)
res = len(tuple_x)
print(res)

"""
4- Write a Python program to define a new tuple from the tuple tu
after repeating its elements three times: 
tu = (' a', ' v', ' d'),  using tuple  repetition operator
"""

tu = (' a', ' v', ' d')
res = tu * 3
print(res)

"""
5- Assume you have the tuples tu, tu1
tu = (12, 30, 43, 22, -9, 4, 21, 44, 3)
tu1 = (' a', ' v', ' d')
write a Python program to:
a.	Check whether an element 'a' exists within a tuple tu.
b.	Find the maximum and minimum number in tu
c.  Create a new copy of tu which contains tu, tu1
    using tuple concatenation and assign operator
d.	Create a new tuple from tu, where it contains the three elements of tu before
    the last one
"""
tu = (12, 30, 43, 22, -9, 4, 21, 44, 3)
tu1 = (' a', ' v', ' d')

# a
res = 'a' in tu
print(res)

# b
res_max = max(tu)
res_min = min(tu)
print(res_max)
print(res_min)

# c
tu += tu1
print(tu)

# d
res = tu[-4: -1]
print(res)



