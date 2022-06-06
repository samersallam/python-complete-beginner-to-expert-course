""" Lecture: Python Dictionaries

    Outlines
    1- How to Create a Dictionary
    2- Dictionary Operators
    3- Accessing to Dictionary Contents
    4- Dictionary Slicing
    5- Some Useful Dictionary Functions
"""

# 1- How to Create a Dictionary
# d1 = dict(a=1, b=2)

dict1 = dict(a=1, b=2)
print(dict1)

# d2 = {'a': 1, 'b': -1}

python_dict = {
    "name": "Python",
    "version": 3.7,
    "description": "High Level Programming Language",
    "level": "beginner"
}

print(python_dict)


# 2- Dictionary Operators (membership)

# in

res = 'version' in python_dict
print(res)

# not in

res = 'version' not in python_dict
print(res)

# 3- Accessing to Dictionary Contents

# Get
# You can access the items of a dictionary by referring to its key name, inside square brackets []

# Example 1

print(python_dict)
print(python_dict['name'])
print(python_dict['description'])



# Update
# You can update the value of a specific item by referring to its key name


# Example 1

print('Before update is : ', python_dict)
python_dict['version'] = 3.8
print('After update is : ', python_dict)

# Delete
"""
del dict['key name']
keyword removes the item with the specified key name
"""

print('Before delete is : ', python_dict)
del python_dict['version']
print('After delete version key is : ', python_dict)

# 4- Dictionary Slicing , No slicing for dictionary


# 5- Some of Useful Dictionary Functions

"""
len (object) -> int
Determines how many items a dictionary has

"""

print(len(python_dict))

"""
dict.values() -> object 
Returns an object containing a list of the values in the dictionary

"""

values1 = python_dict.values()
print(values1)

"""
dict.keys() -> object
Returns an object containing a list of the dictionary's keys

"""

values1 = python_dict.keys()
print(values1)

"""
dict.items() -> object
Returns an object containing a list of tuples for each key value pair

"""

values1 = python_dict.items()
print(values1)

"""
dict.get(key, default = None) -> value
Returns the value of the specified key

"""

# Example 1

res = python_dict.get('level')
print(res)

# Example 2

res = python_dict.get('duration')
print(res)

# Example 3

res = python_dict.get('duration', 'Not found!')
print(res)


"""
dict.pop(key) -> value 
Removes specified key and returns the corresponding value.
"""

# Example 1

res = python_dict.pop('level')
print(res)# Example 2
res = python_dict.pop('lastname', 'Not found!')
print(res)

print(python_dict)



"""
dict.clear()
Removes all the elements from the dictionary

"""

python_dict.clear()
print('python_dict After clear is : ', python_dict)








