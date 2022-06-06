""" Lecture: Comprehensions in Python

    Outlines
    1- List Comprehension
    2- Set Comprehension
    3- Dictionary Comprehension
"""

# 1- List Comprehension
numbers = [1, 2, 3, 4, 5, 6]

# Example 1 [ <expression> for <element> in <iterable> ]


# I want 'n**2' for each 'n' in the list 'numbers'

# Traditional way
new_list = []
for n in numbers:
    new_list.append(n ** 2)

print('Traditional way : ', new_list)


# List comprehension
new_list = [n ** 2 for n in numbers]
print('List comprehension : ', new_list)

# Example 2 [ <expression> for <element> in <iterable>  if  <condition> ]

# I want 'n**2' for each 'n' in the list 'numbers' if 'n>2'
# Traditional way
new_list = []
for n in numbers:
    if n > 2:
        new_list.append(n ** 2)

print('Traditional way : ', new_list)

# List comprehension
new_list = [n ** 2 for n in numbers if n > 2]
print('List comprehension : ', new_list)

# Example 3 [ <expression> if <condition> else < expression> for <element> in <iterable> ]


# I want 'n**2' if 'n>2' else I want 'n/2' for each 'n' in the list 'numbers'
# Traditional way
new_list = []
for n in numbers:
    if n > 2:
        new_list.append(n ** 2)
    else:
        new_list.append(n / 2)

print('Traditional way : ', new_list)

# List comprehension
new_list = [n ** 2 if n > 2 else n / 2 for n in numbers]
print('List comprehension : ', new_list)

# Example 4
uppered_strs = [st.upper() for st in strs]
print(uppered_strs)

# 2- Set Comprehension
lst = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7]

# Example 1

# I want the unique 'n' for each 'n' in lst
st = {n for n in lst}
print(st)

# Example 2

# I want the unique 'n' for each n in lst if 'n > 3'
st = {n for n in lst if n > 3}
print(st)

# # 3- Dictionary Comprehension
# Example1
numbers = [1, 2, 3, 4, 5]

# I want a dictionary in which the VALUE is 'n ** 2' and the KEY is 'n' for each 'n' in numbers
numbers_dict = {n: n ** 2 for n in numbers}
print(numbers_dict)

# Example 2
strs = ['hi', 'hello', 'welcome']

# I want a dictionary in which the KEY is 'st index' and the VALUE is 'st' for each 'st' in strs
strs_dict = {strs.index(val): val for val in strs}
print(strs_dict)
