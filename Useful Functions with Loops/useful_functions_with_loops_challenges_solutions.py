""" Useful Functions With Loops Challenges

   Challenges

"""

"""
1-  Can you iterate over a string fruit = "Apple"
"""

fruit = "Apple"
for i, j in enumerate(fruit):
        print(i, j)

"""
2- Write a Python program to perform sum of the first 10 numbers from 1
using range function
"""
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)

"""
3- Write a python program to join the following tuples first_name, last_name,
to get a full name as a result,

"""
first_name = ("John", "Charles", "Mike")
last_name = ("Jenny", "Christy", "Monica")
res = zip(first_name, last_name)
print('type res is : ', res)

for i, j in res:
    print(i, j)

"""
4- Write a Python program to print all numbers from 0 to 5,
and print a message when the loop ends
  
"""
for x in range(6):
  print(x)
else:
  print("Finally finished!")



