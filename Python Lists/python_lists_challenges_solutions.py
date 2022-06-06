""" Python Lists Challenges

    Challenges

"""

"""
1- Write a Python program to multiply all the items in the list a = [1, 3, 4]

"""

a = [1, 3, 4]
m = 1
m = m * a[0]
m = m * a[1]
m = m * a[2]
print('multiple a items is', m)

"""

2- Write a Python program to create a new copy of the list1
which contains the two lists:
list_1 = [1, 3, 43, 23], list_2= [12, 12, 32, 14] 
using list concatenation and assign operator
"""
list_1 = [1, 3, 43, 23]
list_2 = [12, 12, 32, 14]

list_1 += list_2
print(list_1)

"""

3- Write a Python program to create a new list which contains the list
q= [' a', ' v', ' d'] repeated three times
using list repetition operator 

"""

q = [' a', ' v', ' d']
list_2 = q * 3
print(list_2)

"""
4- If you have the following list_1:
list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]
Write a Python program to:

a.	Delete the elements from first to fourth
b.	Find if list_1 contains 5
c.	Change the first element to 90
d.	Get the third element

"""
list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]

# a

del list_1[0: 4]
print(list_1)

# b

res = 5 in list_1
print(res)

# c

list_1[0] = 90
print(list_1)

# d
res = list_1[2]
print(res)