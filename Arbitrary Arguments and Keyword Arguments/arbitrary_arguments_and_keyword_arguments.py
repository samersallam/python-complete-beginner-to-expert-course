""" Lecture: Arbitrary Arguments and Keyword Arguments

    Outlines
    1- Arbitrary Arguments
    2- Keywords Arguments
    3- Arbitrary Arguments and Keywords Arguments
"""


# 1- Arbitrary Arguments

# Example 1
def dummy(a, b, *args):
    print('a is : ', a)
    print('b is : ', b)
    ty = type(args)
    print('The arg type is : ', ty)
    print('args is : ', args)
    print(10 * '-')


dummy(1, 2)
dummy(1, 2, 4, 5)
dummy(1, 2, 4, 5, 6, 7)


# Example 2

def minimum(a, *args):
    m = a

    for arg in args:
        if arg < m:
            m = arg

    return m

x1 = minimum(1, 2)
x2 = minimum(1, 2, 4, 5)
x3 = minimum(1, 2, 5, 6, 7, -1)
print(x1)
print(x2)
print(x3)


# 2- Keywords Arguments

# Example 1
def dummy(a, b, **kwargs):
    print('a is : ', a)
    print('b is : ', b)
    ty = type(kwargs)
    print('The kwargs type is : ', ty)
    print('kwargs is : ', kwargs)
    print(10 * '-')


dummy(1, 2)
dummy(1, 2, name='samer')
dummy(1, 2, name='samer', title='eng')


# Example 2
def fruit_colors(**kwargs):
    for f, c in kwargs.items():
        co = f'The color of {f} is {c}'
        print(co)


fruit_colors(banana='yellow', apple='red')


# 3- Arbitrary Arguments and Keywords Arguments

def general_function(a, b, c='I am c', d='I am d', *args, **kwargs):
    print('a is : ', a)
    print('b is : ', b)
    print('c is : ', c)
    print('d is : ', d)
    print('args is : ', args)
    print('kwargs is : ', kwargs)


general_function(1, 2)
general_function(1, 2, 'C is changed', 'D is changed')
general_function(1, 2, 'C is changed', 'D is changed', 5, 6, 7)
general_function(1, 2, 'C is changed', 'D is changed', 5, 6, 7, name='samer', title='Eng')
