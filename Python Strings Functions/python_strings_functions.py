""" Lecture: Python Strings Functions

    Outlines
    1- Some Useful String Functions
    2- Is String Immutable
"""

# 1- Some Useful String Functions

# Assume we have the following strings

a = " I love apples, apple is my favorite fruit"

"""
len(obj: string) -> int
Determines how many items a string has
"""

res = len(a)
print(res)

"""
strip(chars = None) -> string
Returns a copy of the string with leading and trailing whitespace remove.
"""

# Example 1

res = a.strip()
print('Before strip is : ', a)
print('After strip is : ', res)

# Example 2

string = ",,,,,rrttgg.....banana....rrr"
res = string.strip(',.grt')
print('Before strip is : ', string)
print('After strip is : ', res)

"""
split (sep:None, maxsplit: int = -1) -> list
Returns a list of the words in the string, using sep as the delimiter string.
"""

# Example 1

res1 = a.split()
print('Before split is : ', a)
print('After split is : ', res1)

# Example 2

res = a.split(",", 1)
print('Before split is : ', a)
print('After split is : ', res)

"""
replace(old: string, new: string, count: int = -1) -> string
Returns a copy with all occurrences of substring old replaced by new.
"""

# Example 1

res = a.replace("f", "J")
print(res)

# Example 2

res = a.replace("f", "J", 1)
print(res)

"""
isspace() -> bool
Returns True if the string is a whitespace string, False otherwise.

"""

res = a.isspace()
print(res)

"""
isdigit() -> bool
Returns True if the string is a digit string, False otherwise.

"""

res = a.isdigit()
print(res)

"""
islower() -> bool
Returns True if all of the string letters are in lower case
"""
res = a.islower()
print(res)

"""
capitalize() -> string
Returns a copy of the string with the first character in upper case

"""

res = a.capitalize()
print(res)

"""
lower() -> string
Returns a copy of the string converted to lowercase.

"""

res = a.lower()
print(res)

"""
title() -> string
Returns a copy of the string where only the first letter of each string is uppercase,
and all remaining letters are lowercase. 
"""

res = a.title()
print(res)

"""
upper() -> string 
Converts lowercase letters in string to uppercase.

"""

res = a.upper()
print(res)

"""
count(sub: string, start: int=0, end: int=last index) -> int
Returns the number of times a specified value sub occurs in a string

"""

# Example 1

x = a.count("apple")
print(x)

# Example 2

x = a.count("apple", 7, 11)
print(x)

"""
find(sub: string, start: int=0, end: int=last index) -> int
Searches the string for a specified value and
returns the position of where it was found

"""

# Example 1

y = a.find('are')
print(y)

# Example 2

y = a.find('are', 2, 25)
print(y)




# 2- Is String Immutable

# Keep in mind that the string is immutable

# try this also string[0] = 'm'