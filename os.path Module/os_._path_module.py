""" Lecture: os.path Module

    Outlines:
    1- Useful os.path Functions
"""

import os
# Start by creating a folder named (test) in the desktop

"""
os.path.basename(p: string) -> string
Returns the final component of a path name.
"""
path = r'C:\Users\Samer\Desktop\test\dummy.txt'
file_name = os.path.basename(path)
print(file_name)

"""
os.path.dirname(p: string) -> string
Returns the directory component of a path name.

"""
path = r'C:\Users\Samer\Desktop\test\dummy.txt'
file_dir = os.path.dirname(path)
print(file_dir)

"""
os.path.split(p:string) -> tuple
Returns a tuple that represents head and tail of the specified path name. 
"""
path = r'C:\Users\Samer\Desktop\test\dummy.txt'
file_dir, file_name = os.path.split(path)
print(file_dir)
print(file_name)

"""
os.path.splitext(p:string) -> tuple
Returns a tuple that represents root and ext part of the specified path name. 

"""
path = r'C:\Users\Samer\Desktop\test\dummy.txt'
file_dir_name, file_ext = os.path.splitext(path)
print(file_dir_name)
print(file_ext)

"""
os.path.isfile(path: string) -> bool
Returns True if specified path is an existing regular file,
otherwise returns False. 

"""
path = r'C:\Users\Samer\Desktop\test\dummy.txt'
is_file = os.path.isfile(path)
print(is_file)

"""
os.path.isdir(path:string) -> bool
Returns True if specified path is an existing directory,
otherwise returns False. 

"""
path = r'C:\Users\Samer\Desktop\test\dummy.txt'
# path = r'C:\Users\Samer\Desktop\test'
is_dir = os.path.isdir(path)
print(is_dir)

"""
os.path.join(path: string, *paths: strings) -> string
Returns a string which represents the concatenated path components. 

"""
file_dir = r'C:\Users\Samer\Desktop\test'
file_name = 'dummy.txt'
path = os.path.join(file_dir, file_name)
print(path)
