""" Python Strings Functions Challenges

   Challenges

"""

"""
1- Write a Python program to calculate the length of the given string
course = ' python beginner to advance '

"""
course = ' python beginner to advance '
res = len(course)
print(res)

"""
 2- Write a Python program to get a string from the given string str1
where all occurrences of its first char have been changed to '#',
except the first char itself.
str1 = 'restart'
"""
str1 = 'restart'
char = str1[0]
str1 = str1.replace(char, '#')
str1 = char + str1[1:]
print(str1)

"""
3- Assume we have the string " python, beginner to advance course ",
write a Python program to:

a.	Remove the word "  python,"
b.	Split this sentence by ","
c.	Replace the word " advance " with "beginner"
d.	Check if the characters are whitespaces
e.	Check if the characters are digits
f.	Check if the characters are lower case
g.	Change the string to title form
h.	Convert the first character to upper case
i.	Count how many "course" words there
j.	Convert the first letter to lower case
k.	Find the position of 'to' 
l.	Convert all letters to upper case

"""
s1 = " python, beginner to advance course "

# a

res = s1.strip(" python,")
print(res)

# b

res = s1.split(",")
print(res)

# c

res = s1.replace("advance", "beginner")
print(res)

# d
res2 = s1.isspace()
print(res2)

# e
res3 = s1.isdigit()
print(res3)

# f
resf = s1.islower()
print(resf)

# g
resg = s1.title()
print(resg)

# h
res4 = s1.capitalize()
print(res4)

# i
res5 = s1.count('course')
print(res5)

# j
res6 = s1.lower()
print(res6)

# k
res7 = s1.find('to')
print(res7)

# l
res8 = s1.upper()
print(res8)

