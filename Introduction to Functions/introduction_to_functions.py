""" Lecture : Introduction to Functions

    Outlines
    1- Why Functions Are Important
    2- How To Define and Call Functions
    3- How to Document a Function
"""

#  1- Why Functions Are Important (Reusability and Maintainability)
# Assume you want to use this snippet of code in 100 different places in your project
print('Hello World 1')
print('Hello World 2')
print('Hello World 3')
print('Hello World 4')


#  2- How To Define and Call a Function
# Define
def say_hi():
    print("Hi Man")

# Call
say_hi()


#  How to Pass Arguments to a Function

# Example 1

def say_hi(name):
    res = f"Hi {name}"
    print(res)

# Call
say_hi('Samer')
say_hi('John')


# Example 2

def say_hi(title, name):
    res = f"Hi {title} {name}"
    print(res)

# Call
say_hi('Eng.', 'Samer')
say_hi('Dr.', 'John')
say_hi(title='Dr.', name='John')
say_hi(name='John', title='Dr.')

# The function does not return anything, it just print
def say_hi(title, name):
    res = f"Hi {title} {name}"
    print(res)

say_hi('Dr.', 'John')



#  How to Return Value(s) From a Function

# Example 1

def calculate_age(birth_year, year):
    age_per_year = year - birth_year
    return age_per_year


age = calculate_age(1992, 2020)
print(age)

# Example 2


def calculate_age2(birth_year, year):
    age_per_year = year - birth_year
    age_per_day = age_per_year * 365
    return age_per_year, age_per_day


age_year, age_day = calculate_age2(1992, 2020)
print(age_year)
print(age_day)


#  How to Use Default Parameters Values

# Example 1

def say_hi(name='Man'):
    res = f"Hi {name}"
    print(res)


say_hi()
say_hi('Samer')

# Example 2


def say_hi(title, name='Man'):  # Try to swap between title and name
    res = f"Hi {title} {name}"
    print(res)


say_hi('')


# 3- How to Document a Function

def say_hi(title, name):
    """ This function prints a welcome sentence
        Inputs: - title (string): the person title
                - name (string): the person name
        Outputs: This function does not return anything
     """
    res = f"Hi {title} {name}"
    print(res)


help(say_hi)

