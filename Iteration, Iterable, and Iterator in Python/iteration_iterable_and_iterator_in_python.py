""" Lecture: Iteration, Iterable and Iterator in Python

    Outlines
    1- Iterable and Iterator

"""

# 1- Iterable and Iterator

lst = [1, 2, 3, 4]

# Example 1

print('Traditional for loop')
for item in lst:
    print(item)

# Example 2

print('What happened behind the scene is ')
# Iterable: Is an object that when it is passed to the built-in iter() function, it returns an iterator

itr = iter(lst)
res = type(itr)
print(res)

# Iterator: Is an object that:
# 1-  Has the ability to save the current state(last item returned)
# 2- When it is passed to the built-in next() function, it returns the next item and updates the current state

# Example 3

itr = iter(lst)

item = next(itr)
print(item)

item = next(itr)
print(item)

item = next(itr)
print(item)

item = next(itr)
print(item)

#item = next(itr)   # This one will cause StopIteration error
#print(item)