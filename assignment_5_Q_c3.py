# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:39:40 2021

@author: Aftab Mallick
"""

n = int(input("Enter no of roww: "))
z=64
#Upper Traingles
for i in range(n, 0, -1):
    #Top Left Triangle
    for j in range(1, i+1): 
        z+=j
        print(chr(z), end =" ")
        z=64
        
        

    #Space between top triangles
    for j in range(n-i):
        print(" ",end=" ")

    #Top Right Triangle
    for j in range(n-1, 0, -1):
        if(i < j):
            print(" ",end=" ")
        else:
            z+=j
            print(chr(z), end =" ") 
            z=64
    print("\n", end="")