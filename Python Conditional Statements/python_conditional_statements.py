""" Lecture: Python Conditional Statements

    Outlines
    1- if Statement
    2- if-else Statement
    3- if-elif …. else Statement
"""
import copy

# 1- if Statement

# Example 1
a = 15
b = 16
if a < b:
    print('a < b')

# Example 2
zoo_animals = {'lion', 'tiger', 'fish', 'duck'}
animals2 = {'lion', 'tiger'}
if animals2.issubset(zoo_animals):
    print('We can see lion and tiger in the zoo')

# Example 3
high_level_pro_lang = ['C++', 'Java', 'Python', 'HTML']
if 'Python' in high_level_pro_lang:
    print('Python is a high level programming language')

# 2- if-else Statement

# Example 1
girl = {'name': 'Huda', 'age': 29}
boy = {'name': 'Ali', 'age': 47}

if boy['age'] > girl['age']:
    print(boy['name'], 'is older than', girl['name'])
else:
    print(girl['name'], 'is older than', boy['name'])

# Example 2
a = 12
b = 17

if a > b:
    print('a > b is true')
    c = a - b
    print('the difference between a, b is', c)
else:
    print('a > b is false')
    c = b - a
    print('the difference between a, b is', c)

# Example 3
student_mark1 = {'name': 'Tasneem', 'mark': 90}
student_mark2 = {'name': 'Ashraf', 'mark': 85}
student_mark3 = {'name': 'Suzan', 'mark': 45}

successful_students = []
failed_students = []

if student_mark1['mark'] > 60:
    successful_students.append(student_mark1['name'])
else:
    failed_students.append(student_mark1['name'])

if student_mark2['mark'] > 60:
    successful_students.append(student_mark2['name'])
else:
    failed_students.append(student_mark2['name'])

if student_mark3['mark'] < 60:
    failed_students.append(student_mark3['name'])
else:
    successful_students.append(student_mark3['name'])

print('Successful students are : ', successful_students)
print('failed students are : ', failed_students)

if 'Suzan' in successful_students:
    print('Suzan pass the exam')
else:
    print('Suzan does not pass the exam')

# Example 4
car_dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
car_dict2 = copy.deepcopy(car_dict1)

if car_dict2 is car_dict1:
    print('car_dict2 is a shallow copy of car_dict1')
else:
    print('car_dict2 is a deep copy of car_dict1')

# 3- if-elif …. else Statement

# Example 1
a = 16
b = 23
q = [10, 2, 23, 15]

if a in q:
    print('a is available in q')
elif b in q:
    print('b is available in q')
else:
    print('a and b are not available')



# Example 2
a = 10
b = 10
if a > b:
    print('a is grater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')

