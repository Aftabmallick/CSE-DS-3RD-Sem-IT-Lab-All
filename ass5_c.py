# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:42:56 2021

@author: Aftab Mallick
"""

n = int(input("Enter no of roww: "))
for i in range(n, 0, -1):
    for j in range(i): 
        print(chr(65+j), end ="")
    print(" "*(n-i)*2+"\b",end="")
    
    for j in range(i-1,-1,-1):
        print(chr(65+j),end ="")
    print("")