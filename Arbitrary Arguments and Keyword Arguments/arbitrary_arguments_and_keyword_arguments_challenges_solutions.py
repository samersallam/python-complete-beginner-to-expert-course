""" Arbitrary Arguments and Keyword Arguments Challenges

    Challenges

"""
"""

1- Define a Python function to find the maximum number assuming that the function can accept any number of arguments. 
Use your function to calculate the maximum of the following passed numbers
a. passed_numbers = (5, 6)
b. passed_numbers = (7, 6, 11, 22)
c. passed_numbers = (4, 9, 34, 100, 67)

"""
def maximum(a, *args):
    m = a

    for arg in args:
        if arg > m:
            m = arg

    return m

x1 = maximum(5, 6)
x2 = maximum(7, 6, 11, 22)
x3 = maximum(4, 9, 34, 100, 67)
print(x1)
print(x2)
print(x3)

"""

2- Define a Python function to print employee details. Use your function to print:
a.	first_name : ali, last_name : ali'
b.	first_name : khaled, last_name : shaaban, speciality = Engineering
c.	first_name : kamal, last_name : 'assad', age : 25


"""

def full_name(first, last, **kwargs):

    f = first
    l = last
    f_name = f'{f} {l}'
    print(f_name, 'details are ', kwargs)

full_name(first='ali', last='ali')
full_name(first='khald', last='shaaban', speciality= 'Engineering')
full_name(first='kamal', last='assad', age = 25)

