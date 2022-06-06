""" Lecture: Namespaces and Scopes in Python

    Outlines:
    1- Built-in Namespace
    2- Global Namespace
    3- Local Namespace


"""

# 1- Built-in Namespace

# Example
a = min(1, 2, 3)  # min is available anywhere because it belongs to the Built-in Namespace (max - sum)
print(a)

# 2- Global Namespace

# Example
d = 5
print('d is : ', d)


def func1():
    print('d inside func1 is : ', d)

    def func2():
        print('d inside func2 is : ', d)

    func2()


func1()


# If you try to print d in any other module,
# an exception will be raised if you have not imported this variable


# 3- Local Namespace

# Example

def function1():
    x = 5

    def function2():
        print('Inside function2 x is : ', x)

    function2()

function1()
print('Out of function1 x is : ', x)
