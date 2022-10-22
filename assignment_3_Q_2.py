# -*- coding: utf-8 -*-
"""
Assingment : 03
Q. 2) Write a python program to check whether a year is Leap Year.
@author: Aftab Mallick
"""

year=int(input("Enter Year: "))
if(year%400 == 0):
    print(year,"is a leap year")
elif(year%4==0 and year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")