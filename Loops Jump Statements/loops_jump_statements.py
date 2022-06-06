""" Lecture: Loops jump Statements

    Outlines
    1- Continue Statement
    2- Break Statement
"""

# 1- Continue Statement

# Continue Statement with for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    # if x == "banana":
    #     continue
    print(x)

# Continue Statement with while loop

i = 0
while i < 6:
    i += 1
    # if i == 3:
    #     continue
    print(i)


# 2- Break Statement

# Break with for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    # if x == "banana":
    #     break


# Break with for else
for i in range(1, 6):
    print(i)
    if i == 3:
        break
else:  # Not executed as there is a break
    print("No Break")

# Break with while loop

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1