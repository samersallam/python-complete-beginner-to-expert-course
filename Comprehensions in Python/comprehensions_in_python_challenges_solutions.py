""" Comprehensions in Python Challenges

    Challenges

"""

"""
1- Write a Python program to convert the list of strings
colors = ['Red', 'Blue', 'Green', 'Black', 'White'] to a list of upper case strings

"""
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = [cols.upper() for cols in colors]
print('colors =', colors)
print('upper_colors', upper_cols)

"""
2- Write a Python program to create a list of numbers
that are divisible by 6 in the range (0,100)
"""
num_list = [y for y in range(100) if y % 6 == 0]
print(num_list)

"""
3- Write a Python program to create a new list which contains square root
of the given list items [16, -4, 49, 0, -9, 25, -36] in case it is possible,
and 0 otherwise

"""
import math as m
list_1 = [16, -4, 49, 0, -9, 25, -36]
new_list = [m.sqrt(x) if x >0 else 0 for x in list_1]
print(new_list)

"""
4- Write a Python program to create a set containing only integers from the given list
[19, 23, 45, 'a', 'b', 5, 'r']

"""

list_2 = [19, 23, 45, 'a', 'b', 5, 'r']
set_1 = {x if type(x) == int else 0 for x in list_2}
print(set_1)

""" 
5- Write a Python program to create a dictionary from the given tuple
fruit = ("apple", "banana", "cherry")
where the key is the tuple element index, and the value is the element itself

"""

fruit = ("apple", "banana", "cherry")
new_dic = {fruit.index(x): x for x in fruit}
print(new_dic)