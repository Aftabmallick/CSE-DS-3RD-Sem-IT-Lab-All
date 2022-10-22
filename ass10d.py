# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:21:30 2022

@author: Aftab Mallick
"""
##Ass 10 D
file1=open("AIML Basic Projects.txt","r")
lines=file1.readlines()
for line in lines:
    print(line,end="")
file1.close()