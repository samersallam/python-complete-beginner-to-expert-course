""" Logical Operators Challenges

   Challenges

"""
"""
1- Assume you have the inputs a=False, b=True, c=True
write a Python program to find the value of q where:
q = (a and b) or ((b or c) and (b and c))

"""
a = False; b = True; c = True
q = (a and b) or ((b or c) and (b and c))
print('q = (a and b ) or ((b or c) and (b and c)) =', q)

"""
2- Assume you have a = False, write a Python program to find the result of
not a 
"""
a = False
res = not a
print('not a = ', res)