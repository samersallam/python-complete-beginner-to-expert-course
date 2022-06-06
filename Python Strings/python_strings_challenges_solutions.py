""" Python Strings Challenges

   Challenges

"""

"""
1- Write a Python program to create and print the string q,
using single quotes and double quotes
(The string is (Python Beginner to advance))

"""
q1 = 'Python Beginner to advance'
q2 = "Python Beginner to advance"
print(q1)
print(q2)

"""
2- Write a Python program to create and print the string 
d = ' In this course, you will be able to start programming in Python ',
using special characters after the comma :
a.	\n
b.	 \t 

"""

n = ' In this course,\nyou will be able to start programming in Python '
print(n)
t = ' In this course,\t you will be able to start programming in Python '
print(t)


"""
3- Write a Python program to get a new string containing two strings s1,s2
using string concatenation operator 
s1="Python", s2 ="course"
 
"""

s1 = "Python "
s2 = "course"
res = s1 + s2
print(res)


"""
4- Write a Python program to get a new copy of string s1 after repeat it
three times using string repetition and assign  operator
s1 = "Python"

"""
#
s1 = "Python"
s1 *= 3
print(s1)

"""
5- Write a Python program to find if the word "course" is contained
in the sentence " You are welcome to this Python course "
 
"""

w1 = "course"
s1 = " You are welcome to Python course "
res = w1 in s1
print(res)

"""
6- Write a Python program to get a string made up of the first 3 and the last 2 chars
from the given string a = 'you like to learn Python'.     
"""
a = 'you like to learn Python'
b = a[0:4] + a[-2:]
print(b)

"""
7- Write a Python program to give you the third and the last letters from the given string
" You are welcome to Python course "
"""

s1 = "You are welcome to Python course"
third = s1[2]
last = s1[-1]
print(third)
print(last)

"""
8- Write a Python program to give you the word " data " from the given sentence 
" Python supports 6 data types "
"""

s1 = " Python supports 6 data types "
w1 = s1[-11: -7]
print(w1)


