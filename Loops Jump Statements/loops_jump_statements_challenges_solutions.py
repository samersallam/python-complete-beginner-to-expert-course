""" Loops jump Statements Challenges

   Challenges

"""

"""
1- Write a Python program that prints all the numbers from 0 to 6
except 3 and 6.
"""
for x in [0,1,2,3,4,5,6]:
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

"""
2- Write a Python program that prints all items in available_names list
and stop when name = "ali"

"""

available_names = ['samer', 'sarah', 'ali', 'ashraf']
for name in available_names:
    print(name)
    if name == 'ali':
        break


"""
3-	Write a Python program to print the variable’s value (grater than zero)
and stop when the variable = 6, each time its value is reduced by one
where variable = 15

"""
variable = 15
while variable > 0:
   print ('Current variable value :', variable)
   variable = variable -1
   if variable == 6:
      break

"""
4-	Write a Python program to print variable’s value (grater than zero)
except 6, each time its value is reduced by one,
where variable = 15

"""
variable = 15
while variable > 0:
   variable = variable -1
   if variable == 6:
      continue
   print ('Current variable value :', variable)