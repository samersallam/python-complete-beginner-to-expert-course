""" Python Conditional Statements Challenges

   Challenges

"""
"""
1- Write a Python program that tell you
if your new email address is available or not.
used_emails = ['student1@gmail.com', 'student2@gmail.com', 'student6@gmail.com']
new_email = 'student6@gmail.com'

"""

used_emails = ['student1@gmail.com', 'student2@gmail.com', 'student6@gmail.com']
new_email = 'student6@gmail.com'
if new_email in used_emails:
    print('your new email is used before')
else:
    print('your new email is available')



"""
2- Create a calculator supporting the main four arithmetic operators (+, -, /, *)
The user should enter two operands and the operator symbol. After that, 
the calculator should be able to identify the operator and print the result after calculation.
"""

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(+, -, *, /): ")

# Check if choice is one of the four options
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '+':
    res = num2 + num1
    print('num1 + num2 is : ', res)


elif choice == '-':
    res = num1 - num2
    print('num1 - num2 is : ', res)


elif choice == '*':
    res = num1 * num2
    print('num1 * num2 is : ', res)


elif choice == '/':
    if num2 != 0:
        res = num1 / num2
        print('num1 / num2 is : ', res)
    else:
        print('Divide by zero error')

else:
    print('Invalid choice')

