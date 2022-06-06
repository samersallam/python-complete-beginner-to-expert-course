""" Python Dictionaries Challenges

   Challenges

"""

"""
1-	Write a python program:
a)	Introduce yourself using python dictionary
b)	Did you includes your " age"
c)	What are the points (the dictionary keys) that you have covered when you introduce yourself?

"""
# a
me_dict = {'name': 'Micheal', 'age': 29, 'specialty': 'Computer engineering and automation'}
print(me_dict)

# b
res = 'age' in me_dict
print(res)

# c
res = me_dict.keys()
print(res)


"""
2-	Write a python program to:
a.	Define a dictionary contains your favorite movie info ("name", "release_year", "director") 
b.	Extract only your movie name
c.	Extract your movie info as a list of tuples
d.	Remove "release_year" from your dictionary
e.	Extract who is your movie director?

"""
# a
movie_dict = {'name': "The Shawshank Redemption", 'release_year': 1994, 'director': "Frank Darabont"}
print(movie_dict)

# b
res = movie_dict['name']
print(res)

# c
res = movie_dict.items()
print(res)

# d
del movie_dict['release_year']
print(movie_dict)

# e
res = movie_dict.get('director')
print(res)

"""
3-	Write a python program to:
a.	Define a dictionary which describes a cat,
    where it should include : name, color, age
b.	Change your cat color to "white"
c.	How many items in your cat_dict?
d.	Extract your cat info (the dictionary values)
e.	Remove your cat color using pop () function
f.	Remove all items from your cat_dict


"""
# a
cat_dict = {'name': "Lolo", 'color': "brown", 'age': " 1 year"}
print(cat_dict)

# b
cat_dict['color'] = 'white'
print(cat_dict)

# c
res = len(cat_dict)
print(res)

# d
res = cat_dict.values()
print(res)

# e
res = cat_dict.pop('color')
print(res)
print(cat_dict)

# f
cat_dict.clear()
print(cat_dict)

