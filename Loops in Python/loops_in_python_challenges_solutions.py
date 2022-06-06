""" Loops in Python Challenges

   Challenges

"""

"""
1- Write a Python program to find those numbers which
are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).
"""
nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(nl)

"""
2- Write a Python program to count the number of even and odd numbers
from the following series

"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)

"""
3- Write a Python program that prints each item
and its corresponding type from the following data_list.

"""

datalist = [1452, 11.23, 1+2j, True, (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))



"""
4- Write a Python program which prints the word 'hello' for 10 times using while loop

"""
i = 0
while i < 10:
    print('hello')
    i+=1


