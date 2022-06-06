""" Decorators in Python Challenges

    Challenges

"""

"""
1-
-   Define a python function “multiply” to multiply all list items by 2.
-	Define a python function “divide” to divide all list items by 2.
-	Define a Python function “process” that accepts two parameters (a function and a list).
    Inside the function “process”,
    call the function for the list and return the result.
-	Use your functions for the following list list1=[12, 13, 14]
a.	To multiply the list items by 2
b.	To divide the list items by 2

"""

def multiply(y):
    for i in range(0, len(y)):
        y[i] = y[i] * 2
    return y

def divide(y):
    for i in range(0, len(y)):
        y[i] = y[i] / 2
    return y

def process(function, x):
    result = function(x)
    return result

x1 = [12, 13, 14]
x2 = [12, 13, 14]

result1 = process(multiply, x1)
result2 = process(divide, x2)
print(result1)
print(result2)



"""
2- 
Define a Python function ‘course_details’ that takes one parameter ‘title’
and returns one of the following two functions according to the ‘title’
value : ‘python_beginner’ or ‘python_advance’.
Each one of these functions should print some details about the related course
a.	course1 = 'Python advance'
details: 'In this course we dive deeply in more complex topics using Python'
b.	course2 = 'Python beginner'
details: 'This course gives you Python basics'

"""
def course_details(title):
    def python_beginner():
        print('This course gives you Python basics')

    def python_advance():
        print('In this course we dive deeply in more complex topics using Python')

    if title == 'Python beginner':
        return python_beginner()

    if title == 'Python advance':
        return python_advance()




course1 = course_details('Python advance')
course2 = course_details('Python beginner')

"""
3- 
- Define a python function that calculates the square root of a number ‘a’
- Define a decorator that improves the previous function by printing
    the following message ‘no sqrt for negative number’
    when the passed number is less than zero
-	Test your decorated function for the following  two cases:
a.	-25
b.	25

 
"""

import math as m

def decorator(func):
    def wrapper(x):
        if x < 0:
            print('no sqrt for negative number')
            return None
        else:
            return func(x)

    return wrapper

@decorator
def compute_sqrt(num):
    result = m.sqrt(num)
    return result



res = compute_sqrt(-25)
res2 = compute_sqrt(25)
print(res)
print(res2)

"""
4- 
-   Define a function ‘task’ that returns the value of 6
-	Define two decorators.
    The first one ‘multiply’ multiplies the returned value of ‘task’ by 3,
    and the second one ‘divide’ divides the value of ‘task’ by 2
a.	Use each one of the decorators individually
b.	Use both decorators together taking into account that
    multiplication should be executed before division


"""

def decor1(func):
    def wrapper():
        x = func()
        return x / 2

    return wrapper


def decor(func):
    def wrapper():
        x = func()
        return 3 * x

    return wrapper

# 1


@decor
def task():
    return 6


res1 = task()
print(res1)


@decor1
def task():
    return 6


res2 = task()
print(res2)


# 2

@decor1
@decor
def task():
    return 6


res = task()
print(res)