""" Lecture: Python Sets

    Outlines
    1- How to Create a Set
    2- Set Operators
    3- How to Update a Set
    4- Some Useful Set Functions
"""

# 1- How to Create a Set

# Example 1
pro_languages = {'C', 'C#', 'R', 'GO', 'Python'}
print('Most popular programming languages are : ', pro_languages)

#
data_types1 = {'Numbers', 'Strings', 'Lists', 'Sets', 'Dictionaries'}
data_types2 = {'Numbers', 'Strings', 'Dictionaries','Sets'}
data_types3 = {'Sets', 'Tuples'}

# 2- Set Operators


# Sets Union
# Function: union()
"""
union(*others: set) -> set
Returns a new set with elements from the set and all others.
It is equivalent to use the operator |
"""

# Example 1 two sets

res1 = data_types1.union(data_types2)
res2 = data_types1 | data_types2

print(res1)
print(res2)

# Example 2 three sets

res1= data_types1.union(data_types2, data_types3)
res2 = data_types1 | data_types2 | data_types3

print(res1)
print(res2)

# Sets Intersection

# Function : intersection(set)
"""
intersection(*others: set) -> set
Returns a new set with elements common to the set and all others.
It is equivalent to use the operator &
"""

# Example 1 two sets

res1 = data_types1.intersection(data_types2)
res2 = data_types1 & data_types2

print(res1)
print(res2)

# Example 2 three sets

res1 = data_types1.intersection(data_types2, data_types3)
res2 = data_types1 & data_types2 & data_types3

print(res1)
print(res2)


#  Sets Difference

# Function : difference(set)
"""
difference(*others: set) -> set
Returns a new set with elements in the set that are not in the others.
It is equivalent to use the operator -
"""

# Example 1 two sets

res1 = data_types1.difference(data_types2)
res2 = data_types1 - data_types2

print(res1)
print(res2)

# Example 2 three sets

res1 = data_types1.difference(data_types2, data_types3)
res2 = data_types1 - data_types2 - data_types3

print(res1)
print(res2)

"""
issubset(other: set) -> bool
Tests whether every element in the set is in the other.
It is equivalent to use the operator <=
"""
res1 = data_types2.issubset(data_types1)
res2 = data_types2 <= data_types1
print('data_types2.issubset(data_types1) is : ', res1)
print('data_types2 <= data_types1 is : ', res2)

"""
issuperset(other: set) -> bool
Tests whether every element in other is in the set.
It is equivalent to use the operator >=
"""

res1 = data_types1.issuperset(data_types2)
res2 = data_types1 >= data_types2

print('data_types2.issuperset(data_types1) is', res1)
print('data_types1 >= data_types2 is : ', res2)


# Membership operators

# in

res = 'Numbers' in data_types1
print(res)

# not in

res = 'float' not in data_types1
print(res)

#  3- How to Update a Set
# Add

"""
add(elem) 
Adds element elem to the set.
"""

print('data_types3 before is : ', data_types3)
data_types3.add('Lists')
print('data_types3 after add is : ', data_types3)

# Remove

"""
remove(elem)
Removes element elem from the set.
Raises KeyError if elem is not contained in the set.
"""

print('data_types3 before is : ', data_types3)
data_types3.remove('Sets')
print('data_types3 after remove is : ', data_types3)

# 4- Some Useful Set Functions

set1 = {3, 2, 12, 34, 7}

"""
len(object) -> int
Determines how many items a set has.

"""

res = len(set1)
print(res)

"""
min(iterable: numeric values) -> int or float
Returns the minimum number in the set.

"""

res = min(set1)
print(res)

"""
max(iterable: numeric values) -> int or float
Returns the maximum number in the set.

"""

res = max(set1)
print(res)

"""
sum(iterable: numeric values) -> int or float
Returns sum of the set elements.

"""

res = sum(set1)
print(res)
