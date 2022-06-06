"""
Required Functions
"""

def em_st(name, hours):
    if hours == 8:
        print(f'{name} is a full time employee')

    elif hours < 8:
        print(f'{name} is a part time employee')

    else:
        print(f'{name} is a full time employee with additional hours')


def bonus(name, experience, sallary):
    if experience > 5:
        bonos_val = 0.5 * sallary


    else:
        bonos_val = 0.2 * sallary

    print(f'{name} has {bonos_val} as a bonos')
