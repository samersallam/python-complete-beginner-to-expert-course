""" pickle Module Challenges

   Challenges

"""

import pickle as pk
import os

"""
1- Write a Python program to create a pickle file on your pc
and write the sentence 'Hello Python' in this file, then read the content
"""
sentence = 'Hello Python'
file_path = r'C:\Users\yourname\Desktop\full_name.pkl'
with open(file_path, 'wb') as f:
    pk.dump(sentence, f)
# read
with open(file_path, 'rb') as f:
    res = pk.load(f)

print(res)

"""
2- Write a Python program to create student_dict = {'name': 'Sarah', 'course': 'Python'}, and
then print the content in two cases:
a.	After converting the object into pickle data
b.	Original object after we convert back the pickle data into its original form

"""
student_dict = {'name': 'Sarah', 'course': 'Python'}
pickled_dict = pk.dumps(student_dict)
print(pickled_dict)

orginal_dict = pk.loads(pickled_dict)
print(orginal_dict)




