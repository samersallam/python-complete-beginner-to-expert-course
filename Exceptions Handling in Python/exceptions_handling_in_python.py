""" Lecture: Exceptions Handling in Python

    Outlines
    1- try-except-else
    2- try-except-else With Specific Exceptions

"""

# 1- try-except-else

# Example 1
try:
    a = 2 / 0
except:
    print("An exception has been raised")
else:
    print("Everything went ok")

# Example 2 (else is optional)
try:
    a = 2 / 0
except:
    print("An exception has been raised")

# Example 3 (You can get the exception object by using 'Exception as e')
try:
    a = 2 / 4
except Exception as e:
    print(e)
else:
    print("Everything went ok")

# Example 4 (Another type of exception is index error)
try:
    a = [1, 2, 3]
    b = a[8]

except Exception as e:
    print('Sending the error to the system logger')
    print(f'The following exception ({e}) has been raised')
else:
    print("Everything went ok")

# 2- try-except-else With Specific Exceptions

# Example 1
try:
    a = 2 / 0

except ZeroDivisionError:
    print("ZeroDivisionError has been raised")
    print('Please make sure that the denominator is not zero')

except:
    print('An exception has been raised')

# Example 2
try:
    a = 2 / 4

    c = [1, 2, 3]
    d = c[8]

except ZeroDivisionError:
    print("ZeroDivisionError has been raised")
    print('Please make sure that the denominator is not zero')

except:
    print('An exception has been raised')

# Example 3
try:
    a = 2 / 4

    c = [1, 2, 3]
    d = c[8]

except ZeroDivisionError:
    print("ZeroDivisionError has been raised")
    print('Please make sure that the denominator is not zero')

except IndexError:
   print(f'Please make sure that the index is between 0 and {len(c) - 1}')

except:
    print('An exception has been raised')


