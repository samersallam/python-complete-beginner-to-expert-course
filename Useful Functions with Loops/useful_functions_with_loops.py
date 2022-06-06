""" Lecture: Useful Functions With Loops

    Outlines
    1- range()
    2- enumerate()
    3- zip()
"""
"""

range(start: int, stop: int, step: int= 1) -> range object
Returns an iterable which generates a sequence of numbers starting from start,
incrementing by step and stopping before stop

"""


# Example 1

x = range(3, 6)
res = type(x)
print('type x is : ', res)

for n in x:
  print(n)

# Example 2
# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1
x = range(3, 20, 2)
res = type(x)
print('type x is : ', res)

for n in x:
  print(n)

"""

enumerate(iterable, start: int =0) --> enumerate object
Takes an iterable and returns another iterable generating a counted version of the original iterable.
The counter starts from start parameter

"""

# Example 1
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
res = type(y)
print('type y is : ', res)
print(y)
print(list(y))

# Example 2
# enumerate with for Loop
person = ['Alfred', 'Ally', 'Belinda']
height = [170, 160, 155]
for i, name in enumerate(person):
    h = height[i]
    print("The height of {} is {}cm".format(name, h))

"""

zip(iter1, iter2,..,*iters) --> zip object
Takes several iterables and returns one iterable aggregating all the inputs together. 
It is used when we want to loop over two or more than two iterables together


"""

# Example 1
a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd', 'e', 'f']

c = zip(a, b)
res = type(c)
print('type c is : ', res)
for i, j in c:
    print(i, j)

# Example 2
a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd', 'e', 'f']
c = ['s1', 's2', 's3', 's4', 's5', 's6']

d = zip(a, b, c)
res = type(d)
print('type d is : ', res)

for i, j, q in d:
    print(i, j, q)



