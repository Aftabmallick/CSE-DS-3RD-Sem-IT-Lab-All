# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:07:30 2021

@author: Aftab Mallick
"""
lst=[]
l=int(input("Enter len of list: "))
print("Enter elements: ")
for _ in range(l):
    x=int(input())
    lst.append(x)
n=int(input("Enter no of rotation: "))
d=input("Enter right/left: ")
if d=='right':
    n=len-n
l1=lst[0:n]
l2=lst[n:l]
new_lst=l2+l1
print(new_lst)
    
