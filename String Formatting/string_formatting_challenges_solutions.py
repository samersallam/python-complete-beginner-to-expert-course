""" String Formatting Challenges

    Challenges

"""

"""
1- Create a string template (Blue Fields) to pass values (Red Fields) to the receipt
using the three methods of string formatting (receipt example.png)
 
"""

# %
date = '04/29/08'
time = '18:22'
atm_num = 'NYO134'
amount = 400.00

template = 'CHASE: Date: % s, Time: %s, ATM NUMBER: %s, AMOUNT = %f $'
string = template % (date, time, atm_num, amount)
print(string)

# format()
date = '04/29/08'
time = '18:22'
atm_num = 'NYO134'
amount = 400.00

template = 'CHASE: Date: {}, Time: {}, ATM NUMBER: {}, AMOUNT = {} $'
string = template.format(date, time, atm_num, amount)
print(string)

# f
date = '04/29/08'
time = '18:22'
atm_num = 'NYO134'
amount = 400.00

string = f'CHASE: Date: {date}, Time: {time}, ATM NUMBER: {atm_num}, AMOUNT = {amount} $'
print(string)
