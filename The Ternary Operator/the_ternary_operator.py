""" Lecture: The Ternary Operator

    Outlines
    1- Ternary Operator Syntax
"""

#  1- Ternary Operator Syntax
# Example 1
a, b = 10, 20
minimum = a if a < b else b
print(minimum)

# Example 2
brands = ['KIA', 'HUNDAY', 'Marcedes']
your_car = 'KIA'
res = 'your car is popular' if your_car in brands else 'your car is not popular'
print(res)

# Example 3
list1 = [1, 2, 4, 5]
list2 = list1
res = 'list2 is shallow copy of list1' if list2 is list1 else 'list2 is deep copy of list1'
print(res)
