""" os Module Challenges

    Challenges

"""

"""
1- Write a Python program to:
a.	Create a folder with the name: my_name
b.	Print your current directory
c.	Change your current working directory to the folder you just created
d.	Create other directories inside your folder: fplder1, folder2, folder3, folder4
e.	Create a directory with the name 'images'
f.	Rename the folder ‘images’ folder to 'photos'
g.	Get a list of available folders in your directory
h.	Remove the folder 'photos'

"""
import os
# a
folder_path = r'C:\Users\yourname\Desktop\my_name'
os.mkdir(folder_path)

# b
cwd1 = os.getcwd()
print(cwd1)

# c
cwd = r'C:\Users\yourname\Desktop\my_name'
#os.chdir(cwd)
cwd1 = os.getcwd()
print(cwd1)

# d
folder_path = r'C:\Users\yourname\Desktop\my_name\folder1\folder2\folder3\folder4'
#os.makedirs(folder_path)

# e
folder_path = r'C:\Users\yourname\Desktop\my_name\images'
#os.mkdir(folder_path)

# f
#os.rename('images', 'photos')

# g
#res = os.listdir()
#print(res)

# h
#os.rmdir('photos')