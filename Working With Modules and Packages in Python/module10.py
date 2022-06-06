""" Lecture: Working With Modules and Packages in Python

    Outlines:
    5- How to Import From a Python Package

"""
# 5- How to Import From a Python Package

import area.area_calc
area.area_calc.circle_area(5)

import area.area_calc as ac
ac.circle_area(5)

from area import area_calc
area_calc.circle_area(5)

from area import area_calc as ac
ac.circle_area(5)

from area import area_calc, dummy_module
area_calc.circle_area(5)

from area.area_calc import circle_area
circle_area(5)

from area.area_calc import circle_area as ca
ca(5)

