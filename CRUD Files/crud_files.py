""" Lecture: CRUD Files

    Outlines:
    1- How to Create a File
    2- How to Read From a File
    3- How to Append Data to a File
    4- How to Delete a File
"""
# 1- How to Create a File

"""
open(file: string, mode: string = 'r') -> file object
Opens file and returns a stream.
Raises OSError upon failure.

"""

"""
write(text: string) -> integer
Writes string to stream and returns the number of characters written
(which is always equal to the length of the string).
"""

"""
close(): Flushes and closes the IO object.
"""

file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
fo = open(file_path, "w")
fo.write("You Are Welcome to My Courses\nIn This Course You Will Learn a Lot\nPython is a great programming language\n")
fo.close()

# 2- How to Read From a File

"""
read(size:int =-1) -> string
Reads at most n characters from stream.
"""

file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
fo = open(file_path, "r")
file_content = fo.read()
print('The file has : \n', file_content)
fo.close()

# 'rb' to read binary file (not a text file)
file_path = r'C:\Users\Samer\Desktop\test\dummyimage.png'
fo = open(file_path, "rb")
file_content = fo.read()
res = type(file_content)
print(res)
res1 = file_content[:20]
print(res1)
fo.close()

# Read a file line by line

"""
readlines(size:int =-1) -> list
Reads all the file lines and returns them as a list of strings.
"""

file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
fo = open(file_path, "r")

for c, line in enumerate(fo.readlines()):
    res3 = 'Line number {} : '.format(c)
    print(res3, line)

# Check if a file is readable or not

"""
readable() -> bool
Returns whether the file stream can be read or not.
"""

file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
fo = open(file_path, "r")
readable = fo.readable()
print('File is readable : ', readable)
fo.close()

# 3- How to Append Data to a File
file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
fo = open(file_path, "a")  # USE "a" not "w"
fo.write("\nMainly, you will learn about Python Programming Language")
fo.close()

fo = open(file_path, "r")
file_content = fo.read()
print('The file after appending has : \n', file_content)
fo.close()

# 4- How to Delete a File
import os

"""
remove(path: string)
Removes a file.
"""

file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
# os.remove(file_path)

# To rename a file

"""
os.rename(src: string, dst: string)
Renames a file.
"""

file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
new_file_path = r'C:\Users\Samer\Desktop\test\new_dummy.txt'
os.rename(file_path, new_file_path)
