""" Lecture : Lines in Python

    Outlines
    1- Single-Line Statement
    2- Multiple-Line Statement
    3- Multi-Statement in One Line
"""
# 1- Single-Line Statement

# Example 1
y = 3 + 5
print('y = ', y)

# Example 2
a = 3
b = 5
c = (a + b) * 2
print('c = ', c)

# 2- Multiple-Line Statement
a = 3
b = 5
c = (a + b) + \
    2 * b + \
    3 * a
print('multi_line c =', c)

# If a statement uses [], {}, or () brackets, we do not need to use the line continuation character
lst = ['python',
       'ML',
       'DL']

dct = {
    'name': 'Samer',
    'Age': 30
}
print(lst)
print(dct)

# 3- Multi-Statement in One Line
first_name = 'Samer'; last_name = 'Sallam'; print('Full name is', first_name, last_name)

a = 5; b = a * a; print('a square is', b)
