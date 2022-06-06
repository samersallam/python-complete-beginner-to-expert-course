""" Lecture: Python Strings

    Outlines
    1- How to Create a String
    2- Special Characters
    3- String Operators
    4- Accessing to String Content
    5- String Slicing
"""

# 1- How to Create a String
string = 'Welcome to python world'
print(string)

string = "Welcome to python world"
print(string)

string = """ Welcome to python world """
print(string)

string = ''' Welcome to python world '''
print(string)

# Notes about how to create a string
string = "Hi I'm John"  # Double quotes are used because a single quote is used as a character in the stringing
print(string)

string = 'You are from "USA"'  # A single quote is used because double quotes are used as a character in the stringing
print(string)

# Triple quotes are used because we create a string over multiple lines
# (it has also some single quotes and double quotes)
string = """ 
       Python is a great programming language ''
       You have to learn Python    " " 
       """
print(string)

# 2- Special Characters
string = 'Hello Samer\nHow are you?'
print(string)

string = 'Hello Samer\tHow are you?'
print(string)

# 3- String Operators

string1 = 'Hello '
string2 = 'World'

# Concatenation (+)

new_string = string1 + string2
print(new_string)

# Concatenation and Assign (+=)

string1 += string2
print(string1)

# Repetition (*)

new_string = string2 * 5
print(new_string)

# Repetition and Assign (*=)

string2 *= 5
print(string2)

# Membership (in, not in)

# in

res = 'e' in string1
print(res)

# in

res = 'h' in string1
print(res)

# not in

res = 'q' not in string1
print(res)

# not in

res = 'o' not in string1
print(res)

# 4- Accessing to String Content

string = "Hello World"

res1 = string[1]
res2 = string[-1]
print('The character at the second position is : ', res1)
print('The last character is : ', res2)

# 5- String Slicing

string = "Hi Python Developers"

# Get the word "Python"

slc = string[3: 10]
print(slc)
type_slc = type(slc)
print(type_slc)

# Get the word "Hi"

slc = string[0:2]  # u can remove 0
print(slc)

# Get the word "Developers"

slc = string[10:20]  # u can remove 20
print(slc)

# Get the word "Developers" by using negative index

slc = string[-10:]  # u can remove 20
print(slc)


