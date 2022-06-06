""" Lecture : String Formatting

    Outlines
    1- Old Style String Formatting (%)
    2- New Style String Formatting (format())
    3- String Interpolation / f-Strings (f)

"""

# 1- Old Style String Formatting (%)

# %d - Integers
template = "My name is John, and I am %d years old"
value = 25
string = template % value
print(string)

# %s - String (or any object with a string representation)
template = "My name is %s, and I am %d years old"
value1 = 'Ali'
value2 = 30
string = template % (value1, value2)
print(string)

# %f - Floating point numbers
template = "My name is %s, and my weight is %f [KG]"
value1 = 'Huda'
value2 = 63.5
string = template % (value1, value2)
print(string)

# %.<number of digits>f - Floating point numbers with a fixed number of digits to the right of the dot
template = "My name is %s, and my weight is %.2f [KG]"
value1 = 'Huda'
value2 = 63.5
string = template % (value1, value2)
print(string)

# 2- New Style String Formatting (format())

# Example 1
template = "My name is {}, and I am {} years old"
value1 = 'Sarah'
value2 = 24
string = template.format(value1, value2)
print(string)

# Example 2
template = "My name is {1}, and my weight is {0} [KG]"
string = template.format(65, 'Ali')
print(string)

# Example 3
template = "My name is {}, and my weight is {:0.2f} [KG]"
value1 = 'Ola'
value2 = 50
string = template.format(value1, value2)
print(string)

# Example 4
template = "My name is {1}, and my weight is {0: 0.2f} [KG]"
string = template.format(60, 'Falak')
print(string)


# 3- String Interpolation / f-Strings (f)
name = 'Samer'
weight = 70.5
string = f"My name is {name}, and my weight is {weight} [KG]"
print(string)


