""" Python Sets Challenges

   Challenges

"""

"""
1-	Write a Python program to:
a.	Create a set containing your favorite colors. Assume (yellow - green)
b.	Are {'white', 'blue'} part of your favorite colors
    (answer in two different ways)
c.	Are your favorite colors part of
   {'white', 'blue', 'brown', 'red', 'yellow', 'green', 'pink'}
   (answer in two different ways) 
d.	Determine how many items in your set


"""
# a
color_set = {'yellow', 'green'}
print(color_set)

# b

# answer 1
new_set = {'white', 'blue'}
res = new_set.issubset(color_set)
print(res)

# answer 2
new_set = {'white', 'blue'}
res = new_set <= color_set
print(res)

# c
# answer 1
new_set = {'white', 'blue', 'brown', 'red', 'yellow', 'green', 'pink'}
res = new_set.issuperset(color_set)
print(res)

# answer 2
new_set = {'white', 'blue', 'brown', 'red', 'yellow', 'green', 'pink'}
res = new_set >= color_set
print(res)

# d
res = len(color_set)
print(res)

"""
2-	Assume you have s1= {10, 23, 65, 78, 90, 54}:
a.	Find the minimum number in your set
b.	Find the maximum number in your set
c.	Find the summation of your set numbers
d.	Add 100 to your set
e.  Find the difference between s1 and s2 where
 s2 = {66, 77, 88, 65, 10} (answer in two different ways) 
f.	What are the shared numbers between s1, s3 where
s3= {67, 78, 9, 11, 12} (answer in two different ways)
g.	Find the union of s1, s4 where s4 = {'w', 'p', 'q'}
(answer in two different ways)

"""
# a
s1= {10, 23, 65, 78, 90, 54}
res = min(s1)
print(res)

# b
res = max(s1)
print(res)

# c
res = sum(s1)
print(res)

# d
s1.add(100)
print(s1)

# e

# answer 1
s2 = {66, 77, 88, 65, 10}
res = s1 - s2
print(res)

# answer 2
s2 = {66, 77, 88, 65, 10}
res = s1.difference(s2)
print(res)

# f

# answer 1
s3 = {67, 78, 9, 11, 12}
res = s1.intersection(s3)
print(res)

# answer 2
s3 = {67, 78, 9, 11, 12}
res = s1 & s3
print(res)

# g

# answer 1
s4 = {'w', 'p', 'q'}
res = s1 | s4
print(res)

# answer 2
s4 = {'w', 'p', 'q'}
res = s1.union(s4)
print(res)

