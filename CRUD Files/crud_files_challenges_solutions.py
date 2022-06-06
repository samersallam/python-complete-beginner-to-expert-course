""" CRUD Files Challenges

    Challenges

"""

"""
1- Write a Python program to:
a.	Create a txt file with the name 'info ' on your Desktop
b.	Write the following sentences inside your file:
              I live in KL
             KL is a great city  
             You have to visit KL at least one time in your life
c.	Check if your file is readable
d.	Read the content of your file
e.	Read your file line by line
f.	Append some personal info to your file, for example: "I work as a Data Scientist"
    and read the new content
g.	Rename your file to 'personal_info ', and get your new file name

"""


import os
# a + b
file_path = r'C:\Users\yourname\Desktop\info.txt'
fo = open(file_path, "w")
fo.write("I live in KL\nKL is a great city\nYou have to visit KL at least one time in your life\n")
fo.close()

# c
file_path = r'C:\Users\yourname\Desktop\info.txt'
fo = open(file_path, "r")
readable = fo.readable()
print('File is readable : ', readable)
fo.close()

# d
file_path = r'C:\Users\yourname\Desktop\info.txt'
fo = open(file_path, "r")
file_content = fo.read()
print('The file has : \n', file_content)
fo.close()

# e
file_path = r'C:\Users\yourname\Desktop\info.txt'
fo = open(file_path, "r")

for c, line in enumerate(fo.readlines()):
    res3 = 'Line number {} : '.format(c)
    print(res3, line)

# f
file_path = r'C:\Users\yourname\Desktop\info.txt'
fo = open(file_path, "a")
fo.write("\nI work as a Data Scientist")
fo.close()

fo = open(file_path, "r")
file_content = fo.read()
print('The file after appending has : \n', file_content)
fo.close()

# g
file_path = r'C:\Users\yourname\Desktop\info.txt'
new_file_path = r'C:\Users\yourname\Desktop\personal_info.txt'
#os.rename(file_path, new_file_path)

path = r'C:\Users\yourname\Desktop\personal_info.txt'
file_name = os.path.basename(path)
print(file_name)


"""
2- Create a folder manually on your Desktop with the name test and save the following
image inside it with the name'python.png'. After that, write a Python program to:
a.	Read that 'python.png' file in binary mode and print the data type that you read
b.	Delete that file


"""
# a
file_path_1 = r'C:\Users\yourname\Desktop\test\python.png'
fo = open(file_path_1, "rb")
file_content = fo.read()
res = type(file_content)
print(res)
print(file_content)
fo.close()

# b
file_path_2 = r'C:\Users\yourname\Desktop\test\python.png'
# os.remove(file_path_2)