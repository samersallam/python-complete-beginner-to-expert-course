""" Lecture: pickle Module

    Outlines:
    1- Serialization (pickling)
    2- Deserialization (unpickling)

"""
import pickle as pk

# File
# 1- Serialization (pickling)
"""
pickle.dump(obj, file)
Writes a pickled representation of obj to the open file object

"""
lst1 = [1, 2, 3, 4]
lst2 = [4, 3, 2, 1]
new_list = list()
for a, b in zip(lst1, lst2):
    new_list.append(a + b)

file_path = r'C:\Users\Samer\Desktop\test\dummy_pickle.pkl'
with open(file_path, 'wb') as f:
    res = 'Dumping {} to the pickle file'.format(new_list)
    print(res)
    pk.dump(new_list, f)

# 2- Deserialization (unpickling)

"""
pickle.load(file) -> object
Reads and returns an object from the pickle data stored in a file.

"""
file_path = r'C:\Users\Samer\Desktop\test\dummy_pickle.pkl'
with open(file_path, 'rb') as f:
    lst = pk.load(f)
    print('The pickle file has : ', lst)

# Network
# 1- Serialization (pickling)

"""
pickle.dumps(obj) -> string
Returns the pickled representation of the object as a bytes object.

"""
lst1 = [1, 2, 3, 4]
lst2 = [4, 3, 2, 1]
new_list = list()
for a, b in zip(lst1, lst2):
    new_list.append(a + b)

pickled_list = pk.dumps(new_list)
print('The pickled list is : ', pickled_list)

# 2- Deserialization (unpickling)

"""
pickle.loads(data) -> object
Reads and returns an object from the given pickle data.
"""
lst1 = [1, 2, 3, 4]
lst2 = [4, 3, 2, 1]
new_list = list()
for a, b in zip(lst1, lst2):
    new_list.append(a + b)

pickled_list = pk.dumps(new_list)
print('The pickled list is : ', pickled_list)

original_list = pk.loads(pickled_list)
print('The original list is : ', original_list)
