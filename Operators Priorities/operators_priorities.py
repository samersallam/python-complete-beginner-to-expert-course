""" Lecture: Operators Priorities

    Outlines
    1- The highest priority is to start executing what inside Parentheses (grouping) is
    2- When two operators have the same priority, the operator on the left is executed first
"""
a = 20
b = 10
c = 15
d = 5


# 1- The highest priority is to start executing what inside Parentheses (grouping) is

e = a + (b * c) / d
print("Value of a + (b * c) / d is ",  e)

# 2- When two operators have the same priority, the operator on the left is executed first

e = (a + b) * (c / d)
print("Value of (a + b) * (c / d) is ",  e)