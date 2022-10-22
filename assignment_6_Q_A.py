# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:06:28 2021

@author: Aftab Mallick
"""

l1=list()
n= int(input("Enter list size: "))
print("Enter ",n,"elements in list : ",end="")
for i in range (n):
    temp=int(input())
    l1.append(temp)
print("largest element is : ",max(l1),"\nSmallest element is: ",min(l1))
