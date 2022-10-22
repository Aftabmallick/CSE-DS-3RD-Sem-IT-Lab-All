# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:26:30 2021

@author: Aftab Mallick
"""

rows = int(input("Enter the number of rows: "))
x = 2*rows - 2  
for i in range(1, rows+1):
    for j in range(1,rows):
        print(end=" ")  
    x = x - 2
    for k in range(1, i + 1):  
        print(k, end=' ')  
    print("")