""" Lecture: Copy in Python

    Outlines
    1- Shallow Copy
    2- Deep Copy
    3- Identity Operator
 """
import copy
# 1- Shallow Copy
# list example

list1 = [1, 2, 4, 5]
list2 = list1
print('List1 before is : ', list1)
print('List2 before is : ', list2)
list2[1] = 100
print('List1 after is : ', list1)
print('List2 after is : ', list2)

# Dictionary example

car_dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
car_dict2 = car_dict1
print('car_dict1 before is : ', car_dict1)
print('car_dict2 before is : ', car_dict2)
car_dict1['year'] = 1970
print('car_dict1 after is : ', car_dict1)
print('car_dict2 after is : ', car_dict2)

# 2- Deep Copy
"""
copy.deepcopy(x: object) -> object :
Creates a deep copy of the x object
"""
# List example

list1 = [1, 2, 4, 5]
list2 = copy.deepcopy(list1)
print('List1 before is : ', list1)
print('List2 before is : ', list2)
list2[1]= 100
print('List1 after is : ', list1)
print('List2 after is : ', list2)

# Dictionary example

car_dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
car_dict2 =copy.deepcopy(car_dict1)
print('car_dict1 before is : ', car_dict1)
print('car_dict2 before is : ', car_dict2)
car_dict1['year'] = 1970
print('car_dict1 after is : ', car_dict1)
print('car_dict2 after is : ', car_dict2)

# 3- Identity Operator

# Sallow Copy
list1 = [1, 2, 4, 5]
list2 = list1
res1 = list2 is list1
res2 = list2 is not list1
print(res1)
print(res2)


# Deep Copy
list1 = [1, 2, 4, 5]
list2 = copy.deepcopy(list1)
res1 = list2 is list1
res2 = list2 is not list1
print(res1)
print(res2)