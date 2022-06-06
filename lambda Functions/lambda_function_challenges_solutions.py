""" lambda Function Challenges

    Challenges

"""

"""
1- Write a Python program to create a lambda function that adds 15 to the given
number ‘a’ that passed in as an argument.
Call your function for a = 10

"""

l = lambda a: a + 15
res1 = l(10)
print(res1)


"""
2- Write a Python program to create a lambda function that multiplies
the numbers x y, z assuming the default value of z is 4.
Print the result in the following cases:
a.	x = 12, y = 4 and use z as a default argument z = 4
b.	x = 3, y = 9, z = 11

"""

l = lambda x, y, z = 4: x * y * z
res1 = l(12, 4)
res2 = l(3, 9, 11)
print(res1)
print(res2)


"""
3- Write a Python program to create a lambda function that finds the maximum
of group numbers assuming that the function could accept any number of arguments. 
Print the result for following cases:
a.	 (10, -3, -4, 12)
b.	 (-12, -13, -5, -3, -9)

"""
l = lambda *args: max(args)
res1 = l(10, -3, -4, 12)
res2 = l(-12, -13, -5, -3, -9)
print(res1)
print(res2)

"""
4- Write a Python program to create a lambda function that finds the minimum
of group of numbers using **kwargs to make the function accept any number of keywords arguments.
Print the result for the following group of numbers: (-12, -13, -5, -3)

"""

l = lambda **kwargs: min(kwargs.values())
res1 = l(f=-12, s=-13, th=-5, fth=-3)
print(res1)

"""
5- Write a Python program to calculate the square of all elements of the list
num = [3, 5, 6, -10, 4.5] using lambda and map functions
"""
num = [3, 5, 6, -10, 4.5]
m = map(lambda x: x*x, num)

res_type = type(m)
print(res_type)

result = list(m)
print(result)

"""
6- Write a python program to find the positive numbers in the list 
num = [3, 5, 6, -10, 4.5, -11, -25, 9] using lambda and filter function

"""
num = [3, 5, 6, -10, 4.5, -11, -25, 9]
f = filter(lambda x: x >= 0, num)

res_type = type(f)
print(res_type)

res = list(f)
print(res)

