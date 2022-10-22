# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:22:18 2021

@author: Aftab Mallick
"""
#Write a python code to generate Fibonacci series up to n terms using loop.
n = int(input("Enter terms:  "))
n1= 0
n2=1
count = 0
if n <= 0:
   print("enter positive no")
elif n == 1:
   print("Fibonacci sequence :")
   print(n1,end=" ")
else:
   print("Fibonacci sequence :")
   while count < n:
       print(n1,end=" ")
       nd = n1 + n2
       n1 = n2
       n2 = nd
       count += 1
    