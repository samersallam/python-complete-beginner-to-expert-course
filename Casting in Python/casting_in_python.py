""" Lecture: Casting in Python

    Outlines
    1- General Examples
    2- Casting could lead to data loss
    3- Casting is not applicable between any two types of data
    4- Casting is sometimes conditionally accepted between two data types
"""


# 1- General Examples

a = 1
# Example 1

print(a)
res = type(a)
print(res)

# Example 2

float_a = float(a)
print('float(a) is : ', float_a)

# Example 3

print(a)
str_a = str(a)
print('str(a) is : ', str_a)

# 2- Casting could lead to data loss
a = 4.567  # float number with important info after the .
print(a)
int_a = int(a)
print('int(a) is : ', int_a)

# 3- Casting is not applicable between any two types of data
a = 25
# list_a = list(a) # will give us an error : 'int' object is not iterable
print(a)
# print('list(a) is : ', list_a)

# 4- Casting is sometimes conditionally accepted between two data types
str_a = 'Hi'
print(str_a)
# int_a = int(str_a)  # will give us an error: ValueError: invalid literal for int() with base 10: 'Hi'
# print(int_a)

# str->int it must be with base 10
str_a = '25'
print(str_a)
int_a = int(str_a)
print('int(a) is : ', int_a)
