# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:59:55 2021

@author: Aftab Mallick
"""
#special no
import math as m
print("Special  no are = ")
for i in range(1,500):
    t=i
    sum=0
    while(t>=1):
        rem=t%10
        sum+=m.factorial(rem)
        t=(t//10)
    if sum==i:
        print(i,)
    

        