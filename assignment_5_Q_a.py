# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:42:34 2021

@author: Aftab Mallick
"""
#two digit automorphic no
print("Automorphic nos are :")
for i in range(10,100):
    sq=(i**2)
    if (i)==(sq%100):
        print(i,end=" ")