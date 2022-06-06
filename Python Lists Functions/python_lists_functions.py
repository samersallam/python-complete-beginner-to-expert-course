""" Lecture: Python Lists Functions

    Outlines
    1- Some Useful List Functions
"""

# 1- Some Useful List Functions

list1 = [4, 20, 6, -1, 4,  7, 4, -2, 1, 20]
list2 = ['s', 't', 'q', 'd', 'f', 'a']
list3 = [3, 11, 54, 9, 43, 12]

"""
len(obj) -> int
Determines how many items a list has

"""

res = len(list1)
print(res)

"""
max(iterable: numeric values) -> int or float
Returns the maximum number in the list

"""


res = max(list1)
print(res)

"""
min(iterable: numeric values) -> int or float
Returns the minimum number in the list

"""

res = min(list1)
print(res)

"""
sum(iterable: numeric values) -> int or float
Returns sum of the list elements

"""

res = sum(list1)
print(res)

"""
append(object: could be any one of python supported data types)
Adds an element at the end of the list

"""


print('Before : ', list1)
list1.append(40)
print('After : ', list1)

"""
extend(iterable)
Adds the elements of a list (or any iterable), to the end of the current list

"""

print('Before : ', list1)
list1.extend(list2)
print('After : ', list1)

"""
remove(value: could be any one of python supported data types)
Removes the first item with the specified value

"""

# Example 1

list1.remove(1)
print(list1)

# Example 2

list2.remove('a')
print(list2)



"""
insert(index: int, object : could be any one of python supported data types)
Adds an element at the specified position

"""

print('Before : ', list1)
list1.insert(4, 'q')
print('After : ', list1)
print(list1)

"""
reverse()
Reverses the order of the list elements

"""


print('Before : ', list1)
list1.reverse()
print('After : ', list1)

"""
index(value: could be any one of python supported data types, start: int = 0, stop: int = last index)
Returns the index of the first element with the specified value

"""

# Example 1

s_index = list3.index(9)
print('9 number index is : ', s_index)

# Example 2

a_index = list3.index(54, 1, 4)
print('54 number index is : ', a_index)

"""
count(value:could be any one of python supported data types) -> int
Returns the number of elements with the specified value

"""

num_count = list1.count(20)
print(' 20 count is : ', num_count)

"""
pop(index: int = -1)
Removes the element at the specified position
by default it removes the last value
"""

# Example 1

print('Before : ', list1)
list1.pop()
print('After : ', list1)

# Example 2

print('Before : ', list1)
list1.pop(2)
print('After : ', list1)

"""
clear()
Removes all the elements from the list

"""

print('Before : ', list1)
list1.clear()
print('After : ', list1)

