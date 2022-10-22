# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:58:12 2021

@author: Aftab Mallick
"""

def tower(n,source,destination,space):
    if n>0:
        tower(n-1,source,space,destination)
        print("\nMove disk {} from source {} to destination {}".format(n,source,destination))
        tower(n-1,space,destination,source) 
n=int(input("Enter the no of disks: "))
print("\nThe sequence of moves involved in the Tower of Hanoi are:")
tower(n,'A','C','B')