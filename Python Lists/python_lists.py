""" Lecture: Python Lists

    Outlines
    1- How to Create a List
    2- List Operators
    3- Accessing to List Contents
    4- List Slicing

"""

# 1- How to Create a List

pro_languages = ['C', 'C#', 'R', 'GO', 'Python']
print('Most popular programming languages are : ', pro_languages)

# 2- List Operators

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation (+)

concat = list1 + list2
print(concat)

# Concatenation and Assign (+=)

list2 += list1
print(list2)

# Repetition (*)

new_list = list1 * 4
print(new_list)

# Repetition and Assign (*=)

list1 *= 4
print(list1)

# Membership(in , not in)

# in

# Example 1

res = 3 in list1
print(res)

# Example 2

res = 5 in list1
print(res)

# not in

# Example 1

res = 9 not in list1
print(res)

# Example 2

res = 2 not in list1
print(res)

# Indexing

# 3- Accessing to List Contents

list1 = [1, 2, 3, 4, 7, 9, 20]

# Get an item

# Positive indexing

res = list1[3]
print(res)

# Negative Indexing

res = list1[-2]
print(res)

# Update an item

# Positive indexing

print('Before : ', list1)
list1[3] = 17
print('After : ', list1)

# Negative Indexing

print('Before : ', list1)
list1[-2] = 17
print('After : ', list1)

# Delete an item 

print('Before : ', list1)
del list1[2]
print('After : ', list1)


# 4- List Slicing

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Positive slicing

res = fruits[0:3]
print(res)

# Negative slicing

res = fruits[-3:-1]
print(res)

