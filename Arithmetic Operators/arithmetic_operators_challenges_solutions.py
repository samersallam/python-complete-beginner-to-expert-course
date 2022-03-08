""" Arithmetic Operators Challenges

   Challenges

"""
"""
1- Write a Python program to calculate a rectangle area if you have:
a.	width = 5 cm, length = 10 cm
b.	length = 10 cm, circumference = 30 cm

"""
# a
L = 10
W = 5
print('area = L * W =', L * W)

# b
C = 30
area = (C*L-2 * L ** 2)/2
print('area = (C*L-2 * L ** 2)/2 =', area)


"""
2- Write a Python program to find the modulus and floor division of:
    A = 145, B= 24

"""
a = 145
b = 24
m = a % b
f = a // b
print('modulus is : ', m)
print('floor division is : ', f)