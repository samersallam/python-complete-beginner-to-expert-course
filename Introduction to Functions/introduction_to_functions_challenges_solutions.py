""" Introduction to Functions Challenges

   Challenges

"""

"""
1- Define a Python function to find the minimum of three numbers (3, 6, -5)..
"""
def min_of_two(x, y):
    if x < y:
        return x
    return y


def min_of_three(x, y, z):
    return min_of_two(x, min_of_two(y, z ))


res = min_of_three(3, 6, -5)
print(res)

"""
2- Define a Python function to find the average of the list l items
l = [8, 2, 3, 0, 7] 
"""


def calculate_average(numbers):
    total = 0
    for x in numbers:
        total += x

    le = len(numbers)
    res = total / le
    return res


l = [8, 2, 3, 0, 7]
print(calculate_average(l))

"""
3- Define a Python function that takes the list [1, 2, 3, 3, 3, 3,9, 11, 9, 4, 5]
and returns a new list containing unique elements of the first one.

"""


def unique(list1):
  x = []
  for a in list1:
    if a not in x:
      x.append(a)
  return x


res = unique([1, 2, 3, 3, 3, 3, 9, 11, 9, 4, 5])
print(res)

"""
4- Define a Python function that prints the following variables values
 (first_name, last_name, full_name). 
The default values are last_name: smith and full_name: john smith

"""


def func(first_name, last_name='smith', full_name='john smith'):
    print('first_name is', first_name)
    print('last_name is', last_name)
    print('full_name is', full_name)

print('---------------')
func('john', 'smith')
print('---------------')


"""
5- Redefine the function calculate_average mentioned in the question 2,
and then add the following sentence as a documentation string to this function: 

This function is to find the average of a list of numbers
"""


def calculate_average(numbers):

    """
    This function is to find the average of a list of numbers
    """
    total = 0
    for x in numbers:
        total += x

    le = len(numbers)
    res = total / le
    return res


help(calculate_average)

