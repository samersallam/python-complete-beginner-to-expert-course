""" Bitwise Operators Challenges

   Challenges

"""
"""
1- Assume you have: a = 60, b=13, write a Python program to find the result of:
a.	a And b 
b.	a Or b
c.	a Xor b
d.	COMPLEMENT
e.	Left Shift of a with 2 bits shift
f.	Right Shift of b with 2 bits shift          
"""
a = 60
b = 13
# a
and_ = a & b

# b
or_ = a | b

# c
xor_ = a ^ b

# d
comp_a = ~ a

# e
ls = a << 2

# f
rs = b >> 2

print('a and b is : ', and_)
print('a or b is : ', or_)
print('a xor b is : ', xor_)
print(' complement a is : ', comp_a)
print(' left shift a is : ', ls)
print('right shift b is : ', rs)