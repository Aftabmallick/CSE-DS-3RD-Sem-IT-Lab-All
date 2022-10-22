# -*- coding: utf-8 -*-
"""
Assignment : 02
Q. B) Consider the basic pay of an employee as user input. AGP is 50% of thebasic pay. Company  provides 50% DA and 15% HRA on the merged basic. Write a python program to calculate and display total salary of the employee
@author: Aftab Mallick
"""

base=int(input("Enter Base salary  : "))
agp=base*.5
da=base*.5
hra=base*.15
t=base+agp+da+hra
print("Total salary = ",t)