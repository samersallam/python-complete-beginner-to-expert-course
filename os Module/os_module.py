""" Lecture: os Module

    Outlines:
    1- Useful os Functions
"""
import os
# Start by creating a folder named (test) in the desktop

# 1- Useful OS Functions

"""
os.getcwd() -> unicode string
Returns a unicode string representing the current working directory.
"""
cwd1 = os.getcwd()
print(cwd1)

"""
os.chdir(path: string)
Changes the current working directory to the specified path.
"""
cwd = r'C:\Users\Samer\Desktop\test'
os.chdir(cwd)

"""
os.mkdir(path: string)
Creates a directory.
"""
folder_path = r'folder1'
# os.mkdir(folder_path)

"""
os.makedirs(name: string)
Super-mkdir; creates a leaf directory and all intermediate ones.
"""
# folder_path = r'C:\Users\Samer\Desktop\test\folder1\folder2\folder3\folder4'
folder_path = r'folder1\folder2\folder3\folder4'
# os.mkdir(folder_path)
# os.makedirs(folder_path)

"""
os.rmdir(path: string)
Removes a directory.
"""
folder_path = 'folder1'
# os.rmdir(folder_path)  # Error because it is not empty

"""
os.removedirs(name: string)
Removes directories.
"""

folder_path = r'folder1\folder2\folder3\folder4'
# os.removedirs(folder_path)


"""
os.rename(src: string, dst: string)
Renames a file or directory.
"""
# os.rename('folder1', 'folder2222')

"""
os.listdir(path: string)-> list
Returns a list containing the names of the files in the directory.
"""
res = os.listdir()
print(res)

# Or
folder_path = r'C:\Users\Samer\Desktop\test'
res = os.listdir(folder_path)
print(res)
