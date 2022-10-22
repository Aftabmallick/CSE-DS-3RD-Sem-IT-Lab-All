# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:15:08 2021

@author: Aftab Mallick
"""
"""
An Electric Power Distribution Company charges its domestic consumers as follows:
Consumption Unit Rate of Charge
0 – 200 Rs 0.50 per unit
201 – 400 Rs 100 + Rs 0.65 per unit
401 – 600 Rs 200 + Rs 0.80 per unit
Above 600 Rs 300 + Rs 1.00 per unit
Write a python program which will accept number of units from the consumer and display the amount to be paid.

"""
u=int(input("Enter no of unit: "))
if u>=0 and u<=200:
    bill =u*.50
elif u>=201 and u<=400:
    bill =100 +u*.65
elif u>=401 and u<=600:
    bill= 200+u*.80
else:
    bill=300 +u*1
print("Your bill is : {}".format(bill))