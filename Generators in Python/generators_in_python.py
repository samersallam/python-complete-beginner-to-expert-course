""" Lecture: Generators in Python

    Outlines
    1- Generators Expressions
    2- Generators Functions

"""
numbers = [1, 2, 3, 4, 5, 6]

# 1- Generators Expressions

# Example 1 ( <expression> for <element> in <iterable> )


# I want 'n**2' for each 'n' in the list 'numbers'
gen1 = (n ** 2 for n in numbers)
print(gen1)

# How to extract the values (The first way using next())
f = next(gen1)
print('The first item : ', f)
s = next(gen1)
print('The second item : ', s)
th = next(gen1)
print('The third item : ', th)
fo = next(gen1)
print('The fourth item : ', fo)
fif = next(gen1)
print('The fifth item : ',fif)
six = next(gen1)
print('The sixth item : ', six)
# next(gen1)

# How to extract the values (The second way using for loop)

gen1 = (n ** 2 for n in numbers)
for val in gen1:
    print(val)

# Example 2 ( <expression> for <element> in <iterable>  if  <condition> )

# I want 'n**2' for each 'n' in the list 'numbers' if 'n>2'
gen2 = (n ** 2 for n in numbers if n > 2)

# How to extract the values (The first way using next())
f2 = next(gen2)
print('The first item : ', f2)
s2 = next(gen2)
print('The second item : ', s2)
s3 = next(gen2)
print('The third item : ', s3)
s4 = next(gen2)
print('The fourth item : ', s4)
# next(gen2)

# How to extract the values (The second way using for loop)

gen2 = (n ** 2 for n in numbers if n > 2)
for val in gen2:
    print(val)

# Example 3 ( <expression> if <condition> else < expression> for <element> in <iterable> )


# I want 'n**2' if 'n>2' else I want 'n/2' for each 'n' in the list 'numbers'
gen3 = (n ** 2 if n > 2 else n / 2 for n in numbers)

# How to extract the values (The first way using next())
f3 = next(gen3)
print('The first item : ', f3)
f4 = next(gen3)
print('The second item : ', f4)
f5 = next(gen3)
print('The third item : ', f5)
f6 = next(gen3)
print('The fourth item : ', f6)
f7 =  next(gen3)
print('The fifth item : ',f7)
f8 = next(gen3)
print('The sixth item : ', f8)
# next(gen3)

# How to extract the values (The second way using for loop)

gen3 = (n ** 2 if n > 2 else n / 2 for n in numbers)
for val in gen3:
    print(val)


# 2- Generators Functions
# Example 1
def gen_func1():
    n = 1
    yield n


gen = gen_func1()
print(gen)
res = next(gen)
print(res)


# print(next(gen))


# Example 2
def gen_func2():
    n = 1
    yield n

    n = n + 1
    yield n

    n = n + 1
    yield n


# How to extract the values (The first way using next())
gen = gen_func2()
res1 = next(gen)
print(res1)
res2 = next(gen)
print(res2)
res3 = next(gen)
print(res3)
#print(next(gen))

# How to extract the values (The second way using for loop)
def gen_func2():
    n = 1
    yield n

    n = n + 1
    yield n

    n = n + 1
    yield n

for item in gen_func2():
    print(item)

# Example 3
for k in range(5):
    print(k)


def range2(n):
    """ This generator generate even numbers up to n """
    for k in range(n):
        if k % 2 == 0:
            yield k


for k in range2(5):
    print(k)

# Talk about large files example (unique words)
