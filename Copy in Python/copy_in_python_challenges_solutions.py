""" Copy in Python Challenges

   Challenges

"""
import copy

"""
1- Assume you have list_1, write a Python program to:
a.	Find list_2 where list_2 = list_1 using deep copy
b.	Change the third element of lis_1 to 3
c.	Reprint list_2
d.	Is list_2 the same to list_1

"""
# a

list_1 = [2, 6, 9, 21]
list_2 = copy.deepcopy(list_1)
print('list_2 = ', list_2)

# b
list_1[2] = 3
print('list_1 = ', list_1)

# c
print('list_2 = ', list_2)

# d
res = list_2 is list_1
print(res)

"""
Assume you have dic_1, write a Python program to:
a.	Find dic_2 where dic_2 = dic_1 using shallow copy.
b.	Change the value of level key to 'Advance' in dic_1
c.	Reprint dic_2
d.	Is dic_2 the same to dic_1

"""
dic_1 = {'course': 'Python', 'level': 'beginner'}

# a
dic_2 = dic_1
print('dic_2 = ', dic_2)

# b
dic_1['level'] = 'Advance'
print('dic_1 = ', dic_1)

# c
print('dic_2 = ', dic_2)

# d
res = dic_2 is dic_1
print(res)