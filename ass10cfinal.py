# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:04:20 2022

@author: Aftab Mallick
"""
file1=open("text3.txt","w")
n = int(input("Enter the nth value: "))
a = 0
b = 1
sum = 0
while(sum <= n):
     file1.write(str(sum)+"\n")
     a = b
     b = sum
     sum = a + b
file1.close()

file1=open("text3.txt","r")
print(file1.read())
file1.close()