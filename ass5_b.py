# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:25:24 2021

@author: Aftab Mallick
"""
n=int(input("enter rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print("\n")