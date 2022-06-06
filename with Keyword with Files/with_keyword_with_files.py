""" Lecture: "with" Keyword with Files

    Outlines:
    1- with syntax and example

"""

# 1- with syntax and example

# fo.closed attribute
file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
fo = open(file_path, "r")
clo1 = fo.closed
print('The file is closed : ', clo1)
fo.close()

# A case when a file will not be closed
try:
    file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
    fo = open(file_path, "r")
    file_content = fo.read()

    a = [1, 2, 4]
    b = a[10]

    fo.close()
except:
    print('There is an error')
clo = fo.closed
print('The file is closed : ', clo)

# To make sure that the file is going to be closed
file_path = r'C:\Users\Samer\Desktop\test\dummy.txt'
with open(file_path) as fo:  # fo = open(file_path, "r")
    try:
        file_content = fo.read()

        a = [1, 2, 4]
        b = a[10]

        
    except:
        print('There is an error')
clo2 = fo.closed
print('The file is closed : ', clo2)
