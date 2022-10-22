# -*- coding: utf-8 -*-
"""
Assignment : 02
Q. A) Write a python program to swap two variables using and without using third variable.


@author: Aftab Mallick
"""
a,b=input("Enter two integers: ").split()
a=int(a)
b=int(b)
temp=a
a=b
b=temp
print("after swap: a=",a,"& b=",b)