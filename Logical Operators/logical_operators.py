""" Lecture: Logical Operators

    Outlines
    1- Logical AND Operator (and)
    2- Logical Or Operator (or)
    3- Logical Not Operator (not)
"""

a = True
b = False

# 1- Logical AND Operator (and)
c = a and b
print('a and b is : ', c)

# 2- Logical OR Operator (or)
c = a or b
print('a or b is : ', c)

# 3- Logical NOT Operator (not)

# Example 1
res1 = not a
print(res1)

# Example 2
res2 = not b
print(res2)

# Example 3
c = not (a and b)
print('not (a and b is) : ', c)
