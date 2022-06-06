""" os.path Module Challenges

    Challenges

"""
"""
1- Manually: Create a folder with the name test,
and create a txt file inside it with the name 'python'
Write a python program to:
a.	Get your file name
b.	Get your file directory(folder)
c.	Get your file name and file directory
d.	Get your file extension
e.	Check if a file (‘course.txt’) is available inside your folder
f.	Check if a directory (folder1) is available inside your folder
g.	Create a path from your directory name and a file name

"""

import os

# 1
path = r'C:\Users\yourname\Desktop\test\python.txt'
file_name = os.path.basename(path)
print(file_name)

# 2
path = r'C:\Users\yourname\Desktop\test\python.txt'
file_dir = os.path.dirname(path)
print(file_dir)

# 3
path = r'C:\Users\yourname\Desktop\test\python.txt'
file_dir, file_name = os.path.split(path)
print(file_dir)
print(file_name)

# 4
path = r'C:\Users\yourname\Desktop\test\python.txt'
file_dir_name, file_ext = os.path.splitext(path)
print(file_dir_name)
print(file_ext)

# 5
path = r'C:\Users\yourname\Desktop\test\course.txt'
is_file = os.path.isfile(path)
print(is_file)

# 6
path = r'C:\Users\yourname\Desktop\test\folder1'
is_dir = os.path.isdir(path)
print(is_dir)

# 7
file_dir = r'C:\Users\yourname\Desktop\test'
file_name = 'python.txt'
path = os.path.join(file_dir, file_name)
print(path)
