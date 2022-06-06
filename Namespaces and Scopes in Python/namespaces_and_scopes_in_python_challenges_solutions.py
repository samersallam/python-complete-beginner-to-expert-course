""" Namespaces and Scopes in Python Challenges

    Challenges

"""
"""
1- Write a Python Program to:
a.	Define a function that defines and prints the variable s = "I love Python!",
    and then try to print the same variable s out of the function,
    Is there any error and why?
b.	Define a function that print a variable s before assignment and see the errors 


"""

# 1


def our_func():
    s = "I love Python!"
    print(s)



our_func()
print(s)


# 2
def our_func():
    print(s)
    s = "I love Python!"


our_func()


