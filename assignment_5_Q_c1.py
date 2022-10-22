# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:17:39 2021

@author: Aftab Mallick
"""
#diamond pattern
n = int(input("ENter no of rows : "))
for i in range(1, (n+1)//2 + 1): #1to (n+1)/2
    for j in range((n+1)//2 - i):
        print(" ", end = " ")
    for k in range((i*2)-1):
        print("*", end = " ")
    print()

for i in range((n+1)//2 + 1, n + 1):#(n+1)/2 + 1 to n
    for j in range(i - (n+1)//2):
        print(" ", end = " ")
    for k in range((n+1 - i)*2 - 1):
        print("*", end = " ")
    print()