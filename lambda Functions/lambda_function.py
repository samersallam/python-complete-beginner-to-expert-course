""" Lecture: lambda Function

    Outlines
    1- lambda Function Syntax
    2- map() Function
    3- filter() Function

"""

# 1- lambda Function Syntax

# Example 1
def normal_func(x):
    return x * x


lambda_func = lambda x: x * x

res1 = normal_func(4)
res2 = lambda_func(4)

print(res1)
print(res2)

# Example 2

full_name = lambda first, last: f'{first} {last}'
res11 = full_name('Samer', 'Sallam')
res22 = full_name('John', 'Smith')
print(res11)
print(res22)

# Example 3

func1 = lambda x, y, z: x + y + z
res_f1 = func1(1, 2, 3)
print(res_f1)

func2 = lambda x, y, z=3: x + y + z
res_f2 = func2(1, 2)
print(res_f2)

func3 = lambda *args: sum(args)
res_f3 = func3(1, 2, 3, 4)
res_f31 = func3(1, 2, 3, 4, 5, 6, 7)
print(res_f3)
print(res_f31)

func4 = lambda **kwargs: sum(kwargs.values())
res_f4 = func4(four=1, five=2, six=6)
print(res_f4)

# 2- map() Function

"""
map(func, iterables) -> map object
Calls the given function for each item of a given iterable (list, tuple etc.)
and returns a map object(iterable)

"""

# Example 1

strs = ['HI', 'HELLO']

lowerd = map(lambda x: x.lower(), strs)
res = type(lowerd)
print(res)

for s in lowerd:
    print(s)

lowerd = map(lambda x: x.lower(), strs)
lowerd_list = list(lowerd)
print(lowerd_list)

# Example 2

lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]

lst_c = lst1 + lst2  # It is concatenation not addition
res_con = lst_c
print(res_con)

lst_a = map(lambda x, y: x + y, lst1, lst2)
res = list(lst_a)
print(res)

# 3- filter() Function

"""
filter(function, iterable) -> filter object
Returns an iterable from elements of another iterable for
which a function returns true
"""

# Example (find odd numbers)

lst = [1, 2, 3, 4, 5]

odd_fltrd = filter(lambda x: x % 2 != 0, lst)
t_odd = type(odd_fltrd)
l_odd = list(odd_fltrd)
print(t_odd)
print(l_odd)

# Example (find strings with more than 2 characters)

lst = ['a', 'aa', 'bb', 'ccc', 'dddd']
fltrd = filter(lambda x: len(x) > 2, lst)
res = list(fltrd)
print(res)
