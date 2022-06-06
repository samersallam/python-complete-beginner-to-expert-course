""" "with" Keyword with Files Challenges

     Challenges

"""

"""
1- Create a txt file manually on your Desktop with the name “info.txt”
write 'hello python' inside it. After that:
a-	Open the file using open function, read the content,
    insert the following line of code, a = [1,2,3]; print(a[10]),
    close the file, and print the file status to know if it is closed or not.
    Make sure to use try – except to make the program be executed without any problem
b-	Open the file using open function with ‘with’ statement, read the content,
    insert the following line of code, a = [1,2,3]; print(a[10]) in the body of ‘with’,
     and print the file status out of with body to know if it is closed or not.
     Make sure to use try – except to make the program be executed without any problem

"""

# a
file_path = r'C:\Users\yourname\Desktop\info.txt'
fo = open(file_path, 'r')
try:
    res = fo.read()
    print(res)
    a = [1, 2, 3]
    print(a[10])
    fo.close()
    

except Exception as e:
    print(e)

status = fo.closed
print('file close status is ', status)

# b
file_path = r'C:\Users\yourname\Desktop\info.txt'
with open(file_path, 'r') as fo:
    try:
        res = fo.read()
        print(res)
        a = [1, 2, 3]
        print(a[10])
    except Exception as e:
        print(e)

status1 = fo.closed
print('file close status is ',status1)



