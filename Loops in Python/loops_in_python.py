""" Lecture: Loops in Python

    Outlines
    1- for Loop
    2- for-else loop
    3- while Loop
"""
import random

# 1- for Loop

# Looping through list

# Example 1

fruits = ["apple", "banana", "cherry"]
print('fruits_list =', fruits)
for x in fruits:
  print(x)

# Example 2

ages = [12, 23, 25, 42, 14]
for age in ages:
    if age >= 20:
        print(age, 'he can be employed')
    else:
        print(age, 'he can not be employed')

# Looping through tuple
items = (3, 5, 6)
print('items_tuple =', items)
for y in items:
    y+= 1
    print(y)

# Looping through string
b = "banana"
print('banana string')
for x in b:
  print(x)

# Looping through dictionary

# Example 1

modules = {'module1': 'python setup', 'module2': 'run first program', 'module3': 'python variables'}
for key in modules:
    print(modules[key])

# Example 2
students_marks = {'Student1': 5, 'Student2': 10, 'Student3': 15}
for student, mark in students_marks.items():
    print(student, ':', mark)
#

# Looping through set
test_set = {'a', 'b', 'c', 'd'}
for item in test_set:
    print(item)

# 2- for-else loop

# Example 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
else:
  print("Finally finished!")

# Example 2

for x in range(6):
  print(x)
else:
  print("we fetch the range!")

# 3- While Loop

# Example 1

i = 1
print('initial value of i =', i)
print('our condition is i < 6')
while i < 6:
  print(i)
  i += 1

# Example 2

i = 0
while i < 10:
    temp = random.randint(25, 100)
    if temp < 60:
        print(f'{temp} degree is in normal range')
    else:
        print(f'{temp} degree is out of normal range')

    i = i + 1


