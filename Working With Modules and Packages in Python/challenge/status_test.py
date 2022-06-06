""" Working With Modules and Packages in Python Challenges

    Challenges

"""

"""
1- Do the following tasks
a.	Create a module "employee_status"
b.	This module should have a function that specify if an employee is a full-time or part-time ‘em_st’, and function to compute the bonus an employee deserves ‘bonus’
c.	Create a module with the name "status_test"
d.	Import the module "employee_status" in different ways and use the available functions
e.	Move the "employee_status" into a package of the name status, do the required corrections
f.	Create a new module inside status package, and give us some info about your package using a documentation string 
     module name "info"
"""
from status import employee_status
res = employee_status.em_st('ayham', 5)

from status.employee_status import bonus

res2 = bonus('tasneem', 5, 48000)

from status import info as i
print(help(i))
