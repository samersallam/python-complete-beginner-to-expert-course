""" Lecture: Bitwise Operators

    Outlines
    1- Bitwise AND Operator (&)
    2- Bitwise Or Operator (|)
    3- Bitwise Xor Operator (^)
    4- Bitwise Not Operator (~)
    5- Bitwise Left Shift Operator (<<)
    6- Bitwise Right Shift Operator (>>)
"""

a = 17  # 10001
b = 19  # 10011

# 1- Bitwise AND Operator (&)
c = a & b
print('a & b is : ', c)

# 2- Bitwise OR Operator (|)
c = a | b
print('a | b is : ', c)

# 3- Bitwise XOR Operator (^)
c = a ^ b
print('a ^ b is : ', c)

# 4- Bitwise NOT Operator (~)
c = ~b
print('~ b is : ', c)

# 5- Bitwise Left Shift Operator (<<)
c = a << 2
print('a << 2 is : ', c)

# 6- Bitwise Right Shift Operator (>>)
c = a >> 2
print('a >> 2 is : ', c)
