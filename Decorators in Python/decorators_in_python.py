""" Lecture: Decorators in Python

    Outlines
    1- How to Pass Functions As Arguments
    2- How to Define Functions Inside Other Functions
    3- How to Create a Decorator
    4- How to Apply Multiple Decorators
"""

# 1- How to Pass Functions As Arguments

def increase(x):
    return x + 1


def decrease(x):
    return x - 1


def call(func, x):
    result = func(x)
    return result


x = 0
x = call(increase, x)
print(x)

x = 1
x = call(decrease, x)
print(x)


# 2- How to Define Functions Inside Other Functions

# Example 1

def say_hi(name):
    def hi(name):
        return f'Hi {name}'

    res = hi(name)

    return res


x = say_hi('Samer')
print(x)


# Example 2 (A function can return another function)
def greeting(word):
    def say_hi(name):
        return f'Hi {name}'

    def say_hello(name):
        return f'Hello {name}'

    if word == 'hi':
        return say_hi

    if word == 'hello':
        return say_hello


greeting_func = greeting('hi')
x = greeting_func('John')
print(x)

greeting_func = greeting('hello')
y = greeting_func('John')
print(y)


# 3- How to Create a Decorator

# Example 1
def div(a, b):
    return a / b

# x = div(4, 2)
# y = div(4, 0)
# print(x)
# print(y)


def decorator(func):
    def wrapper(x, y):
        if y == 0:
            print('the second argument cannot be zoro')
            return None
        else:
            return func(x, y)

    return wrapper


decorated_div = decorator(div)
w = decorated_div(4, 2)
print(w)
z = decorated_div(4, 0)
print(z)


# Example 2 (Another way to use decorator)


def decorator(func):
    def wrapper(x, y):
        if y == 0:
            print('the second argument cannot be zoro')
            return None
        else:
            return func(x, y)

    return wrapper


@decorator
def div(a, b):
    return a / b

n = div(4, 2)
print(n)
m = div(4, 0)
print(m)


# 4- How to Apply Multiple Decorators


def uppering(func):
    def wrapper():
        st = func()
        return st.upper()

    return wrapper


def lowering(func):
    def wrapper():
        st = func()
        return st.lower()

    return wrapper


@uppering
@lowering
def get_str():
    return 'Hi Samer'

res = get_str()
print(res)
