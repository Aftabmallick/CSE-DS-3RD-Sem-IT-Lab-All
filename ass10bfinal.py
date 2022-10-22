# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:12:37 2022

@author: Aftab Mallick
"""

file1=open("textprime.txt","w")
n=int(input("Enter no of prime no: "))
c=0
num=2
while c<n:
    for i in range(2,num):
        if (num%i)==0:
            break
    else:
        file1.write(str(num)+"  ")
        c=c+1
    num=num+1
file1.close()
file1=open("textprime.txt","r")
print(file1.read())
file1.close()