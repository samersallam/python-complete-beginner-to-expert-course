""" Python Lists Functions Challenges

    Challenges

"""
""""
1- Write a Python program to print the following list_1
after removing the 4th element.
list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]
"""

list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]
list_1.remove(-4)
print(list_1)


"""
2-	If you have the following list_1:
list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]
Write a Python program to:
a.	Find list_1 length
b.	Find maximum number of list_1
c.	Find minimum number of list_1
d.	Find sum of list_1 element
e.	Add 9 to the list_1
f.	Add [' a', ' v', ' d'] to the list_1
g.	Remove -4 from list_1
h.	Insert ' r' to the second position of list_1
i.	Reverse the order of the list_1
j.	Find index of element 45 of the list_1
k.	How many 32 in list_1
l.	Remove the element in the fourth position
m.	Remove all the elements from the list_1

"""

list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]

# a
res = len(list_1)
print(res)

# b
res = max(list_1)
print(res)

# c
res = min(list_1)
print(res)

# d
res = sum(list_1)
print(res)

# e
list_1.append(9)
print(list_1)

# f
list_2 = ['a', 'v', 'd']
list_1.extend(list_2)
print(list_1)

# g
list_1.remove(-4)
print(list_1)

# h
list_1.insert(1, 'r')
print(list_1)

# i
list_1.reverse()
print(list_1)

# j
res = list_1.index(45)
print(res)

# k
res = list_1.count(32)
print(res)

# l
list_1.pop(3)
print(list_1)

# m
list_1.clear()
print(list_1)

