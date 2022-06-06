""" Lecture: Python Tuples

    Outlines
    1- How to Create a Tuple
    2- Tuple Operators
    3- Accessing to Tuple Contents
    4- Tuple Slicing
    5- Some Useful Tuple Functions
"""

# 1- How to Create a Tuple

fruit = ("apple", "banana", "cherry")
print('Fruit tuple is : ', fruit)

#
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 2- Tuple Operators

# Concatenation (+)

new_tuple = tuple1 + tuple2
print('New tuple is : ', new_tuple)

# Concatenation and Assign (+=)

tuple1 += tuple2
print('New tuple is : ', tuple1)

# Repetition (*)

new_tuple = tuple1*5
print('New tuple is : ', new_tuple)

# Repetition and Assign (*=)

tuple1 *= 5
print('New tuple is : ', tuple1)

# Membership (in, not in)

# in

# Example 1

res = 1 in tuple1
print(res)

# Example 2

res = 100 in tuple1
print(res)

# not in

# Example 1

res = 5 not in tuple1
print(res)

# Example 2

res = 11 not in tuple1
print(res)

# 3- Accessing to Tuple Contents

# get
# Positive indexing

res = tuple1[0]
print('The first item is : ', res)

# Negative indexing

res = tuple1[-1]
print('The last item is : ', res)

# update and delete an item are not applicable

# 4- Tuple Slicing

# Positive slicing

new_tuple = tuple1[0:2]
print('New tuple is : ', new_tuple)

# Negative slicing

new_tuple = tuple1[-3:-1]
print('New tuple is : ', new_tuple)


# 5- Some of Useful Tuple Functions

"""
len(object) -> int
Determines how many items a tuple has

"""

res = len(tuple1)
print('The tuple length is', res)

"""
max(iterable: numeric values) -> int or float
Returns the maximum number in the tuple

"""

res = max(tuple1)
print('The maximum number in tuple a is', res)

"""
min(iterable: numeric values) -> int or float
Returns the minimum number in the tuple

"""

res = min(tuple1)
print('the minimum number in tuple a is', res)

"""
sum(iterable: numeric values) -> int or float
Returns sum of the tuple elements

"""

res = sum(tuple1)
print('Sum a tuple is : ', res)
